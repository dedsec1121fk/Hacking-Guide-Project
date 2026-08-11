#!/usr/bin/env python3
"""Strict static quality audit for Hacking Guide Project.

Standard-library only. It checks source Markdown, Python, JSON, stale branding,
unsafe legacy patterns, formatting, code fences, heading hierarchy, and links.
"""
from __future__ import annotations

import ast
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {'.md', '.py', '.json', '.txt'}
LEGACY_PATTERNS = {
    'legacy CEH material': re.compile(r'\bCEH(?:-v\d+)?\b|EC-Council|Samsar4|Ethical-Hacking-Labs', re.I),
    'public legacy target': re.compile(r'hackthissite\.org|\bnsa\.gov\b', re.I),
    'anti-forensics history clearing': re.compile(r'HISTSIZE\s*=\s*0|\bhistory\s+-c\b|Clear-History', re.I),
    'anti-forensics audit/log clearing': re.compile(r'auditpol\s+/clear|\bclearev\b|sed\s+-i[^\n]*(?:/var/log|auth\.log)', re.I),
    'packet flood command': re.compile(r'--flood\b', re.I),
    'netcat command execution': re.compile(r'\bnc\b[^\n`]*\s-e(?:\s|$)', re.I),
    'credential dumping command': re.compile(r'Invoke-Mimikatz|sekurlsa::|lsadump::', re.I),
    'metadata credential fetch': re.compile(r'(?:curl|wget)[^\n`]*169\.254\.169\.254', re.I),
    'encoded PowerShell': re.compile(r'powershell(?:\.exe)?[^\n`]*(?:-enc|-encodedcommand)\b', re.I),
    'shell over socat': re.compile(r'\bsocat\b[^\n`]*(?:EXEC|SYSTEM):', re.I),
    'operational detection evasion': re.compile(r'\bevade\s+(?:ids|ips|detection)\b|\bbypass\s+(?:ids|ips)\b|\bcovering\s+tracks\b', re.I),
}
OLD_NAME = re.compile(('Hacking'+r'\s+'+'101')+'|'+('hacking'+'101'), re.I)
REMOTE_IMAGE = re.compile(r'!\[[^\]]*\]\(https?://|<img\b[^>]*\bsrc=["\']https?://', re.I)
MODULE_CLI = re.compile(r'python(?:3)?\s+["\']Hacking Guide Project\.py["\']\s+--(?:search|path|language|module|list|stats|doctor|categories|labs)\b', re.I)
LINK_RX = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
FENCE_RX = re.compile(r'^\s*(`{3,}|~{3,})')
HEADING_RX = re.compile(r'^(#{1,6})\s+\S')


def source_markdown(root: Path):
    for lang in ('English', 'Greek'):
        base = root / lang
        if not base.exists():
            continue
        for p in base.rglob('*.md'):
            if 'Combined' not in p.parts:
                yield p


def all_text_files(root: Path, include_generated: bool):
    for p in root.rglob('*'):
        if not p.is_file() or p.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        if not include_generated and 'Combined' in p.parts:
            continue
        yield p


