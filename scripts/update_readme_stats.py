"""Render GBA README statistics; no third-party Python dependencies."""
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/images/stats'
DIGITS = {'0':['111','101','101','101','111'],'1':['010','110','010','010','111'],'2':['111','001','111','100','111'],'3':['111','001','111','001','111'],'4':['101','101','111','001','001'],'5':['111','100','111','001','111'],'6':['111','100','111','101','111'],'7':['111','001','010','010','010'],'8':['111','101','111','101','111'],'9':['111','101','111','001','111']}

def get_json(url, github=False):
    headers = {'User-Agent': 'CARTIS-readme-stats', 'Accept': 'application/json'}
    if github and os.getenv('GITHUB_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GITHUB_TOKEN']
    with urlopen(Request(url, headers=headers), timeout=30) as response:
        return json.load(response)

def fetch_counts():
    total, page = 0, 1
    existing_ids = set()
    while True:
        releases = get_json(f'https://api.github.com/repos/FredZ6/CARTIS/releases?per_page=100&page={page}', True)
        for release in releases:
            if not release['draft']:
                total += sum(asset['download_count'] for asset in release['assets'])
                existing_ids.update(asset['id'] for asset in release['assets'])
        if len(releases) < 100:
            break
        page += 1
    views = get_json('https://hits.sh/api/urns/github.com/FredZ6/kpb-socket/')['total']
    if not isinstance(views, int) or views < 0:
        raise ValueError('Invalid Hits total')
    history = json.loads((OUT / 'historical-downloads.json').read_text())
    historical = sum(asset['downloads'] for asset in history['assets'] if asset['id'] not in existing_ids)
    return {'downloads': total + historical, 'views': views, 'historical_downloads': historical, 'current_asset_downloads': total}

def pixel_number(number):
    value = str(number)
    unit = min(6, 126 / max(1, len(value)*4-1))
    left = 190 - (len(value)*4-1)*unit/2
    return ''.join(f'<rect x="{left+(i*4+x)*unit:g}" y="{105+y*unit:g}" width="{unit:g}" height="{unit:g}"/>' for i, digit in enumerate(value) for y, row in enumerate(DIGITS[digit]) for x, bit in enumerate(row) if bit == '1')

def console(label, number, subtitle):
    download = subtitle == 'INCLUDING ARCHIVED APK'
    shell, light, shade = ('#6536dc', '#b48bff', '#35147d') if download else ('#1647c7', '#68caff', '#102b7e')
    stars = ''
    for i in range(38):
        x, y = (i*83+17)%372+4, (i*47+11)%214+4
        color = ['#16339a','#5939cc','#3a8fff','#bb88ff'][i%4]
        stars += f'<rect x="{x}" y="{y}" width="3" height="3" fill="{color}"/>'
    for x,y in [(34,30),(334,36),(24,186),(350,181),(298,204)]:
        stars += f'<path d="M{x-6} {y-2}h4v-4h4v4h4v4h-4v4h-4v-4h-4Z" fill="#ffe7a0"/>'
    # Layered, stepped orbital ribbons match the cover's hard-edged nebulae.
    orbit = ''
    for offset, color in [(0,'#0b1b67'),(5,'#172caa'),(10,'#3449e3'),(15,'#7041db'),(20,'#a675ed')]:
        orbit += f'<path d="M8 {84+offset}h12v-12h20v-12h32v-10h48v-8h62v-6h64v8h48v10h36v12h24v12h18" fill="none" stroke="{color}" stroke-width="5"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="380" height="222" viewBox="0 0 380 222" role="img" aria-labelledby="title desc" shape-rendering="crispEdges">
