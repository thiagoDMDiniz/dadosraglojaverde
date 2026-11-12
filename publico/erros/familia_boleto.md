---
doc_id: "LV-PUB-COD-0003"
titulo: "Códigos de erro: Pagamento com boleto"
categoria: "codigos_de_erro"
acesso: "publico"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
familia: "boleto"
---

# Códigos de erro: Pagamento com boleto

Este catálogo explica os códigos de erro que podem aparecer quando o pagamento é feito com boleto bancário. Cada código tem quatro dígitos, e códigos parecidos podem ter causas bem diferentes. Confira o número exato na tela antes de seguir uma orientação. Lembre-se de que o boleto vence em 2 dias úteis. Para ajuda adicional, o SAC atende pelo 0800 700 0100.

## ERR-5601: boleto vencido

O código ERR-5601 indica que o prazo de pagamento do boleto terminou antes de o valor ser compensado. Como o boleto vence em 2 dias úteis, a situação ocorre quando o pagamento não foi feito dentro desse intervalo. O pedido continua registrado, mas o boleto original não pode mais ser pago.

**O que fazer:**

1. Verifique a data de vencimento impressa no boleto e no pedido.
2. Solicite a emissão de um novo boleto pela tela do pedido, se o pedido ainda estiver ativo.
3. Pague o novo boleto dentro do prazo, preferindo o aplicativo ou o internet banking.

## ERR-5626: código de barras inválido

O código ERR-5626 indica que a linha digitável ou o código de barras informado não foi reconhecido pelo sistema bancário. Erros de digitação e fotografias borradas são as causas mais comuns. O valor do boleto não é cobrado enquanto o código não for validado.

**O que fazer:**

1. Confira a linha digitável com atenção, número por número, comparando com o documento original.
2. Se estiver pagando por foto, use uma imagem nítida e reta do código.
3. Caso o erro continue, baixe o PDF do boleto diretamente no pedido e pague por ele.

## ERR-5628: banco emissor fora do ar

O código ERR-5628 indica que o banco responsável pelo boleto está temporariamente indisponível. A falha não depende do cliente e costuma ser resolvida em pouco tempo. Enquanto o banco não volta, o pagamento não pode ser confirmado naquele momento.

**O que fazer:**

1. Aguarde alguns minutos e tente o pagamento novamente.
2. Evite pagar em horários de manutenção anunciados pelo próprio banco.
3. Se o boleto estiver perto do vencimento, procure o SAC para avaliar a emissão de uma nova via.

## ERR-5631: pagamento não compensado em 3 dias úteis

O código ERR-5631 indica que o pagamento do boleto foi feito, mas não foi compensado no prazo de 3 dias úteis. A compensação depende do processamento bancário, que pode ser mais lento em alguns casos. Guarde o comprovante até a confirmação ser concluída.

**O que fazer:**

1. Guarde o comprovante de pagamento com data, hora e valor.
2. Acompanhe o status do pedido em Meus Pedidos durante os dias úteis seguintes.
3. Se a compensação não aparecer após o prazo, procure o SAC com o comprovante em mãos.

## ERR-5639: boleto já pago anteriormente

O código ERR-5639 indica que o boleto informado já foi quitado. Isso acontece quando o cliente paga duas vezes, seja pelo aplicativo, seja pelo banco. O segundo pagamento não gera um novo pedido nem uma nova cobrança para o mesmo título.

**O que fazer:**

1. Verifique em Meus Pedidos se o pagamento aparece como confirmado.
2. Compare o comprovante do banco com o status do pedido.
3. Se houver cobrança duplicada, procure o SAC para tratar o valor pago a mais.

## ERR-5642: valor pago diferente do boleto

O código ERR-5642 indica que o valor pago no banco não coincide com o valor do boleto emitido. Diferenças podem surgir por juros aplicados depois do vencimento, por pagamentos parciais ou por digitação incorreta do valor no caixa eletrônico.

**O que fazer:**

1. Confira o valor impresso no boleto e compare com o comprovante do pagamento.
2. Não tente completar o valor por conta própria, pois isso pode gerar um novo título.
3. Entre em contato com o SAC informando o valor pago e o número do pedido.

## ERR-5645: segunda via indisponível

O código ERR-5645 indica que a segunda via do boleto não pode ser gerada no momento. A emissão pode estar bloqueada por uma restrição do pedido ou por instabilidade no serviço bancário. A situação não afeta o pedido em si.

**O que fazer:**

1. Tente gerar a segunda via novamente depois de alguns minutos.
2. Verifique se o pedido não está cancelado ou em análise.
3. Se a segunda via continuar indisponível, procure o SAC para que a equipe emita o documento.

## ERR-5655: pedido cancelado após o vencimento

O código ERR-5655 indica que o pedido foi cancelado automaticamente porque o boleto não foi pago até a data de vencimento. Nesse caso, o pagamento não pode ser aceito para o pedido original, e nenhuma cobrança é feita pelo boleto cancelado.

**O que fazer:**

1. Confira em Meus Pedidos o status de cancelamento e a data do vencimento.
2. Refaça o pedido com os mesmos produtos, se ainda tiver interesse na compra.
3. Escolha uma forma de pagamento mais rápida, como o Pix, para concluir a nova compra.

## ERR-5661: limite de reemissões atingido

O código ERR-5661 indica que o número máximo de reemissões de boleto para aquele pedido já foi alcançado. O limite existe para evitar que um mesmo título seja pago de formas diferentes. Quando o limite é atingido, a loja orienta o pagamento por outra forma.

**O que fazer:**

1. Verifique se alguma das versões anteriores do boleto já foi paga.
2. Escolha outro meio de pagamento, como Pix ou cartão de crédito, para o pedido.
3. Caso precise de uma exceção, procure o SAC para avaliar a situação.

## ERR-5669: CPF do pagador diferente do cadastro

O código ERR-5669 indica que o CPF da pessoa que pagou o boleto é diferente do CPF cadastrado no pedido. Essa verificação protege o cliente contra pagamentos feitos por terceiros sem vínculo com a compra.

**O que fazer:**

1. Confira o CPF cadastrado no pedido, em Meus Dados.
2. Informe o titular da compra a pagar o boleto, ou peça que o cadastro seja ajustado antes do pagamento.
3. Se o CPF estiver correto e o erro continuar, procure o SAC com o número do pedido.
