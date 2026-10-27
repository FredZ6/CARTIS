import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('stats_api', Path(__file__).resolve().parents[1] / 'api/readme-stats.py')
api = importlib.util.module_from_spec(spec)
spec.loader.exec_module(api)

class StatsAPITest(unittest.TestCase):
    def setUp(self):
        api._cache.clear()

    def test_live_svg_and_15_minute_cache(self):
        with patch.object(api, 'fetch_metric', return_value=145) as fetch, patch.object(api.time, 'time', return_value=1000):
            status, headers, body = api.response('/downloads.svg')
            self.assertEqual(status, 200)
            self.assertIn('下载次数：145', body)
            self.assertEqual(headers['X-Stats-Source'], 'live')
            self.assertIn('max-age=900', headers['Vercel-CDN-Cache-Control'])
            api.response('/downloads.svg')
            self.assertEqual(fetch.call_count, 1)

    def test_expired_cache_reads_new_data(self):
        api._cache['views'] = (1000, 164, '2026-10-27T15:00:00+00:00')
        with patch.object(api.time,'time',return_value=1901), patch.object(api,'fetch_metric',return_value=170) as fetch:
            status, headers, body = api.response('/views.svg')
            self.assertIn('访问次数：170', body)
            fetch.assert_called_once_with('views')

    def test_failure_labels_snapshot_and_short_cache(self):
        with patch.object(api,'fetch_metric',side_effect=TimeoutError):
            status, headers, body = api.response('/views.svg')
            self.assertEqual(status,200)
            self.assertEqual(headers['X-Stats-Source'],'snapshot')
            self.assertIn('OFFLINE', body)
            self.assertIn('max-age=60', headers['Vercel-CDN-Cache-Control'])

    def test_invalid_route_does_not_call_sources(self):
        with patch.object(api,'fetch_metric') as fetch:
            self.assertEqual(api.response('/unknown.svg')[0],404)
            self.assertEqual(api.response('/api/readme-stats?metric=invalid')[0],404)
            fetch.assert_not_called()

    def test_head_uses_get_headers(self):
        with patch.object(api,'fetch_metric',return_value=167):
            status, headers, body = api.response('/views.svg')
            self.assertEqual(headers['Content-Type'],'image/svg+xml; charset=utf-8')
            self.assertGreater(len(body),1000)

if __name__ == '__main__':
    unittest.main()