<title id="title">{escape(label)}：{number}</title><desc id="desc">深蓝星空像素 GBA，奶黄色数字，每小时自动刷新</desc>
<path d="M8 0H372V8H380V214H372V222H8V214H0V8H8Z" fill="#030620"/>
<path d="M8 1H372V8H379V214H372V221H8V214H1V8H8Z" fill="none" stroke="#17215c" stroke-width="2"/>
{stars}{orbit}
<path d="M20 156h16v12h32v12h52v8h64v8h72v-8h48v-8h32v-12h24" fill="none" stroke="#152b93" stroke-width="6"/>
<path d="M34 162h16v12h32v12h52v8h64v8h56" fill="none" stroke="#6437c7" stroke-width="4"/>
<path d="M50 62H78V50H302V62H330V72H350V84H362V158H350V170H330V182H50V170H30V158H18V84H30V72H50Z" fill="#010314"/>
<path d="M50 66H82V54H298V66H330V76H346V88H358V154H346V166H326V178H54V166H34V154H22V88H34V76H50Z" fill="{shade}"/>
<path d="M50 66H82V54H298V66H330V76H346V88H354V146H342V158H322V170H58V158H38V146H26V88H38V76H50Z" fill="{shell}"/>
<path d="M50 66H82V54H298V66H330V76H342V84" fill="none" stroke="{light}" stroke-width="4"/>
<path d="M38 146v8h20v12h264v-12h20v-8" fill="none" stroke="#24115e" stroke-width="4"/>
<path d="M86 62H294V70H302V158H294V166H86V158H78V70H86Z" fill="#070921"/>
<path d="M90 70H290V74H294V150H290V154H90V150H86V74H90Z" fill="#151947"/>
<rect x="102" y="78" width="176" height="70" fill="#070d36"/>
<path d="M104 80H276V84H108V146H104Z" fill="#243a89"/>
<path d="M110 126H270M110 134H270M110 142H270" stroke="#111e51" stroke-width="1"/>
<text x="190" y="96" text-anchor="middle" fill="#a8cfff" font-family="sans-serif" font-size="11" font-weight="bold" letter-spacing="3">{escape(label)}</text>
<g fill="#ffe9a8">{pixel_number(number)}</g>
<text x="190" y="160" text-anchor="middle" fill="#9a9ddd" font-family="monospace" font-size="5.5" font-weight="bold" letter-spacing="2">CARTIS ADVANCE</text>
<path d="M42 94H54V106H66V118H54V130H42V118H30V106H42Z" fill="#080b29"/>
<path d="M44 96H52V108H64V110H50V98H44Z" fill="#bfc9ff"/>
<path d="M44 110H50V116H44Z" fill="#5865a6"/>
<path d="M310 109H322V113H326V125H322V129H310V125H306V113H310Z M336 91H348V95H352V107H348V111H336V107H332V95H336Z" fill="#080b29"/>
<path d="M311 112H321V122H311Z M337 94H347V104H337Z" fill="#f0ddff"/>
<path d="M317 112H321V122H317Z M343 94H347V104H343Z" fill="#b491f4"/>
<rect x="310" y="78" width="4" height="4" fill="#ffe7a0"/>
<path d="M46 144h12v4H46Z M48 154h12v4H48Z" fill="#c9b8ff"/>
<path d="M310 144h4v4h4v4h-4v-4h-4Z M320 140h4v4h4v4h-4v-4h-4Z M330 136h4v4h4v4h-4v-4h-4Z" fill="#080b29"/>
<text x="190" y="24" text-anchor="middle" fill="#d7dfff" font-family="monospace" font-size="7" letter-spacing="3">C A R T I S · S T A T S</text>
<text x="190" y="210" text-anchor="middle" fill="#a8a3ec" font-family="monospace" font-size="6" letter-spacing="1.5">{('DOWNLOADS · ARCHIVE + LIVE' if download else 'README VIEWS · SINCE 2026.10.25')}</text>
</svg>'''

def main():
    counts = fetch_counts()  # Fetch both before changing files.
    OUT.mkdir(parents=True, exist_ok=True)
    for key, label, subtitle in [('downloads','下载次数','INCLUDING ARCHIVED APK'), ('views','访问次数','SINCE 2026.10.25')]:
        (OUT / f'gba-{key}.svg').write_text(console(label, counts[key], subtitle), encoding='utf-8')
    (OUT / 'counts.json').write_text(json.dumps(counts, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(counts))

if __name__ == '__main__':
    main()
