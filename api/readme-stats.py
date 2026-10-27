"""Public SVG endpoints; reads existing counters without incrementing Hits."""
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler
import json
from pathlib import Path
import sys
import threading
import time
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.update_readme_stats import console, fetch_download_counts, fetch_views

TTL = 900
_cache = {}
_locks = {'downloads': threading.Lock(), 'views': threading.Lock()}
SNAPSHOT = json.loads((ROOT / 'docs/images/stats/counts.json').read_text())


def fetch_metric(metric):
    if metric == 'views':
        return fetch_views()
    current, historical = fetch_download_counts()
    return current + historical


def response(path):
    url = urlsplit(path)
    routes = {'/downloads.svg': 'downloads', '/views.svg': 'views'}
    metric = routes.get(url.path)
    if url.path == '/api/readme-stats':
        metric = parse_qs(url.query).get('metric', [''])[0]
    if metric not in _locks:
        return 404, {'Content-Type': 'text/plain; charset=utf-8', 'Cache-Control': 'no-store'}, 'Not found'

    # CDN handles most requests; warm-process caching avoids duplicate API reads.
    with _locks[metric]:
        now = time.time()
        cached = _cache.get(metric)
        offline = False
        if not cached or now - cached[0] >= TTL:
            try:
                value = fetch_metric(metric)
                if not isinstance(value, int) or isinstance(value, bool) or value < 0:
                    raise ValueError('Invalid counter')
                cached = (time.time(), value, datetime.now(timezone.utc).isoformat(timespec='seconds'))
                _cache[metric] = cached
            except Exception as error:
                print(f'{metric} source unavailable: {type(error).__name__}', file=sys.stderr)
                offline = True
                if cached is None:
                    cached = (0, SNAPSHOT[metric], SNAPSHOT['updated_at'])
        source = 'snapshot' if offline else 'live'
        # Limit downstream freshness to the remaining lifetime of the fetched data.
        remaining = 60 if offline else max(1, int(TTL - (time.time() - cached[0])))

    label, subtitle = ('下载次数', 'INCLUDING ARCHIVED APK') if metric == 'downloads' else ('访问次数', 'SINCE 2026.10.25')
    svg = console(label, cached[1], subtitle)
    svg = svg.replace('每15分钟尝试刷新', '访问时生成，缓存约15分钟')
    stamp = cached[2].replace('T', ' ')[:16] + ' UTC'
    text = ('OFFLINE · LAST VERIFIED ' if offline else 'UPDATED ') + stamp
    svg = svg.replace('</svg>', f'<text x="190" y="193" text-anchor="middle" fill="#8d9ac5" font-family="monospace" font-size="5.5">{text}</text></svg>')
    return 200, {
        'Content-Type': 'image/svg+xml; charset=utf-8',
        'Cache-Control': f'public, max-age={min(remaining, 300)}',
        'Vercel-CDN-Cache-Control': f'public, max-age={remaining}',
        'CDN-Cache-Control': f'public, max-age={remaining}',
        'X-Stats-Source': source,
        'X-Stats-Value': str(cached[1]),
        'X-Stats-Updated-At': cached[2],
        'X-Content-Type-Options': 'nosniff',
    }, svg


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self._respond(False)

    def do_HEAD(self):
        self._respond(True)

    def _respond(self, head):
        status, headers, body = response(self.path)
        data = body.encode('utf-8')
        self.send_response(status)
        for name, value in headers.items():
            self.send_header(name, value)
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        if not head:
            self.wfile.write(data)
