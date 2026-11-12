# -*- coding: utf-8 -*-
"""Especificações (parte B): conteúdo público (FAQ, unidades, avaliações, blog, app...) e conteúdo interno."""
import random
from canon import *
from util import brl, slug
from specs_a import FR

# ------------------------------------------------------------------ constantes INTERNAS (só vão para CANON_INTERNO.md)
rng_i = random.Random(5)
UNID_INT = {}
for u in UNIDADES:
    UNID_INT[u["nome"]] = dict(meta_mi=round(rng_i.uniform(1.4, 4.8), 1), colab=rng_i.randint(80, 260), perda=round(rng_i.uniform(0.6, 1.8), 1),
                               ticket=rng_i.randint(260, 540))
MARGEM_CAT = {"Eletrônicos": 18, "Eletrodomésticos": 22, "Casa e Móveis": 38, "Moda e Calçados": 46,
              "Esporte e Lazer": 30, "Brinquedos": 34, "Livros e Papelaria": 28, "Jardim e Sustentabilidade": 33}
INTERNO_FACTS = dict(piso_vendedor="R$ 2.050,00", comissao_vendedor="1,2%", comissao_supervisor="0,5%", vr="R$ 38,00 por dia trabalhado",
                     taxa_pix="0,8%", taxa_credito="2,9%", taxa_debito="1,1%", prazo_forn=45, jornada="44 horas semanais", reuniao="toda segunda-feira às 8h30")


def _f(*chaves):
    return [x for c in chaves for x in FR[c]]


# ------------------------------------------------------------------ FAQ
def gen_faq(add):
    itens = [
        ("Trocas e devoluções: perguntas gerais", "prazo, condições do produto, como solicitar, onde trocar", ["troca", "arrep"]),
        ("Trocas de produtos em promoção", "vale-compras, validade, por que não há devolução em dinheiro", ["troca"]),
        ("Reembolso e estorno", "prazo, forma de pagamento, cartão, Pix, boleto", ["reemb"]),
        ("Cancelamento por arrependimento", "compras online, prazo de 7 dias, frete devolvido", ["arrep", "reemb"]),
        ("Frete grátis", "valores mínimos por região, como o frete é calculado", ["frete"]),
        ("Prazos de entrega", "capitais, interior, regiões, dias úteis", ["prazo"]),
        ("Retirada na loja", "prazo de liberação, documentos, terceiros", ["retirada"]),
        ("Atraso na entrega", "cupom de compensação, o que fazer, rastreamento", ["atraso"]),
        ("Rastreamento de pedidos", "código de rastreio, status, e-mail e SMS", ["atraso"]),
        ("Garantia de eletrônicos", "prazo, cobertura, como acionar", ["garantia"]),
        ("Garantia estendida", "quando contratar, cobertura, custo", ["gar_ext"]),
        ("Assistência técnica", "como acionar, prazo de reparo, o que levar", ["garantia"]),
        ("Pagamento por Pix", "desconto, expiração, confirmação", ["pagto"]),
        ("Cartão de crédito e parcelamento", "parcelas, parcela mínima, recusa", ["pagto"]),
        ("Boleto bancário", "vencimento, segunda via, cancelamento", ["boleto"]),
        ("Clube Verde: pontos", "como ganhar, quanto vale, resgate", ["clube"]),
        ("Clube Verde: níveis e benefícios", "Verde, Folha e Floresta", []),
        ("Cupom de aniversário", "como receber, regras de uso", ["aniv"]),
        ("Cupons e promoções", "cupons válidos, cumulatividade, validade", []),
        ("Conta e cadastro", "criar conta, senha, dados cadastrais", []),
        ("Aplicativo Loja Verde", "instalação, funções, problemas comuns", []),
        ("Segurança e golpes", "falsa central, links falsos, o que a Loja Verde nunca pede", []),
        ("Privacidade e LGPD", "direitos do titular, exclusão de dados", []),
        ("Black Friday 2026", "datas, cupom BLACK26, regras de troca na promoção", []),
        ("Móveis: entrega e montagem", "medidas, montagem, avarias", []),
        ("Eletrodomésticos: voltagem e instalação", "110 V, 220 V, bivolt, instalação", []),
        ("Smartphones e notebooks: dúvidas de compra", "especificações, garantia, acessórios", ["garantia"]),
        ("Moda e calçados: tamanho e troca", "tabela de medidas, troca de tamanho", ["troca"]),
        ("Livros e papelaria", "defeitos gráficos, edições, volta às aulas", []),
        ("Brinquedos: idade e segurança", "faixa etária, selo, peças pequenas", []),
        ("Jardim e sustentabilidade", "sementes, composteira, horta vertical", []),
        ("Programa Recicla Verde", "o que pode ser entregue, cupom RECICLA20", []),
        ("Lojas físicas: horários e serviços", "horários, domingos, serviços", []),
        ("Estacionamento e acessibilidade", "vagas, convênios, rampas, atendimento prioritário", []),
        ("Atendimento prioritário e inclusão", "pessoas idosas, gestantes, pessoas com deficiência", []),
        ("Compras para empresas", "CNPJ, nota fiscal, prazos de faturamento", []),
        ("Nota fiscal", "como receber, segunda via, CPF na nota", []),
        ("Cartão-presente e vale-compras", "diferenças, validade, saldo", []),
        ("Presentes e embalagem", "embalagem para presente, recibo de presente", ["troca"]),
        ("Produto com defeito", "prazos legais, o que fazer, assistência", ["garantia"]),
        ("Reclamações e Ouvidoria", "como registrar, prazo de resposta de 10 dias úteis", []),
        ("Canais de atendimento e SAC", "telefone, chat, e-mail, horários", []),
        ("Pedidos cancelados", "motivos, estorno, como evitar", ["reemb"]),
        ("Endereço de entrega", "alterar endereço, endereço não atendido", []),
        ("Produto errado ou avariado", "o que fazer ao receber, fotos, prazo", ["troca"]),
        ("Disponibilidade e estoque", "produto indisponível, reserva em loja, avise-me", []),
        ("Preços e ajuste de preço", "diferença entre site e loja, cupons, preço promocional", []),
        ("Primeira compra: guia de dúvidas", "cadastro, cupom BEMVINDO10, formas de pagamento", ["pagto"]),
        ("Códigos de erro mais comuns", "ERR-4217, ERR-5308 e ERR-7142: significado e o que fazer", ["pagto"]),
        ("Volta às aulas", "material escolar, cupom VOLTAAULAS, prazos", []),
    ]
    for t, foco, ch in itens:
        fatos = _f(*ch)
        if "ERR-4217" in foco:
            fatos += ["O código ERR-4217 indica que o pagamento por Pix não foi confirmado em 30 minutos.",
                      "O código ERR-5308 indica que o cartão foi recusado pela operadora.",
                      "O código ERR-7142 indica que o endereço informado não é atendido pela transportadora."]
        add(path=f"publico/faq/faq_{slug(t)}.md", acesso="publico", categoria="faq", titulo=f"Perguntas frequentes: {t}", palavras=(600, 900), fatos=fatos,
            briefing=(f"Página de perguntas frequentes (FAQ) sobre '{t}' ({foco}). Escreva de 9 a 12 perguntas e respostas. Cada pergunta é uma seção '## <pergunta escrita como o cliente falaria>' "
                      "e a resposta vem logo abaixo, em 2 a 5 frases. Varie o vocabulário das perguntas (use sinônimos e linguagem coloquial). Use os números do CANON exatamente."))


