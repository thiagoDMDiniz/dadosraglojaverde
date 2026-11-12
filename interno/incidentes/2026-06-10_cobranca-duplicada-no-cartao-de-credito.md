---
doc_id: "LV-INT-POS-0004"
titulo: "Post-mortem 2026-06-10: Cobrança duplicada no cartão de crédito"
categoria: "postmortem"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Post-mortem 2026-06-10: Cobrança duplicada no cartão de crédito

**USO INTERNO** · Data do incidente: 2026-06-10 (10/06/2026) · Severidade: alta · Responsável pelo documento: Gerência de Operações de Pagamentos

## Resumo

Em 10/06/2026, parte dos pedidos pagos com cartão de crédito foi cobrada duas vezes pela operadora. O problema ocorreu quando o cliente, diante de uma resposta demorada do checkout, clicava novamente em "Confirmar pagamento". Em alguns casos, o sistema também recebia a segunda autorização do mesmo pedido após uma recusa intermediária, e a operadora registrava as duas como aprovadas. A falha afetou 58 pedidos, e todos foram estornados manualmente.

O código ERR-5308 apareceu para parte dos clientes que tentaram de novo logo após a primeira recusa, o que gerou confusão, porque a primeira cobrança já estava aprovada em alguns casos.

## Linha do tempo (horários)

- 10h02: o financeiro identifica dois lançamentos de mesmo valor para o mesmo pedido em conciliação de fim de manhã.
- 10h20: o SAC começa a receber chamados de clientes que aparecem com duas cobranças na fatura.
- 10h45: a equipe de pagamentos abre o incidente e suspende temporariamente a repetição automática de autorização.
- 11h30: a causa é localizada no tratamento de tempo limite do gateway, que reenvia a requisição quando a resposta não chega a tempo.
- 12h10: a repetição automática é desativada em definitivo e o checkout passa a bloquear o segundo clique durante o processamento.
- 13h00: o incidente é encerrado após conferência de todos os pedidos do dia.

## Impacto

Foram identificados 58 pedidos com cobrança duplicada, totalizando R$ 23.410,00 em valores lançados a mais. Todos foram estornados manualmente, com prazo de até duas faturas para aparecer na fatura do cliente, conforme a política de reembolso no cartão de crédito. Três clientes já tinham pago a fatura antes do estorno e receberam o crédito em conta, com acompanhamento do SAC.

O SAC registrou 143 contatos no dia, e o tempo de espera médio chegou a 19 minutos. O impacto de confiança foi alto, porque vários clientes relataram que deixaram de comprar pelo site após o episódio.

## Causa raiz

O gateway de pagamentos possuía uma regra de reenvio automático de autorização em caso de timeout de resposta. Essa regra foi criada para evitar pedidos perdidos, mas não verificava se a primeira autorização tinha sido concluída. Somado ao clique repetido do cliente, isso gerou duas autorizações aprovadas para o mesmo pedido.

Não existia uma chave de idempotência persistida entre o checkout e o gateway, o que permitia que a mesma intenção de pagamento fosse processada duas vezes.

## Ações imediatas

- Desativação da repetição automática de autorização até a nova versão estar validada.
- Bloqueio do botão de confirmação durante o processamento, com indicação visual de espera.
- Estorno manual dos 58 pedidos, com registro de comprovante no sistema de pedidos.
- Comunicado padrão no SAC para explicar o prazo do estorno e orientar o cliente a não pagar de novo.

## Ações preventivas com responsáveis e prazos

- Implantação de chave de idempotência por pedido em todas as chamadas de autorização. Responsável: Equipe de Integração de Pagamentos. Prazo: 30 dias corridos.
- Conciliação automática entre pedidos e autorizações ao fim de cada hora, com alerta de duplicidade. Responsável: Controladoria. Prazo: 20 dias corridos.
- Revisão de mensagens de erro do checkout para diferenciar recusa de pagamento de falha de comunicação, com orientação clara ao cliente. Responsável: Produto Digital. Prazo: 45 dias corridos.
- Teste de estresse com cliques repetidos e respostas lentas do gateway, realizado antes de cada mudança no fluxo de pagamento. Responsável: Qualidade de Software. Prazo: próxima mudança programada.

## Lições aprendidas

Um mecanismo de segurança para evitar perda de pedido acabou produzindo cobrança em duplicidade. A lição principal é que toda operação financeira precisa de identificador único, para que o sistema reconheça uma tentativa repetida como a mesma operação.

Também se reforçou que a conciliação não deve ser apenas diária. Pegar o problema às 10h02, e não no dia seguinte, reduziu o número de clientes afetados e permitiu que a comunicação fosse feita antes que o cliente precisasse procurar o banco emissor.
