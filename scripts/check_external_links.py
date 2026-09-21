#!/usr/bin/env python3
"""Check registered community URLs and official media without downloading files."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def targets():
    found = {}
    def add(url, kind, source):
        row = found.setdefault(url, {'url': url, 'kind': kind, 'sources': []})
        if source not in row['sources']:
            row['sources'].append(source)
    for e in json.loads((ROOT / 'data/community-sources.json').read_text())['entries']:
        for field, kind in [('source_url', 'page'), ('prompt_url', 'page'),
                            ('video_url', 'video'), ('thumbnail_url', 'image')]:
            add(e[field], kind, e['id'])
    body = (ROOT / 'docs/official-h3-examples.md').read_text()
    for url in re.findall(r'https://[^\s<>\)"\]]+', body):
        if re.search(r'\.(mp4|webm|gif|png|jpg|webp)(?:\?|$)', url, re.I):
            kind = 'video' if re.search(r'\.(mp4|webm)', url) else 'image'
            if url.startswith('https://github.com/') and '/blob/' in url:
                kind = 'page'
            add(url, kind, 'official-h3-examples')
    for url in ['https://flyne.ai/model/minimax-h3/', 'https://flyne.ai/free-minimax-h3/']:
        add(url, 'page', 'Flyne entry')
    return list(found.values())


def classify(status, content_type, kind):
    if status in (401, 403, 429):
        return 'restricted'
    if status in (404, 410):
        return 'unavailable'
    if status >= 500 or status in (408, 425):
        return 'temporary-error'
    if 200 <= status < 300:
        if kind in ('image', 'video') and not content_type.lower().startswith(kind + '/'):
            return 'unexpected-content'
        return 'reachable'
    return 'needs-review'


def request(url, method, timeout):
    headers = {'User-Agent': 'FlyneGuide-LinkCheck/1.0 (public repository maintenance)'}
    if method == 'GET':
        headers['Range'] = 'bytes=0-0'
    req = urllib.request.Request(url, headers=headers, method=method)
    try:
        # Inspect headers only; close without reading response bodies.
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status, response.headers.get('Content-Type', ''), response.geturl()
    except urllib.error.HTTPError as exc:
        try:
            return exc.code, exc.headers.get('Content-Type', ''), exc.geturl()
        finally:
            exc.close()


def check(target, timeout=12):
    try:
        status, ctype, final = request(target['url'], 'HEAD', timeout)
        method = 'HEAD'
        # Some CDNs reject HEAD. Confirm missing responses before flagging them.
        if status in (400, 403, 404, 405, 410, 501):
            status, ctype, final = request(target['url'], 'GET', timeout)
            method = 'GET headers only'
        return dict(target, status=classify(status, ctype, target['kind']),
                    http_status=status, content_type=ctype, final_url=final, method=method)
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return dict(target, status='network-error', error=str(exc))


def markdown(report):
    rows = report['results']
    counts = {status: sum(r['status'] == status for r in rows) for status in sorted({r['status'] for r in rows})}
    lines = ['# External link check / 外链检查', '', report['checked_at'], '',
             ', '.join(f'{key}: {value}' for key, value in counts.items()), '',
             'Header reachability only. It does not prove playback, prompt completeness or model identity.', '',
             'restricted = 访问受限或限流，不表示已删除。unavailable = 本次返回 404/410，需人工复核。网络错误不表示永久失效。', '',
             '| Source | Type | Status | HTTP | URL |', '|---|---|---|---|---|']
    for r in rows:
        lines.append(f"| {', '.join(r['sources'])} | {r['kind']} | {r['status']} | {r.get('http_status', '—')} | [link]({r['url']}) |")
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(check, targets()))
    report = {'checked_at': datetime.now(timezone.utc).isoformat(), 'results': rows}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / 'links.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    (args.output_dir / 'links.md').write_text(markdown(report))
    for status in sorted({r['status'] for r in rows}):
        print(f"{status}: {sum(r['status'] == status for r in rows)}")
    if any(r['status'] in ('unavailable', 'unexpected-content') for r in rows):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
