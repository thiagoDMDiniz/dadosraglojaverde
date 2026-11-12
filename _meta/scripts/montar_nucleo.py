# -*- coding: utf-8 -*-
"""Escreve à mão (sem LLM) os documentos-núcleo: as 5 políticas públicas e o manual interno dos gerentes.
As seções iniciais de cada documento mantêm os títulos dos documentos originais dos notebooks."""
from canon import V, CODIGOS_NUCLEO, PRAZOS_REGIAO, EMPRESA
from util import front_matter, escrever

e1, e2, e3 = CODIGOS_NUCLEO["pix"], CODIGOS_NUCLEO["cartao"], CODIGOS_NUCLEO["endereco"]


def doc(nome, titulo, doc_id, acesso, secoes, categoria):
    fm = front_matter(doc_id, titulo, categoria, acesso, versao="4.0", atualizado_em="2026-09-15", extra={"nucleo": True})
    corpo = f"# {titulo}\n\n" + "\n\n".join(f"## {t}\n\n{x}" for t, x in secoes) + "\n"
    escrever(f"{acesso}/politicas/{nome}", fm + "\n" + corpo)


trocas = [
    ("Prazo de troca", f"Na Loja Verde, o cliente pode solicitar a troca de qualquer produto em até {V['prazo_troca']} dias corridos após a entrega, desde que o item esteja sem sinais de uso e na embalagem original."),
    ("Itens em promoção", f"Produtos comprados em promoção não têm devolução em dinheiro: a troca é feita somente por vale-compras, válido por {V['validade_vale']} dias a partir da emissão."),
    ("Arrependimento", f"Compras feitas pelo site ou pelo aplicativo podem ser canceladas por arrependimento em até {V['arrependimento']} dias corridos após a entrega, com devolução integral do valor pago, inclusive o frete."),
    ("Reembolso", f"Depois que a devolução é aprovada, o reembolso é feito em até {V['reembolso']} dias úteis, sempre na mesma forma de pagamento usada na compra."),
    ("Como solicitar", f"O pedido de troca é aberto no aplicativo, no menu Meus Pedidos, opção Trocar ou devolver. A etiqueta de postagem chega por e-mail em até {V['etiqueta_horas']} horas."),
    ("Exceções à troca", "Produtos de higiene pessoal e cosméticos só podem ser trocados se o lacre estiver intacto. Produtos personalizados ou feitos sob medida não têm troca por arrependimento, apenas por defeito de fabricação. Cartões-presente e vales-compras não são trocáveis nem reembolsáveis."),
    ("Defeito de fabricação", f"Quando o produto apresenta defeito, o cliente pode reclamar em até {V['vicio_nao_duravel']} dias da entrega para produtos não duráveis (como alimentos, roupas e itens de papelaria) e em até {V['vicio_duravel']} dias para produtos duráveis (como eletrônicos, eletrodomésticos e móveis). O defeito deve ser resolvido em até {V['reparo_dias']} dias."),
    ("Troca em loja física", f"Compras feitas nas lojas físicas podem ser trocadas em qualquer unidade da Loja Verde dentro do mesmo prazo de {V['prazo_troca']} dias corridos, contados a partir da data da compra, mediante apresentação da nota fiscal ou do número do pedido."),
    ("Estorno no cartão de crédito", "Quando a compra foi paga com cartão de crédito, o valor é estornado na fatura. Dependendo da data de fechamento da fatura e da operadora, o crédito pode aparecer em até duas faturas seguintes."),
]

