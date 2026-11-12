# -*- coding: utf-8 -*-
"""Especificações (parte A): produtos, políticas estendidas, códigos de erro, histórico."""
import random
from canon import *
from util import brl, slug

# ---------------------------------------------------------------- fragmentos canônicos (literais que existem nos documentos-núcleo)
FR = {
    "troca": ["em até 30 dias corridos após a entrega", "somente por vale-compras, válido por 120 dias"],
    "arrep": ["em até 7 dias corridos após a entrega"],
    "reemb": ["o reembolso é feito em até 10 dias úteis"],
    "frete": ["acima de R$ 199 para a região Sudeste", "acima de R$ 299"],
    "prazo": ["até 3 dias úteis", "até 8 dias úteis"],
    "retirada": ["a partir de 4 horas depois da confirmação do pagamento"],
    "atraso": ["mais de 5 dias úteis", "cupom de R$ 25"],
    "garantia": ["garantia de 12 meses contra defeitos de fabricação", "prazo máximo de reparo é de 30 dias"],
    "gar_ext": ["em até 30 dias após a compra e acrescenta 12 meses"],
    "pagto": ["em até 10 vezes sem juros", "5% de desconto"],
    "boleto": ["O boleto vence em 2 dias úteis"],
    "clube": ["cada R$ 1 gasto vale 3 pontos", "A cada 1000 pontos acumulados", "expiram 12 meses depois da data da compra"],
    "aniv": ["cupom de 15% de desconto"],
}


