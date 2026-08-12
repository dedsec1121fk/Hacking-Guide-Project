#!/usr/bin/env python3
"""Validate bilingual/category structure and rebuild combined Hacking Guide Project editions."""
from __future__ import annotations
import argparse, ast, html, json, re, shutil, subprocess, sys
sys.dont_write_bytecode = True
from pathlib import Path
from urllib.parse import unquote
from quality_audit import audit_project
ROOT=Path(__file__).resolve().parents[1]
LANGS={'en':'English','gr':'Greek'}
LAUNCHER='Hacking Guide Project.py'
CATEGORY_LABELS={
 'en':{
  '01-Fundamentals-and-Methodology':'Fundamentals & Methodology','02-Recon-Pentesting-Web-and-AppSec':'Recon, Pentesting, Web & AppSec','03-Systems-Malware-and-Reverse-Engineering':'Systems, Malware & Reverse Engineering','04-Network-Wireless-and-Internet':'Networks, Wireless & Internet','05-Mobile-IoT-and-Hardware':'Mobile, IoT & Hardware','06-Identity-Cryptography-and-Trust':'Identity, Cryptography & Trust','07-Cloud-Containers-and-Supply-Chain':'Cloud, Containers & Supply Chain','08-Blue-Team-IR-Forensics-and-Resilience':'Blue Team, IR & Forensics','09-AI-GRC-Privacy-Data-and-Human-Security':'AI, GRC, Privacy & Human Security','10-Termux-and-Security-Automation':'Termux & Security Automation','11-Labs-Capstones-and-Career':'Labs, Capstones & Career'},
 'gr':{
  '01-Fundamentals-and-Methodology':'Βάσεις & Μεθοδολογία','02-Recon-Pentesting-Web-and-AppSec':'Recon, Pentesting, Web & AppSec','03-Systems-Malware-and-Reverse-Engineering':'Συστήματα, Malware & Reverse Engineering','04-Network-Wireless-and-Internet':'Δίκτυα, Ασύρματα & Internet','05-Mobile-IoT-and-Hardware':'Κινητά, IoT & Hardware','06-Identity-Cryptography-and-Trust':'Ταυτότητα, Κρυπτογραφία & Trust','07-Cloud-Containers-and-Supply-Chain':'Cloud, Containers & Supply Chain','08-Blue-Team-IR-Forensics-and-Resilience':'Blue Team, IR & Forensics','09-AI-GRC-Privacy-Data-and-Human-Security':'AI, GRC, Ιδιωτικότητα & Human Security','10-Termux-and-Security-Automation':'Termux & Αυτοματοποίηση Ασφάλειας','11-Labs-Capstones-and-Career':'Labs, Capstones & Καριέρα'}}
GUIDES=['README.md','Guides/START-HERE.md','Guides/STUDY-METHOD.md','Guides/LAB-GUIDE.md','Guides/TERMUX-QUICKSTART.md','Guides/REFERENCE-CHEATSHEET.md','Guides/ADVANCED-TRACK.md']
HIGH_RISK={
 'packet-flood command':re.compile(r'--flood\b',re.I),
 'netcat command-execution mode':re.compile(r'\bnc\b[^\n`]*\s-e(?:\s|$)',re.I),
 'meterpreter log-clearing':re.compile(r'\bclearev\b',re.I),
 'shell-history clearing':re.compile(r'\bhistory\s+-c\b',re.I),
 'credential-dumping command':re.compile(r'(?:Invoke-Mimikatz|sekurlsa::|lsadump::)',re.I),
 'metadata credential fetch':re.compile(r'(?:curl|wget)[^\n`]*169\.254\.169\.254',re.I),
 'encoded powershell':re.compile(r'powershell(?:\.exe)?[^\n`]*(?:-enc|-encodedcommand)\b',re.I),
 'shell over socat':re.compile(r'\bsocat\b[^\n`]*(?:EXEC|SYSTEM):',re.I),
}

def manifest(): return json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
def module_numbers(m): return sorted(map(int,m.get('modules',{})))
def expected_numbers(m):
 nums=module_numbers(m)
 return list(range(1,max(nums)+1)) if nums else []
def module_path(m,lang,n):
 meta=m['modules'][str(n)]; return ROOT/LANGS[lang]/meta['category']/meta['filename']
def modules(m,lang): return [(n,module_path(m,lang,n)) for n in module_numbers(m)]
def heading(p):
 for line in p.read_text(encoding='utf-8',errors='replace').splitlines():
  if line.startswith('# '): return re.sub(r'<[^>]+>','',line[2:]).strip()
 return p.stem

