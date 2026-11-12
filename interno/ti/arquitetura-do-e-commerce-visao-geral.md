---
doc_id: "LV-INT-TI-0001"
titulo: "Arquitetura do e-commerce (visão geral)"
categoria: "ti"
acesso: "interno"
unidade: "rede"
status: "vigente"
versao: "1.0"
vigencia_inicio: "2026-01-01"
atualizado_em: "2026-10-30"
---

# Arquitetura do e-commerce (visão geral)

Código do documento: LV-INT-TI-0001. Classificação: USO INTERNO. Vigência: a partir de 01/01/2026.

## Finalidade deste documento

Este documento apresenta, em linhas gerais, como o e-commerce da Loja Verde está organizado: os principais componentes, a forma como conversam entre si e os cuidados de operação que equipes de atendimento e de produto precisam conhecer. Não é um manual de implantação. Detalhes de configuração, de acesso e de infraestrutura são mantidos pela área de tecnologia em documentação restrita.

O canal digital atende o site www.lojaverde.example e o aplicativo Loja Verde, que compartilham o catálogo, os pedidos e a base de clientes.

## Componentes principais

A vitrine é a camada que o cliente vê: páginas de produto, busca, carrinho e finalização da compra, tanto no site quanto no aplicativo. Ela consome o catálogo, que concentra os produtos, preços, estoque e informações de garantia por categoria, com os departamentos Eletrônicos, Eletrodomésticos, Casa e Móveis, Moda e Calçados, Esporte e Lazer, Brinquedos, Livros e Papelaria e Jardim e Sustentabilidade.

O módulo de pedidos registra cada compra, o status de pagamento e a logística. O módulo de pagamentos integra as formas aceitas: Pix, boleto, cartão de crédito e, nas lojas físicas, débito, vale-compras e cartão-presente. O módulo de cupons valida os códigos vigentes e aplica as regras de cada campanha.

O Clube Verde, programa de pontos e de níveis, consulta o histórico de compras para calcular pontos, saldo e benefícios. A integração com transportadoras calcula frete e prazos por região e envia o rastreamento ao cliente.

## Fluxo de uma compra

O cliente monta o carrinho, aplica cupom quando for o caso e escolhe a forma de entrega. Na finalização, o pedido é criado e o pagamento é iniciado. No caso do Pix, o sistema aguarda a confirmação, e a ausência de confirmação em 30 minutos gera o código ERR-4217, com cancelamento automático do pedido e nenhuma cobrança.

Após a confirmação, o pedido entra na fila de separação, seguindo para o centro de distribuição ou para a unidade escolhida para retirada. O rastreamento é disparado quando o pedido sai do centro de distribuição.

## Ambientes e publicação

O e-commerce mantém ambientes separados de desenvolvimento, homologação e produção. Alterações passam por revisão e por testes antes de chegar à produção, e as mudanças de maior impacto são feitas em janelas acordadas com o atendimento. Nenhuma alteração deve ser publicada diretamente em produção sem registro.

## Integração e dados

As integrações usam interfaces padronizadas e registros de log para rastreabilidade. Dados pessoais de clientes são acessados somente por perfis autorizados, e as telas de atendimento exibem CPF mascarado no formato ***.***.***-**. O tratamento de dados segue a política de privacidade, com prazo de guarda de dados de compra de 5 anos.

## Responsabilidades

A área de tecnologia mantém a arquitetura, define padrões e responde pela segurança da plataforma. A área de produto define o catálogo e as regras de campanha. O atendimento consome as informações do sistema e reporta falhas com os códigos de erro. Equipes de loja usam o sistema de retirada e a integração com o balcão.

## Cuidados operacionais

Equipes de atendimento não devem solicitar acessos administrativos nem compartilhar credenciais de qualquer natureza. Problemas técnicos devem ser abertos como incidente, com a descrição do que aconteceu, o horário, o código de erro e o pedido afetado, quando houver.

## Erros comuns

- Tratar um código de erro como problema isolado, sem consultar o histórico de ocorrências.
- Alterar o catálogo diretamente em produção sem passar pelo fluxo de revisão.
- Compartilhar prints de telas com dados de clientes sem mascaramento.
- Confundir a vitrine do site com a do aplicativo ao reportar um problema, sem indicar o canal afetado.