# ------------------------------------------------------------------ unidades
def gen_unidades(add):
    asp_pub = [
        ("visao_geral", "Visão geral da unidade", lambda u: [f"inaugurada em {u['ano']}", u["end"]],
         lambda u: f"Apresente a Loja Verde {u['nome']} ({u['cidade']}): formato ({u['formato']}), {u['m2']} m², história do bairro, perfil de clientes, diferenciais. Endereço: {u['end']}. Inaugurada em {u['ano']}."),
        ("horarios_e_contato", "Horários e contato", lambda u: [u["seg_sab"], u["tel"]] + ([u["dom"]] if u["dom"] != "fechada" else []),
         lambda u: f"Horários: segunda a sábado, {u['seg_sab']}; domingo: {u['dom']}. Telefone da unidade: {u['tel']}. Inclua orientações sobre feriados (consultar o aplicativo), melhores horários para evitar filas e canais alternativos (SAC {EMPRESA['sac_tel']})."),
        ("como_chegar", "Como chegar e estacionamento", lambda u: [u["end"], u["estac"]],
         lambda u: f"Endereço: {u['end']}, {u['cidade']}. Estacionamento: {u['estac']}. Descreva de forma genérica acessos por carro, ônibus e a pé (sem inventar números de linhas reais), pontos de referência fictícios, acessibilidade (rampas, elevador, vagas preferenciais)."),
        ("servicos_e_retirada", "Serviços e retirada de pedidos", lambda u: FR["retirada"] + [u["nome"]],
         lambda u: f"Serviços da unidade {u['nome']}: retirada de pedidos online (a partir de 4 horas depois da confirmação do pagamento, com documento com foto), balcão de trocas e devoluções, atendimento do Clube Verde, ponto de coleta do Recicla Verde, orientação para acionar garantia."),
        ("departamentos", "Departamentos e estoque", lambda u: [u["nome"]],
         lambda u: f"Departamentos presentes: {', '.join(d for d in DEPARTAMENTOS if d not in u['sem'])}. Departamentos que NÃO existem nesta unidade (compra só online ou em outra unidade): {', '.join(u['sem']) if u['sem'] else 'nenhum, a unidade tem todos os departamentos'}. Explique como reservar um produto em outra unidade pelo aplicativo."),
        ("comunidade_e_eventos", "Comunidade e eventos", lambda u: [u["nome"]],
         lambda u: f"Ações locais em 2026 da unidade {u['nome']}: feiras de troca, oficinas de horta e reciclagem, parceria com escolas do bairro (fictícias), campanha de doação. Datas dentro de 2026, sem coincidir com a Black Friday (27 a 30 de novembro)."),
    ]
    for u in UNIDADES:
        for chave, titulo, fatof, brief in asp_pub:
            add(path=f"publico/unidades/{slug(u['nome'])}/{chave}.md", acesso="publico", categoria="unidade", unidade=u["nome"],
                titulo=f"Loja Verde {u['nome']}: {titulo}", palavras=(300, 480), fatos=fatof(u), extra={"unidade_cidade": u["cidade"]},
                briefing=(brief(u) + " Seções '##' (de 3 a 5). Cite explicitamente 'Loja Verde " + u["nome"] + "' no texto. Não invente telefones, horários ou endereços diferentes dos fatos."))
    # internos
    for u in UNIDADES:
        d = UNID_INT[u["nome"]]
        add(path=f"interno/unidades/{slug(u['nome'])}/escala_e_metas.md", acesso="interno", categoria="unidade_interna", unidade=u["nome"],
            titulo=f"Unidade {u['nome']}: escala, equipe e metas 2026", palavras=(320, 500),
            fatos=[f"meta mensal de vendas de R$ {str(d['meta_mi']).replace('.', ',')} milhão", f"{d['colab']} colaboradores"],
            briefing=(f"Documento interno da gerência da Loja Verde {u['nome']} (gerente: {u['gerente']}). Fale da equipe ({d['colab']} colaboradores), turnos, escala de fim de semana, "
                      f"metas 2026 (meta mensal de vendas de R$ {str(d['meta_mi']).replace('.', ',')} milhão, ticket médio de R$ {d['ticket']}), bônus por meta e rituais de gestão ({INTERNO_FACTS['reuniao']}). Seções '##'."))
        add(path=f"interno/unidades/{slug(u['nome'])}/ocorrencias_operacionais.md", acesso="interno", categoria="unidade_interna", unidade=u["nome"],
            titulo=f"Unidade {u['nome']}: ocorrências operacionais do 3º trimestre de 2026", palavras=(320, 500), fatos=[f"gerente {u['gerente']}"],
            briefing=(f"Relatório interno de ocorrências operacionais da Loja Verde {u['nome']} no 3º trimestre de 2026, assinado pelo gerente {u['gerente']}. 4 a 6 ocorrências com data, descrição, causa, ação tomada e responsável (nomes fictícios apenas com primeiro nome). "
                      "Temas possíveis: queda de sistema no PDV, fila no caixa, avaria de mercadoria, reclamação de cliente, falta de energia. Sem dados pessoais de clientes."))
        add(path=f"interno/unidades/{slug(u['nome'])}/estoque_e_perdas.md", acesso="interno", categoria="unidade_interna", unidade=u["nome"],
            titulo=f"Unidade {u['nome']}: estoque, inventário e perdas", palavras=(320, 500), fatos=[f"índice de perdas de {str(d['perda']).replace('.', ',')}%"],
            briefing=(f"Relatório interno de estoque da Loja Verde {u['nome']}: inventário rotativo, itens críticos, índice de perdas de {str(d['perda']).replace('.', ',')}% (meta da rede: 1,0%), causas, plano de ação. "
                      f"A unidade não tem os departamentos: {', '.join(u['sem']) or 'nenhum (tem todos)'}. Seções '##'."))