def validate_links(errors):
 rx=re.compile(r'\[[^\]]+\]\(([^)]+)\)')
 for p in ROOT.rglob('*.md'):
  for target in rx.findall(p.read_text(encoding='utf-8',errors='replace')):
   if target.startswith(('http://','https://','#','mailto:')): continue
   clean=unquote(target.split('#',1)[0])
   if clean and not (p.parent/clean).resolve().exists(): errors.append(f'Broken link: {p.relative_to(ROOT)} -> {target}')

def validate():
 e=[]
 if not (ROOT/'manifest.json').exists(): return ['Missing manifest.json']
 if not (ROOT/'LICENSE.md').exists(): e.append('Missing LICENSE.md')
 if not (ROOT/'.github'/'SECURITY.md').exists(): e.append('Missing .github/SECURITY.md')
 m=manifest(); expected=expected_numbers(m); total=len(expected)
 if module_numbers(m)!=expected: e.append(f'manifest.json modules must be continuous 1..{max(expected) if expected else 0}')
 if list(ROOT.glob('[0-9]*.md')): e.append('Numbered Markdown modules must not be stored in repository root')
 root_mds=[p.name for p in ROOT.glob('*.md')]
 if sorted(root_mds)!=['LICENSE.md','README.md']: e.append(f'Root Markdown should contain README.md and LICENSE.md only; found {root_mds}')
 cats=[x['id'] for x in m.get('categories',[])]
 seen_cat=[]
 for cat in m.get('categories',[]): seen_cat.extend(cat.get('modules',[]))
 if sorted(seen_cat)!=expected: e.append('Each module must appear exactly once across manifest categories')
 for lang,dirname in LANGS.items():
  base=ROOT/dirname
  if not base.is_dir(): e.append(f'Missing language directory: {dirname}'); continue
  for rel in GUIDES:
   if not (base/rel).exists(): e.append(f'Missing {dirname}/{rel}')
  for cat in cats:
   if not (base/cat).is_dir(): e.append(f'Missing category {dirname}/{cat}')
   if not (base/cat/'README.md').exists(): e.append(f'Missing category index {dirname}/{cat}/README.md')
  found=[]
  for n,p in modules(m,lang):
   if not p.exists(): e.append(f'Missing {lang} module {n}: {p.relative_to(ROOT)}'); continue
   found.append(n); text=p.read_text(encoding='utf-8',errors='replace')
   if lang=='en' and '## Guided study workflow' not in text: e.append(f'English module {n} missing guided workflow')
   if lang=='gr':
    if '## Καθοδηγούμενο εργαστήριο' not in text: e.append(f'Greek module {n} missing guided lab')
    if not re.search(r'[Α-Ωα-ωάέήίόύώϊϋΐΰ]',text): e.append(f'Greek module {n} has no Greek text')
   for label,rx in HIGH_RISK.items():
    if rx.search(text): e.append(f'High-risk legacy pattern ({label}) in {p.relative_to(ROOT)}')
  if found!=expected: e.append(f'{lang} numbering/parity failure')
 launcher=ROOT/LAUNCHER
 if not launcher.exists(): e.append(f'Missing {LAUNCHER}')
 else:
  try: ast.parse(launcher.read_text(encoding='utf-8'))
  except SyntaxError as x: e.append(f'{LAUNCHER} syntax error: {x}')
 # Explicitly reject the old project name in user-facing/source text.
 old=re.compile(('Hacking'+r'\s+'+'101')+'|'+('hacking'+'101'),re.I)
 for p in ROOT.rglob('*'):
  if p.is_file() and p.suffix.lower() in {'.md','.py','.json','.txt'}:
   try: text=p.read_text(encoding='utf-8',errors='replace')
   except OSError: continue
   if old.search(text): e.append(f'Legacy project name remains in {p.relative_to(ROOT)}')
 validate_links(e)
 e.extend(audit_project(ROOT, include_generated=False))
 # Keep error output stable when structural and quality checks report the same issue.
 return sorted(set(e))

