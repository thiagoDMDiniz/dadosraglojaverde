---
doc_id: "LV-INT-TI-0004"
titulo: "Gestão de incidentes de TI"
categoria: "ti"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Gestão de incidentes de TI

Código do documento: LV-INT-TI-0004. Classificação: USO INTERNO. Vigência: a partir de 01/01/2026.

## Objetivo

Este documento define como a área de tecnologia recebe, classifica, trata e encerra os incidentes que afetam os sistemas da Loja Verde. Um incidente é qualquer interrupção ou degradação não planejada de um serviço, como site fora do ar, falha no pagamento, erro na retirada de pedidos ou lentidão no aplicativo. O processo busca restabelecer o serviço com rapidez e registrar o que aconteceu para evitar a repetição.

## Abertura do incidente

Incidentes podem ser abertos pelo monitoramento automático, pelo atendimento, pelas lojas ou pelas equipes técnicas. A abertura deve conter a descrição do problema, o horário em que começou, o serviço afetado, o canal impactado (site, aplicativo, loja ou SAC) e, quando houver, o código de erro exibido e os pedidos envolvidos.

Quem abre o incidente não precisa diagnosticar a causa. A informação precisa é suficiente para que a equipe de plantão comece a investigação sem precisar voltar ao solicitante para perguntas básicas.

## Classificação de severidade

Os incidentes são classificados em níveis de severidade conforme o impacto. Severidade alta é aquela em que a venda ou o pagamento estão indisponíveis para a maior parte dos clientes, ou em que dados estão em risco. Severidade média afeta uma funcionalidade importante ou um grupo de clientes. Severidade baixa é um problema pontual, com alternativa de uso disponível.

A classificação é feita pelo plantonista e pode ser revisada pelo gerente de tecnologia à medida que o impacto se torna mais claro.

## Fluxo de tratamento

O plantonista confirma o incidente, comunica a severidade ao atendimento e às lojas e inicia o diagnóstico. Se a causa estiver em uma integração externa, como a operadora de pagamento ou a transportadora, o contato com o fornecedor é feito pelo responsável técnico do serviço.

Enquanto a correção não chega, a equipe pode aplicar medidas paliativas, como a desativação temporária de uma forma de pagamento ou a exibição de aviso no aplicativo. Essas medidas são registradas e revertidas assim que o serviço estiver normal.

Pedidos afetados são listados para que o atendimento possa acompanhar os clientes. Pedidos cancelados automaticamente, como os que recebem o código ERR-4217 por falta de confirmação do Pix, devem ser identificados separadamente quando o problema for de integração.

## Comunicação

O atendimento é o principal canal de comunicação com o cliente durante o incidente. Ele recebe, em cada atualização, o status do serviço, a previsão de normalização quando confirmada e as orientações de conduta. Enquanto a equipe técnica não confirmar um prazo, o atendimento não deve informá-lo ao cliente.

Mensagens públicas sobre incidentes relevantes são aprovadas pela gerência de tecnologia em conjunto com a comunicação corporativa.

## Encerramento e revisão

O incidente é encerrado quando o serviço volta ao funcionamento normal e os pedidos afetados estão resolvidos. Incidentes de severidade alta e média exigem relatório pós-incidente, com a linha do tempo, a causa raiz, o impacto estimado, as ações tomadas e as medidas preventivas propostas.

As revisões são discutidas em reuniões periódicas, em que se acompanha a recorrência de incidentes e a evolução das medidas preventivas.

## Responsabilidades

O plantonista de tecnologia conduz o diagnóstico e a comunicação técnica. O gerente de tecnologia define prioridades, aprova medidas de exceção e assina o relatório. O atendimento reporta padrões e comunica os clientes. As lojas registram o impacto local e informam o horário em que as operações foram afetadas.

## Erros comuns

- Abrir incidente sem horário nem serviço afetado, atrasando o diagnóstico.
- Informar prazo de normalização ao cliente antes de confirmação técnica.
- Encerrar o incidente sem verificar os pedidos afetados.
- Deixar de registrar medidas paliativas, impedindo a reversão posterior.
- Tratar incidentes recorrentes como casos isolados, sem relatório.