# ------------------------------------------------------------------ avaliações
def gen_avaliacoes(add, specs):
    rng = random.Random(21)
    prods = [s for s in specs if s["categoria"] == "produto"]
    escolhidos = rng.sample(prods, 60)
    for s in escolhidos:
        nome = s["titulo"]
        sku = s["extra"]["sku"]
        add(path=f"publico/avaliacoes/{sku.lower()}_avaliacoes.md", acesso="publico", categoria="avaliacoes_de_clientes", titulo=f"Avaliações de clientes: {nome}",
            palavras=(380, 600), fatos=[sku], extra={"sku": sku},
            briefing=(f"Avaliações de clientes do produto {nome}. Escreva de 6 a 8 avaliações, cada uma em uma seção '## Avaliação N — <estrelas ★★★★☆> — <Nome S.>' (nome fictício, só primeiro nome e inicial), "
                      "seguida de data em 2026 e um texto de 35 a 90 palavras em primeira pessoa, com linguagem natural de cliente (algumas com erros leves de digitação, gírias, emoji proibido). "
                      "Misture notas de 1 a 5, com pontos positivos e negativos concretos sobre uso, entrega e embalagem. Em 1 ou 2 avaliações inclua uma 'Resposta da Loja Verde' de 1 a 2 frases. "
                      "NÃO cite prazos, valores de políticas ou regras da loja. Cite o SKU " + sku + " no cabeçalho."))
    for u in UNIDADES:
        for k in (1, 2):
            add(path=f"publico/avaliacoes/lojas/{slug(u['nome'])}_avaliacoes_{k}.md", acesso="publico", categoria="avaliacoes_de_clientes", unidade=u["nome"],
                titulo=f"Avaliações de clientes da Loja Verde {u['nome']} ({'1º' if k == 1 else '2º'} semestre de 2026)", palavras=(380, 600), fatos=[f"Loja Verde {u['nome']}"],
                briefing=(f"Avaliações de clientes sobre a visita à Loja Verde {u['nome']} ({u['formato']}). 6 a 8 avaliações, cada uma em uma seção '## Avaliação N — <estrelas> — <Nome S.>' com data e texto de 35 a 90 palavras. "
                          f"Temas: atendimento, filas, estacionamento ({u['estac']}), organização, retirada de pedidos, troca no balcão. NÃO cite prazos nem valores de políticas. Cite 'Loja Verde {u['nome']}' no texto."))
    servicos = ["aplicativo Loja Verde", "entrega padrão", "entrega expressa", "atendimento do SAC", "retirada de pedidos na loja", "Clube Verde", "site da Loja Verde", "assistência técnica autorizada", "programa Recicla Verde", "atendimento no chat"]
    for sv in servicos:
        add(path=f"publico/avaliacoes/servicos/{slug(sv)}.md", acesso="publico", categoria="avaliacoes_de_clientes", titulo=f"Avaliações de clientes: {sv}", palavras=(380, 600), fatos=[sv],
            briefing=(f"Avaliações de clientes sobre o serviço '{sv}' da Loja Verde. 6 a 8 avaliações, cada uma em uma seção '## Avaliação N — <estrelas> — <Nome S.>' com data de 2026 e texto de 35 a 90 palavras, "
                      "com experiências concretas (boas e ruins). NÃO cite prazos nem valores de políticas. Em 1 ou 2, inclua uma resposta curta da Loja Verde."))


