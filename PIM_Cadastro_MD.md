30/06/2026, 07:39 

PIM Cadastro 

## PIM Cadastro 

## Sumário 

Contextualização Problema a ser resolvido O que é Responsabilidades do PIM O que NÃO é Fora do escopo do PIM: Objetivo e resultado esperado - Cenário Atual (AS IS) Ecossistema de sistemas e integrações Sistemas de origem — fontes dos dados básicos Sistemas consumidores — canais que recebem e utilizam os dados Sistemas de apoio ao e-commerce Fluxo de dados atual Fluxo de lançamento de produtos Etapas do fluxo 1. Submissão pelo fornecedor 2. Validações internas 3. Comitê de decisão de compra 5. Etapa apartada de E-commerce Fluxo de manutenção de produtos Origens das solicitações de manutenção Via Cervello Via Teams e e-mail Via sinalização da indústria Via percepção de impacto em indicadores Cenários típicos de manutenção Cenário 1 — Atualização de dados pelo fornecedor Cenário 2 — Erro regulatório identificado internamente Cenário 3 — Imagem desatualizada identificada por auditoria Cenário 4 — Troca de EAN Cenário 5 — Produto inativo permanecendo visível nos canais Enriquecimento de produtos Mapeamento de dores e problemas - Dores e problemas Experiência do cliente Dores e problemas - Consistência entre sistemas/canais - Dores e problemas Operacionais Perspectiva Cadastro Perspectiva E-commerce Perspectiva Profarma ON - Cenário Futuro (TO BE) Fluxo de lançamento de produtos — Etapa 1 Submissão pelo fornecedor (Cervello) — Etapa 2 Validações internas (Cervello) — Etapa 3 Comitê de decisão de compra (Cervello) Etapa 4 — Conclusão do cadastro e gatilho de integração (Cervello → ERPs → PIM) — Etapa 5 Gate de qualidade (PIM) — Etapa 6 Enriquecimento complementar (PIM) Etapa 7 — Publicação nos canais (PIM → canais consumidores) Fluxo de manutenção de produtos Canais de entrada de manutenção Canal 1 — Fornecedor via Cervello Canal 2 — Time interno via interface do PIM Canal 3 — Integração automática com parceiros de enriquecimento Canal 4 — Alerta automático do PIM Fluxo de aprovação por tipo de campo Mecanismo de propagação para canais Gestão de Imagens PIM como repositório central de imagens Política de prioridade de fonte por categoria Atualização e versionamento de imagens Propagação de imagens para os canais Decomposição Funcional do PIM 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

1/28 

30/06/2026, 07:39 

PIM Cadastro 

Visão Geral dos Módulos M1 — Catálogo de Produtos Registro de produto Modelo de dados por contexto Modelo de atributos por categoria Dados estruturais (origem ERP) Dados complementares (origem PIM) Árvore mercadológica M2 — Ingestão e Integração Integração com ITEC Integração com SAP Integração com Cervello Integração com parceiros Integração com sistemas consumidores Monitoramento de integrações M3 — Governança e Qualidade Gate de qualidade na ingestão Regras de validação por campo Validação regulatória Gestão de alertas e pendências Governança da árvore mercadológica M4 — Enriquecimento de Conteúdo Gestão de atributos complementares Repositório central de imagens Política de prioridade de fonte de imagem Recebimento e validação de imagens de parceiros M5 — Ciclo de Vida do Produto Máquina de estados do produto Propagação de inativação Versionamento de dados Rollback Log de auditoria M6 — Distribuição por Canal Configuração de canais consumidores Regras de atributos por canal Publicação inicial Propagação de atualizações Controle de publicação por canal Painel de status de distribuição M7 — Manutenção e Solicitações Central de solicitações de manutenção Criação de solicitação via interface PIM Aplicação e propagação da manutenção Notificações e comunicação 

M8 — Administração e Configuração Gestão de usuários e perfis de acesso Configuração do modelo de dados Configuração de regras de negócio e validação Configuração de integrações Configuração de canais e regras de distribuição Monitoramento operacional Dependências e riscos Dependências 

1. Integração Cervello → ERPs 

2. Qualidade dos dados de origem nos ERPs (ITEC e SAP) 

3. Mapeamento e adição dos campos complementares na Cervello 

4. Governança da árvore mercadológica 

5. Alinhamento organizacional do processo de manutenção 

6. Avaliação de viabilidade de integração com parceiros de enriquecimento Riscos Direcionamento: Aquisição ou Internalização 

Próximos Passos 

## Contextualização 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

2/28 

30/06/2026, 07:39 

PIM Cadastro 

## Problema a ser resolvido 

A fragmentação dos dados de produto em sistemas legados (ITEC e SAP), aliada à ausência de governança centralizada e de um repositório para dados complementares, compromete a confiabilidade das informações em toda a cadeia. Desde a gestão interna, marcada por retrabalho, ações manuais e falta de rastreabilidade, até os canais digitais, onde essas inconsistências impactam diretamente a experiência e a confiança do cliente final. 

## O que é 

O projeto PIM Cadastro propõe a implementação de uma solução de Product Information Management para cadastro, manutenção e governança dos dados cadastrais e complementares de produtos da d1000 e Profarma, incluindo diferentes atributos, descrições e imagens. A plataforma atuará como repositório central de enriquecimento e distribuição, garantindo padronização, integridade, consistência e rastreabilidade dos dados nos canais de venda digitais. 

O PIM ocupa o espaço que hoje não existe entre os ERPs e os canais digitais: enquanto ITEC e SAP continuam sendo a origem e a fonte oficial dos dados básicos e estruturais, o PIM atua majoritariamente após essa camada, enriquecendo, complementando e distribuindo as informações de forma padronizada para cada sistema consumidor. O PIM será, portanto, a fonte oficial para consumo dos dados de produto pelos canais, sem substituir nem concorrer com os sistemas de origem. 

A solução suportará diferentes contextos de negócio (varejo e distribuição), permitindo que determinados atributos possuam variações conforme a necessidade operacional de cada modelo, sem que isso represente duplicidade de dados. 

- OBS: A operação de Distribuição será contemplada em fases futuras do projeto, o que inclui a integração com o SAP e distribuição de dados para o canal Profarma ON. 

## Responsabilidades do PIM 

- Centralizar a ingestão dos dados cadastrais provenientes de sistemas internos e/ou fornecedores; 

- Consolidar e organizar os dados provenientes de diferentes sistemas, respeitando a origem de cada informação; 

- Gerenciar e manter os atributos complementares dos produtos, com regras de validação e controle de qualidade da informação; 

- Controlar o ciclo de vida dos dados de produto, incluindo criação, atualização, validação, aprovação e publicação; 

- Registrar logs de alterações, com versionamento e suporte a rollback para restauração de estados anteriores; 

- Orquestrar a distribuição dos dados de forma padronizada e consistente para os sistemas consumidores, respeitando as regras e particularidades de cada canal; 

- Suportar a gestão de imagens dos produtos, permitindo múltiplas imagens por item e associação conforme necessidade dos canais de venda; 

- Realizar integrações por meio de APIs e/ou mensageria, conforme o perfil técnico de cada sistema integrado. 

## O que NÃO é 

O PIM não substitui os sistemas legados (ERPs) existentes. ITEC e SAP continuam sendo responsáveis pela origem e manutenção dos dados estruturais e operacionais, e o fluxo atual de cadastro segue inalterado: as solicitações continuam 

nascendo no Cervello, as validações das áreas (Comercial, Fiscal, Regulatório, entre outras) continuam acontecendo normalmente, e os ERPs continuam sendo a fonte oficial dos dados básicos. 

## Fora do escopo do PIM: 

- Alterações, customizações ou correções nos sistemas de origem e consumidores (SAP, ITEC, Cervello, Profarma ON, iFood, VTEX, Rappi e demais); 

- Gestão de preços, estoque, pedidos, promoções ou regras comerciais; 

- Criação, produção ou revisão de conteúdo de marketing (imagens, textos comerciais, fotos e vídeos); 

- Acesso direto de fornecedores ao PIM, que continuarão interagindo via Cervello; 

- Substituição dos sistemas legados ou migração de suas responsabilidades para o PIM. 

## Objetivo e resultado esperado 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

3/28 

30/06/2026, 07:39 

PIM Cadastro 

Com a implementação da solução, a organização passa a contar com uma camada dedicada de governança e distribuição de dados de produtos, viabilizando uma gestão mais eficiente, rastreável e escalável, o que deverá: 

- Melhorar a eficiência operacional no processo de cadastro e manutenção de produtos, reduzindo falhas cadastrais e inconsistências nas plataformas de venda que afetam a experiência do cliente final; 

- Reduzir retrabalho e correções manuais nos sistemas e canais de venda; 

- Aumentar a velocidade de disponibilização de produtos nos canais digitais; 

- Garantir governança sobre os dados, padronização, controle de alterações, integridade, consistência e rastreabilidade das informações ao longo de todo o ciclo de vida do produto; 

- Suportar diferentes contextos de negócio (varejo e distribuição) em fases futuras, respeitando suas particularidades e permitindo que determinados atributos possuam variações conforme a necessidade operacional de cada modelo; 

   - OBS: Essas variações não representam duplicidade de dados, mas sim adequações necessárias, como por exemplo dimensões de produto considerando unidade (varejo) ou embalagem logística (distribuição); 

- Permitir a gestão dos dados por canal de venda, garantindo que cada sistema consumidor utilize apenas os atributos relevantes para sua operação, respeitando as particularidades de cada plataforma; 

- Possibilitar escalabilidade na inclusão de novos canais de venda e sistemas consumidores. 

## Cenário Atual (AS-IS) 

## Ecossistema de sistemas e integrações 

O cenário atual é sustentado por um conjunto de sistemas com papéis distintos e integrações nem sempre estáveis entre si. 

## Sistemas de origem — fontes dos dados básicos 

- ITEC — ERP responsável pela origem e manutenção dos dados cadastrais da operação de varejo (d1000). É a fonte oficial dos dados estruturais de produto para o canal varejo; 

- SAP — ERP responsável pela origem e manutenção dos dados cadastrais da operação de distribuição (Profarma). É a fonte oficial dos dados estruturais de produto para o canal distribuição; 