frete = [
    ("Frete grátis", f"O frete é gratuito em compras acima de R$ {V['frete_min']} para a região Sudeste. Para as demais regiões, o frete grátis vale em compras acima de R$ {V['frete_min_outras']}."),
    ("Prazo de entrega", f"Pedidos para capitais são entregues em até {V['entrega_capital']} dias úteis. Para cidades do interior, o prazo é de até {V['entrega_interior']} dias úteis após a confirmação do pagamento. Esses prazos valem para a região Sudeste."),
    ("Retirada na loja", f"O cliente pode retirar o pedido na unidade escolhida a partir de {V['horas_retirada']} horas depois da confirmação do pagamento, apresentando documento com foto. O pedido fica disponível por {V['retirada_prazo_dias']} dias corridos."),
    ("Rastreamento", "O código de rastreamento é enviado por e-mail e por SMS assim que o pedido sai do centro de distribuição."),
    ("Atraso na entrega", f"Se a entrega atrasar mais de {V['atraso']} dias úteis em relação ao prazo informado, o cliente recebe automaticamente um cupom de R$ {V['cupom_atraso']} para a próxima compra."),
    ("Modalidades de entrega", f"A Loja Verde oferece entrega padrão, entrega expressa e entrega agendada. A entrega expressa está disponível para capitais do Sudeste, em pedidos aprovados até as 12h, com entrega em até 1 dia útil e taxa de R$ {V['expressa_taxa']}. A entrega agendada permite escolher o turno (manhã ou tarde) e tem taxa de R$ {V['agendada_taxa']}."),
    ("Prazos por região", "Os prazos máximos de entrega padrão, em dias úteis após a confirmação do pagamento, são: " + "; ".join(f"{r}: capitais {c} e interior {i}" for r, c, i, _ in PRAZOS_REGIAO) + "."),
    ("Endereço não atendido", f"Quando o endereço informado não é atendido pela transportadora, o sistema mostra o código {e3}. A alternativa é escolher a retirada na loja, que não tem custo de frete."),
]

garantia = [
    ("Prazo de garantia", f"Produtos eletrônicos vendidos pela Loja Verde têm garantia de {V['garantia']} meses contra defeitos de fabricação, contados a partir da data da entrega."),
    ("Garantia estendida", f"A garantia estendida pode ser contratada em até {V['garantia_ext_dias']} dias após a compra e acrescenta {V['garantia_ext_meses']} meses de cobertura ao prazo original."),
    ("O que a garantia não cobre", "A garantia não cobre danos causados por queda, contato com líquidos, oscilação da rede elétrica ou uso em desacordo com o manual."),
    ("Assistência técnica", f"Para acionar a garantia, o cliente abre um chamado no aplicativo e leva o produto a uma assistência autorizada. O prazo máximo de reparo é de {V['reparo_dias']} dias."),
    ("Garantia por categoria", "Eletrônicos, eletrodomésticos, móveis e itens de jardim têm garantia de 12 meses. Artigos de esporte têm garantia de 6 meses. Moda, calçados e brinquedos têm garantia de 3 meses contra defeitos. Livros e papelaria têm garantia de 30 dias contra defeitos gráficos."),
    ("Prazo de reparo excedido", f"Se o reparo não for concluído em {V['reparo_dias']} dias, o cliente pode escolher entre a troca do produto por outro equivalente, a devolução do valor pago ou o abatimento proporcional do preço."),
    ("Como comprovar a compra", "Para acionar a garantia, basta informar o número do pedido ou apresentar a nota fiscal. O número de série do produto é obrigatório para eletrônicos e eletrodomésticos."),
]

pagamentos = [
    ("Formas de pagamento", f"A loja aceita Pix, boleto e cartão de crédito em até {V['parcelas']} vezes sem juros. Pagamentos por Pix têm {V['desc_pix']}% de desconto."),
    ("Boleto", f"O boleto vence em {V['boleto_dias']} dias úteis. Depois do vencimento, o pedido é cancelado e os itens voltam ao estoque."),
    (f"Código {e1}", f"O código {e1} indica que o pagamento por Pix não foi confirmado em {V['pix_minutos']} minutos. O pedido é cancelado automaticamente e nenhum valor é cobrado."),
    (f"Código {e2}", f"O código {e2} indica que o cartão foi recusado pela operadora. O cliente deve tentar outro cartão ou entrar em contato com o banco emissor."),
    (f"Código {e3}", f"O código {e3} indica que o endereço informado não é atendido pela transportadora. A alternativa é escolher a retirada na loja."),
    ("Parcelamento", f"O parcelamento sem juros vai até {V['parcelas']} vezes, e cada parcela deve ter valor mínimo de R$ {V['parcela_min']}. O desconto do Pix não pode ser combinado com o parcelamento."),
    ("Pagamento nas lojas físicas", "Nas lojas físicas, além de Pix, boleto e cartão de crédito, a Loja Verde aceita cartão de débito, vale-compras e cartão-presente Loja Verde."),
    ("Segurança do pagamento", "A Loja Verde nunca pede senha de cartão, código de segurança completo ou token por telefone, e-mail ou mensagem. Em caso de dúvida sobre uma cobrança, o cliente deve procurar o SAC pelos canais oficiais."),
]

