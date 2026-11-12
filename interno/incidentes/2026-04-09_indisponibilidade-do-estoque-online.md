---
doc_id: "LV-INT-POS-0006"
titulo: "Post-mortem 2026-04-09: Indisponibilidade do estoque online"
categoria: "postmortem"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Post-mortem 2026-04-09: Indisponibilidade do estoque online

**USO INTERNO** · Data do incidente: 2026-04-09 (09/04/2026) · Severidade: média · Responsável pelo documento: Coordenação de Estoque e E-commerce

## Resumo

Em 09/04/2026, a consulta de disponibilidade de produtos no site e no aplicativo deixou de refletir o estoque real das lojas físicas durante a maior parte da manhã. Itens esgotados nas unidades apareciam como disponíveis para compra online, e alguns produtos com saldo positivo apareciam como indisponíveis. O problema foi causado por uma divergência de sincronização entre o sistema de estoque e o catálogo digital, que só foi corrigida após o reprocessamento completo das contagens.

Durante a janela, foram aceitos pedidos de itens que não existiam fisicamente em uma das unidades, o que obrigou a equipe a cancelar ou remanejar parte deles.

## Linha do tempo (horários)

- 07h40: a equipe de atendimento percebe clientes reclamando de pedidos de retirada na loja que não podiam ser separados.
- 08h05: a Coordenação de Estoque confirma diferença entre o saldo do PDV da unidade Pampulha e o saldo exibido no site para a mesma linha de produtos.
- 08h20: o incidente é aberto e a publicação de novas atualizações de estoque é pausada para evitar propagar dados inconsistentes.
- 09h10: a integração identifica que a fila de atualização noturna não foi concluída e que um lote de 3 mil registros ficou com data de referência antiga.
- 10h35: o lote é reprocessado e a consistência é verificada em amostra de dez unidades.
- 11h50: a publicação automática é reativada e o site passa a exibir o saldo atualizado.
- 13h00: o incidente é encerrado, com conferência manual dos pedidos abertos desde as 7h da manhã.

## Impacto

Foram registrados 187 pedidos com itens marcados como disponíveis que não puderam ser atendidos pela unidade indicada. Desses, 128 foram remanejados para outra unidade com estoque, 41 tiveram o prazo de entrega ajustado e 18 foram cancelados, com aviso ao cliente por e-mail e SMS.

A unidade Pampulha foi a mais afetada, com cerca de 40% dos casos, por ter passado por inventário rotativo no fim da semana anterior.

## Causa raiz

A investigação identificou que a fila de atualização do estoque noturno tinha um limite de tamanho de lote que não era revisado desde a migração do catálogo. Quando o volume de transferências entre unidades aumentou com a campanha de primavera, o lote passou a ser rejeitado parcialmente sem gerar erro visível, e os registros não processados mantiveram a data anterior.

O sistema de estoque tinha validação de integridade apenas no total de itens, e não por unidade. Por isso, a divergência não apareceu nos painéis de monitoramento até que um cliente a reportasse.

## Ações imediatas

- Pausa da publicação automática de saldo entre 08h20 e 11h50.
- Reprocessamento do lote de 3 mil registros e conferência em amostra de dez unidades, incluindo Savassi e Contagem.
- Conferência manual dos 187 pedidos afetados, com remanejamento ou cancelamento conforme o caso.
- Comunicado interno para os gerentes de unidade, para que confirmem o saldo físico dos itens citados antes de separar pedidos.

## Ações preventivas com responsáveis e prazos

- Validação de integridade por unidade e por linha de produto, com alerta quando qualquer loja ficar mais de 2 horas sem atualização. Responsável: Coordenação de Estoque. Prazo: 30 dias corridos.
- Revisão do limite de tamanho de lote e registro de rejeições parciais em log visível no painel. Responsável: Equipe de Integração. Prazo: 20 dias corridos.
- Inclusão de uma etapa de conferência por amostragem antes de qualquer campanha que aumente o volume de transferências entre unidades. Responsável: Gerência de Logística. Prazo: antes da próxima campanha.
- Inventário rotativo com conferência do saldo do site após cada ciclo de contagem. Responsável: Supervisão de Unidades. Prazo: 60 dias corridos.

## Lições aprendidas

A divergência entre loja e site não era um problema de dados ruins na origem, e sim de uma validação que olhava apenas o total. Uma lição prática é que um painel verde não garante consistência, e a checagem precisa ser feita no nível em que o cliente enxerga o produto, que é a unidade.