- Cervello — Plataforma de gestão de chamados adaptada para operar como workflow de cadastro e manutenção de produtos. É o ponto de entrada do fluxo de lançamento, por onde fornecedores submetem informações e times internos realizam validações; 

- Simplus/Syndigo — Plataforma externa de dados de produto, integrada ao workflow da Cervello como etapa do fluxo de lançamento. Fornece informações enriquecidas automaticamente para os produtos cujos EANs estão cadastrados na plataforma. Nem todos os fornecedores possuem parceria com a Simplus, o que torna sua cobertura parcial. 

## Sistemas consumidores — canais que recebem e utilizam os dados 

- VTEX — Plataforma de e-commerce do varejo (d1000). Principal canal digital consumidor dos dados de produto; 

- iFood e Rappi — Plataformas de venda online do varejo (d1000), consumidoras dos dados de produto; 

- Profarma ON — Plataforma de venda online da distribuição (Profarma), consumidora dos dados de produto. 

## Sistemas de apoio ao e-commerce 

- Shopnext — Plataforma integrada com a VTEX, utilizada pelo time de e-commerce para alterações e publicações automatizadas de dados, incluindo imagens; 

- Parceiros de enriquecimento de dados e imagens — Além da Simplus, o time de e-commerce utiliza Placeholder e Intellibrand como fontes complementares de imagens, sem uma política formal de prioridade entre elas. 

## Fluxo de dados atual 

Visão Macro 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

4/28 

30/06/2026, 07:39 

PIM Cadastro 

Para o varejo, os dados percorrem o seguinte caminho após a conclusão do workflow na Cervello: 

Para a distribuição: 

Essas integrações funcionam de forma predominantemente automatizada, mas com pontos de intervenção manual conhecidos, como por exemplo o preenchimento do grupo de preço no SAP, que não é automatizado e depende de ação manual do time de Cadastro. A integração entre Cervello e ERPs também apresenta algumas falhas, resultando em campos ausentes, incompletos ou incorretos, sem mecanismo de alerta ou reprocessamento estruturado. 

## Fluxo de lançamento de produtos 

- O fluxo de lançamento é conduzido e centralizado pela plataforma Cervello, que foi adaptada para operar como workflow. Atualmente, o fluxo tem duração média de 16 dias (no mês de maio a média estava em 27 dias devido a definições internas), contra uma meta de 11 dias. Esse prazo contempla desde o início do cadastro até o pedido inicial de compra no supply chain, excluindo o tempo adicional do e-commerce, que demanda um tempo adicional por depender da disponibilidade de estoque físico, e que por isso é medido de forma dissociada do SLA principal; 

- São realizados aproximadamente 150 a 180 cadastros de EANs mensalmente. 

## Etapas do fluxo 

## 1. Submissão pelo fornecedor 

O fornecedor acessa a Cervello e inicia o workflow preenchendo os formulários iniciais disponíveis na plataforma. 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

5/28 

30/06/2026, 07:39 

PIM Cadastro 

Concluída essa etapa, o time de Cadastro aciona a integração com a Simplus para verificar se o EAN do produto existe na plataforma. 

- Se o produto existir na Simplus, diversas informações do formulário são preenchidas automaticamente com dados enriquecidos, e o time de Cadastro realiza as validações necessárias; 

- Se o produto não existir na Simplus, todos os dados são preenchidos manualmente pelo fornecedor, o que reduz significativamente a confiabilidade das informações submetidas e aumenta o risco de inconsistências ao longo do fluxo. 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

6/28 

30/06/2026, 07:39 

PIM Cadastro 

Abas Externas: dados do produto, logísticos e fiscais são abas universais preenchidas para qualquer outro distribuidor/varejista para além da Profarma 

Abas Internas: condições da compra, preço sugerido e pedido inicial são abas preenchidas na Simplus pelo fornecedor exclusivamente para a Profarma 

## 2. Validações internas 

— O produto percorre um workflow de validações com diferentes times internos Cadastro, Comercial (Gestão de Categorias e Sell — Out), Regulatório, Pricing e Fiscal , cada um responsável por verificar e complementar as informações dentro de sua alçada. Embora o time de Cadastro não possa alterar diretamente o que o fornecedor preencheu, pode contestar dados inconsistentes e solicitar correções. 

O time de Regulatório exerce papel crítico nesta etapa, sendo responsável por indicar quais itens devem ou não estar listados por questões de controle e retenção de receita. Falhas nessa validação geram marcações incorretas nos canais digitais e impactam o tratamento dos pedidos. 

## 3. Comitê de decisão de compra 

Durante o workflow, existe uma etapa de comitê para deliberação sobre a decisão de compra do produto. O lançamento só avança após aprovação nessa instância. 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

7/28 

30/06/2026, 07:39 

PIM Cadastro 

4. Conclusão do cadastro e integração com os ERPs 

Após aprovação no comitê e validações das áreas de Precificação, Fiscal e Regulatório, o time de Cadastro indica na plataforma que todos os dados foram confirmados. Esse registro serve de gatilho para uma automação que dispara os dados coletados para os dois ERPs simultaneamente (SAP e ITEC). 

## Validações das áreas interna: 

OBS: Produtos que não são medicamentos não passam pela etapa de validação do time regulatório. 

Gatilho para integração: 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

8/28 

30/06/2026, 07:39 

PIM Cadastro 

Após a execução das automações, o time de Cadastro acessa cada ERP individualmente para verificar se as informações foram — corretamente registradas etapa manual e sem rastreabilidade centralizada. 

- SAP - Distribuição = Cadastro acessa uma transação do SAP para realizar a validação dos dados. 

   - O campo "Grupo de Preço" é preenchido manualmente. Serve basicamente para agrupar produtos com preços semelhantes, sendo um processo que precisa ser feito no ERP. 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

9/28 