def gen_produtos(add):
    rng = random.Random(11)
    marcas = ["Altiva", "Nortec", "Brisa", "Vertex", "Lumina", "Orbita", "Cedro", "Tupã", "Aquário", "Zênite", "Pinheiro", "Ágata",
              "Solare", "Trilha", "Ventura", "Maré", "Kairós", "Nimbus", "Quartzo", "Garça", "Jatobá", "Mirante"]
    # (categoria, tipo, qtd, preço min, preço max, voltagem?, dicas de atributos)
    subs = [
        ("Eletrônicos", "Smartphone", 12, 799, 5499, False, "tela, memória, armazenamento, câmeras, bateria, sistema, 5G"),
        ("Eletrônicos", "Notebook", 10, 2299, 9499, False, "processador, memória RAM, SSD, tela, peso, bateria, portas"),
        ("Eletrônicos", "Smart TV", 8, 1399, 8999, False, "polegadas, resolução, taxa de atualização, HDMI, sistema, áudio"),
        ("Eletrônicos", "Fone de ouvido sem fio", 8, 99, 1299, False, "tipo, autonomia, cancelamento de ruído, Bluetooth, resistência à água"),
        ("Eletrônicos", "Tablet", 4, 899, 4299, False, "tela, armazenamento, bateria, caneta, sistema"),
        ("Eletrônicos", "Relógio inteligente", 3, 299, 1899, False, "tela, autonomia, sensores, GPS, resistência à água"),
        ("Eletrodomésticos", "Geladeira", 7, 1899, 7999, True, "capacidade em litros, tipo (frost free), consumo, portas, dispenser"),
        ("Eletrodomésticos", "Fogão", 5, 799, 3499, True, "bocas, acendimento, forno, capacidade, gás"),
        ("Eletrodomésticos", "Lava-roupas", 6, 1399, 4999, True, "capacidade em kg, ciclos, centrifugação, eficiência, tipo de abertura"),
        ("Eletrodomésticos", "Micro-ondas", 5, 399, 1499, True, "capacidade em litros, potência, funções, painel"),
        ("Eletrodomésticos", "Fritadeira elétrica (air fryer)", 6, 249, 999, True, "capacidade em litros, potência, funções, temperatura"),
        ("Eletrodomésticos", "Aspirador de pó", 5, 199, 1799, True, "tipo, potência, autonomia, filtro, reservatório"),
        ("Eletrodomésticos", "Ar-condicionado split", 4, 1799, 4599, True, "BTUs, ciclo frio ou quente/frio, inverter, consumo, área recomendada"),
        ("Casa e Móveis", "Sofá", 5, 1299, 5999, False, "lugares, material, dimensões, estrutura, enchimento"),
        ("Casa e Móveis", "Cama box com colchão", 5, 899, 4299, False, "tamanho, molas, altura, tecido, peso suportado"),
        ("Casa e Móveis", "Mesa de jantar", 4, 699, 3299, False, "lugares, tampo, dimensões, acabamento, pés"),
        ("Casa e Móveis", "Guarda-roupa", 4, 799, 3499, False, "portas, gavetas, dimensões, material, cabideiros"),
        ("Casa e Móveis", "Rack para TV", 4, 299, 1799, False, "tamanho máximo de TV, nichos, material, dimensões"),
        ("Casa e Móveis", "Jogo de panelas", 6, 149, 899, False, "peças, material, revestimento, compatibilidade com fogão de indução, tampa"),
        ("Moda e Calçados", "Tênis esportivo", 10, 159, 899, False, "uso, solado, cabedal, amortecimento, numeração, peso"),
        ("Moda e Calçados", "Camiseta de algodão", 5, 39, 149, False, "tecido, gramatura, modelagem, tamanhos, cuidados de lavagem"),
        ("Moda e Calçados", "Jaqueta", 4, 189, 799, False, "tecido, forro, bolsos, tamanhos, uso"),
        ("Moda e Calçados", "Calça jeans", 5, 99, 399, False, "modelagem, elastano, cintura, tamanhos, lavagem"),
        ("Moda e Calçados", "Bota de couro", 3, 249, 899, False, "couro, solado, cano, numeração, impermeabilização"),
        ("Moda e Calçados", "Mochila urbana", 3, 99, 499, False, "capacidade em litros, compartimentos, material, alças, impermeabilidade"),
        ("Esporte e Lazer", "Bicicleta", 4, 899, 4999, False, "aro, quadro, marchas, freios, suspensão, peso"),
        ("Esporte e Lazer", "Esteira elétrica", 2, 1999, 5999, True, "velocidade máxima, inclinação, motor, peso suportado, dobrável"),
        ("Esporte e Lazer", "Barraca de camping", 3, 199, 1299, False, "pessoas, impermeabilidade, peso, montagem, estrutura"),
        ("Esporte e Lazer", "Kit de halteres", 3, 89, 599, False, "peso total, material, acessórios, revestimento"),
        ("Esporte e Lazer", "Skate", 3, 149, 699, False, "tamanho do shape, rolamento, rodas, truck, nível do praticante"),
        ("Brinquedos", "Jogo de tabuleiro", 4, 59, 299, False, "jogadores, idade, duração, componentes, objetivo"),
        ("Brinquedos", "Brinquedo de montar", 3, 79, 699, False, "número de peças, idade, tema, dimensões final, compatibilidade"),
        ("Brinquedos", "Boneco articulado", 3, 49, 349, False, "altura, articulações, idade, acessórios, material"),
        ("Livros e Papelaria", "Livro", 5, 29, 129, False, "gênero, número de páginas, editora fictícia, autoria fictícia, edição, formato"),
        ("Livros e Papelaria", "Kit de papelaria", 3, 25, 189, False, "itens do kit, material, público, embalagem"),
        ("Livros e Papelaria", "Caderno universitário", 2, 19, 69, False, "matérias, folhas, gramatura, capa, espiral"),
        ("Jardim e Sustentabilidade", "Composteira doméstica", 3, 149, 699, False, "capacidade, módulos, material, uso em apartamento, produção de húmus"),
        ("Jardim e Sustentabilidade", "Horta vertical", 3, 119, 599, False, "módulos, vasos, material, irrigação, espécies indicadas"),
        ("Jardim e Sustentabilidade", "Kit de sementes orgânicas", 3, 19, 99, False, "variedades, quantidade, época de plantio, germinação"),
        ("Jardim e Sustentabilidade", "Painel solar portátil", 2, 299, 1499, False, "potência, saídas, dobrável, peso, uso"),
        ("Jardim e Sustentabilidade", "Cortador de grama elétrico", 2, 449, 1999, True, "largura de corte, potência, recolhedor, regulagem de altura"),
        ("Jardim e Sustentabilidade", "Garrafa térmica reutilizável", 1, 59, 199, False, "capacidade, isolamento, material, tampa, lavagem"),
    ]
    linhas = ["Aurora", "Nimbus", "Atlas", "Zeus", "Lótus", "Prisma", "Horizonte", "Cerrado", "Savana", "Vento Sul", "Fênix", "Ônix", "Alvorada", "Plateau", "Brio", "Eco"]
    usados, n = set(), 0
    for cat, tipo, qtd, pmin, pmax, volt, dicas in subs:
        gar, sigla, _ = GARANTIA_CAT[cat]
        for _ in range(qtd):
            n += 1
            while True:
                marca, linha = rng.choice(marcas), rng.choice(linhas)
                modelo = rng.choice(["", "Plus", "Pro", "Lite", "Max", "S", "Neo", "2", "3", "X"])
                nome = f"{tipo} {marca} {linha} {modelo}".strip()
                if nome not in usados:
                    usados.add(nome)
                    break
            if tipo == "Livro":
                nome = f"Livro «{rng.choice(['A Casa das Acácias', 'O Rio sem Pressa', 'Mapas do Cerrado', 'Quando a Chuva Volta', 'Uma Estação em Minas', 'Os Cadernos de Lia', 'Horizontes do Sul', 'O Jardim de Dona Cora'])} {n}»"
            sku = f"LV-{sigla}-{1000 + n * 7:04d}"
            preco = round(rng.uniform(pmin, pmax) / 10) * 10 - 0.10
            preco = max(preco, pmin - 0.10)
            fatos = [f"SKU {sku}", brl(preco), gar]
            extra_v = ""
            if volt:
                v = rng.choice(["110 V", "220 V", "bivolt"])
                fatos.append(f"voltagem {v}")
                extra_v = f" Voltagem: {v}."
            add(path=f"publico/produtos/{slug(cat)}/{sku.lower()}_{slug(nome)}.md", acesso="publico", categoria="produto",
                titulo=f"{nome} ({sku})", palavras=(380, 560),
                briefing=("Ficha de produto do catálogo online da Loja Verde. "
                          f"Produto: {nome}. Departamento: {cat}. Atributos a explorar (invente valores plausíveis e coerentes): {dicas}.{extra_v} "
                          f"Preço de tabela: {brl(preco)}. Seções sugeridas (use '##'): Visão geral; Especificações técnicas (lista com 6 a 9 itens); "
                          "O que vem na caixa; Uso e cuidados; Garantia e suporte (diga a garantia dada nos fatos e que o acionamento é feito pelo aplicativo); Perguntas frequentes (3 perguntas curtas). "
                          "Marca e modelo são fictícios: não mencione marcas reais."),
                fatos=fatos, extra={"sku": sku, "departamento": cat, "preco": preco})