def build_category_readmes(m):
 for lang,dirname in LANGS.items():
  cats=m['categories']; base=ROOT/dirname
  for idx,cat in enumerate(cats):
   catdir=base/cat['id']; title=CATEGORY_LABELS[lang].get(cat['id'],cat['id'])
   out=[f'# {title}','']
   if lang=='en': out += ['[← English Home](../README.md) · [Start Here](../Guides/START-HERE.md) · [Lab Guide](../Guides/LAB-GUIDE.md)','',f'**{len(cat["modules"])} lessons in this category.** Select any lesson below; module numbers remain global across Hacking Guide Project.','']
   else: out += ['[← Αρχική Ελληνικών](../README.md) · [Ξεκίνα εδώ](../Guides/START-HERE.md) · [Οδηγός Labs](../Guides/LAB-GUIDE.md)','',f'**{len(cat["modules"])} μαθήματα σε αυτή την κατηγορία.** Επίλεξε μάθημα παρακάτω· οι αριθμοί παραμένουν ίδιοι σε όλο το Hacking Guide Project.','']
   for n in cat['modules']:
    p=module_path(m,lang,n); out.append(f'- **{n:03d}** — [{heading(p)}]({p.name})')
   out += ['','---','']; nav=[]
   if idx>0:
    prev=cats[idx-1]; nav.append(f'[← {CATEGORY_LABELS[lang].get(prev["id"],prev["id"])}](../{prev["id"]}/README.md)')
   nav.append('[English Home](../README.md)' if lang=='en' else '[Αρχική Ελληνικών](../README.md)')
   if idx+1<len(cats):
    nxt=cats[idx+1]; nav.append(f'[{CATEGORY_LABELS[lang].get(nxt["id"],nxt["id"])} →](../{nxt["id"]}/README.md)')
   out.append(' · '.join(nav)); (catdir/'README.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
   legacy=catdir/'INDEX.md'
   if legacy.exists(): legacy.unlink()

def anchor(t):
 t=re.sub(r'<[^>]+>','',t.lower()); t=re.sub(r'[^\w\s-]','',t,flags=re.UNICODE)
 return re.sub(r'[\s_]+','-',t).strip('-')

def combined(m,lang):
 label='Hacking Guide Project — All Modules' if lang=='en' else 'Hacking Guide Project — Όλα τα Μαθήματα'
 gen='Generated from the categorized English modules. Edit individual lessons, then rebuild.' if lang=='en' else 'Δημιουργήθηκε από τα κατηγοριοποιημένα ελληνικά μαθήματα. Επεξεργάσου τα επιμέρους αρχεία και μετά κάνε rebuild.'
 out=[f'# {label}','',f'> {gen}','','## Index' if lang=='en' else '## Ευρετήριο','']
 for cat in m['categories']:
  out += [f'### {cat["id"]}','']
  for n in cat['modules']:
   p=module_path(m,lang,n); t=heading(p); out.append(f'- {n:03d}. [{t}](#{anchor(t)})')
  out.append('')
 out += ['---','']; nums=module_numbers(m)
 for i,n in enumerate(nums):
  p=module_path(m,lang,n); out.append(p.read_text(encoding='utf-8').rstrip())
  if i+1<len(nums): out += ['','---','']
 return '\n'.join(out).rstrip()+'\n'

def build_one(m,lang):
 base=ROOT/LANGS[lang]/'Combined'; base.mkdir(parents=True,exist_ok=True)
 md=base/'All-Modules.md'; h=base/'All-Modules.html'; text=combined(m,lang); md.write_text(text,encoding='utf-8')
 pandoc=shutil.which('pandoc'); title='Hacking Guide Project — All Modules' if lang=='en' else 'Hacking Guide Project — Όλα τα Μαθήματα'
 if pandoc: subprocess.run([pandoc,'--from=gfm',str(md),'--standalone','--metadata',f'title={title}','-o',str(h)],check=True)
 else: h.write_text('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><style>body{font-family:system-ui,sans-serif;max-width:1100px;margin:2rem auto;padding:0 1rem;line-height:1.5}pre{white-space:pre-wrap;word-wrap:break-word}</style></head><body><pre>'+html.escape(text)+'</pre></body></html>',encoding='utf-8')

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); a=ap.parse_args(); e=validate(); m=manifest(); total=len(module_numbers(m))
 if e:
  for x in e: print('ERROR:',x,file=sys.stderr)
  return 1
 if a.check:
  print(f'OK: bilingual structure validated — {total} English + {total} Greek modules.')
  return 0
 build_category_readmes(m); build_one(m,'en'); build_one(m,'gr'); e=validate()
 if e:
  for x in e: print('ERROR after build:',x,file=sys.stderr)
  return 1
 print(f'OK: rebuilt English and Greek combined editions; {total*2} module files validated.')
 return 0
if __name__=='__main__': raise SystemExit(main())
