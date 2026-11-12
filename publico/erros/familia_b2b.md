---
doc_id: "LV-PUB-COD-0016"
titulo: "Códigos de erro: Vendas para empresas"
categoria: "codigos_de_erro"
acesso: "publico"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
familia: "b2b"
---

# Códigos de erro: Vendas para empresas

Este catálogo reúne os códigos de erro que aparecem nas compras feitas por empresas, como faturamento, cadastro fiscal, limites e aprovações internas. Cada código tem quatro dígitos. Antes de consultar uma seção, confira o número exato na tela, porque códigos parecidos tratam de situações diferentes. Para compras empresariais, o atendimento pode ser acionado pelo 0800 700 0100 ou pelo e-mail atendimento@lojaverde.example.

## ERR-9700: CNPJ não habilitado para compras

O código ERR-9700 indica que o CNPJ informado ainda não foi habilitado para realizar compras com a Loja Verde. A habilitação é feita após a conferência dos dados cadastrais e da situação da empresa junto aos órgãos competentes. Enquanto ela não é concluída, o carrinho pode ser montado, mas o pedido não é finalizado.

**O que fazer:**

1. Confira se o CNPJ informado está completo e corresponde ao da empresa compradora.
2. Verifique no cadastro empresarial se o envio dos documentos foi concluído.
3. Aguarde a conclusão da análise de habilitação e tente novamente depois do retorno da loja.

Quando procurar o SAC: se a empresa estiver regular e o código continuar aparecendo após a análise.

## ERR-9707: limite de crédito empresarial excedido

O código ERR-9707 indica que o valor do pedido ultrapassa o limite de crédito liberado para a empresa. O limite considera o perfil da conta e os pedidos ainda não faturados. Compras a prazo só podem ser concluídas quando o total fica dentro desse limite.

**O que fazer:**

1. Consulte no painel empresarial o limite disponível e os pedidos em aberto.
2. Divida a compra em entregas menores, se a operação permitir.
3. Pague o pedido excedente à vista, por Pix ou boleto, ou solicite a revisão do limite ao atendimento empresarial.

## ERR-9728: faturamento em 30 dias não aprovado

O código ERR-9728 indica que a modalidade de faturamento com vencimento em 30 dias não foi aprovada para o pedido. A análise leva em conta o histórico de pagamentos, as faturas em aberto e os dados financeiros do cadastro. Uma recusa não impede a compra por outras formas de pagamento.

**O que fazer:**

1. Verifique se há faturas em atraso e regularize-as, se for o caso.
2. Atualize os dados financeiros e os documentos exigidos no cadastro.
3. Finalize o pedido à vista enquanto solicita uma nova análise do faturamento.

## ERR-9735: inscrição estadual divergente

O código ERR-9735 indica que a inscrição estadual informada não corresponde ao CNPJ ou à unidade da federação do pedido. Essa informação define a tributação da nota fiscal, por isso precisa estar exatamente de acordo com o registro da empresa. Sem a correspondência, o pedido não avança.

**O que fazer:**

1. Localize a inscrição estadual no comprovante emitido pelo órgão fazendário do estado da empresa.
2. Corrija o campo no cadastro fiscal, digitando somente os caracteres exigidos.
3. Confirme se o estado do endereço fiscal é o mesmo da inscrição e refaça o pedido.

## ERR-9740: nota fiscal com razão social divergente

O código ERR-9740 indica que a razão social usada no pedido é diferente do nome oficial vinculado ao CNPJ. A nota fiscal exige o nome exatamente igual ao do registro, com o tipo societário correto. Quando há divergência, a emissão fica suspensa até a correção.

**O que fazer:**

1. Consulte o comprovante atualizado do CNPJ e copie a razão social como consta nele.
2. Ajuste o cadastro da empresa, sem usar o nome fantasia.
3. Solicite novamente a emissão da nota pelo pedido correspondente.

## ERR-9747: pedido acima da quantidade máxima

O código ERR-9747 indica que a quantidade de um produto no pedido ultrapassa o máximo permitido para compras empresariais. O limite existe para manter o abastecimento equilibrado entre os clientes e evitar pedidos atípicos por engano. A regra se aplica ao item indicado na mensagem.

**O que fazer:**

1. Reduza a quantidade do item até o limite informado na tela.
2. Divida a compra em mais de um pedido, se a necessidade for maior.
3. Solicite a ampliação da quantidade ao atendimento empresarial, justificando a demanda.

## ERR-9758: contrato corporativo expirado

O código ERR-9758 indica que o contrato corporativo que sustentava as condições de compra da empresa já venceu. Enquanto o contrato não for renovado, os preços e as condições negociadas não podem ser aplicados ao pedido. A renovação segue o acordo feito com o gestor comercial.

**O que fazer:**

1. Verifique a data de validade do contrato no painel empresarial.
2. Entre em contato com o gestor comercial da conta para tratar da renovação.
3. Após a renovação, atualize a tela e refaça o pedido.

## ERR-9765: endereço de entrega comercial não cadastrado

O código ERR-9765 indica que o endereço escolhido para a entrega não está cadastrado como endereço comercial da empresa. Para pedidos empresariais, a entrega só é feita em locais previamente registrados, o que facilita a conferência de recebimento e a emissão da nota.

**O que fazer:**

1. Abra o cadastro da empresa e confira a lista de endereços de entrega.
2. Inclua o novo endereço comercial com CEP e complemento corretos.
3. Selecione o endereço recém-cadastrado e finalize o pedido.

## ERR-9772: aprovação do gestor pendente

O código ERR-9772 indica que o pedido aguarda a aprovação de um gestor interno da empresa antes de ser concluído. Esse controle é configurado pela própria empresa para acompanhar as compras de cada área. Enquanto a aprovação não acontece, o pedido fica em espera.

**O que fazer:**

1. Avise o gestor responsável pela aprovação do pedido.
2. Acompanhe o status em Meus Pedidos, onde aparece quem precisa aprovar.
3. Após a aprovação, confirme o pedido e verifique o pagamento.

## ERR-9776: tabela de preços corporativa indisponível

O código ERR-9776 indica que a tabela de preços especial da empresa não está disponível no momento da compra. Os preços corporativos são carregados a partir da tabela vinculada ao cadastro, e uma falha ou atualização em andamento impede essa leitura. Na maioria das vezes, a situação é temporária.

**O que fazer:**

1. Aguarde alguns minutos e atualize a tela do carrinho.
2. Confira se o cadastro da empresa está vinculado à tabela correta.
3. Se a indisponibilidade continuar, procure o atendimento empresarial antes de finalizar o pedido.