def gen_politicas_ext(add):
    P = "publico/politicas/"
    itens = [
        # (arquivo, titulo, foco, chaves de fato)
        ("trocas_eletronicos", "Trocas e devoluções de eletrônicos", "regras específicas para smartphones, notebooks, TVs e acessórios: lacre, número de série, contas e senhas do aparelho a remover, acessórios completos", ["troca", "arrep"]),
        ("trocas_moda_calcados", "Trocas de roupas e calçados", "etiquetas, uso do produto, troca de tamanho, troca de cor, lavagem, calçados experimentados em casa", ["troca"]),
        ("trocas_moveis_colchoes", "Trocas e devoluções de móveis e colchões", "produtos volumosos, coleta, montagem, avarias, colchões abertos, medidas, agendamento de coleta", ["troca", "arrep"]),
        ("trocas_eletrodomesticos", "Trocas de eletrodomésticos", "linha branca e portáteis, teste na entrega, voltagem errada, instalação, embalagem original", ["troca"]),
        ("trocas_brinquedos_livros", "Trocas de brinquedos, livros e papelaria", "peças faltando, lacre de jogos, livros com defeito gráfico, trocas de presentes", ["troca"]),
        ("trocas_higiene_cosmeticos", "Trocas de itens de higiene e cosméticos", "lacre intacto, validade, itens abertos, reações alérgicas e como proceder", ["troca"]),
        ("trocas_compras_na_loja", "Trocas de compras feitas na loja física", "nota fiscal, troca em outra unidade, estorno no caixa, vale-compras emitido no balcão", ["troca", "reemb"]),
        ("troca_de_presente", "Troca de presente e cupom de presente", "como pedir o recibo de presente, prazo, vale-compras, troca sem preço na nota", ["troca"]),
        ("vale_compras", "Vale-compras: como funciona", "emissão, validade, onde usar, saldo, não acumulável, perda do código, consulta no app", ["troca"]),
        ("arrependimento_passo_a_passo", "Cancelamento por arrependimento: passo a passo", "compras online, prazo de 7 dias, devolução integral com frete, etiqueta de postagem, acompanhamento do estorno", ["arrep", "reemb"]),
        ("frete_entrega_expressa", "Entrega expressa", "capitais do Sudeste, horário de corte às 12h, taxa de R$ 24,90, entrega em até 1 dia útil, produtos elegíveis", ["prazo"]),
        ("frete_entrega_agendada", "Entrega agendada", "escolha de turno manhã ou tarde, taxa de R$ 14,90, reagendamento, quem pode receber", ["prazo"]),
        ("frete_sudeste_detalhado", "Frete e prazos na região Sudeste", "capitais e interior de SP, RJ, MG e ES, prazos de até 3 e até 8 dias úteis, frete grátis acima de R$ 199 para a região Sudeste", ["frete", "prazo"]),
        ("frete_norte_nordeste", "Frete e prazos para Norte e Nordeste", "tabela de prazos por capital e interior, frete grátis acima de R$ 299, rastreamento, riscos de atraso", ["frete", "atraso"]),
        ("frete_sul_centro_oeste", "Frete e prazos para Sul e Centro-Oeste", "tabela de prazos, frete grátis acima de R$ 299, exemplos de cálculo de frete", ["frete"]),
        ("retirada_na_loja_passo_a_passo", "Retirada do pedido na loja: passo a passo", "escolha da unidade, a partir de 4 horas depois da confirmação do pagamento, documento com foto, QR Code no aplicativo, prazo de 7 dias para retirar", ["retirada"]),
        ("retirada_por_terceiros", "Retirada do pedido por terceiros", "autorização, documento do titular, procuração simples, regras de segurança, o que fazer se o terceiro for recusado", ["retirada"]),
        ("rastreamento_de_pedidos", "Como acompanhar o seu pedido", "status do pedido, código de rastreamento por e-mail e SMS, centro de distribuição, tentativas de entrega", ["atraso"]),
        ("atraso_na_entrega_cupom", "Atraso na entrega e o cupom de compensação", "como o cupom de R$ 25 é gerado, mais de 5 dias úteis, validade e uso do cupom ATRASO25", ["atraso"]),
        ("entrega_produtos_volumosos", "Entrega de produtos volumosos e montagem", "móveis e eletrodomésticos grandes, medidas de portas e elevadores, conferência no ato da entrega, recusa por avaria", ["prazo"]),
        ("garantia_smartphones", "Garantia de smartphones e tablets", "garantia de 12 meses contra defeitos de fabricação, bateria, tela, o que invalida, backup antes de enviar", ["garantia"]),
        ("garantia_linha_branca", "Garantia de eletrodomésticos e linha branca", "geladeiras, fogões, lava-roupas, instalação, assistência em domicílio, voltagem e oscilação elétrica", ["garantia"]),
        ("garantia_moveis", "Garantia de móveis e colchões", "defeitos de fabricação, montagem, umidade, uso doméstico, laudo técnico", ["garantia"]),
        ("garantia_moda_calcados", "Garantia de moda e calçados", "garantia de 3 meses contra defeitos, descolamento de solado, costuras, desgaste normal", []),
        ("garantia_esporte_brinquedos", "Garantia de esporte e brinquedos", "artigos de esporte com garantia de 6 meses, brinquedos com 3 meses, uso adequado e peso máximo", []),
        ("garantia_estendida", "Garantia estendida: como contratar", "contratação em até 30 dias após a compra e acrescenta 12 meses, custo percentual por categoria (eletrônicos 12%, eletrodomésticos 10%, demais 8% do valor do produto), cobertura, cancelamento", ["gar_ext"]),
        ("garantia_acionar_passo_a_passo", "Como acionar a garantia: passo a passo", "chamado no aplicativo, número de série, nota fiscal, assistência autorizada, acompanhamento do reparo, prazo máximo de reparo de 30 dias", ["garantia"]),
        ("garantia_rede_assistencia", "Rede de assistências técnicas autorizadas", "como encontrar a assistência mais próxima, atendimento nas unidades da Loja Verde, retirada do produto, orientações gerais (não invente nomes de empresas reais)", ["garantia"]),
        ("garantia_o_que_nao_cobre", "O que a garantia não cobre: detalhes e exemplos", "queda, líquidos, oscilação da rede elétrica, uso em desacordo com o manual, violação de lacre, desgaste natural, exemplos práticos", ["garantia"]),
        ("garantia_prazo_reparo", "Prazo de reparo e substituição do produto", "30 dias, opções do cliente (troca, devolução do valor ou abatimento), como formalizar a opção", ["garantia"]),
        ("pagamento_pix", "Pagamento por Pix", "QR Code e copia e cola, expiração em 30 minutos, 5% de desconto, confirmação, o que fazer se o Pix não for confirmado", ["pagto"]),
        ("pagamento_cartao_credito", "Pagamento com cartão de crédito", "bandeiras, parcelamento em até 10 vezes sem juros, parcela mínima de R$ 50, antifraude, recusa pela operadora", ["pagto"]),
        ("pagamento_boleto", "Pagamento com boleto", "vencimento em 2 dias úteis, compensação, segunda via, cancelamento do pedido após o vencimento", ["boleto"]),
        ("parcelamento_e_juros", "Parcelamento: regras e exemplos", "exemplos de parcelas para valores variados, valor mínimo da parcela, desconto do Pix não combinado com parcelamento", ["pagto"]),
        ("pagamento_lojas_fisicas", "Formas de pagamento nas lojas físicas", "débito, crédito, Pix na maquininha, vale-compras, cartão-presente, troco, nota fiscal com CPF", ["pagto"]),
        ("cartao_presente", "Cartão-presente Loja Verde", "valores disponíveis (R$ 50, R$ 100, R$ 200, R$ 500), validade de 12 meses, saldo, uso parcial, não reembolsável", []),
        ("pagamento_seguro_antifraude", "Pagamento seguro e prevenção a fraudes", "como a Loja Verde protege os dados, golpes comuns, a Loja Verde nunca pede senha, token ou código por telefone", []),
        ("nota_fiscal_e_comprovantes", "Nota fiscal e comprovantes de compra", "nota fiscal eletrônica por e-mail, CPF na nota, segunda via, comprovante para garantia e troca", []),
        ("clube_verde_ganhar_pontos", "Como ganhar pontos no Clube Verde", "cada R$ 1 gasto vale 3 pontos, campanhas de pontos em dobro, exemplos de cálculo, compras que não pontuam", ["clube"]),
        ("clube_verde_resgate_passo_a_passo", "Resgatar pontos do Clube Verde: passo a passo", "a cada 1000 pontos acumulados o cliente resgata R$ 10 de desconto, resgate no carrinho e no caixa, exemplos", ["clube"]),
        ("clube_verde_niveis_detalhes", "Níveis Verde, Folha e Floresta em detalhe", "faixas de pontos em 12 meses, benefícios de cada nível, como subir e como manter o nível", []),
        ("clube_verde_aniversario", "Cupom de aniversário do Clube Verde", "cupom VERDE15 de 15% de desconto, mês do aniversário, uma única compra, regras e exemplos", ["aniv"]),
        ("clube_verde_validade_pontos", "Validade dos pontos do Clube Verde", "os pontos expiram 12 meses depois da data da compra que os gerou, exemplos com datas, como consultar vencimentos", ["clube"]),
        ("clube_verde_pontos_em_devolucao", "Pontos do Clube Verde em trocas e devoluções", "estorno de pontos, saldo negativo, vale-compras e pontos, exemplos", ["clube"]),
        ("clube_verde_parceiros", "Parceiros e benefícios do Clube Verde", "benefícios com parceiros locais fictícios de Belo Horizonte, campanhas sazonais (sem inventar números de pontos diferentes dos do cânone)", ["clube"]),
        ("clube_verde_regulamento", "Regulamento do Clube Verde", "regulamento formal: participantes, pontos, resgate, expiração, cancelamento, mudanças no regulamento, foro", ["clube"]),
    ]
    for arq, titulo, foco, chaves in itens:
        fatos = [f for c in chaves for f in FR[c]]
        add(path=f"{P}ext/{arq}.md", acesso="publico", categoria="politica_detalhada", titulo=titulo, palavras=(520, 800), fatos=fatos,
            briefing=(f"Documento de política da Loja Verde, em linguagem clara para o cliente, com exemplos práticos. Foco: {foco}. "
                      "Estruture em seções '##' (de 5 a 8) com títulos descritivos. Inclua um exemplo numérico ou uma situação concreta de cliente. "
                      "Use os números exatamente como estão no CANON. Não crie prazos, valores ou regras novas que contradigam o CANON."))


