# PIM Cadastro

## **OBJETIVO DA AGENDA**

## **Objetivo da agenda**

Visão geral sobre o trabalho de aprofundamento realizado, abordando os seguintes tópicos:

- Contextualização
- Cenário Atual (AS-IS)
- Dores e problemas identificados
- Cenário Futuro (TO-BE)
- Decomposição Funcional do PIM
- Dependências e riscos
- Direcionamento: Aquisição ou Internalização
- Próximos Passos

**Resultados Esperados**

- Nivelar o entendimento sobre o problema a ser resolvido
- Apresentar o papel esperado do PIM dentro da arquitetura atual
- Consolidar a visão proposta para o funcionamento do PIM Cadastro
- Demonstrar a decomposição funcional do produto
- Evidenciar dependências, riscos e próximos passos

## **ALINHAMENTO DE EXPECTATIVAS**

Ao longo do aprofundamento, foram mapeados o cenário atual, os principais problemas, a visão futura do produto e a decomposição funcional do PIM Cadastro.

**O que esta entrega é:** uma consolidação do problema, da visão TO-BE e das capacidades esperadas do PIM Cadastro.

**O que esta entrega não é:** detalhamento de backlog, sprints ou arquitetura técnica detalhada.

**Observação:** a operação de Distribuição será contemplada em fases futuras do projeto, o que inclui a integração com o SAP e distribuição de dados para o canal Profarma ON.

## **CONTEXTO DO PIM**

**Objetivo:** nivelar o entendimento sobre por que o projeto existe.

### Problema a ser resolvido

A fragmentação dos dados de produto em sistemas legados (ITEC e SAP), aliada à ausência de governança centralizada e de um repositório para dados complementares, compromete a confiabilidade das informações e a eficiência operacional.

### O que é

O projeto PIM Cadastro propõe a implementação de uma solução de Product Information Management para cadastro, manutenção e governança dos dados cadastrais e complementares de produtos.

O PIM ocupa o espaço que hoje não existe entre os ERPs e os canais digitais: enquanto ITEC e SAP continuam sendo a origem e a fonte oficial dos dados básicos e estruturais, o PIM atua como camada dedicada à governança, enriquecimento e distribuição padronizada dos dados para os sistemas consumidores.

A solução suportará diferentes contextos de negócio (varejo e distribuição), permitindo que determinados atributos possuam variações conforme a necessidade operacional de cada modelo, sem representar duplicidade de dados.

### Responsabilidades do PIM

- Centralizar a ingestão dos dados cadastrais provenientes de sistemas internos e/ou fornecedores
- Consolidar e organizar os dados provenientes de diferentes sistemas, respeitando a origem de cada informação
- Gerenciar e manter os atributos complementares dos produtos, com regras de validação e controle de qualidade da informação
- Controlar o ciclo de vida dos dados de produto, incluindo criação, atualização, validação, aprovação e publicação
- Registrar logs de alterações, com versionamento e suporte a rollback para restauração de estados anteriores
- Orquestrar a distribuição dos dados de forma padronizada e consistente para os sistemas consumidores, respeitando as regras e particularidades de cada canal
- Suportar a gestão de imagens dos produtos, permitindo múltiplas imagens por item e associação conforme necessidade dos canais de venda
- Realizar integrações por meio de APIs e/ou mensageria, conforme o perfil técnico de cada sistema integrado

### O que o PIM não é

- Não substitui os sistemas legados (ERPs) existentes
- ITEC e SAP continuam sendo responsáveis pela origem e manutenção dos dados estruturais e operacionais
- O fluxo atual de cadastro segue nascendo no Cervello
- As validações das áreas continuam acontecendo normalmente
- Os ERPs continuam sendo a fonte oficial dos dados básicos

### Fora do escopo do PIM

- Alterações, customizações ou correções nos sistemas de origem e consumidores (SAP, ITEC, Cervello, Profarma ON, iFood, VTEX, Rappi e demais)
- Gestão de preços, estoque, pedidos, promoções ou regras comerciais
- Criação, produção ou revisão de conteúdo de marketing (imagens, textos comerciais, fotos e vídeos)
- Acesso direto de fornecedores ao PIM, que continuarão interagindo via Cervello
- Substituição dos sistemas legados ou migração de suas responsabilidades para o PIM