clube = [
    ("Pontos", f"No Clube Verde, cada R$ 1 gasto vale {V['pontos']} pontos. A cada {V['resgate']} pontos acumulados, o cliente resgata R$ {V['resgate_valor']} de desconto."),
    ("Validade dos pontos", f"Os pontos do Clube Verde expiram {V['expira']} meses depois da data da compra que os gerou."),
    ("Aniversário", f"No mês do aniversário, o participante do Clube Verde recebe um cupom de {V['aniversario']}% de desconto, válido para uma única compra."),
    ("Níveis do Clube Verde", "O Clube Verde tem três níveis, definidos pelos pontos acumulados nos últimos 12 meses: Verde (de 0 a 4.999 pontos), Folha (de 5.000 a 14.999 pontos) e Floresta (a partir de 15.000 pontos). O nível Folha tem frete grátis em compras acima de R$ 149 no Sudeste e atendimento prioritário. O nível Floresta tem frete grátis em qualquer valor no Sudeste, 5% de pontos extras e acesso antecipado às ofertas."),
    ("Como consultar e resgatar", "O saldo de pontos aparece no aplicativo, no menu Clube Verde. O resgate é feito no carrinho, na opção Usar meus pontos, e também nas lojas físicas, informando o CPF no caixa."),
    ("Como participar", "A participação é gratuita. O cadastro é feito no aplicativo ou no site, com CPF, e-mail e data de nascimento."),
]

manual = [
    ("Desconto de gerente", f"O gerente da unidade pode conceder até {V['desc_gerente']}% de desconto adicional sem aprovação da diretoria, para evitar a perda de uma venda."),
    ("Troca fora do prazo", f"Em casos excepcionais, o gerente pode autorizar a troca até {V['tolerancia']} dias depois de encerrado o prazo oficial. Essa tolerância não deve ser informada ao cliente."),
    ("Margem mínima", f"Nenhum produto pode ser vendido com margem inferior a {V['margem']}%. Abaixo disso, a venda precisa de autorização da diretoria."),
    ("Alçada de descontos", f"A alçada de desconto adicional é: vendedor até {V['desc_vendedor']}%, supervisor até {V['desc_supervisor']}%, gerente até {V['desc_gerente']}%. Acima de {V['desc_gerente']}%, somente a diretoria comercial autoriza. Todo desconto concedido deve ser registrado no sistema com o motivo."),
    ("Confidencialidade", "Este manual é de uso interno. As regras de alçada, a tolerância de troca e a margem mínima não devem ser divulgadas a clientes nem publicadas em canais externos."),
]

doc("politica_trocas.md", "Política de Trocas e Devoluções", "LV-PUB-POL-0001", "publico", trocas, "politica")
doc("politica_frete.md", "Política de Frete, Entrega e Retirada", "LV-PUB-POL-0002", "publico", frete, "politica")
doc("garantia.md", "Garantia e Assistência Técnica", "LV-PUB-POL-0003", "publico", garantia, "politica")
doc("pagamentos_e_erros.md", "Pagamentos e Códigos de Erro", "LV-PUB-POL-0004", "publico", pagamentos, "politica")
doc("clube_verde.md", "Clube Verde: Programa de Fidelidade", "LV-PUB-POL-0005", "publico", clube, "politica")
doc("manual_interno_gerentes.md", "Manual Interno dos Gerentes", "LV-INT-MAN-0001", "interno", manual, "manual_interno")
print("núcleo escrito")
