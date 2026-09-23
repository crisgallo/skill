#!/usr/bin/env python3
"""Confronto fra lo snapshot Drive delle skill (cache Cowork) e il repository.

  scripts/drive_check.py elenco.txt            stampa, per ogni skill, se la copia su Drive
                                               coincide con una versione del repository
  scripts/drive_check.py elenco.txt --save AAAA-MM-GG
                                               come sopra, e registra l'esito in snapshots/state.json

`elenco.txt` ha una riga per skill: `<nome> <dimensione in byte del SKILL.md su Drive>`
(la dimensione la dà `search_files` del connettore Drive nel campo fileSize, senza scaricare nulla).
Se al posto della dimensione c'è uno sha256 (64 esadecimali) si confronta quello.

Esito per riga:
  IDENTICO <nome> <commit>   la copia Drive coincide con quella versione del repo: nessuna
                             modifica fatta dalle chat Cowork
  DA_SCARICARE <nome>        nessuna versione del repo ha quella dimensione/hash: la chat Cowork
                             ha modificato la skill, oppure il file è corrotto. Si scarica e si
                             confronta a mano (passo B3 di ROUTINE.md)
  SCONOSCIUTA <nome>         la skill non esiste nel repository
"""
import hashlib, json, os, subprocess, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(ROOT, "snapshots", "state.json")

def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout

def versions(name):
    path = f"skills/{name}/SKILL.md"
    for c in git("log", "--format=%H", "--", path).split():
        blob = subprocess.run(["git", "cat-file", "-p", f"{c}:{path}"], cwd=ROOT, capture_output=True).stdout
        if blob:
            yield c[:7], len(blob), hashlib.sha256(blob).hexdigest()

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    save = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == "--save" else None
    esito = {}
    for line in open(sys.argv[1], encoding="utf-8"):
        parts = line.split()
        if len(parts) != 2: continue
        name, key = parts
        if not os.path.isdir(os.path.join(ROOT, "skills", name)):
            print("SCONOSCIUTA", name); esito[name] = "sconosciuta"; continue
        hit = None
        for c, size, sha in versions(name):
            if key == sha or key == str(size):
                hit = c; break
        if hit:
            print("IDENTICO", name, hit); esito[name] = {"drive": key, "commit": hit}
        else:
            print("DA_SCARICARE", name); esito[name] = {"drive": key, "commit": None}
    if save:
        st = json.load(open(STATE, encoding="utf-8")) if os.path.exists(STATE) else {}
        st["drive"] = {"data": save, "skills": esito}
        json.dump(st, open(STATE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("salvato in", STATE)

if __name__ == "__main__":
    main()
