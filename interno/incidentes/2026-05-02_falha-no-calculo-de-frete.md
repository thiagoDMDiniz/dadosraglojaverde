---
doc_id: "LV-INT-POS-0002"
titulo: "Post-mortem 2026-05-02: Falha no cálculo de frete"
categoria: "postmortem"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Post-mortem 2026-05-02: Falha no cálculo de frete

**USO INTERNO** · Data do incidente: 2026-05-02 (02/05/2026) · Severidade: alta · Responsável pelo documento: Coordenação de Precificação e Frete

## Resumo

No dia 02/05/2026, uma regra de frete grátis foi aplicada de forma indevida a pedidos com valor abaixo de R$ 199 destinados à região Sudeste. A política vigente concede frete grátis acima de R$ 199 para essa região, mas o cálculo passou a liberar o benefício a partir de R$ 149 para um conjunto de CEPs, por causa de uma configuração herdada de uma campanha antiga. O erro durou cerca de quatro horas e atingiu principalmente pedidos feitos pelo aplicativo no fim da tarde.

Ao todo, foram 1.146 pedidos com frete zerado indevidamente.

## Linha do tempo (horários)

- 13h15: a área de precificação publica uma alteração de faixas de frete para testar nova tabela de CEPs do interior de Minas.
- 14h40: a alteração é promovida para produção sem a etapa de validação com os valores de referência.
- 16h20: o painel financeiro mostra queda no valor médio de frete arrecadado no Sudeste, bem acima da variação habitual.
- 16h35: o plantão abre o incidente e identifica que a faixa de isenção está configurada com o valor de campanha antiga.
- 17h10: a faixa é corrigida para R$ 199 nas regiões indicadas e a validação de cálculo é repetida em amostra de 50 CEPs.
- 17h25: o incidente é encerrado e o cálculo volta a seguir a política vigente.

## Impacto

Dos 1.146 pedidos afetados, 611 eram de capitais do Sudeste e 535 de cidades do interior. A diferença de frete não cobrada totalizou aproximadamente R$ 18 mil, valor que foi registrado como custo operacional do trimestre.

O SAC recebeu 39 reclamações de clientes que tinham visto frete grátis em carrinhos com valor inferior a R$ 199 e depois foram informados de que a condição não se aplicava.

## Causa raiz

A tabela de faixas de frete continha uma regra de exceção criada para uma campanha de fevereiro, que não foi removida ao fim do período. A regra estava ligada a um conjunto de CEPs e tinha prioridade maior que a faixa padrão. Como o teste de 13h15 incluiu esses CEPs na mesma tabela, a exceção passou a valer para um conjunto mais amplo.

A etapa de validação prevista no processo exigia comparar o resultado com uma planilha de referência de 30 cenários, mas essa etapa foi pulada por causa de prazo, e o responsável pela publicação não tinha permissão para bloquear a promoção.

## Ações imediatas

- Correção da faixa de isenção para R$ 199 na região Sudeste e reversão da tabela de teste.
- Conferência de todos os pedidos aprovados entre 14h40 e 17h10, com registro do valor não cobrado.
- Comunicado ao financeiro para contabilizar a diferença como custo operacional.
- Revisão das regras de exceção ativas no sistema, com remoção de tudo que estivesse vencido.

## Ações preventivas com responsáveis e prazos

- Bloqueio de publicação de tabela de frete sem a conferência automática de 30 cenários de referência. Responsável: Coordenação de Precificação e Frete. Prazo: 30 dias corridos.
- Data de validade obrigatória para toda regra de exceção de frete, com aviso automático sete dias antes do vencimento. Responsável: Equipe de Sistemas Comerciais. Prazo: 45 dias corridos.
- Separação de permissões entre quem configura e quem publica tabelas de frete. Responsável: Diretoria de Tecnologia. Prazo: 60 dias corridos.
- Alerta no painel financeiro para variação de frete médio acima de 15% em uma hora. Responsável: Controladoria. Prazo: 30 dias corridos.

## Lições aprendidas

A campanha antiga deixou uma regra esquecida, e isso mostra que exceções temporárias precisam de prazo de vencimento. O custo da falha foi pequeno em comparação com o risco de um erro maior, e o time concluiu que a conferência por cenários não pode ser pulada, mesmo sob pressão de prazo.

A equipe também registrou que a comunicação com o cliente deve ser objetiva. Pedidos já confirmados foram honrados, e essa decisão reduziu o número de reclamações e preservou a relação com quem comprou de boa-fé.