def markdown_structure_issues(p: Path, text: str):
    issues=[]
    is_numbered = bool(re.match(r'^\d+-', p.name))
    h1_count = 0
    in_fence=False
    fence_char=None
    prev_level=None
    fence_start=None
    for ln,line in enumerate(text.splitlines(),1):
        if line.rstrip() != line:
            issues.append(f'{p.relative_to(ROOT)}:{ln}: trailing whitespace')
        fm=FENCE_RX.match(line)
        if fm:
            char=fm.group(1)[0]
            if not in_fence:
                in_fence=True; fence_char=char; fence_start=ln
            elif char==fence_char:
                in_fence=False; fence_char=None; fence_start=None
            continue
        if in_fence:
            continue
        hm=HEADING_RX.match(line)
        if hm:
            level=len(hm.group(1))
            if level==1: h1_count += 1
            if prev_level is not None and level > prev_level + 1:
                issues.append(f'{p.relative_to(ROOT)}:{ln}: heading jumps H{prev_level} -> H{level}')
            prev_level=level
    if in_fence:
        issues.append(f'{p.relative_to(ROOT)}:{fence_start}: unclosed Markdown code fence')
    if is_numbered and h1_count != 1:
        issues.append(f'{p.relative_to(ROOT)}: expected exactly one H1, found {h1_count}')
    if '\ufffd' in text:
        issues.append(f'{p.relative_to(ROOT)}: Unicode replacement character present')
    if '\x00' in text:
        issues.append(f'{p.relative_to(ROOT)}: NUL byte present')
    if REMOTE_IMAGE.search(text):
        issues.append(f'{p.relative_to(ROOT)}: remote image embed found; keep the guide offline/self-contained')
    if is_numbered and MODULE_CLI.search(text):
        issues.append(f'{p.relative_to(ROOT)}: normal lesson still requires CLI flags instead of menu navigation')

    # Repeated long prose within a single file usually indicates accidental template duplication.
    paras=Counter()
    for para in re.split(r'\n\s*\n', text):
        norm=' '.join(para.split())
        if len(norm) >= 220 and not norm.startswith(('#','```','~~~')):
            paras[norm] += 1
    for para,count in paras.items():
        if count > 1:
            issues.append(f'{p.relative_to(ROOT)}: repeated long paragraph x{count}: {para[:90]}...')
    return issues


def link_issues(root: Path, p: Path, text: str):
    issues=[]
    for target in LINK_RX.findall(text):
        target=target.strip().strip('<>')
        if not target or target.startswith(('http://','https://','#','mailto:','tel:')):
            continue
        clean=unquote(target.split('#',1)[0])
        if clean and not (p.parent / clean).resolve().exists():
            issues.append(f'{p.relative_to(root)}: broken relative link -> {target}')
    return issues


def audit_project(root: Path = ROOT, include_generated: bool = False):
    issues=[]
    if not (root / 'LICENSE.md').is_file():
        issues.append('LICENSE.md: required project license is missing')
    if not (root / '.github' / 'SECURITY.md').is_file():
        issues.append('.github/SECURITY.md: required security policy is missing')
    # Source Markdown gets the strict line-by-line checks.
    for p in source_markdown(root):
        text=p.read_text(encoding='utf-8', errors='replace')
        issues.extend(markdown_structure_issues(p,text))
        issues.extend(link_issues(root,p,text))

    # User-facing/source text must not regress to old branding or legacy unsafe material.
    for p in all_text_files(root, include_generated):
        try: text=p.read_text(encoding='utf-8',errors='replace')
        except OSError: continue
        if OLD_NAME.search(text):
            issues.append(f'{p.relative_to(root)}: old project name remains')
        if p.suffix.lower()=='.md':
            for label,rx in LEGACY_PATTERNS.items():
                if rx.search(text): issues.append(f'{p.relative_to(root)}: {label}')

    # Python and JSON must parse.
    for p in root.rglob('*.py'):
        try: ast.parse(p.read_text(encoding='utf-8'))
        except (SyntaxError,UnicodeError) as exc: issues.append(f'{p.relative_to(root)}: Python parse error: {exc}')
    for p in root.rglob('*.json'):
        try: json.loads(p.read_text(encoding='utf-8'))
        except (json.JSONDecodeError,UnicodeError) as exc: issues.append(f'{p.relative_to(root)}: JSON parse error: {exc}')

    # Build/runtime junk should never ship.
    for p in root.rglob('*'):
        if p.name=='__pycache__' or p.suffix=='.pyc':
            issues.append(f'{p.relative_to(root)}: generated Python cache must not ship')
    return sorted(set(issues))


def main():
    include_generated='--include-generated' in sys.argv[1:]
    issues=audit_project(ROOT,include_generated=include_generated)
    if issues:
        print(f'FAILED: {len(issues)} quality issue(s)')
        for x in issues: print('ERROR:',x)
        return 1
    print('OK: strict line-by-line quality audit passed.')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