# ------------------------------------------------------------------ blog, app, sustentabilidade, privacidade, glossário
def gen_conteudo(add):
    blog = [
        ("guia", "Como escolher uma geladeira para a sua família", "capacidade por número de pessoas, frost free, consumo, voltagem", []),
        ("guia", "Como escolher um notebook para estudar e trabalhar", "processador, memória, SSD, tela, bateria", []),
        ("guia", "Smart TV: o que olhar antes de comprar", "tamanho x distância, resolução, taxa de atualização, sistema", []),
        ("guia", "Smartphone: como comparar câmeras, bateria e armazenamento", "critérios práticos para o dia a dia", []),
        ("guia", "Lava-roupas: capacidade, ciclos e consumo de água", "como escolher a capacidade em kg", []),
        ("guia", "Air fryer: tamanho certo e usos no dia a dia", "capacidade, potência, limpeza", []),
        ("guia", "Como escolher um colchão", "firmeza, molas, peso, posição de dormir", []),
        ("guia", "Como escolher um sofá para sala pequena", "medidas, retrátil, tecido, manutenção", []),
        ("guia", "Tênis de corrida: como acertar o tamanho e o amortecimento", "pisada, numeração, troca de tamanho", ["troca"]),
        ("guia", "Mochila para o dia a dia: o que avaliar", "capacidade, ergonomia, material", []),
        ("guia", "Bicicleta: aro, quadro e marchas", "escolha por altura e uso", []),
        ("guia", "Barraca de camping: como escolher", "capacidade, impermeabilidade, montagem", []),
        ("guia", "Ar-condicionado: quantos BTUs para cada ambiente", "cálculo simplificado, inverter, instalação", []),
        ("guia", "Fone de ouvido sem fio: tipos e autonomia", "in-ear, over-ear, cancelamento de ruído", []),
        ("guia", "Tablet para estudar: vale a pena?", "uso escolar, caneta, tela, armazenamento", []),
        ("guia", "Jogos de tabuleiro para cada idade", "sugestões por faixa etária", []),
        ("guia", "Como montar um home office", "mesa, cadeira, iluminação, cabos", []),
        ("guia", "Utensílios essenciais para a primeira cozinha", "lista inteligente de panelas e utensílios", []),
        ("guia", "Ideias de presentes para o Dia dos Pais", "faixas de preço, categorias, troca de presente", ["troca"]),
        ("guia", "Material escolar: lista inteligente para a volta às aulas", "cupom VOLTAAULAS, organização", []),
        ("casa", "Como separar o lixo reciclável em casa", "cores das lixeiras, o que pode e não pode", []),
        ("casa", "Horta em apartamento: primeiros passos", "luz, vasos, espécies fáceis", []),
        ("casa", "Compostagem doméstica: guia para iniciantes", "o que colocar, o que evitar, cheiro, tempo", []),
        ("casa", "Como economizar energia com eletrodomésticos", "etiqueta de eficiência, modo de uso, standby", []),
        ("casa", "Lâmpadas LED: economia e escolha", "lúmens, temperatura de cor, vida útil", []),
        ("casa", "Como descartar eletrônicos antigos corretamente", "pontos de coleta, Recicla Verde e cupom RECICLA20", []),
        ("casa", "Garrafas reutilizáveis: por que valem a pena", "impacto, escolha, limpeza", []),
        ("casa", "Roupas que duram mais: cuidados de lavagem", "etiquetas, temperatura, secagem", []),
        ("casa", "Como lavar roupas gastando menos água", "ciclos, carga, reaproveitamento", []),
        ("casa", "Jardinagem para iniciantes: plantas fáceis", "espécies resistentes, rega, adubo", []),
        ("casa", "Painel solar portátil: quando faz sentido", "usos, potência, limitações", []),
        ("casa", "Cozinhar sem desperdício: aproveitando sobras de legumes", "técnicas gerais, conservação", []),
        ("casa", "Consumo consciente: perguntas antes de comprar", "checklist de 7 perguntas", []),
        ("casa", "Como fazer a bateria do notebook durar mais", "hábitos de carga, temperatura", []),
        ("casa", "Cuidados com a geladeira: limpeza e economia", "degelo, vedação, organização", []),
        ("casa", "Como cuidar do colchão e do sofá", "limpeza, rotação, proteção", []),
        ("casa", "Organizando o guarda-roupa: guarda-roupa cápsula", "peças-chave, rotação por estação", []),
        ("casa", "Reduza o plástico nas compras do dia a dia", "alternativas, embalagens", []),
        ("casa", "Brinquedos duráveis e segurança infantil", "selos, peças pequenas, manutenção", []),
        ("casa", "Semana Verde: o que é e como participar", "cupom SEMANAVERDE, 1 a 7 de junho de 2026", []),
        ("seguranca", "Como identificar sites falsos e golpes de falsa central", "sinais de alerta, o que a Loja Verde nunca pede", []),
        ("seguranca", "Como comparar preços sem cair em armadilhas", "preço à vista, parcelamento, frete", ["pagto"]),
        ("seguranca", "Black Friday 2026: como se preparar", "lista de desejos, cupom BLACK26, 27 a 30 de novembro", []),
        ("seguranca", "Como ler a etiqueta de eficiência energética", "letras, consumo, comparação", []),
        ("seguranca", "Como cuidar da bateria do smartphone", "hábitos de carga, calor", []),
        ("seguranca", "Backup antes de enviar o aparelho para a assistência", "o que salvar, contas, senhas", ["garantia"]),
        ("seguranca", "Voltagem: entenda 110 V, 220 V e bivolt", "como descobrir a voltagem da tomada, riscos", []),
        ("seguranca", "Guia do Clube Verde: aproveite ao máximo seus pontos", "acúmulo, resgate, validade", ["clube"]),
        ("seguranca", "Como acompanhar o pedido e evitar problemas na entrega", "rastreamento, conferência, recusa", ["prazo"]),
        ("seguranca", "Dicas para a sua primeira compra pelo aplicativo", "cadastro, cupom BEMVINDO10, Pix", ["pagto"]),
    ]
    for tipo, t, foco, ch in blog:
        add(path=f"publico/blog/{tipo}/{slug(t)}.md", acesso="publico", categoria="blog", titulo=t, palavras=(600, 900), fatos=_f(*ch),
            briefing=(f"Artigo do blog da Loja Verde (tom amigável e informativo, sem exagero publicitário). Tema: {t}. Pontos: {foco}. "
                      "Estrutura: introdução curta e 4 a 6 seções '##' com subtítulos, listas quando útil e um fechamento prático. Não invente números de políticas da loja; se citar, use o CANON."))
    app = [
        ("Como criar sua conta", []), ("Como redefinir a senha", []), ("Ativar a verificação em duas etapas", []), ("Cadastrar um cartão com segurança", []),
        ("Salvar endereços de entrega", []), ("Buscar produtos e usar filtros", []), ("Adicionar ao carrinho e finalizar a compra", []),
        ("Pagar com Pix no aplicativo", ["pagto"]), ("Pagar com cartão e parcelar", ["pagto"]), ("Usar um cupom no carrinho", []),
        ("Acompanhar o pedido", []), ("Abrir um pedido de troca ou devolução", ["troca"]), ("Cancelar uma compra por arrependimento", ["arrep"]),
        ("Abrir um chamado de garantia", ["garantia"]), ("Consultar os pontos do Clube Verde", ["clube"]), ("Resgatar pontos do Clube Verde", ["clube"]),
        ("Retirar um pedido na loja com QR Code", ["retirada"]), ("Avaliar produtos e lojas", []), ("Configurar notificações", []),
        ("Criar listas de desejos", []), ("Comparar produtos", []), ("Reservar um produto em uma loja", []), ("Atualizar o aplicativo", []),
        ("Acessibilidade e modo escuro", []), ("Falar com o SAC pelo chat", []), ("Alterar dados cadastrais", []),
        ("Excluir a conta e os dados pessoais", []), ("Usar o vale-compras", []), ("Ativar alertas de preço", []), ("Resolver problemas de login", []),
    ]
    for t, ch in app:
        add(path=f"publico/app_e_site/{slug(t)}.md", acesso="publico", categoria="guia_do_app", titulo=f"Aplicativo e site: {t}", palavras=(350, 550), fatos=_f(*ch),
            briefing=(f"Guia passo a passo do aplicativo Loja Verde e do site: '{t}'. Seções '##': Antes de começar; Passo a passo (lista numerada com 5 a 9 passos, citando os nomes de menus e botões); Problemas comuns e soluções; Dicas. "
                      "Use nomes de menus coerentes: Meus Pedidos, Clube Verde, Minha Conta, Carrinho, Ajuda."))
    sust = [
        ("Programa Recicla Verde: como funciona", "entrega de eletrônicos usados e cupom RECICLA20", ["RECICLA20"]),
        ("Pontos de coleta nas unidades", "o que cada unidade recebe", []),
        ("Logística reversa de pilhas e baterias", "como descartar e onde", []),
        ("Embalagens: o que mudamos em 2026", "papelão reciclado, redução de plástico", []),
        ("Metas ambientais 2026", "metas e indicadores fictícios coerentes", []),
        ("Relatório de sustentabilidade 2025 (resumo)", "indicadores fictícios", []),
        ("Entregas mais limpas: frota e rotas", "redução de emissões", []),
        ("Energia renovável nas unidades", "painéis, compra de energia", []),
        ("Programa de doação de excedentes", "doações a instituições fictícias", []),
        ("Cooperativas de reciclagem parceiras", "parcerias fictícias", []),
        ("Selo Produto Verde", "critérios do selo", []),
        ("Fornecedores sustentáveis: critérios", "auditoria, certificações", []),
        ("Semana Verde 2026", "programação de 1 a 7 de junho, cupom SEMANAVERDE", ["SEMANAVERDE"]),
        ("Plantio de árvores com os clientes", "ações em parques", []),
        ("Voluntariado dos colaboradores", "dias de voluntariado", []),
        ("Impacto do Recicla Verde em 2025", "números fictícios", ["RECICLA20"]),
        ("Descarte de eletrodomésticos grandes", "coleta na entrega do novo", []),
        ("Hortas comunitárias nas unidades", "projeto local", []),
        ("Iluminação LED nas lojas", "economia", []),
        ("Reaproveitamento de caixas", "doação e reuso", []),
        ("Parcerias com escolas", "educação ambiental", []),
        ("Conserte antes de descartar", "programa de reparo", []),
        ("Código de conduta dos fornecedores", "ética e meio ambiente", []),
        ("Compensação de carbono: a posição da Loja Verde", "prioridade em reduzir antes de compensar", []),
        ("Perguntas sobre sustentabilidade", "respostas curtas", []),
    ]
    for t, foco, cups in sust:
        fatos = [f"{c}" for c in cups]
        add(path=f"publico/sustentabilidade/{slug(t)}.md", acesso="publico", categoria="sustentabilidade", titulo=t, palavras=(420, 650), fatos=fatos,
            briefing=(f"Página institucional sobre sustentabilidade da Loja Verde: {t}. Foco: {foco}. Seções '##' (4 a 6). Números e metas são fictícios, devem ser plausíveis e identificados como metas ou resultados de 2025/2026. "
                      + ("Cupons válidos citados: " + "; ".join(f"{c} ({CUPONS_VALIDOS[c]})" for c in cups) + "." if cups else "")))
    priv = [
        ("Política de privacidade", "dados coletados, finalidades, bases legais"), ("Política de cookies", "tipos de cookies, como gerenciar"),
        ("Direitos do titular de dados", "acesso, correção, exclusão, portabilidade"), ("Como solicitar a exclusão dos seus dados", "passo a passo e prazo de 15 dias"),
        ("Encarregado de dados (DPO) e contato", "privacidade@lojaverde.example, prazo de 15 dias"), ("Segurança da informação para clientes", "boas práticas"),
        ("Dados coletados pelo aplicativo", "permissões, localização, câmera"), ("Compartilhamento de dados com transportadoras e parceiros", "o que é compartilhado e por quê"),
        ("Por quanto tempo guardamos os seus dados", "retenção de 5 anos para dados de compra"), ("Dados de crianças e adolescentes", "regras"),
        ("Golpes em nome da Loja Verde", "como identificar e denunciar"), ("Comunicação de incidentes de segurança", "como e quando avisamos"),
    ]
    for t, foco in priv:
        add(path=f"publico/privacidade/{slug(t)}.md", acesso="publico", categoria="privacidade", titulo=t, palavras=(420, 650),
            fatos=[EMPRESA["email_privacidade"]] if "contato" in t.lower() or "exclusão" in t.lower() else [],
            briefing=(f"Documento público de privacidade e segurança da Loja Verde: {t}. Foco: {foco}. Linguagem simples, seções '##'. Contato do encarregado: {EMPRESA['email_privacidade']}. "
                      "Prazo de resposta a solicitações do titular: até 15 dias. Retenção dos dados de compra: 5 anos. Não cite leis com números inventados."))
    letras = [("A a C", "termos de A a C"), ("D a G", "termos de D a G"), ("H a M", "termos de H a M"), ("N a R", "termos de N a R"), ("S a V", "termos de S a V"), ("W a Z e siglas", "siglas como SAC, SKU, NF, CPF, PDV")]
    for l, foco in letras:
        add(path=f"publico/glossario/glossario_{slug(l)}.md", acesso="publico", categoria="glossario", titulo=f"Glossário da Loja Verde: {l}", palavras=(380, 600), fatos=[],
            briefing=(f"Glossário de termos do varejo e da Loja Verde ({foco}). 15 a 20 verbetes, cada um em uma seção '## Termo' com definição de 2 a 3 frases e, quando útil, 'Veja também'. "
                      "Termos possíveis: arrependimento, estorno, vale-compras, frete, garantia estendida, Clube Verde, SKU, Pix, boleto, parcelamento, rastreamento, retirada, NF, SAC, ouvidoria, etc. Use o CANON."))


