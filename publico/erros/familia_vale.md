---
doc_id: "LV-PUB-COD-0013"
titulo: "Códigos de erro: Vale-compras e cartão-presente"
categoria: "codigos_de_erro"
acesso: "publico"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
familia: "vale"
---

# Códigos de erro: Vale-compras e cartão-presente

Este catálogo reúne os códigos de erro relacionados ao vale-compras e ao cartão-presente. Ambos são usados em lojas físicas e no site, mas têm regras próprias: o vale-compras é válido por 120 dias a partir da emissão, e o cartão-presente, com valores de R$ 50, R$ 100, R$ 200 ou R$ 500, tem validade de 12 meses. Cada código tem quatro dígitos, e códigos parecidos podem ter causas diferentes. Para ajuda, o SAC atende pelo 0800 700 0100.

## ERR-8401: vale-compras expirado

O código ERR-8401 indica que o vale-compras passou do prazo de validade de 120 dias contados da emissão. Depois desse período, o sistema não aceita mais o código, e o saldo não pode ser recuperado automaticamente.

**O que fazer:**

1. Verifique a data de emissão do vale no comprovante ou na mensagem recebida.
2. Procure o SAC para saber se há alguma condição especial para o seu caso.
3. Use os próximos vales dentro do prazo, anotando a data de emissão.

## ERR-8431: saldo insuficiente

O código ERR-8431 indica que o saldo do vale ou do cartão-presente não cobre o valor pretendido. O sistema verifica o total disponível antes de concluir a operação e impede a aplicação de valor maior do que o saldo.

**O que fazer:**

1. Consulte o saldo disponível no aplicativo ou no comprovante.
2. Ajuste o carrinho para que o total fique igual ou menor ao saldo.
3. Complete o pagamento com outra forma de pagamento, caso o total seja maior.

## ERR-8435: código do vale inválido

O código ERR-8435 indica que o código digitado não corresponde a nenhum vale-compras ou cartão-presente da Loja Verde. A causa mais comum é um caractere digitado errado, como uma letra no lugar de um número.

**O que fazer:**

1. Confira o código letra por letra, comparando com o comprovante original.
2. Evite copiar espaços antes ou depois do código.
3. Se o código estiver correto e o erro continuar, procure o SAC com o comprovante.

## ERR-8439: vale já utilizado

O código ERR-8439 indica que o vale-compras informado já foi consumido em uma compra anterior. Cada vale tem código único, e o uso é registrado assim que a compra é concluída.

**O que fazer:**

1. Verifique em Meus Pedidos se algum pedido recente utilizou o vale.
2. Use o código mais recente enviado pela loja, se houver mais de um.
3. Procure o SAC caso não encontre nenhum uso anterior.

## ERR-8440: vale não acumulável com a promoção

O código ERR-8440 indica que o vale-compras não pode ser somado à promoção aplicada ao carrinho. Produtos comprados em promoção aceitam o vale apenas quando a oferta permite a combinação.

**O que fazer:**

1. Retire o vale do carrinho e confira quais itens estão em promoção.
2. Separe a compra em dois pedidos, se for vantajoso.
3. Aguarde o fim da promoção, ou procure o SAC para tirar dúvidas sobre a oferta.

## ERR-8449: cartão-presente bloqueado

O código ERR-8449 indica que o cartão-presente está bloqueado para uso. O bloqueio pode ser preventivo, quando há uma revisão de segurança em curso, ou decorrente de uma irregularidade na compra original.

**O que fazer:**

1. Não tente usar o cartão repetidamente enquanto o bloqueio estiver ativo.
2. Verifique se o cartão foi comprado pela loja e se o pagamento foi confirmado.
3. Procure o SAC com o número do cartão para revisar o bloqueio.

## ERR-8454: recarga indisponível

O código ERR-8454 indica que a recarga do cartão-presente ou do vale não pode ser concluída no momento. A recarga depende da habilitação do cartão e do funcionamento do sistema de pagamentos.

**O que fazer:**

1. Confira a validade do cartão ou do vale antes de tentar a recarga.
2. Aguarde alguns minutos e tente novamente.
3. Se a recarga continuar indisponível, procure o SAC para avaliar alternativas.

## ERR-8465: uso parcial não permitido no site

O código ERR-8465 indica que o vale-compras foi informado para cobrir apenas uma parte do pedido, e essa forma de uso não é aceita pelo site ou pelo aplicativo. O vale deve cobrir o total da compra, dentro do seu saldo.

**O que fazer:**

1. Revise o total do pedido, incluindo o frete.
2. Ajuste o carrinho para que o valor fique igual ou menor ao saldo do vale.
3. Escolha outra forma de pagamento para a diferença, se o pedido for maior que o vale.

## ERR-8469: cartão-presente de outra rede

O código ERR-8469 indica que o cartão-presente apresentado foi emitido por outra rede e não pode ser aceito na Loja Verde. Somente cartões emitidos pela própria loja são válidos para pagamento.

**O que fazer:**

1. Confira o nome e a identificação impressos no cartão.
2. Use um cartão-presente emitido pela Loja Verde, ou escolha outra forma de pagamento.
3. Procure o SAC caso acredite que o cartão é da Loja Verde e o erro persistir.

## ERR-8472: valor acima do limite permitido

O código ERR-8472 indica que o valor informado para o vale ou para o cartão-presente é maior do que o limite permitido na operação. Os cartões-presente são vendidos nos valores fixos de R$ 50, R$ 100, R$ 200 ou R$ 500.

**O que fazer:**

1. Reduza o valor da operação para o limite indicado na tela.
2. Escolha um dos valores fixos de cartão-presente, se for o caso.
3. Divida a compra em mais de um vale, se a necessidade for maior.
