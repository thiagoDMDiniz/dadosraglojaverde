---
doc_id: "LV-INT-TI-0003"
titulo: "Backup e recuperação de desastres"
categoria: "ti"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Backup e recuperação de desastres

Código do documento: LV-INT-TI-0003. Classificação: USO INTERNO. Vigência: a partir de 01/01/2026.

## Objetivo

Este documento descreve, em nível geral, a estratégia de cópia de segurança e de recuperação dos sistemas da Loja Verde, incluindo o site, o aplicativo, o sistema de pedidos, o sistema de estoque e as bases de clientes. O objetivo é que a rede consiga restabelecer suas operações com perda de dados mínima e em tempo compatível com o impacto no atendimento e nas vendas.

Os parâmetros numéricos de cada serviço, como prazos de recuperação e intervalos de cópia, são definidos pela área de tecnologia em documentação restrita. Este texto trata da lógica do processo e das responsabilidades.

## Princípios da estratégia

A estratégia segue três princípios. O primeiro é a separação de responsabilidades: quem opera o sistema não é o único responsável por suas cópias de segurança. O segundo é a verificação: cópia que nunca foi testada não é considerada confiável. O terceiro é a segregação geográfica, de modo que um incidente em um local não destrua ao mesmo tempo os dados e as cópias.

As cópias de segurança são classificadas por criticidade. Bases de pedidos, de pagamentos e de clientes estão na categoria mais alta, seguidas pelo catálogo e pelo estoque, e por fim pelos registros de log e de atendimento.

## Tipos de cópia

A rede utiliza cópias completas, feitas periodicamente, e cópias incrementais, que guardam apenas as alterações desde a última cópia. A combinação permite restaurar um estado específico no tempo com menor volume de armazenamento. Toda cópia recebe identificação, data e status de verificação.

Dados de cartão de crédito não são armazenados nas bases de cópia da loja. Os dados de pagamento ficam com os processadores autorizados, e o que a loja guarda é o registro necessário ao pedido.

## Testes de restauração

Os testes de restauração são feitos em ambiente isolado, em ciclos regulares, com a documentação do resultado. Um teste bem-sucedido registra o tempo gasto, os dados verificados e as diferenças encontradas. Falhas geram ação corretiva e novo teste antes de a cópia voltar a ser considerada válida.

## Recuperação de desastres

Quando ocorre um incidente grave, como indisponibilidade prolongada de um serviço ou perda de dados, a equipe de tecnologia ativa o plano de recuperação. A primeira decisão é avaliar o impacto e definir a ordem de restauração, normalmente priorizando pagamentos, pedidos e retirada nas lojas.

Durante a recuperação, a comunicação com o atendimento é feita pelo canal de incidentes, com informações sobre o que está indisponível e o que foi restabelecido. O atendimento não deve prometer prazos aos clientes antes da confirmação da equipe técnica.

## Pós-incidente

Ao término da recuperação, a equipe elabora o relatório do incidente, com a causa, as ações tomadas, os dados afetados e as recomendações de melhoria. O relatório é revisado pela gerência de tecnologia e pode gerar mudanças no próprio plano de recuperação.

## Responsabilidades

A área de tecnologia executa as cópias, realiza os testes e conduz a recuperação. A gerência de tecnologia aprova o plano e as mudanças de criticidade. As áreas de negócio informam quais processos são essenciais. O atendimento e as lojas seguem as orientações de comunicação do incidente.

## Erros comuns

- Considerar a cópia confiável sem nunca ter feito teste de restauração.
- Guardar cópias no mesmo ambiente do sistema original.
- Restaurar uma base sem avaliar se o estado é o mais recente consistente.
- Prometer ao cliente um prazo de restabelecimento que a equipe técnica ainda não confirmou.
- Deixar de registrar o incidente em relatório, o que impede a melhoria do plano.