## **FLUXO AS-IS**

**Objetivo:** apresentar o cenário atual e os principais pontos de fragmentação.

### Ecossistema de sistemas e integrações

O cenário atual é sustentado por um conjunto de sistemas com papéis distintos e integrações nem sempre estáveis entre si.

### Sistemas de origem — fontes dos dados básicos

- ITEC — ERP responsável pela origem e manutenção dos dados cadastrais da operação de varejo (d1000)
- SAP — ERP responsável pela origem e manutenção dos dados cadastrais da operação de distribuição (Profarma)
- Cervello — plataforma de gestão de chamados adaptada para operar como workflow de cadastro e manutenção de produtos
- Simplus/Syndigo — plataforma externa de dados de produto, integrada ao workflow da Cervello como etapa do fluxo de lançamento

### Sistemas consumidores — canais que recebem e utilizam os dados

- VTEX — plataforma de e-commerce do varejo (d1000)
- iFood e Rappi — plataformas de venda online do varejo (d1000)
- Profarma ON — plataforma de venda online da distribuição (Profarma)

### Sistemas de apoio ao e-commerce

- Shopnext — plataforma integrada com a VTEX, utilizada pelo time de e-commerce para alterações e publicações automatizadas de dados, incluindo imagens
- Placeholder e Intellibrand — fontes complementares de imagens utilizadas pelo time de e-commerce, sem uma política formal de prioridade

### Fluxo de lançamento atual

- O fluxo de lançamento é conduzido e centralizado pela plataforma Cervello
- Atualmente, o fluxo tem duração média de 16 dias
- São realizados aproximadamente 150 a 180 cadastros de EANs mensalmente

**Etapas principais:**

1. Submissão pelo fornecedor na Cervello
2. Integração com a Simplus para verificação do EAN e enriquecimento quando disponível
3. Validações internas por Cadastro, Comercial, Regulatório, Pricing e Fiscal
4. Comitê de decisão de compra
5. Conclusão do cadastro e integração com os ERPs
6. Validação manual posterior nos ERPs pelo time de Cadastro

### Fluxo de manutenção atual

O fluxo de manutenção é, na visão dos times, a maior dor operacional do cenário atual.

Não existe um canal único pelo qual as solicitações de manutenção devem obrigatoriamente passar. Na prática, as demandas chegam por uma combinação de caminhos:

- Via Cervello
- Via Teams e e-mail
- Via sinalização da indústria
- Via percepção de impacto em indicadores

### Cenários típicos de manutenção

- Atualização de dados pelo fornecedor
- Erro regulatório identificado internamente
- Imagem desatualizada identificada por auditoria
- Troca de EAN
- Produto inativo permanecendo visível nos canais

## **DORES E PROBLEMAS IDENTIFICADOS**

### Visão geral

As dores mapeadas ao longo do Discovery evidenciam que os impactos do cenário atual não se restringem a um único time ou processo, pois atravessam áreas, sistemas e canais.

### Consistência e rastreabilidade

- Fragmentação dos dados entre ITEC, SAP e fontes externas
- Ausência de governança centralizada
- Ausência de repositório para dados complementares
- Integrações nem sempre estáveis entre sistemas
- Correções realizadas na origem não chegam à ponta
- Ausência de rastreabilidade centralizada no fluxo de manutenção

### Operacionais

- Retrabalho e correções manuais nos sistemas e canais de venda
- Validação manual posterior nos ERPs
- Pontos de intervenção manual conhecidos, como o preenchimento do campo "Grupo de Preço" no SAP
- Processo de manutenção fragmentado, informal e sem estrutura
- Enriquecimento de produtos sem fluxo estruturado

### Perspectiva Cadastro

O time de Cadastro opera no centro do fluxo de dados de produto, sendo ao mesmo tempo responsável pela qualidade das informações e refém das limitações dos sistemas e processos que o cercam.

O resultado é um time que valida por amostragem o que deveria ser validado por completude, corrige manualmente o que deveria ser automatizado e opera sem visibilidade consolidada sobre o estado real das informações.