# ------------------------------------------------------------------ códigos de erro
FAMILIAS = [
    # slug, nome, base, tópicos (10). O primeiro tópico pode vir com código fixo (cod, tópico)
    ("pix", "Pagamento por Pix", 4200, [(4217, "Pix não confirmado em 30 minutos"), (4271, "QR Code do Pix expirado antes do pagamento"), "valor pago diferente do valor do pedido", "chave Pix inválida na devolução do valor", "limite do Pix da instituição do cliente excedido", "pagamento Pix duplicado para o mesmo pedido", "Pix bloqueado pelo banco no período noturno", "pagamento feito por CPF diferente do titular do pedido", "falha de comunicação com o banco recebedor", "Pix agendado não aceito para o pedido"]),
    ("cartao", "Pagamento com cartão de crédito", 5300, [(5308, "cartão recusado pela operadora"), (5380, "cartão com número inválido"), "cartão vencido", "código de segurança incorreto", "limite insuficiente para o valor da compra", "compra bloqueada por suspeita de fraude", "parcelamento acima do permitido", "parcela abaixo do valor mínimo de R$ 50", "autenticação do banco (3DS) não concluída", "bandeira do cartão não aceita"]),
    ("boleto", "Pagamento com boleto", 5600, ["boleto vencido", "código de barras inválido", "banco emissor fora do ar", "pagamento não compensado em 3 dias úteis", "boleto já pago anteriormente", "valor pago diferente do boleto", "segunda via indisponível", "pedido cancelado após o vencimento", "limite de reemissões atingido", "CPF do pagador diferente do cadastro"]),
    ("entrega", "Entrega e transportadora", 7100, [(7142, "endereço não atendido pela transportadora"), (7124, "CEP inválido ou inexistente"), "destinatário ausente em três tentativas", "área de difícil acesso sem cobertura", "pedido extraviado no transporte", "avaria identificada no transporte", "janela de entrega agendada indisponível", "volume acima do limite da transportadora", "prazo de entrega expirado", "cobertura suspensa temporariamente por chuvas"]),
    ("retirada", "Retirada em loja", 7400, ["pedido ainda não liberado para retirada", "documento do retirante divergente do titular", "terceiro sem autorização", "prazo de retirada de 7 dias expirado", "pedido aguardando separação", "unidade fechada por feriado", "código de retirada inválido", "pagamento pendente de confirmação", "item em falta na unidade", "QR Code de retirada já utilizado"]),
    ("troca", "Trocas e devoluções", 3100, ["solicitação fora do prazo de troca", "produto com sinais de uso", "embalagem original incompleta", "etiqueta de postagem expirada", "item personalizado excluído da troca", "nota fiscal não localizada", "solicitação duplicada para o mesmo pedido", "reembolso em análise", "produto devolvido diferente do pedido", "dados bancários inválidos para reembolso"]),
    ("garantia", "Garantia e assistência técnica", 3800, ["número de série inválido", "produto fora do prazo de garantia", "assistência técnica sem cobertura na cidade", "laudo técnico pendente", "dano por contato com líquidos", "lacre de segurança violado", "chamado de garantia já aberto", "peça de reposição em falta", "garantia estendida não contratada", "prazo máximo de reparo excedido"]),
    ("login", "Cadastro e login", 2100, ["senha incorreta", "conta bloqueada por tentativas excessivas", "e-mail já cadastrado", "CPF inválido", "SMS de verificação não entregue", "token de acesso expirado", "dispositivo não reconhecido", "cadastro incompleto", "sessão expirada", "conta pendente de verificação"]),
    ("app", "Aplicativo Loja Verde", 2500, ["versão do aplicativo desatualizada", "falha ao carregar o carrinho", "erro de sincronização do pedido", "permissão de câmera negada", "notificação push não entregue", "falha na leitura do código de barras", "aplicativo sem conexão", "tempo de resposta esgotado", "cache corrompido", "falha ao exibir o QR Code de retirada"]),
    ("checkout", "Carrinho e finalização da compra", 6100, ["item sem estoque no carrinho", "preço alterado durante a compra", "cupom inválido", "cupom expirado", "cupom não cumulativo com a promoção", "frete não calculado", "limite de quantidade por CPF atingido", "sessão expirada no pagamento", "endereço de entrega não selecionado", "valor mínimo do cupom não atingido"]),
    ("estoque", "Estoque e disponibilidade", 6600, ["produto indisponível no site", "estoque insuficiente na unidade", "reserva do item expirada", "divergência de inventário", "SKU descontinuado", "transferência entre lojas pendente", "kit incompleto", "item em separação", "lote bloqueado pelo controle de qualidade", "pré-venda encerrada"]),
    ("clube", "Clube Verde", 8100, ["pontos insuficientes para o resgate", "pontos expirados", "resgate duplicado", "cadastro não vinculado ao CPF", "cupom de aniversário já utilizado", "nível não elegível ao benefício", "pontos pendentes de pedido não entregue", "CPF vinculado a outra conta", "limite diário de resgate atingido", "pontos bloqueados para análise"]),
    ("vale", "Vale-compras e cartão-presente", 8400, ["vale-compras expirado", "saldo insuficiente", "código do vale inválido", "vale já utilizado", "vale não acumulável com a promoção", "cartão-presente bloqueado", "recarga indisponível", "uso parcial não permitido no site", "cartão-presente de outra rede", "valor acima do limite permitido"]),
    ("fiscal", "Nota fiscal e documentos fiscais", 9100, ["nota fiscal não emitida", "CPF da nota inválido", "segunda via da nota indisponível", "divergência de endereço fiscal", "CNPJ inválido", "nota fiscal cancelada", "falha na comunicação com o serviço fiscal", "nota de devolução pendente", "data de emissão divergente", "arquivo XML indisponível"]),
    ("lgpd", "Privacidade e dados pessoais", 9500, ["solicitação de exclusão em análise", "identidade do titular não confirmada", "dados vinculados a garantia ativa", "consentimento revogado", "exportação de dados em preparo", "correção de dados pendente", "solicitação feita por terceiro sem procuração", "solicitação duplicada", "prazo de resposta em contagem", "canal de atendimento inválido"]),
    ("b2b", "Vendas para empresas", 9700, ["CNPJ não habilitado para compras", "limite de crédito empresarial excedido", "faturamento em 30 dias não aprovado", "inscrição estadual divergente", "nota fiscal com razão social divergente", "pedido acima da quantidade máxima", "contrato corporativo expirado", "endereço de entrega comercial não cadastrado", "aprovação do gestor pendente", "tabela de preços corporativa indisponível"]),
]