30/06/2026, 07:39 PIM Cadastro @ setera Auda ey 9° ~)«e1@e¢e a8 ee AIIOAREHR GS Zousarocto Avec Teun eIJ7800135244664Hai7300435244671Bean©~ "||7500435241649 7300435240529ecard7500435241656FSO0NSSZIONIT aedINP23055,e305!235442330923308ootdo Matera 22.0462. 43fa2.02.72.02.432.042.43ee2208.2-7Data SAP Cod.| Fornec SAP (aFabekcantePRGP&GP&GCePRGP06) 00910086[0001SSF06020085F..._|SPRAYFRA_ANTITRANEeANTITRANDieFRADesc.PAMPERSPANPERSProduteQUERA SUPERS. AtacadoOLDOLD PANTE...SUPERS.. **SS** PI.PLPP ANTITRANSP FRADesc.ANTITRANSPutSPRAYRAPANWERSPAMPERSProdutoaeQUERA Ui PANTENE **OLD** SUPERSECSUFERSEC **SPICE** PGPREE.. **CLEA.** XG ..‘Cara Ebarque **12,000** Dd9,000eee10001,000 P P[PSCategorsPF jonreni9tnd807741058(80746127eelCod. **077724** Produtoee,89 Formec FRAPANPERSseeSPRAY **ANTITRANSP** FRAilDesc. MelPAMPERSProdutoQUERA ae SUPERSOLD PANTE..OLDSUPERS. **S** PI.PL Desconto CompraIOS0,000,Cieled0,0,00 **00** FE DUNea17500438244678.17500435240526. **1750** thet7OESISIIOS435241653,0435241645tees HSErb.CauaCeocae0,060Boal **0,000** 0,000Pack 00 **0** Moeitor....Corroradort\rertonmarianartea **rma** borges@profema.com..borges@profsera.com... **r** rartan.borgesGertonrtan.borges@protaemrtan.borges@profborpee@prDorger@prefoana.com.z!@i)| **o** rofaera.comfeane.comn **a** rma.com....com...0, **.** 0)..0.0.0,0.=| ~~ 7) 7991177763998 2322023053, 2.042.722.04.2. 1060 \MIRAFLO..P&G 0091 1236 _KITFRA FIORUCCIPAMPERS FLOR SUPERS...MA. FRAKIT FIORUCCIPAMPERS FLORSUPERSECMARA SAB.XG 3.. 6,0001,000 P (9074612714032024 \KITFRA PAMPERSFIORUCCE FLORSUPERS HA. . 0,000,00 6799117763590 i 0,0000,000 00 ‘artan.borges@orofaera.com...rrara.porto@reded1000.combr 0.0. [Bil17|72960349304387998687734409rescons7e2zz2 235972340923229 06.05.2.99076.05.2.72.042.eee 169199 AS[NESTLE...|1276HYPERAALTHAIA__ 130105271050 |_BENEDESC STARBUCKSBROMIDRATOGIDCOFF 5450+10N6 PLUSFRAPPLICC.DE PEDIA. VOR.-ENOCOFFGBENEDESCSTARBUCSS BROM VORTIOXETINAS#SU#IOMG PLUSFRAPPUCCINOPEDIAT MELEL2G/.SMG MO. _ 50.00024,00070,000_24,000PS60 12591089Ce23007-01187 pcreBENEDESCBROMIDRATOone en PLUS neeDE VOR.PEDIA.. a37,0013,00oa 1789609493043517898687734405eeered 9,000paomnies0.6000,000 |e10 © FEee‘thaane.damascenoGprofarma..fula.gomesGorofarma.combrewertne See atre@orofeanasene conor 1eae0:0. ~ 7991000389225Pemevoseo17 2276822770 27.052.ee 9043 aNESTLE. 1180 NESCAFEeeeeCAPPUCCINO... ei Ee pa eee a eeee[eae] ee E[7898636193899] 7e966SBOSE6927996658040262[24242] 2364022568 01.072. 433713.05.2.13.052. 49464946 LABOFAR..GENIONM_LABOFAR..1382 06751382 _CONDCITALOPRAMPREDNISOLONATIO NACHO20MG40NGGIN_30. **.** GCONDGNESCAFE PREDNISOLONACITALOPRAMTIO CAPPUCCINONACHO20MG GBISENG 40MG7@PR. CANEL.30CPR 4.(.. 50,24,00050,12,000 **000** P **G** 40440001007951125711391008079 NESCAFECONDPREDNISOLONACITALOPRAM TIO CAPPUCCINO... NACHO204640NG GBI.30. 66740,000,00 **,00** 17898636193896 17891000389239 0,0,0000,0000, **000** 0 0 **1** rrarion.borges@profaera.com...jyewerton.sha@protaca.com.br **ula.gomes** t@proferma.combr@protarma.combt =2 0. 30, 7898610377611eeeeee ee ee ee Ce fee ta (Se EN 7| 7896523228297 2343021717 11.102.13.05.2. 18364272 COMEDPROMOVEO1..13341561 ASCPRESKMED HASKELL KMISINH.. BIFUS. ASCPRES KMED HASKELL K-MISINHA INFUSAOTRADI.DEO. 24,00060,000P0 71608144 ASCPRES K-MEDHASKELLK-HISHON IFUS. 9,000,00 1789652322824 0,0000,000 00 mara.porto@rededi000.combrrobson.stra@profarma.combt 0.0. | ||7ensese0se0747e90523228003 21718 11,102. 4272 COMED O1..1334 _K-MED K-MISIVHA TRA. K-HED K-MISIHA TRADICION.. 21,000 0 108145 AGED K-HISIWHA TRA. 0,00 1789623228300 0,000 0 r0dson.stra@profarma.combe 0. | | 7e97947612266 2116116238 4,09204.092. 42721 CONED‘ACHE DL..13341508 PROTENACAL PRO **AE** LO VERAGOCPSD __CALAMEDPROTENA PROALOE 60VERACPS POS SO 32,000030,000 P 1501278101588 PROTEWACALANED ALOEPRO G0CPS VERA 0,0000 1789794761263 0,0000,000 00 eonardo.alves@profarra.com.brpapepoe 0. | |22827701S4049 21014 31.072. 9297 PIERRE 1863 CLEANANCEUV AVENE CLEANANCEUV AVENE TOW 12,000 F po0e6023 CLEANANCE UV AVENE 0,00 3328270154640 0,000 0 marion borges@profarma.com.. 0. | 7908615017846 20879 24.072. 4609 LOREAL 1860 KIT EFFACLARSAB CO... KIT EFFACLARSAB CONCEN 7. 12,000 F 12651300 KIT EFFACLAR SAB CO. 0,00 7998615017860 0,000 0 martan.borges@orofaema.com...0. || 34993200154627908615020297 2069520630 24.072.31.07.2..17614609 LOREALGALDER.. . 04340689 ESMCETAPHILCOLORAMACR PROTODA.AD .. ESMCETAPHE COLORAMACR PROTODA AD RESTOR. PRODU 12,00012,000 PP 112653000106010043 ESMCETAPHRCOLORAMACR PROTODA AD 0,000,00 7908615020303, 0,0000,000 00 leonardopacb.ho@profarma.combr alvest@peotarma.com.br0.0. |_| 7998642871347 20631 04.092. 9011 APTHLOL 1301 TOP SALON YENZAH S. TOP SALON YENZAHSH SOOM 6,000 F 07304 TOP SALON YENZAH S 0,00 17898540472861 0,000 0 ‘ara,porto@rededi000.combr 0, ||_| 7996523226227|7es6s232283107801142206624 217072371516745 431.102.427211.102.14.122. 42729507 COMEDCOMEDHYPERAD1.1334DI..13340726 _EPISOLPRESPRES KMEDKMEDGRUMAK-MISIVH.K-MISINH..FACIAL . PRESPRES K-MEDEPISOLK-MEDGRUMA K-MISINHA K-MISINHAFACIAL FPSSO **B** YVISWIS **L** 602112,000 **,000 0** F 21038-0 **10** 84 **14** 76 **PRES** EPISOL **K-MED** BRUNA **K-H** FACIALISIOMISIN 13,00 **0,00 17** 1789114220682189 **96523283** 2417 **0,000** 0,000 **0** 0 favortabrantes@profarma.com.. **obson.s** ha@profarma.com.ta@profarma.com **b** er **0.** 0. |__| 79974116505107036172516308 1638216091 06.0213.09.228568 MULTILA.AIHI 0455.S061 COLCHICBIACYGNUSD 7000UI 0,5§G C/i_39. CYGNUS COLCHICBIAD 70000,5§NGUI 1230CPRCPSNO. 96,00035,000 6R #2153019026 COLCHICDIACYGNUS D 7000UI0,546 C/t39 75,0010,00 0,0000,000 11 jula,gomes@oroferma.combrthamestevam@profaera.combr 33 |_| 790215157243 16958 341222022 PIRACAN. 1785 COMPOSTO EXCELLEN.. COMPOSTO EXCELLENCE LT 8. 12,000 P 10263 COMPOSTO EXCELLEN 0,00 17998215157240 0,000 0 paclo.fiho@orofarre.combr 0. | | 701150082861 16701 13.122._9677 UNILEVE. 0092 SAB LUX EDB DAMA D._ SAB LUX ESSEN BRASIL DAMA 72,000 P 68710933 SAB LUK EDB DAMA 0 0,00 9789150082864 0,000 0 pad.fiho@orofarra.combr 0. |___ 7891150062779 16544 131229677 UNILEVE 0092 SAB LEQ LUX EDS FLOR. SAB LIQ LUX ESSEN GRASR C. 12,000 P 66710890 SAB LIQ LUX EDS FLOR. 0,00 2791150062773 0,000 0 pacle.tho@profama.combr 0. 79911500824627896112160366 16462 21.12.2133 TEUTO 0423 HEM ZOLPIDEM 106. HEM ZOLPIDEM1066 200R . 100,000 G 036 HEM ZOLPIDEM 10 0,00 1769612160363 0,000 1 3 ||7500435186416 **70** 0 16866 **1** 8.1312 **2** _2 **.** 967743 UNILEVEPRG **00** 9286 SABESPUBARBGRLETTE... LIQ.LUX EDB MAO_. ESPUBARBGRLETTSAB LIQ MAOS LUX **E** SSS **EN** SI1.BR. **12,000 P** e00e+4i16671004 "SAB(ESPULIQ BARB LUK EDB GRLETTEMAO. _ 0,0, **00** 21 **7** 99150043518150082 **4** 7766 0,0, **000 0 ‘** pacle.the@ormartan.borg **e** s@ptar **r** a.cootar **m** b:a.com..00. **.** >aoisizeeoiiai1s227oo 3.8522 9231 sora loses - VAL BETAMET GENT.C —_ MBETGENTTOLNCUO. a«120.000 G —«424482«=SSSSVALBETAMETGENTC.itt-—=—66,00 1789131700910somo ag omestorofarma.combr 2” • ITEC - Varejo = Cadastro também acessa o ERP diretamente para validar, porém não existe ação manual, dado que os campos são preenchidos automaticamente. dec Qa HR Slee SACSON meDIIROS DF SOURA;RAOR Cadastro de produto Heme Cadasiro Froato rs Céoge Desergo Onsergho reuse seats tne 23082 RB xe mesons surcnsecr C **a** ssecaiheun SaorcarceFRA PALIPERS SUPERSEC P-420N arwe oRosAsMn FARMMALIFE rawcxo ROSARIO 20052.48A PAMPERS SUPERSEC P A2UN 22052.59A PAMPERS SUPERSEC P-42UN 20052.5RA PAMPERS SUPERSEC P 42UN 22052. /RA PAMIPERS SUPERSEC P 42UN a chege Onserge Deserghe reaucise 200K) FRA PAUPERS SUPERSEC PUN 5BA PANIPERS SUPERSEC B A2UN 8. teen Feercarte ‘Stucbo 02 proata Meee 487357 PROCTER PERFUnEARIA | Bio ¥ amo . Rexpenuive: peso casas ars caaaere Daca ao un aeeragbo —_<_=_{&=_>_—=E#K[Z&[]E=_TOO une aow awouzen peur (© 2017 mecract - ec Suste GWS, 20187010 lec . Q) Bec sACNSON mMeDEROSDE SOUZA LRIOR ~ « Cécigo Descrigo Describe redurids Seamus zoo Qe pawns surensecr Una Cussstengboaun FapccarceFRA PAMIPERS SUPERSEC P AZUN arwo orocasian FARDUALIE Tavoro ROSARIO 20052.5RA PAMIPERS SUPERSEC P 42UN 2305284 PAMPERS SUPERSEC P 42UN 20052.5RA PAMIPERS SUPERSEC P 42UN 23052.58A PAMPERS SUPERSEC P 420N ‘coerce [Eee Categoria Oegaramerss see nets 278 FRALOA INFANTE BP | Q Bs Ao DEFINIDO censume segneneo ae Mave BCG © who pero | | ex 9 NAO OEFWIOO | | Poe 4 | wwranrn | Q | marca 0 NAOWFORMADO | | Femina 9 NAO IMFORMADO | | Apresentabo 0 NAO DEFIMDO | Q | Equine 12196 pAMPeRs supERSEC 1a | Gp exposeho ies,10111 FRA PAMAPERS SUPERSEC TAME CX CX | | Classiicagbo 0 NAO DEFIDO | Q | © NAO DEFMNCO iQ | 9 NAO OEFINNDO 1 Q | NAO DEFINOO | Q | Responsive peio cadastro Data cadestro Dace ae uiume ameragbo: ——£—_=_—=_=_[_ unxane pevouze peur 5. Etapa apartada de E-commerce https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 10/28 

30/06/2026, 07:39 

PIM Cadastro 

O time de E-commerce também possui um formulário próprio na Cervello para validação dos dados, porém essa etapa não é — impeditiva para o lançamento dado que o produto precisa estar comprado e disponível no estoque físico antes de ser publicado no canal digital, o e-commerce opera em um tempo dissociado do fluxo principal. 

- Os campos "Departamento" e "Categoria" não são preenchidos automaticamente e exigem ação manual do time de e- commerce, dado que a estrutura da árvore mercadológica é diferente entre o ERP e a VTEX; 

- Para medicamento, o campo "Subcategoria" não é preenchido; 

- Os campos de cubagem possuem permissão de edição intermitente, alguns permitem manipulação e outros não; 

- Campos editáveis: 

   - Palavras Similares 

   - Text Link 

   - Meta Tag 

   - Marca 

## Fluxo de manutenção de produtos 

O fluxo de manutenção é, na visão dos times, a maior dor operacional do cenário atual. Diferentemente do fluxo de lançamento, que tem um processo minimamente estruturado via Cervello, a manutenção não conta com uma plataforma centralizada de gestão e opera de forma fragmentada entre diferentes canais, responsabilidades e sistemas. 

A ausência de estrutura no fluxo de manutenção não é um problema periférico. É a razão pela qual inconsistências conhecidas 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

11/28 

30/06/2026, 07:39 

PIM Cadastro 

permanecem nos canais por tempo indeterminado, correções realizadas na origem não chegam à ponta, e os times desenvolvem contornos informais para manter algum nível de controle operacional. 

Para além do retrabalho operacional, cada manutenção não rastreada é uma oportunidade perdida de aprendizado sobre os padrões de falha do processo, bem como cada correção feita fora do sistema oficial é uma inconsistência potencial entre ambientes, e cada produto com dado desatualizado que permanece no catálogo é um risco ativo de impacto ao cliente. Isso torna o fluxo estruturalmente incapaz de garantir a consistência e a confiabilidade do catálogo de produtos nos canais digitais. 

## Origens das solicitações de manutenção 

Não existe um canal único pelo qual as solicitações de manutenção devem obrigatoriamente passar, especialmente quando se trata de erros internos. Na prática, as demandas chegam por uma combinação de caminhos, dependendo de quem identificou o problema e de qual é a sua natureza: 

## Via Cervello 

Idealmente, as solicitações de manutenção deveriam nascer via Cervello, iniciadas pelos próprios fornecedores e seguindo um fluxo estruturado. Na prática, esse caminho é utilizado em uma parcela dos casos, principalmente quando a manutenção envolve dados que o próprio fornecedor precisa atualizar e quando há tempo hábil para percorrer o workflow. A Cervello, por ter sido adaptada como ferramenta de workflow e não concebida para essa função, apresenta limitações que desincentivam seu uso para manutenções mais simples ou urgentes. 

## Via Teams e e-mail 

A maioria das solicitações de manutenção chega por canais informais, mensagens no Microsoft Teams ou e-mails direcionados aos times de Cadastro e E-commerce. Esse é o caminho padrão para erros internos, como um produto que passou incorretamente pelo Regulatório ou uma imagem desatualizada sinalizada pelo time de e-commerce. Não há formulário, não há campo de justificativa obrigatório, não há registro formal da solicitação e não há rastreabilidade sobre o que foi pedido, por quem, quando foi tratado e qual foi o resultado. 

## Via sinalização da indústria 

Quando o fabricante identifica que suas informações estão incorretas ou desatualizadas nos canais digitais, seja por auditoria própria, por comparação com concorrentes ou por reclamação de clientes. A sinalização chega de forma não estruturada para os times internos, geralmente por e-mail ou contato direto com o time comercial, que repassa para Cadastro ou E-commerce. Não há SLA definido, não há priorização formal e a correção depende da urgência, disponibilidade e julgamento do time que recebe a demanda. 

## Via percepção de impacto em indicadores 

Parte das manutenções é identificada de forma reativa pelos próprios times ao monitorar indicadores operacionais, como taxa de cancelamento de pedidos, reclamações, auditorias ou comparação com a concorrência. Nesses casos, o problema já chegou ao cliente antes de ser detectado internamente. A correção começa a partir da percepção do sintoma, sem necessariamente identificar ou eliminar a causa raiz. 

## Cenários típicos de manutenção 

A diversidade de cenários que demandam manutenção é um fator agravante. Não existe um tipo único de manutenção, cada situação tem uma origem diferente, um responsável diferente e um caminho de resolução diferente, o que torna impossível padronizar o processo sem uma plataforma centralizada. 

## Cenário 1 — Atualização de dados pelo fornecedor 

O fornecedor identifica que uma informação sobre seu produto está incorreta ou desatualizada (descrição, embalagem, composição). O time de Cadastro avalia, realiza a correção no ERP e espera que o dado reflita na VTEX. Quando se trata de informações complementares, o time de E-commerce realiza as correções manualmente. Não há registro formal da solicitação nem confirmação estruturada ao solicitante. 

## Cenário 2 — Erro regulatório identificado internamente 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

12/28 

30/06/2026, 07:39 

PIM Cadastro 

Um produto passa pelo Regulatório no fluxo de lançamento com classificação incorreta, marcado como controlado quando não deveria ser, ou vice-versa. O erro é identificado posteriormente por outro time, geralmente E-commerce. A correção chega ao time de Cadastro por Teams ou e-mail, é realizada no ERP e precisa ser verificada manualmente na VTEX. O histórico do erro e da correção não é registrado em nenhum sistema. 

## Cenário 3 — Imagem desatualizada identificada por auditoria 

O time de E-commerce, ao realizar auditoria ou ao comparar os canais com a concorrência, identifica imagens desatualizadas ou incorretas. Dependendo da fonte e da urgência, o time realiza a troca diretamente na VTEX via Shopnext ou outro parceiro de enriquecimento (fora do fluxo oficial). Não há rastreabilidade sobre a origem da imagem anterior, quando foi publicada ou quem a aprovou. 

## Cenário 4 — Troca de EAN 

Um produto recebe novo EAN por alguma mudança significativa em sua característica. O novo EAN é cadastrado no ITEC, mas o EAN anterior não é automaticamente inativado nos canais digitais. Os dois registros passam a coexistir na VTEX com informações potencialmente divergentes, sem que haja visibilidade clara sobre qual é o EAN ativo e qual deveria ser despublicado. 

## Cenário 5 — Produto inativo permanecendo visível nos canais 

Um produto é descontinuado e inativado no ERP. Sem mecanismo de propagação automática, permanece disponível na VTEX. O time de E-commerce só identifica quando por exemplo realiza uma varredura manual do catálogo. Como contorno, o time criou categorias específicas na VTEX ("Produtos Inativos") para tentar manter visibilidade sobre esses itens, solução que existe fora de qualquer sistema oficial e depende de atualização manual. 

## Enriquecimento de produtos 

O enriquecimento de dados de produtos existentes (atualização de descrições, adição de imagens complementares, inclusão de atributos por categoria, etc) não segue um fluxo estruturado e nem um calendário definido. É uma atividade conduzida por prioridade de negócio, sem processo formal e por fora do fluxo de lançamento da Cervello. 

Na prática, o enriquecimento ocorre em resposta a gatilhos externos: urgência de relançamento de um produto, reclamação formal da indústria sobre a qualidade das informações exibidas, lacunas em relação à concorrência, categorias que entram em foco por sazonalidade ou estratégia comercial e entre outros fatores. Fora desses gatilhos, produtos com dados básicos, incompletos ou desatualizados permanecem no catálogo indefinidamente sem que haja mecanismo de identificação ou priorização de enriquecimento. 

## Mapeamento de dores e problemas 

As dores mapeadas ao longo do Discovery evidenciam que os impactos do cenário atual não se restringem a um único time ou processo, pois atravessam áreas, sistemas e canais, com manifestações distintas em cada camada. Os pontos foram categorizados em 3 tipos: Experiência do cliente; Operacionais; Consistência entre sistemas/canais. As imagens a seguir consolidam cada problema identificado com seu detalhamento, resultado, exemplo prático, frequência, criticidade e causa hipotética. 

## Dores e problemas - Experiência do cliente 

## Dores e problemas - Consistência entre sistemas/canais 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

13/28 

30/06/2026, 07:39 

PIM Cadastro 

## Dores e problemas - Operacionais 

## Perspectiva Cadastro 

O time de Cadastro opera no centro do fluxo de dados de produto, sendo ao mesmo tempo responsável pela qualidade das informações e refém das limitações dos sistemas e processos que o cercam. As dores dessa perspectiva têm origem predominantemente em alguns fatores que se retroalimentam: a dependência de fontes externas para garantir a confiabilidade dos dados na entrada, as limitações técnicas de uma plataforma adaptada, a ausência de automação e rastreabilidade nos processos de integração e manutenção. 

O resultado é um time que valida por amostragem o que deveria ser validado por completude, corrige manualmente o que deveria ser automatizado e opera sem visibilidade consolidada sobre o estado real dos dados que gerencia. A soma dessas condições cria um ambiente onde erros são inevitáveis e difíceis de rastrear, e onde a manutenção ocorre fora do controle dos sistemas. 

## Perspectiva E-commerce 

O time de E-commerce é a camada mais próxima do cliente final e, por consequência, o primeiro a sentir e a ter que resolver os impactos das inconsistências geradas. As dores dessa perspectiva se manifestam de 2 formas principais: problemas que chegam ao cliente antes de serem detectados internamente, e problemas operacionais que consomem capacidade do time em correções 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

14/28 

30/06/2026, 07:39 

PIM Cadastro 

manuais e repetitivas que não eliminam a causa raiz. 

A ausência de propagação automática de dados entre os sistemas força intervenções diretas na VTEX que deveriam ser desnecessárias. A falta de governança sobre a árvore mercadológica e o mapeamento de campos gera inconsistências estruturais que se acumulam. O e-commerce opera, em grande parte, contornando as limitações do sistema em vez de se beneficiar dele. 

## Perspectiva Profarma ON 

Os dados básicos do SAP atendem à necessidade operacional do canal, mas a qualidade e atualização das imagens são um ponto crítico. Em eventos de alta demanda, o serviço de imagens já apresentou falhas graves de performance, com registros de até 17 mil acessos simultâneos derrubando o serviço, forçando a desativação temporária das imagens no portal. A visão do canal de distribuição é que o PIM pode oferecer dados mais ricos, desde que não substitua o SAP como fonte estrutural. 

## Cenário Futuro (TO-BE) 

Esta seção apresenta a visão proposta para o funcionamento do PIM Cadastro, construída a partir dos problemas mapeados no Discovery e dos requisitos levantados na especificação inicial. As propostas aqui descritas estão sujeitas à validação dos times envolvidos antes da definição final do escopo de desenvolvimento. 

## Fluxo de lançamento de produtos 

O fluxo de lançamento no TO-BE mantém a Cervello como ponto de entrada e os ERPs como sistemas de origem dos dados estruturais do produto. O PIM não substitui nem replica essa responsabilidade, mas sim atua como destino dos dados complementares que os ERPs não precisam e não devem possuir, e também como camada de distribuição para os canais digitais, substituindo as integrações diretas ERP → canal que hoje operam de forma fragmentada e sujeita a falhas. 

É um ponto central desta arquitetura: os dados estruturais continuam nascendo, sendo validados e mantidos nos ERPs. O PIM recebe esses dados por leitura, os utiliza como referência e os distribui para os canais, mas não os origina e não os sobrescreve. 

## — Etapa 1 Submissão pelo fornecedor (Cervello) 

- Atores: Fornecedor 

- Sistema: Cervello 

O fornecedor acessa a Cervello e inicia o workflow de cadastro, preenchendo os formulários disponíveis. A integração com a Simplus é acionada para verificação do EAN e captura automática de dados enriquecidos quando disponíveis. Quando o produto não existe na Simplus, o preenchimento manual pelo fornecedor continua sendo necessário (ponto que permanece como limitação do fluxo e não é resolvido pelo PIM no primeiro momento). 

## — Etapa 2 Validações internas (Cervello) 

- Atores: Times de Cadastro, Gestão de Categorias e Sell Out 

- Sistema: Cervello 

O produto percorre o workflow de validações internas na Cervello. Cada área valida e complementa as informações dentro de sua alçada, garantindo que os dados estejam consistentes e confiáveis. 

## — Etapa 3 Comitê de decisão de compra (Cervello) 

- Atores: Áreas comerciais envolvidas 

- Sistema: Cervello 

A decisão de compra é deliberada em comitê. Em caso de reprovação, o fluxo é encerrado. Em caso de aprovação, o fluxo avança para as validações finais de Precificação, Fiscal e Regulatório. O time de Regulatório confirma as classificações de retenção de receita e controle para medicamentos. O time de E-commerce realiza sua validação complementar, sem caráter impeditivo para o avanço do fluxo. 

Etapa 4 — Conclusão do cadastro e gatilho de integração (Cervello → ERPs → PIM) 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

15/28 

30/06/2026, 07:39 

PIM Cadastro 

- Ator: Time de Cadastro 

- Sistemas: Cervello, ITEC, SAP, PIM 

O time de Cadastro indica na Cervello que todos os dados foram confirmados. Esse registro dispara duas ações simultâneas e independentes: 

1. Automação de integração com os ERPs (ITEC e SAP), que registram os dados estruturais do produto (códigos, dimensões, classificações regulatórias, status, EANs e demais atributos operacionais). Esses dados continuam sendo de responsabilidade exclusiva dos ERPs. 

2. Envio ao PIM dos dados complementares coletados ao longo do workflow na Cervello (campos que não pertencem ao escopo dos ERPs e que precisam ser mapeados e adicionados à plataforma previamente para que essa transmissão ocorra). O PIM recebe esses dados como ingestão inicial do produto e, em paralelo, realiza leitura dos dados estruturais dos ERPs para compor o registro completo do produto em seu catálogo. 

   - a. OBS: Esta etapa pressupõe um trabalho prévio de mapeamento e configuração dos campos complementares na Cervello, de modo que o workflow passe a coletar essas informações de forma estruturada e transmiti-las ao PIM ao final do processo. 

Gatilho: confirmação do time de Cadastro na Cervello. 

## — Etapa 5 Gate de qualidade (PIM) 

- Ator: PIM (automático) 

- Sistema: PIM 

O PIM aplica o gate de qualidade sobre os dados recebidos, verificando completude e consistência dos campos definidos como obrigatórios para o lançamento do produto. 

Os dados complementares, como descrições longas, metatags, atributos por categoria, imagens não são bloqueantes nesta etapa, salvo definição contrária do negócio para campos ou categorias específicas. Essa decisão reflete o modelo atual, em que o enriquecimento não é impeditivo para o lançamento, e preserva a agilidade do fluxo. 

- Se aprovado: o produto avança para enriquecimento e publicação. 

- Se reprovado: o PIM gera notificação ao time responsável com indicação dos campos pendentes. O produto não é distribuído até que as pendências sejam resolvidas. 

## — Etapa 6 Enriquecimento complementar (PIM) 

- Atores: Time de E-commerce, Time de Cadastro, parceiros externos 

- Sistema: PIM 

Com o produto aprovado no gate de qualidade, o PIM disponibiliza o registro para enriquecimento com atributos complementares: descrições longas, metatags, atributos específicos por categoria de produto, imagens adicionais e demais informações relevantes para a experiência digital. Essa etapa é padrão para todos os produtos, mas não é impeditiva para a publicação inicial. 

O enriquecimento pode ser realizado por duas vias: diretamente no PIM pelos times internos autorizados, ou de forma automatizada por parceiros externos integrados à plataforma. O PIM deve estar preparado para receber contribuições de parceiros de enriquecimento de forma plugável, ou seja, a integração com qualquer parceiro externo deve ser uma capacidade da plataforma, e não uma dependência estrutural. O PIM precisa funcionar plenamente mesmo na ausência de parceiros integrados, com os times internos como única fonte de enriquecimento quando necessário. 

OBS: A integração com parceiros específicos, como Simplus/Syndigo ou outros será avaliada caso a caso, considerando a disponibilidade técnica de cada plataforma para integração direta. 

## Etapa 7 — Publicação nos canais (PIM → canais consumidores) 

- Ator: PIM (automático) 

- Sistemas: VTEX, iFood, Rappi, Profarma ON 

Após a conclusão do enriquecimento e validação final, o PIM orquestra a distribuição dos dados para cada canal consumidor, enviando apenas os atributos definidos como relevantes para cada plataforma. A publicação é registrada em log com data, hora e versão publicada. 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

16/28 

30/06/2026, 07:39 

PIM Cadastro 

## Fluxo de manutenção de produtos 

No TO-BE, o PIM passa a ser o canal único e oficial de manutenção de dados de produto para os canais digitais. Toda solicitação de manutenção é registrada, rastreada e propagada pelo PIM, eliminando o modelo atual baseado em canais informais sem governança. 

## Canais de entrada de manutenção 

## Canal 1 — Fornecedor via Cervello 

Manutenções originadas pelo fornecedor continuam sendo submetidas via Cervello, seguindo o fluxo estruturado existente. Ao final do processo na Cervello, os dados atualizados são enviados ao PIM, que valida e propaga as alterações para os canais afetados. 

## Canal 2 — Time interno via interface do PIM 

Times internos (Cadastro, E-commerce, Regulatório, entre outros) podem submeter solicitações de manutenção diretamente na interface do PIM, informando dados como o campo a ser alterado, o novo valor e a justificativa. Esse canal substitui as comunicações informais via Teams e e-mail, garantindo rastreabilidade desde o momento da solicitação. 

## Canal 3 — Integração automática com parceiros de enriquecimento 

O PIM deve estar preparado para receber atualizações automáticas de parceiros externos integrados, quando esses parceiros identificam mudanças em atributos ou imagens de produtos já cadastrados. O PIM recebe a atualização, aplica as regras de validação e, se aprovada, propaga para os canais afetados sem necessidade de intervenção manual. A disponibilidade desse canal está condicionada à existência de integração ativa com ao menos um parceiro. O PIM deve operar normalmente na ausência de parceiros integrados, sem que isso comprometa os demais canais de entrada. 

## Canal 4 — Alerta automático do PIM 

O PIM monitora continuamente os dados recebidos dos sistemas de origem e aciona alertas automáticos quando identifica mudanças relevantes, como a inativação de um produto no ERP, a troca de EAN ou a alteração de uma classificação regulatória. O alerta é registrado como uma solicitação de manutenção e encaminhado ao time responsável para validação e ação. 

## Fluxo de aprovação por tipo de campo 

Nem toda manutenção exige o mesmo nível de aprovação. A proposta é que o PIM suporte a configuração de regras de aprovação por tipo de campo: 

- Campos de aprovação direta —alterações em atributos complementares de baixo risco (como descrição longa ou metatag) podem ser aplicadas diretamente pelo time responsável sem etapa adicional de aprovação. 

- Campos com workflow de aprovação — alterações em campos estruturais ou regulatórios (como classificação Anvisa, tipo de receita ou EAN) exigem aprovação de uma área específica antes de serem aplicadas e propagadas. 

- Campos somente leitura no PIM — campos cujo sistema master é o ERP não podem ser alterados diretamente no PIM. Alterações nesses campos precisam ser realizadas na origem e serão refletidas no PIM via integração. 

## Mecanismo de propagação para canais 

Após a aprovação da manutenção, automática ou via workflow, o PIM identifica quais canais são impactados pela alteração e propaga o dado atualizado exclusivamente para esses canais, sem necessidade de republicação completa do produto. A propagação é registrada em log com identificação do campo alterado, valor anterior, novo valor, responsável pela alteração e canais impactados. 

## Gestão de Imagens 

No TO-BE, o PIM passa a ser o repositório central de imagens de produto, eliminando a gestão descentralizada e manual que caracteriza o cenário atual. 

## PIM como repositório central de imagens 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

17/28 

30/06/2026, 07:39 

PIM Cadastro 

Todas as imagens de produto serão armazenadas e gerenciadas no PIM. O PIM suportará múltiplas imagens por produto, com associação por tipo (imagem principal, imagens complementares, imagem de embalagem, entre outros) e por canal de destino, garantindo que cada plataforma receba as imagens adequadas ao seu formato e requisitos técnicos. 

## Política de prioridade de fonte por categoria 

O PIM suportará a configuração de uma política de prioridade de fonte de imagem por categoria de produto, definindo qual fonte deve ser consultada primeiro e qual é a ordem de fallback quando a fonte prioritária não possui imagem disponível ou atualizada. Essa política elimina a decisão manual e ad hoc que ocorre hoje, garantindo consistência e rastreabilidade sobre qual imagem é exibida em cada canal. 

A definição da política é uma decisão de negócio que precisa ser construída e validada pelos times de E-commerce e Cadastro antes da configuração do PIM. 

OBS: O PIM não deve assumir que os parceiros atualmente utilizados pelo time de e-commerce estarão disponíveis para integração direta. Plataformas como Placeholder e Intellibrand são utilizadas hoje de forma manual, sem integração técnica estabelecida, e não se sabe se oferecem APIs ou mecanismos compatíveis com uma integração automatizada. O PIM deve ser resiliente quanto às fontes disponíveis, sendo capaz de operar com qualquer combinação de parceiros integrados, com upload manual como alternativa sempre disponível, e sem dependência estrutural de nenhum parceiro específico para seu funcionamento. 

## Atualização e versionamento de imagens 

Toda substituição de imagem gera uma nova versão no PIM, com registro da fonte, data de recebimento e responsável pela aprovação. O histórico de imagens anteriores é mantido, permitindo rollback quando necessário. Quando uma atualização de imagem é recebida de um parceiro integrado, o PIM notifica o time responsável para validação antes da publicação nos canais, eliminando o risco atual de imagens desatualizadas serem propagadas automaticamente sem revisão. 

## Propagação de imagens para os canais 

Após validação, o PIM distribui as imagens para cada canal conforme as regras de associação definidas, respeitando os requisitos técnicos de cada plataforma (formato, resolução, quantidade máxima de imagens, entre outros). A propagação é registrada em log, garantindo rastreabilidade sobre qual imagem está sendo exibida em cada canal e quando foi publicada. 

## Decomposição Funcional do PIM 

Esta seção apresenta a decomposição funcional do PIM Cadastro em módulos, derivada diretamente dos requisitos levantados e da visão TO-BE. Cada módulo representa um domínio funcional coeso, com responsabilidades bem delimitadas e interfaces definidas com os demais, estrutura que serve de base para a definição de escopo, arquitetura da solução, roadmap e backlog. 

## Visão Geral dos Módulos 

O produto é composto por oito módulos funcionais. A tabela abaixo apresenta cada módulo e sua responsabilidade central: 

**==> picture [454 x 161] intentionally omitted <==**

**----- Start of picture text -----**<br>
Módulo Responsabilidade central<br>1 M1 — Catálogo de Produtos Repositório central e único dos dados de produto<br>2 M2 — Ingestão e Integração Recepção e consolidação de dados de sistemas externos<br>M3 — Governança e Qualidade Validação, regras de negócio e controle de qualidade<br>3<br>dos dados<br>4 M4 — Enriquecimento de Conteúdo Gestão de atributos complementares e imagens<br>**----- End of picture text -----**<br>


https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

18/28 

30/06/2026, 07:39 

PIM Cadastro 

**==> picture [454 x 118] intentionally omitted <==**

**----- Start of picture text -----**<br>
5 M5 — Ciclo de Vida do Produto Controle de estados, versionamento e rastreabilidade<br>M6 — Distribuição por Canal Publicação e propagação de dados para sistemas<br>6<br>consumidores<br>7 M7 — Manutenção e Solicitações Gestão centralizada de solicitações de alteração<br>8 M8 — Administração e Configuração Configurações sistêmicas, acessos e parametrizações<br>**----- End of picture text -----**<br>


## M1 — Catálogo de Produtos 

O Catálogo é o coração do PIM. Todo dado ingerido, enriquecido e distribuído parte dele. É o repositório central e único que elimina a fragmentação atual entre ITEC, SAP e fontes externas, oferecendo um ponto único de consulta e gestão para os dados de produto. 

## Registro de produto 

- Manter registro único por produto identificado pelo EAN como chave primária 

- Suportar múltiplos EANs por produto com indicação de EAN principal e EANs secundários 

- Associar código d1000 (ITEC) e código de distribuição (SAP) ao mesmo registro, evitando duplicidade entre contextos 

- Permitir que um produto exista em um ou ambos os contextos (varejo e/ou distribuição) sem duplicação de registro 

## Modelo de dados por contexto 

- Suportar atributos com valores distintos por contexto de negócio (varejo vs. distribuição) no mesmo registro de produto 

- Garantir que variações de atributos por contexto não representem duplicidade de registros, mas adequações do mesmo produto 

- Exemplos de atributos com variação por contexto: dimensões (unidade para varejo, embalagem logística para distribuição), descrições e códigos de fornecedor 

## Modelo de atributos por categoria 

- Suportar a configuração de conjuntos de atributos obrigatórios e opcionais por categoria de produto 

- Permitir que categorias distintas exijam campos diferentes — medicamentos com princípio ativo, tipo de receita e classificação Anvisa; dermocosméticos com tipo de pele; fraldas com faixa de peso, etc. 

- Garantir que o modelo de atributos por categoria seja extensível sem necessidade de alteração estrutural do sistema 

## Dados estruturais (origem ERP) 

- Armazenar e exibir todos os campos originados do ITEC e SAP 

- Campos somente leitura no PIM quando o sistema master é o ERP — alterações só são aceitas via integração com o sistema de origem 

- Sinalizar visualmente ao usuário quais campos são de origem ERP e não editáveis diretamente no PIM 

## Dados complementares (origem PIM) 

- Armazenar e permitir edição de atributos complementares gerenciados exclusivamente pelo PIM: descrição longa para canal digital, metatags/SEO, atributos por categoria, indicação, contraindicação e demais campos não presentes nos ERPs 

- Esses campos são editáveis diretamente no PIM pelos times autorizados 

## Árvore mercadológica 

- Manter a árvore mercadológica oficial (departamento, categoria, subcategoria) como entidade gerenciada pelo PIM 

- Associar cada produto a um nó da árvore mercadológica 

- Manter mapeamento entre a árvore d1000 e a estrutura de categorias de cada canal consumidor, permitindo tradução automática da categoria do produto para o formato esperado por cada plataforma 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

19/28 

30/06/2026, 07:39 

PIM Cadastro 

• Sinalizar produtos sem categoria mapeada para o canal de destino antes da publicação 

## M2 — Ingestão e Integração 

Este módulo é a porta de entrada do PIM. Sua responsabilidade é receber dados dos sistemas de origem e parceiros externos, consolidá-los no catálogo respeitando as regras de sistema master, e expor interfaces de integração para os sistemas consumidores. A fragmentação atual entre ITEC, SAP, Cervello e parceiros externos sem uma camada de integração centralizada é a causa raiz da maioria das inconsistências mapeadas. 

## Integração com ITEC 

- Receber dados cadastrais do varejo (d1000) via integração automatizada (API ou mensageria) 

- Processar atualizações incrementais (delta): apenas campos alterados desde a última sincronização 

- Detectar e registrar divergências entre o dado recebido do ITEC e o dado atualmente armazenado no PIM 

- Suportar reprocessamento manual de uma ingestão específica em caso de falha 

## Integração com SAP 

- Receber dados cadastrais da distribuição (Profarma) via integração automatizada 

- Processar atualizações incrementais com as mesmas capacidades da integração ITEC 

- Tratar variações de atributos específicas do contexto de distribuição (ex: embalagem logística) 

## Integração com Cervello 

- Receber dados complementares coletados ao longo do workflow de cadastro ao final do processo na Cervello 

- Mapear os campos recebidos da Cervello para o modelo de dados do PIM 

- Registrar log de cada ingestão proveniente da Cervello com identificação do workflow de origem 

## Integração com parceiros 

- Suportar integração plugável com parceiros externos de enriquecimento de dados e imagens, sem dependência estrutural de nenhum parceiro específico 

- Aplicar política de sistema master por campo: dados de parceiros não sobrescrevem campos cujo master é o ERP ou o PIM sem validação prévia 

- Registrar a fonte de cada atributo recebido via parceiro 

- O PIM deve operar plenamente mesmo na ausência de qualquer parceiro integrado 

## Integração com sistemas consumidores 

- Expor APIs padronizadas para consumo dos dados de produto pelos sistemas consumidores (VTEX, iFood, Rappi, Profarma ON) 

- Suportar modelo de push (PIM envia dados ao canal quando há atualização) e pull (canal consulta o PIM sob demanda) 

- Garantir que cada sistema consumidor acesse apenas os atributos definidos para sua operação via controle de escopo por canal 

- Suportar integração via mensageria para sistemas que demandem esse modelo de comunicação 

## Monitoramento de integrações 

- Exibir painel de status das integrações ativas com indicação de última execução, volume processado e status (sucesso, erro, parcial) 

- Gerar alertas automáticos em caso de falha de integração ou ausência de dados esperados dentro de uma janela de tempo configurável 

- Registrar log detalhado de cada execução de integração, incluindo erros, campos ignorados e registros não processados 

- Permitir reprocessamento manual de integrações com falha sem necessidade de intervenção técnica para casos operacionais 

## M3 — Governança e Qualidade 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

20/28 

30/06/2026, 07:39 

PIM Cadastro 

Este módulo é o mecanismo que garante que o PIM cumpra sua promessa de fonte oficial confiável. A ausência de uma camada de validação centralizada é a razão pela qual dados incorretos chegam hoje aos canais digitais e ao cliente final. 

## Gate de qualidade na ingestão 

- Aplicar verificação automática de completude dos campos obrigatórios a cada ingestão recebida 

- Aplicar verificação de consistência entre campos relacionados (ex: Produto Controlado = SIM deve ser consistente com Tipo de Receita e Controle SNGPC) 

- Bloquear a distribuição de produtos que não atingirem o critério mínimo de qualidade configurado 

- Gerar notificação automática ao time responsável com indicação dos campos pendentes ou inconsistentes 

- Permitir configuração do percentual mínimo de completude por contexto (varejo, distribuição) e por categoria de produto 

## Regras de validação por campo 

- Suportar configuração de regras de validação por campo: tipo de dado, formato, valores permitidos, obrigatoriedade condicional e consistência com outros campos 

- Aplicar regras de validação tanto na ingestão automática quanto na edição manual de campos no PIM 

- Exibir mensagem de erro descritiva ao usuário quando uma regra de validação é violada, indicando o campo e o critério não atendido 

- Permitir criação e manutenção de regras de validação sem necessidade de desenvolvimento 

## Validação regulatória 

- Aplicar regras de consistência específicas para campos regulatórios farmacêuticos: Classificação Anvisa, Tipo de Receita, Produto Controlado, Controle SNGPC, Antibiótico, Registro MS 

- Identificar e sinalizar automaticamente inconsistências regulatórias antes da publicação 

- Registrar em log toda alteração em campos regulatórios com identificação do responsável e justificativa 

## Gestão de alertas e pendências 

- Centralizar todas as pendências de qualidade em um painel único, com filtros por produto, campo, tipo de inconsistência, responsável e status de resolução 

- Permitir atribuição de pendências a times ou usuários específicos 

- Registrar histórico de tratamento de cada pendência: quem recebeu, quando resolveu e qual ação foi tomada 

- Gerar relatórios de qualidade com indicadores de completude, taxa de inconsistências e tempo médio de resolução por tipo de pendência 

## Governança da árvore mercadológica 

- Controlar a criação de novos nós na árvore mercadológica mediante aprovação de usuário autorizado 

- Impedir a criação de nós duplicados ou inconsistentes com a estrutura existente 

- Validar o match entre categorias d1000 e estruturas dos canais consumidores antes de permitir a publicação de produtos naquela categoria 

- Exibir alerta quando um produto é associado a uma categoria sem match configurado para o canal de destino 

## M4 — Enriquecimento de Conteúdo 

Este módulo cria a capacidade de realizar a gestão estruturada de dados complementares de produto e de imagens como repositório central e oficial. É onde o PIM transforma dados básicos em informação rica para a experiência digital. 

## Gestão de atributos complementares 

- Permitir criação e edição de atributos complementares diretamente no PIM por usuários autorizados: descrição longa, metatags, SEO, indicação, contraindicação, atributos específicos por categoria 

- Suportar edição em massa de atributos complementares para múltiplos produtos simultaneamente 

- Registrar log de todas as alterações em atributos complementares com identificação do responsável e versão anterior 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

21/28 

30/06/2026, 07:39 

PIM Cadastro 

## Repositório central de imagens 

- Armazenar imagens de produto com suporte a múltiplas imagens por produto, tipadas por função: imagem principal, imagens complementares, imagem de embalagem, imagem de detalhe 

- Associar imagens a contextos e canais específicos, permitindo que um produto tenha imagens distintas por canal de destino quando necessário 

- Suportar upload manual de imagens pelos times internos com validação de formato, resolução e tamanho conforme requisitos dos canais consumidores 

- Manter histórico de todas as versões de imagem com possibilidade de rollback para versão anterior 

## Política de prioridade de fonte de imagem 

- Permitir configuração de política de prioridade de fonte de imagem por categoria de produto, definindo ordem de preferência entre as fontes disponíveis e regras de fallback 

- Aplicar automaticamente a política configurada na seleção da imagem a ser distribuída para cada canal 

- Sinalizar quando nenhuma fonte disponível possui imagem para um produto, gerando pendência para resolução manual 

- A política deve ser resiliente à ausência de qualquer fonte específica: o PIM deve operar normalmente com qualquer combinação de fontes disponíveis, incluindo o cenário em que o upload manual é a única fonte ativa 

## Recebimento e validação de imagens de parceiros 

- Receber automaticamente atualizações de imagem provenientes de parceiros externos integrados 

- Notificar o time responsável quando uma nova imagem é recebida de parceiro, antes de publicá-la nos canais 

- Aplicar validações técnicas automáticas na imagem recebida (formato, resolução mínima, tamanho máximo) antes de disponibilizá-la para distribuição 

- Registrar a fonte e a data de recebimento de cada imagem 

## M5 — Ciclo de Vida do Produto 

A ausência de controle de ciclo de vida é a causa direta de produtos inativos visíveis nos canais, EANs desatualizados em circulação e ausência de rastreabilidade sobre o que foi alterado, quando e por quem. Este módulo endereça essas dores de forma estrutural, garantindo que qualquer mudança no estado de um produto seja detectada, registrada e propagada. 

## Máquina de estados do produto 

- Controlar os estados possíveis de um produto no PIM: em enriquecimento, pendente de aprovação, aprovado, publicado, atualização em andamento, inativo 

- Garantir que transições de estado só ocorram quando as condições configuradas forem atendidas (ex: produto só avança para publicado após aprovação no gate de qualidade) 

- Registrar cada transição de estado com identificação do responsável, data e evento que a disparou 

## Propagação de inativação 

- Detectar automaticamente a inativação de um produto no sistema de origem (ITEC ou SAP) 

- Propagar imediatamente o status de inativação para todos os canais consumidores onde o produto está publicado 

- Registrar em log a inativação com identificação da origem, data e canais notificados 

- Gerar alerta para o time responsável quando uma inativação é detectada e propagada 

## Versionamento de dados 

- Gerar automaticamente uma nova versão do registro do produto a cada alteração confirmada em qualquer campo 

- Manter histórico integral de versões com identificação de quais campos foram alterados em cada versão 

- Permitir consulta ao estado de qualquer campo em qualquer versão anterior do produto 

- Exibir comparativo entre versões para facilitar a auditoria de alterações 

## Rollback 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

22/28 

30/06/2026, 07:39 

PIM Cadastro 

- Permitir a restauração de uma versão anterior do produto, completa ou parcial por campo 

- Exigir justificativa para execução de rollback, registrada no log do produto 

- Aplicar as mesmas validações de qualidade e consistência na versão restaurada antes de republicá-la nos canais 

- Restringir a execução de rollback a usuários com perfil autorizado 

## Log de auditoria 

- Registrar toda ação realizada sobre um produto: ingestão, edição, aprovação, publicação, inativação, rollback e atribuição de responsável 

- Cada registro de log deve conter: campo alterado, valor anterior, novo valor, usuário responsável, sistema de origem quando automático, data e hora 

- Permitir consulta ao log completo de um produto com filtros por período, tipo de ação e usuário 

- Garantir imutabilidade do log, os registros não podem ser editados ou excluídos 

## M6 — Distribuição por Canal 

Este módulo centraliza a publicação e atualização dos dados de produto nos sistemas consumidores, substituindo as integrações diretas e fragmentadas que existem hoje. Com ele, qualquer canal recebe dados consistentes, atualizados e no formato correto, com rastreabilidade completa sobre o que foi enviado, quando e com qual resultado. 

## Configuração de canais consumidores 

- Manter cadastro de canais consumidores com suas configurações específicas: nome, tipo de integração (API/mensageria), atributos aceitos, formato de dados esperado e regras de publicação 

- Permitir adição de novos canais consumidores sem necessidade de alteração na arquitetura dos demais módulos 

- Suportar ativação e desativação de canais sem impacto nos demais 

## Regras de atributos por canal 

- Configurar quais atributos são enviados para cada canal consumidor, garantindo que cada plataforma receba apenas os dados relevantes para sua operação 

- Suportar mapeamento de nomes de campos entre o modelo de dados do PIM e o modelo esperado por cada canal 

- Permitir configuração de transformações simples de dados por canal (ex: formatação de texto, conversão de unidades) 

## Publicação inicial 

- Orquestrar a publicação de um novo produto em todos os canais configurados após aprovação no gate de qualidade 

- Registrar o resultado da publicação por canal com status (sucesso, erro, parcial) e detalhamento de eventuais falhas 

- Gerar alerta em caso de falha de publicação em qualquer canal, com indicação do canal e do erro 

## Propagação de atualizações 

- Detectar alterações em campos de um produto e identificar automaticamente quais canais são impactados por aquela alteração 

- Propagar a atualização exclusivamente para os canais afetados, sem necessidade de republicação completa do produto 

- Registrar log de propagação com identificação dos campos alterados, canais notificados, data e resultado 

## Controle de publicação por canal 

- Permitir publicação seletiva por canal: um produto pode estar publicado em determinados canais e não em outros 

- Suportar agendamento de publicação para data e hora específicas 

- Permitir despublicação de um produto em um canal específico sem afetar os demais 

- Registrar histórico de publicações e despublicações por canal 

## Painel de status de distribuição 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

23/28 

30/06/2026, 07:39 

PIM Cadastro 

- Exibir status de publicação de cada produto por canal: publicado, pendente, com erro, inativo 

- Permitir filtros por canal, status, categoria e período de publicação 

- Exibir data e versão da última publicação bem-sucedida por canal para cada produto 

- Permitir reenvio manual de um produto para um canal específico em caso de falha 

## M7 — Manutenção e Solicitações 

O fluxo de manutenção é a maior dor operacional identificada. Este módulo transforma um processo hoje fragmentado, informal e sem rastreabilidade em um canal único, governado e auditável. 

## Central de solicitações de manutenção 

- Centralizar em um único painel todas as solicitações de manutenção (interface PIM, parceiro externo ou alerta automático) 

- Exibir para cada solicitação: produto afetado, campo(s) a alterar, valor atual, valor proposto, solicitante, canal de entrada, status e histórico de tratamento 

- Permitir filtros por produto, campo, solicitante, status e período 

## Criação de solicitação via interface PIM 

- Permitir que times internos autorizados criem solicitações de manutenção diretamente na interface do PIM 

- Exigir preenchimento obrigatório de: campo a alterar, novo valor proposto e justificativa 

- Registrar automaticamente solicitante, data e hora de criação 

## Aplicação e propagação da manutenção 

- Após aprovação, aplicar a alteração no registro do produto no PIM gerando nova versão 

- Identificar automaticamente os canais consumidores impactados pela alteração 

- Propagar a atualização para os canais afetados via módulo de distribuição 

- Registrar resultado da propagação por canal com status e detalhamento de eventuais falhas 

## Notificações e comunicação 

- Notificar o solicitante sobre mudanças de status da sua solicitação: recebida, em aprovação, aprovada, rejeitada, aplicada 

- Notificar o aprovador quando uma solicitação aguarda sua análise 

- Notificar o time responsável quando um alerta automático gera uma solicitação de manutenção 

- Suportar configuração de destinatários de notificação por tipo de campo e por canal 

## M8 — Administração e Configuração 

Este módulo garante que o PIM possa ser operado e evoluído pelas áreas responsáveis com mínima dependência de TI para operações rotineiras. 

## Gestão de usuários e perfis de acesso 

- Manter cadastro de usuários com autenticação integrada ao diretório corporativo 

- Suportar perfis de acesso configuráveis com granularidade por módulo, funcionalidade e conjunto de dados 

- Suportar perfis específicos por contexto: usuário com acesso apenas ao contexto varejo, apenas distribuição, ou ambos 

- Registrar log de acesso e ações realizadas por usuário 

## Configuração do modelo de dados 

- Permitir criação, edição e desativação de atributos no modelo de dados sem necessidade de desenvolvimento 

- Configurar obrigatoriedade, tipo de dado, formato, valores permitidos e visibilidade por perfil para cada atributo 

- Configurar conjuntos de atributos obrigatórios e opcionais por categoria de produto 

- Garantir que alterações no modelo de dados não corrompam dados já existentes 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 24/28 

30/06/2026, 07:39 

PIM Cadastro 

## Configuração de regras de negócio e validação 

- Permitir criação e manutenção de regras de validação por campo sem necessidade de desenvolvimento 

- Configurar critérios do gate de qualidade: percentual mínimo de completude, campos críticos e comportamento em caso de reprovação 

- Configurar regras de consistência entre campos 

- Configurar fluxos de aprovação por campo para o módulo de manutenção 

## Configuração de integrações 

- Manter configuração de cada integração: sistema de origem/destino, tipo de conexão, frequência de execução, mapeamento de campos e regras de consolidação 

- Permitir ativação, desativação e ajuste de integrações sem impacto nos demais módulos 

- Suportar configuração de sistema master por campo diretamente na interface administrativa 

## Configuração de canais e regras de distribuição 

- Manter configuração de cada canal consumidor e suas regras de atributos 

- Permitir configuração da política de prioridade de fonte de imagem por categoria 

- Configurar mapeamento entre árvore mercadológica d1000 e estruturas de categoria dos canais consumidores 

## Monitoramento operacional 

- Exibir painel consolidado de saúde do sistema: status das integrações, volume de produtos por estado, pendências de qualidade, falhas de distribuição e alertas ativos 

- Permitir configuração de alertas operacionais com definição de destinatários, condições de disparo e canal de notificação 

- Exibir indicadores operacionais: SLA de processamento de ingestão, taxa de sucesso de distribuição, volume de manutenções por período e tempo médio de resolução de pendências 

## Dependências e riscos 

O sucesso da implementação do PIM Cadastro está diretamente condicionado ao atendimento de um conjunto de dependências externas ao produto e à mitigação de riscos identificados. Esta seção consolida esses pontos com o objetivo de orientar o planejamento, antecipar bloqueios e estabelecer responsabilidades claras antes do início do desenvolvimento ou da implantação da solução. 

## Dependências 

## 1. Integração Cervello → ERPs 

A integração que hoje já apresenta falhas, com campos chegando incompletos ou incorretos aos ERPs após a conclusão do workflow, e é essa mesma integração que irá alimentar o PIM. Dessa forma, o PIM poderá receber dados com as mesmas inconsistências que existem hoje e as distribuirá para todos os canais. 

## 2. Qualidade dos dados de origem nos ERPs (ITEC e SAP) 

Os ERPs carregam um histórico de dados inconsistentes acumulados ao longo do tempo. O PIM ingerirá esses dados como base do catálogo central e os distribuirá para os canais. Sendo assim, a confiabilidade dos dados do PIM depende diretamente da consistência das informações nas origens. 

## 3. Mapeamento e adição dos campos complementares na Cervello 

Para que o fluxo TO-BE funcione conforme proposto com o PIM recebendo dados complementares diretamente da Cervello ao final do workflow de cadastro, esses campos precisam existir na plataforma previamente. Hoje a Cervello não coleta a maioria dos atributos complementares que o PIM precisará gerenciar. 

https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

25/28 

30/06/2026, 07:39 

PIM Cadastro 

Esse mapeamento e a adição dos campos na Cervello são trabalhos que precisam ocorrer antes da integração Cervello → PIM ser ativada, e dependem de decisão e execução das áreas responsáveis pela plataforma. 

## 4. Governança da árvore mercadológica 

É necessário um trabalho de revisão e validação da árvore atual, com definição da estrutura oficial e do match com a VTEX, antes que o PIM comece a distribuí-la. Essa é uma decisão de negócio que requer envolvimento ativo das áreas de Cadastro e E- commerce. 

## 5. Alinhamento organizacional do processo de manutenção 

O PIM será o canal único e oficial de manutenção de dados de produto para os canais digitais. Para que essa transição ocorra de forma efetiva, o processo precisa estar acordado entre as áreas antes do go-live. Sem esse alinhamento organizacional, os canais informais continuarão sendo utilizados em paralelo ao PIM, esvaziando a governança que o sistema se propõe a criar. 

## 6. Avaliação de viabilidade de integração com parceiros de enriquecimento 

Os parceiros atualmente utilizados pelo time de e-commerce (Simplus/Syndigo, Shopnext, Placeholder e Intellibrand) são operados de forma predominantemente manual, sem integração técnica estabelecida com os sistemas internos. Não se sabe, no momento, quais desses parceiros disponibilizam APIs ou mecanismos compatíveis com uma integração automatizada com o PIM. 

Essa avaliação precisa ocorrer antes da definição do escopo final de integrações do produto. 

## Riscos 

**==> picture [467 x 437] intentionally omitted <==**

**----- Start of picture text -----**<br>
Risco Descrição Impacto Probabilidade<br>Dados inconsistentes herdados  Dados incorretos acumulados nos ERPs são  Alto Alta<br>1 dos ERPs ingeridos pelo PIM e distribuídos em escala<br>para os canais<br>Instabilidade da integração  PIM recebe dados com as mesmas falhas  Alto Alta<br>2 Cervello → ERPs  atuais, comprometendo a confiabilidade<br>desde o início<br>Falta de definição de sistema  Conflitos de sobrescrita entre fontes geram  Alto Média<br>3 master por campo inconsistências no catálogo central e perda<br>de confiança no PIM<br>Baixa adesão das áreas ao novo  Times continuam utilizando canais informais  Alto Alta<br>4<br>processo de manutenção em paralelo ao PIM, esvaziando a governança<br>Complexidade das integrações  Integrações com ITEC, SAP e Cervello  Alto Média<br>5 com sistemas legados demandam mais esforço do que o estimado,<br>gerando atrasos<br>Parceiros de enriquecimento  Integrações planejadas com parceiros  Médio Média<br>sem API disponível externos não são tecnicamente viáveis,<br>6<br>reduzindo o escopo de enriquecimento<br>automático<br>Árvore mercadológica não Categorias inconsistentes distribuídas pelo  Alto Alta<br>7 revisada PIM para todos os canais simultaneamente,<br>ampliando o problema atual<br>**----- End of picture text -----**<br>


https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

26/28 

30/06/2026, 07:39 

PIM Cadastro 

**==> picture [467 x 174] intentionally omitted <==**

**----- Start of picture text -----**<br>
Escopo crescente durante o  Pressão das áreas para incluir  Médio Alta<br>8 desenvolvimento funcionalidades além do escopo definido,<br>comprometendo prazo e qualidade<br>Ausência de engajamento  Decisões de negócio necessárias ao longo do  Alto Média<br>9 contínuo das áreas de negócio projeto não são tomadas em tempo hábil,<br>gerando bloqueios<br>Expectativas desalinhadas  Áreas esperam que o PIM resolva problemas  Médio Alta<br>sobre o que o PIM resolve que estão fora do seu escopo (ex: falhas na<br>10<br>Cervello, qualidade dos dados nos ERPs),<br>gerando frustração<br>**----- End of picture text -----**<br>


A maioria das dependências e riscos identificados tem origem em problemas preexistentes no ecossistema atual , portanto não são criados pelo PIM, mas precisam ser endereçados para que o PIM entregue seu valor. Isso reforça um ponto central do Discovery: o PIM é uma condição necessária, mas não suficiente, para resolver os problemas mapeados. Sua implementação precisa ser acompanhada de iniciativas paralelas de estabilização de integrações, higienização de dados, governança de processos e alinhamento organizacional. 

## Direcionamento: Aquisição ou Internalização 

Syndigo PIM 

- 

Akeneo 

- 

- 

Stibo Systems 

inRiver 

Informatica (Salesforce) 

- 

- 

- 

## Próximos Passos 

O período de aprofundamento entregou clareza sobre o problema, sobre o que o PIM precisa fazer e sobre as condições necessárias para que funcione. Sendo assim, o próximo passo é transformar essa clareza em decisão e execução. Esta seção consolida as ações necessárias e as decisões que ainda dependem da liderança e das áreas de negócio. 

**==> picture [455 x 92] intentionally omitted <==**

**----- Start of picture text -----**<br>
Ação Responsável Critério de conclusão<br>Validar a proposta de TO-BE: fluxos de  E-commerce + Cadastro Times validam ou solicitam ajustes formais<br>1<br>lançamento e manutenção nos fluxos propostos<br>**----- End of picture text -----**<br>


https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 

27/28 

**==> picture [498 x 360] intentionally omitted <==**

**----- Start of picture text -----**<br>
30/06/2026, 07:39 PIM Cadastro<br>Validar a decomposição funcional do  E-commerce + Cadastro Áreas confirmam aderência dos módulos e<br>2<br>produto (funcionalidades e módulos) funcionalidades às suas necessidades<br>Definir o MVP: quais módulos,  E-commerce + Cadastro Escopo de MVP documentado e aprovado<br>3 funcionalidades e canais do Varejo  pelos aprovadores do projeto<br>compõem o primeiro ciclo de entrega<br>Realizar trabalho de saneamento e  E-commerce + Cadastro Árvore mercadológica revisada e validada,<br>4 validação da árvore mercadológica  com mapeamento (de-para) de categorias<br>visando o match com a VTEX (de-para) para VTEX aprovado<br>Avaliar viabilidade técnica de  TI Digital Confirmação da viabilidade com parceiros,<br>integração com parceiros de  considerando esforço de integração<br>5<br>enriquecimento (Shopnext,<br>Placeholder, Intellibrand)<br>Endereçamento da estruturação de  TI Digital Recursos, capacidades e prazos de<br>6<br>squad conforme caminho escolhido mobilização definidos<br>Levantamento de campos necessários  E-commerce Relação de campos por categoria de<br>7<br>por categoria específica produto disponibilizada aos times envolvidos<br>Mapear e adicionar os campos  Cadastro + Cervello Campos complementares mapeados e<br>8 complementares necessários na  implementados na Cervello, prontos para o<br>Cervello fluxo de ingestão<br>**----- End of picture text -----**<br>


https://loop.cloud.microsoft/print/eyJwIjp7InUiOiJodHRwczovL3Byb2Zhcm1hcmouc2hhcmVwb2ludC5jb20vY29udGVudHN0b3JhZ2UvQ1NQXz… 28/28 

