#!/usr/bin/env python3
"""Hacking Guide Project — bilingual offline search/reader for Hacking Guide Project.

Termux-friendly and Python-standard-library only. The program searches and
reads local Markdown lessons. It does not scan networks or execute attacks.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import shutil
import sys
import textwrap
from collections import Counter
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Iterable

APP_NAME = "Hacking Guide Project"
MODULE_RE = re.compile(r"^(\d+)-.+\.md$", re.I)
TOKEN_RE = re.compile(r"[\w+#.-]{2,}", re.UNICODE)
TAG_RE = re.compile(r"<[^>]+>")
ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")
LANG_DIRS = {"en": "English", "gr": "Greek"}
LANG_NAMES = {"en": "English", "gr": "Ελληνικά"}

STOPWORDS = {
    "en": {"a","an","and","are","as","at","be","been","by","can","do","for","from","how","in","into","is","it","of","on","or","that","the","their","this","to","use","using","what","when","where","which","with","you","your","we","will","should","than","then","if","not"},
    "gr": {"και","ή","η","ο","οι","το","τα","των","της","του","σε","στο","στη","στην","στον","με","για","από","ως","είναι","ένα","μια","μία","που","να","θα","πως","πώς","τι","όταν","χωρίς","πριν","μετά","αυτό","αυτή","αυτά","τους","τις","τον"},
}

GUIDE_DOCS = {
    "start": "START-HERE.md",
    "study": "STUDY-METHOD.md",
    "labs": "LAB-GUIDE.md",
    "termux": "TERMUX-QUICKSTART.md",
    "cheatsheet": "REFERENCE-CHEATSHEET.md",
    "advanced": "ADVANCED-TRACK.md",
}

LEARNING_PATHS = {
    "beginner": [1,28,29,51,52,5,11,14,21,27,45],
    "termux": [28,29,30,31,36,51,52,27,45,56],
    "blue": [1,5,7,8,12,23,32,33,37,38,47,48,59,80,81,106],
    "appsec": [1,11,13,14,20,22,39,40,41,52,69,70,71,89,90,92,93,108],
    "cloud": [1,19,21,22,24,41,49,50,75,76,94,97,98,104,105,113,114],
    "mobile": [17,28,29,30,31,39,44,54,55,56,82,83],
    "ai": [20,21,22,25,39,41,46,49,57,59,114],
    "governance": [5,26,37,42,43,48,50,57,59,60,114],
    "career": [1,28,29,36,45,58,85,115,139,140],
    "advanced": list(range(61,141)),
    "reverse": [62,63,64,65,67,77,79,82,83,84,95,99,109,111,112,115,116,117,118,119,120,121],
    "exploit-research": [53,61,62,63,64,65,66,67,68,84,99,109,115,116,117,118,119],
    "identity": [21,32,39,49,72,73,76,78,92,93,100,103,113,128,129,130,131,132],
    "protocol": [20,49,51,52,69,70,77,78,86,87,89,91,100,101,122,123,124,125,128,131],
    "detection": [12,23,37,47,59,72,73,74,75,76,79,80,81,96,106,107,110,115,120,125,137,140],
    "internet-core": [51,77,86,87,88],
    "modern-api": [52,69,70,71,89,90,91,92,93,108,124,126,127],
    "platform-internals": [62,64,73,74,75,94,95,96,99,102,103,111,112,116,117,118,119,120,121],
    "supply-chain": [22,24,49,84,97,98,99,109,133,134,135],
    "crypto-modern": [20,49,78,92,100,101,102,103,113,125,131,132],
    "cloud-native": [19,24,75,76,97,104,105,113,114,132,134,135,136,137],
    "purple": [23,47,80,81,96,106,107,110],
    "code-audit": [40,61,65,67,84,99,108,109,116,117,127,139],
    "identity-federation": [21,39,72,92,93,113,128,129,130,131,132],
    "modern-transport": [51,52,69,77,87,89,124,125,126,127],
    "platform-security": [53,62,73,74,95,103,116,117,118,119,120,121,122,123],
    "secure-ai-development": [22,25,40,41,46,108,109,138,139,140],
}

PATH_DESCRIPTIONS = {
    "en": {
        "beginner":"Foundations to safe hands-on practice and a first capstone.",
        "termux":"Android/Termux operations, automation, networking and mobile security.",
        "blue":"Detection, incident response, forensics, recovery and SOC operations.",
        "appsec":"HTTP, sessions, web/API security, secure coding and architecture.",
        "cloud":"Cloud identity, containers, DevSecOps, supply chain and data security.",
        "mobile":"Android, Termux, application internals, device and proximity security.",
        "ai":"LLM/agentic security, identity, tool permissions and data protection.",
        "governance":"Risk, privacy, resilience, disclosure, evidence and metrics.",
        "career":"Practical projects that build a defensible cybersecurity portfolio.",
        "advanced":"Deep internals, reverse engineering, identity, protocols and research.",
        "identity-federation":"SAML, SCIM, PAM, WebAuthn, workload identity and enterprise federation.",
        "modern-transport":"HTTP/3, QUIC, DNS trust/privacy, edge proxies and parser boundaries.",
        "platform-security":"Memory, IPC, isolation, macOS/iOS, cellular and RF platform internals.",
        "secure-ai-development":"RAG security, AI-generated code review and secure AI-assisted engineering.",
    },
    "gr": {
        "beginner":"Από τις βάσεις μέχρι ασφαλή πρακτική εξάσκηση και πρώτο capstone.",
        "termux":"Android/Termux, αυτοματοποίηση, δίκτυα και ασφάλεια κινητών.",
        "blue":"Ανίχνευση, incident response, forensics, recovery και λειτουργία SOC.",
        "appsec":"HTTP, sessions, web/API security, secure coding και αρχιτεκτονική.",
        "cloud":"Cloud identity, containers, DevSecOps, supply chain και ασφάλεια δεδομένων.",
        "mobile":"Android, Termux, εσωτερική λειτουργία εφαρμογών και ασφάλεια συσκευών.",
        "ai":"Ασφάλεια LLM/agents, ταυτότητες, δικαιώματα εργαλείων και δεδομένα.",
        "governance":"Κίνδυνος, ιδιωτικότητα, ανθεκτικότητα, disclosure, αποδείξεις και metrics.",
        "career":"Πρακτικά projects για ισχυρό και αποδείξιμο cybersecurity portfolio.",
        "advanced":"Βαθιά internals, reverse engineering, identity, protocols και research.",
        "identity-federation":"SAML, SCIM, PAM, WebAuthn, workload identity και enterprise federation.",
        "modern-transport":"HTTP/3, QUIC, DNS trust/privacy, edge proxies και parser boundaries.",
        "platform-security":"Memory, IPC, isolation, macOS/iOS, cellular και RF platform internals.",
        "secure-ai-development":"RAG security, review AI-generated code και ασφαλές AI-assisted engineering.",
    },
}

CATEGORY_LABELS = {
    "en": {
        "01-Fundamentals-and-Methodology": "Fundamentals & Methodology",
        "02-Recon-Pentesting-Web-and-AppSec": "Recon, Pentesting, Web & AppSec",
        "03-Systems-Malware-and-Reverse-Engineering": "Systems, Malware & Reverse Engineering",
        "04-Network-Wireless-and-Internet": "Networks, Wireless & Internet",
        "05-Mobile-IoT-and-Hardware": "Mobile, IoT & Hardware",
        "06-Identity-Cryptography-and-Trust": "Identity, Cryptography & Trust",
        "07-Cloud-Containers-and-Supply-Chain": "Cloud, Containers & Supply Chain",
        "08-Blue-Team-IR-Forensics-and-Resilience": "Blue Team, IR & Forensics",
        "09-AI-GRC-Privacy-Data-and-Human-Security": "AI, GRC, Privacy & Human Security",
        "10-Termux-and-Security-Automation": "Termux & Security Automation",
        "11-Labs-Capstones-and-Career": "Labs, Capstones & Career",
    },
    "gr": {
        "01-Fundamentals-and-Methodology": "Βάσεις & Μεθοδολογία",
        "02-Recon-Pentesting-Web-and-AppSec": "Recon, Pentesting, Web & AppSec",
        "03-Systems-Malware-and-Reverse-Engineering": "Συστήματα, Malware & Reverse Engineering",
        "04-Network-Wireless-and-Internet": "Δίκτυα, Ασύρματα & Internet",
        "05-Mobile-IoT-and-Hardware": "Κινητά, IoT & Hardware",
        "06-Identity-Cryptography-and-Trust": "Ταυτότητα, Κρυπτογραφία & Trust",
        "07-Cloud-Containers-and-Supply-Chain": "Cloud, Containers & Supply Chain",
        "08-Blue-Team-IR-Forensics-and-Resilience": "Blue Team, IR & Forensics",
        "09-AI-GRC-Privacy-Data-and-Human-Security": "AI, GRC, Ιδιωτικότητα & Human Security",
        "10-Termux-and-Security-Automation": "Termux & Αυτοματοποίηση Ασφάλειας",
        "11-Labs-Capstones-and-Career": "Labs, Capstones & Καριέρα",
    },
}


TOPIC_GROUPS = {
    "en": [
        ("Start & Foundations", [
            ("Cybersecurity foundations", "security fundamentals methodology"),
            ("Termux & Android Linux", "Termux Android Linux"),
            ("Networking", "networking TCP UDP DNS routing"),
            ("Web & HTTP", "HTTP browser web security"),
            ("Linux security", "Linux security hardening capabilities"),
            ("Windows & Active Directory", "Windows Active Directory Kerberos"),
        ]),
        ("Application & Identity", [
            ("Web application security", "web application OWASP sessions authorization"),
            ("API security", "API authorization OAuth GraphQL gRPC"),
            ("Authentication & Passkeys", "authentication WebAuthn passkeys FIDO2"),
            ("Identity & Kerberos", "identity Kerberos Active Directory federation"),
            ("Secure coding", "secure coding code review ASVS"),
            ("Cryptography & PKI", "cryptography TLS PKI key management"),
        ]),
        ("Advanced Research", [
            ("Reverse engineering", "reverse engineering binary disassembly"),
            ("Memory safety", "memory corruption mitigations heap lifetime"),
            ("Fuzzing", "fuzzing harness coverage crash triage"),
            ("Malware analysis", "malware analysis behavioral triage"),
            ("Forensics", "digital forensics evidence timeline memory"),
            ("Firmware & hardware", "firmware hardware embedded boot security"),
        ]),
        ("Cloud, Defense & Modern Security", [
            ("Cloud & IAM", "cloud IAM control plane temporary credentials"),
            ("Containers & Kubernetes", "containers Kubernetes isolation admission policy"),
            ("Detection & SOC", "detection engineering SOC SIEM EDR telemetry"),
            ("Incident response", "incident response threat hunting recovery"),
            ("AI / LLM / Agent security", "AI LLM agentic MCP RAG security"),
            ("OSINT & threat intelligence", "OSINT threat intelligence reconnaissance"),
            ("Wireless, Bluetooth & RF", "wireless WPA3 Bluetooth NFC RF security"),
            ("Labs & capstones", "authorized labs capstone practice"),
        ]),
    ],
    "gr": [
        ("Έναρξη & Βάσεις", [
            ("Βάσεις κυβερνοασφάλειας", "security fundamentals methodology"),
            ("Termux & Android Linux", "Termux Android Linux"),
            ("Δίκτυα", "δίκτυο TCP UDP DNS routing"),
            ("Web & HTTP", "HTTP browser web security"),
            ("Ασφάλεια Linux", "Linux security hardening capabilities"),
            ("Windows & Active Directory", "Windows Active Directory Kerberos"),
        ]),
        ("Εφαρμογές & Ταυτότητα", [
            ("Ασφάλεια web εφαρμογών", "web application OWASP sessions authorization"),
            ("API security", "API authorization OAuth GraphQL gRPC"),
            ("Authentication & Passkeys", "authentication WebAuthn passkeys FIDO2"),
            ("Identity & Kerberos", "identity Kerberos Active Directory federation"),
            ("Secure coding", "secure coding code review ASVS"),
            ("Κρυπτογραφία & PKI", "κρυπτογραφία TLS PKI key management"),
        ]),
        ("Προχωρημένο Research", [
            ("Reverse engineering", "reverse engineering binary disassembly"),
            ("Memory safety", "memory corruption mitigations heap lifetime"),
            ("Fuzzing", "fuzzing harness coverage crash triage"),
            ("Malware analysis", "malware analysis behavioral triage"),
            ("Digital forensics", "ψηφιακή εγκληματολογία evidence timeline memory"),
            ("Firmware & hardware", "firmware hardware embedded boot security"),
        ]),
        ("Cloud, Άμυνα & Σύγχρονη Ασφάλεια", [
            ("Cloud & IAM", "cloud IAM control plane temporary credentials"),
            ("Containers & Kubernetes", "containers Kubernetes isolation admission policy"),
            ("Detection & SOC", "ανίχνευση SOC SIEM EDR telemetry"),
            ("Incident response", "incident response threat hunting recovery"),
            ("AI / LLM / Agent security", "AI LLM agentic MCP RAG security"),
            ("OSINT & threat intelligence", "OSINT threat intelligence reconnaissance"),
            ("Wireless, Bluetooth & RF", "wireless WPA3 Bluetooth NFC RF security"),
            ("Labs & capstones", "authorized labs capstone practice"),
        ]),
    ],
}

ALIASES = {
    "en": {
        "ad":["active directory","kerberos","domain"], "ai":["llm","agentic","mcp"],
        "api":["endpoint","authorization","oauth"], "android":["mobile","termux","keystore"],
        "auth":["authentication","identity","authorization"], "cloud":["iam","container","saas"],
        "forensics":["evidence","timeline","memory","filesystem"], "kerberos":["ticket","tgt","spn"],
        "networking":["tcp","udp","dns","routing","ipv6"], "reverse engineering":["binary","disassembly","decompiler"],
        "termux":["android","shell","packages","storage"], "web":["http","browser","owasp","session"],
    },
    "gr": {
        "ενεργός κατάλογος":["active directory","kerberos","domain"], "τεχνητή νοημοσύνη":["ai","llm","agentic","mcp"],
        "εφαρμογή":["application","app","api"], "android":["mobile","termux","keystore"],
        "ταυτοποίηση":["authentication","identity","authorization"], "εξουσιοδότηση":["authorization","permissions","rbac","abac"],
        "δίκτυο":["network","tcp","udp","dns","routing","ipv6"], "δικτύωση":["networking","tcp","udp","dns"],
        "κρυπτογραφία":["cryptography","crypto","tls","pki"], "ανίχνευση":["detection","soc","siem","telemetry"],
        "ψηφιακή εγκληματολογία":["forensics","evidence","timeline","memory"], "αντίστροφη μηχανική":["reverse engineering","binary","disassembly"],
        "ευπάθεια":["vulnerability","cve","cvss"], "ιστός":["web","http","browser","owasp"],
        "νέφος":["cloud","iam","container","saas"], "termux":["android","shell","packages","storage"],
    },
}

@dataclass(frozen=True)
class Section:
    language: str
    module: int
    module_title: str
    category: str
    path: Path
    heading: str
    level: int
    text: str
    line_start: int
    line_end: int

@dataclass
class Result:
    score: float
    section: Section
    snippet: str

class Palette:
    def __init__(self, enabled: bool): self.enabled=enabled
    def c(self,code,v): return f"\033[{code}m{v}\033[0m" if self.enabled else v
    def title(self,v): return self.c("1;36",v)
    def strong(self,v): return self.c("1",v)
    def dim(self,v): return self.c("2",v)
    def good(self,v): return self.c("32",v)
    def warn(self,v): return self.c("33",v)
    def bad(self,v): return self.c("31",v)

def project_root(explicit: str|None) -> Path:
    candidates=[]
    if explicit: candidates.append(Path(explicit).expanduser())
    candidates += [Path(__file__).resolve().parent, Path.cwd()]
    for c in candidates:
        c=c.resolve()
        if (c/'manifest.json').exists() and any((c/d).is_dir() for d in LANG_DIRS.values()): return c
    raise SystemExit("Could not locate the bilingual guide root. Use --directory PATH.")

def load_manifest(root: Path) -> dict:
    return json.loads((root/'manifest.json').read_text(encoding='utf-8'))

def module_files(root: Path, lang: str, manifest: dict) -> list[tuple[int,Path]]:
    langdir=root/LANG_DIRS[lang]
    found=[]
    for key,meta in manifest['modules'].items():
        n=int(key); p=langdir/meta['category']/meta['filename']
        if p.exists(): found.append((n,p))
    return sorted(found)

def clean_heading(value: str) -> str:
    return TAG_RE.sub('',value).strip().strip('#').strip()

def parse_module(lang: str, n: int, path: Path) -> tuple[str,list[Section]]:
    lines=path.read_text(encoding='utf-8',errors='replace').splitlines()
    title=path.stem
    for line in lines:
        if line.startswith('# '): title=clean_heading(line[2:]); break
    sections=[]; heading=title; level=1; start=1; buf=[]
    def flush(end):
        nonlocal buf,start
        text='\n'.join(buf).strip()
        if text: sections.append(Section(lang,n,title,path.parent.name,path,heading,level,text,start,end))
        buf=[]
    for i,line in enumerate(lines,1):
        m=re.match(r'^(#{1,6})\s+(.+?)\s*$',line)
        if m:
            flush(i-1); level=len(m.group(1)); heading=clean_heading(m.group(2)); start=i; buf=[line]
        else: buf.append(line)
    flush(len(lines)); return title,sections

def tokenize(text: str, lang: str) -> list[str]:
    stop=STOPWORDS.get(lang,set())
    return [t.lower().strip('.-') for t in TOKEN_RE.findall(text) if t.lower().strip('.-') not in stop]

def make_snippet(text: str, terms:list[str], phrase:str, width=260) -> str:
    plain=re.sub(r"[`*_>#|]",' ',text)
    plain=re.sub(r"\[[^\]]+\]\([^)]+\)",' ',plain)
    plain=re.sub(r"\s+",' ',plain).strip(); low=plain.lower()
    positions=[]
    if phrase and phrase in low: positions.append(low.find(phrase))
    positions += [low.find(t) for t in terms if t in low]
    pos=min(positions) if positions else 0; start=max(0,pos-width//3); end=min(len(plain),start+width)
    s=plain[start:end].strip()
    return ('…' if start else '')+s+('…' if end<len(plain) else '')

class GuideIndex:
    def __init__(self, root:Path, languages:list[str]):
        self.root=root; self.manifest=load_manifest(root); self.languages=languages
        self.modules:dict[str,list[tuple[int,Path]]]={}; self.titles:dict[str,dict[int,str]]={}; self.sections=[]
        for lang in languages:
            mods=module_files(root,lang,self.manifest); self.modules[lang]=mods; self.titles[lang]={}
            for n,p in mods:
                title,secs=parse_module(lang,n,p); self.titles[lang][n]=title; self.sections.extend(secs)
        self.section_tokens=[]; self.df=Counter()
        for s in self.sections:
            c=Counter(tokenize(s.text+' '+s.heading,s.language)); self.section_tokens.append(c); self.df.update(c.keys())
        self.total=max(1,len(self.sections))
    def idf(self,t): return math.log((self.total+1)/(self.df.get(t,0)+1))+1
    def search(self,q:str,limit=10,exact=False,module=None,languages=None):
        q=q.strip(); results=[]
        if not q:return results
        allowed=set(languages) if languages else None
        for idx,s in enumerate(self.sections):
            if allowed is not None and s.language not in allowed: continue
            if module is not None and s.module!=module: continue
            terms=tokenize(q,s.language) or [q.lower()]; phrase=q.lower(); counts=self.section_tokens[idx]
            text=s.text.lower(); head=s.heading.lower(); title=s.module_title.lower(); score=0; matched=0
            if exact and phrase not in text and phrase not in head and phrase not in title: continue
            for term in terms:
                tf=counts.get(term,0)
                if tf: matched+=1; score+=(1+math.log(tf))*self.idf(term)
                if term in head: score+=3.5
                if term in title: score+=4.5
            if phrase in head: score+=12
            elif phrase in title: score+=10
            elif phrase in text: score+=6
            if not exact:
                for key,vals in ALIASES.get(s.language,{}).items():
                    if key in phrase:
                        for v in vals:
                            for t in tokenize(v,s.language):
                                if counts.get(t): score+=.3*self.idf(t)
                if matched<len(terms):
                    vocab=list(counts.keys())[:800]
                    for t in terms:
                        if counts.get(t) or len(t)<4: continue
                        best=max((SequenceMatcher(None,t,c).ratio() for c in vocab if c[:1]==t[:1] and abs(len(c)-len(t))<=3), default=0)
                        if best>=.84: score+=best*.7
            if terms: score+=2*(matched/len(terms))
            if score>0: results.append(Result(score,s,make_snippet(s.text,terms,phrase)))
        results.sort(key=lambda r:(-r.score,r.section.language,r.section.module,r.section.line_start))
        return results[:max(1,limit)]
    def stats(self):
        out={}
        for lang in self.languages:
            words=lines=0
            for _,p in self.modules[lang]:
                t=p.read_text(encoding='utf-8',errors='replace'); words+=len(re.findall(r'\b\w+\b',t,re.UNICODE)); lines+=t.count('\n')+1
            out[lang]={'modules':len(self.modules[lang]),'words':words,'lines':lines,'sections':sum(1 for s in self.sections if s.language==lang)}
        return out

def render_markdown_text(text:str, skip_first_h1:bool=False)->str:
    out=[]; code=False; skipped_h1=False
    for line in text.splitlines():
        if skip_first_h1 and not skipped_h1 and line.startswith('# '):
            skipped_h1=True
            continue
        if line.strip().startswith('```'): code=not code; continue
        if code: out.append('    '+line); continue
        line=TAG_RE.sub('',line); line=re.sub(r'^#{1,6}\s*','',line)
        line=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1 (\2)',line)
        line=line.replace('**','').replace('__','').replace('`',''); out.append(line)
    return '\n'.join(out)

def page_text(text:str,lang:str='en'):
    if not sys.stdout.isatty(): print(text); return
    lines=text.splitlines(); page=max(8,shutil.get_terminal_size((88,24)).lines-4)
    prompt='-- Enter = next page | 0 = stop reading -- ' if lang=='en' else '-- Enter = επόμενη σελίδα | 0 = τέλος ανάγνωσης -- '
    for i in range(0,len(lines),page):
        print('\n'.join(lines[i:i+page]))
        if i+page<len(lines):
            try: ch=input(prompt).strip().lower()
            except (EOFError,KeyboardInterrupt): print(); return
            if ch in ('0','q'): return

def state_path() -> Path:
    override=os.environ.get('HACKING_GUIDE_PROJECT_STATE')
    return Path(override).expanduser() if override else Path.home()/'.hacking-guide-project'/'state.json'

def empty_state() -> dict:
    return {
        'version': 1,
        'language': 'en',
        'last_module': {'en': None, 'gr': None},
        'bookmarks': {'en': [], 'gr': []},
        'completed': {'en': [], 'gr': []},
        'recent': {'en': [], 'gr': []},
        'search_history': {'en': [], 'gr': [], 'both': []},
    }

def load_state() -> dict:
    state=empty_state(); path=state_path()
    try:
        raw=json.loads(path.read_text(encoding='utf-8'))
        if isinstance(raw,dict):
            for key in ('language','last_module','bookmarks','completed','recent','search_history'):
                if key in raw: state[key]=raw[key]
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        pass
    for lang in ('en','gr'):
        state.setdefault('last_module',{}).setdefault(lang,None)
        for key in ('bookmarks','completed','recent'):
            vals=state.setdefault(key,{}).setdefault(lang,[])
            state[key][lang]=[int(v) for v in vals if str(v).isdigit() and 1<=int(v)<=10000]
    hist=state.setdefault('search_history',{})
    for scope in ('en','gr','both'):
        values=hist.setdefault(scope,[])
        hist[scope]=[str(v).strip() for v in values if str(v).strip()][:20]
    if state.get('language') not in ('en','gr'): state['language']='en'
    return state

def save_state(state:dict):
    path=state_path()
    try:
        path.parent.mkdir(parents=True,exist_ok=True)
        tmp=path.with_suffix('.tmp')
        tmp.write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8')
        tmp.replace(path)
    except OSError:
        pass

def record_visit(state:dict,lang:str,module:int):
    state['last_module'][lang]=module
    recent=[n for n in state['recent'][lang] if n!=module]
    state['recent'][lang]=([module]+recent)[:20]
    save_state(state)

def record_search(state:dict,scope:str,query:str):
    query=query.strip()
    if not query:return
    scope=scope if scope in ('en','gr','both') else 'en'
    values=[q for q in state['search_history'][scope] if q.casefold()!=query.casefold()]
    state['search_history'][scope]=([query]+values)[:20]
    save_state(state)

def toggle_state_item(state:dict,key:str,lang:str,module:int)->bool:
    values=state[key][lang]
    if module in values: values.remove(module); enabled=False
    else: values.append(module); values.sort(); enabled=True
    save_state(state); return enabled

def friendly_category(cat_id:str,lang:str)->str:
    return CATEGORY_LABELS.get(lang,{}).get(cat_id,cat_id.split('-',1)[-1].replace('-',' '))

def module_marker(state:dict,lang:str,n:int)->str:
    done='✓' if n in state['completed'][lang] else ' '
    star='★' if n in state['bookmarks'][lang] else ' '
    last='→' if state['last_module'][lang]==n else ' '
    return f'{done}{star}{last}'

def print_results(results,p):
    if not results: print(p.warn('No matching lesson sections found. / Δεν βρέθηκαν σχετικά μαθήματα.')); return
    width=min(100,shutil.get_terminal_size((88,24)).columns)
    for i,r in enumerate(results,1):
        s=r.section; flag='EN' if s.language=='en' else 'GR'
        print(p.strong(f'[{i}] [{flag}] Module {s.module:03d} — {s.module_title}'))
        if s.heading!=s.module_title: print('    '+p.title(s.heading))
        rel=s.path.relative_to(s.path.parents[2]) if len(s.path.parents)>2 else s.path.name
        print('    '+p.dim(f'{rel}:{s.line_start}-{s.line_end}  score={r.score:.2f}'))
        for line in textwrap.wrap(r.snippet,max(30,width-4)) or ['']: print('    '+line)
        print()

def print_compact_results(results,p,lang):
    if not results:
        print(p.warn('No matching lessons found.' if lang=='en' else 'Δεν βρέθηκαν σχετικά μαθήματα.'))
        return
    width=min(96,shutil.get_terminal_size((88,24)).columns)
    for i,r in enumerate(results,1):
        sec=r.section; flag='EN' if sec.language=='en' else 'GR'
        print(p.strong(f'{i:02d}. [{flag}] {sec.module:03d} — {sec.module_title}'))
        if sec.heading!=sec.module_title:
            print('    '+p.title(sec.heading))
        short=r.snippet
        if len(short)>180: short=short[:177].rstrip()+'…'
        for line in textwrap.wrap(short,max(30,width-4))[:2]: print('    '+line)
        print()

def list_modules(index,p,lang,state=None):
    for n,path in index.modules[lang]:
        marker=module_marker(state,lang,n)+' ' if state else ''
        print(f"{marker}{p.strong(f'{n:03d}')}  {index.titles[lang][n]}  {p.dim(path.parent.name+'/'+path.name)}")

def show_module(index,selector,p,lang,state=None,skip_title=False):
    num=int(selector) if str(selector).isdigit() else None
    if num is None:
        q=str(selector).lower(); hits=[(n,t) for n,t in index.titles[lang].items() if q in t.lower()]
        if len(hits)==1:num=hits[0][0]
        elif hits:
            for n,t in hits: print(f'{n:03d} {t}')
            return False
    if num not in index.titles[lang]: print(p.warn('Module not found. / Το μάθημα δεν βρέθηκε.')); return False
    path=dict(index.modules[lang])[num]
    if state is not None: record_visit(state,lang,num)
    page_text(render_markdown_text(path.read_text(encoding='utf-8',errors='replace'),skip_first_h1=skip_title),lang); return True

def read_module_loop(index,num,p,lang,state):
    max_num=max(index.titles[lang]) if index.titles[lang] else 0
    while 1<=num<=max_num and num in index.titles[lang]:
        print('\n'+p.title(f"{'Module' if lang=='en' else 'Μάθημα'} {num:03d} — {index.titles[lang][num]}"))
        print(p.dim(f"[{friendly_category(dict(index.modules[lang])[num].parent.name,lang)}]"))
        show_module(index,str(num),p,lang,state,skip_title=True)
        while True:
            done=num in state['completed'][lang]; bookmarked=num in state['bookmarks'][lang]
            if lang=='gr':
                status=(('✓ Ολοκληρωμένο' if done else '○ Μη ολοκληρωμένο')+'   '+('★ Bookmark' if bookmarked else '☆ Χωρίς bookmark'))
                print('\n'+p.dim(status))
                print('1 Επόμενο   2 Προηγούμενο   3 Ολοκλήρωση   4 Bookmark')
                print('5 Αναζήτηση   6 Αρχική   0 Έξοδος')
            else:
                status=(('✓ Complete' if done else '○ Not complete')+'   '+('★ Bookmarked' if bookmarked else '☆ Not bookmarked'))
                print('\n'+p.dim(status))
                print('1 Next   2 Previous   3 Complete   4 Bookmark')
                print('5 Search   6 Home   0 Exit')
            try: ch=input('Choose / Επιλογή: ').strip().lower()
            except (EOFError,KeyboardInterrupt): print(); return 'home'
            if ch in ('1','n','next','ε'):
                if num < max_num: num += 1
                break
            if ch in ('2','p','prev','previous','π'):
                if num > 1: num -= 1
                break
            if ch in ('3','c','complete','ο'):
                on=toggle_state_item(state,'completed',lang,num)
                print(p.good('Marked complete.' if on and lang=='en' else 'Ολοκληρώθηκε.' if on else 'Marked incomplete.' if lang=='en' else 'Αφαιρέθηκε η ολοκλήρωση.'))
                continue
            if ch in ('4','b','bookmark'):
                on=toggle_state_item(state,'bookmarks',lang,num)
                print(p.good('Bookmark saved.' if on and lang=='en' else 'Αποθηκεύτηκε bookmark.' if on else 'Bookmark removed.' if lang=='en' else 'Αφαιρέθηκε bookmark.'))
                continue
            if ch in ('5','s','search','α'): return 'search'
            if ch in ('0','q','quit','exit'): return 'quit'
            if ch in ('6','h','home',''): return 'home'
    return 'home'

def show_doc(index,key,p,lang):
    filename=GUIDE_DOCS[key]; path=index.root/LANG_DIRS[lang]/'Guides'/filename
    if not path.exists(): print(p.warn(f'Missing: {path}')); return False
    page_text(render_markdown_text(path.read_text(encoding='utf-8',errors='replace')),lang); return True

def show_path(index,name,p,lang,state=None):
    nums=LEARNING_PATHS.get(name)
    if not nums: print(p.warn('Unknown path.')); return False
    desc=PATH_DESCRIPTIONS.get(lang,{}).get(name) or PATH_DESCRIPTIONS.get('en',{}).get(name,'')
    print(p.title(name)); print(desc)
    for i,n in enumerate(nums,1):
        title=index.titles[lang].get(n,'[missing]'); marker=(module_marker(state,lang,n)+' ') if state else ''
        unit='Module' if lang=='en' else 'Μάθημα'
        print(f'{i:02d}. {marker}{unit} {n:03d} — {title}')
    return True

def list_paths(index,p,lang,state=None):
    for name in LEARNING_PATHS:
        desc=PATH_DESCRIPTIONS.get(lang,{}).get(name) or PATH_DESCRIPTIONS.get('en',{}).get(name,'')
        nums=LEARNING_PATHS[name]
        done=sum(1 for n in nums if state and n in state['completed'][lang])
        progress=f' [{done}/{len(nums)}]' if state else ''
        print(f'{p.strong(name):22} {desc}{progress}')

def list_categories(root,p,lang,manifest,state=None):
    print(p.title('Categories' if lang=='en' else 'Κατηγορίες'))
    for i,cat in enumerate(manifest['categories'],1):
        existing=[n for n in cat['modules'] if (root/LANG_DIRS[lang]/cat['id']/manifest['modules'][str(n)]['filename']).exists()]
        done=sum(1 for n in existing if state and n in state['completed'][lang])
        prog=f' — {done}/{len(existing)} complete' if lang=='en' and state else f' — {done}/{len(existing)} ολοκληρωμένα' if state else ''
        print(f"  {i:02d}. {friendly_category(cat['id'],lang)} ({len(existing)}){prog}")

def browse_category(index,p,lang,state,cat):
    modules=[n for n in cat['modules'] if n in index.titles[lang]]
    while True:
        print('\n'+p.title(friendly_category(cat['id'],lang)))
        for i,n in enumerate(modules,1):
            print(f"{i:02d}. {module_marker(state,lang,n)} {n:03d} — {index.titles[lang][n]}")
        print('0. '+('Back' if lang=='en' else 'Πίσω'))
        try: raw=input(('Lesson number: ' if lang=='en' else 'Αριθμός μαθήματος: ')).strip()
        except (EOFError,KeyboardInterrupt): print(); return 'home'
        if raw in ('0','b','back',''): return 'home'
        if not raw.isdigit(): continue
        value=int(raw); num=modules[value-1] if 1<=value<=len(modules) else value if value in modules else None
        if num:
            action=read_module_loop(index,num,p,lang,state)
            if action in ('quit','search','home'): return action

def browse_categories(index,p,lang,state):
    cats=index.manifest['categories']
    while True:
        print('\n'+p.title('Browse categories' if lang=='en' else 'Περιήγηση κατηγοριών'))
        for i,cat in enumerate(cats,1):
            mods=[n for n in cat['modules'] if n in index.titles[lang]]
            done=sum(1 for n in mods if n in state['completed'][lang])
            print(f"{i:02d}. {friendly_category(cat['id'],lang)}  {p.dim(f'[{done}/{len(mods)}]')}")
        print('0. '+('Home' if lang=='en' else 'Αρχική'))
        try: raw=input('> ').strip()
        except (EOFError,KeyboardInterrupt): print(); return 'home'
        if raw in ('0','b','back',''): return 'home'
        if raw.isdigit() and 1<=int(raw)<=len(cats):
            action=browse_category(index,p,lang,state,cats[int(raw)-1])
            if action in ('quit','search','home'): return action

def _dedupe_search_results(results,limit=15):
    out=[]; seen=set()
    for result in results:
        key=(result.section.language,result.section.module)
        if key in seen: continue
        seen.add(key); out.append(result)
        if len(out)>=limit: break
    return out

def search_results_menu(index,p,lang,state,query,scope=None):
    scope=scope or lang
    languages=['en','gr'] if scope=='both' else [scope]
    record_search(state,scope,query)
    results=_dedupe_search_results(index.search(query,80,languages=languages),15)
    print('\n'+p.title(('Search results' if lang=='en' else 'Αποτελέσματα αναζήτησης')+f': {query}'))
    print_compact_results(results,p,lang)
    if not results:return 'home'
    back='Back' if lang=='en' else 'Πίσω'
    print(f'0. {back}')
    try: raw=input(('Choose a result number: ' if lang=='en' else 'Επίλεξε αριθμό αποτελέσματος: ')).strip()
    except (EOFError,KeyboardInterrupt): print(); return 'home'
    if raw.isdigit() and 1<=int(raw)<=len(results):
        chosen=results[int(raw)-1].section
        return ('read',chosen.language,chosen.module)
    return 'home'

def topic_picker(index,p,lang,state,scope=None):
    groups=TOPIC_GROUPS[lang]
    flat=[]
    while True:
        print('\n'+p.title('Browse popular topics' if lang=='en' else 'Δημοφιλή θέματα'))
        flat=[]; n=1
        for group,items in groups:
            print('\n'+p.strong(group))
            for label,query in items:
                print(f'  {n:02d}. {label}')
                flat.append((label,query)); n+=1
        print('\n0. '+('Back' if lang=='en' else 'Πίσω'))
        try: raw=input(('Choose a topic: ' if lang=='en' else 'Επίλεξε θέμα: ')).strip()
        except (EOFError,KeyboardInterrupt): print(); return 'home'
        if raw in ('0',''): return 'home'
        if raw.isdigit() and 1<=int(raw)<=len(flat):
            label,query=flat[int(raw)-1]
            return search_results_menu(index,p,lang,state,query,scope or lang)

def recent_searches_menu(index,p,lang,state):
    while True:
        choices=[]
        # Show current-language history first, followed by searches performed in both languages.
        for scope in (lang,'both'):
            for q in state['search_history'].get(scope,[]):
                key=(scope,q.casefold())
                if key not in {(s,x.casefold()) for s,x in choices}: choices.append((scope,q))
                if len(choices)>=15: break
            if len(choices)>=15: break
        print('\n'+p.title('Recent searches' if lang=='en' else 'Πρόσφατες αναζητήσεις'))
        if not choices:
            print(p.dim('No recent searches yet.' if lang=='en' else 'Δεν υπάρχουν πρόσφατες αναζητήσεις.'))
            return 'home'
        for i,(scope,q) in enumerate(choices,1):
            tag='EN+GR' if scope=='both' else scope.upper()
            print(f'{i:02d}. [{tag}] {q}')
        print('0. '+('Back' if lang=='en' else 'Πίσω'))
        try: raw=input(('Choose a search: ' if lang=='en' else 'Επίλεξε αναζήτηση: ')).strip()
        except (EOFError,KeyboardInterrupt): print(); return 'home'
        if raw in ('0',''): return 'home'
        if raw.isdigit() and 1<=int(raw)<=len(choices):
            scope,q=choices[int(raw)-1]
            return search_results_menu(index,p,lang,state,q,scope)

def interactive_search(index,p,lang,state):
    while True:
        print('\n'+p.title('Search lessons' if lang=='en' else 'Αναζήτηση μαθημάτων'))
        if lang=='en':
            print('1 Type what you are looking for')
            print('2 Pick a popular topic')
            print('3 Recent searches')
            print('4 Search English + Greek together')
            print('5 Jump directly to a module number')
            print('0 Back')
        else:
            print('1 Γράψε τι ψάχνεις')
            print('2 Επίλεξε δημοφιλές θέμα')
            print('3 Πρόσφατες αναζητήσεις')
            print('4 Αναζήτηση μαζί σε Ελληνικά + English')
            print('5 Άνοιξε απευθείας αριθμό μαθήματος')
            print('0 Πίσω')
        try: choice=input('Choose / Επιλογή: ').strip()
        except (EOFError,KeyboardInterrupt): print(); return 'home'
        if choice in ('0',''): return 'home'
        if choice=='1':
            try: q=input('Words / Λέξεις: ').strip()
            except (EOFError,KeyboardInterrupt): print(); continue
            if q:return search_results_menu(index,p,lang,state,q,lang)
        elif choice=='2':
            return topic_picker(index,p,lang,state,lang)
        elif choice=='3':
            return recent_searches_menu(index,p,lang,state)
        elif choice=='4':
            try: q=input('Words / Λέξεις: ').strip()
            except (EOFError,KeyboardInterrupt): print(); continue
            if q:return search_results_menu(index,p,lang,state,q,'both')
        elif choice=='5':
            try: raw=input(('Module number: ' if lang=='en' else 'Αριθμός μαθήματος: ')).strip()
            except (EOFError,KeyboardInterrupt): print(); continue
            if raw.isdigit() and int(raw) in index.titles[lang]: return ('read',lang,int(raw))
            print(p.warn('Module not found.' if lang=='en' else 'Το μάθημα δεν βρέθηκε.'))

def interactive_paths(index,p,lang,state):
    names=list(LEARNING_PATHS)
    while True:
        print('\n'+p.title('Learning paths' if lang=='en' else 'Διαδρομές μάθησης'))
        for i,name in enumerate(names,1):
            nums=LEARNING_PATHS[name]; done=sum(1 for n in nums if n in state['completed'][lang])
            print(f'{i:02d}. {name:<20} [{done}/{len(nums)}]')
        print('0. '+('Back' if lang=='en' else 'Πίσω'))
        try: raw=input('> ').strip()
        except (EOFError,KeyboardInterrupt): print(); return 'home'
        if raw in ('0','b','back',''): return 'home'
        if raw.isdigit() and 1<=int(raw)<=len(names):
            name=names[int(raw)-1]; show_path(index,name,p,lang,state)
            nums=LEARNING_PATHS[name]
            try: pick=input(('Open path item or module number (Enter = back): ' if lang=='en' else 'Άνοιξε θέση ή αριθμό μαθήματος (Enter = πίσω): ')).strip()
            except (EOFError,KeyboardInterrupt): print(); continue
            if pick.isdigit():
                v=int(pick); num=nums[v-1] if 1<=v<=len(nums) else v if v in nums else None
                if num:return ('read',lang,num)

def bookmarks_menu(index,p,lang,state):
    nums=state['bookmarks'][lang]
    print('\n'+p.title('Bookmarks' if lang=='en' else 'Bookmarks'))
    if not nums:
        print(p.dim('No bookmarks yet.' if lang=='en' else 'Δεν υπάρχουν bookmarks ακόμη.')); return 'home'
    for i,n in enumerate(nums,1): print(f'{i:02d}. ★ {n:03d} — {index.titles[lang].get(n,"[missing]")}')
    try: raw=input(('Open bookmark (Enter = back): ' if lang=='en' else 'Άνοιξε bookmark (Enter = πίσω): ')).strip()
    except (EOFError,KeyboardInterrupt): print(); return 'home'
    if raw.isdigit():
        v=int(raw); num=nums[v-1] if 1<=v<=len(nums) else v if v in nums else None
        if num:return ('read',lang,num)
    return 'home'

def progress_view(index,p,lang,state):
    done=set(state['completed'][lang]); total=len(index.modules[lang]); pct=(100*len(done)/total) if total else 0
    print('\n'+p.title('Progress' if lang=='en' else 'Πρόοδος'))
    print(f"{len(done)}/{total}  ({pct:.1f}%)")
    barw=30; fill=round(barw*pct/100); print('['+'#'*fill+'-'*(barw-fill)+']')
    for cat in index.manifest['categories']:
        mods=[n for n in cat['modules'] if n in index.titles[lang]]; c=sum(1 for n in mods if n in done)
        print(f'{friendly_category(cat["id"],lang):42} {c:>3}/{len(mods):<3}')
    if state['recent'][lang]:
        print('\n'+p.strong('Recent lessons' if lang=='en' else 'Πρόσφατα μαθήματα'))
        for i,n in enumerate(state['recent'][lang][:10],1): print(f'  {i:02d}. {n:03d} — {index.titles[lang].get(n,"[missing]")}')

def progress_recent_menu(index,p,lang,state):
    while True:
        progress_view(index,p,lang,state)
        recent=state['recent'][lang][:10]
        if lang=='en': print('\n1-10 Open recent item   11 Completed lessons   0 Back')
        else: print('\n1-10 Άνοιξε πρόσφατο   11 Ολοκληρωμένα μαθήματα   0 Πίσω')
        try: raw=input('Choose / Επιλογή: ').strip()
        except (EOFError,KeyboardInterrupt): print(); return 'home'
        if raw in ('0',''): return 'home'
        if raw.isdigit() and 1<=int(raw)<=len(recent): return ('read',lang,recent[int(raw)-1])
        if raw=='11':
            nums=state['completed'][lang]
            print('\n'+p.title('Completed lessons' if lang=='en' else 'Ολοκληρωμένα μαθήματα'))
            if not nums: print(p.dim('None yet.' if lang=='en' else 'Κανένα ακόμη.'))
            for i,n in enumerate(nums,1): print(f'{i:03d}. {n:03d} — {index.titles[lang].get(n,"[missing]")}')

def quick_guides_menu(index,p,lang):
    items=[('start','Start Here' if lang=='en' else 'Ξεκίνα εδώ'),('study','Study Method' if lang=='en' else 'Μεθοδολογία Μελέτης'),('termux','Termux Quick Start'),('labs','Authorized Labs' if lang=='en' else 'Εξουσιοδοτημένα Labs'),('cheatsheet','Reference Cheatsheet'),('advanced','Advanced Track')]
    print('\n'+p.title('Quick guides' if lang=='en' else 'Γρήγοροι οδηγοί'))
    for i,(_,label) in enumerate(items,1): print(f'{i}. {label}')
    try: raw=input(('Guide (Enter = back): ' if lang=='en' else 'Οδηγός (Enter = πίσω): ')).strip()
    except (EOFError,KeyboardInterrupt): print(); return
    if raw.isdigit() and 1<=int(raw)<=len(items): show_doc(index,items[int(raw)-1][0],p,lang)

def all_modules_menu(index,p,lang,state,page_size=12):
    modules=[n for n,_ in index.modules[lang]]
    page=0; pages=max(1,(len(modules)+page_size-1)//page_size)
    while True:
        page=max(0,min(page,pages-1)); chunk=modules[page*page_size:(page+1)*page_size]
        print('\n'+p.title(('All lessons' if lang=='en' else 'Όλα τα μαθήματα')+f' — {page+1}/{pages}'))
        for i,n in enumerate(chunk,1): print(f'{i:02d}. {module_marker(state,lang,n)} {n:03d} — {index.titles[lang][n]}')
        if lang=='en': print('\n97 Jump to module   98 Previous page   99 Next page   0 Back')
        else: print('\n97 Μετάβαση σε μάθημα   98 Προηγούμενη σελίδα   99 Επόμενη σελίδα   0 Πίσω')
        try: raw=input('Choose / Επιλογή: ').strip()
        except (EOFError,KeyboardInterrupt): print(); return 'home'
        if raw in ('0',''): return 'home'
        if raw=='98': page-=1; continue
        if raw=='99': page+=1; continue
        if raw=='97':
            try: jump=input(('Module number: ' if lang=='en' else 'Αριθμός μαθήματος: ')).strip()
            except (EOFError,KeyboardInterrupt): print(); continue
            if jump.isdigit() and int(jump) in index.titles[lang]: return ('read',lang,int(jump))
            continue
        if raw.isdigit() and 1<=int(raw)<=len(chunk): return ('read',lang,chunk[int(raw)-1])

def settings_menu(p,lang,state):
    while True:
        print('\n'+p.title('Settings' if lang=='en' else 'Ρυθμίσεις'))
        if lang=='en':
            print('1 Use English interface')
            print('2 Χρήση Ελληνικού interface')
            print('0 Back')
        else:
            print('1 Use English interface')
            print('2 Χρήση Ελληνικού interface')
            print('0 Πίσω')
        try: raw=input('Choose / Επιλογή: ').strip()
        except (EOFError,KeyboardInterrupt): print(); return lang
        if raw=='0' or raw=='': return lang
        if raw in ('1','2'):
            newlang='en' if raw=='1' else 'gr'; state['language']=newlang; save_state(state); return newlang

def doctor(index,p):
    print(p.title('Hacking Guide Project doctor'))
    failures=0
    for lang in index.languages:
        nums=[n for n,_ in index.modules[lang]]
        expected=sorted(map(int,index.manifest['modules']))
        ok=nums==expected
        print((p.good('OK') if ok else p.bad('FAIL'))+f'  {LANG_NAMES[lang]} modules: {len(nums)}/{len(expected)}')
        failures += 0 if ok else 1
    print((p.good('OK') if sys.version_info>=(3,9) else p.bad('FAIL'))+f'  Python: {sys.version.split()[0]}')
    print((p.good('OK') if (index.root/'manifest.json').exists() else p.bad('FAIL'))+'  manifest.json')
    try:
        state_path().parent.mkdir(parents=True,exist_ok=True); writable=os.access(state_path().parent,os.W_OK)
    except OSError: writable=False
    print((p.good('OK') if writable else p.warn('WARN'))+f'  progress storage: {state_path()}')
    return 1 if failures else 0

def choose_language(default='en'):
    if not sys.stdin.isatty(): return default
    print('1  English\n2  Ελληνικά\n3  Both / Και τα δύο')
    ch=input('Language / Γλώσσα: ').strip()
    return {'1':'en','2':'gr','3':'both'}.get(ch,default)

def interactive(root,p,lang_mode):
    # Load both editions once so language switching and bilingual search are instant.
    index=GuideIndex(root,['en','gr'])
    first_run=not state_path().exists()
    state=load_state()
    active=lang_mode if lang_mode in ('en','gr') else state.get('language','en')
    if first_run and sys.stdin.isatty():
        print('\n'+p.title(APP_NAME))
        print('Choose your language / Επίλεξε γλώσσα')
        print('1. English\n2. Ελληνικά')
        try: raw=input('Choose / Επιλογή: ').strip()
        except (EOFError,KeyboardInterrupt): raw='1'
        active='gr' if raw=='2' else 'en'; state['language']=active; save_state(state)
    while True:
        last=state['last_module'][active]; done=len(state['completed'][active]); total=len(index.modules[active])
        print('\n'+p.title(f'{APP_NAME} — {LANG_NAMES[active]}'))
        print(p.dim((f'Progress: {done}/{total}' if active=='en' else f'Πρόοδος: {done}/{total}')+'   '+('★ '+str(len(state['bookmarks'][active])))))
        if active=='en':
            print('1 Continue'+(f' — Module {last:03d}' if last else ' — Start Module 001'))
            print('2 Search lessons')
            print('3 Browse categories')
            print('4 Browse popular topics')
            print('5 Learning paths')
            print('6 Bookmarks')
            print('7 Progress & recent lessons')
            print('8 Quick guides')
            print('9 All lessons')
            print('10 Language / Settings')
            print('0 Exit')
        else:
            print('1 Συνέχεια'+(f' — Μάθημα {last:03d}' if last else ' — Έναρξη από Μάθημα 001'))
            print('2 Αναζήτηση μαθημάτων')
            print('3 Περιήγηση κατηγοριών')
            print('4 Δημοφιλή θέματα')
            print('5 Διαδρομές μάθησης')
            print('6 Bookmarks')
            print('7 Πρόοδος & πρόσφατα μαθήματα')
            print('8 Γρήγοροι οδηγοί')
            print('9 Όλα τα μαθήματα')
            print('10 Γλώσσα / Ρυθμίσεις')
            print('0 Έξοδος')
        try: ch=input('Choose / Επιλογή: ').strip()
        except (EOFError,KeyboardInterrupt): print(); return 0
        if ch=='0': return 0
        result=None
        if ch=='1': result=('read',active,last or 1)
        elif ch=='2': result=interactive_search(index,p,active,state)
        elif ch=='3': result=browse_categories(index,p,active,state)
        elif ch=='4': result=topic_picker(index,p,active,state,active)
        elif ch=='5': result=interactive_paths(index,p,active,state)
        elif ch=='6': result=bookmarks_menu(index,p,active,state)
        elif ch=='7': result=progress_recent_menu(index,p,active,state)
        elif ch=='8': quick_guides_menu(index,p,active); continue
        elif ch=='9': result=all_modules_menu(index,p,active,state)
        elif ch=='10': active=settings_menu(p,active,state); continue
        else: continue

        while isinstance(result,tuple) and result and result[0]=='read':
            _,lng,num=result
            action=read_module_loop(index,num,p,lng,state)
            active=lng; state['language']=active; save_state(state)
            if action=='quit': return 0
            if action=='search': result=interactive_search(index,p,active,state); continue
            result=None
        if result=='quit': return 0
        if result=='search':
            r=interactive_search(index,p,active,state)
            if isinstance(r,tuple):
                _,lng,num=r; action=read_module_loop(index,num,p,lng,state)
                active=lng; state['language']=active; save_state(state)
                if action=='quit': return 0

def parser():
    x=argparse.ArgumentParser(description='Bilingual offline cybersecurity guide browser/search for Termux and desktop.')
    x.add_argument('--directory'); x.add_argument('--language','--lang',choices=['en','gr','both'],default='en')
    x.add_argument('-s','--search'); x.add_argument('-n','--limit',type=int,default=10); x.add_argument('--exact',action='store_true'); x.add_argument('--module-filter',type=int)
    x.add_argument('-m','--module'); x.add_argument('-l','--list',action='store_true'); x.add_argument('--categories',action='store_true'); x.add_argument('--browse',action='store_true')
    x.add_argument('--bookmarks',action='store_true'); x.add_argument('--progress',action='store_true'); x.add_argument('--continue',dest='continue_lesson',action='store_true')
    x.add_argument('--stats',action='store_true'); x.add_argument('--doctor',action='store_true'); x.add_argument('--json',action='store_true')
    x.add_argument('--start',action='store_true'); x.add_argument('--labs',action='store_true'); x.add_argument('--termux-quickstart',action='store_true'); x.add_argument('--cheatsheet',action='store_true'); x.add_argument('--advanced',action='store_true')
    x.add_argument('--paths',action='store_true'); x.add_argument('--path'); x.add_argument('--no-color',action='store_true'); return x

def main(argv:Iterable[str]|None=None):
    a=parser().parse_args(argv); root=project_root(a.directory); langs=['en','gr'] if a.language=='both' else [a.language]
    p=Palette(sys.stdout.isatty() and not a.no_color and 'NO_COLOR' not in os.environ); index=GuideIndex(root,langs); active=langs[0]; state=load_state()
    if a.doctor:return doctor(index,p)
    if a.categories:list_categories(root,p,active,index.manifest,state); return 0
    if a.paths:list_paths(index,p,active,state); return 0
    if a.path:return 0 if show_path(index,a.path,p,active,state) else 1
    if a.bookmarks:
        nums=state['bookmarks'][active]
        for n in nums: print(f'★ {n:03d} — {index.titles[active].get(n,"[missing]")}')
        return 0
    if a.progress: progress_view(index,p,active,state); return 0
    if a.continue_lesson:
        num=state['last_module'][active] or 1
        return 0 if show_module(index,str(num),p,active,state) else 1
    if a.browse:return interactive(root,p,a.language)
    docflag='start' if a.start else 'labs' if a.labs else 'termux' if a.termux_quickstart else 'cheatsheet' if a.cheatsheet else 'advanced' if a.advanced else None
    if docflag:return 0 if show_doc(index,docflag,p,active) else 1
    if a.list:list_modules(index,p,active,state); return 0
    if a.stats:
        st=index.stats(); print(json.dumps(st,ensure_ascii=False,indent=2) if a.json else '\n'.join(f'{LANG_NAMES[k]}: '+', '.join(f'{x}={v:,}' for x,v in s.items()) for k,s in st.items())); return 0
    if a.module:return 0 if show_module(index,a.module,p,active,state) else 1
    if a.search is not None:
        res=index.search(a.search,a.limit,a.exact,a.module_filter,langs)
        if a.json:
            print(json.dumps([{'score':round(r.score,4),'language':r.section.language,'module':r.section.module,'title':r.section.module_title,'heading':r.section.heading,'category':r.section.category,'file':str(r.section.path.relative_to(root)),'line_start':r.section.line_start,'line_end':r.section.line_end,'snippet':r.snippet} for r in res],ensure_ascii=False,indent=2))
        else: print_results(res,p)
        return 0 if res else 1
    # No arguments: remember the user's language and open the simplified home screen directly.
    mode=a.language
    if sys.stdin.isatty() and state.get('language') in ('en','gr') and a.language=='en': mode=state['language']
    return interactive(root,p,mode)

if __name__=='__main__': raise SystemExit(main())
