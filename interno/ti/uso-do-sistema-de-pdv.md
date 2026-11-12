---
doc_id: "LV-INT-TI-0005"
titulo: "Uso do sistema de PDV"
categoria: "ti"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Uso do sistema de PDV

**USO INTERNO** | Área de Tecnologia da Informação e Operações de Caixa

## Visão geral

O sistema de PDV é a ferramenta usada em todos os caixas das unidades físicas da Loja Verde para registrar vendas, aplicar descontos autorizados, receber pagamentos e emitir o comprovante da compra. Ele se comunica com o estoque e com o programa Clube Verde, de modo que cada venda atualiza a posição de produtos e os pontos do cliente. Este documento descreve a rotina básica de operação e os cuidados que o operador deve ter para evitar divergências no fechamento do caixa.

## Abertura do caixa

Antes de iniciar o turno, o operador faz login com sua credencial pessoal, confere se a impressora de cupons e o leitor de código de barras estão conectados e registra o fundo de troco informado pelo supervisor. Um caixa aberto com credencial de outro colaborador gera registro de inconsistência e deve ser corrigido antes da primeira venda. Se o sistema apresentar mensagem de versão desatualizada, o operador não deve ignorá-la e sim acionar o suporte, pois versões antigas podem calcular preços de forma diferente.

## Registro de vendas e descontos

Cada item é lido pelo leitor ou digitado pelo código interno quando a etiqueta estiver danificada. Antes de finalizar a venda, o operador confere a descrição e o preço exibidos na tela com a etiqueta física. Descontos só podem ser aplicados quando houver cupom válido ou autorização do supervisor dentro da alçada prevista, e o sistema registra quem autorizou cada desconto. Cupons vencidos ou inexistentes são recusados automaticamente, e o cliente deve ser orientado a consultar os cupons vigentes no aplicativo.

## Formas de pagamento

O PDV aceita Pix, débito, crédito, vale-compras e cartão-presente. No Pix, o QR Code expira em 30 minutos; se o pagamento não for confirmado nesse intervalo, o sistema exibe o código ERR-4217 e cancela o pedido automaticamente, sem cobrança. Quando a operadora recusar um cartão, o sistema exibe o código ERR-5308, e o operador deve pedir ao cliente que tente outro meio de pagamento ou que procure o banco emissor, sem repetir a tentativa várias vezes seguidas. Nunca peça ao cliente que informe senha ou código de segurança no caixa.

## Sangria, suprimento e fechamento

Retiradas de dinheiro durante o turno são chamadas de sangria e devem ser registradas no próprio sistema, com o motivo e a assinatura do supervisor no comprovante. Reforços de troco são chamados de suprimento e seguem o mesmo procedimento. No fechamento, o operador conta o dinheiro, confere os totais por forma de pagamento apresentados pelo PDV e registra eventuais diferenças. Diferenças não justificadas devem ser comunicadas ao supervisor antes de o caixa ser encerrado, e nunca devem ser compensadas com valores do próprio bolso.

## Falhas e queda do sistema

Se o PDV ficar indisponível, o operador deve anotar o horário, o último item registrado e os cupons emitidos, sem tentar reiniciar o equipamento por conta própria enquanto o suporte não orientar. Em caso de queda prolongada, o supervisor aciona a equipe de TI pelo ramal técnico e a gerência é informada para avaliar a abertura de caixa alternativo. Após a normalização, as vendas registradas em contingência devem ser conferidas item a item antes de qualquer lançamento definitivo.

## Boas práticas de atendimento no caixa

O operador deve manter a tela e o teclado organizados, sem papéis ou copos sobre o equipamento, e nunca deixar o caixa aberto e sem supervisão durante intervalos. Em filas longas, o colaborador deve avisar o gerente para avaliar reforço de caixa, pois demora excessiva é uma das reclamações mais frequentes registradas no SAC. O cupom deve ser entregue sempre, inclusive quando o cliente não o solicitar, pois ele é a comprovação necessária para trocas e para o acompanhamento da garantia.
