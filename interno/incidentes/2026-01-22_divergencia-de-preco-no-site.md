---
doc_id: "LV-INT-POS-0011"
titulo: "Post-mortem 2026-01-22: Divergência de preço no site"
categoria: "postmortem"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Post-mortem 2026-01-22: Divergência de preço no site

USO INTERNO. Documento restrito à gerência comercial, ao comitê de preços e à equipe de e-commerce.

## Resumo

Em 22/01/2026, preços de uma linha de eletrônicos foram exibidos de forma incorreta no site e no aplicativo durante cerca de três horas. Alguns itens apareceram com valor inferior ao praticado na tabela vigente, e outros com valor superior. O problema afetou apenas a linha de televisores e de áudio portátil e foi corrigido manualmente após a identificação da causa. Pedidos efetivados nesse período foram revisados caso a caso pela área comercial.

## Linha do tempo (horários)

- 08h40: a atualização semanal da tabela de preços é publicada no sistema de catálogo.
- 09h15: uma analista de e-commerce percebe diferença entre a tabela enviada pelo comitê e os valores exibidos em três produtos.
- 09h32: a equipe de catálogo confirma que a importação aplicou a coluna de preços da semana anterior para um grupo de itens.
- 09h50: a exibição dos itens afetados é suspensa temporariamente, e a gerência comercial é informada.
- 10h20: a tabela correta é reimportada e conferida por amostragem em quarenta produtos.
- 11h45: a exibição normal é restabelecida e uma nota interna registra o período afetado.

## Impacto

Durante o intervalo, foram realizados pedidos com preço divergente dos itens da linha afetada. A área comercial decidiu honrar os pedidos com valor menor que o praticado, desde que o cliente tivesse finalizado a compra antes da correção. Nos casos com valor superior ao da tabela, o cliente foi contatado e pôde escolher manter o pedido pelo preço da tabela vigente ou cancelá-lo sem custo. Não houve reclamação formal registrada na ouvidoria, mas o SAC recebeu dúvidas sobre preços que mudavam entre a página de listagem e a página do produto.

## Causa raiz

O arquivo de importação continha duas colunas de preço com cabeçalhos semelhantes, e o processo de carga leu a coluna incorreta para os itens cadastrados com código de fornecedor alternativo. A validação automática comparava apenas a quantidade de linhas importadas e não o valor de cada produto. Além disso, a conferência manual prevista no procedimento não foi executada porque a equipe estava sobrecarregada com a campanha de janeiro.

## Ações imediatas

- Suspensão da exibição dos itens afetados até a reimportação.
- Reimportação da tabela correta e conferência por amostragem.
- Levantamento dos pedidos efetivados no período, com revisão caso a caso.
- Comunicado interno à equipe de atendimento para padronizar as respostas.

## Ações preventivas com responsáveis e prazos

- Incluir no processo de carga uma comparação automática entre o preço importado e o preço da tabela aprovada pelo comitê, sob responsabilidade da coordenação de e-commerce, antes da próxima atualização semanal.
- Padronizar o layout do arquivo de importação, eliminando cabeçalhos ambíguos, sob responsabilidade da equipe de catálogo, com prazo de um ciclo de atualização.
- Tornar obrigatória a conferência manual de amostra de produtos de linhas com alto giro, sob responsabilidade do gerente comercial de eletrônicos.
- Criar relatório diário de divergências entre preço de tabela e preço exibido, sob responsabilidade da área de dados.

## Lições aprendidas

Validar apenas a contagem de linhas não basta para uma carga de preços. A comparação deve ser feita por valor, com a tabela aprovada como referência. O episódio também mostrou que a conferência manual, quando depende de disponibilidade da equipe, tende a ser pulada em semanas de campanha. Por isso, a checagem automática precisa cobrir o caso comum, e a conferência humana deve ficar restrita a amostras definidas antecipadamente. Por fim, a decisão de honrar pedidos com preço menor foi comunicada tarde, e o comitê de preços deve definir antecipadamente o critério para incidentes desse tipo.