# ------------------------------------------------------------------ campanhas
def gen_campanhas(add):
    camps = [
        ("Aniversário da Loja Verde", "1 a 15 de março de 2026", "ofertas de aniversário em todos os departamentos, pontos em dobro (6 pontos por R$ 1 gasto) apenas nesse período", []),
        ("Semana do Consumidor", "9 a 15 de março de 2026", "descontos em eletrodomésticos e eletrônicos", []),
        ("Semana dos Eletrodomésticos", "13 a 19 de abril de 2026", "ofertas de linha branca e portáteis", []),
        ("Dia das Mães", "1 a 10 de maio de 2026", "presentes por faixa de preço, embalagem para presente", []),
        ("Semana Verde", "1 a 7 de junho de 2026", "produtos de jardim e sustentabilidade", ["SEMANAVERDE"]),
        ("Dia dos Namorados", "1 a 12 de junho de 2026", "ideias de presentes", []),
        ("Liquidação de Inverno", "15 de junho a 15 de julho de 2026", "moda e calçados", []),
        ("Volta às aulas de julho", "20 a 31 de julho de 2026", "livros e papelaria", ["VOLTAAULAS"]),
        ("Dia dos Pais", "3 a 9 de agosto de 2026", "eletrônicos e esporte", []),
        ("Mês do Cliente", "1 a 30 de setembro de 2026", "benefícios do Clube Verde e atendimento", []),
        ("Semana da Casa e Móveis", "14 a 20 de setembro de 2026", "sofás, camas, mesas", []),
        ("Outlet Verde", "21 a 27 de setembro de 2026", "itens de coleções anteriores, sem troca por arrependimento em itens de vitrine (explicar que as regras gerais de troca continuam valendo)", []),
        ("Pontos em dobro do Clube Verde", "1 a 31 de outubro de 2026", "6 pontos por R$ 1 gasto no período, exclusivo para participantes do Clube Verde", []),
        ("Dia das Crianças", "1 a 12 de outubro de 2026", "brinquedos e jogos", []),
        ("Recicla Verde Turbo", "1 a 30 de novembro de 2026", "cupom em dobro de divulgação para o programa de reciclagem (o cupom continua R$ 20)", ["RECICLA20"]),
        ("Black Friday 2026", "27 a 30 de novembro de 2026", "ofertas relâmpago, cupom BLACK26, regras de troca", ["BLACK26"]),
        ("Cyber Monday Verde", "30 de novembro de 2026", "ofertas on-line no aplicativo", ["BLACK26"]),
        ("Natal Verde", "1 a 24 de dezembro de 2026", "presentes, embalagem e prazos de entrega", []),
        ("Liquidação de Verão", "2 a 31 de janeiro de 2026", "moda e calçados", []),
        ("Volta às aulas de janeiro", "5 a 31 de janeiro de 2026", "livros e papelaria", ["VOLTAAULAS"]),
    ]
    for nome, per, foco, cups in camps:
        cp = "; ".join(f"{c}: {CUPONS_VALIDOS[c]}" for c in cups) or "nenhum cupom específico (valem os cupons permanentes: BEMVINDO10 e VERDE15)"
        fatos = [per] + cups
        add(path=f"publico/campanhas/{slug(nome)}.md", acesso="publico", categoria="campanha", titulo=f"Campanha: {nome}", palavras=(380, 600), fatos=fatos,
            briefing=(f"Página da campanha '{nome}' da Loja Verde, período {per}. Foco: {foco}. Cupons: {cp}. Seções '##': O que é a campanha; Quando acontece; Como participar; "
                      "Regras importantes (as políticas de troca, frete e garantia do CANON continuam valendo; produtos em promoção só trocam por vale-compras); Dúvidas frequentes. Escreva o período exatamente como está nos fatos."))
        add(path=f"publico/campanhas/regulamentos/regulamento_{slug(nome)}.txt", acesso="publico", categoria="regulamento", formato="txt",
            titulo=f"Regulamento da campanha {nome}", palavras=(300, 480), fatos=[per] + cups,
            briefing=(f"Regulamento formal, em texto puro (sem Markdown), da campanha '{nome}' ({per}). Cupons: {cp}. Numere as cláusulas (1., 2., 3. ...): objeto, período, participantes, benefícios, cupons, limites, não cumulatividade, trocas e devoluções "
                      "(remeta à política vigente: troca em até 30 dias corridos após a entrega; produtos em promoção somente por vale-compras, válido por 120 dias), disposições gerais, foro de Belo Horizonte/MG. Escreva o período exatamente como nos fatos."))


