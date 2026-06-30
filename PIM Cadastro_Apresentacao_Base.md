30 | Junho 2026 

## **OBJETIVO DA AGENDA** 

## **Objetivo da agenda** 

Visão geral sobre o trabalho de aprofundamento realizado, abordando os seguintes tópicos: 

✓ C ✓ E ✓ F ✓ A 

**Resultados Esperados** 

## **ALINHAMENTO DE EXPECTATIVAS** 

**==> picture [324 x 67] intentionally omitted <==**

## **Ju DESENVOLVEDORA** 

Foco na **geração de eficiência operacional** para garantir a escala omnichannel 

Ao longo das últimas semanas foram realizadas agendas com os times de:  Cadastro; E-commerce (Varejo); Profarma ON (Distribuição) com o objetivo de: 

Entender o funcionamento atual do processo Identificar dores e oportunidades 

Definir o papel esperado do PIM dentro da arquitetura atual 

Apoiar a decisão de solução futura 

**O que esta entrega é:** um norte claro sobre o que precisa ser construído e por quê. A direção estratégica do produto está definida. 

**O que esta entrega não é:** o "como" — backlog, sprints, arquitetura técnica detalhada. PIM é um produto completo; existem empresas inteiras dedicadas só a isso. O detalhamento de execução vem na sequência, não nesta etapa. 

Drive de priorização: Recomendação: iniciar pelo Varejo, expandir para Distribuição em um segundo momento, devido a volume de problemas mapeados, maturidade de integração, criticidade para o cliente final 

## **CONTEXTO DO PIM** 

**==> picture [86 x 36] intentionally omitted <==**

**Objetivo:** nivelar todo mundo sobre por que o projeto existe. **Conteúdo em 3 colunas (reaproveitando a estrutura já validada):** 

- **Por que foi solicitado** — fragmentação de dados, inconsistências, retrabalho 

- **Qual problema ataca** — a versão final e unificada da descrição do problema já trabalhada 

• **O que o PIM não é** — não substitui ERPs, não gerencia preço/estoque/promoção, não recria o workflow da Cervello **Nota de apresentação:** rápido — a audiência já deve ter algum contexto prévio. Use para reforçar, não para ensinar do zero. 

## **FLUXO AS-IS** 

**==> picture [86 x 36] intentionally omitted <==**

**Objetivo:** mostrar que o entendimento do cenário atual é sólido, sem entrar em detalhe operacional excessivo. **Conteúdo:** 

- Diagrama simplificado de alto nível com dois blocos paralelos: Fluxo de Lançamento e Fluxo de Manutenção 

- Lançamento: Cervello → validações → comitê → ERPs, com destaque para o SLA (27 dias vs. meta de 11) 

- Manutenção: múltiplas origens (Cervello, Teams, e-mail) convergindo sem rastreabilidade — representar visualmente a fragmentação, não listar cenários 

## **DORES E PROBLEMAS IDENTIFICADOS** 

**Impedimentos:** 

## **Pontos de atenção:** 

Dependência da segregação de canais na loja e contratos de verba para prática de ofertas exclusivas para o APP 

**Descrição** : Adequação da integração já existente para permitir 

tratamento independente de preços entre APP e SITE, suportando estratégias comerciais específicas por canal 

## **ONDE O PIM APOIA** 

**Descrição** : Adequação da integração já existente para permitir tratamento independente de promoções entre APP e SITE, suportando estratégias comerciais específicas por canal 

**Impacto / Objetivo** : Permitir maior flexibilidade na estratégia de promoções digitais, aumentando competitividade do APP, potencializando conversão e reduzindo dependência de uma política única de ofertas entre os canais 

## **Impedimentos:** 

## **Pontos de atenção:** 

Dependência da segregação de canais na loja e contratos de verba para prática de ofertas exclusivas para o APP 

## **FLUXO TO-BE** 

**Descrição** : Adequação da integração já existente com a VTEX para permitir tratamento independente de preços para a plataforma MEVO, suportando estratégias comerciais 

específicas por canal 

**Impacto / Objetivo** : Garantir que o novo canal possa operar 

corretamente com preços consistentes e alinhados com a 

operação 

## **DECOMPOSIÇÃO FUNCIONAL** 

## **Impedimentos:** 

Definição sobre utilização das filiais do ITEC (19/06 - 27/06) 

**Objetivo:** demonstrar a profundidade do trabalho de 

arquitetura de produto sem entrar em funcionalidade por funcionalidade. 

## **Conteúdo:** 

- Visual dos 8 módulos em grid ou diagrama de camadas, cada um com nome e uma linha de responsabilidade central 

Manutenção e restauração do banco de HML (01/06 - 02/06) 

## **Pontos de atenção:** 

Dependência de homologação com a Delage a partir de 10/06 

- Destaque visual diferenciando módulos de "núcleo" (Catálogo, Ingestão, Governança, Distribuição) dos módulos de "diferencial" (Enriquecimento, Manutenção) 

- Frase de apoio: "Esta decomposição é a base para o backlog técnico — não vamos detalhar cada funcionalidade aqui, mas o documento de apoio traz o detalhamento completo" 

## **DEPENDÊNCIAS E RISCOS** 

## **Impedimentos:** 

Definição sobre utilização das filiais do ITEC (19/06 - 27/06) 

Manutenção e restauração do banco de HML (01/06 - 02/06) 

## **Pontos de atenção:** 

**Objetivo:** mostrar maturidade — antecipar o que pode bloquear o projeto antes que isso vire surpresa. 

Dependência de homologação com a Delage a partir de 10/06 

## **Conteúdo:** 

- Top 4-5 dependências mais críticas (não as 8 completas), com ícone de criticidade 

- Destaque visual separado para o risco de maior probabilidade × impacto (provavelmente: dados inconsistentes herdados dos ERPs) 

- Frase de fechamento: "Essas dependências não são causadas pelo PIM — são pré-condições para que ele entregue valor" 

## **AQUISIÇÃO VS INTERNALIZAÇÃO** 

## **Impedimentos:** 

Definição sobre utilização das filiais do ITEC (19/06 - 27/06) 

Manutenção e restauração do banco de HML (01/06 - 02/06) 

**Iniciativa** : MEVO | **Item** : Integração de Promoções | **Status** 

**atual** : Deploy programado 

## **Pontos de atenção:** 

Dependência de homologação com a Delage a partir de 10/06 

**Descrição** : Adequação da integração já existente com a VTEX 

para permitir tratamento independente de promoções para a 

plataforma MEVO, suportando estratégias comerciais 

específicas por canal 

**Impacto / Objetivo** : Garantir que o novo canal possa operar 

corretamente com preços consistentes e alinhados com a 

operação 

## **PRÓXIMOS PASSOS** 

## **Impedimentos:** 

Definição sobre utilização das filiais do ITEC (19/06 - 27/06) 

Manutenção e restauração do banco de HML (01/06 - 02/06) 

**Iniciativa** : MEVO | **Item** : Integração de Promoções | **Status** 

**atual** : Deploy programado 

## **Pontos de atenção:** 

Dependência de homologação com a Delage a partir de 10/06 

**Descrição** : Adequação da integração já existente com a VTEX 

para permitir tratamento independente de promoções para a 

plataforma MEVO, suportando estratégias comerciais 

específicas por canal 

**Impacto / Objetivo** : Garantir que o novo canal possa operar 

corretamente com preços consistentes e alinhados com a 

operação 

