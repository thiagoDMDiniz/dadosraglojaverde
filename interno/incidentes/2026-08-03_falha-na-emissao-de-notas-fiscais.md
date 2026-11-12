---
doc_id: "LV-INT-POS-0007"
titulo: "Post-mortem 2026-08-03: Falha na emissão de notas fiscais"
categoria: "postmortem"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Post-mortem 2026-08-03: Falha na emissão de notas fiscais

**USO INTERNO** · Data do incidente: 2026-08-03 (03/08/2026) · Severidade: alta · Responsável pelo documento: Coordenação Fiscal

## Resumo

No dia 03/08/2026, o serviço de emissão de notas fiscais eletrônicas ficou indisponível por cerca de três horas. Durante esse período, os pedidos aprovados no site, no aplicativo e nos caixas das unidades não geraram documento fiscal no momento da venda. A emissão foi retomada em lote, e todas as notas foram transmitidas dentro do mesmo dia, sem prejuízo para o cliente, mas com retrabalho significativo para a equipe fiscal.

A indisponibilidade foi causada por um certificado digital expirado no módulo de comunicação com a secretaria estadual, que passou a recusar as transmissões sem gerar um alerta claro no painel interno.

## Linha do tempo (horários)

- 09h10: o primeiro caixa da unidade Savassi informa que a nota não foi emitida e que o cupom fiscal ficou pendente.
- 09h25: o monitor de transmissão mostra zero envios bem-sucedidos desde as 09h00.
- 09h40: a Coordenação Fiscal abre o incidente e aciona a equipe de sistemas responsável pela integração.
- 10h15: a equipe identifica a recusa de autenticação e confirma que o certificado do módulo expirou na véspera.
- 11h30: o certificado renovado é instalado e os testes de comunicação passam a ser aprovados.
- 12h10: a fila de notas pendentes começa a ser transmitida em lotes de 200 documentos.
- 13h00: a fila é zerada e o incidente é encerrado após conferência por amostragem.

## Impacto

Foram represadas 1.374 notas fiscais durante a indisponibilidade, sendo 812 de vendas online, 421 de vendas em lojas físicas e 141 de trocas e devoluções. Todas foram emitidas dentro do mesmo dia. Nenhum cliente teve a compra cancelada, mas 36 vendas em loja precisaram de comprovante provisório, emitido manualmente pelo gerente da unidade com o número do pedido.

A equipe fiscal precisou reconferir 96 notas emitidas em lote, para confirmar que a data de emissão e o valor do imposto estavam corretos. O SAC recebeu 23 contatos de clientes que pediram a nota para fins de reembolso de empresa, todos atendidos no mesmo dia.

## Causa raiz

O certificado digital usado na autenticação com o sistema da secretaria tinha validade de um ano, e o processo de renovação dependia de um lembrete manual que foi perdido após a troca de responsável pela área. Como o módulo não tinha alerta de vencimento integrado ao painel, a expiração passou despercebida até a primeira recusa.

O monitor de transmissão media o volume de notas, mas não o número de respostas positivas, por isso o zero só apareceu no painel depois de algum tempo.

## Ações imediatas

- Renovação e instalação do certificado digital, com testes de transmissão em ambiente de homologação e em produção.
- Retransmissão em lotes de 200 notas, com conferência de números e valores.
- Emissão de comprovantes provisórios nas unidades, com registro no sistema de pedidos.
- Comunicado interno à rede sobre o procedimento de contingência para caixa.

## Ações preventivas com responsáveis e prazos

- Alerta de vencimento de certificado com 60, 30 e 7 dias de antecedência, enviado a dois responsáveis. Responsável: Coordenação Fiscal. Prazo: 15 dias corridos.
- Indicador de transmissões bem-sucedidas por hora no painel, com alarme quando ficar zerado por 15 minutos. Responsável: Equipe de Sistemas Fiscais. Prazo: 30 dias corridos.
- Registro formal de responsáveis por cada credencial técnica, com revisão trimestral. Responsável: Diretoria Administrativa. Prazo: 60 dias corridos.
- Teste de contingência para caixa com emissão offline e posterior transmissão, executado a cada trimestre. Responsável: Supervisão de Unidades. Prazo: 90 dias corridos.

## Lições aprendidas

Uma credencial técnica esquecida pode parar a operação inteira, porque o problema não aparece no sistema de vendas e sim na etapa fiscal. O incidente mostrou que a responsabilidade por cada certificado precisa ser registrada em nome de um cargo, e não de uma pessoa que pode mudar de função.

Também se confirmou que a contingência do caixa funcionou, e que o comprovante provisório evitou filas maiores nas unidades. O procedimento deve ser treinado com mais frequência.