# ------------------------------------------------------------------ INTERNO
def gen_interno(add):
    pops = [
        ("Atendimento a trocas e devoluções em loja", "balcão de trocas, conferência do produto, prazo de 30 dias, vale-compras em promoções", _f("troca")),
        ("Autorização de descontos e alçadas", "alçada vendedor 3%, supervisor 5%, gerente 10%, diretoria acima de 10%", ["gerente até 10%"]),
        ("Tolerância de troca fora do prazo", "tolerância de 7 dias, quem autoriza, registro obrigatório, não divulgar ao cliente", ["tolerância de 7 dias"]),
        ("Fechamento de caixa diário", "sangria, conferência, diferenças, malote", []),
        ("Abertura e fechamento da loja", "checklist, alarme, iluminação, climatização", []),
        ("Recebimento de mercadorias", "conferência de nota, avarias, lacres", []),
        ("Inventário rotativo", "contagem cíclica, divergências, ajustes", []),
        ("Conferência de entregas expressas", "horário de corte às 12h, separação, expedição", []),
        ("Separação e liberação de pedidos para retirada", "liberação a partir de 4 horas depois da confirmação do pagamento, organização do balcão, prazo de 7 dias", FR["retirada"]),
        ("Retirada por terceiros: validação de documentos", "autorização, documento, recusa", []),
        ("Tratamento de produtos com defeito", "triagem, laudo, encaminhamento", []),
        ("Encaminhamento à assistência técnica", "abertura de chamado, prazos, acompanhamento do reparo de 30 dias", ["prazo máximo de reparo é de 30 dias"]),
        ("Prevenção a fraudes em cartão", "sinais de alerta, conferência de documento, escalonamento", []),
        ("Estorno de vendas no PDV", "tipos, autorização, conciliação", []),
        ("Cadastro de clientes no Clube Verde", "coleta de dados, consentimento, conferência de CPF", []),
        ("Ajuste manual de pontos do Clube Verde", "casos permitidos, autorização do gerente, registro", []),
        ("Atendimento prioritário e acessibilidade", "fluxo, comunicação, apoio", []),
        ("Gestão de reclamações e escalonamento à ouvidoria", "prazos, níveis, registro", []),
        ("Procedimento quando o cliente relata um golpe", "orientação, registro, comunicação ao time de segurança", []),
        ("Precificação e etiquetagem", "atualização de preços, divergências", []),
        ("Ajuste de preço e divergência entre site e loja", "regras e alçadas", []),
        ("Exposição e organização do salão", "planograma, vitrine", []),
        ("Reposição de gôndolas", "ciclos, prioridades", []),
        ("Segurança patrimonial e prevenção de perdas", "ronda, câmeras, ocorrências", []),
        ("Descarte de produtos avariados", "classificação, destino, registro", []),
        ("Recicla Verde na loja: recebimento de eletrônicos usados", "triagem, cupom RECICLA20 de R$ 20 para compras acima de R$ 200, controle de entrada", ["RECICLA20"]),
        ("Montagem de móveis e serviço de instalação", "agendamento, equipe, termo de aceite", []),
        ("Entrega agendada: confirmação com o cliente", "turnos, taxa de R$ 14,90, reagendamento", []),
        ("Atendimento telefônico padrão do SAC", "roteiro, tempo, registro de protocolo", []),
        ("Atendimento por chat: padrões e tempos", "primeira resposta, encerramento, pesquisa de satisfação", []),
        ("Tratamento de dados pessoais no atendimento", "mascaramento de CPF, o que não pedir", []),
        ("Auditoria de margem e autorização da diretoria", "margem mínima de 15%, relatório semanal", ["margem inferior a 15%"]),
        ("Operação da Black Friday", "escala, estoque, cupom BLACK26, 27 a 30 de novembro de 2026", ["BLACK26"]),
        ("Aplicação de cupons no PDV", "cupons válidos, bloqueios, não cumulatividade", []),
        ("Vale-compras: emissão e conferência", "validade de 120 dias, emissão em trocas de itens em promoção", ["válido por 120 dias"]),
        ("Cartão-presente: venda e ativação", "valores, ativação, bloqueio", []),
        ("Gestão de filas e tempo de espera", "abertura de caixas, metas de espera", []),
        ("Integração de novos colaboradores", "trilha de 30 dias", []),
        ("Treinamento de produtos", "calendário e certificação interna", []),
        ("Plano de contingência para queda de sistema", "PDV offline, comunicação ao cliente", []),
    ]
    for t, foco, fatos in pops:
        add(path=f"interno/procedimentos/pop_{slug(t)}.md", acesso="interno", categoria="procedimento_operacional", titulo=f"POP: {t}", palavras=(480, 760), fatos=fatos,
            briefing=(f"Procedimento operacional padrão (POP) interno da Loja Verde: {t}. Foco: {foco}. Seções '##': Objetivo; Responsáveis; Quando usar; Passo a passo (numerado); Registros e sistemas; Exceções e escalonamento; Erros comuns. "
                      "Uso interno: pode citar alçadas e margens do CANON_INTERNO."))
    rh = ["Política de remuneração e comissionamento", "Plano de carreira no varejo", "Jornada de trabalho e escalas", "Banco de horas", "Política de férias",
          "Código de conduta", "Canal de denúncias", "Avaliação de desempenho", "Benefícios dos colaboradores", "Uso de redes sociais pelos colaboradores",
          "Prevenção ao assédio", "Segurança do trabalho e EPIs", "Processo seletivo", "Processo de desligamento", "Treinamentos obrigatórios de 2026"]
    for t in rh:
        fatos = []
        if "remuneração" in t:
            fatos = [f"piso de {INTERNO_FACTS['piso_vendedor']}", f"comissão de {INTERNO_FACTS['comissao_vendedor']}"]
        if "Jornada" in t:
            fatos = [INTERNO_FACTS["jornada"]]
        add(path=f"interno/rh/{slug(t)}.md", acesso="interno", categoria="rh", titulo=t, palavras=(450, 700), fatos=fatos,
            briefing=(f"Documento interno de Recursos Humanos da Loja Verde: {t}. Seções '##' (5 a 7). Valores do CANON_INTERNO: piso de vendedor {INTERNO_FACTS['piso_vendedor']}, comissão de vendedor {INTERNO_FACTS['comissao_vendedor']} sobre vendas, "
                      f"supervisor {INTERNO_FACTS['comissao_supervisor']} sobre vendas da equipe, vale-refeição de {INTERNO_FACTS['vr']}, jornada de {INTERNO_FACTS['jornada']}. Sem nomes reais."))
    fin = ["Margens por categoria em 2026", "Política de preços", "Regras do comitê de preços", "Condições comerciais com fornecedores", "Contrato com a transportadora principal (fictícia)",
           "Prazos de pagamento a fornecedores", "Custo de frete por região", "Orçamento 2026 por unidade", "Metas de vendas de 2026", "Análise de quebra de estoque",
           "Custo da garantia estendida", "Provisão para trocas e devoluções", "Taxas dos meios de pagamento", "Política de bonificação de fornecedores", "Plano de investimentos 2026-2027",
           "Indicadores das lojas (KPIs)", "Indicadores do e-commerce", "Conciliação de pagamentos", "Prevenção de chargeback", "Política de crédito corporativo (B2B)",
           "Fechamento contábil mensal", "Auditoria interna 2026", "Risco de estoque obsoleto", "Gestão de caixa", "Sazonalidade e planejamento de compras"]
    for t in fin:
        fatos = []
        if t.startswith("Margens"):
            fatos = [f"{c}: {m}%" for c, m in MARGEM_CAT.items()]
        if t.startswith("Taxas"):
            fatos = [f"Pix {INTERNO_FACTS['taxa_pix']}", f"cartão de crédito {INTERNO_FACTS['taxa_credito']}"]
        if t.startswith("Prazos de pagamento"):
            fatos = [f"{INTERNO_FACTS['prazo_forn']} dias"]
        add(path=f"interno/financeiro/{slug(t)}.md", acesso="interno", categoria="financeiro", titulo=t, palavras=(450, 720), fatos=fatos,
            briefing=(f"Documento interno financeiro/comercial da Loja Verde: {t}. Seções '##' (5 a 7), com tabelas em Markdown quando útil. Use os números do CANON_INTERNO (margens por categoria, taxas, margem mínima de 15%). "
                      "Dados fictícios e plausíveis; marque claramente como confidencial."))
    ti = ["Arquitetura do e-commerce (visão geral)", "Política de senhas e acessos", "Backup e recuperação de desastres", "Gestão de incidentes de TI", "Uso do sistema de PDV",
          "Catálogo de códigos de erro (visão técnica)", "Integração com transportadoras", "Monitoramento do aplicativo", "Política de dispositivos móveis", "Plano de continuidade de negócios"]
    for t in ti:
        add(path=f"interno/ti/{slug(t)}.md", acesso="interno", categoria="ti", titulo=t, palavras=(420, 680), fatos=["ERR-4217"] if "erro" in t else [],
            briefing=(f"Documento interno de TI da Loja Verde: {t}. Seções '##' (5 a 7). Não inclua senhas, chaves ou segredos reais ou realistas; use descrições genéricas. "
                      + ("Cite que ERR-4217 (Pix não confirmado em 30 minutos), ERR-5308 (cartão recusado) e ERR-7142 (endereço não atendido) são os três códigos mais frequentes." if "erro" in t else "")))
    inc = [
        ("2026-03-14", "Instabilidade no Pix", "pagamentos por Pix demoraram a confirmar e muitos clientes viram ERR-4217", ["ERR-4217"]),
        ("2026-05-02", "Falha no cálculo de frete", "frete grátis aplicado indevidamente a pedidos abaixo de R$ 199 no Sudeste", ["R$ 199"]),
        ("2025-11-28", "Queda do aplicativo na Black Friday de 2025", "indisponibilidade por 47 minutos", []),
        ("2026-06-10", "Cobrança duplicada no cartão de crédito", "pedidos cobrados duas vezes, estornos manuais", ["ERR-5308"]),
        ("2026-07-21", "Atraso da transportadora principal", "atrasos acima de 5 dias úteis e cupons ATRASO25 emitidos", ["ATRASO25"]),
        ("2026-04-09", "Indisponibilidade do estoque online", "divergência entre estoque da loja e do site", []),
        ("2026-08-03", "Falha na emissão de notas fiscais", "notas não emitidas por 3 horas", []),
        ("2026-02-18", "Envio indevido de e-mail de marketing", "e-mail enviado ao público errado, sem dados sensíveis", []),
        ("2026-09-12", "Uso fraudulento de cupom", "tentativa de uso de um cupom inexistente divulgado em redes sociais", []),
        ("2026-10-05", "Pico de chamados no SAC", "aumento de chamados sobre ERR-7142", ["ERR-7142"]),
        ("2026-01-22", "Divergência de preço no site", "preços de uma linha de eletrônicos exibidos incorretamente", []),
        ("2026-09-30", "Falta de energia na unidade Barreiro", "unidade fechada por 4 horas", []),
    ]
    for data, t, resumo, fatos in inc:
        add(path=f"interno/incidentes/{data}_{slug(t)}.md", acesso="interno", categoria="postmortem", titulo=f"Post-mortem {data}: {t}", palavras=(450, 700), fatos=[data] + fatos,
            briefing=(f"Relatório de incidente (post-mortem) da Loja Verde ocorrido em {data}: {t}. Resumo: {resumo}. Seções '##': Resumo; Linha do tempo (horários); Impacto; Causa raiz; Ações imediatas; Ações preventivas com responsáveis e prazos; Lições aprendidas. "
                      "Sem nomes reais; use cargos ou primeiros nomes fictícios."))
    atas = []
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro"]
    for i, m in enumerate(meses, start=1):
        atas.append((f"Ata da reunião mensal da diretoria de {m} de 2026", f"2026-{i:02d}-12", "md", "resultados do mês, decisões sobre metas e investimentos, manutenção das políticas comerciais (prazo de troca em 30 dias corridos, frete grátis acima de R$ 199 no Sudeste)"))
    for i, m in enumerate(["fevereiro", "abril", "junho", "agosto", "outubro", "novembro"], start=1):
        atas.append((f"Ata do comitê de preços de {m} de 2026", f"2026-{[2, 4, 6, 8, 10, 11][i - 1]:02d}-20", "txt", "ajustes de preço, margem mínima de 15%, exceções autorizadas, desconto de gerente de até 10%"))
    for i, m in enumerate(["fevereiro", "maio", "agosto", "novembro", "março", "setembro"], start=1):
        atas.append((f"Ata do comitê de qualidade de {m} de 2026", f"2026-{[2, 5, 8, 11, 3, 9][i - 1]:02d}-25", "txt", "defeitos recorrentes, garantia de 12 meses, indicadores de reparo em até 30 dias"))
    for i, m in enumerate(["março", "abril", "junho", "agosto", "outubro", "novembro"], start=1):
        atas.append((f"Ata da reunião de gerentes regionais de {m} de 2026", f"2026-{[3, 4, 6, 8, 10, 11][i - 1]:02d}-05", "txt", "metas por unidade, alçadas de desconto, tolerância de troca de 7 dias (uso interno), escalas de Black Friday"))
    for m, mm in [("abril", "04"), ("julho", "07"), ("outubro", "10"), ("dezembro", "12")]:
        atas.append((f"Ata do comitê de sustentabilidade de {m} de 2026", f"2026-{mm}-15", "txt", "Recicla Verde, Semana Verde, metas ambientais"))
    for m in ["fevereiro", "maio", "agosto", "novembro"]:
        atas.append((f"Ata do comitê de tecnologia de {m} de 2026", "2026-" + {"fevereiro": "02", "maio": "05", "agosto": "08", "novembro": "11"}[m] + "-18", "txt", "estabilidade do app, códigos ERR mais frequentes, roadmap"))
    for m in ["março", "junho", "setembro", "dezembro"]:
        atas.append((f"Ata do comitê de experiência do cliente de {m} de 2026", "2026-" + {"março": "03", "junho": "06", "setembro": "09", "dezembro": "12"}[m] + "-22", "txt", "pesquisa de satisfação, reclamações da ouvidoria, Clube Verde"))
    for t, data, fmt, foco in atas:
        add(path=f"interno/atas/{data}_{slug(t)}.{fmt}", acesso="interno", categoria="ata", formato=fmt, titulo=t, palavras=(350, 580), fatos=[],
            briefing=(f"{t}, realizada em {data}. Pauta: {foco}. Estrutura: PARTICIPANTES (cargos e primeiros nomes fictícios), PAUTA, DISCUSSÃO (por item), DECISÕES (numeradas) e ENCAMINHAMENTOS (responsável e prazo). "
                      + ("Escreva em Markdown com seções '##'." if fmt == "md" else "Escreva em texto puro, sem Markdown.")
                      + " Decisões devem manter as políticas do CANON; nunca altere valores vigentes."))


