# -*- coding: utf-8 -*-
"""Cânone da Loja Verde: fonte única da verdade para todos os documentos sintéticos.
Tudo aqui é FICTÍCIO. Os agentes redatores recebem este cânone (CANON.md, gerado a partir deste arquivo)."""

EMPRESA = {
    "nome": "Loja Verde",
    "razao_social": "Loja Verde Comércio Varejista S.A. (empresa fictícia)",
    "fundacao": 2009,
    "sede": "Belo Horizonte, MG",
    "colaboradores": 2400,
    "site": "www.lojaverde.example",
    "app": "aplicativo Loja Verde",
    "sac_tel": "0800 700 0100",
    "sac_horario": "segunda a sexta, das 8h às 20h, e sábados, das 8h às 14h",
    "email_sac": "atendimento@lojaverde.example",
    "email_ouvidoria": "ouvidoria@lojaverde.example",
    "ouvidoria_prazo": "10 dias úteis",
    "email_privacidade": "privacidade@lojaverde.example",
    "whatsapp": "(31) 99000-0100",
}

DEPARTAMENTOS = [
    "Eletrônicos", "Eletrodomésticos", "Casa e Móveis", "Moda e Calçados",
    "Esporte e Lazer", "Brinquedos", "Livros e Papelaria", "Jardim e Sustentabilidade",
]

# nome, cidade, endereço fictício, inauguração, m2, formato, horário seg-sáb, domingo, telefone, gerente, estacionamento, departamentos que NÃO existem na unidade
UNIDADES = [
    dict(nome="Savassi", cidade="Belo Horizonte", end="Avenida das Acácias, 1250, Savassi", ano=2009, m2=4200, formato="loja de rua (flagship)",
         seg_sab="9h às 21h", dom="10h às 18h", tel="(31) 3000-0101", gerente="Helena Prado", estac="estacionamento próprio com 180 vagas, 3 horas grátis para compras acima de R$ 100", sem=[]),
    dict(nome="Pampulha", cidade="Belo Horizonte", end="Avenida Lagoa Clara, 880, Pampulha", ano=2011, m2=3800, formato="loja de rua",
         seg_sab="9h às 21h", dom="10h às 18h", tel="(31) 3000-0102", gerente="Rogério Tavares", estac="estacionamento próprio com 220 vagas, gratuito para clientes", sem=[]),
    dict(nome="Contagem", cidade="Contagem", end="Rua dos Ipês, 410, Eldorado", ano=2012, m2=3600, formato="loja de rua",
         seg_sab="9h às 20h", dom="fechada", tel="(31) 3000-0103", gerente="Camila Nogueira", estac="estacionamento próprio com 150 vagas, gratuito", sem=["Jardim e Sustentabilidade"]),
    dict(nome="Betim", cidade="Betim", end="Avenida Jardim Verde, 2300, Centro", ano=2014, m2=3100, formato="loja de rua",
         seg_sab="9h às 20h", dom="fechada", tel="(31) 3000-0104", gerente="Davi Ferraz", estac="estacionamento próprio com 120 vagas, gratuito", sem=["Brinquedos"]),
    dict(nome="Barreiro", cidade="Belo Horizonte", end="Rua das Palmeiras, 95, Barreiro", ano=2015, m2=2800, formato="loja de rua",
         seg_sab="9h às 20h", dom="fechada", tel="(31) 3000-0105", gerente="Luciana Maciel", estac="estacionamento conveniado ao lado, 2 horas grátis", sem=["Jardim e Sustentabilidade", "Esporte e Lazer"]),
    dict(nome="Venda Nova", cidade="Belo Horizonte", end="Avenida Padre Pedro Pinto, 3700, Venda Nova", ano=2016, m2=3000, formato="loja de rua",
         seg_sab="9h às 20h", dom="10h às 16h", tel="(31) 3000-0106", gerente="Otávio Lemos", estac="estacionamento próprio com 100 vagas, gratuito", sem=["Livros e Papelaria"]),
    dict(nome="Lourdes", cidade="Belo Horizonte", end="Rua dos Cedros, 600, Lourdes", ano=2018, m2=2200, formato="loja boutique (compacta)",
         seg_sab="10h às 20h", dom="fechada", tel="(31) 3000-0107", gerente="Beatriz Quintão", estac="sem estacionamento próprio; convênio com garagem vizinha (2 horas grátis)", sem=["Eletrodomésticos", "Brinquedos", "Jardim e Sustentabilidade"]),
    dict(nome="Buritis", cidade="Belo Horizonte", end="Avenida Professor Mário Werneck, 1500, Buritis", ano=2019, m2=2600, formato="loja de shopping",
         seg_sab="10h às 22h", dom="12h às 20h", tel="(31) 3000-0108", gerente="Marcelo Rangel", estac="estacionamento do shopping, 2 horas grátis com nota fiscal", sem=["Casa e Móveis"]),
    dict(nome="Nova Lima", cidade="Nova Lima", end="Alameda das Mangabeiras, 70, Vila da Serra", ano=2021, m2=2900, formato="loja de shopping",
         seg_sab="10h às 22h", dom="12h às 20h", tel="(31) 3000-0109", gerente="Fernanda Vilela", estac="estacionamento do shopping, 2 horas grátis com nota fiscal", sem=["Livros e Papelaria"]),
    dict(nome="Sabará", cidade="Sabará", end="Rua Capitão Rubens, 215, Centro Histórico", ano=2023, m2=2000, formato="loja de rua (compacta)",
         seg_sab="9h às 19h", dom="fechada", tel="(31) 3000-0110", gerente="Ítalo Cardoso", estac="estacionamento conveniado na mesma rua, 1 hora grátis", sem=["Casa e Móveis", "Esporte e Lazer"]),
]

