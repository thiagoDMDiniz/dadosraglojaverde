---
doc_id: "LV-INT-POS-0003"
titulo: "Post-mortem 2025-11-28: Queda do aplicativo na Black Friday de 2025"
categoria: "postmortem"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Post-mortem 2025-11-28: Queda do aplicativo na Black Friday de 2025

USO INTERNO. Documento restrito à diretoria, à gerência de tecnologia e às equipes de atendimento e operações.

## Resumo

Na tarde de 28/11/2025, o aplicativo Loja Verde ficou indisponível por 47 minutos durante o pico de acessos da Black Friday. Durante esse intervalo, clientes não conseguiam entrar na conta, consultar pedidos, aplicar cupons nem finalizar compras pelo celular. O site continuou funcionando, mas com tempo de resposta elevado nas páginas de carrinho. A indisponibilidade foi resolvida com a reversão de uma alteração de configuração feita pouco antes do pico.

## Linha do tempo (horários)

- 14h02: a equipe de plataforma aplica uma alteração de configuração no balanceador de carga que deveria ajustar o limite de conexões simultâneas.
- 14h09: o volume de acessos ao aplicativo sobe acima do habitual, com erros de autenticação em série.
- 14h14: o painel de monitoramento registra a primeira onda de respostas com erro 503 nas chamadas de login.
- 14h18: o atendimento do SAC recebe as primeiras reclamações de clientes sem acesso ao aplicativo.
- 14h23: o coordenador de infraestrutura confirma a indisponibilidade e aciona a equipe de plantão.
- 14h31: a alteração de configuração é identificada como provável causa, a partir da comparação com o último estado estável.
- 14h41: a configuração anterior é restaurada e os novos acessos voltam a ser autenticados.
- 14h49: o aplicativo volta a responder de forma normal em todas as regiões, após a limpeza do cache de sessões.

## Impacto

A indisponibilidade durou 47 minutos. Estimou-se que parte dos pedidos iniciados pelo aplicativo naquele intervalo não foi concluída e precisou ser refeita pelos clientes. O site não foi derrubado, mas registrou lentidão no carrinho. O SAC recebeu um volume de chamadas acima do previsto para o período, e o WhatsApp oficial recebeu mensagens de clientes pedindo orientação sobre cobrança duplicada. Não houve vazamento de dados, e nenhuma cobrança indevida foi confirmada pelo setor financeiro.

## Causa raiz

A alteração de configuração foi testada apenas em ambiente de homologação com carga reduzida. Em produção, o novo limite de conexões simultâneas reduziu a capacidade efetiva do serviço de autenticação, que não estava dimensionado para o volume da Black Friday. A checklist de mudança não exigia simulação de carga para alterações feitas em janela de pico, e a revisão de pares foi concluída sem o número de aprovações previsto no processo.

## Ações imediatas

- Reversão imediata da configuração para o estado estável anterior.
- Limpeza do cache de sessões para restabelecer o login de clientes afetados.
- Comunicado aos clientes pelo aplicativo e pelo WhatsApp oficial, com orientação para conferir pedidos.
- Reforço temporário da equipe do SAC durante o restante da campanha.

## Ações preventivas com responsáveis e prazos

- Proibir alterações de configuração em produção durante a janela de pico, sob responsabilidade da gerência de tecnologia, com prazo para a próxima campanha sazonal.
- Incluir simulação de carga obrigatória para mudanças de infraestrutura, sob responsabilidade do coordenador de infraestrutura, até o fim do trimestre seguinte.
- Revisar o processo de aprovação de mudanças e exigir o número mínimo de aprovações, sob responsabilidade do gerente de qualidade de software, antes da próxima alteração planejada.
- Criar alerta automático para aumento de erros 503 no login, sob responsabilidade da equipe de plataforma, com teste em homologação antes da campanha.

## Lições aprendidas

O incidente mostrou que a homologação precisa refletir o pico real de acessos quando a mudança afeta o caminho de autenticação. Também ficou claro que o SAC deve ter um roteiro pronto para indisponibilidades, para responder com as mesmas informações em todos os canais. A decisão de reverter rapidamente, em vez de tentar corrigir em produção, reduziu o tempo de impacto e deve virar prática registrada. Por fim, a comunicação com clientes precisa sair mais cedo, porque boa parte das dúvidas chegou antes de qualquer aviso oficial.
