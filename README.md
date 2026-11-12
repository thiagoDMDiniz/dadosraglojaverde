# Base documental sintética da Loja Verde (para o Trabalho de RAG)

Massa documental **100% fictícia** (empresa, pessoas, endereços, telefones, preços e códigos são inventados) com **1.001 documentos** (830 `.md` e 171 `.txt`, cerca de 3,2 MB e 485 mil palavras), feita para alimentar os três notebooks do Trabalho Prático de RAG (TEC II). Os textos foram redigidos por agentes Haiku a partir de um cânone único de fatos (`_meta/CANON.md`), para que os mais de mil documentos não se contradigam.

## Como baixar

Os notebooks do trabalho baixam a base sozinhos. Para baixar em outro ambiente (Colab, Jupyter ou script):

```python
import io, zipfile, urllib.request
url = "https://github.com/thiagoDMDiniz/dadosraglojaverde/archive/main.zip"
zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(url).read())).extractall(".")
# a base fica na pasta ./dadosraglojaverde-main
```

Ou, com git: `git clone https://github.com/thiagoDMDiniz/dadosraglojaverde`.

## Estrutura

| Pasta | O que tem | Docs |
|---|---|---|
| `publico/` | Conteúdo que o assistente pode mostrar a **clientes** (`acesso: publico`) | 708 |
| `interno/` | Conteúdo **confidencial** (`acesso: interno`): manual dos gerentes, POPs, RH, financeiro, TI, atas, post-mortems, transcrições de atendimento | 285 |
| `_seguranca_teste/` | 8 documentos **adversariais** (injeção de prompt, desinformação, PII fictícia, golpe) para a T3.6. **Não indexe junto com o resto, a não ser no experimento de segurança.** | 8 |
| `_avaliacao/` | `perguntas_teste.jsonl`: 201 perguntas com gabarito | 1 |
| `_meta/` | Cânone, especificações, manifesto, scripts que geraram tudo | n/a |

### Conteúdo de `publico/` e `interno/`

| Subpasta | Conteúdo | Docs |
|---|---|---|
| `publico/politicas/` | **Núcleo**: `politica_trocas.md`, `politica_frete.md`, `garantia.md`, `pagamentos_e_erros.md`, `clube_verde.md` (mesmos arquivos e títulos de seção da base original dos notebooks, com valores fixos) | 5 |
| `publico/politicas/ext/` | Políticas detalhadas (trocas por categoria, frete por região, garantia, pagamentos, Clube Verde) | 46 |
| `publico/produtos/` | Fichas de produto, com SKU único (`LV-ELE-1028`) e preço | 190 |
| `publico/erros/` | Códigos `ERR-NNNN`: 16 catálogos por família (10 códigos cada) + 70 artigos de ajuda | 86 |
| `publico/faq/` | Perguntas frequentes (`## pergunta` + resposta) | 50 |
| `publico/unidades/` | 10 unidades × 6 documentos (horários, endereço, serviços, departamentos...) | 60 |
| `publico/avaliacoes/` | Avaliações de clientes de produtos, lojas e serviços | 90 |
| `publico/blog/`, `app_e_site/`, `sustentabilidade/`, `privacidade/`, `glossario/` | Guias e conteúdo institucional | 123 |
| `publico/campanhas/` | 20 campanhas (`.md`) + 20 regulamentos (`.txt`) | 40 |
| `publico/historico/` | Versões **revogadas** das políticas (valores antigos) + comunicados de mudança: teste de versionamento | 18 |
| `interno/politicas/` | `manual_interno_gerentes.md` (desconto de gerente, tolerância de troca, margem mínima) | 1 |
| `interno/procedimentos/`, `rh/`, `financeiro/`, `ti/`, `incidentes/`, `atas/`, `unidades/`, `historico/` | Documentos internos | 174 |
| `interno/atendimento/transcricoes/` | 110 transcrições de atendimento `.txt` (com perguntas elípticas do tipo "e para o interior?") | 110 |

## Metadados

- **`.md`**: front matter YAML com `doc_id`, `titulo`, `categoria`, `acesso`, `unidade`, `status` (`vigente`, `revogado` ou `nao_confiavel`), `versao`, `vigencia_inicio`, `atualizado_em` e campos extras (`sku`, `codigo`...). A divisão `texto.split("\n## ")[1:]` do Notebook 1 continua funcionando, porque o front matter e o título `#` ficam antes da primeira seção. Todos os `.md` têm seções `##` (média de 6,3 por documento).
- **`.txt`**: texto puro, sem cabeçalho de metadados. Os metadados deles estão em `_meta/manifest.jsonl` (e `acesso` também pela pasta).
- **`_meta/manifest.jsonl`**: uma linha por documento (`doc_id`, `path`, `titulo`, `categoria`, `acesso`, `unidade`, `status`, `formato`, `palavras`, `bytes`).

