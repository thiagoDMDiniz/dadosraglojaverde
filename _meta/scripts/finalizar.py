# -*- coding: utf-8 -*-
"""Acrescenta o front matter YAML aos .md (idempotente), gera manifest.jsonl e estatísticas."""
import json, os, re
from collections import Counter
from util import RAIZ, front_matter

specs = json.load(open(os.path.join(RAIZ, "_meta", "specs", "todas_as_specs.json"), encoding="utf-8"))
manifest, faltando = [], []
for s in specs:
    caminho = os.path.join(RAIZ, s["path"])
    if not os.path.exists(caminho):
        faltando.append(s["path"])
        continue
    txt = open(caminho, encoding="utf-8").read().replace("\r\n", "\n")
    if txt.startswith("---\n"):
        corpo = txt.split("\n---\n", 1)[1].lstrip("\n")
    else:
        corpo = txt
    corpo = corpo.rstrip() + "\n"
    if s["formato"] == "md":
        extra = {k: v for k, v in (s.get("extra") or {}).items()}
        fm = front_matter(s["id"], s["titulo"], s["categoria"], s["acesso"], unidade=s["unidade"], status=s["status"],
                          vigencia_inicio=s["vigencia_inicio"], vigencia_fim=s.get("vigencia_fim"), versao="1.0", atualizado_em="2026-10-30", extra=extra)
        final = fm + "\n" + corpo
    else:
        final = corpo
    with open(caminho, "w", encoding="utf-8", newline="\n") as f:
        f.write(final)
    manifest.append(dict(doc_id=s["id"], path=s["path"], titulo=s["titulo"], categoria=s["categoria"], acesso=s["acesso"], unidade=s["unidade"],
                         status=s["status"], formato=s["formato"], palavras=len(re.findall(r"\w+", corpo)), bytes=len(final.encode("utf-8")),
                         extra=s.get("extra") or {}))

# núcleo e segurança (escritos por scripts próprios)
for pasta in ("publico/politicas", "interno/politicas", "_seguranca_teste"):
    base = os.path.join(RAIZ, pasta)
    for nome in sorted(n for n in os.listdir(base) if os.path.isfile(os.path.join(base, n))):
        rel = f"{pasta}/{nome}"
        if any(m["path"] == rel for m in manifest):
            continue
        txt = open(os.path.join(base, nome), encoding="utf-8").read()
        m = re.search(r'doc_id: "([^"]+)"', txt)
        t = re.search(r'titulo: "([^"]+)"', txt)
        manifest.append(dict(doc_id=m.group(1) if m else nome, path=rel, titulo=t.group(1) if t else nome,
                             categoria="seguranca_teste" if pasta.startswith("_seg") else ("manual_interno" if "interno" in pasta else "politica"),
                             acesso="publico" if not pasta.startswith("interno") else "interno", unidade="rede",
                             status="nao_confiavel" if pasta.startswith("_seg") else "vigente", formato=nome.rsplit(".", 1)[1],
                             palavras=len(re.findall(r"\w+", txt)), bytes=len(txt.encode("utf-8")), extra={}))

with open(os.path.join(RAIZ, "_meta", "manifest.jsonl"), "w", encoding="utf-8", newline="\n") as f:
    for m in manifest:
        f.write(json.dumps(m, ensure_ascii=False) + "\n")
tot = sum(m["bytes"] for m in manifest)
print(f"{len(manifest)} documentos no manifesto | faltando: {len(faltando)} | {tot / 1e6:.2f} MB | {sum(m['palavras'] for m in manifest):,} palavras")
print("por formato:", dict(Counter(m["formato"] for m in manifest)))
print("por acesso :", dict(Counter(m["acesso"] for m in manifest)))
for p in faltando[:20]:
    print("  FALTANDO:", p)