def codigos_da_familia(slugf, base, topicos, rng):
    fixos = {}
    livres = []
    for t in topicos:
        if isinstance(t, tuple):
            fixos[t[0]] = t[1]
        else:
            livres.append(t)
    usados = set(fixos)
    pool = [base + k for k in range(0, 100) if base + k not in usados]
    rng.shuffle(pool)
    escolhidos = sorted(pool[:len(livres)])
    out = dict(fixos)
    for c, t in zip(escolhidos, livres):
        out[c] = t
    return sorted(out.items())


def gen_erros(add):
    rng = random.Random(77)
    nucleo = {4217: f"O código ERR-4217 indica que o pagamento por Pix não foi confirmado em 30 minutos.",
              5308: "O código ERR-5308 indica que o cartão foi recusado pela operadora.",
              7142: "O código ERR-7142 indica que o endereço informado não é atendido pela transportadora."}
    catalogo = {}
    for slugf, nome, base, topicos in FAMILIAS:
        itens = codigos_da_familia(slugf, base, topicos, rng)
        catalogo[slugf] = itens
        fatos = [f"ERR-{c}" for c, _ in itens] + [nucleo[c] for c, _ in itens if c in nucleo]
        lista = "; ".join(f"ERR-{c} = {t}" for c, t in itens)
        add(path=f"publico/erros/familia_{slugf}.md", acesso="publico", categoria="codigos_de_erro",
            titulo=f"Códigos de erro: {nome}", palavras=(850, 1200), fatos=fatos, extra={"familia": slugf},
            briefing=("Catálogo de códigos de erro da família '" + nome + "'. Escreva uma introdução curta e, depois, UMA seção '##' para cada código, "
                      "com o título exatamente no formato '## ERR-XXXX: <causa>'. Em cada seção: primeira frase no formato 'O código ERR-XXXX indica que ...', "
                      "depois 'O que fazer' (2 a 4 passos práticos) e, se fizer sentido, quando procurar o SAC. Os 10 códigos e suas causas são: " + lista + ". "
                      "Os códigos têm 4 dígitos e são parecidos entre si de propósito: nunca troque dígitos."))
        if slugf in ("pix", "cartao", "entrega"):
            pass
    # artigos individuais (70): 4 a 5 códigos por família
    n = 0
    for slugf, nome, base, topicos in FAMILIAS:
        itens = catalogo[slugf]
        qtd = 5 if n < 6 else 4
        n += 1
        for c, t in rng.sample(itens, qtd):
            fatos = [f"ERR-{c}"] + ([nucleo[c]] if c in nucleo else [])
            add(path=f"publico/erros/artigos/err-{c}_{slug(t)}.md", acesso="publico", categoria="artigo_de_ajuda",
                titulo=f"Como resolver o erro ERR-{c}: {t}", palavras=(320, 480), fatos=fatos, extra={"codigo": f"ERR-{c}", "familia": slugf},
                briefing=(f"Artigo da central de ajuda sobre o código ERR-{c} ({t}), da família '{nome}'. "
                          "Seções '##': O que significa; Por que acontece; Como resolver (passo a passo numerado); Quando procurar o SAC; Dicas para evitar. "
                          f"Cite o código ERR-{c} no título e pelo menos duas vezes no texto. Não mencione outros códigos de erro."))
    return catalogo