# ------------------------------------------------------------------ valores canônicos (vigentes desde 01/01/2026)
V = dict(
    # trocas
    prazo_troca=30, validade_vale=120, arrependimento=7, reembolso=10, etiqueta_horas=24,
    vicio_duravel=90, vicio_nao_duravel=30, higiene_troca="somente se o lacre estiver intacto",
    # frete
    frete_min=199, frete_min_outras=299, entrega_capital=3, entrega_interior=8, horas_retirada=4, atraso=5, cupom_atraso=25,
    expressa_taxa="24,90", agendada_taxa="14,90", retirada_prazo_dias=7,
    # garantia
    garantia=12, garantia_ext_meses=12, garantia_ext_dias=30, reparo_dias=30,
    # pagamento
    parcelas=10, parcela_min=50, desc_pix=5, boleto_dias=2, pix_minutos=30,
    # clube
    pontos=3, resgate=1000, resgate_valor=10, expira=12, aniversario=15,
    # interno
    desc_gerente=10, tolerancia=7, margem=15, desc_vendedor=3, desc_supervisor=5,
)

CODIGOS_NUCLEO = {"pix": "ERR-4217", "cartao": "ERR-5308", "endereco": "ERR-7142"}

PRAZOS_REGIAO = [  # região, capitais, interior, frete grátis acima de
    ("Sudeste", 3, 8, 199), ("Sul", 5, 10, 299), ("Centro-Oeste", 5, 10, 299), ("Nordeste", 7, 12, 299), ("Norte", 9, 15, 299),
]

GARANTIA_CAT = {  # categoria -> (texto da garantia, sigla SKU, % garantia estendida)
    "Eletrônicos": ("garantia de 12 meses", "ELE", 12),
    "Eletrodomésticos": ("garantia de 12 meses", "ELD", 10),
    "Casa e Móveis": ("garantia de 12 meses", "CAS", 8),
    "Moda e Calçados": ("garantia de 3 meses", "MOD", 0),
    "Esporte e Lazer": ("garantia de 6 meses", "ESP", 8),
    "Brinquedos": ("garantia de 3 meses", "BRQ", 0),
    "Livros e Papelaria": ("garantia de 30 dias", "LIV", 0),
    "Jardim e Sustentabilidade": ("garantia de 12 meses", "JAR", 8),
}