## Valores canônicos (resumo)

Troca em **30 dias corridos**; vale-compras de **120 dias** (promoção); arrependimento **7 dias**; reembolso **10 dias úteis**; frete grátis acima de **R$ 199** (Sudeste) e **R$ 299** (demais regiões); entrega **3 dias úteis** (capitais) e **8** (interior); retirada em **4 horas**; atraso (>**5** dias úteis) = cupom de **R$ 25**; garantia **12 meses**; garantia estendida em **30 dias** (+**12 meses**); até **10x** sem juros (parcela mínima **R$ 50**); Pix **5%**; **3 pontos** por R$ 1; resgate a cada **1000 pontos** = R$ 10; pontos expiram em **12 meses**; aniversário **15%**. Interno: gerente até **10%**, tolerância de **7 dias**, margem mínima **15%**. Códigos do núcleo: `ERR-4217` (Pix), `ERR-5308` (cartão), `ERR-7142` (endereço). Cupom `FRETE100` **não existe**. Tudo em `_meta/fatos_canonicos.json`.

## Perguntas de teste (`_avaliacao/perguntas_teste.jsonl`)

201 perguntas, uma por linha. Campos: `id`, `tipo`, `pergunta`, `docs_relevantes` (caminhos), `evidencias` (trechos **literais** que existem nesses documentos), `acesso_requerido`, e, conforme o tipo, `docs_tambem_contem_evidencia`, `historico`/`pergunta_completa`, `docs_armadilha`, `docs_maliciosos`, `resposta_esperada(_para_cliente)`, `comportamento_esperado`.

| Tipo | Qtd | Para que serve |
|---|---|---|
| `natural` | 36 | Busca vetorial; inclui as 14 perguntas originais dos notebooks (T1, T2, T3.5) |
| `codigo` | 38 | `ERR-NNNN` sozinho, BM25 x vetorial, híbrida (T2.5); inclui códigos vizinhos (`4271`, `5380`, `7124`) parecidos com os do núcleo |
| `composta` | 8 | Trecho pai (T3.3) |
| `conversa` | 10 | Reescrita com histórico (T3.1) |
| `permissao` | 10 | Só existem em `interno/`: com filtro `acesso = publico` a resposta deve ser "não encontrei" (T2.3) |
| `fora_da_base` | 12 | Limiar de similaridade (T2.4); nenhum documento trata desses assuntos |
| `versionamento` | 9 | A versão revogada em `publico/historico/` é a armadilha |
| `seguranca` | 5 | Documentos em `_seguranca_teste/` (T3.6) |
| `produto` | 32 | Busca por SKU, preço, garantia |
| `unidade` | 35 | Filtro por metadado `unidade` |
| `protocolo` | 6 | Busca exata por número de protocolo em `.txt` internos |

Todas as evidências foram verificadas automaticamente contra os documentos.

## Observações e limitações

- **Os valores não dependem do RA**, ao contrário da base original. Se quiserem manter números personalizados por aluno, o caminho é selecionar/derivar a partir de `fatos_canonicos.json`, ou trocar o valor antes de indexar (as perguntas e evidências trazem os valores canônicos).
- Os 3 códigos de erro do núcleo e as perguntas originais usam os valores canônicos acima (não os da base original).
- **Data de referência do corpus: fim de 2026.** Algumas atas de comitês (nov. e dez. de 2026) têm data posterior a 12/11/2026; tratem-nas como reuniões já realizadas.
- O total de colaboradores citado na empresa (cerca de 2.400) inclui sede e centro de distribuição; a soma das unidades é de 1.552.
- Detalhes de redação que não são políticas (nomes de botões, dicas, exemplos) foram inventados pelos redatores e podem variar entre documentos; os **números e regras** foram verificados contra o cânone (`_meta/scripts/validar.py`: 0 problemas em 987 documentos gerados).
- Os documentos de `_seguranca_teste/` contêm instruções maliciosas **fictícias e inofensivas**, rotuladas como sintéticas.
- Reprodução: `_meta/scripts/gerar_specs.py` (manifesto de especificações), `montar_nucleo.py`, `montar_seguranca.py`, redação por agentes (`_meta/PROMPT_REDATOR.md`), `finalizar.py`, `validar.py`, `perguntas.py`.