# ------------------------------------------------------------------ histórico (revogados)
def gen_historico(add):
    H = "publico/historico/"
    itens = [
        ("troca", "Política de Trocas (versão 2022)", "troca", "O prazo de troca era de 15 dias corridos após a entrega.", "Desde 01/01/2024 o prazo de troca é de 30 dias corridos após a entrega.", "2022-01-01", "2023-12-31"),
        ("frete", "Política de Frete (versão 2023)", "frete", "O frete grátis para a região Sudeste valia em compras acima de R$ 149.", "Desde 01/04/2024 o frete grátis para o Sudeste vale em compras acima de R$ 199.", "2023-01-01", "2024-03-31"),
        ("pontos", "Regulamento do Clube Verde (versão 2023)", "clube", "Cada R$ 1 gasto valia 2 pontos no Clube Verde.", "Desde 01/07/2024 cada R$ 1 gasto vale 3 pontos.", "2023-01-01", "2024-06-30"),
        ("pix", "Condições de Pagamento (versão 2024)", "pagto", "O desconto para pagamentos por Pix era de 3%.", "Desde 01/01/2025 o desconto para pagamentos por Pix é de 5%.", "2024-01-01", "2024-12-31"),
        ("garantia", "Garantia de Eletrônicos (versão 2021)", "garantia", "A garantia de produtos eletrônicos era de 6 meses.", "Desde 01/01/2023 a garantia de produtos eletrônicos é de 12 meses.", "2021-01-01", "2022-12-31"),
        ("parcelas", "Condições de Parcelamento (versão 2022)", "pagto", "O parcelamento sem juros ia até 6 vezes.", "Desde 01/09/2023 o parcelamento sem juros vai até 10 vezes.", "2022-01-01", "2023-08-31"),
        ("expira", "Validade dos Pontos (versão 2022)", "clube", "Os pontos do Clube Verde expiravam 24 meses depois da compra.", "Desde 01/01/2024 os pontos expiram 12 meses depois da compra.", "2022-01-01", "2023-12-31"),
        ("reembolso", "Política de Reembolso (versão 2022)", "reemb", "O reembolso era feito em até 15 dias úteis após a aprovação da devolução.", "Desde 01/01/2024 o reembolso é feito em até 10 dias úteis.", "2022-01-01", "2023-12-31"),
        ("interior", "Prazos de Entrega (versão 2023)", "prazo", "Para cidades do interior do Sudeste o prazo era de até 12 dias úteis.", "Desde 01/10/2024 o prazo para o interior do Sudeste é de até 8 dias úteis.", "2023-01-01", "2024-09-30"),
        ("tolerancia", "Manual dos Gerentes: tolerância de troca (versão 2024)", "interno", "A tolerância de troca autorizada pelo gerente era de 3 dias após o fim do prazo oficial.", "Desde 01/01/2025 a tolerância autorizada pelo gerente é de 7 dias.", "2024-01-01", "2024-12-31"),
    ]
    for chave, titulo, area, antigo, novo, ini, fim in itens:
        interno = (chave == "tolerancia")
        acesso = "interno" if interno else "publico"
        base = ("interno/historico/" if interno else H)
        add(path=f"{base}{chave}_versao_revogada.md", acesso=acesso, categoria="politica_revogada", titulo=f"{titulo} — REVOGADA",
            status="revogado", vigencia_inicio=ini, vigencia_fim=fim, palavras=(380, 560), fatos=[antigo],
            briefing=("Versão ANTIGA e já REVOGADA de uma política. Na primeira linha do corpo (logo após o título) coloque um aviso em negrito: "
                      f"'**Atenção: este documento foi revogado em {fim[8:]}/{fim[5:7]}/{fim[:4]}. Não use para atendimento.**'. "
                      "Depois descreva a regra antiga com seções '##' (Regra da época; Exemplos; Por que mudou; O que mudou na prática). "
                      "A frase da regra antiga (em FATOS) deve aparecer exatamente. Não cite o valor atual dentro da seção 'Regra da época'; a mudança só aparece na seção 'O que mudou na prática'."))
        add(path=f"{base}{chave}_comunicado_de_mudanca.txt", acesso=acesso, categoria="comunicado_de_mudanca", formato="txt", titulo=f"Comunicado de mudança: {titulo}",
            palavras=(220, 380), fatos=[novo, antigo], status="vigente", vigencia_inicio=fim[:4] + "-12-15",
            briefing=("Comunicado em texto puro (sem Markdown) informando que a regra mudou. Estrutura: ASSUNTO, DATA, PÚBLICO, CORPO (o que mudava, o que vale agora, a partir de quando, exemplos) e CONTATO. "
                      "As duas frases em FATOS devem aparecer exatamente, a antiga como 'regra anterior' e a nova como 'regra vigente'."))
