---
doc_id: "LV-INT-POS-0008"
titulo: "Post-mortem 2026-02-18: Envio indevido de e-mail de marketing"
categoria: "postmortem"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Post-mortem 2026-02-18: Envio indevido de e-mail de marketing

USO INTERNO. Documento restrito ao encarregado de dados (LGPD), à gerência de marketing e à diretoria de operações.

## Resumo

Em 18/02/2026, uma campanha de e-mail de marketing sobre a linha de jardinagem foi enviada para uma lista de contatos que incluía clientes que haviam cancelado o recebimento de comunicações promocionais. O erro foi causado pela seleção de uma lista antiga de contatos. Não houve exposição de dados sensíveis: o e-mail continha apenas o nome do destinatário e o convite para a campanha. Cerca de 1.800 mensagens foram enviadas indevidamente, segundo o relatório da ferramenta de disparo.

## Linha do tempo (horários)

- 07h55: o analista de marketing agenda o disparo da campanha para as 08h00, usando a lista de segmentação de jardinagem.
- 08h00: o disparo é executado conforme o agendamento.
- 08h27: duas clientes respondem à mensagem informando que cancelaram o recebimento de promoções.
- 08h35: o gerente de marketing identifica que a lista utilizada não passou pela filtragem de descadastro.
- 08h41: o disparo restante é cancelado na ferramenta, e a lista é bloqueada para novos envios.
- 09h10: o encarregado de dados é comunicado e inicia o registro do incidente.
- 10h30: o SAC recebe mensagens de clientes que questionam o e-mail, e um roteiro de resposta é enviado à equipe.

## Impacto

O envio atingiu clientes que não deveriam receber a comunicação, o que afeta a confiança e pode gerar reclamações à ouvidoria. Não houve envio de dados de pagamento, senhas ou informações de compra. A ouvidoria registrou quatro manifestações até o fim do dia, todas respondidas com a explicação do ocorrido e com a confirmação do descadastro. O encarregado de dados avaliou o caso como incidente de baixo risco, sem necessidade de comunicação à autoridade nacional, mas com registro formal.

## Causa raiz

A lista de segmentação foi criada em 2024 e reutilizada sem atualização. O processo de disparo não exigia a conferência com a base de descadastro antes do agendamento, e a checagem dependia da memória do analista. Além disso, a ferramenta permitia agendar campanhas sem aprovação de segunda pessoa para listas com mais de mil contatos.

## Ações imediatas

- Cancelamento do disparo restante e bloqueio da lista utilizada.
- Envio de confirmação de descadastro aos clientes que reclamaram.
- Registro formal do incidente com o encarregado de dados.
- Roteiro de resposta para o SAC e para a ouvidoria.

## Ações preventivas com responsáveis e prazos

- Tornar obrigatória a filtragem pela base de descadastro antes de qualquer agendamento, sob responsabilidade da gerência de marketing, antes da próxima campanha.
- Exigir aprovação de uma segunda pessoa para listas com mais de mil contatos, sob responsabilidade da equipe de ferramentas digitais, com configuração feita no sistema de disparo.
- Revisar as listas de segmentação com mais de um ano de idade, sob responsabilidade do analista de dados de marketing, até o fim do semestre.
- Incluir a checagem de descadastro no checklist de campanha, assinado pelo gerente responsável.

## Lições aprendidas

O incidente reforça que a proteção de dados depende de processos que não dependem da atenção individual. A lista antiga deveria ter sido revalidada antes do uso, e o disparo deveria exigir uma segunda conferência. A resposta rápida da equipe, com o cancelamento em menos de uma hora, limitou o alcance do erro. Ainda assim, o episódio mostra que a ouvidoria precisa de um roteiro pronto, para que as manifestações sejam respondidas com a mesma clareza em todos os canais.
