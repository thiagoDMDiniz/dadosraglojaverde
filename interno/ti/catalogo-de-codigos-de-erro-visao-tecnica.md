---
doc_id: "LV-INT-TI-0006"
titulo: "Catálogo de códigos de erro (visão técnica)"
categoria: "ti"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Catálogo de códigos de erro (visão técnica)

Código do documento: LV-INT-TI-0006. Classificação: USO INTERNO. Vigência: a partir de 01/01/2026.

## Finalidade

Este catálogo reúne os códigos de erro emitidos pelos sistemas da Loja Verde durante o atendimento e o processamento de pedidos. Os códigos seguem o formato ERR-NNNN, com quatro dígitos. A finalidade é padronizar a leitura dos erros entre as equipes de atendimento, de tecnologia e de loja, para que um mesmo código signifique a mesma coisa em qualquer canal.

O catálogo descreve o significado de cada código e a ação esperada. Não inclui detalhes internos de implementação, nem credenciais, nem endereços de serviços.

## Os três códigos mais frequentes

Três códigos concentram a maior parte das ocorrências registradas no atendimento: ERR-4217, ERR-5308 e ERR-7142. Equipes que atendem clientes devem conhecê-los de memória.

## ERR-4217

O código ERR-4217 indica que o pagamento por Pix não foi confirmado em 30 minutos. Nesse caso, o pedido é cancelado automaticamente e nenhum valor é cobrado. Do ponto de vista técnico, a ocorrência significa que a notificação de confirmação do banco não chegou ao sistema dentro da janela configurada. O atendimento deve verificar se o cliente efetivamente não pagou antes de orientar uma nova compra, pois um pagamento tardio costuma ser estornado pelo próprio banco.

## ERR-5308

O código ERR-5308 indica que o cartão foi recusado pela operadora. O cliente deve tentar outro cartão ou contatar o banco emissor. A recusa é uma resposta da operadora, e o sistema da loja apenas a reproduz. Por isso, não cabe ao atendimento tentar contornar a recusa com novas tentativas repetidas, o que pode gerar bloqueios adicionais.

## ERR-7142

O código ERR-7142 indica que o endereço informado não é atendido pela transportadora. A alternativa é a retirada na loja. Quando o erro ocorre, o sistema não deve permitir a finalização com entrega domiciliar naquele endereço, e o atendimento pode oferecer a retirada em uma das unidades.

## Outros códigos

Além dos três códigos principais, o sistema gera erros de validação de cupom, de indisponibilidade temporária de integração com transportadoras e de falha de sincronização de estoque. Esses casos devem ser registrados com o código, o horário e o pedido afetado, e encaminhados à área de tecnologia quando não houver solução no atendimento.

## Como registrar uma ocorrência

Toda ocorrência técnica registrada pelo atendimento deve informar o código, o canal (site, aplicativo, loja ou SAC), o horário aproximado, o número do pedido quando houver e o passo que estava sendo executado. O CPF de clientes nunca deve aparecer no registro sem mascaramento no formato ***.***.***-**.

## Responsabilidades

A área de tecnologia mantém o catálogo, atualiza as descrições quando o comportamento do sistema muda e acompanha a frequência de cada código. O atendimento aplica a orientação indicada e reporta padrões. A área de produto é consultada quando um código sugere problema em regra de negócio, como cupons.

## Erros comuns

- Orientar o cliente a refazer um pagamento Pix sem verificar se o pedido já foi cancelado.
- Repetir sucessivas tentativas de cartão recusado, o que pode acionar bloqueios.
- Confundir ERR-7142 com falha de cadastro do cliente, quando o problema é a cobertura da transportadora.
- Registrar o código sem o horário, o que impede a correlação com os logs.
- Tratar um código não listado como irrelevante, sem reportar à tecnologia.
