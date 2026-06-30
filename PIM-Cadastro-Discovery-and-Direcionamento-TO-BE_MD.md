GRUPO PROFARMA · TIME DE TI DIGITAL 

**PIM Cadastro — Discovery & Direcionamento TO-BE** Resultado das 5 semanas de aprofundamento | Time de TI Digital **Data** · **Versão** · **Autor(es)** 

## **O que essa apresentação entrega** 

Esta apresentação consolida o trabalho das 5 semanas de Discovery e estabelece a base para as decisões que os times de negócio e TI precisam tomar a seguir. 

## **O que foi feito** 

5 semanas de Discovery: entrevistas com as áreas de Cadastro, E-commerce e Distribuição/Profarma ON, mapeamento de sistemas e análise do ecossistema ASIS. 

**O que entregamos hoje** Diagnóstico das dores por camada, dependências críticas, riscos com mitigações e proposta funcional TO-BE para validação dos times. 

**O que ainda será validado** Decisão build vs. buy, definição do MVP, processo formal de manutenção e capacidade do squad — com critérios e próximos passos definidos. 

## **Por que o PIM foi solicitado** 

## **O problema** 

Dados fragmentados, sem governança centralizada, gerando inconsistências nos canais digitais e retrabalho manual recorrente entre times de cadastro, e-commerce e distribuição. 

## **O objetivo declarado** 

Repositório central e distribuidor oficial dos dados de produto, garantindo padronização e rastreabilidade em VTEX, iFood, Rappi, PEL e Delage. 

## **O que o PIM não é** 

Não substitui ITEC nem SAP. Não gerencia estoque, preços ou promoções. Não recria o workflow da Cervello. O escopo é específico: **dados de produto e sua distribuição.** 

## **Como conduzimos o Discovery** 

## **Áreas entrevistadas** 

**Linha do tempo — 5 semanas** 

Cadastro 

## **Semanas 1–2** 

- e E-commerce 

Distribuição / Profarma ON 

Mapeamento AS-IS: 

entrevistas, 

## **Sistemas mapeados** 

> levantamento de **Semanas 3–4** 

processos e identificação 

e Cervello, ITEC, SAP dos sistemas envolvidos. Aprofundamento e e análise: validação de VTEX, Shopnext integrações, ° Simplus / Syndigo **Semana 5** @ mapeamento de falhas e e iFood, Rappi, PEL, Delage consolidação de dores. Consolidação e proposta 

TO-BE: visão funcional, 

dependências críticas e riscos com mitigações. 

## **Como o ecossistema funciona hoje** 

O mapeamento AS-IS revelou um ecossistema fragmentado, com múltiplas fontes de origem e canais consumidores operando com integrações diretas que falham individualmente — sem camada central de governança. 

## **O que o Discovery revelou: dores por camada** 

## **Dados e origem** 

- Inconsistência quando fornecedor preenche sem Simplus 

- Integração Cervello → ERP falha ou chega incompleta 

- Preenchimento manual no SAP 

- Árvore mercadológica divergente entre d1000 e VTEX 

## **Manutenção e ciclo de vida** 

- Atualizações no ERP não refletem nos canais 

- Produtos inativos continuam visíveis na VTEX 

- Troca de EAN gera duplicidade 

- Manutenções chegam por canais informais 

## **Canais e distribuição** 

- Imagens desatualizadas ou divergentes chegando ao cliente Medidas erradas causando cancelamento logístico 

- Produtos em categorias incorretas 

- E-commerce sem visibilidade de inativação 

## **Dependências críticas e riscos mapeados** 

O PIM só funcionará se estas quatro condições forem atendidas antes do go-live. Os riscos abaixo requerem ação preventiva. 

**2** 

**1 3** 

## **Estabilização Cervello → ERP** 

## **Qualidade dos dados de origem** 

Dados inconsistentes acumulados precisam de higienização com critério de aceite. 

Falhas upstream se tornam falhas do PIM em escala. 

|**3**<br>**Governança da árvore mercadológica**<br>Versão validada com match para VTEX; requer decisão de negócio.<br>**4**<br>**Processo formal de manutenção**<br>Inativação de canais informais (Teams, e-mail) como parte do go-live.|
|---|
|**Risco**<br>**Origem**<br>**Impacto no PIM**<br>**Mitigação proposta**<br>Dados inconsistentes dos ERPs<br>Acúmulo histórico + falhas<br>Cervello→ERP<br>Distribui inconsistência em escala<br>Gate de qualidade + higienização com critério de aceite<br>Árvore mercadológica sem governança<br>Criação de categorias fora de<br>processo<br>Inconsistências em todos os canais<br>Congelar novos nós + corrigir antes da distribuição<br>Manutenção sem dono definido<br>Fluxo em Cervello, Teams e e-mail<br>Manutenções fora do PIM<br>Processo formal + inativar canais informais no go-live<br>Sem política de imagem<br>Fontes concorrentes sem regra<br>Curadoria manual constante<br>Política por categoria antes de configurar módulo<br>Sem sistema master por campo<br>Atributos com múltiplas origens<br>Conflitos de sobrescrita<br>Workshop de responsabilidades por campo<br>Complexidade de legados<br>Especificidades ITEC, SAP, Cervello<br>Atrasos e retrabalho<br>Priorizar integrações por criticidade; não integrar tudo no MVP<br>Custo/prazo acima (se build)<br>Escopo amplo com customizações<br>Comprometimento do roadmap<br>Benchmarking com plataformas antes da decisão|



## **Governança da árvore mercadológica** 

Versão validada com match para VTEX; requer decisão de negócio. 

## **Visão funcional TO-BE proposta** 

**Esta é uma proposta construída com base no Discovery. Precisamos da validação de vocês.** 

## **Fluxos TO-BE propostos** 

## **Lançamento de produtos** 

01 

## **Fornecedor via Cervello** 

Workflow de aprovação: Cadastro, Comercial, Regulatório e Fiscal 

## **Manutenção de produtos** 

01 

## **Origens de solicitação** 

Fornecedor via Cervello · Time interno no PIM · Parceiro (ex: Simplus) · Alerta automático do PIM 

02 

02 

## **PIM recebe dados consolidados** 

Gate de qualidade: completude mínima atingida? 

## **Validação e aprovação** 

Conforme regra do campo, com rastreabilidade completa 

03 

## **Distribuição simultânea** 

✓ SIM → VTEX, iFood, Rappi, PEL, Delage 

� Notificação ao time com campo(s) pendente(s) 

03 

## **Propagação e log** 

PIM propaga para canais afetados; log com responsável, data e versão anterior 

Nenhuma manutenção por Teams ou e-mail — toda correção passa pelo PIM e gera rastreabilidade. 

## **A decisão que ainda precisa ser tomada** 

## **Plataforma de mercado** 

## **Desenvolvimento interno** 

Akeneo, Pimcore, Syndigo 

**Pronto:** modelo varejo/farmácia, conectores VTEX, gestão de imagens, workflows, versionamento. 

**A construir:** repositório, workflows, versionamento, imagens, delta sync, APIs. 

**Vantagem:** controle total, sem licença, customização irrestrita. 

**A construir:** integrações ITEC, SAP, Cervello; customizações regulatórias. 

**Risco:** 18–24 meses para squad; competição com demandas urgentes. 

**Risco:** custo de licença + dependência de fornecedor. 

**Para decidir:** benchmarking de custo total, avaliação de aderência regulatória e capacidade do squad. 

