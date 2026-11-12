---
doc_id: "LV-INT-POS-0009"
titulo: "Post-mortem 2026-09-12: Uso fraudulento de cupom"
categoria: "postmortem"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Post-mortem 2026-09-12: Uso fraudulento de cupom

**USO INTERNO** · Data do incidente: 2026-09-12 (12/09/2026) · Severidade: média · Responsável pelo documento: Coordenação de Promoções e Prevenção a Fraudes

## Resumo

Em 12/09/2026, o time de prevenção a fraudes identificou tentativas de uso de um código promocional que não existia na base de cupons da Loja Verde. O código circulava em publicações de redes sociais, apresentado como uma oferta de desconto para compras no site e no aplicativo. Foram registradas 214 tentativas de aplicação no período da manhã, a maioria vinda de contas criadas poucas horas antes da tentativa.

Nenhum desconto foi concedido, porque o sistema recusou o código por não constar na lista de cupons válidos. O incidente foi tratado como tentativa de fraude e teve como efeito principal um aumento de chamados de clientes que viram a divulgação e não entenderam por que o código não funcionava.

## Linha do tempo (horários)

- 08h15: o monitor de tentativas de cupom mostra aumento de 40 vezes no volume de recusas para um mesmo texto de código.
- 08h30: a equipe de prevenção identifica publicações em redes sociais citando o código e associando-o à Loja Verde, sem qualquer vínculo oficial.
- 08h50: o incidente é aberto e o bloqueio de novas criações de conta com o mesmo padrão de e-mail é ativado.
- 09h20: a Coordenação de Promoções confirma que o código não pertence a nenhuma campanha, nem passada nem futura.
- 10h10: o time de comunicação publica orientação no site e nas redes oficiais, esclarecendo que somente cupons divulgados pela própria Loja Verde são válidos.
- 11h40: as contas suspeitas são sinalizadas e o volume de tentativas volta ao patamar normal.
- 14h00: o incidente é encerrado após revisão de 48 horas de registros.

## Impacto

Não houve desconto concedido nem prejuízo financeiro. Foram bloqueadas 87 contas criadas para testar o código, e 19 delas já haviam feito pedidos sem finalização de pagamento. Os pedidos incompletos foram cancelados automaticamente pelo sistema.

O SAC recebeu 61 contatos de clientes, a maioria perguntando se o código era válido. A orientação padrão foi repetida em todos os casos, e nenhum cliente foi acusado de má-fé.

## Causa raiz

Não havia nenhuma exigência de validação antes da divulgação de códigos nas redes sociais, e o sistema não cruzava tentativas de cupom com a origem da conta.

Além disso, a criação de contas em massa não tinha limite de frequência por endereço de e-mail, o que permitiu a repetição das tentativas em pouco tempo.

## Ações imediatas

- Bloqueio das 87 contas suspeitas e cancelamento dos pedidos incompletos associados.
- Inclusão do texto do código na lista de termos monitorados pelo sistema de prevenção.
- Publicação de orientação oficial no site, no aplicativo e nas redes sociais da Loja Verde.
- Orientação ao SAC sobre o roteiro de atendimento para dúvidas sobre cupons não reconhecidos.

## Ações preventivas com responsáveis e prazos

- Limite de criação de contas por endereço de e-mail e por dispositivo em 24 horas. Responsável: Equipe de Segurança da Informação. Prazo: 30 dias corridos.
- Monitoramento contínuo de menções a cupons em redes sociais, com alerta à equipe de promoções. Responsável: Coordenação de Promoções. Prazo: 45 dias corridos.
- Lista pública de cupons vigentes na página de ajuda, atualizada a cada nova campanha. Responsável: Equipe de Conteúdo Digital. Prazo: 30 dias corridos.
- Campanha de conscientização sobre golpes de cupom, com o canal oficial de WhatsApp e o SAC como referências. Responsável: Comunicação Institucional. Prazo: 60 dias corridos.

## Lições aprendidas

O caso mostrou que um cupom falso não causa dano se o sistema tiver validação consistente, mas causa dano reputacional quando o cliente não sabe a quem perguntar. A resposta mais eficaz foi a orientação simples e repetida, sem tom de acusação.

A equipe também registrou que a Loja Verde nunca pede senha, token ou código de segurança por telefone, e-mail ou mensagem. Esse aviso deve constar em qualquer comunicação sobre fraudes, para que o cliente reconheça outros golpes que possam surgir a partir deste.