# ------------------------------------------------------------------ transcrições de atendimento (interno, .txt)
SCEN = [
    ("troca", "cliente quer trocar um tênis que não serviu, comprado há 12 dias", _f("troca")),
    ("troca", "cliente comprou na promoção e quer o dinheiro de volta, não apenas vale-compras", ["somente por vale-compras, válido por 120 dias"]),
    ("troca", "arrependimento de compra feita pelo aplicativo, 5 dias após a entrega", FR["arrep"]),
    ("troca", "prazo de 30 dias vencido há 3 dias e o cliente pede exceção; o atendente escala para o gerente, que aplica a tolerância interna de 7 dias", ["tolerância de 7 dias"]),
    ("reembolso", "estorno no cartão de crédito não apareceu na fatura", FR["reemb"] + ["até duas faturas"]),
    ("reembolso", "cliente pagou com Pix e pergunta quando recebe o reembolso", FR["reemb"]),
    ("frete", "cliente de Salvador pergunta a partir de que valor o frete é grátis", ["acima de R$ 299"]),
    ("frete", "prazo de entrega para capital; depois o cliente pergunta 'e para o interior?'", FR["prazo"]),
    ("frete", "pedido atrasou 6 dias úteis; atendente informa o cupom de compensação", FR["atraso"]),
    ("frete", "retirada em loja: tempo de liberação e documentos", FR["retirada"]),
    ("frete", "o marido do titular vai retirar o pedido; regras para terceiros", FR["retirada"]),
    ("frete", "o sistema mostra ERR-7142 ao finalizar a compra; alternativa é retirada na loja", ["O código ERR-7142 indica que o endereço informado não é atendido pela transportadora."]),
    ("frete", "rastreamento sem atualização há dois dias", []),
    ("garantia", "celular parou de ligar sozinho, 8 meses de uso", ["garantia de 12 meses contra defeitos de fabricação"]),
    ("garantia", "cliente derrubou água no notebook e pergunta se a garantia cobre", ["contato com líquidos"]),
    ("garantia", "cliente quer contratar garantia estendida 20 dias depois da compra", FR["gar_ext"]),
    ("garantia", "reparo passou de 30 dias; cliente escolhe entre troca, devolução do valor e abatimento", ["prazo máximo de reparo é de 30 dias"]),
    ("pagamento", "cliente quer parcelar em 10 vezes e descobre a parcela mínima de R$ 50", ["em até 10 vezes sem juros", "R$ 50"]),
    ("pagamento", "Pix não confirmado, ERR-4217, pedido cancelado automaticamente", ["O código ERR-4217 indica que o pagamento por Pix não foi confirmado em 30 minutos."]),
    ("pagamento", "cartão recusado, ERR-5308; orientação para tentar outro cartão ou falar com o banco", ["O código ERR-5308 indica que o cartão foi recusado pela operadora."]),
    ("pagamento", "boleto vencido e pedido cancelado", FR["boleto"]),
    ("pagamento", "cliente pergunta se pode somar desconto do Pix com parcelamento", ["5% de desconto"]),
    ("clube", "quantos pontos o cliente ganha e quanto vale o resgate", FR["clube"]),
    ("clube", "pontos expirados; o cliente reclama", ["expiram 12 meses depois da data da compra"]),
    ("clube", "cupom de aniversário do Clube Verde", FR["aniv"]),
    ("clube", "dúvida sobre os níveis Verde, Folha e Floresta", ["Folha"]),
    ("cupom", "cupom BEMVINDO10 combinado com Pix", ["BEMVINDO10"]),
    ("cupom", "cliente viu nas redes sociais um cupom FRETE100 de 100% de desconto; o atendente explica que esse cupom NÃO existe e orienta sobre golpes", ["FRETE100"]),
    ("app", "cliente não consegue entrar no aplicativo, conta bloqueada", []),
    ("app", "como abrir um chamado de garantia pelo aplicativo", ["chamado no aplicativo"]),
    ("produto", "dúvida entre dois modelos de geladeira, voltagem e consumo", ["voltagem"]),
    ("produto", "disponibilidade de um smartphone na unidade Pampulha e reserva pelo aplicativo", []),
    ("loja", "horário de funcionamento de domingo na unidade Contagem, que fecha aos domingos, e alternativa na Pampulha", ["fechada"]),
    ("loja", "estacionamento na unidade Lourdes, que não tem estacionamento próprio", ["convênio com garagem vizinha"]),
    ("privacidade", "cliente pede a exclusão dos seus dados pessoais", ["privacidade@lojaverde.example"]),
    ("golpe", "cliente recebeu ligação de falsa central pedindo token; atendente orienta que a Loja Verde nunca pede senha, token ou código", ["nunca pede senha"]),
    ("reclamacao", "cliente insatisfeito pede o registro na ouvidoria; prazo de resposta de 10 dias úteis", ["10 dias úteis"]),
    ("sustentabilidade", "como descartar um celular antigo e ganhar o cupom RECICLA20", ["RECICLA20"]),
    ("black", "dúvida sobre datas e cupom da Black Friday 2026", ["BLACK26", "27 a 30 de novembro de 2026"]),
]


