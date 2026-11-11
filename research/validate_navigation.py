#!/usr/bin/env python3
"""Validate Mathlab agent entry links and route references; stdlib only."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / 'docs/research/RESEARCH-MAP.json'
DOCS = [ROOT / name for name in ('README.md','AGENTS.md','docs/RESEARCH-INDEX.md')]
LINKS = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')

def main():
    x = json.loads(MAP.read_text(encoding='utf-8'))
    errors = []
    if x.get('schema_version') != '1.0.0': errors.append('Unknown map version')
    ids = [n['id'] for n in x['nodes']]
    if len(ids) != len(set(ids)) or not ids: errors.append('Duplicate or missing node IDs')
    for n in x['nodes']:
        for field in ('entry_path','status_authority'):
            if not (ROOT / n[field]).is_file(): errors.append(f"{n['id']}: missing {field} {n[field]}")
        if not n.get('topic_tags'): errors.append(f"{n['id']}: no topic_tags")
        if any(field in n for field in ('status','ci','head')): errors.append(f"{n['id']}: stores live state")
    for e in x['edges']:
        if e['from'] not in ids or e['to'] not in ids or e['type'] != 'navigation_related': errors.append(f'Invalid graph edge: {e}')
    for doc in DOCS:
        for link in LINKS.findall(doc.read_text(encoding='utf-8')):
            s = urlsplit(link)
            if s.scheme or s.netloc or link.startswith('#') or not s.path: continue
            if not (doc.parent / unquote(s.path)).exists(): errors.append(f'{doc.relative_to(ROOT)}: broken {link}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        raise SystemExit(1)
    print(f"Navigation OK: {len(ids)} nodes, {len(x['edges'])} topic links")

if __name__ == '__main__': main()
