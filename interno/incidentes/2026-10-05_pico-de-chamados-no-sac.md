---
doc_id: "LV-INT-POS-0010"
titulo: "Post-mortem 2026-10-05: Pico de chamados no SAC"
categoria: "postmortem"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Post-mortem 2026-10-05: Pico de chamados no SAC

**USO INTERNO** · Data do incidente: 2026-10-05 (05/10/2026) · Severidade: média · Responsável pelo documento: Coordenação do SAC e Atendimento

## Resumo

No dia 05/10/2026, o SAC registrou um pico de chamados sobre o código ERR-7142, que indica que o endereço informado pelo cliente não é atendido pela transportadora. O volume chegou a quase o dobro da média de uma terça-feira comum, e o tempo de espera ultrapassou 20 minutos no fim da manhã. A causa principal foi uma nova regra de cobertura, publicada na véspera, que retirou de algumas rotas de entrega bairros de Contagem e de Betim, sem comunicação prévia ao atendimento.

Os clientes que receberam o ERR-7142 não tinham clareza sobre o motivo e perguntavam se o site estava fora do ar, o que gerou tentativas repetidas de pagamento e aumento da fila telefônica.

## Linha do tempo (horários)

- 04/10, 18h00: a área de logística publica a atualização de cobertura de entregas, sem aviso à equipe de atendimento.
- 05/10, 08h30: o primeiro lote de chamados sobre ERR-7142 chega pelo WhatsApp oficial, (31) 99000-0100, e pelo chat do aplicativo.
- 09h15: a supervisão percebe que o volume de chamados com o mesmo código ultrapassou a média diária em quatro vezes.
- 09h40: o incidente é aberto e a equipe de atendimento recebe o roteiro provisório para ERR-7142.
- 10h30: a fila telefônica chega a 22 minutos de espera e são abertos dois postos extras de atendimento.
- 11h20: a Logística confirma a regra de cobertura e disponibiliza a lista de bairros atualizada.
- 12h45: a orientação padrão é publicada no aplicativo e o volume de contatos começa a cair.
- 16h00: o incidente é encerrado com o volume da tarde dentro da média.

## Impacto

Foram registrados 503 contatos sobre o código, somando telefone, WhatsApp, chat e e-mail. O tempo médio de espera no telefone foi de 16 minutos, acima da meta de 5 minutos para o período. Cerca de 40% dos clientes afetados já tinham tentado o pagamento mais de uma vez, o que exigiu conferência para evitar cobranças duplicadas, todas canceladas antes da confirmação.



## Causa raiz

A atualização de cobertura foi aplicada no sistema de entregas sem integração com a base do atendimento. Como o código ERR-7142 é apresentado ao cliente sem explicação detalhada, muitos interpretaram a mensagem como falha técnica do site e não como restrição de endereço.

Não havia um procedimento de comunicação prévia para mudanças de cobertura, e a equipe de atendimento não recebia a lista de bairros afetados antes da publicação.

## Ações imediatas

- Disponibilização da lista de bairros afetados ao atendimento, por meio de documento compartilhado.
- Abertura de postos extras de atendimento telefônico durante a manhã.
- Publicação de orientação no aplicativo explicando que o endereço não é atendido e que a retirada na loja é a alternativa.
- Resposta padrão no WhatsApp oficial com a opção de retirada e o telefone da unidade mais próxima.

## Ações preventivas com responsáveis e prazos

- Comunicação obrigatória de mudanças de cobertura à Coordenação do SAC com 48 horas de antecedência. Responsável: Gerência de Logística. Prazo: 15 dias corridos.
- Texto explicativo para o código ERR-7142 na tela de finalização, com a sugestão de retirada em loja. Responsável: Produto Digital. Prazo: 30 dias corridos.
- Painel de volume por código de erro, com alerta quando um mesmo código ultrapassar três vezes a média diária. Responsável: Coordenação de Dados. Prazo: 30 dias corridos.
- Revisão do roteiro do SAC para mensagens de erro de checkout, incluindo o passo a passo para o cliente. Responsável: Coordenação do SAC. Prazo: 20 dias corridos.

## Lições aprendidas

Uma mudança de regra de negócio que afeta o cliente precisa ser comunicada à equipe que atende o cliente antes de entrar em vigor. Sem essa conversa, o SAC se torna a primeira linha de defesa de uma decisão que não conhece.

A equipe também percebeu que a mensagem de erro deve explicar o que aconteceu e o que fazer. Um código sem texto de apoio gera ansiedade, repetição de tentativas e aumento de contatos.
