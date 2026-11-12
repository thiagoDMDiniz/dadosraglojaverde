---
doc_id: "LV-INT-POS-0005"
titulo: "Post-mortem 2026-07-21: Atraso da transportadora principal"
categoria: "postmortem"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Post-mortem 2026-07-21: Atraso da transportadora principal

**USO INTERNO** · Data do incidente: 2026-07-21 (21/07/2026) · Severidade: média · Responsável pelo documento: Gerência de Logística

## Resumo

Entre o fim de junho e o dia 21/07/2026, a transportadora principal da Loja Verde acumulou atrasos em entregas do Sudeste e do Nordeste. Um conjunto de pedidos ultrapassou o prazo de cinco dias úteis, o que aciona o cupom automático ATRASO25, de R$ 25. O atraso teve origem em um gargalo no centro de distribuição de Contagem, somado à paralisação de três dias de uma das filiais parceiras. Ao longo da semana, o cupom ATRASO25 foi emitido para 764 clientes de forma automática, como prevê a política.

O incidente foi formalmente declarado em 21/07/2026, quando o indicador de entregas no prazo caiu abaixo de 80% por dois dias consecutivos.

## Linha do tempo (horários)

- 22/06: o centro de distribuição de Contagem registra fila de expedição acima do normal após a troca de um turno de conferência.
- 08/07: a transportadora informa redução de frota por motivo operacional e pede revisão de rotas no Sudeste.
- 15/07: a paralisação de uma filial parceira em Betim adiciona cerca de 300 pedidos à fila de entrega.
- 21/07, 09h00: o painel de logística mostra 58% de entregas no prazo nas últimas 48 horas e o incidente é aberto.
- 21/07, 11h30: a Gerência de Logística aprova rota emergencial com uma segunda transportadora para capitais do Sudeste.
- 21/07, 16h00: o sistema de cupons emite o ATRASO25 automaticamente para os pedidos que passaram de cinco dias úteis.
- 24/07: a fila de expedição volta ao nível normal e o incidente é encerrado.

## Impacto

Foram emitidos 764 cupons ATRASO25, no valor total de R$ 19.100,00. O SAC recebeu 412 chamados sobre atraso, e a maior parte deles era de clientes de Belo Horizonte e Contagem. Houve também 57 pedidos de cancelamento, dos quais 41 foram revertidos após a atualização da previsão de entrega.

A reputação da rede sofreu em redes sociais, principalmente pela comparação com a expectativa de entrega em até três dias úteis para capitais do Sudeste. A unidade Contagem precisou reforçar o balcão de retirada, já que muitos clientes preferiram buscar o pedido na loja.

## Causa raiz

A causa primária foi a falta de um plano de contingência com a transportadora secundária. O contrato principal previa apenas dois dias de tolerância para variações de frota, e o gargalo de conferência no centro de distribuição de Contagem foi tratado como exceção local, e não como risco da operação.

Como fator contribuinte, a comunicação de atraso ao cliente foi feita apenas por e-mail, e a previsão de entrega não foi atualizada no aplicativo, o que aumentou o volume de contatos ao SAC.

## Ações imediatas

- Ativação de rota emergencial com segunda transportadora para capitais do Sudeste, a partir de 21/07.
- Emissão automática do cupom ATRASO25 para os pedidos fora do prazo, conforme a política vigente.
- Atualização da previsão de entrega no aplicativo e envio de SMS para pedidos em atraso.
- Reforço de três operadores no SAC durante a semana, com roteiro de atendimento para atrasos.

## Ações preventivas com responsáveis e prazos

- Contrato de contingência com transportadora secundária para cobrir até 20% do volume do Sudeste. Responsável: Gerência de Logística. Prazo: 60 dias corridos.
- Indicador diário de entregas no prazo por centro de distribuição e por região, com alerta abaixo de 85%. Responsável: Coordenação de Dados Logísticos. Prazo: 30 dias corridos.
- Revisão do turno de conferência de Contagem, com dimensionamento de equipe conforme volume sazonal. Responsável: Gerência do Centro de Distribuição. Prazo: 45 dias corridos.
- Comunicação de atraso por aplicativo, além de e-mail e SMS, com a nova previsão de entrega. Responsável: Produto Digital. Prazo: 30 dias corridos.

## Lições aprendidas

O atraso ficou visível para a operação muito antes de ser tratado como incidente. Indicadores que mostram tendência, e não só o estado final, teriam permitido reagir uma semana antes. A equipe também concluiu que o cupom automático funcionou como previsto, mas que o custo da compensação precisa entrar no planejamento de cada rota.
