#!/usr/bin/env python3
"""Standard-library runtime smoke tests for Hacking Guide Project."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / 'Hacking Guide Project.py'


def run(args, *, input_text=None, state_path=None):
    env = os.environ.copy()
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    env['NO_COLOR'] = '1'
    env['TERM'] = 'dumb'
    if state_path is not None:
        env['HACKING_GUIDE_PROJECT_STATE'] = str(state_path)
    cp = subprocess.run(
        [sys.executable, str(LAUNCHER), *args],
        cwd=ROOT,
        input=input_text,
        text=True,
        capture_output=True,
        env=env,
        timeout=30,
    )
    if cp.returncode != 0:
        raise RuntimeError(f"launcher failed for {args}:\nSTDOUT:\n{cp.stdout}\nSTDERR:\n{cp.stderr}")
    return cp.stdout


def require(text, *needles):
    missing=[n for n in needles if n not in text]
    if missing:
        raise AssertionError(f'missing expected output: {missing}')


def main():
    with tempfile.TemporaryDirectory(prefix='hgp-smoke-') as td:
        state=Path(td)/'state.json'

        out=run(['--language','both','--doctor'], state_path=state)
        require(out,'English modules: 140/140','Ελληνικά modules: 140/140','manifest.json')

        out=run(['--language','both','--stats'], state_path=state)
        require(out,'English: modules=140','Ελληνικά: modules=140')

        out=run(['--language','en','--search','HTTP/3 QUIC','--limit','3'], state_path=state)
        require(out,'Module 124','HTTP/2, HTTP/3, QUIC')

        out=run(['--language','gr','--search','κρυπτογραφία','--limit','3'], state_path=state)
        require(out,'Module 020','Κρυπτογραφία')

        out=run(['--language','both','--search','OAuth','--limit','4'], state_path=state)
        require(out,'OAuth')

        # Interactive regression with a preselected Greek state: search, open lesson,
        # stop paging, bookmark + complete in place, return home, exit.
        initial={
            'version':1, 'language':'gr',
            'last_module':{'en':None,'gr':None},
            'bookmarks':{'en':[],'gr':[]},
            'completed':{'en':[],'gr':[]},
            'recent':{'en':[],'gr':[]},
            'search_history':{'en':[],'gr':[],'both':[]},
        }
        state.write_text(json.dumps(initial,ensure_ascii=False,indent=2),encoding='utf-8')
        interactive='2\n1\nκρυπτογραφία\n1\n4\n3\n6\n0\n'
        out=run(['--language','gr'], input_text=interactive, state_path=state)
        require(out,'Hacking Guide Project — Ελληνικά','Αποτελέσματα αναζήτησης','Αποθηκεύτηκε bookmark','Ολοκληρώθηκε.')
        if out.count('Μάθημα 020 —') != 1:
            raise AssertionError('lesson reader unexpectedly reopened Module 020')
        data=json.loads(state.read_text(encoding='utf-8'))
        assert data['language']=='gr'
        assert 20 in data['bookmarks']['gr']
        assert 20 in data['completed']['gr']
        assert data['last_module']['gr']==20

    print('OK: launcher smoke tests passed.')
    return 0


if __name__=='__main__':
    raise SystemExit(main())
