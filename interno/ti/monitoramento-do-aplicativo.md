---
doc_id: "LV-INT-TI-0008"
titulo: "Monitoramento do aplicativo"
categoria: "ti"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Monitoramento do aplicativo

Código do documento: LV-INT-TI-0008. Classificação: USO INTERNO. Vigência: a partir de 01/01/2026.

## Objetivo

Este documento descreve como o aplicativo Loja Verde é monitorado em produção, quais indicadores são acompanhados, como os alertas são disparados e como a equipe responde a eles. O monitoramento busca identificar problemas antes que eles cheguem ao cliente e dar visibilidade ao impacto de cada falha sobre a jornada de compra.

O aplicativo compartilha o catálogo, os pedidos e a base de clientes com o site, de modo que parte dos indicadores se refere ao sistema como um todo e parte é específica da experiência mobile.

## Indicadores acompanhados

Os principais indicadores são a disponibilidade das telas de vitrine, de busca, de carrinho e de finalização, o tempo de resposta das consultas de produto e de pedido, a taxa de erros nas chamadas de pagamento e a taxa de falhas no envio de notificações. Também é observada a estabilidade das versões instaladas, com registro de travamentos por sistema operacional.

Os indicadores de negócio, como a conversão do carrinho e o volume de pedidos por canal, são acompanhados em painel conjunto com a área de produto, mas não disparam alertas técnicos por si sós.

## Alertas e limiares

Cada indicador possui limiares que disparam alertas para a equipe de plantão. Alertas críticos são enviados de forma imediata. Alertas de atenção são agrupados e revisados no turno. Os limiares são definidos pela área de tecnologia com base no histórico do aplicativo e revisados após cada mudança relevante.

Alertas que se repetem sem ação devem ser avaliados, pois podem indicar limiar mal calibrado. Ajustes desse tipo são registrados junto ao motivo.

## Resposta a alertas

Ao receber um alerta crítico, o plantonista verifica se o problema está restrito a uma versão do aplicativo, a um sistema operacional ou a um serviço de terceiros. Quando o problema é de integração de pagamento, a comunicação com o atendimento segue o processo de incidentes.

Se a falha afeta a finalização da compra, o plantonista avalia medidas paliativas, como a desativação temporária de uma forma de pagamento, e comunica o atendimento para que os clientes afetados sejam orientados.

## Monitoramento da experiência do cliente

Além dos indicadores técnicos, a equipe acompanha relatos de erro registrados pelo atendimento, com os códigos de erro mais recorrentes, como ERR-5308, quando o cartão é recusado pela operadora, e ERR-4217, quando o Pix não é confirmado em 30 minutos. Esses códigos ajudam a separar falhas da loja de recusas esperadas do sistema de pagamento.

Avaliações publicadas nas lojas de aplicativos são lidas pela área de produto, mas não substituem o monitoramento técnico.

## Privacidade no monitoramento

Os registros de monitoramento não devem conter dados pessoais além do mínimo necessário. Identificadores de cliente são substituídos por códigos internos, e o CPF nunca aparece nos painéis. Acessos aos registros completos são restritos e auditados.

## Responsabilidades

A equipe de tecnologia mantém os indicadores, calibra os alertas e atende as ocorrências críticas. A área de produto acompanha os indicadores de negócio e prioriza as melhorias. O atendimento reporta padrões de erro. A gerência de tecnologia revisa periodicamente o resumo de disponibilidade.

## Erros comuns

- Ignorar alertas repetidos por considerá-los rotineiros, sem avaliar a calibração.
- Registrar CPF em logs de depuração.
- Tratar a queda de conversão como falha técnica sem verificar o status dos serviços.
- Deixar de comunicar o atendimento durante uma falha de pagamento.
- Usar avaliação de loja de aplicativo como único indicador de qualidade.
