---
doc_id: "LV-PUB-ART-0045"
titulo: "Como resolver o erro ERR-6158: frete não calculado"
categoria: "artigo_de_ajuda"
acesso: "publico"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
codigo: "ERR-6158"
familia: "checkout"
---

# Como resolver o erro ERR-6158: frete não calculado

## O que significa

O erro ERR-6158 aparece quando o sistema não consegue calcular o valor do frete para o pedido. Sem esse cálculo, o total da compra fica incompleto e o pagamento não pode ser concluído. A falha geralmente está ligada ao CEP informado, à região de entrega ou à modalidade escolhida, e não ao produto em si. O código pertence à família Carrinho e finalização da compra e é mostrado logo antes da etapa de pagamento.

## Por que acontece

O cálculo do frete depende de informações precisas, como CEP, região, peso e volume do pedido. Se algum desses dados estiver incompleto ou inconsistente, o sistema não consegue apresentar a cotação. Também acontece quando a modalidade escolhida, como entrega expressa ou agendada, não está disponível para aquele endereço. Em compras com volumes grandes, o cálculo pode falhar se o pedido ultrapassar o limite de uma das modalidades de envio.

## Como resolver

1. Confira o CEP informado no endereço de entrega e corrija-o, se houver algum dígito incorreto.
2. Verifique se o endereço está completo, com número, complemento e bairro.
3. Tente outra modalidade de entrega disponível no resumo do pedido.
4. Se o frete continuar sem cálculo, recalcule removendo e incluindo novamente um item do carrinho.
5. Caso o problema persista, considere a retirada em uma unidade física, que não depende do cálculo de frete.

## Quando procurar o SAC

Procure o SAC quando o código ERR-6158 aparecer com um CEP correto e em todas as modalidades, ou quando o frete não for exibido mesmo após atualizar a página. O atendimento funciona de segunda a sexta, das 8h às 20h, e aos sábados, das 8h às 14h, pelo telefone 0800 700 0100. Também é possível escrever para atendimento@lojaverde.example. Informe o CEP e a lista de itens do carrinho.

## Dicas para evitar

- Revise o CEP antes de confirmar o endereço, especialmente em cidades com nomes parecidos.
- Lembre-se de que o frete é grátis acima de R$ 199 para a região Sudeste e acima de R$ 299 nas demais regiões.
- Atualize o aplicativo antes de finalizar compras grandes, para garantir o cálculo mais recente.
- Compare os prazos de entrega por região antes de escolher a modalidade.
- Se o pedido for retirado na loja, o cálculo de frete não é necessário.