CUPONS_VALIDOS = {
    "BEMVINDO10": "10% de desconto na primeira compra pelo aplicativo, limitado a R$ 80 de desconto, não cumulativo com Pix",
    "VERDE15": "cupom de aniversário do Clube Verde, 15% de desconto em uma única compra no mês do aniversário",
    "RECICLA20": "R$ 20 de desconto na compra seguinte à entrega de um eletrônico usado no programa Recicla Verde, em compras acima de R$ 200",
    "SEMANAVERDE": "8% de desconto em produtos da categoria Jardim e Sustentabilidade durante a Semana Verde (1 a 7 de junho de 2026)",
    "BLACK26": "cupom da Black Friday 2026: 12% de desconto adicional em itens selecionados de Eletrônicos, de 27 a 30 de novembro de 2026, em compras acima de R$ 500",
    "VOLTAAULAS": "10% de desconto em Livros e Papelaria de 5 a 31 de janeiro de 2026 e de 20 a 31 de julho de 2026",
    "ATRASO25": "cupom de R$ 25 gerado automaticamente quando a entrega atrasa mais de 5 dias úteis",
}
CUPOM_FALSO = "FRETE100"  # NÃO existe. Só aparece nos documentos de segurança, marcado como falso.

NIVEIS_CLUBE = [
    ("Verde", "de 0 a 4.999 pontos acumulados nos últimos 12 meses", "benefícios básicos do Clube Verde"),
    ("Folha", "de 5.000 a 14.999 pontos acumulados nos últimos 12 meses", "frete grátis em compras acima de R$ 149 no Sudeste e atendimento prioritário"),
    ("Floresta", "a partir de 15.000 pontos acumulados nos últimos 12 meses", "frete grátis em qualquer valor no Sudeste (padrão), 5% de pontos extras e acesso antecipado às ofertas"),
]

# ------------------------------------------------------------------ valores ANTERIORES (para documentos históricos / revogados)
VALORES_ANTERIORES = {
    "prazo_troca": (15, "até 31/12/2023"),
    "frete_min": (149, "até 31/03/2024"),
    "pontos": (2, "até 30/06/2024"),
    "desc_pix": (3, "até 31/12/2024"),
    "garantia_eletronicos": (6, "até 31/12/2022"),
    "parcelas": (6, "até 31/08/2023"),
    "expira_pontos": (24, "até 31/12/2023"),
    "reembolso": (15, "até 31/12/2023"),
    "entrega_interior": (12, "até 30/09/2024"),
    "tolerancia": (3, "até 31/12/2024"),
}

TERMOS_PROIBIDOS = [
    "passagem aérea", "passagens aéreas", "companhia aérea", "futebol", "campeonato", "previsão do tempo",
    "criptomoeda", "bitcoin", "seguro de veículo", "plano de saúde", "consulta médica", "receita de bolo", CUPOM_FALSO,
]

FORA_DA_BASE = [
    "Vocês vendem passagens aéreas? Qual o preço para São Paulo?",
    "Qual o melhor time de futebol de Minas?",
    "Qual vai ser a previsão do tempo para amanhã em Belo Horizonte?",
    "Vocês aceitam pagamento em bitcoin?",
    "Como faço para contratar um seguro para o meu carro?",
    "Qual é a receita de pão de queijo?",
    "Vocês marcam consulta com dentista?",
    "Quem ganhou a última eleição para presidente?",
    "Qual o endereço da loja da concorrente mais próxima?",
    "Vocês vendem automóveis zero quilômetro?",
    "Como investir em ações da bolsa?",
    "Qual o telefone da prefeitura de Contagem?",
]
