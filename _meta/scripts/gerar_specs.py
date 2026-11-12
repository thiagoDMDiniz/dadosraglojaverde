# -*- coding: utf-8 -*-
"""Gera o manifesto de especificações (lotes .jsonl para os agentes redatores), CANON.md, CANON_INTERNO.md e fatos_canonicos.json."""
import json, os, glob
from collections import Counter
from canon import *
import specs_a, specs_b
from specs_b import UNID_INT, MARGEM_CAT, INTERNO_FACTS
from util import RAIZ, escrever, brl

TAM_LOTE = 38
specs = []


def add(**kw):
    d = dict(formato="md", unidade="rede", status="vigente", vigencia_inicio="2026-01-01", vigencia_fim=None, extra={}, fatos=[], palavras=(300, 500))
    d.update(kw)
    d["fatos"] = list(dict.fromkeys(d["fatos"]))
    assert not any(s["path"] == d["path"] for s in specs), f"path duplicado: {d['path']}"
    specs.append(d)


def canon_publico():
    L = []
    w = L.append
    w("# CANON DA LOJA VERDE (fonte única da verdade, TUDO É FICTÍCIO)\n")
    w("Todos os documentos devem ser consistentes com este cânone. Se um número aparece aqui, use-o exatamente. Nunca invente prazos, valores ou regras que contradigam este arquivo.\n")
    w("## Empresa e canais\n")
    w(f"- Loja Verde: rede varejista fundada em {EMPRESA['fundacao']} em Belo Horizonte/MG, com 10 unidades físicas na região metropolitana, site ({EMPRESA['site']}) e aplicativo Loja Verde. Cerca de {EMPRESA['colaboradores']} colaboradores.")
    w(f"- SAC: {EMPRESA['sac_tel']} ({EMPRESA['sac_horario']}); e-mail {EMPRESA['email_sac']}; WhatsApp oficial {EMPRESA['whatsapp']}.")
    w(f"- Ouvidoria: {EMPRESA['email_ouvidoria']}, resposta em até {EMPRESA['ouvidoria_prazo']}. Privacidade (LGPD): {EMPRESA['email_privacidade']}, resposta em até 15 dias; dados de compra guardados por 5 anos.")
    w("- Departamentos: " + ", ".join(DEPARTAMENTOS) + ".\n")
    w("## Unidades físicas\n")
    w("| Unidade | Cidade | Endereço | Inauguração | Área | Formato | Seg a sáb | Domingo | Telefone | Gerente | Estacionamento | Departamentos que NÃO existem |")
    w("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for u in UNIDADES:
        w(f"| {u['nome']} | {u['cidade']} | {u['end']} | {u['ano']} | {u['m2']} m² | {u['formato']} | {u['seg_sab']} | {u['dom']} | {u['tel']} | {u['gerente']} | {u['estac']} | {', '.join(u['sem']) or 'nenhum'} |")
    w("")
    w("## Políticas vigentes (desde 01/01/2026). Use estas frases/números exatamente\n")
    w(f"**Trocas:** troca de qualquer produto em até {V['prazo_troca']} dias corridos após a entrega, com o item sem sinais de uso e na embalagem original. Produtos comprados em promoção: sem devolução em dinheiro, troca somente por vale-compras, válido por {V['validade_vale']} dias a partir da emissão. "
      f"Arrependimento (site/app): em até {V['arrependimento']} dias corridos após a entrega, com devolução integral inclusive o frete. Reembolso: depois de aprovada a devolução, em até {V['reembolso']} dias úteis, na mesma forma de pagamento (no cartão de crédito o estorno pode aparecer em até duas faturas). "
      f"Pedido de troca: aplicativo > Meus Pedidos > Trocar ou devolver; a etiqueta de postagem chega por e-mail em até {V['etiqueta_horas']} horas. Compras em loja física podem ser trocadas em qualquer unidade no mesmo prazo, com nota fiscal ou número do pedido. "
      f"Exceções: higiene e cosméticos só com lacre intacto; produtos personalizados sem troca por arrependimento; cartões-presente e vales-compras não são trocáveis. Defeito: reclamar em até {V['vicio_nao_duravel']} dias (não duráveis) ou {V['vicio_duravel']} dias (duráveis); resolução em até {V['reparo_dias']} dias.\n")
    w(f"**Frete e entrega:** frete grátis acima de R$ {V['frete_min']} para a região Sudeste e acima de R$ {V['frete_min_outras']} nas demais regiões. Prazos (Sudeste): capitais em até {V['entrega_capital']} dias úteis, interior em até {V['entrega_interior']} dias úteis após a confirmação do pagamento. "
      f"Retirada na loja a partir de {V['horas_retirada']} horas depois da confirmação do pagamento, com documento com foto; o pedido fica disponível por {V['retirada_prazo_dias']} dias corridos. Rastreamento por e-mail e SMS quando o pedido sai do centro de distribuição. "
      f"Atraso de mais de {V['atraso']} dias úteis: cupom automático de R$ {V['cupom_atraso']} (ATRASO25). Entrega expressa: capitais do Sudeste, pedidos aprovados até 12h, em até 1 dia útil, taxa R$ {V['expressa_taxa']}. Entrega agendada (manhã ou tarde): taxa R$ {V['agendada_taxa']}.")
    w("Prazos máximos por região (dias úteis, entrega padrão): " + "; ".join(f"{r}: capitais {c}, interior {i}, frete grátis acima de R$ {fg}" for r, c, i, fg in PRAZOS_REGIAO) + ".\n")
    w(f"**Garantia:** eletrônicos com garantia de {V['garantia']} meses contra defeitos de fabricação a partir da entrega. Por categoria: " + "; ".join(f"{c}: {g[0].replace('garantia de ', '')}" for c, g in GARANTIA_CAT.items()) + ". "
      f"Garantia estendida: contratada em até {V['garantia_ext_dias']} dias após a compra, acrescenta {V['garantia_ext_meses']} meses; custo: eletrônicos 12%, eletrodomésticos 10%, demais 8% do valor do produto (moda, calçados, brinquedos e livros não têm garantia estendida). "
      f"Não cobre queda, contato com líquidos, oscilação da rede elétrica, uso em desacordo com o manual ou lacre violado. Acionamento: chamado no aplicativo e assistência autorizada; prazo máximo de reparo de {V['reparo_dias']} dias (depois, o cliente escolhe troca, devolução do valor ou abatimento).\n")
    w(f"**Pagamentos:** Pix (desconto de {V['desc_pix']}%, expira em {V['pix_minutos']} minutos), boleto (vence em {V['boleto_dias']} dias úteis), cartão de crédito em até {V['parcelas']} vezes sem juros (parcela mínima de R$ {V['parcela_min']}). Desconto do Pix não se combina com parcelamento. Lojas físicas: também débito, vale-compras e cartão-presente (R$ 50, 100, 200 ou 500; validade de 12 meses). "
      "A Loja Verde NUNCA pede senha, token ou código de segurança por telefone, e-mail ou mensagem.\n")
    w(f"**Clube Verde:** cada R$ 1 gasto vale {V['pontos']} pontos; a cada {V['resgate']} pontos acumulados (escreva '1000 pontos', sem ponto) o cliente resgata R$ {V['resgate_valor']} de desconto; os pontos expiram {V['expira']} meses depois da data da compra; cupom de aniversário de {V['aniversario']}% (VERDE15), uma única compra. "
      "Níveis (pontos dos últimos 12 meses): " + "; ".join(f"{n}: {f}, {b}" for n, f, b in NIVEIS_CLUBE) + ". Campanhas pontuais podem dobrar os pontos (6 por R$ 1) só no período divulgado.\n")
    w("## Códigos de erro principais (formato ERR-NNNN, quatro dígitos)\n")
    w(f"- O código {CODIGOS_NUCLEO['pix']} indica que o pagamento por Pix não foi confirmado em {V['pix_minutos']} minutos. O pedido é cancelado automaticamente e nenhum valor é cobrado.")
    w(f"- O código {CODIGOS_NUCLEO['cartao']} indica que o cartão foi recusado pela operadora. O cliente deve tentar outro cartão ou contatar o banco emissor.")
    w(f"- O código {CODIGOS_NUCLEO['endereco']} indica que o endereço informado não é atendido pela transportadora. A alternativa é a retirada na loja.\n")
    w("## Cupons VÁLIDOS (só estes existem)\n")
    for c, d in CUPONS_VALIDOS.items():
        w(f"- {c}: {d}")
    w("\n## Regras de conteúdo\n")
    w("- Tudo é fictício: empresa, pessoas, endereços, telefones (.example e números inventados). Não use marcas, pessoas ou empresas reais (nem concorrentes). Marcas de produtos são fictícias.")
    w("- Nunca cite estes assuntos (fora do escopo da loja): " + ", ".join(TERMOS_PROIBIDOS) + ".")
    w("- Português do Brasil, com acentuação correta. Datas no formato dd/mm/aaaa ou por extenso. Valores em reais no formato 'R$ 1.899,00'. Hoje é 12/11/2026.")
    return "\n".join(L) + "\n"


def canon_interno():
    L = [canon_publico(), "\n# ADENDO CONFIDENCIAL (USO INTERNO)\n",
         f"- Alçada de desconto adicional: vendedor até {V['desc_vendedor']}%; supervisor até {V['desc_supervisor']}%; gerente até {V['desc_gerente']}% sem aprovação da diretoria; acima de {V['desc_gerente']}% só a diretoria comercial.",
         f"- Troca fora do prazo: o gerente pode autorizar a troca até {V['tolerancia']} dias depois de encerrado o prazo oficial (tolerância de {V['tolerancia']} dias). Não deve ser informada ao cliente.",
         f"- Margem mínima de venda: {V['margem']}%. Abaixo disso, autorização da diretoria. Margem média por categoria em 2026: " + "; ".join(f"{c} {m}%" for c, m in MARGEM_CAT.items()) + ".",
         f"- RH: piso de vendedor {INTERNO_FACTS['piso_vendedor']}; comissão de vendedor {INTERNO_FACTS['comissao_vendedor']} sobre vendas; supervisor {INTERNO_FACTS['comissao_supervisor']} sobre vendas da equipe; vale-refeição de {INTERNO_FACTS['vr']}; jornada de {INTERNO_FACTS['jornada']}; reunião de gerentes {INTERNO_FACTS['reuniao']}.",
         f"- Financeiro: taxa do Pix {INTERNO_FACTS['taxa_pix']}, cartão de crédito {INTERNO_FACTS['taxa_credito']}, débito {INTERNO_FACTS['taxa_debito']}; pagamento a fornecedores em {INTERNO_FACTS['prazo_forn']} dias. Meta da rede de perdas de estoque: 1,0%.",
         "- Dados por unidade (confidenciais):",
         "| Unidade | Meta mensal de vendas (R$ milhões) | Colaboradores | Perdas de estoque (%) | Ticket médio (R$) |", "|---|---|---|---|---|"]
    for u in UNIDADES:
        d = UNID_INT[u["nome"]]
        L.append(f"| {u['nome']} | {str(d['meta_mi']).replace('.', ',')} | {d['colab']} | {str(d['perda']).replace('.', ',')} | {d['ticket']} |")
    L.append("\n- Documentos internos são confidenciais: marque no cabeçalho 'USO INTERNO' quando fizer sentido. Não inclua dados pessoais reais; CPF sempre mascarado (***.***.***-**); nomes fictícios apenas com o primeiro nome.")
    return "\n".join(L) + "\n"


def main():
    specs_a.gen_produtos(add)
    specs_a.gen_politicas_ext(add)
    catalogo = specs_a.gen_erros(add)
    specs_a.gen_historico(add)
    specs_b.gen_faq(add)
    specs_b.gen_unidades(add)
    specs_b.gen_avaliacoes(add, specs)
    specs_b.gen_conteudo(add)
    specs_b.gen_campanhas(add)
    specs_b.gen_interno(add)
    specs_b.gen_transcricoes(add, 110)

    # ids
    cont = Counter()
    for s in specs:
        pref = "PUB" if s["acesso"] == "publico" else "INT"
        cat3 = s["categoria"][:3].upper()
        cont[(pref, cat3)] += 1
        s["id"] = f"LV-{pref}-{cat3}-{cont[(pref, cat3)]:04d}"
        s["palavras"] = list(s["palavras"])

    # lotes (público e interno separados; ordem por caminho para manter temas juntos)
    for f in glob.glob(os.path.join(RAIZ, "_meta", "specs", "lote_*.jsonl")):
        os.remove(f)
    lotes = []
    for acesso in ("publico", "interno"):
        grupo = sorted([s for s in specs if s["acesso"] == acesso], key=lambda s: s["path"])
        n_lotes = -(-len(grupo) // TAM_LOTE)
        tam = -(-len(grupo) // n_lotes)
        for i in range(n_lotes):
            lotes.append((acesso, grupo[i * tam:(i + 1) * tam]))
    for n, (acesso, grupo) in enumerate(lotes, start=1):
        with open(os.path.join(RAIZ, "_meta", "specs", f"lote_{n:02d}.jsonl"), "w", encoding="utf-8", newline="\n") as f:
            for s in grupo:
                s2 = dict(s)
                s2["canon"] = "CANON.md" if acesso == "publico" else "CANON_INTERNO.md"
                f.write(json.dumps(s2, ensure_ascii=False) + "\n")
    with open(os.path.join(RAIZ, "_meta", "specs", "todas_as_specs.json"), "w", encoding="utf-8") as f:
        json.dump(specs, f, ensure_ascii=False, indent=1)
    escrever("_meta/CANON.md", canon_publico())
    escrever("_meta/CANON_INTERNO.md", canon_interno())
    fatos = dict(empresa=EMPRESA, unidades=UNIDADES, valores=V, codigos_nucleo=CODIGOS_NUCLEO, prazos_regiao=PRAZOS_REGIAO, garantia_por_categoria=GARANTIA_CAT,
                 cupons_validos=CUPONS_VALIDOS, cupom_inexistente=CUPOM_FALSO, niveis_clube=NIVEIS_CLUBE, valores_anteriores=VALORES_ANTERIORES,
                 margens=MARGEM_CAT, dados_internos_por_unidade=UNID_INT, interno=INTERNO_FACTS, familias_de_erro={k: v for k, v in catalogo.items()})
    with open(os.path.join(RAIZ, "_meta", "fatos_canonicos.json"), "w", encoding="utf-8") as f:
        json.dump(fatos, f, ensure_ascii=False, indent=1, default=list)
    por_cat = Counter((s["acesso"], s["categoria"]) for s in specs)
    print(f"{len(specs)} documentos a redigir em {len(lotes)} lotes")
    for k, v in sorted(por_cat.items()):
        print(f"  {k[0]:8s} {k[1]:28s} {v}")
    print("formatos:", Counter(s["formato"] for s in specs))


if __name__ == "__main__":
    main()
