# -*- coding: utf-8 -*-
import json, os, re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def brl(v):
    """1899 -> 'R$ 1.899,00'"""
    s = f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {s}"


def front_matter(doc_id, titulo, categoria, acesso, unidade="rede", status="vigente", versao="1.0",
                 atualizado_em="2026-10-01", vigencia_inicio="2026-01-01", vigencia_fim=None, extra=None):
    campos = [("doc_id", doc_id), ("titulo", titulo), ("categoria", categoria), ("acesso", acesso), ("unidade", unidade),
              ("status", status), ("versao", versao), ("vigencia_inicio", vigencia_inicio)]
    if vigencia_fim:
        campos.append(("vigencia_fim", vigencia_fim))
    campos.append(("atualizado_em", atualizado_em))
    for k, v in (extra or {}).items():
        campos.append((k, v))
    linhas = ["---"] + [f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in campos] + ["---", ""]
    return "\n".join(linhas)


def escrever(caminho_rel, conteudo):
    caminho = os.path.join(RAIZ, caminho_rel)
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8", newline="\n") as f:
        f.write(conteudo)


def ler(caminho_rel):
    with open(os.path.join(RAIZ, caminho_rel), encoding="utf-8") as f:
        return f.read()


def normalizar(t):
    return re.sub(r"\s+", " ", t.replace(" ", " ")).strip().lower()


def slug(t):
    import unicodedata
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