### Perspectiva E-commerce

O time de E-commerce é a camada mais próxima do cliente final e, por consequência, o primeiro a sentir e a ter que resolver os impactos das inconsistências geradas.

A ausência de propagação automática de dados entre os sistemas força intervenções diretas na VTEX que deveriam ser desnecessárias. A falta de governança sobre a árvore mercadológica e o mapeamento de categorias amplia a necessidade de ações manuais e repetitivas.

### Perspectiva Profarma ON

Os dados básicos do SAP atendem à necessidade operacional do canal, mas a qualidade e atualização das imagens são um ponto crítico.

## **ONDE O PIM APOIA**

O PIM atua como a camada dedicada de governança, enriquecimento e distribuição dos dados de produto entre os ERPs e os canais digitais.

Com a implementação da solução, a organização passa a contar com uma camada dedicada de governança e distribuição de dados de produtos, viabilizando uma gestão mais eficiente, rastreável e padronizada.

### Resultados esperados

- Melhorar a eficiência operacional no processo de cadastro e manutenção de produtos
- Reduzir retrabalho e correções manuais nos sistemas e canais de venda
- Aumentar a velocidade de disponibilização de produtos nos canais digitais
- Garantir governança sobre os dados, padronização, controle de alterações, integridade, consistência e rastreabilidade das informações ao longo de todo o ciclo de vida do produto
- Permitir a gestão dos dados por canal de venda, garantindo que cada sistema consumidor utilize apenas os atributos relevantes para sua operação
- Possibilitar escalabilidade na inclusão de novos canais de venda e sistemas consumidores

## **FLUXO TO-BE**

### Princípios da visão futura

O fluxo de lançamento no TO-BE mantém a Cervello como ponto de entrada e os ERPs como sistemas de origem dos dados estruturais do produto. O PIM não substitui nem replica essa responsabilidade.

Os dados estruturais continuam nascendo, sendo validados e mantidos nos ERPs. O PIM recebe esses dados por leitura, os utiliza como referência e os distribui para os canais consumidores.

### Fluxo de lançamento de produtos

**Etapa 1 — Submissão pelo fornecedor (Cervello)**

- Ator: Fornecedor
- Sistema: Cervello
- A integração com a Simplus é acionada para verificação do EAN e captura automática de dados quando disponíveis

**Etapa 2 — Validações internas (Cervello)**

- Atores: Times de Cadastro, Gestão de Categorias e Sell Out
- Sistema: Cervello
- Cada área valida e complementa as informações dentro de sua alçada

**Etapa 3 — Comitê de decisão de compra (Cervello)**

- Atores: Áreas comerciais envolvidas
- Sistema: Cervello
- Em caso de reprovação, o fluxo é encerrado; em caso de aprovação, o fluxo avança

**Etapa 4 — Conclusão do cadastro e gatilho de integração (Cervello → ERPs → PIM)**

- Ator: Time de Cadastro
- Sistemas: Cervello, ITEC, SAP, PIM
- A confirmação do time de Cadastro dispara duas ações simultâneas e independentes:
  1. Automação de integração com os ERPs
  2. Envio ao PIM dos dados complementares coletados ao longo do workflow na Cervello
- Esta etapa pressupõe trabalho prévio de mapeamento e configuração dos campos complementares na Cervello

**Etapa 5 — Gate de qualidade (PIM)**

- Ator: PIM (automático)
- Sistema: PIM
- O PIM aplica o gate de qualidade sobre os dados recebidos, verificando completude e consistência dos campos definidos como obrigatórios para o lançamento do produto
- Se aprovado, o produto avança para enriquecimento e publicação
- Se reprovado, o PIM gera notificação ao time responsável e o produto não é distribuído até que as pendências sejam resolvidas

**Etapa 6 — Enriquecimento complementar (PIM)**

- Atores: Time de E-commerce, Time de Cadastro, parceiros externos
- Sistema: PIM
- O PIM disponibiliza o registro para enriquecimento com atributos complementares
- O enriquecimento pode ser realizado diretamente no PIM pelos times internos autorizados ou de forma automatizada por parceiros externos integrados

