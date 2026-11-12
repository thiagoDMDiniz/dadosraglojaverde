---
doc_id: "LV-PUB-COD-0014"
titulo: "Códigos de erro: Nota fiscal e documentos fiscais"
categoria: "codigos_de_erro"
acesso: "publico"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
familia: "fiscal"
---

# Códigos de erro: Nota fiscal e documentos fiscais

Este catálogo reúne os códigos de erro relacionados a notas fiscais, segundas vias, XML, dados fiscais e comunicação com o serviço de emissão. Eles são importantes para clientes pessoa física e pessoa jurídica que precisam dos documentos para comprovação, contabilidade ou reembolso. Cada código tem quatro dígitos, e códigos parecidos podem ter causas diferentes. Confira o número exato antes de seguir uma orientação. O SAC atende pelo 0800 700 0100 e pelo e-mail atendimento@lojaverde.example.

## ERR-9126: nota fiscal não emitida

O código ERR-9126 indica que a nota fiscal do pedido ainda não foi gerada. A compra continua válida, e a emissão costuma ser concluída depois de algumas horas, quando o faturamento do pedido é finalizado.

**O que fazer:**

1. Consulte o status da nota em Meus Pedidos, algumas horas depois da compra.
2. Confira se o CPF ou o CNPJ informado está completo e correto.
3. Se a nota não aparecer após um dia útil, procure o SAC com o número do pedido.

## ERR-9138: CPF da nota inválido

O código ERR-9138 indica que o CPF informado para a nota fiscal não foi reconhecido como válido. A verificação confere a quantidade de dígitos e os dígitos verificadores, e um único número trocado já é suficiente para o erro.

**O que fazer:**

1. Confira o CPF no documento oficial e digite somente os números.
2. Atualize o campo no cadastro e solicite novamente a nota pelo pedido.
3. Procure o SAC se o CPF estiver correto e o erro persistir.

## ERR-9141: segunda via da nota indisponível

O código ERR-9141 indica que a segunda via da nota fiscal não pode ser gerada no momento. A indisponibilidade pode ser temporária, ou relacionada a uma restrição do pedido.

**O que fazer:**

1. Tente gerar a segunda via outra vez depois de alguns minutos.
2. Guarde o número do pedido e a data da compra, para facilitar o atendimento.
3. Se a segunda via continuar indisponível, procure o SAC para a emissão manual.

## ERR-9153: divergência de endereço fiscal

O código ERR-9153 indica que o endereço fiscal informado é diferente do endereço registrado para o CNPJ ou o CPF da compra. A nota precisa trazer dados idênticos aos cadastros oficiais, e a diferença costuma ser de abreviação, número ou complemento.

**O que fazer:**

1. Compare o endereço do cadastro com o documento oficial, campo por campo.
2. Corrija a rua, o número, o bairro, o CEP e o complemento divergentes.
3. Envie o comprovante ao SAC se a diferença não for de digitação.

## ERR-9157: CNPJ inválido

O código ERR-9157 indica que o CNPJ informado não passou na validação. Assim como no CPF, a checagem confere a quantidade de dígitos e os dígitos verificadores, e pontos ou traços em excesso podem gerar o erro.

**O que fazer:**

1. Copie o CNPJ do comprovante e digite somente os números.
2. Salve o cadastro e refaça a solicitação da nota.
3. Procure o SAC se o CNPJ estiver correto e a empresa estiver regular.

## ERR-9166: nota fiscal cancelada

O código ERR-9166 indica que a nota fiscal do pedido foi cancelada, em geral porque o pedido também foi cancelado ou ajustado. Um documento cancelado não tem validade fiscal e não pode ser usado para comprovação.

**O que fazer:**

1. Verifique em Meus Pedidos se o pedido foi cancelado ou alterado.
2. Se houve alteração, aguarde a emissão de uma nova nota para o pedido atualizado.
3. Procure o SAC para confirmar a situação do documento.

## ERR-9175: falha na comunicação com o serviço fiscal

O código ERR-9175 indica que houve uma falha temporária na comunicação entre a loja e o serviço de emissão fiscal. O documento não é perdido e, em geral, é gerado assim que a conexão se restabelece.

**O que fazer:**

1. Aguarde alguns minutos e consulte o pedido novamente.
2. Evite solicitar a emissão várias vezes seguidas, para não duplicar a tentativa.
3. Se a falha persistir por mais de um dia útil, procure o SAC.

## ERR-9178: nota de devolução pendente

O código ERR-9178 indica que existe uma nota de devolução ainda não concluída para o pedido. Enquanto ela não for finalizada, a nota original fica bloqueada para novas emissões ou alterações.

**O que fazer:**

1. Confira em Meus Pedidos se há uma devolução ou troca em andamento.
2. Aguarde a conclusão do processo de devolução, que é acompanhado pelo aplicativo.
3. Procure o SAC se a devolução já foi concluída e a mensagem continuar aparecendo.

## ERR-9197: data de emissão divergente

O código ERR-9197 indica que a data de emissão registrada na nota não coincide com a data do pedido ou do pagamento. A divergência pode ocorrer quando a nota é solicitada em um período de fechamento fiscal.

**O que fazer:**

1. Confira a data da compra e a data do pagamento em Meus Pedidos.
2. Solicite a emissão em outro momento, se o período estiver em fechamento.
3. Procure o SAC para revisar a data do documento, se necessário.

## ERR-9198: arquivo XML indisponível

O código ERR-9198 indica que o arquivo XML da nota fiscal não está acessível para download. O XML é a versão eletrônica do documento e, em geral, fica disponível pouco depois da emissão.

**O que fazer:**

1. Tente baixar o XML novamente depois de alguns minutos.
2. Verifique se o PDF da nota já está disponível, enquanto o XML não aparece.
3. Procure o SAC com o número do pedido se o arquivo não aparecer em um dia útil.
