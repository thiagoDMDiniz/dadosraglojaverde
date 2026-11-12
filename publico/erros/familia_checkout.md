---
doc_id: "LV-PUB-COD-0010"
titulo: "Códigos de erro: Carrinho e finalização da compra"
categoria: "codigos_de_erro"
acesso: "publico"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
familia: "checkout"
---

# Códigos de erro: Carrinho e finalização da compra

Este catálogo explica os códigos que aparecem entre a montagem do carrinho e a confirmação do pedido. Eles tratam de estoque no carrinho, preço, cupons, frete, limites por CPF e sessão de pagamento. Cada código tem quatro dígitos, e códigos parecidos podem ter causas diferentes. Confira o número exato antes de seguir uma orientação. Para ajuda, o SAC atende pelo 0800 700 0100 e pelo e-mail atendimento@lojaverde.example.

## ERR-6102: item sem estoque no carrinho

O código ERR-6102 indica que um dos produtos do carrinho acabou ou não tem quantidade suficiente em estoque para o pedido. Como o carrinho não reserva unidades por tempo indeterminado, a disponibilidade pode mudar enquanto a compra é montada.

**O que fazer:**

1. Abra o carrinho e identifique o item marcado com a mensagem.
2. Reduza a quantidade ou troque o produto por um equivalente disponível.
3. Se o item for essencial, consulte a disponibilidade nas unidades próximas.

## ERR-6103: preço alterado durante a compra

O código ERR-6103 indica que o preço de um produto foi alterado depois que ele entrou no carrinho. Isso pode acontecer ao fim de uma promoção ou com a entrada de uma nova campanha. A loja exibe o valor atualizado antes de cobrar, para que você decida se quer continuar.

**O que fazer:**

1. Revise o carrinho e compare o preço novo com o que você viu antes.
2. Remova o item e adicione-o de novo para atualizar o valor.
3. Confirme o pedido apenas se o valor exibido estiver de acordo com o que você deseja pagar.

## ERR-6109: cupom inválido

O código ERR-6109 indica que o cupom digitado não existe ou não está habilitado para a compra. Cupons devem ser digitados exatamente como foram divulgados, com letras e números idênticos. A Loja Verde aceita apenas os cupons que estão ativos no momento.

**O que fazer:**

1. Confira a grafia do cupom, sem espaços antes ou depois.
2. Verifique se o cupom é para a categoria dos produtos do carrinho.
3. Se o cupom veio de um e-mail ou de uma campanha, confira se ele ainda está vigente.

## ERR-6116: cupom expirado

O código ERR-6116 indica que o cupom existe, mas o período de uso já terminou. Cupons têm datas específicas de início e fim, e o sistema não os aplica depois desse prazo. Por isso, é importante consultar a validade antes de finalizar.

**O que fazer:**

1. Verifique no e-mail ou na campanha a data de validade do cupom.
2. Caso o cupom tenha sido enviado pela loja, procure um cupom atual nas ofertas em vigor.
3. Finalize a compra sem cupom se nenhuma outra opção estiver disponível.

## ERR-6143: cupom não cumulativo com a promoção

O código ERR-6143 indica que o cupom escolhido não pode ser combinado com a promoção aplicada ao carrinho. Cada cupom tem regras próprias, e algumas ofertas excluem a soma de descontos para manter a condição divulgada.

**O que fazer:**

1. Compare o valor final com e sem o cupom, para escolher a melhor condição.
2. Remova a promoção do carrinho, se ela for menos vantajosa que o cupom.
3. Consulte as regras do cupom e da promoção antes de finalizar.

## ERR-6158: frete não calculado

O código ERR-6158 indica que o valor do frete não pôde ser calculado para o endereço informado. O cálculo depende do CEP, da região e do peso ou tamanho dos produtos. Sem o frete, o total do pedido não fica completo.

**O que fazer:**

1. Confira se o CEP foi digitado corretamente e se o endereço está completo.
2. Atualize a tela do carrinho para refazer o cálculo.
3. Se o problema persistir, retire um item de cada vez para descobrir qual impede o cálculo, e procure o SAC.

## ERR-6167: limite de quantidade por CPF atingido

O código ERR-6167 indica que o CPF da conta já atingiu o limite de unidades permitido para aquele produto dentro do período de venda. A regra evita que um único cliente monopolize itens em promoções ou lançamentos.

**O que fazer:**

1. Reduza a quantidade do produto no carrinho.
2. Aguarde a próxima janela de compra, se a campanha tiver períodos definidos.
3. Procure o SAC caso acredite que o limite foi aplicado de forma incorreta.

## ERR-6176: sessão expirada no pagamento

O código ERR-6176 indica que o tempo de uso da tela de pagamento terminou antes da confirmação. Por segurança, a sessão é encerrada depois de um período sem atividade. Isso não cobra nada do cliente e o carrinho costuma ser preservado.

**O que fazer:**

1. Entre novamente na conta e abra o carrinho.
2. Revise o pedido e escolha a forma de pagamento sem demora.
3. Confirme o pagamento antes de sair da tela, e verifique em Meus Pedidos se o pedido foi criado.

## ERR-6194: endereço de entrega não selecionado

O código ERR-6194 indica que nenhum endereço de entrega foi escolhido antes da finalização. Sem um endereço selecionado, o frete e o prazo de entrega não podem ser definidos corretamente.

**O que fazer:**

1. Abra a etapa de entrega no carrinho.
2. Escolha um endereço já cadastrado ou cadastre um novo, com CEP e número.
3. Confirme o endereço antes de avançar para o pagamento.

## ERR-6198: valor mínimo do cupom não atingido

O código ERR-6198 indica que o total do carrinho é menor que o valor mínimo exigido pelo cupom. Alguns cupons só valem em compras acima de determinado montante, o que é informado nas condições de cada um.

**O que fazer:**

1. Confira o valor mínimo exigido pelo cupom nas condições divulgadas.
2. Acrescente produtos ao carrinho até atingir o valor mínimo, se fizer sentido.
3. Caso não queira ampliar a compra, finalize sem o cupom.