**Etapa 7 — Publicação nos canais (PIM → canais consumidores)**

- Ator: PIM (automático)
- Sistemas: VTEX, iFood, Rappi, Profarma ON
- O PIM orquestra a distribuição dos dados para cada canal consumidor, enviando apenas os atributos definidos como relevantes para cada plataforma

### Fluxo de manutenção de produtos

No TO-BE, o PIM passa a ser o canal único e oficial de manutenção de dados de produto para os canais digitais.

### Canais de entrada de manutenção

- Canal 1 — Fornecedor via Cervello
- Canal 2 — Time interno via interface do PIM
- Canal 3 — Integração automática com parceiros de enriquecimento
- Canal 4 — Alerta automático do PIM

### Fluxo de aprovação por tipo de campo

- Campos de aprovação direta
- Campos com workflow de aprovação
- Campos somente leitura no PIM quando o sistema master é o ERP

### Gestão de imagens

No TO-BE, o PIM passa a ser o repositório central de imagens de produto, eliminando a gestão descentralizada e manual que caracteriza o cenário atual.

## **DECOMPOSIÇÃO FUNCIONAL**

**Objetivo:** demonstrar a estrutura funcional do produto sem detalhar exaustivamente cada funcionalidade.

O produto é composto por oito módulos funcionais:

1. **M1 — Catálogo de Produtos** — Repositório central e único dos dados de produto
2. **M2 — Ingestão e Integração** — Recepção e consolidação de dados de sistemas de origem e parceiros
3. **M3 — Governança e Qualidade** — Regras, validações, pendências e controle de qualidade
4. **M4 — Enriquecimento de Conteúdo** — Gestão estruturada de atributos complementares e imagens
5. **M5 — Ciclo de Vida do Produto** — Controle de estados, versionamento e rastreabilidade
6. **M6 — Distribuição por Canal** — Publicação e propagação de dados para sistemas consumidores
7. **M7 — Manutenção e Solicitações** — Canal único, governado e auditável para manutenção
8. **M8 — Administração e Configuração** — Configuração operacional do produto com mínima dependência de TI

### Destaques da decomposição funcional

- Registro único por produto identificado pelo EAN como chave primária
- Suporte a múltiplos EANs por produto
- Suporte a atributos com valores distintos por contexto de negócio
- Modelo de atributos por categoria
- Campos de origem ERP como somente leitura no PIM
- Gate de qualidade na ingestão
- Regras de validação por campo e validação regulatória
- Repositório central de imagens com versionamento e rollback
- Máquina de estados do produto
- Propagação de inativação
- Publicação inicial e propagação de atualizações por canal
- Central de solicitações de manutenção
- Configuração de integrações, canais e regras de distribuição

## **DEPENDÊNCIAS E RISCOS**

### Dependências

1. Integração Cervello → ERPs
2. Qualidade dos dados de origem nos ERPs (ITEC e SAP)
3. Mapeamento e adição dos campos complementares na Cervello
4. Governança da árvore mercadológica
5. Alinhamento organizacional do processo de manutenção
6. Avaliação de viabilidade de integração com parceiros de enriquecimento

### Riscos

A maioria das dependências e riscos identificados tem origem em problemas preexistentes no ecossistema atual, portanto não são criados pelo PIM, mas precisam ser endereçados para que o PIM entregue valor.

### Destaque

Os dados inconsistentes herdados dos ERPs representam um risco relevante, pois o PIM ingerirá esses dados como base do catálogo central e os distribuirá para os canais.

## **AQUISIÇÃO VS INTERNALIZAÇÃO**

O material apresenta como direcionamento de avaliação as seguintes alternativas:

- Syndigo PIM
- Akeneo
- Stibo Systems
- inRiver
- Informatica (Salesforce)

## **PRÓXIMOS PASSOS**

O próximo passo é transformar a visão consolidada em direcionamento de evolução do produto.

### Próximas ações

1. Validar a proposta de TO-BE
2. Validar a decomposição funcional do produto
3. Endereçar dependências críticas para viabilizar a evolução do projeto
4. Apoiar a decisão entre aquisição ou internalização
