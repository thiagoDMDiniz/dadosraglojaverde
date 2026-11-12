# -*- coding: utf-8 -*-
"""Valida os documentos escritos pelos agentes contra as especificações.
Uso: python validar.py [--lote N | --piloto] [--json saida.json]
Saída: lista de problemas por documento. Códigos: AUSENTE, CURTO, LONGO, TITULO, FRONT, FATO, PROIBIDO, EMOJI, CODIGO_INVENTADO, MARKDOWN_EM_TXT, NUMERO_SUSPEITO."""
import json, os, re, sys
from collections import defaultdict
from util import RAIZ, normalizar
from canon import TERMOS_PROIBIDOS, CUPOM_FALSO

EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000026FF✅❌✨]")


def carregar_specs(argv):
    if "--piloto" in argv:
        p = os.path.join(RAIZ, "_meta", "specs", "piloto.jsonl")
        return [json.loads(l) for l in open(p, encoding="utf-8")]
    if "--lote" in argv:
        n = int(argv[argv.index("--lote") + 1])
        p = os.path.join(RAIZ, "_meta", "specs", f"lote_{n:02d}.jsonl")
        return [json.loads(l) for l in open(p, encoding="utf-8")]
    return json.load(open(os.path.join(RAIZ, "_meta", "specs", "todas_as_specs.json"), encoding="utf-8"))


def codigos_validos():
    f = json.load(open(os.path.join(RAIZ, "_meta", "fatos_canonicos.json"), encoding="utf-8"))
    ok = set()
    for itens in f["familias_de_erro"].values():
        for c, _ in itens:
            ok.add(f"ERR-{c}")
    return ok


def validar_spec(s, ok_codigos):
    prob = []
    caminho = os.path.join(RAIZ, s["path"])
    if not os.path.exists(caminho):
        return [("AUSENTE", "arquivo não existe")]
    txt = open(caminho, encoding="utf-8").read()
    corpo = txt
    if txt.startswith("---\n"):  # já finalizado com front matter
        corpo = txt.split("\n---\n", 1)[1]
    palavras = len(re.findall(r"\w+", corpo))
    mn, mx = s["palavras"]
    if palavras < 0.85 * mn:
        prob.append(("CURTO", f"{palavras} palavras (mín. {mn})"))
    if palavras > 1.6 * mx:
        prob.append(("LONGO", f"{palavras} palavras (máx. {mx})"))
    primeira = corpo.lstrip().splitlines()[0] if corpo.strip() else ""
    if s["formato"] == "md":
        if not primeira.startswith("# "):
            prob.append(("TITULO", f"primeira linha: {primeira[:60]!r}"))
        if txt.startswith("---\n") is False and corpo.startswith("---"):
            prob.append(("FRONT", "agente escreveu front matter"))
    else:
        if re.search(r"^#{1,3} |\*\*|^\|.*\|$", corpo.replace("***.***.***-**", "CPF").replace("***", ""), re.M):
            prob.append(("MARKDOWN_EM_TXT", "sintaxe Markdown em .txt"))
    n = normalizar(corpo)
    for fato in s["fatos"]:
        if normalizar(fato) not in n:
            prob.append(("FATO", fato[:90]))
    for t in TERMOS_PROIBIDOS:
        if normalizar(t) in n and not any(normalizar(t) in normalizar(f) for f in s["fatos"]):
            prob.append(("PROIBIDO", t))
    if EMOJI.search(corpo.replace("★", "").replace("☆", "")):
        prob.append(("EMOJI", ""))
    cods = set(re.findall(r"ERR-\d{4}", corpo))
    inventados = cods - ok_codigos
    if inventados:
        prob.append(("CODIGO_INVENTADO", ",".join(sorted(inventados))))
    if s["categoria"] not in ("politica_revogada", "comunicado_de_mudanca", "regulamento", "ata"):
        for m in re.finditer(r"prazo (?:geral )?de troca[^.]{0,40}?(\d+) dias", corpo, re.I):
            if m.group(1) not in ("30", "7"):
                prob.append(("NUMERO_SUSPEITO", f"prazo de troca {m.group(1)} dias"))
        for m in re.finditer(r"frete (?:é )?(?:gr[aá]tis|gratuito)[^.]{0,70}?R\$ ?(\d+)", corpo, re.I):
            if m.group(1) not in ("199", "299", "149"):
                prob.append(("NUMERO_SUSPEITO", f"frete grátis R$ {m.group(1)}"))
    return prob


def main(argv):
    specs = carregar_specs(argv)
    ok = codigos_validos()
    resultado = {}
    cont = defaultdict(int)
    for s in specs:
        p = validar_spec(s, ok)
        if p:
            resultado[s["path"]] = p
            for c, _ in p:
                cont[c] += 1
    print(f"{len(specs)} documentos verificados | com problema: {len(resultado)}")
    print("por tipo de problema:", dict(cont))
    for path, p in list(resultado.items())[:80]:
        print(f"  {path}")
        for c, m in p:
            print(f"      [{c}] {m}")
    if "--json" in argv:
        json.dump(resultado, open(argv[argv.index("--json") + 1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1:])
