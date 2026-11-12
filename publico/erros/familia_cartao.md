---
doc_id: "LV-PUB-COD-0002"
titulo: "Códigos de erro: Pagamento com cartão de crédito"
categoria: "codigos_de_erro"
acesso: "publico"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
familia: "cartao"
---

# Códigos de erro: Pagamento com cartão de crédito

Este catálogo reúne os códigos de erro que aparecem quando o pagamento é feito com cartão de crédito. Cada código tem quatro dígitos e, como outros códigos da loja, pode ser parecido com um vizinho e ter causa diferente. Confira o número na tela antes de seguir uma orientação. As compras podem ser parceladas em até 10 vezes sem juros, com parcela mínima de R$ 50. Para ajuda, o SAC atende pelo 0800 700 0100.

## ERR-5308: cartão recusado pela operadora

O código ERR-5308 indica que o cartão foi recusado pela operadora. A recusa pode ter motivos como saldo ou limite indisponível, bloqueio preventivo ou restrição definida pelo banco emissor. A Loja Verde não tem acesso aos motivos internos da operadora, por isso o banco é o melhor canal para esclarecer a situação.

**O que fazer:**

1. Tente outro cartão de crédito no mesmo pedido.
2. Entre em contato com o banco emissor para verificar se há bloqueio ou restrição.
3. Após a liberação, refaça o pagamento pelo carrinho ou pelo pedido.

## ERR-5326: cartão vencido

O código ERR-5326 indica que a data de validade informada para o cartão já passou. Cartões vencidos não podem ser aceitos, mesmo que o número esteja correto. A situação é comum quando o plástico foi substituído pelo banco e o cadastro não foi atualizado.

**O que fazer:**

1. Confira a validade impressa no cartão atual.
2. Atualize os dados do cartão no momento do pagamento, sem usar informações de um plástico antigo.
3. Se o banco enviou um novo cartão, use-o para concluir a compra.

## ERR-5341: código de segurança incorreto

O código ERR-5341 indica que o código de segurança digitado, aquele de três ou quatro dígitos no verso ou na frente do cartão, não confere com o registro do banco. O erro costuma ser de digitação, mas também pode ocorrer com cartões emitidos recentemente.

**O que fazer:**

1. Digite novamente o código de segurança, com cuidado para não trocar números.
2. Confirme se o cartão usado é o mesmo cadastrado no pedido.
3. Se o erro persistir, use outro cartão ou procure o banco para confirmar o código.

## ERR-5343: limite insuficiente para o valor da compra

O código ERR-5343 indica que o limite disponível no cartão não cobre o valor da compra. O limite pode estar comprometido por outras faturas ou compras recentes. Antes de tentar de novo, vale conferir o saldo disponível no aplicativo do banco.

**O que fazer:**

1. Consulte o limite disponível no aplicativo do banco emissor.
2. Divida o pagamento em um cartão diferente ou escolha o Pix, que tem desconto de 5%.
3. Reduza o valor do pedido ou tente o pagamento em outro momento, se preferir.

## ERR-5351: compra bloqueada por suspeita de fraude

O código ERR-5351 indica que a compra foi bloqueada por um sistema de prevenção a fraudes, porque o padrão do pedido foi considerado incomum. Pedidos de valor alto, em endereços novos ou feitos em sequência podem disparar essa verificação.

**O que fazer:**

1. Confirme com o banco emissor que a compra foi reconhecida como sua.
2. Confira se os dados de cadastro e de entrega estão corretos.
3. Após a confirmação, tente o pagamento novamente ou escolha outra forma de pagamento.

## ERR-5353: parcelamento acima do permitido

O código ERR-5353 indica que o número de parcelas escolhido é maior do que o permitido pela loja. O cartão de crédito aceita parcelamento em até 10 vezes sem juros, e a escolha acima desse limite não é processada.

**O que fazer:**

1. Escolha até 10 parcelas no momento do pagamento.
2. Confira se o valor de cada parcela atende ao mínimo indicado.
3. Se preferir, pague à vista pelo Pix, que oferece desconto de 5% e não se combina com parcelamento.

## ERR-5355: parcela abaixo do valor mínimo de R$ 50

O código ERR-5355 indica que o parcelamento escolhido resulta em uma parcela abaixo do valor mínimo de R$ 50. Para cada opção de parcelamento, o valor da parcela não pode ser inferior a esse limite, o que impede pagamentos fracionados demais.

**O que fazer:**

1. Reduza o número de parcelas até que cada uma fique em R$ 50 ou mais.
2. Verifique o valor final do pedido, incluindo frete, antes de escolher as parcelas.
3. Se a compra for pequena, pague à vista para evitar o limite de parcelas.

## ERR-5372: autenticação do banco (3DS) não concluída

O código ERR-5372 indica que a confirmação de segurança exigida pelo banco, conhecida como 3DS, não foi concluída. Ela costuma ser feita por um aviso no aplicativo do banco ou por uma página de verificação. Sem essa etapa, o pagamento não é autorizado.

**O que fazer:**

1. Procure no aplicativo do banco a solicitação de confirmação da compra e aprove-a.
2. Não feche a janela de verificação antes do fim do processo.
3. Refaça o pagamento depois da aprovação, dentro do mesmo pedido.

## ERR-5380: cartão com número inválido

O código ERR-5380 indica que o número informado não corresponde a um cartão válido. A causa mais comum é um dígito digitado errado, mas o erro também pode aparecer ao usar um cartão cancelado ou substituído.

**O que fazer:**

1. Confira o número de dezesseis dígitos do cartão, comparando com o plástico.
2. Verifique se o cartão não foi cancelado ou trocado pelo banco.
3. Digite os dados novamente ou utilize outro cartão válido.

## ERR-5393: bandeira do cartão não aceita

O código ERR-5393 indica que a bandeira do cartão informado não é aceita para pagamento na Loja Verde. A bandeira é identificada pelo número do cartão, e a lista de bandeiras aceitas aparece na tela de pagamento.

**O que fazer:**

1. Consulte a lista de bandeiras aceitas na tela de pagamento.
2. Use um cartão de uma bandeira aceita para concluir o pedido.
3. Se preferir, pague com Pix ou boleto, que não dependem da bandeira do cartão.