def gen_transcricoes(add, n=110):
    rng = random.Random(33)
    canais = ["chat do aplicativo", "chat do site", "telefone (SAC)", "balcão da loja", "WhatsApp oficial"]
    humores = ["calmo e objetivo", "irritado, mas educado", "com pressa", "inseguro e com muitas dúvidas", "bem-humorado", "desconfiado"]
    nomes_c = ["Marcos", "Ana", "Paulo", "Juliana", "Ricardo", "Mariana", "Carlos", "Patrícia", "Fábio", "Aline", "Sérgio", "Tatiane", "Lucas", "Renata", "Eduardo", "Cláudia"]
    nomes_a = ["Bruna", "Otto", "Larissa", "Rafael", "Natália", "Gustavo", "Priscila", "Vinícius"]
    for i in range(n):
        area, situ, fatos = SCEN[i % len(SCEN)]
        canal, humor = rng.choice(canais), rng.choice(humores)
        u = rng.choice(UNIDADES)["nome"] if canal == "balcão da loja" else "e-commerce"
        proto = f"LV-2026-{rng.randint(100000, 999999)}"
        data = f"2026-{rng.randint(1, 10):02d}-{rng.randint(1, 28):02d}"
        turnos = rng.randint(8, 14)
        cli, att = rng.choice(nomes_c), rng.choice(nomes_a)
        add(path=f"interno/atendimento/transcricoes/at_{i + 1:03d}_{area}_{proto.lower()}.txt", acesso="interno", categoria="transcricao_atendimento", formato="txt", unidade=u if u != "e-commerce" else "rede",
            titulo=f"Atendimento {proto} ({area})", palavras=(260, 480), fatos=[f"Protocolo: {proto}"] + fatos, extra={"protocolo": proto, "assunto": area},
            briefing=(f"Transcrição de um atendimento ao cliente da Loja Verde, em texto puro. Situação: {situ}. Canal: {canal}. Unidade/origem: {u}. Data: {data}. Cliente: {cli} (humor: {humor}). Atendente: {att}. Cerca de {turnos} trocas de mensagens. "
                      f"Formato: cabeçalho com linhas 'Protocolo: {proto}', 'Canal: ...', 'Data: ...', 'Cliente: {cli} (CPF ***.***.***-**)', 'Atendente: {att}'; depois uma linha '---'; depois as falas '[HH:MM] Cliente: ...' e '[HH:MM] Atendente: ...'; "
                      "depois '---' e 'Resolução: ...' com 1 a 2 frases. Inclua pelo menos uma mensagem curta e elíptica do cliente que só faz sentido com o histórico (ex.: 'e para o interior?', 'em quantas vezes?', 'e se foi na promoção?'). "
                      "O atendente deve responder com as regras do CANON usando as frases dos FATOS. CPF sempre mascarado; nunca escreva dados pessoais completos."))
