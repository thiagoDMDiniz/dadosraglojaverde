---
doc_id: "LV-PUB-COD-0001"
titulo: "Códigos de erro: Pagamento por Pix"
categoria: "codigos_de_erro"
acesso: "publico"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
familia: "pix"
---

# Códigos de erro: Pagamento por Pix

Este catálogo reúne os códigos de erro da família Pagamento por Pix, usados pelo site e pelo aplicativo Loja Verde quando uma cobrança instantânea não é concluída como esperado. Cada código tem quatro dígitos e segue o formato ERR-NNNN. Os números são parecidos entre si de propósito, por isso confira o código exibido na tela.

Em todos os casos, o pagamento por Pix tem janela de 30 minutos para ser confirmado. Quando o prazo expira sem confirmação, o pedido é cancelado automaticamente. Se a tela mostrar um código diferente dos listados aqui, ou se o problema persistir após as orientações, o SAC pode ser acionado pelo telefone 0800 700 0100, de segunda a sexta, das 8h às 20h, e aos sábados, das 8h às 14h.

## ERR-4202: valor pago diferente do valor do pedido

O código ERR-4202 indica que o valor transferido pelo Pix não corresponde ao total do pedido. Isso costuma acontecer quando o cliente altera o carrinho depois de gerar o QR Code ou digita manualmente um valor diferente do exibido.

O que fazer:
1. Confira o valor total do pedido no aplicativo, em Meus Pedidos.
2. Se o valor pago estiver a maior, aguarde a confirmação do SAC antes de qualquer nova tentativa.
3. Se o valor estiver a menor, gere um novo QR Code com o total atualizado.

Quando procurar o SAC: sempre que o valor pago não aparecer no extrato do banco, anote o número do pedido e o comprovante da transferência.

## ERR-4210: chave Pix inválida na devolução do valor

O código ERR-4210 indica que a chave Pix informada para receber a devolução não existe ou não está ativa no banco do cliente. Sem uma chave válida, o estorno não consegue ser concluído pelo meio original.

O que fazer:
1. Acesse o aplicativo e vá em Meus Pedidos para conferir a chave cadastrada.
2. Atualize a chave Pix no seu banco, caso ela tenha sido desativada ou trocada.
3. Informe ao SAC a chave correta, para que a devolução seja refeita.

## ERR-4217: Pix não confirmado em 30 minutos

O código ERR-4217 indica que o pagamento por Pix não foi confirmado em 30 minutos. O pedido é cancelado automaticamente e nenhum valor é cobrado. Esse é o erro mais comum quando o cliente gera o QR Code e demora para abrir o aplicativo do banco.

O que fazer:
1. Gere um novo pedido pelo aplicativo ou pelo site, sem reaproveitar o QR Code anterior.
2. Pague logo após gerar o código, dentro da janela de 30 minutos.
3. Se o valor já tiver saído da conta, guarde o comprovante e procure o SAC para conferência.

Quando procurar o SAC: somente se houver cobrança no extrato e o pedido aparecer como cancelado.

## ERR-4232: limite do Pix da instituição do cliente excedido

O código ERR-4232 indica que o limite diário de Pix configurado na instituição financeira do cliente foi atingido. A operação é recusada pelo banco antes de chegar à Loja Verde.

O que fazer:
1. Consulte o limite de Pix no aplicativo do seu banco.
2. Aumente o limite temporariamente, se a sua instituição permitir, ou faça o pagamento no dia seguinte.
3. Como alternativa, escolha cartão de crédito ou boleto no checkout.

Quando procurar o SAC: não é necessário, pois o ajuste depende apenas do banco do cliente.

## ERR-4249: pagamento Pix duplicado para o mesmo pedido

O código ERR-4249 indica que dois pagamentos Pix chegaram para o mesmo pedido. Isso acontece quando o cliente paga duas vezes o mesmo QR Code, ou quando paga um código antigo depois de gerar outro.

O que fazer:
1. Verifique no extrato do banco se as duas transferências saíram da conta.
2. Não faça uma terceira tentativa de pagamento para o mesmo pedido.
3. Envie os dois comprovantes ao SAC para que o valor excedente seja devolvido.

Quando procurar o SAC: sempre que houver dois comprovantes para um único pedido. Tenha em mãos o número do pedido.

## ERR-4271: QR Code do Pix expirado antes do pagamento

O código ERR-4271 indica que o QR Code foi gerado, mas o pagamento não foi feito antes de ele expirar. Como o prazo máximo do Pix é de 30 minutos, códigos antigos não podem ser pagos depois desse período.

O que fazer:
1. Volte ao pedido e gere um novo QR Code.
2. Copie o código ou escaneie a tela no mesmo momento em que o gerar.
3. Pague sem demora dentro da janela de 30 minutos.

Quando procurar o SAC: não é preciso, pois basta gerar um novo código.

## ERR-4281: Pix bloqueado pelo banco no período noturno

O código ERR-4281 indica que a instituição financeira do cliente bloqueou a transferência Pix no período noturno, por política de segurança do próprio banco. A Loja Verde não tem controle sobre esse bloqueio.

O que fazer:
1. Verifique nas configurações do aplicativo do banco se há horário de bloqueio ativo.
2. Faça o pagamento em horário liberado, dentro do prazo do QR Code.
3. Se preferir, use outra forma de pagamento disponível no checkout.

Quando procurar o SAC: apenas se o bloqueio persistir durante o dia e não houver explicação pelo banco.

## ERR-4293: pagamento feito por CPF diferente do titular do pedido

O código ERR-4293 indica que o Pix foi enviado por uma conta cujo CPF não corresponde ao titular do pedido. Por segurança, a Loja Verde não aceita pagamentos de terceiros sem validação.

O que fazer:
1. Confira no pedido qual CPF está cadastrado como titular.
2. Faça o pagamento a partir de uma conta cujo titular seja a mesma pessoa do pedido.
3. Caso o pagamento precise ser feito por outra pessoa, procure o SAC antes de tentar novamente.

Quando procurar o SAC: se o titular do pedido for a mesma pessoa e o erro continuar aparecendo. Nunca informe senhas ou códigos de segurança durante o atendimento.

## ERR-4294: falha de comunicação com o banco recebedor

O código ERR-4294 indica que houve falha temporária de comunicação entre a Loja Verde e o banco que recebe o Pix. A transferência pode ter sido iniciada, mas a confirmação não chegou ao sistema.

O que fazer:
1. Aguarde alguns minutos e atualize a tela do pedido.
2. Confira no extrato do seu banco se o valor saiu da conta.
3. Se o valor saiu e o pedido não foi confirmado, guarde o comprovante.

Quando procurar o SAC: sempre que o valor tiver saído da conta e o pedido permanecer sem confirmação. Informe o número do pedido e o horário da transferência.

## ERR-4299: Pix agendado não aceito para o pedido

O código ERR-4299 indica que o cliente tentou pagar por Pix agendado, modalidade que o pedido não aceita. O pagamento precisa ser feito imediatamente, dentro da janela de confirmação.

O que fazer:
1. Cancele o agendamento no aplicativo do banco, para evitar uma cobrança futura.
2. Gere um novo QR Code no pedido e pague na modalidade Pix imediato.
3. Se preferir, escolha boleto ou cartão de crédito no checkout.

Quando procurar o SAC: se o agendamento já tiver sido debitado e o pedido não confirmado, procure o atendimento com o comprovante em mãos.
