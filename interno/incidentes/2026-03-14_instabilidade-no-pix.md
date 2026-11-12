---
doc_id: "LV-INT-POS-0001"
titulo: "Post-mortem 2026-03-14: Instabilidade no Pix"
categoria: "postmortem"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Post-mortem 2026-03-14: Instabilidade no Pix

**USO INTERNO** · Data do incidente: 2026-03-14 (14/03/2026) · Severidade: alta · Responsável pelo documento: Gerência de Operações de Pagamentos

## Resumo

Na tarde de 14/03/2026, o fluxo de pagamentos por Pix da Loja Verde apresentou atraso na confirmação das transações. Entre 15h10 e 17h45, uma parcela relevante dos pedidos ficou com status "aguardando pagamento" mesmo após o cliente ter efetuado a transferência. Após 30 minutos sem confirmação, o sistema encerrou a tentativa e exibiu o código ERR-4217 na tela de finalização do site e do aplicativo. Conforme a política vigente, esses pedidos foram cancelados automaticamente e nenhum valor foi cobrado.



## Linha do tempo (horários)

- 15h10: o time de SAC registra o primeiro chamado de cliente informando que o Pix foi pago e o pedido segue pendente.
- 15h22: o monitor de filas do meio de pagamento acusa atraso acima do limite de 60 segundos na confirmação de cobranças.
- 15h31: o plantão de sustentação abre o incidente interno e comunica a Gerência de Operações de Pagamentos.
- 15h48: o volume de chamados sobe e o código ERR-4217 aparece em capturas de tela enviadas pelos clientes às redes sociais.
- 16h05: a equipe de integração identifica a fila de retorno do provedor com mensagens acumuladas e reinicia o consumidor responsável.
- 16h40: as confirmações voltam ao normal, porém o backlog de notificações leva cerca de uma hora para ser processado.
- 17h45: a Gerência declara o fim do incidente após conferir que nenhuma nova cobrança ficou sem baixa.

## Impacto

Foram afetados 412 pedidos com tentativa de pagamento por Pix nesse intervalo. Desses, 173 foram confirmados tardiamente pela fila de retorno e não geraram cancelamento. Os demais 239 receberam o ERR-4217 e foram cancelados automaticamente, sem cobrança. Houve 96 chamados no SAC sobre o tema, com tempo médio de espera de 14 minutos, acima da meta de 5 minutos para o período.

## Causa raiz

A análise de logs mostrou que o consumidor de mensagens de retorno do provedor de Pix ficou travado após uma reconexão de rede no fim da manhã. Como o processo não tinha tempo limite de reprocessamento, as mensagens se acumularam na fila sem gerar alerta, porque o alarme monitorava apenas erros e não atrasos. Quando a fila chegou a cerca de 9 mil itens, o tempo de confirmação já estava acima do limite e o temporizador do checkout expirou.

Em resumo, faltavam dois controles: alarme de latência na fila e reinício automático do consumidor após falha de conexão.

## Ações imediatas

- Reinício controlado do consumidor de retorno, feito pela equipe de plantão às 16h05.
- Reprocessamento manual da fila acumulada, com conferência dos pedidos cancelados que possuíam comprovante de pagamento.
- Publicação de comunicado padrão no site e no aplicativo, orientando o cliente a não repetir o pagamento antes de conferir o pedido em Meus Pedidos.
- Estorno de 22 cobranças duplicadas, concluído em até 10 dias úteis.

## Ações preventivas com responsáveis e prazos

- Alarme de latência para a fila de retorno, com limite de 60 segundos e escalonamento automático. Responsável: Coordenação de Plataforma. Prazo: 30 dias corridos.
- Reinício automático do consumidor após queda de conexão, com registro em log. Responsável: Equipe de Integração de Pagamentos. Prazo: 45 dias corridos.
- Revisão do tempo de expiração do checkout para Pix, mantendo a regra de 30 minutos e incluindo mensagem de espera ao cliente. Responsável: Produto Digital. Prazo: 60 dias corridos.
- Teste de carga com simulação de queda de rede, executado antes de cada grande campanha. Responsável: Qualidade de Software. Prazo: próxima campanha programada.

## Lições aprendidas

O time percebeu que a ausência de alarme de atraso escondeu o problema por mais de meia hora. Monitorar apenas erros não basta quando a falha é de lentidão. Outra lição é que a comunicação precisa ser antecipada: o comunicado padrão só foi publicado às 16h30, e nesse intervalo o SAC recebeu chamados que poderiam ter sido evitados com uma mensagem na tela de pagamento.
