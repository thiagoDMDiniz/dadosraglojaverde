---
doc_id: "LV-INT-TI-0007"
titulo: "Integração com transportadoras"
categoria: "ti"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Integração com transportadoras

Código do documento: LV-INT-TI-0007. Classificação: USO INTERNO. Vigência: a partir de 01/01/2026.

## Objetivo

Este documento descreve como os sistemas da Loja Verde se integram às transportadoras parceiras para calcular frete, reservar entregas, gerar etiquetas, acompanhar o rastreamento e tratar exceções de entrega. A integração é o que permite ao cliente acompanhar o pedido desde a saída do centro de distribuição até a chegada ao endereço.

As regras comerciais, como frete grátis acima de R$ 199 na região Sudeste e acima de R$ 299 nas demais regiões, são definidas pela área de produto e apenas aplicadas pelo sistema. A integração técnica não altera essas regras.

## Visão geral da integração

A cada pedido confirmado, o sistema de pedidos consulta a transportadora para verificar se o endereço é atendido e qual o prazo estimado. Com a resposta, o frete é calculado e apresentado ao cliente no carrinho. Quando o pedido é liberado para envio, a integração gera a etiqueta de postagem e a registra no sistema.

As informações de rastreamento retornam por evento. A cada mudança de status relevante, como a saída do centro de distribuição ou a entrega, o cliente recebe a notificação por e-mail e SMS.

## Cálculo de prazo e cobertura

O prazo de entrega padrão é contado em dias úteis a partir da confirmação do pagamento, de acordo com a região e com o tipo de cidade, capital ou interior. A tabela de prazos é mantida pela área de logística e atualizada na integração quando há mudança de contrato.

Endereços não atendidos pela transportadora geram o código ERR-7142. Nesse caso, o sistema não permite finalizar a entrega domiciliar e oferece a retirada na loja como alternativa.

## Entregas com atraso

Quando uma entrega passa do prazo, o sistema verifica se o atraso ultrapassou cinco dias úteis. Nessa situação, o cupom ATRASO25, de R$ 25, é gerado automaticamente. A geração é feita pela regra de negócio, e a integração apenas informa a data de atraso.

Atrasos que não se enquadram na regra são acompanhados pelo atendimento, que pode consultar a transportadora pelo número de rastreamento.

## Exceções e devoluções

Quando a transportadora registra uma ocorrência de endereço incorreto, recusa ou avaria, o evento chega ao sistema e fica disponível para o atendimento. O cliente é informado do que aconteceu e das providências. Devoluções ao centro de distribuição seguem o fluxo de troca e reembolso das políticas da loja.

Falhas temporárias de comunicação com a transportadora geram alertas técnicos, e o pedido permanece com o último status conhecido até a sincronização.

## Segurança das credenciais

As credenciais de acesso às transportadoras são armazenadas em cofre próprio e não são compartilhadas com equipes de atendimento ou de loja. Solicitações de acesso devem ser feitas pela área de tecnologia, com justificativa e aprovação do gerente.

## Responsabilidades

A área de tecnologia mantém a integração, monitora as falhas e aplica as atualizações contratuais. A logística define os prazos e os parceiros, e acompanha o desempenho das transportadoras. O atendimento orienta o cliente com base no rastreamento e registra ocorrências. As lojas que servem de retirada recebem os pedidos alternativos.

## Erros comuns

- Informar prazo de entrega sem consultar a região e o tipo de cidade.
- Tentar contornar ERR-7142 cadastrando endereço vizinho que não corresponde ao destino.
- Compartilhar credenciais da integração em canais de atendimento.
- Tratar a notificação de rastreamento como confirmação de entrega, quando é apenas um evento de status.
- Esquecer de registrar a ocorrência de endereço incorreto para acompanhamento.
