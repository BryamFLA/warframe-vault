---
title: Warframe — Segunda Mente
aliases: [Warframe — Segunda Mente, Warframe  Segunda  Mente]
tipo: home
resumo: Todos os Warframes Prime são obtidos via Relíquias do Void em missões de Fissura.
status: completo
rag: true
tags: [home, index, warframe, guia-ia, agente]
atualizado: 2026-10-07
agente: opus
jogo: Warframe
produtora: Digital Extremes
distribuidora: Digital Extremes
plataformas: [PC, PlayStation 4, PlayStation 5, Xbox One, Xbox Series X/S, Nintendo Switch]
modelo: free-to-play
genero: [third-person shooter, action RPG, looter shooter]
lancamento: 2013-03-25
modo: multiplayer cooperativo (1–4 jogadores)
motor: Evolution Engine
site: "https://www.warframe.com"
wiki: "https://wiki.warframe.com"
idioma: pt-BR
arquivo_raiz: true
autossuficiente: true
descricao: "Arquivo único de apresentação e consulta do vault Warframe — Segunda Mente. Contém a visão geral do projeto, o protocolo operacional para agentes de IA e o dump consolidado de todo o conteúdo do vault."
---

# 🧠 Warframe — Segunda Mente

> [!quote]
> *"O Tenno não esquece. O Tenno organiza."*


## ⚡ Leia primeiro — Warframe — Segunda Mente


Este é o **arquivo raiz e autossuficiente** do vault *Warframe — Segunda Mente*: uma wiki pessoal de Warframe em Obsidian, escrita em Português do Brasil, projetada para ser consultada tanto por humanos quanto por agentes de IA.

Ele reúne, em um só documento, as três camadas do projeto:

| Parte | O que contém | Para quem |
|---|---|---|
| **Apresentação** (abaixo) | O que é o jogo, como o vault está organizado, mapa de índices, história e curiosidades | Humanos e IA — contexto inicial |
| **[Parte 1 — Protocolo para Agentes de IA](#parte-1--protocolo-para-agentes-de-ia)** | Arquitetura, estado de completude, convenções, regras de consulta e edição, prioridades | Agentes de IA — instruções operacionais |
| **[Parte 2 — Dados Consolidados do Vault](#parte-2--dados-consolidados-do-vault)** | Dump integral do conteúdo de todos os arquivos do vault, seção por seção | Agentes de IA — base de conhecimento |

> [!important] Para agentes de IA
> Se você recebeu **apenas este arquivo**, ele é suficiente: a Parte 2 contém o conteúdo real de cada nota do vault. Não invente dados que não estejam aqui — sinalize lacunas conforme a seção *Regras para o Agente*.
> Se você tem **acesso ao vault completo**, use este arquivo como mapa e leia as notas originais para obter a versão mais recente.


## Sobre o Jogo — Warframe — Segunda Mente


Warframe é um TPS cooperativo free-to-play ambientado no Sistema Origem — versão futurista do Sistema Solar. O jogador controla um Tenno, guerreiro antigo reanimado, operando dentro de exoesqueletos biomecânicos chamados Warframes. O jogo é construído em torno de farmear recursos, craftar equipamentos e dominar sistemas de build cada vez mais profundos.

**Ciclo central:** missões procedurais → recursos → crafting → novos frames e armas → Mastery Rank → conteúdo end-game.

**Modelo de conteúdo:** expansões gratuitas chamadas *Updates* adicionam novos Warframes, quests, open worlds e modos de jogo continuamente desde 2013.


## Arquitetura do Vault — Warframe — Segunda Mente


Este vault organiza o conhecimento do jogo em pilares independentes com escopo definido e sem sobreposição entre seções.

| Pasta | Conteúdo | Volume |
| --- | --- | --- |
| `warframes/` | Um arquivo por frame — base, Prime e Umbra. Habilidades, papel e como obter. | 64 regulares + 50 primes + 1 umbra = **115** |
| `armas/` | Primárias, secundárias, brancas e archwing. Um arquivo por arma. | 129 + 93 + 135 + 23 = **380** |
| `mods/` | Mods de warframe, armas, companheiros e especiais. Um arquivo por mod. | 91 armas + 54 warframes + 33 companheiros + 38 especiais = **216** |
| `recursos/` | Materiais de crafting por raridade e sistema de origem. | 10 comuns + 3 incomuns + 11 raros + 23 especiais + open world + railjack |
| `missoes/` | Tipos de missão, jornadas, junctions e bounties. | 24 principais + 12 secundárias + 18 jornadas/junções + 35 tipos + 5 bounties |
| `mecanicas/` | Sistemas transversais: combate, progressão, economia, sindicatos e eventos. | 19 mecânicas + eventos + sindicatos |
| `locais/` | Planetas do mapa estelar e open worlds. | 19 planetas + 5 open worlds |
| `lore/` | Cronologia, facções, personagens e chefes. | 29 chefes + 7 cronologia + 8 facções + 26 personagens |
| `companheiros/` | Sentinels, kubrows, kavats, MOAs, hounds e variantes de Deimos. | 16 + 6 + 10 + 6 + 7 = **45** |
| `cosmeticos/` | Skins, syandanas, capacetes, efemeras, paletas e anexos. | 11 arquivos temáticos |

**Regras do sistema:**
- Um arquivo por entidade — cada frame, arma, mod e recurso tem seu próprio `.md`
- **Autossuficiência** — cada arquivo responde sozinho as dúvidas sobre o seu elemento; duplicar dado de outro arquivo é permitido e desejado (ver `_MODELOS/_CONVENCOES.md`, seção 12)
- Uma entidade tem um lar só — inimigos ficam em `lore/faccoes/` via tag `inimigo`, mesmo que sejam citados em outros arquivos
- Mecânicas transversais ficam em `mecanicas/` sem hierarquia profunda
- Rivens têm pasta própria em `mods/especiais/` pelo volume potencial de entradas


## Índices do Sistema — Warframe — Segunda Mente


| Índice                                  | Responde perguntas sobre                                                 | Sub-índices                                                                                                                                                             |
| --------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[warframes/_Warframes _Indice.md\|Warframes]]       | Frames, funções, bosses associados, onde obter, pré-requisitos de acesso | —                                                                                                                                                                       |
| [[armas/_Armas _Indice.md\|Armas]]               | Slots, tipos, fontes, facções e sistemas de origem                       | [[armas/primarias/_Armas _Primarias _Indice.md\|Primárias]] · [[armas/secundarias/_Armas _Secundarias _Indice.md\|Secundárias]] · [[armas/brancas/_Armas _Brancas _Indice.md\|Brancas]] · [[armas/archwing/_Armas _Archwing _Indice.md\|Archwing]] |
| [[mods/_Mods _Indice.md\|Mods]]                 | Raridades, categorias, efeitos resumidos, fontes de obtenção             | [[mods/warframe/_Mods Warframe _Indice.md\|Warframe]] · [[mods/armas/_Mods Armas _Indice.md\|Armas]] · [[mods/companheiros/_Mods Companheiros _Indice.md\|Companheiros]] · [[mods/especiais/_Mods Especiais _Indice.md\|Especiais]]           |
| [[recursos/_Recursos _Indice.md\|Recursos]]         | Materiais, raridades, planetas de origem, métodos de coleta              | —                                                                                                                                                                       |
| [[companheiros/_Companheiros _Indice.md\|Companheiros]] | Tipos, funções, fontes de obtenção, sistemas de origem                   | —                                                                                                                                                                       |
| [[missoes/_Missoes _Indice.md\|Missões]]           | Tipos de missão, objetivos, jornadas, junctions e bounties               | —                                                                                                                                                                       |
| [[mecanicas/_Mecanicas _Indice.md\|Mecânicas]]       | Sistemas de combate, progressão, economia e social                       | [[mecanicas/sindicatos/_Sindicatos _Indice.md\|Sindicatos]] · [[mecanicas/eventos/_Eventos _Indice.md\|Eventos]]                                                                                                     |
| [[locais/_Locais _Indice.md\|Locais]]             | Planetas, facções dominantes, bosses, recursos nativos, como acessar     | —                                                                                                                                                                       |
| [[lore/_Lore _Indice.md\|Lore]]                 | Facções, personagens, chefes, cronologia do universo                     | [[lore/faccoes/_Faccoes _Indice.md\|Facções]] · [[lore/personagens/_Personagens _Indice.md\|Personagens]] · [[lore/chefes/_Chefes _Indice.md\|Chefes]]                                                                     |
| [[cosmeticos/_Cosmeticos _Indice.md\|Cosméticos]]     | Tipos de cosmético, fontes, exclusividade, sistema Tennogen              | —                                                                                                                                                                       |


## História do Jogo — Warframe — Segunda Mente


| Marco | Detalhe |
|---|---|
| **Lançamento** | 25 de março de 2013 — PC, Open Beta |
| **Consoles** | PS4 em novembro de 2013 · Xbox One em setembro de 2014 |
| **Nintendo Switch** | Novembro de 2018 |
| **Modelo F2P** | Gratuito desde o lançamento — monetização via Platinum sem pay-to-win |
| **Plains of Eidolon** | Outubro de 2017 — primeiro open world do jogo |
| **The Second Dream** | Dezembro de 2015 — maior virada narrativa da história do jogo |
| **The Sacrifice** | Junho de 2018 — origem dos Warframes revelada |
| **The New War** | Dezembro de 2021 — quest mais longa e cinematográfica do jogo |
| **The Duviri Paradox** | Abril de 2023 — open world roguelike, Drifter jogável |
| **1999** | Dezembro de 2024 — nova era narrativa, Cidade 1999 |
| **Base de jogadores** | Mais de 70 milhões de contas registradas (2023) |
| **Modelo de updates** | Expansões gratuitas 2–4x por ano com hotfixes contínuos |


## 💡 Curiosidades — Warframe — Segunda Mente


- O jogo ficou em desenvolvimento interno por anos antes do lançamento — a Digital Extremes quase cancelou o projeto.
- "Warframe" era originalmente o nome do exoesqueleto, não do jogo — o título foi mantido por falta de alternativa melhor na época.
- O sistema de parkour foi inspirado em *Mirror's Edge* e expandido ao ponto de se tornar identidade central do jogo.
- Excalibur Prime é o único item completamente indisponível — dado apenas a apoiadores do Founder's Pack em 2013, nunca mais oferecido.
- O lore completo só é revelado através de quests — a maioria dos jogadores passa centenas de horas sem compreender a narrativa principal.
- Warframe tem uma das maiores taxas de retorno de jogadores do Steam — o modelo F2P sem pay-to-win é frequentemente citado como referência do setor.
- O personagem Lotus foi dublado por Rebecca Ford — a mesma pessoa que é diretora de comunidade da Digital Extremes.
- O modo Conclave (PvP) existe desde 2014 mas é considerado pelos próprios desenvolvedores um modo secundário e pouco jogado.
- A DE mantém uma política chamada "não pay-to-win": Platinum não compra poder direto, apenas cosméticos e conveniência de tempo.
- O jogo possui mais de 50 Warframes únicos com 4 habilidades exclusivas cada — mais de 200 habilidades distintas no total.

---
---

# PARTE 1 — PROTOCOLO PARA AGENTES DE IA

## Visão Geral do Projeto — Warframe — Segunda Mente

- Este é um vault Obsidian que serve como uma wiki pessoal de Warframe.
- **Propósito:** Responder a perguntas, planejar builds, acompanhar o progresso e documentar a lore do jogo.
- **Idioma:** Escrito em Português do Brasil, utilizando YAML frontmatter para metadados.
- **Arquivo Raiz:** `_Warframe _Segunda _Mente.md` — este próprio arquivo, que também é o ponto de entrada para agentes.
- **Volumetria das pastas:** ver a tabela *Arquitetura do Vault* na seção de apresentação acima.

## Estado de Completude — Warframe — Segunda Mente

| Nível | Descrição | Exemplos |
|-------|-----------|----------|
| 🟢 Gold Standard (11-38KB) | Artigos completos, detalhados e bem estruturados. | ash.md, atlas.md, ash_prime.md, todos os 14 índices. |
| 🟡 Ficha Básica (600B-1.8KB) | Estrutura principal preenchida com dados essenciais. | excalibur, volt, mag, planetas, alguns chefes, cosméticos. |
| 🟠 Template Vazio (400-900B) | Possui a estrutura base, mas os valores estão em branco ou placeholders básicos. | ~53 warframes regulares. |
| 🔴 Stub/Placeholder (0-130B) | Apenas arquivos criados ou com informações mínimas/nulas. | A maioria das armas, companheiros, mods, facções, personagens e mecânicas. |

**Progresso Geral Estimado:** ~5-8%

## Padrões e Convenções — Warframe — Segunda Mente

- **Nomenclatura de Arquivos:** letras minúsculas com underscores (ex: `ash_prime.md`).
- **Índices:** Nomeados como `_NomeDaSeção _Indice.md`.
- **Emojis nos Cabeçalhos:**
  - 📖 História
  - 🎮 Gameplay
  - 💡 Trivia
  - 🔮 Habilidades
  - 🏗️ Aquisição
  - 📊 Stats
  - 🛠️ Builds
  - 🧬 Helminth
  - 🔗 Sinergias
  - 🎨 Fashion Frame

## Regras para o Agente — Warframe — Segunda Mente

- **Consulta:** Comece sempre procurando informações nos índices relevantes (ou nas seções correspondentes da Parte 2 deste arquivo). Use Português do Brasil nas respostas. Informe o usuário se o conteúdo não estiver presente ou estiver incompleto (🔴 Stub ou 🟠 Template Vazio).
- **Edição:** Siga rigorosamente o padrão "Gold Standard" visto em `ash.md`. Preserve as seções do YAML, mantenha o uso dos emojis nos cabeçalhos e atualize as datas ao modificar arquivos.
- **Planejamento:** Faça referências cruzadas entre seções (ex: relacionando armas com warframes ou missões com recursos). Considere Maestria (MR) e pré-requisitos ao recomendar planos. Use tabelas e checklists sempre que possível para facilitar a leitura.

## Como navegar a Parte 2 — Warframe — Segunda Mente

- A Parte 2 é um dump linear do vault, agrupado por `## Seção: <pasta>` e, dentro dela, por `### 📄 arquivo: <nome>.md`.
- Para localizar uma entidade, busque pelo nome do arquivo (ex: `arquivo: ash_prime.md`) ou pelo título da nota.
- A seção raiz não é repetida na Parte 2 — o conteúdo dela é justamente a apresentação no topo deste documento.

## Prioridades de Expansão — Warframe — Segunda Mente

1. **CRITICAL:** Mecânicas (dano_e_status, critico, helminth, etc. - todos vazios atualmente)
2. **HIGH:** ~53 templates de warframes aguardando preenchimento.
3. **HIGH:** Facções e personagens da Lore (todos vazios).
4. **MEDIUM:** 49 stubs de warframes primes.
5. **MEDIUM-LOW:** Armas populares.
6. **LOW:** Catálogo completo restante (mods, recursos, companheiros, missões).

---
---

# PARTE 2 — DADOS CONSOLIDADOS DO VAULT

> Dump integral do conteúdo das notas do vault, por seção. A seção raiz foi omitida por já constar na apresentação acima.

## Seção: warframes — Warframe — Segunda Mente

### 📄 arquivo: _Warframes _Indice.md

# Warframes — Índice

> [!quote]
> *"Nós construímos um quadro ao redor da Infestação... canalizamos sua aflição... a transformamos em força."* — Ballas


## 📊 Visão Geral — Warframe — Segunda Mente


Warframes são exoesqueletos biomecânicos letais controlados pelos **Tenno** através de uma simbiose chamada **Transferência**. Forjados a partir do vírus Helminth combinado à tecnologia Orokin, surgiram durante a Antiga Guerra como resposta contra os Sentients. Cada frame canaliza energias elementais, distorcionais ou físicas únicas — definindo um papel distinto em combate.


## 🌍 Onde Conseguir — Warframe — Segunda Mente


Warframes não são dropados prontos — são construídos na **Fundição** a partir de quatro diagramas:

| Componente | Descrição |
|---|---|
| **Diagrama Principal** | Comprado por Créditos no Mercado ou obtido em quests |
| **Chassi** | Armadura pesada com musculatura infestada artificial |
| **Neurovisor** | Capacete orgânico com interfaces neurais de Transferência |
| **Sistemas** | Matriz de processamento energético e controle de habilidades |

Subcomponentes levam **12 horas** cada. O frame completo leva **72 horas**. Platinum agiliza qualquer etapa.

**Fontes de diagramas:**
- Assassinar chefes em nódulos planetários
- Completar jornadas (quests)
- Pesquisa em laboratórios de Clã
- Bounties em Open Worlds
- Relíquias do Void (versões Prime)

### Mastery e Rank

Todo Warframe nasce no Rank 0 e avança até o Rank 30 via Afinidade. Cada rank concede um ponto de capacidade de mod. Ao atingir Rank 30 pela primeira vez, o frame contribui com **6.000 pontos de Mastery** na conta.

### Subsunção (Helminth)

Após Rank 30, versões base (não-Prime) podem ser **sacrificadas ao Helminth**. O Helminth aprende uma habilidade predefinida do frame consumido — disponível para ser injetada em qualquer outro Warframe do arsenal, permitindo builds híbridas.


## Mecânicas Base — Warframe — Segunda Mente


| Atributo | Função |
|---|---|
| **Vida** | Barra principal — não regenera sozinha. Recuperada com Orbes Vermelhos ou habilidades de cura |
| **Escudos** | Primeira linha de defesa — regeneram automaticamente. Quebrar ativa Shield Gating (invulnerabilidade breve) |
| **Armadura** | Reduz dano recebido na Vida (não nos Escudos, salvo exceções) |
| **Energia** | Combustível das habilidades — recuperada com Orbes Azuis ou passivas de Aura |


## Mods e Polaridades — Warframe — Segunda Mente


O poder real de um Warframe vem dos **Mods** equipados, não do nível base. Quatro vetores de customização:

| Vetor | Efeito |
|---|---|
| **Força** | Amplifica o potencial das habilidades |
| **Alcance** | Expande a área de efeito |
| **Duração** | Prolonga efeitos temporais |
| **Eficiência** | Reduz o custo de Energia |

**Formas e Polaridades:** aplicar uma Forma reseta o rank para 0 mas adiciona uma polaridade ao slot. Mods na polaridade correta custam metade da capacidade. O slot de **Aura**, quando alinhado, concede capacidade extra em vez de consumir.


## 📋 Lista Completa — Warframe — Segunda Mente


### Warframes Base

| Warframe | Função | Fonte | Local | Pré-requisito |
|---|---|---|---|---|
| [[warframes/regular/ash.md\|Ash]] | DPS furtivo | Manics (inimigo especial Grineer) | Sedna e outros | — |
| [[warframes/regular/atlas.md\|Atlas]] | Melee / Terra | Quest — The Jordas Precept | Eris | The New Strange |
| [[warframes/regular/banshee.md\|Banshee]] | Amplificador de dano | Pesquisa de Clã (Bio Lab) | Dojo | — |
| [[warframes/regular/baruuk.md\|Baruuk]] | Pacifista / Melee | Bounties — Orbe Vallis | Vênus | Rank Instrument (Solaris United) |
| [[warframes/regular/caliban.md\|Caliban]] | Sentient híbrido | Quest — The New War | — | The New War |
| [[warframes/regular/chroma.md\|Chroma]] | Elementar / Tanque | Quest — The New Strange | — | Vor's Prize |
| [[warframes/regular/citrine.md\|Citrine]] | Suporte / Cristal | Drop — Sanctum Anatomica | Deimos | Whispers in the Walls |
| [[warframes/regular/cyte_09.md\|Cyte-09]] | Tático / Franco-atirador | Missões — Cidade 1999 | 1999 | Quest 1999 |
| [[warframes/regular/dagath.md\|Dagath]] | DPS / Amaldiçoada | Drop — inimigos Whispers in the Walls | Deimos | Whispers in the Walls |
| [[warframes/regular/dante.md\|Dante]] | Suporte / DPS Mágico | Drop — Sanctum Anatomica | Deimos | Whispers in the Walls |
| [[warframes/regular/ember.md\|Ember]] | DPS fogo | Assassinato — Sargas Ruk | Saturno | — |
| [[warframes/regular/equinox.md\|Equinox]] | Dual-form DPS/suporte | Assassinato — Tyl Regor | Urano | — |
| [[warframes/regular/excalibur.md\|Excalibur]] | Melee balanceado | Assassinato — Lech Kril | Marte | — |
| [[warframes/regular/follie.md\|Follie]] | DPS / Suporte | A verificar | — | — |
| [[warframes/regular/frost.md\|Frost]] | Controle / Defesa | Assassinato — Lech Kril | Ceres | — |
| [[warframes/regular/gara.md\|Gara]] | Vidro / Controle | Bounties — Planícies de Eidolon | Terra | — |
| [[warframes/regular/garuda.md\|Garuda]] | DPS sangue | Bounties — Orbe Vallis | Vênus | — |
| [[warframes/regular/gauss.md\|Gauss]] | Velocidade | Disruption — Kelpie | Sedna | — |
| [[warframes/regular/grendel.md\|Grendel]] | Tanque glutão | Missões tributo (3 nodos) | Europa / Lua / Fortaleza Kuva | The War Within |
| [[warframes/regular/gyre.md\|Gyre]] | DPS elétrico | Bounties — Zariman | Zariman | Angels of the Zariman |
| [[warframes/regular/harrow.md\|Harrow]] | Suporte / Buff | Defection + Void Fissure (Rotação C) | Eris / Void | Chains of Harrow |
| [[warframes/regular/hildryn.md\|Hildryn]] | Tanque escudo | Vox Solaris (Fortuna) | Vênus | Rank Hand (Vox Solaris) |
| [[warframes/regular/hydroid.md\|Hydroid]] | Controle / Loot | Assassinato — Vay Hek | Terra | — |
| [[warframes/regular/inaros.md\|Inaros]] | Tanque HP | Quest — Sands of Inaros | — | MR5, The Second Dream |
| [[warframes/regular/ivara.md\|Ivara]] | Furtivo / Loot | Spy — Rotação C | Lua / Corpus | — |
| [[warframes/regular/jade.md\|Jade]] | Suporte angelical | Quest — Jade Shadows | — | Angels of the Zariman |
| [[warframes/regular/khora.md\|Khora]] | DPS / Controle | Elite Sanctuary Onslaught | — | MR8 |
| [[warframes/regular/koumei.md\|Koumei]] | Suporte / Sorte | The Circuit — Duviri | Duviri | The Duviri Paradox |
| [[lore/chefes/kullervo.md\|Kullervo]] | Melee pesado | Kullervo's Hold | Duviri | The Duviri Paradox |
| [[warframes/regular/lavos.md\|Lavos]] | Alquimista elemental | Pesquisa de Clã (Entrati Lab) | Câmbion Drift | Heart of Deimos |
| [[warframes/regular/limbo.md\|Limbo]] | Controle dimensional | Quest — The Limbo Theorem | — | MR2 |
| [[warframes/regular/loki.md\|Loki]] | Furtivo / Controle | Assassinato — Hyena Pack | Netuno | — |
| [[warframes/regular/mag.md\|Mag]] | Magnético / Controle | Starter — Vor's Prize | — | — |
| [[warframes/regular/mesa.md\|Mesa]] | DPS pistolas | Assassinato — Ambulas | Plutão | Patient Zero |
| [[warframes/regular/mirage.md\|Mirage]] | DPS ilusão | Quest — Hidden Messages | — | MR4 |
| [[warframes/regular/nekros.md\|Nekros]] | Necromante / Loot | Assassinato — Lephantis | Deimos | — |
| [[warframes/regular/nezha.md\|Nezha]] | Suporte ágil | Pesquisa de Clã (Tenno Lab) | Dojo | — |
| [[warframes/regular/nidus.md\|Nidus]] | Infestado / Tanque | Infested Salvage — Eris | Eris | The Glast Gambit |
| [[warframes/regular/nokko.md\|Nokko]] | Suporte / Defesa | A verificar | — | — |
| [[warframes/regular/nova.md\|Nova]] | Controle / DPS | Assassinato — Raptors | Europa | — |
| [[warframes/regular/nyx.md\|Nyx]] | Controle mental | Assassinato — Alad V | Júpiter | — |
| [[warframes/regular/oberon.md\|Oberon]] | Paladino / Suporte | Drop — Eximus (qualquer planeta) | Qualquer | — |
| [[warframes/regular/octavia.md\|Octavia]] | Bardo / DPS | Caches — Orokin Derelict / Lua | Deimos / Lua | Octavia's Anthem |
| [[warframes/regular/oraxia.md\|Oraxia]] | Controle / DPS | A verificar | — | — |
| [[warframes/regular/protea.md\|Protea]] | Suporte / Turrets | Quest — The Deadlock Protocol | — | MR8 |
| [[warframes/regular/qorvex.md\|Qorvex]] | Tanque radiação | Drop — Sanctum Anatomica | Deimos | Whispers in the Walls |
| [[warframes/regular/revenant.md\|Revenant]] | Eidolon / Tanque | Bounties — Planícies (noite) | Terra | Mask of the Revenant |
| [[warframes/regular/rhino.md\|Rhino]] | Tanque clássico | Assassinato — Jackal | Vênus | — |
| [[warframes/regular/saryn.md\|Saryn]] | DPS veneno | Assassinato — Kela de Thaym | Sedna | — |
| [[warframes/regular/sevagoth.md\|Sevagoth]] | Sombra / Drenagem | Void Storms — Railjack | Railjack | Rising Tide |
| [[warframes/regular/styanax.md\|Styanax]] | Tanque / Suporte | Quest — Veilbreaker (gratuito) | — | The New War |
| [[warframes/regular/temple.md\|Temple]] | Tanque / Melee | A verificar | — | — |
| [[warframes/regular/titania.md\|Titania]] | Fada / Archwing | Quest — The Silver Grove | — | The Second Dream |
| [[warframes/regular/trinity.md\|Trinity]] | Suporte / Cura | Assassinato — Phobos | Phobos | — |
| [[warframes/regular/uriel.md\|Uriel]] | Suporte angelical | A verificar | — | — |
| [[warframes/regular/valkyr.md\|Valkyr]] | Berserker melee | Assassinato — Alad V (Zanuka) | Júpiter | — |
| [[warframes/regular/vauban.md\|Vauban]] | Suporte / Controle | Nightwave / Sorties | — | — |
| [[warframes/regular/volt.md\|Volt]] | DPS elétrico / Velocidade | Starter / Pesquisa de Clã | Dojo | — |
| [[warframes/regular/voruna.md\|Voruna]] | Furtivo / Assaltante | Assassinato — Lua | Lua | The Second Dream |
| [[warframes/regular/wisp.md\|Wisp]] | Suporte / DPS | Assassinato — Ropalolyst | Júpiter | — |
| [[warframes/regular/wukong.md\|Wukong]] | Clones / Sobrevivência | Pesquisa de Clã (Tenno Lab) | Dojo | — |
| [[warframes/regular/xaku.md\|Xaku]] | Void / DPS | Bounties — Câmbion Drift | Deimos | Heart of Deimos |
| [[warframes/regular/yareli.md\|Yareli]] | Aquático / K-Drive | Quest — The Waverider | — | Heart of Deimos |
| [[warframes/regular/zephyr.md\|Zephyr]] | Aéreo / Mobilidade | Pesquisa de Clã (Tenno Lab) | Dojo | — |


### Warframes Prime

> [!info] Aquisição
> Todos os Warframes Prime são obtidos via **Relíquias do Void** em missões de **Fissura**. Relíquias com peças específicas podem ser refinadas com Void Traces para aumentar a raridade das recompensas. Frames em **Prime Vault** têm suas relíquias temporariamente fora de rotação — retornam periodicamente via Prime Resurgence.

| Warframe Prime                       | Função                    | Rotação                                |
| ------------------------------------ | ------------------------- | -------------------------------------- |
| [[warframes/primes/ash_prime.md\|Ash Prime]]             | DPS furtivo               | Normal                                 |
| [[warframes/primes/atlas_prime.md\|Atlas Prime]]         | Melee / Terra             | Normal                                 |
| [[warframes/primes/banshee_prime.md\|Banshee Prime]]     | Amplificador de dano      | Normal                                 |
| [[warframes/primes/baruuk_prime.md\|Baruuk Prime]]       | Pacifista / Melee         | Normal                                 |
| [[warframes/primes/caliban_prime.md\|Caliban Prime]]     | Sentient híbrido          | Normal                                 |
| [[warframes/primes/chroma_prime.md\|Chroma Prime]]       | Elementar / Tanque        | Prime Vault                            |
| [[warframes/primes/ember_prime.md\|Ember Prime]]         | DPS fogo                  | Prime Vault                            |
| [[warframes/primes/equinox_prime.md\|Equinox Prime]]     | Dual-form DPS/suporte     | Normal                                 |
| [[warframes/primes/excalibur_prime.md\|Excalibur Prime]] | Melee balanceado          | **Indisponível** — Founder's Pack 2013 |
| [[warframes/primes/frost_prime.md\|Frost Prime]]         | Controle / Defesa         | Prime Vault                            |
| [[warframes/primes/gara_prime.md\|Gara Prime]]           | Vidro / Controle          | Normal                                 |
| [[warframes/primes/garuda_prime.md\|Garuda Prime]]       | DPS sangue                | Normal                                 |
| [[warframes/primes/gauss_prime.md\|Gauss Prime]]         | Velocidade                | Normal                                 |
| [[warframes/primes/grendel_prime.md\|Grendel Prime]]     | Tanque glutão             | Normal                                 |
| [[warframes/primes/gyre_prime.md\|Gyre Prime]]           | DPS elétrico              | Normal                                 |
| [[warframes/primes/harrow_prime.md\|Harrow Prime]]       | Suporte / Buff            | Normal                                 |
| [[warframes/primes/hildryn_prime.md\|Hildryn Prime]]     | Tanque escudo             | Normal                                 |
| [[warframes/primes/hydroid_prime.md\|Hydroid Prime]]     | Controle / Loot           | Prime Vault                            |
| [[warframes/primes/inaros_prime.md\|Inaros Prime]]       | Tanque HP                 | Normal                                 |
| [[warframes/primes/ivara_prime.md\|Ivara Prime]]         | Furtivo / Loot            | Normal                                 |
| [[warframes/primes/khora_prime.md\|Khora Prime]]         | DPS / Controle            | Normal                                 |
| [[warframes/primes/lavos_prime.md\|Lavos Prime]]         | Alquimista elemental      | Normal                                 |
| [[warframes/primes/limbo_prime.md\|Limbo Prime]]         | Controle dimensional      | Prime Vault                            |
| [[warframes/primes/loki_prime.md\|Loki Prime]]           | Furtivo / Controle        | Prime Vault                            |
| [[warframes/primes/mag_prime.md\|Mag Prime]]             | Magnético / Controle      | Prime Vault                            |
| [[warframes/primes/mesa_prime.md\|Mesa Prime]]           | DPS pistolas              | Normal                                 |
| [[warframes/primes/mirage_prime.md\|Mirage Prime]]       | DPS ilusão                | Prime Vault                            |
| [[warframes/primes/nekros_prime.md\|Nekros Prime]]       | Necromante / Loot         | Prime Vault                            |
| [[warframes/primes/nezha_prime.md\|Nezha Prime]]         | Suporte ágil              | Normal                                 |
| [[warframes/primes/nidus_prime.md\|Nidus Prime]]         | Infestado / Tanque        | Normal                                 |
| [[warframes/primes/nova_prime.md\|Nova Prime]]           | Controle / DPS            | Prime Vault                            |
| [[warframes/primes/nyx_prime.md\|Nyx Prime]]             | Controle mental           | Prime Vault                            |
| [[warframes/primes/oberon_prime.md\|Oberon Prime]]       | Paladino / Suporte        | Prime Vault                            |
| [[warframes/primes/octavia_prime.md\|Octavia Prime]]     | Bardo / DPS               | Normal                                 |
| [[warframes/primes/protea_prime.md\|Protea Prime]]       | Suporte / Turrets         | Normal                                 |
| [[warframes/primes/revenant_prime.md\|Revenant Prime]]   | Eidolon / Tanque          | Normal                                 |
| [[warframes/primes/rhino_prime.md\|Rhino Prime]]         | Tanque clássico           | Prime Vault                            |
| [[warframes/primes/saryn_prime.md\|Saryn Prime]]         | DPS veneno                | Normal                                 |
| [[warframes/primes/sevagoth_prime.md\|Sevagoth Prime]]   | Sombra / Drenagem         | Normal                                 |
| [[warframes/primes/titania_prime.md\|Titania Prime]]     | Fada / Archwing           | Normal                                 |
| [[warframes/primes/trinity_prime.md\|Trinity Prime]]     | Suporte / Cura            | Prime Vault                            |
| [[warframes/primes/valkyr_prime.md\|Valkyr Prime]]       | Berserker melee           | Prime Vault                            |
| [[warframes/primes/vauban_prime.md\|Vauban Prime]]       | Suporte / Controle        | Prime Vault                            |
| [[warframes/primes/volt_prime.md\|Volt Prime]]           | DPS elétrico / Velocidade | Prime Vault                            |
| [[warframes/primes/voruna_prime.md\|Voruna Prime]]       | Furtivo / Assaltante      | Normal                                 |
| [[warframes/primes/wisp_prime.md\|Wisp Prime]]           | Suporte / DPS             | Normal                                 |
| [[warframes/primes/wukong_prime.md\|Wukong Prime]]       | Clones / Sobrevivência    | Normal                                 |
| [[warframes/primes/xaku_prime.md\|Xaku Prime]]           | Void / DPS                | Normal                                 |
| [[warframes/primes/yareli_prime.md\|Yareli Prime]]       | Aquático / K-Drive        | Normal                                 |
| [[warframes/primes/zephyr_prime.md\|Zephyr Prime]]       | Aéreo / Mobilidade        | Normal                                 |


### Warframe Umbra

> [!info] Aquisição
> Warframes Umbra são versões com consciência própria — operam de forma autônoma quando o Operador abandona o controle. Excalibur Umbra é o único existente e só pode ser obtido via quest.

| Warframe | Função | Fonte | Pré-requisito |
|---|---|---|---|
| [[warframes/umbra/excalibur_umbra.md\|Excalibur Umbra]] | Melee / Anti-Sentient | Quest — The Sacrifice | The War Within |


## Por Função — Warframe — Segunda Mente


### Tanques e Bruisers
[[warframes/regular/rhino.md|Rhino]] · [[warframes/primes/rhino_prime.md|Rhino Prime]] · [[warframes/regular/inaros.md|Inaros]] · [[warframes/primes/inaros_prime.md|Inaros Prime]] · [[warframes/regular/nidus.md|Nidus]] · [[warframes/primes/nidus_prime.md|Nidus Prime]] · [[warframes/regular/hildryn.md|Hildryn]] · [[warframes/primes/hildryn_prime.md|Hildryn Prime]] · [[warframes/regular/valkyr.md|Valkyr]] · [[warframes/primes/valkyr_prime.md|Valkyr Prime]] · [[warframes/regular/grendel.md|Grendel]] · [[warframes/primes/grendel_prime.md|Grendel Prime]] · [[warframes/regular/styanax.md|Styanax]] · [[warframes/regular/chroma.md|Chroma]] · [[warframes/primes/chroma_prime.md|Chroma Prime]] · [[warframes/regular/revenant.md|Revenant]] · [[warframes/primes/revenant_prime.md|Revenant Prime]] · [[warframes/regular/qorvex.md|Qorvex]] · [[warframes/regular/temple.md|Temple]] · [[warframes/regular/wukong.md|Wukong]] · [[warframes/primes/wukong_prime.md|Wukong Prime]]

### DPS e Nukers
[[warframes/regular/saryn.md|Saryn]] · [[warframes/primes/saryn_prime.md|Saryn Prime]] · [[warframes/regular/mesa.md|Mesa]] · [[warframes/primes/mesa_prime.md|Mesa Prime]] · [[warframes/regular/ember.md|Ember]] · [[warframes/primes/ember_prime.md|Ember Prime]] · [[warframes/regular/khora.md|Khora]] · [[warframes/primes/khora_prime.md|Khora Prime]] · [[warframes/regular/garuda.md|Garuda]] · [[warframes/primes/garuda_prime.md|Garuda Prime]] · [[warframes/regular/gyre.md|Gyre]] · [[warframes/primes/gyre_prime.md|Gyre Prime]] · [[warframes/regular/mirage.md|Mirage]] · [[warframes/primes/mirage_prime.md|Mirage Prime]] · [[warframes/regular/dagath.md|Dagath]] · [[warframes/regular/titania.md|Titania]] · [[warframes/primes/titania_prime.md|Titania Prime]] · [[warframes/regular/volt.md|Volt]] · [[warframes/primes/volt_prime.md|Volt Prime]] · [[warframes/regular/xaku.md|Xaku]] · [[warframes/primes/xaku_prime.md|Xaku Prime]] · [[warframes/regular/cyte_09.md|Cyte-09]] · [[warframes/regular/excalibur.md|Excalibur]] · [[warframes/regular/equinox.md|Equinox]] · [[warframes/primes/equinox_prime.md|Equinox Prime]]

### Suporte e Buffers
[[warframes/regular/trinity.md|Trinity]] · [[warframes/primes/trinity_prime.md|Trinity Prime]] · [[warframes/regular/wisp.md|Wisp]] · [[warframes/primes/wisp_prime.md|Wisp Prime]] · [[warframes/regular/harrow.md|Harrow]] · [[warframes/primes/harrow_prime.md|Harrow Prime]] · [[warframes/regular/protea.md|Protea]] · [[warframes/primes/protea_prime.md|Protea Prime]] · [[warframes/regular/oberon.md|Oberon]] · [[warframes/primes/oberon_prime.md|Oberon Prime]] · [[warframes/regular/nezha.md|Nezha]] · [[warframes/primes/nezha_prime.md|Nezha Prime]] · [[warframes/regular/citrine.md|Citrine]] · [[warframes/regular/dante.md|Dante]] · [[warframes/regular/jade.md|Jade]] · [[warframes/regular/koumei.md|Koumei]] · [[warframes/regular/nokko.md|Nokko]] · [[warframes/regular/uriel.md|Uriel]] · [[warframes/regular/octavia.md|Octavia]] · [[warframes/primes/octavia_prime.md|Octavia Prime]]

### Controle de Grupo
[[warframes/regular/frost.md|Frost]] · [[warframes/primes/frost_prime.md|Frost Prime]] · [[warframes/regular/limbo.md|Limbo]] · [[warframes/primes/limbo_prime.md|Limbo Prime]] · [[warframes/regular/nyx.md|Nyx]] · [[warframes/primes/nyx_prime.md|Nyx Prime]] · [[warframes/regular/vauban.md|Vauban]] · [[warframes/primes/vauban_prime.md|Vauban Prime]] · [[warframes/regular/gara.md|Gara]] · [[warframes/primes/gara_prime.md|Gara Prime]] · [[warframes/regular/mag.md|Mag]] · [[warframes/primes/mag_prime.md|Mag Prime]] · [[warframes/regular/nova.md|Nova]] · [[warframes/primes/nova_prime.md|Nova Prime]] · [[warframes/regular/hydroid.md|Hydroid]] · [[warframes/primes/hydroid_prime.md|Hydroid Prime]] · [[warframes/regular/yareli.md|Yareli]] · [[warframes/primes/yareli_prime.md|Yareli Prime]] · [[warframes/regular/zephyr.md|Zephyr]] · [[warframes/primes/zephyr_prime.md|Zephyr Prime]] · [[warframes/regular/oraxia.md|Oraxia]] · [[warframes/regular/lavos.md|Lavos]] · [[warframes/primes/lavos_prime.md|Lavos Prime]] · [[warframes/regular/nekros.md|Nekros]] · [[warframes/primes/nekros_prime.md|Nekros Prime]]

### Furtivos e Táticos
[[warframes/regular/loki.md|Loki]] · [[warframes/primes/loki_prime.md|Loki Prime]] · [[warframes/regular/ivara.md|Ivara]] · [[warframes/primes/ivara_prime.md|Ivara Prime]] · [[warframes/regular/ash.md|Ash]] · [[warframes/primes/ash_prime.md|Ash Prime]] · [[warframes/regular/voruna.md|Voruna]] · [[warframes/primes/voruna_prime.md|Voruna Prime]] · [[warframes/regular/banshee.md|Banshee]] · [[warframes/primes/banshee_prime.md|Banshee Prime]]

### Melee e Híbridos
[[warframes/regular/atlas.md|Atlas]] · [[warframes/primes/atlas_prime.md|Atlas Prime]] · [[warframes/regular/baruuk.md|Baruuk]] · [[warframes/primes/baruuk_prime.md|Baruuk Prime]] · [[lore/chefes/kullervo.md|Kullervo]] · [[warframes/regular/caliban.md|Caliban]] · [[warframes/primes/caliban_prime.md|Caliban Prime]] · [[warframes/regular/follie.md|Follie]] · [[warframes/regular/sevagoth.md|Sevagoth]] · [[warframes/primes/sevagoth_prime.md|Sevagoth Prime]] · [[warframes/regular/gauss.md|Gauss]] · [[warframes/primes/gauss_prime.md|Gauss Prime]] · [[warframes/umbra/excalibur_umbra.md|Excalibur Umbra]]


## 🔗 Relacionados — Warframe — Segunda Mente


| Sistema | Índice |
|---|---|
| Mods de Warframe | [[mods/warframe/_Mods Warframe _Indice.md\|Mods — Warframe]] |
| Bosses e drops | [[lore/chefes/_Chefes _Indice.md\|Chefes]] |
| Locais de obtenção | [[locais/_Locais _Indice.md\|Locais]] |
| Missões e jornadas | [[missoes/_Missoes _Indice.md\|Missões]] |
| Sistemas de progressão | [[mecanicas/_Mecanicas _Indice.md\|Mecânicas]] |


## 💡 Curiosidades — Warframe — Segunda Mente


- Excalibur foi o primeiro Warframe jogável — presente desde o alpha interno em 2012.
- Loki era o frame mais popular no early game por anos pela invisibilidade e utilidade universal — perdeu relevância com powercreep de frames mais recentes.
- Excalibur Umbra é único no jogo: opera de forma autônoma com IA própria quando o Operador abandona o controle, reagindo ativamente ao ambiente.
- Ash foi por muito tempo considerado inviável — sua habilidade Blade Storm era lenta e manual. Uma rework completa o tornou competitivo.
- Nidus não possui Escudos — sobrevive exclusivamente por stacks de mutação e regeneração, tornando-o imune à mecânica de Shield Gating.
- Nekros foi projetado especificamente para "resolver" o problema de drop rate — Desecrate rola drops adicionais em cadáveres, dobrando efetivamente o rendimento de farm.
- Titania foi o primeiro frame a introduzir voo em miniatura (Razorwing) — transforma o jogador em um archwing pessoal dentro de missões terrestres.
- Octavia é o único frame onde o jogador compõe a própria música que alimenta as habilidades, via o instrumento Mandachord.
- Ivara foi historicamente o frame mais difícil de obter — componentes só dropavam em missões Spy completadas sem acionar alarmes, com rotação C.
- Oberon é o único frame base cujos componentes não vêm de um boss específico — dropam aleatoriamente de inimigos Eximus em qualquer planeta.

----------------------------------------

## Seção: warframes\regular — Warframe — Segunda Mente

### 📄 arquivo: ash.md

> *"A lenda diz que um predador letal ataca a partir das sombras. Ash não tem como alvo os olhos, mas sim as defesas de seus oponentes. Ele é conhecido como o patrono das lâminas imperturbáveis."* — **Códice, Warframe.com**

## 📖 História e Códice — Warframe — Segunda Mente


Desenvolvido durante o [[lore/faccoes/orokin.md|Império Orokin]], Ash foi concebido como uma solução para missões que exigiam letalidade silenciosa e infiltração. Sua tecnologia modular e métodos de combate derivam da escola de assassinos conhecida como *Scoria*. Ao contrário de modelos criados para a linha de frente da Antiga Guerra contra os [[lore/faccoes/sentient.md|Sentient]], Ash especializou-se na eliminação de alvos de alto valor e na neutralização de traidores em ambientes restritos, executando táticas de extermínio sem detecção prévia.

## 🎮 Visão Geral e Gameplay — Warframe — Segunda Mente


Ash é um Warframe focado em mobilidade, invisibilidade e dano direto focado. Sua eficácia principal reside na capacidade de infligir "Dano Verdadeiro" através da constante aplicação de status de Sangramento (Cortante/Slash). Essa mecânica permite que ele escale facilmente em curvas de dificuldade altas (como o [[sistemas/caminho_de_aco.md|Caminho de Aço]]), onde a armadura inimiga mitiga quase todo o dano padrão. O estilo de jogo recomendado é o reposicionamento contínuo, a manutenção cautelosa da habilidade de invisibilidade (Smoke Screen) e foco em eliminações chave utilizando suas habilidades letais em vez de assumir postura de defesa em área fixa.

## 💡 Curiosidades (Trivia) — Warframe — Segunda Mente


Durante a fase de desenvolvimento alfa na Digital Extremes, Ash recebeu o nome inicial de "Ninja", o que justifica os elementos de design estético de sua armadura padrão, inspirados no folclore de armaduras lamelares e besouros.

No seu lançamento em 2013, o estilo anatômico do chassi foi considerado uma contraparte tática direta aos modelos focados em controle de multidão com magia elemental da época, como [[warframes/saryn.md|Saryn]] e [[warframes/nyx.md|Nyx]].

As quatro habilidades de Ash causam estritamente dano físico (frequentemente tipo Cortante), o que o torna uma exceção entre warframes de longo alcance que normalmente dependem de efeitos elementais para dano base.

## 🔮 Habilidades — Warframe — Segunda Mente


* **Passiva (Hemorragia):** Efeitos de status Cortante (*Slash*) infligidos de qualquer fonte originada por Ash recebem **25% de Dano Adicional** e um **incremento de 50% em sua duração base**.

* **1. Shuriken (25 Energia):** Arremessa instantaneamente duas lâminas teleguiadas em alvos próximos. As lâminas rasgam armaduras e aplicam um efeito de sangramento imediato garantido.

* **2. Smoke Screen (35 Energia):** Derruba uma bomba de fumaça. Atordoa os inimigos dentro do raio de impacto inicial e concede invisibilidade a Ash.

* **3. Teleport (25 Energia):** Teletransporta Ash instantaneamente para o local do inimigo ou aliado focado. Ao surgir, o alvo fica suscetível a sofrer uma finalização de execução (*Finisher*) imediata.

* **4. Blade Storm (Drenagem Mirada):** Entra em um modo visual rastejante para aplicar marcas adversárias. Ao recativular a habilidade, clones invulneráveis do Ash avançarão pelas paredes para despachar alvos marcados em dano cortante concentrado.

## 🌍 Onde Conseguir — Warframe — Segunda Mente


Os diagramas de Ash são listados exclusivamente nas tabelas de drops do modo **[[missoes/railjack.md|Railjack]] (Facção [[lore/faccoes/corpus.md|Corpus]])**, limitados às Rotações C de missões de longa duração, como as de Defesa e [[missoes/sobrevivencia.md|Sobrevivência]] em proximidades específicas. 

#### Tabela de Fabricação Base
| Componente            | Missões de Drop de Diagrama                                                     | Requisitos Materiais e [[recursos/creditos.md\|Créditos]]                                                                                                                                                                                             | Tempo de Forja |
| --------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| **Warframe Completo** | Mercado do Jogo (35.000 [[recursos/creditos.md\|Créditos]])                     | 25.000 [[recursos/creditos.md\|Créditos]] + 1 [[recursos/celula_orokin.md\|Célula Orokin]] + **Sistemas, Chassi e Neurovisor**                                                                                                                        | 72 Horas       |
| **Neurovisor**        | [[missoes/railjack.md\|Railjack]]: [[locais/netuno_proxima.md\|Netuno Próxima]] | 15.000 [[recursos/creditos.md\|Créditos]] + 1 [[recursos/sensores_neurais.md\|Sensores Neurais]] + 150 [[recursos/pacotes_de_polimero.md\|Placas Polímero]] + 500 [[recursos/rubedo.md\|Rubedo]] + 150 [[recursos/placas_de_liga.md\|Placas da Liga]] | 12 Horas       |
| **Chassi**            | [[missoes/railjack.md\|Railjack]]: [[locais/plutao_proxima.md\|Plutão Próxima]] | 15.000 [[recursos/creditos.md\|Créditos]] + 1 [[recursos/morficos.md\|Mórficos]] + 1.000 [[recursos/ferrite.md\|Ferrites]] + 300 [[recursos/rubedo.md\|Rubedo]]                                                                                       | 12 Horas       |
| **Sistemas**          | [[missoes/railjack.md\|Railjack]]: [[locais/venus_proxima.md\|Vênus Próxima]]   | 15.000 [[recursos/creditos.md\|Créditos]] + 1 [[recursos/modulo_de_controle.md\|Módulo de Controle]] + 1 Mórfico + 500 [[recursos/plastidos.md\|Plásticos]] + 500 [[recursos/sucata.md\|Sucatas]]                                                     | 12 Horas       |

#### Vias Alternativas de Obtenção:

* **Iniciação de [[recursos/platina.md|Platina]]:** O pacote exato completo do quadro é comercializável pronto via [[recursos/platina.md|Platina]] dentro do Mercado na Orbiter (vem com um [[sistemas/reator_orokin.md|Reator Orokin]] e Slot Inclusos).

* **O Circuito ([[locais/duviri.md|Duviri]]):** Há semanas rotativas regulares do "Paradoxo de [[locais/duviri.md|Duviri]]" normal, nas quais todas as partes de diagramas do Ash podem ser coletadas completando etapas da jornada.

## 📊 Estatísticas Matemáticas e Sobrevivência (Rank 0 -> 30) — Warframe — Segunda Mente


| Atributo Oficial | Status Base (Rank 0) | Evolução Máxima (Rank 30) |
|------------------|----------------------|---------------------------|
| **Vida (Saúde)** | 150 | **450** |
| **Escudo**       | 100 | **300** |
| **Armadura**     | 100 | 100 |
| **Energia**      | 100 | **150** |
| **Vel. Sprint**  | 1.15 | 1.15 |

> **Polaridades Inatas Ocultas:** 2x Naramon (Traço -)
> **Slot de Aura Inata:** Naramon (Traço -)

## 🛠️ Build — Warframe — Segunda Mente


Os guias avançados centralizam no uso da mecânica do Warframe atrelada à invisibilidade defensiva enquanto priorizam melhorias ofensivas em Dano Verdadeiro. O end-game prescinde normalmente de mods massivos de resiliência e saúde crua. O viés ideal exige o aumento contínuo no status de Força (Strength) somado à estabilidade contínua entre as pausas automáticas das mecânicas ativas de execuções.

#### 🎛️ O Arsenal Essencial e Aquisições Core

| Ferramenta / Mod / Arcano                                | Categoria Original | Efeito Funcional da Configuração                                                                                                                                                          | Como Obter                                                                                                                                                                 |
| -------------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[[mods/fatal_teleport.md\|Fatal Teleport]]**           | Mod de Ampliação   | Habilita animações passivas e automáticas de execuções (*Finishers*) na Habilidade 3 e concede base aditiva de +200% de dano.                                                             | Associações dos Sindicatos Nativos (*[[lore/faccoes/sindicatos/veu_vermelho.md\|Véu Vermelho]]* ou *[[lore/faccoes/sindicatos/arbitros_de_hexis.md\|Árbitros de Hexis]]*). |
| **[[mods/rising_storm.md\|Rising Storm]]**               | Mod de Ampliação   | Permite aos clones invocados pela Habilidade 4 contribuírem ativamente com rebatidas no "Medidor de Combo Corpo A Corpo".                                                                 | Associações dos Sindicatos Nativos (*[[lore/faccoes/sindicatos/veu_vermelho.md\|Véu Vermelho]]* ou *[[lore/faccoes/sindicatos/arbitros_de_hexis.md\|Árbitros de Hexis]]*). |
| **[[mods/transient_fortitude.md\|Transient Fortitude]]** | Mod Corrompido     | Intensifica significativamente a Força de Habilidade bruta com sacrifício tático associado na estatística da Duração de Habilidades.                                                      | Abordagens dentro dos *Cofres Estelares ([[locais/deimos.md\|Deimos]] Vaults)* e transações em platina.                                                                    |
| **[[mods/arcane_trickery.md\|Arcane Trickery]]**         | Aprimoramento      | Garante que todas as execuções instintivas apliquem porcentagem limpa e passiva (15% chance por abate) de adicionar sobrecarga de **invisibilidade orgânica absoluta de 30s de duração**. | Conclusões primárias nos abates de bestas Eidolons em [[locais/open-worlds/cetus.md\|Cetus]] ou Trocas comerciais.                                                                        |

## 🧬 Subsunção e Acoplagem do Helminte — Warframe — Segunda Mente


**Poder Cedido Base (Doação [[sistemas/helminte.md|Helminte]]):** **Shuriken**. Com a infecção e o descarte permanente de uma réplica do chassi na Enfermaria do Helminth da escotilha local, essa habilidade modular de atiradores perfurantes limpos está aberta para incorporação transversal de qualquer outro *warframe* na carga.

## 🔗 Terrenos de Atuação, Sinergia e Lâminas Reais — Warframe — Segunda Mente


#### 📍 Compatibilidade de Modalidades de Guerra:

* **Incursões End-Game Solo (Aço, [[missoes/exterminio.md|Extermínios]], [[missoes/sobrevivencia.md|Sobrevivência]]):** Considerável força e sobrevivência inata devida à invisibilidade e capacidade de escalonar "Damage real", ultrapassando defesas ativas de inimigos ultra blindados ([[sistemas/caminho_de_aco.md|Caminho de Aço]]).
* **Alvos Nativos Base (Assassinato/Hunt):** Utilidade crítica e cirúrgica limpa para destruir [[lich_de_kuva|Líches de Kuva]] ou [[chefes|Chefões]] robustos pela facilidade pura de penetrar o bloqueio da vida deles nativamente na fase orgânica de embate.
* **Contra-Indicação (Missões de Protetor Estático):** Fragilidade alta constatada para missões prolongadas focadas puramente na proteção de equipamentos desarmados abertos ao fogo cruzado, como Célio de Criogenia de [[missoes/defesa.md|Defesas]] ou Extratores ([[missoes/escavacao.md|Escavação]]), já que ele não abrange barreiras espaciais.

#### 🤝 Sinergia em Time:

* **[[warframes/banshee.md|Banshee]] (Meta Primordial Subsunção):** A utilidade cruzada com "Silence" (Silêncio) escalona drasticamente a utilidade. Se aliado à tática de esquadrão, a habilidade propõe paralisia. Injetada no painel modular dentro das rotas de Ash, essa adição de atordoamento propaga diretamente nas cópias animadas passivas, **acrescentando passivos fixos pesados de +300% de bônus adicional bruto em Finishers** contínuos durante os ciclos repetitivos de "Blade Storm".
* **[[warframes/harrow.md|Harrow]] / [[warframes/nova.md|Nova]]:** Aplicam efeitos passivos utilitários como contenção maciça ([[warframes/harrow.md|Harrow]]) ou lentidão massiva pesada ([[warframes/nova.md|Nova]]) na fenda dos corredores, dando mais espaço estático confortável para posicionamentos do extermínio orgânico limpo de Ash no fluxo biológico da partida regular. 

#### ⚔️ Conexões Canônicas com O Arsenal Furtivo:

O design do personagem invoca nativamente a associação canônica da classe original de ninjas aos atributos base em combates focados de Katanas, **[[armas/nikana.md|Nikanas]]** ou Lâminas Pequenas Brutais Furtivas. Usos extensivos com **[[armas/adagas.md|Adagas]]** modulares acopladas puramente na progressão de bônus diretos com a estampa mod de "[[mods/covert_lethality.md|Covert Lethality]]" garantem execuções completas e diretas de classe letal nos alvos atingidos. Além do alcance orgânico, snipers clássicas como a **[[armas/vectis_prime.md|Vectis Prime]]** cumprem com naturalidade as exigências visuais base como arsenal de tiro único seguro e furtivo na operação contínua coberta pelas próprias restrições densas estéticas e cinzas da bomba de fumaça primária dele (Smoke Screen).

## 🎨 Apresentação e Estilização (Fashion Frame) — Warframe — Segunda Mente


A estilização visual de Ash frequentemente acompanha temas centrados nos arquétipos de ninjas, operativos furtivos e assassinos cibernéticos, seguindo o rigor de sua anatomia base esguia e utilitária. 

#### Skins e Geometrias de Destaque
* **[[cosmeticos/skins/koga_skin.md|Koga Skin]] (Deluxe):** Implementa uma silhueta fundamentada em vestimentas tradicionais de *shinobis*. Remove as armaduras protuberantes em favor de ataduras estéticas, faixas e remodelação total do chassi. 
* **[[cosmeticos/skins/shroud_skin.md|Shroud Skin]] (Deluxe):** Altera a base para o formato de um guerreiro oriental velado, incorporando mantos texturizados e geometria agressiva com contornos de monges-assassinos.
* **Skins [[cosmeticos/skins/tennogen.md|TennoGen]] (Baihu, Tsukuyomi e Carabid):** Opções originadas e validadas pela comunidade que aprimoram traços de anatomia felina (tigre) ou reforçam o exoesqueleto natural para lembrar carapaças insetoides orgânicas densas com fendas iluminadas.

#### Padrões de Cores e Paletas Recomendadas
A distribuição de canais de customização no modelo base do Ash distribui suas colorações principais em largos blocos de tecido liso e armadura fosca.
* **Camuflagem e Fundo Tático (Cores Base):** A estética primordial e de mais fácil combinação envolve tons puros e variados de Preto, Cinza-Carvão e Ouro Branco Escurecido *(Paletas: [[cosmeticos/paletas/smoke_colors.md|Smoke Colors]] ou [[cosmeticos/paletas/classic.md|Classic]])* aplicados nas camadas Primárias, Secundárias e Terciárias para simular a discrição exigida pelo personagem.
* **Canais de Emissão (Energia):** Dada a inclinação anatômica aos danos de perfuração e habilidades umbilicais ao fogo, aplicar fendas de emissividade focadas em Vermelho Sangue *(Paleta [[cosmeticos/paletas/halloween.md|Halloween]])* ou Tons Cianos *(Paleta [[cosmeticos/paletas/dojo.md|Dojo]] ou [[cosmeticos/paletas/orokin.md|Orokin]])* gera alto contraste visual adequado ao tema.
* **Adornos e Fixadores (Acentos):** Detalhes minúsculos de fivelas e pinos metálicos reagem consistentemente aos tons prateados neutros ou cobre esmaecido, evitando saturações que anulem o apelo militarista focado na neutralidade corporal.

----------------------------------------

## Seção: warframes\regular — Warframe — Segunda Mente

### 📄 arquivo: atlas.md

> *"Este é Atlas, o lutador, o forte. Mover montanhas não é uma tarefa fácil, Tenno. Atlas resiste."* — **Códice, Warframe.com**

## 📖 História e Códice — Warframe — Segunda Mente


A descoberta de Atlas remonta à aniquilação de uma ameaça cataclísmica direcionada à [[locais/terra.md|Terra]]. Durante os tempos remotos do [[lore/faccoes/orokin.md|Império Orokin]], a seita paramilitar fanática conhecida como [[lore/faccoes/temple_telamon.md|Temple Telamon]] redirecionou a trajetória de um asteroide massivo para colidir com o planeta, em prol de suas profecias apocalípticas de renascimento. Como último recurso tático para interceptar a estrutura geológica, os [[lore/faccoes/orokin.md|Orokin]] empregaram Atlas. 

Utilizando sua proficiência cinética e manipulação elementar terrena, Atlas interceptou o asteroide de forma solitária. Direcionando frequências de ressonância através de suas formações tectônicas, ele induziu a desintegração estrutural total do corpo celeste, neutralizando a insurgência Telamon definitivamente. Suas escórias estruturais foram posteriormente retidas no domínio de [[locais/eris.md|Eris]], caindo sob o controle biológico da [[lore/faccoes/infestados.md|Infestação]].

## 🎮 Visão Geral e Gameplay — Warframe — Segunda Mente


A arquitetura biomecânica de Atlas foi desenhada para atuar como mitigador contínuo de dano e força impositiva em engajamentos de área fechada (Brawler). A base sistêmica operacional atua otimizando instâncias de sobrevivência a partir da aglomeração retroalimentativa de blindagem rochosa ([[mecanicas/rubble.md|Rubble]]). Aplicando índices devastadores através da otimização corpo a corpo (mecânica modular de contágio de atrito e [[mecanicas/stat_sticks.md|Stat Sticks]]), o chassi subjuga zonas de impacto ao aplicar controle restritivo via fossilização progressiva dos oponentes em seu perímetro visual.

Estes parâmetros atestam o chassi de Atlas como uma escolha primária no engajamento massivo de hordas blindadas em instâncias de durabilidade extrema, como incursões no [[sistemas/caminho_de_aco.md|Caminho de Aço]], consolidando-se como um baluarte ofensivo intransponível cuja eficiência escala passivamente com a aniquilação territorial contínua.

## 💡 Curiosidades (Trivia) — Warframe — Segunda Mente


- Desenvolvido em ambientes de laboratório de *game design* da [[empresas/digital_extremes.md|Digital Extremes]] sob a alcunha referencial "Brawler", terminologia estruturante ainda rastreável nas nomenclaturas de pastas binárias do jogo.
- A natureza progressiva da paralisação induzida reflete as origens conceituais do mito basilar da [[lore/referencias/medusa.md|Górgona Medusa]] da cosmologia grega. A passiva inamovível espelha [[lore/referencias/antaeus.md|Antaeus]], combatente legendário indestrutível enquanto mantivesse convergência direta com o substrato fixo da terra.
- Consolida o escopo de primeiro Warframe do inventário original projetado desde o lançamento primário ostentando sinergia sistêmica canônica com um arsenal físico próprio listado: a arma [[armas/tekko.md|Tekko]].

## 🔮 Habilidades — Warframe — Segunda Mente


* **Passiva (Imobilidade Tectônica):** Retém imunidade técnica absoluta a efeitos externos que promovam impactos de [[mecanicas/derrubada.md|Derrubada (Knockdown)]] ou paralisia gravitacional enquanto os sensores de nivelamento permanecerem contíguos a estratos rígidos da superfície.

* **1. Landslide (25 Energia):** Exerce propulsão avassaladora de deslocamento instantâneo resultando em ruptura física extrema por esmagamento. Reativações sequenciais acionam matrizes de impacto em progressão matemática geométrica de agressividade e raio de influência, decaindo as taxas exigidas da reserva de energia em cada novo engate acoplado.

* **2. Tectonics (50 Energia):** Condensa compostos do relevo adjacente na formulação estática de uma placa geométrica obstrutiva intransponível. Estimulações reativas da parede originam instabilidade estrutural, convertendo-a em projétil rochoso invasivo capaz de penetração múltipla de hordas invasoras em formato de esfera rolante.

* **3. Petrify (75 Energia):** Submete hordas em zona angular frontal a fluxos eletromagnéticos enrijecedores, comprometendo todas as malhas protetoras biológicas até a solidificação fóssil total e escalonando danos colaterais induzidos. Resíduos desintegrados de inimigos nesta contenção provêem sedimentos que curam o vetor principal ou convertem-se em carapaça ativa.

* **4. Rumblers (100 Energia):** Mobiliza acúmulos aglomerados do cenário em dois construtos táticos automatizados e perigosos. Estas unidades agem capturando focos isolados de opositores, irradiando restrições motoras nos vetores alvejados. Ao concluírem suas operações geológicas, os construtos colapsam em acúmulos massivos de rochas protetoras consumíveis.

## 🌍 Onde Conseguir — Warframe — Segunda Mente


#### Tabela de Fabricação Base

| Componente     | Fonter/Drop                                                        | Planeta        | Créditos | Recursos Extraordinários                                                                         | Tempo |
| -------------- | ------------------------------------------------------------------ | -------------- | -------- | ------------------------------------------------------------------------------------------------ | ----- |
| Diagrama Maior | Missão [[lore/jornadas/the_jordas_precept.md\|The Jordas Precept]] | [[locais/eris.md\|Eris]] | 50.000   | 100.000x [[recursos/alloy_plate.md\|Placa de Liga]]                                              | 72h   |
| Neurovisor     | Assassinato [[NPCs/chefes/jordas_golem.md\|Jordas Golem]]          | [[locais/eris.md\|Eris]] | 15.000   | 1.500x [[recursos/polymer_bundle.md\|Pacote de Polímero]], 1x [[recursos/sensores_neurais.md\|Sensor Neural]]                      | 12h   |
| Chassi         | Assassinato [[NPCs/chefes/jordas_golem.md\|Jordas Golem]]          | [[locais/eris.md\|Eris]] | 15.000   | 1.000x [[recursos/nano_spores.md\|Nano Esporos]], 2x [[recursos/extrato_de_nitain.md\|Extrato de Nitain]]                           | 12h   |
| Sistemas       | Assassinato [[NPCs/chefes/jordas_golem.md\|Jordas Golem]]          | [[locais/eris.md\|Eris]] | 15.000   | 1.500x [[recursos/polymer_bundle.md\|Pacote de Polímero]], 3x [[recursos/neurodes.md\|Neurodes]] | 12h   |

#### Vias Alternativas de Obtenção:
A matriz de Diagrama do núcleo arquitetônico é restaurada após falhas vitais no diretório isolado de [[NPCs/cephalon_simaris.md|Cephalon Simaris]]. Aquisições integrativas modulares da arquitetura se fazem operacionais através do preenchimento semanal em fases na dinâmica de [[sistemas/o_circuito.md|O Circuito]] atrelados à paisagem abstrata originária de [[locais/duviri.md|Duviri]]. Operações secundárias de intercâmbio rápido permanecem liberadas via negociação de contrato baseada em [[recursos/platina.md|Platina]].

## 📊 Estatísticas Matemáticas e Sobrevivência (Rank 0 -> 30) — Warframe — Segunda Mente


| Atributo Oficial | Status Base (Rank 0) | Evolução Máxima (Rank 30) |
|------------------|----------------------|---------------------------|
| **Vida (Saúde)** | 100 | **270** |
| **Escudo**       | 100 | **270** |
| **Armadura**     | 475 | **475** |
| **Energia**      | 150 | **175** |
| **Vel. Sprint**  | 0.9 | 0.9 |

> **Polaridades Inatas Ocultas:** Traço D (Vazarin), Traço - (Naramon), Traço V (Madurai)
> **Slot de Aura Inata:** Traço V (Madurai)

## 🛠️ Build — Warframe — Segunda Mente


Os guias avançados centralizam no uso da mecânica do Warframe atrelada à fossilização defensiva e acúmulo de blindagem ([[mecanicas/rubble.md|Rubble]]) enquanto priorizam multiplicadores brutos de corpo-a-corpo. O end-game prescinde do balanceamento passivo defensivo garantido, migrando para sobreposições rigorosas para intensificar o impacto brutal da habilidade fundamental. O viés ideal exige foco direcionado em [[mecanicas/forca_de_habilidade.md|Força de Habilidade]] combinada à sinergia do arsenal através do uso meticuloso de [[mecanicas/stat_sticks.md|Stat Sticks]] customizados.

#### 🎛️ O Arsenal Essencial e Aquisições Core

| Ferramenta / Mod / Arcano                                | Categoria Original | Efeito Funcional da Configuração                                                                                                                                                             | Como Obter                                                                                                                                                                      |
| -------------------------------------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[[mods/path_of_statues.md\|Path of Statues]]**         | Mod de Ampliação   | Injeta fluídos petrificantes rastreáveis nas trilhas deixadas pela propulsão do Landslide, automatizando a contenção tática sem gasto adicional.                                             | Associações dos Sindicatos Nativos (*[[lore/faccoes/sindicatos/cephalon_suda.md\|Cephalon Suda]]* ou *[[lore/faccoes/sindicatos/veu_vermelho.md\|Véu Vermelho]]*).              |
| **[[mods/rubble_heap.md\|Rubble Heap]]**                 | Mod de Ampliação   | Anula o limite gravitacional de decaimento natural da blindagem extra. O custo do Landslide decai a zero e adquire velocidade pura extra após o teto de escombros batido.                    | Associações dos Sindicatos Nativos (*[[lore/faccoes/sindicatos/cephalon_suda.md\|Cephalon Suda]]* ou *[[lore/faccoes/sindicatos/veu_vermelho.md\|Véu Vermelho]]*).              |
| **[[mods/blind_rage.md\|Blind Rage]]**                   | Mod Corrompido     | Intensifica drasticamente a [[mecanicas/forca_de_habilidade.md\|Força de Habilidade]] com elevado sacrifício sobre a [[mecanicas/eficiencia.md\|Eficiência]] geral operacional.                                                           | Abordagens dentro dos *Cofres Estelares ([[locais/deimos.md\|Deimos]] Vaults)* e transações comerciais puras com platina.                                                       |
| **[[mods/arcane_avenger.md\|Arcane Avenger]]**           | Aprimoramento      | Garante que o recebimento contínuo de dano físico nativo incorra em acréscimos diretos e brutos massivos (+45%) na [[mecanicas/chance_critica.md\|Chance Crítica]] corporificante, maximizando agressões primárias.         | Capturas e Derrotas das bestas Eidolons ultra-resistentes na matriz aberta de [[locais/cetus.md\|Cetus]] ou em negociações p2p orgânicas entre contratantes.                    |

## 🧬 Subsunção e Acoplagem do Helminte — Warframe — Segunda Mente


**Poder Cedido Base (Doação [[sistemas/helminte.md|Helminte]]):** **Petrify**. O algoritmo sistêmico de desestabilização biomolecular contida é permanentemente cimentado pela Helminte à extração modular livre, compartilhando sua vasta utilidade de controle impositivo de grupo maciço frontal e petrificação garantida para a infusão do painel modular tático em outros construtos e chasises adjacentes.

## 🔗 Terrenos de Atuação, Sinergia e Golems Reais — Warframe — Segunda Mente


#### 📍 Compatibilidade de Modalidades de Guerra:

* **Incursões Fixas e Defesas (Zonas Estáticas, [[missoes/defesa.md|Defesa]]):** Considerável viabilidade como baluarte graças às concentrações de massas tectônicas geográficas e de obstrução puras (*Tectonics*) e golens de patrulha perimetral indestrutíveis (*Rumblers*).
* **Sobrevivências de Altíssimo Desgaste ([[sistemas/caminho_de_aco.md|Caminho de Aço]]):** Potência cirúrgica contra falanges e exércitos inteiros graças ao acúmulo contínuo sistêmico de sobrevida passiva e atrito físico propiciada pelo foco unicamente devotado em abates corporais massivos de curto alcance (via Landslide).
* **Contra-Indicação (Missões de Movimentos Rápido ou Abordagens):** Extrema e notória inadequabilidade utilitária tática para missões ativas baseadas que dependam de velocidade abstrata veloz natural e fugas temporais como Operações em [[missoes/espionagem.md|Espionagem]], devido fundamentalmente à completa ausência de mecânicas furtivas baseadas dentro do chassi pesado.

#### 🤝 Sinergia em Time:

* **[[warframes/wisp.md|Wisp]] / [[warframes/citrine.md|Citrine]]:** Impõem em zona contígua passiva seus suportes vitais focados puramente de base protetora ou amplificadores orgânicos para durabilidade celular que catalisam as propulsões terrestres do Atlas frente a exércitos de contenção extremamente densos e blindados sem recuos obrigatórios.
* **[[warframes/nidus.md|Nidus]] (Via Larva):** Atribui a conglomeração estendida de todos os oponentes num ponto focal. Essa aproximação via atração geométrica encurraladora compila um alvo fácil, tornando viável esmagar e apagar agrupamentos maciços brutalmente compactados simultaneamente utilizando-se de apenas a onda em arco expansivo central do Landslide.

#### ⚔️ Conexões Canônicas com O Arsenal Furtivo/Primordial:

Em observância estrutural dos primórdios operacionais originais do design focado em combate aproximado bruto, é possível atrelar o *status* da classe a partir do manejo imperativo orgânico de suas armas corpo-a-corpo focadas em furação (soqueiras perfurantes): **[[armas/tekko.md|Tekko]]** ou a variação superior letal natural de **[[armas/tekko_prime.md|Tekko Prime]]**. Esta escolha de infraestrutura resulta sistêmica organicativa base provendo de estampa acréscimos brutos de atributos puramente (+6% status adicional limpo base), maximizando a sinergia indissolúvel das lutas corpo-a-corpo sem interferência impura no meta game.

## 🎨 Apresentação e Estilização (Fashion Frame) — Warframe — Segunda Mente


A estilização e apresentação estética de visual do lorde das pedras frequentemente espelha e amplifica representações calcárias base de lendas de geodos inertes intocados mantendo fiel às concepções originais brutas originárias estritamente orgânicas à armadura de um pugilista inabalável denso focado.

#### Skins e Geometrias de Destaque
* **[[cosmeticos/skins/karst_skin.md|Karst Skin]] (Deluxe):** Transfigura o chassi para a versão visual pautada na geologia mineral, entregando os aspectos afiados característicos idênticos a joias ornamentais e fraturas geométricas. Transforma esteticamente os golens de *Rumblers* (habilidade quatro) em monstros ametistas completos, solidificando o porte de golem de alta-fidelidade perfeitamente cristalizado.
* **Skins [[cosmeticos/skins/tennogen.md|TennoGen]] (Arhat, Monolith e Shikoro):** Pacotes idealizados exclusivamente pelos designes primários da plataforma em realçar a estética estoica maciça densa. Focada sobretudo em proteger as omoplatas em blindagens inteiriçadas compostas com chifres na anatomia craniana sem omissões fúteis.

#### Padrões de Cores e Paletas Recomendadas
O escoamento das pigmentações principais focam em coloração plana sem verniz focado unindo ao tema opressivo do basalto na terra fria.
* **Ambientação Mineral e Geológica (Cores Base):** Aspecto geológico de colorações de matiz basáltico natural orgulhoso rochoso providas através de conjuntos de matriz originárias como [[cosmeticos/paletas/crepusculo.md|Crepúsculo]] ou a aba natural [[cosmeticos/paletas/grinner.md|Grineer]]. Transmite a imutabilidade militar do granito bruto.
* **Canais de Emissão (Energia):** Dada toda afinidade original com a fundação magmática que aquece por dentro. Opções como vulcânico âmbar (*Paleta [[cosmeticos/paletas/halloween.md|Halloween]]* ou tons áureos da [[cosmeticos/paletas/orokin.md|Orokin]]) ressaltam o fervor que pulsa no núcleo incandescente dos seus golens recém-erguidos.
* **Adornos Temáticos (Acentos):** Recomenda-se rigorosamente que peças complementares não quebrem o rigor militar purista focado na neutralidade corporal opressiva pesada da placa peitoral. Emprega-se preferencialmente de maneira canônica fiel o uso solene anexado com clareza da manta estrutural **[[cosmeticos/syandanas/stratum.md|Stratum Syandana]]** exclusiva projetada e recomendada nativamente junto ao lutador.

----------------------------------------

## Seção: warframes\regular — Warframe — Segunda Mente

### 📄 arquivo: excalibur.md

# Excalibur

> [!info] Visão Geral
> Warframe inicial balanceado com espada exaltada poderosa

## 🌍 Onde Conseguir — Warframe — Segunda Mente

- Fonte: Assassination (Lieutenant Lech Kril) ou Escolha Inicial
- Drop location: War, Marte
- Blueprint: Mercado (35,000 Créditos)

## 🔮 Habilidades — Warframe — Segunda Mente


| # | Nome | Custo | Descrição |
|---|------|-------|-----------|
| Passiva | Swordsmanship | — | +10% de Velocidade de Ataque e Dano ao usar espadas (Longswords, Dual Swords, Nikanas, Rapiers). |
| 1 | Slash Dash | 25 | Avança entre inimigos com a Exalted Blade, causando dano. |
| 2 | Radial Blind | 50 | Emite um flash brilhante, cegando inimigos próximos. |
| 3 | Radial Javelin | 75 | Lança dardos nos inimigos, causando dano massivo. |
| 4 | Exalted Blade | 25 inicial | Evoca uma espada de puro brilho que atira ondas de energia cortante. |

## 📊 Stats Base — Warframe — Segunda Mente


| Stat | Valor |
|------|-------|
| HP | 100 (300 no Nv 30) |
| Escudo | 100 (300 no Nv 30) |
| Armadura | 250 |
| Energia | 100 (150 no Nv 30) |
| Sprint | 1.0 |
| Polaridades | 1 Madurai (V), 1 Vazarin (D) |

## 🛠️ Build — Warframe — Segunda Mente

> Preencher após obter o Warframe.
- [ ]

## 🔗 Relacionados — Warframe — Segunda Mente

- Sinergias: Mag (Magnetize + Radial Javelin), Volt (Speed)
- Recursos necessários: Plástidos, Célula Orokin, Rubedo, Restos
- Quests relacionadas: O Despertar (Tutorial), O Sacrifício (relacionada ao Excalibur Umbra)

----------------------------------------

## Seção: warframes\regular — Warframe — Segunda Mente

### 📄 arquivo: volt.md

# Volt

> [!info] Visão Geral
> DPS elétrico versátil e escudo condutor

## 🌍 Onde Conseguir — Warframe — Segunda Mente

- Fonte: Pesquisa do Dojo (Laboratório Tenno) ou Escolha Inicial
- Drop location: Dojo - Laboratório Tenno
- Blueprint: Mercado (35,000 Créditos) ou Dojo

## 🔮 Habilidades — Warframe — Segunda Mente


| # | Nome | Custo | Descrição |
|---|------|-------|-----------|
| Passiva | Eletricidade Estática | — | Movimentar-se pelo solo acumula carga elétrica, aplicável ao próximo ataque (até 1000 de dano extra). |
| 1 | Shock | 25 | Dispara um projétil elétrico que causa dano e se encadeia entre inimigos próximos. |
| 2 | Speed | 50 | Aumenta drasticamente a velocidade de movimento e ataque corpo a corpo dele e dos aliados. |
| 3 | Electric Shield | 50 | Posiciona um escudo de energia. Tiros aliados que o atravessam ganham dano elétrico e crítico. |
| 4 | Discharge | 100 | Paralisa inimigos com uma descarga elétrica que danifica e choca alvos próximos (Chain-Lightning). |

## 📊 Stats Base — Warframe — Segunda Mente


| Stat | Valor |
|------|-------|
| HP | 100 (300 no Nv 30) |
| Escudo | 150 (450 no Nv 30) |
| Armadura | 15 |
| Energia | 100 (150 no Nv 30) |
| Sprint | 1.0 |
| Polaridades | 2 Naramon (Traço) |

## 🛠️ Build — Warframe — Segunda Mente

> Preencher após obter o Warframe.
- [ ]

## 🔗 Relacionados — Warframe — Segunda Mente

- Sinergias: Mag (Shock + Magnetize para área danosa), Titania/Gauss (Speed)
- Recursos necessários: Placas de Liga, Pacote de Polímero, Célula Orokin, Módulo de Controle
- Quests relacionadas: O Despertar (Tutorial)

----------------------------------------

## Seção: warframes\regular — Warframe — Segunda Mente

### 📄 arquivo: mag.md

# Mag

> [!info] Visão Geral
> Controle magnético: atrai projéteis e implode escudos

## 🌍 Onde Conseguir — Warframe — Segunda Mente

- Fonte: Assassination (The Sergeant) ou Escolha Inicial
- Drop location: Iliad, Fobos
- Blueprint: Mercado (25,000 Créditos)

## 🔮 Habilidades — Warframe — Segunda Mente


| # | Nome | Custo | Descrição |
|---|------|-------|-----------|
| Passiva | Atração Magnética | — | Atrai drops (recursos, mods, munição) ao realizar um Bullet Jump. |
| 1 | Pull | 25 | Puxa inimigos em direção à Mag, causando dano e derrubando-os. |
| 2 | Magnetize | 50 | Cria um campo magnético ao redor de um alvo, prendendo inimigos e atraindo projéteis. |
| 3 | Polarize | 75 | Emite um pulso que drena escudos e armaduras inimigas, restaurando os escudos dos aliados. |
| 4 | Crush | 100 | Magnetiza os ossos dos inimigos próximos, levantando-os e esmagando para causar dano. |

## 📊 Stats Base — Warframe — Segunda Mente


| Stat | Valor |
|------|-------|
| HP | 75 (225 no Nv 30) |
| Escudo | 150 (450 no Nv 30) |
| Armadura | 65 |
| Energia | 175 (262.5 no Nv 30) |
| Sprint | 1.0 |
| Polaridades | 2 Naramon (Traço), Aura: Naramon (Traço) |

## 🛠️ Build — Warframe — Segunda Mente

> Preencher após obter o Warframe.
- [ ]

## 🔗 Relacionados — Warframe — Segunda Mente

- Sinergias: Excalibur (Radial Javelin + Magnetize), Armas de projétil (ex: Lanka, Nataruk)
- Recursos necessários: Placas de Liga, Circuitos, Módulo de Controle, Plástidos
- Quests relacionadas: O Despertar (Tutorial)

----------------------------------------

## Seção: warframes\primes — Warframe — Segunda Mente

### 📄 arquivo: ash_prime.md

> *"Especialista na arte militar da distração e subterfúgio, Ash Prime ataca não visto, mas deixa para trás um rastro de letalidade inconfundível. Uma relíquia letal e aprimorada de uma era distante."* — **Códice, Warframe.com**

## 📖 História e Códice — Warframe — Segunda Mente


Ash Prime é a variante ancestral e militarmente otimizada do chassi [[warframes/ash.md|Ash]] original, manufaturada durante o ápice do [[lore/faccoes/orokin.md|Império Orokin]]. Operava como o carrasco e a lâmina silenciosa dos Executores, empregado taticamente para fins de eliminação de alvos de alto valor e desestabilização de frentes sem ativar protocolos de alerta limitantes.

## 🎮 Visão Geral e Gameplay — Warframe — Segunda Mente


O núcleo tático deste Warframe repousa no dano focado contínuo e imunidade tática através de furtividade ativa. Ash Prime anula alvos singulares extremamente blindados em conteúdos de alto nível (como o [[sistemas/caminho_de_aco.md|Caminho de Aço]]) ignorando a camada física defensiva via status inato de Sangramento (Corte). Exige precisão e controle operante de energia, priorizando extermínios rápidos e isolamento de ameaças sistêmicas no campo de batalha em abordagens majoritariamente solo.

## 💡 Curiosidades (Trivia) — Warframe — Segunda Mente


Possui o design do capacete com inspiração militar restrita voltada no tradicional "Kabuto" dos samurais japoneses originais.

Apresenta caligrafia Orokin gráfica nativa em seu chassi equivalente à identificação serial: *"Tenno Model 24N - Serial 147H"*.

## 🔮 Habilidades — Warframe — Segunda Mente


*   **Passiva (Hemorragia):** Efeitos de status Cortante (*Slash*) infligidos de qualquer fonte originada por Ash recebem **25% de Dano Adicional** e um **incremento de 50% em sua duração base**.

*   **1. Shuriken (25 Energia):** Dispara projéteis teleguiados de perfil afiado. Ao contato físico, empala e impõe garantidamente status punitivo severo de sangramento na integridade estática do alvo. 

*   **2. Smoke Screen (35 Energia):** Detonação de distração ao solo imediato. Interrompe ativamente quadros agressivos em um raio curto de atuação (Atordoamento base) e garante furtividade momentânea militar não-rastreável por unidades orgânicas ou robóticas.

*   **3. Teleport (25 Energia):** Relocação vetorial instantânea orientada para a geometria física do alvo travado em tela. Realiza uma aproximação letal tática, frequentemente atrelando finalizadores de retalhação automatizados (recupera parcialmente o custo base de energia em eliminações singulares).

*   **4. Blade Storm (12 Energia por Marcação):** Invoca hologramas sombrios de clones operantes que escalam independente do estado atual do chassi mestre para varredura de área. Marca alvos múltiplos na visão. A execução ignora inteiramente e de forma absoluta defesas de armaduras pesadas aplicando dano de Sangramento real puro.

## 🌍 Onde Conseguir — Warframe — Segunda Mente


O plano Prime exige obtenção exclusiva de diagramas por partições de Relíquias abertas no [[sistemas/prime_vault.md|Cofre Primordial]] (Prime Vault) ou Resgate fixo por Ayas via [[sistemas/ressurgencia_prime.md|Ressurgência Prime]]. O projeto central é manufaturado em etapas parciais físicas.

#### Tabela de Fabricação Base

| Componente | Missões de Drop de Diagrama (Relíquias) | Requisitos Materiais e [[recursos/creditos.md\|Créditos]] | Tempo de Forja |
| :--- | :--- | :--- | :--- |
| **Warframe Completo** | [[sistemas/reliquias.md\|Axi I3]], [[sistemas/reliquias.md\|Meso V2]] | 25.000 [[recursos/creditos.md\|Créditos]] + 1 [[recursos/celula_orokin.md\|Célula Orokin]] + **Sistemas, Chassi e Neurovisor** | 72 Horas |
| **Neurovisor** | [[sistemas/reliquias.md\|Lith V7]], [[sistemas/reliquias.md\|Neo N4]] | 15.000 [[recursos/creditos.md\|Créditos]] + 150 [[recursos/placas_de_liga.md\|Placas da Liga]], 2 [[recursos/sensores_neurais.md\|Sensores Neurais]], 150 [[recursos/plastidos.md\|Plásticos]], 500 [[recursos/rubedo.md\|Rubedo]] | 12 Horas |
| **Chassi** | [[sistemas/reliquias.md\|Meso C1]], [[sistemas/reliquias.md\|Meso S3]] | 15.000 [[recursos/creditos.md\|Créditos]] + 1 [[recursos/galio.md\|Gálio]], 1000 [[recursos/nano_esporos.md\|Nano Esporos]], 300 [[recursos/rubedo.md\|Rubedo]] | 12 Horas |
| **Sistemas** | [[sistemas/reliquias.md\|Axi K12]], [[sistemas/reliquias.md\|Neo N3]] | 15.000 [[recursos/creditos.md\|Créditos]] + 1 [[recursos/modulo_de_controle.md\|Módulo de Controle]], 1 [[recursos/celula_orokin.md\|Célula Orokin]], 500 [[recursos/sucata.md\|Sucata]], 220 [[recursos/ferrite.md\|Ferrite]] | 12 Horas |

#### Vias Alternativas de Obtenção:

* **Comércio entre Jogadores (Trade):** Ao invés de abrir relíquias, o jogador pode comercializar os Diagramas do Chassi, Sistemas, Neurovisor ou Diagrama Principal listados no Mercado de Troca com outros Tennos em troca de [[recursos/platina.md|Platina]].
* **[[sistemas/ressurgencia_prime.md|Ressurgência Prime]]:** A aquisição fora da janela convencional acontece por meio da lojista [[varzia|Varzia]] em [[locais/maroos_bazaar.md|Maroo's Bazaar]]. É possível trocar Ayas Regulares para obter as Relíquias trancadas do Cofre, ou adquirir de forma imediata o quadro completo finalizado utilizando Ayas Régias monetizadas (O quadro neste caso já vem acompanhado de um Slot Livrado e um [[sistemas/reator_orokin.md|Reator Orokin]] pré-instalados).

## 📊 Estatísticas Matemáticas e Sobrevivência (Rank 0 -> 30) — Warframe — Segunda Mente


| Atributo Oficial | Status Base (Rank 0) | Evolução Máxima (Rank 30) |
|------------------|----------------------|---------------------------|
| **Vida (Saúde)** | 150 | **455** |
| **Escudo**       | 125 | **365** |
| **Armadura**     | 185 | 185 |
| **Energia**      | 100 | **150** |
| **Vel. Sprint**  | 1.2  | 1.2 |

> **Polaridades Inatas Ocultas:** Naramon (Traço -), 2x Madurai (Traço V)
> **Slot de Aura Inata:** Madurai (Traço V)

## 🛠️ Build — Warframe — Segunda Mente


Os guias avançados centralizam no uso da mecânica do Warframe atrelada à invisibilidade defensiva enquanto priorizam melhorias ofensivas em Dano Verdadeiro. O end-game prescinde normalmente de mods massivos de resiliência e saúde crua. O viés ideal exige o aumento contínuo no status de Força (Strength) somado à estabilidade contínua entre as pausas automáticas das mecânicas ativas de execuções.

#### 🎛️ O Arsenal Essencial e Aquisições Core

| Ferramenta / Mod / Arcano | Categoria Original | Efeito Funcional da Configuração | Como Obter |
| :--- | :--- | :--- | :--- |
| **[[mods/seeking_shuriken.md\|Seeking Shuriken]]** | Mod de Ampliação | Alteração direta da Habilidade 1. Disparos cortantes degradam permanentemente armadura residual. | Origina-se do *[[lore/faccoes/sindicatos/veu_vermelho.md\|Véu Vermelho]]* ou *[[lore/faccoes/sindicatos/arbitros_de_hexis.md\|Árbitros de Hexis]]*. |
| **[[mods/fatal_teleport.md\|Fatal Teleport]]** | Mod de Ampliação | Aprimoramento da Habilidade 3. Adiciona multiplicador automático de +200% de dano finalizador puro. | Origina-se do *[[lore/faccoes/sindicatos/veu_vermelho.md\|Véu Vermelho]]* ou *[[lore/faccoes/sindicatos/arbitros_de_hexis.md\|Árbitros de Hexis]]*. |
| **[[mods/transient_fortitude.md\|Transient Fortitude]]** | Mod Corrompido | Intensifica significativamente a Força de Habilidade bruta com sacrifício tático associado na duração. | Cofres Estelares ([[locais/deimos.md\|Deimos]] Vaults). |

## 🧬 Subsunção e Acoplagem do Helminte — Warframe — Segunda Mente


**Poder Cedido Base (Doação [[sistemas/helminte.md|Helminte]]):** **Shuriken**. Ao interagir no sacrifício, Ash Prime cede nativamente em doação permanente esta habilidade. 
Ao otimizar o próprio chassi no recebimento modular, este exemplar apresenta máxima eficiência absorvendo a injeção mecânica do **Silence** (da [[warframes/banshee.md|Banshee]]) encaixável rotacionalmente, acoplada para ativar multiplicadores de danos atordoando inimigos e protegendo os Clones do *Blade Storm*.

## 🔗 Terrenos de Atuação, Sinergia e Lâminas Reais — Warframe — Segunda Mente


#### 📍 Compatibilidade de Modalidades de Guerra:

*   **Incursões End-Game Solo ([[missoes/exterminio.md|Extermínios]], [[missoes/sobrevivencia.md|Sobrevivência]]):** Considerável força e sobrevivência inata devida à invisibilidade e capacidade de escalonar "Damage real", ultrapassando defesas ativas no [[sistemas/caminho_de_aco.md|Caminho de Aço]].
*   **Caças Furtivas ([[missoes/espionagem.md|Espionagem]], [[missoes/assassinato.md|Assassinato]]):** Performa de maneira autoconclusiva para operações que exigem restrição de alarmes sistêmicos no território.

#### 🤝 Sinergia em Time:

*   **[[warframes/mag.md|Mag]] / [[warframes/nidus.md|Nidus]]:** Expande margens de lucro tático quando apoiado diretamente por atrações espaciais magnéticas estáticas que confinam os alvos para abate facilitado do Blade Storm.
*   **[[warframes/banshee.md|Banshee]]:** A injeção de Silence escala drasticamente a paralisação tática.

#### ⚔️ Conexões Canônicas com O Arsenal Furtivo:

O design militarizado purista do Ash Prime ratifica e invoca a progressão letal no combate focado em lâminas ancestrais cortantes, especialmente o trançado passivo de golpes de **[[armas/nikana.md|Nikanas]]** ou a aplicação cirúrgica de uso de **[[armas/adagas.md|Adagas]]** operando combinadas com o Mod Assassino nato de "[[mods/covert_lethality.md|Covert Lethality]]". No folclore do Lançamento do Cofre Prime, Ash Prime foi visualmente apresentado de forma canônica atrelado ao rifle sniper **[[armas/vectis_prime.md|Vectis Prime]]** e em suporte tático robótico com o sentinela utilitária **[[companheiros/carrier_prime.md|Carrier Prime]]**, cristalizando assim o estilo militar estrito e autônomo (não necessitando de drops de munição no terreno e atirando oculto na fumaça).

## 🎨 Apresentação e Estilização (Fashion Frame) — Warframe — Segunda Mente


O rigor base do chassi Ash Prime compele a arquétipos letais sombrios em fardamentos militarizados restritos, favorecendo intensamente a utilização elementar de paletas monocromáticas.

#### Skins e Geometrias de Destaque
*   **[[cosmeticos/skins/koga_skin.md|Ash Koga]] (Deluxe):** Aborda silhuetas exclusivas com reminiscência limpa a estéticas asiáticas marciais ancestrais.
*   **Skins [[cosmeticos/skins/tennogen.md|TennoGen]]:** Opções originadas pela comunidade que garantem maior customização orgânica ou reforço tático visual sobre as camadas da versão Prime.

#### Padrões de Cores e Paletas Recomendadas
Aconselha-se tonalidades absolutas pretas perante cinzas chumbo estáticos operacionais (Paleta **[[cosmeticos/paletas/smoke_colors.md|Smoke Colors]]**) contrastados por canais de energia puramente alaranjados densos (Paleta **[[cosmeticos/paletas/halloween.md|Halloween]]**), simulando processos ininterruptos de queimas de brasas de carvão vegetal.

----------------------------------------

## Seção: armas — Warframe — Segunda Mente

### 📄 arquivo: _Armas _Indice.md

# Armas — Índice

> [!quote]
> *"Uma arma é apenas metal. O Tenno que a empunha é o que a torna letal."*


## 📊 Visão Geral — Warframe — Segunda Mente


Armas em Warframe são o principal meio de combate do Tenno. Dividem-se em quatro categorias de slot: **Primária**, **Secundária**, **Branca (Melee)** e **Archwing**. Cada slot é independente — o jogador equipa uma de cada tipo simultaneamente (exceto Archwing, usado apenas em zonas específicas).

O poder real de uma arma vem dos **Mods equipados**, não do nível base. Stats nativos (dano, critical chance, status chance, fire rate) definem o potencial; os mods amplificam ou redirecionam esse potencial.


## 🌍 Onde Conseguir — Warframe — Segunda Mente


A maioria das armas é **construída na Fundição** a partir de blueprints e recursos:

| Fonte                            | Exemplos                                          |
| -------------------------------- | ------------------------------------------------- |
| Mercado (blueprint por Créditos) | Maioria das armas base                            |
| Drop de inimigos / chefes        | Wraith, Vandal, Prisma e variantes                |
| Pesquisa de Clã                  | Arca Plasmor, Ignis Wraith, Glaxion Vandal        |
| Relíquias do Void                | Versões Prime                                     |
| Liches (Kuva)                    | Kuva Bramma, Kuva Nukor, Kuva Shildeg etc.        |
| Irmãs de Parvos (Tenet)          | Tenet Cycron, Tenet Exec, Tenet Arca Plasmor etc. |
| Sindicatos                       | Rakta Cernos, Sancti Tigris, Vaykor Hek etc.      |
| Quests                           | Paracesis, War, Broken War, Nataruk etc.          |
| Nightwave / Eventos              | Prisma Grakata, Dex Furis etc.                    |
| Kitguns (modular)                | Rattleguts, Catchmoon, Tombfinger, Gaze           |
| Zaws (modular)                   | Armas brancas customizadas em Cetus               |

Tempo de craft: **12 horas** para componentes, **24 horas** para a arma completa (varia por arma).


## Stats e Mecânicas — Warframe — Segunda Mente


| Stat                    | Função                                                 |
| ----------------------- | ------------------------------------------------------ |
| **Dano base**           | Total de dano por disparo antes de mods                |
| **Distribuição IPS**    | Porcentagem de Impact / Puncture / Slash               |
| **Critical Chance**     | Chance de acerto crítico (dano × multiplicador)        |
| **Critical Multiplier** | Multiplicador de dano em crits (ex: 2.0×)              |
| **Status Chance**       | Chance de aplicar um proc elemental por projétil       |
| **Fire Rate**           | Disparos por segundo                                   |
| **Magazine**            | Capacidade do carregador                               |
| **Reload**              | Tempo de recarga em segundos                           |
| **Multishot**           | Projéteis adicionais por disparo (base + mods)         |

### Combinações de Dano Elemental

| Combinação         | Elemento  |
| ------------------ | --------- |
| Calor + Frio       | Blast     |
| Calor + Elétrico   | Radiação  |
| Calor + Tóxico     | Gás       |
| Frio + Elétrico    | Magnético |
| Frio + Tóxico      | Viral     |
| Elétrico + Tóxico  | Corrosivo |


## Mastery — Warframe — Segunda Mente


Cada arma contribui com **Affinity de Mastery** quando levada ao Rank 30 pela primeira vez:
- **Armas comuns:** 3.000 pontos
- **Armas Prime:** 6.000 pontos (contam separado da versão base)


## Sub-Índices — Warframe — Segunda Mente


Cada sub-índice cobre mecânicas exclusivas da sua categoria além da lista de armas:

| Sub-Índice | Mecânicas Exclusivas Cobertas |
|---|---|
| [[armas/primarias/_Armas _Primarias _Indice.md\|Primárias]] | Modos de disparo, tipos de munição, punch-through, beam weapons, Incarnon |
| [[armas/secundarias/_Armas _Secundarias _Indice.md\|Secundárias]] | Sistema Kitgun modular, armas de arremesso, prefixo Ak- (dual-wield), Incarnon |
| [[armas/brancas/_Armas _Brancas _Indice.md\|Brancas]] | Stances por tipo de arma, combo counter, heavy attacks, finishers, slam attacks |
| [[armas/archwing/_Armas _Archwing _Indice.md\|Archwing]] | Modos espacial/atmosfera/terrestre, Archgun Deployer, Zenith Crown, pool de mods exclusivo |


## 📋 Lista Completa — Warframe — Segunda Mente


### Primárias (129)

| Arma | Tipo | Fonte |
|---|---|---|
| [[armas/primarias/acceltra.md\|Acceltra]] | Rifle de Assalto | Drop (Demolyst Manic, Steel Path) |
| [[armas/primarias/acceltra_prime.md\|Acceltra Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/ambassador.md\|Ambassador]] | Rifle de Assalto | Drop (Amalgam, Jupiter) |
| [[armas/primarias/amprex.md\|Amprex]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[armas/primarias/arca_plasmor.md\|Arca Plasmor]] | Espingarda | Pesquisa de Clã (Corpus) |
| [[armas/primarias/astilla.md\|Astilla]] | Espingarda | Pesquisa de Clã (Corpus) |
| [[armas/primarias/astilla_prime.md\|Astilla Prime]] | Espingarda | Relíquias (Prime) |
| [[armas/primarias/attica.md\|Attica]] | Arco | Mercado (blueprint) |
| [[armas/primarias/battacor.md\|Battacor]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[armas/primarias/baza.md\|Baza]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/baza_prime.md\|Baza Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/boltor.md\|Boltor]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/boltor_prime.md\|Boltor Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/braton.md\|Braton]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/braton_prime.md\|Braton Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/braton_vandal.md\|Braton Vandal]] | Rifle de Assalto | Evento / Drop (Acolytes) |
| [[armas/primarias/buzlok.md\|Buzlok]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/cedo.md\|Cedo]] | Espingarda | Pesquisa de Clã (Entrati) |
| [[armas/primarias/cernos.md\|Cernos]] | Arco | Mercado (blueprint) |
| [[armas/primarias/cernos_prime.md\|Cernos Prime]] | Arco | Relíquias (Prime) |
| [[armas/primarias/convectrix.md\|Convectrix]] | Espingarda | Pesquisa de Clã (Corpus) |
| [[armas/primarias/corinth.md\|Corinth]] | Espingarda | Mercado (blueprint) |
| [[armas/primarias/corinth_prime.md\|Corinth Prime]] | Espingarda | Relíquias (Prime) |
| [[armas/primarias/daikyu.md\|Daikyu]] | Arco | Mercado (blueprint) |
| [[armas/primarias/dera.md\|Dera]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/dera_vandal.md\|Dera Vandal]] | Rifle de Assalto | Nightwave / Evento |
| [[armas/primarias/dex_sybaris.md\|Dex Sybaris]] | Rifle Semi-Auto | Evento (Aniversário DE) |
| [[armas/primarias/drakgoon.md\|Drakgoon]] | Espingarda | Mercado (blueprint) |
| [[armas/primarias/exergis.md\|Exergis]] | Espingarda | Pesquisa de Clã (Corpus) |
| [[armas/primarias/felarx.md\|Felarx]] | Incarnon | Incarnon (Duviri) |
| [[armas/primarias/ferrox.md\|Ferrox]] | Rifle Especial | Mercado (blueprint) |
| [[armas/primarias/flux_rifle.md\|Flux Rifle]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[armas/primarias/fulmin.md\|Fulmin]] | Rifle Especial | Drop (Amalgam, Jupiter) |
| [[armas/primarias/fulmin_prime.md\|Fulmin Prime]] | Rifle Especial | Relíquias (Prime) |
| [[armas/primarias/glaxion.md\|Glaxion]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[armas/primarias/glaxion_vandal.md\|Glaxion Vandal]] | Rifle de Assalto | Nightwave / Evento |
| [[armas/primarias/gorgon.md\|Gorgon]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/gorgon_wraith.md\|Gorgon Wraith]] | Rifle de Assalto | Nightwave / Evento |
| [[armas/primarias/grakata.md\|Grakata]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/harpak.md\|Harpak]] | Rifle Especial | Mercado (blueprint) |
| [[armas/primarias/hek.md\|Hek]] | Espingarda | Mercado (blueprint) |
| [[armas/primarias/hind.md\|Hind]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/ignis.md\|Ignis]] | Lança-Chamas | Pesquisa de Clã (Grineer) |
| [[armas/primarias/ignis_wraith.md\|Ignis Wraith]] | Lança-Chamas | Pesquisa de Clã (blueprint tradável) / Evento |
| [[armas/primarias/javlok.md\|Javlok]] | Lançador | Mercado (blueprint) |
| [[armas/primarias/karak.md\|Karak]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/karak_wraith.md\|Karak Wraith]] | Rifle de Assalto | Evento / Drop (Acolytes) |
| [[armas/primarias/kohm.md\|Kohm]] | Espingarda | Mercado (blueprint) |
| [[armas/primarias/komorex.md\|Komorex]] | Sniper | Pesquisa de Clã (Corpus) |
| [[armas/primarias/kuva_bramma.md\|Kuva Bramma]] | Lançador | Kuva Lich |
| [[armas/primarias/kuva_chakkhurr.md\|Kuva Chakkhurr]] | Sniper | Kuva Lich |
| [[armas/primarias/kuva_hek.md\|Kuva Hek]] | Espingarda | Kuva Lich |
| [[armas/primarias/kuva_ogris.md\|Kuva Ogris]] | Lançador | Kuva Lich |
| [[armas/primarias/kuva_quartakk.md\|Kuva Quartakk]] | Rifle de Assalto | Kuva Lich |
| [[armas/primarias/kuva_tonkor.md\|Kuva Tonkor]] | Lançador | Kuva Lich |
| [[armas/primarias/kuva_zarr.md\|Kuva Zarr]] | Lançador | Kuva Lich |
| [[armas/primarias/lanka.md\|Lanka]] | Sniper | Mercado (blueprint) |
| [[armas/primarias/latron.md\|Latron]] | Rifle Semi-Auto | Mercado (blueprint) |
| [[armas/primarias/latron_prime.md\|Latron Prime]] | Rifle Semi-Auto | Relíquias (Prime) |
| [[armas/primarias/latron_wraith.md\|Latron Wraith]] | Rifle Semi-Auto | Nightwave / Evento |
| [[armas/primarias/lenz.md\|Lenz]] | Arco | Mercado (blueprint) |
| [[armas/primarias/miter.md\|Miter]] | Lançador | Mercado (blueprint) |
| [[armas/primarias/mk1_braton.md\|MK1-Braton]] | Rifle de Assalto | Starter / Mercado |
| [[armas/primarias/mutalist_quanta.md\|Mutalist Quanta]] | Lançador | Drop (Invasões Infested, Eris) |
| [[armas/primarias/nataruk.md\|Nataruk]] | Arco | Nakak, Cetus (pós The New War) |
| [[armas/primarias/ogris.md\|Ogris]] | Lançador | Mercado (blueprint) |
| [[armas/primarias/opticor.md\|Opticor]] | Sniper | Pesquisa de Clã (Corpus) |
| [[armas/primarias/opticor_vandal.md\|Opticor Vandal]] | Sniper | Nightwave / Evento |
| [[armas/primarias/panthera.md\|Panthera]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[armas/primarias/panthera_prime.md\|Panthera Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/paracyst.md\|Paracyst]] | Rifle Especial | Mercado (blueprint) |
| [[armas/primarias/paris.md\|Paris]] | Arco | Mercado (blueprint) |
| [[armas/primarias/paris_prime.md\|Paris Prime]] | Arco | Relíquias (Prime) |
| [[armas/primarias/penta.md\|Penta]] | Lançador | Mercado (blueprint) |
| [[armas/primarias/phantasma.md\|Phantasma]] | Espingarda | Pesquisa de Clã (Entrati) |
| [[armas/primarias/phantasma_prime.md\|Phantasma Prime]] | Espingarda | Relíquias (Prime) |
| [[armas/primarias/phenmor.md\|Phenmor]] | Incarnon | Incarnon (Duviri) |
| [[armas/primarias/prisma_grakata.md\|Prisma Grakata]] | Rifle de Assalto | Baro Ki'Teer / Nightwave |
| [[armas/primarias/proboscis_cernos.md\|Proboscis Cernos]] | Arco | Pesquisa de Clã (Entrati) |
| [[armas/primarias/quanta.md\|Quanta]] | Lançador | Pesquisa de Clã (Corpus) |
| [[armas/primarias/quanta_vandal.md\|Quanta Vandal]] | Lançador | Nightwave / Evento |
| [[armas/primarias/rakta_cernos.md\|Rakta Cernos]] | Arco | Sindicato (Red Veil) |
| [[armas/primarias/rubico.md\|Rubico]] | Sniper | Mercado (blueprint) |
| [[armas/primarias/rubico_prime.md\|Rubico Prime]] | Sniper | Relíquias (Prime) |
| [[armas/primarias/sancti_tigris.md\|Sancti Tigris]] | Espingarda | Sindicato (New Loka) |
| [[armas/primarias/scourge.md\|Scourge]] | Lançador | Pesquisa de Clã (Entrati) |
| [[armas/primarias/scourge_prime.md\|Scourge Prime]] | Lançador | Relíquias (Prime) |
| [[armas/primarias/secura_penta.md\|Secura Penta]] | Lançador | Sindicato (Perrin Sequence) |
| [[armas/primarias/shedu.md\|Shedu]] | Rifle Especial | Drop (Sentients, Murex — Empyrean) |
| [[armas/primarias/simulor.md\|Simulor]] | Lançador | Pesquisa de Clã (Corpus) |
| [[armas/primarias/snipetron.md\|Snipetron]] | Sniper | Baro Ki'Teer |
| [[armas/primarias/snipetron_vandal.md\|Snipetron Vandal]] | Sniper | Evento |
| [[armas/primarias/sobek.md\|Sobek]] | Espingarda | Mercado (blueprint) |
| [[armas/primarias/soma.md\|Soma]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/soma_prime.md\|Soma Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/sporothrix.md\|Sporothrix]] | Arco | Pesquisa de Clã (Entrati) |
| [[armas/primarias/stahlta.md\|Stahlta]] | Rifle de Assalto | Pesquisa de Clã (Entrati) |
| [[armas/primarias/stradavar.md\|Stradavar]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/stradavar_prime.md\|Stradavar Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/strun.md\|Strun]] | Espingarda | Mercado (blueprint) |
| [[armas/primarias/strun_wraith.md\|Strun Wraith]] | Espingarda | Nightwave / Evento |
| [[armas/primarias/supra.md\|Supra]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[armas/primarias/supra_vandal.md\|Supra Vandal]] | Rifle de Assalto | Nightwave / Evento |
| [[armas/primarias/sybaris.md\|Sybaris]] | Rifle Semi-Auto | Mercado (blueprint) |
| [[armas/primarias/sybaris_prime.md\|Sybaris Prime]] | Rifle Semi-Auto | Relíquias (Prime) |
| [[armas/primarias/synoid_simulor.md\|Synoid Simulor]] | Lançador | Sindicato (Cephalon Suda) |
| [[armas/primarias/telos_boltor.md\|Telos Boltor]] | Rifle de Assalto | Sindicato (Arbiters of Hexis) |
| [[armas/primarias/tenet_arca_plasmor.md\|Tenet Arca Plasmor]] | Espingarda | Irmãs de Parvos |
| [[armas/primarias/tenet_envoy.md\|Tenet Envoy]] | Lançador | Irmãs de Parvos |
| [[armas/primarias/tenet_ferrox.md\|Tenet Ferrox]] | Rifle Especial | Irmãs de Parvos |
| [[armas/primarias/tenet_flux_rifle.md\|Tenet Flux Rifle]] | Rifle de Assalto | Irmãs de Parvos |
| [[armas/primarias/tenora.md\|Tenora]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/tenora_prime.md\|Tenora Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/tiberon.md\|Tiberon]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/tiberon_prime.md\|Tiberon Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/tigris.md\|Tigris]] | Espingarda | Mercado (blueprint) |
| [[armas/primarias/tigris_prime.md\|Tigris Prime]] | Espingarda | Relíquias (Prime) |
| [[armas/primarias/tonkor.md\|Tonkor]] | Lançador | Mercado (blueprint) |
| [[armas/primarias/trumna.md\|Trumna]] | Lançador | Pesquisa de Clã (Entrati) |
| [[armas/primarias/vaykor_hek.md\|Vaykor Hek]] | Espingarda | Sindicato (Steel Meridian) |
| [[armas/primarias/vectis.md\|Vectis]] | Sniper | Mercado (blueprint) |
| [[armas/primarias/vectis_prime.md\|Vectis Prime]] | Sniper | Relíquias (Prime) |
| [[armas/primarias/veldt.md\|Veldt]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/vermisplicer.md\|Vermisplicer]] | Espingarda | Pesquisa de Clã (Entrati) |
| [[armas/primarias/vulkar.md\|Vulkar]] | Sniper | Mercado (blueprint) |
| [[armas/primarias/vulkar_wraith.md\|Vulkar Wraith]] | Sniper | Nightwave / Evento |
| [[armas/primarias/zarr.md\|Zarr]] | Lançador | Mercado (blueprint) |
| [[armas/primarias/zhuge.md\|Zhuge]] | Arco | Mercado (blueprint) |
| [[armas/primarias/zhuge_prime.md\|Zhuge Prime]] | Arco | Relíquias (Prime) |


### Secundárias (93)

| Arma | Tipo | Fonte |
|---|---|---|
| [[armas/secundarias/acrid.md\|Acrid]] | Especial | Drop (Invasões Infested) |
| [[armas/secundarias/akarius.md\|Akarius]] | Pistolas Duplas | Pesquisa de Clã (Entrati) |
| [[armas/secundarias/akbolto.md\|Akbolto]] | Pistolas Duplas | Mercado (2× Bolto) |
| [[armas/secundarias/akbolto_prime.md\|Akbolto Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[armas/secundarias/akjagara.md\|Akjagara]] | Pistolas Duplas | Mercado (blueprint) |
| [[armas/secundarias/akjagara_prime.md\|Akjagara Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[armas/secundarias/aklex.md\|Aklex]] | Pistolas Duplas | Mercado (2× Lex) |
| [[armas/secundarias/aklex_prime.md\|Aklex Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[armas/secundarias/aksomati.md\|Aksomati]] | Pistolas Duplas | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/aksomati_prime.md\|Aksomati Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[armas/secundarias/akstiletto.md\|Akstiletto]] | Pistolas Duplas | Mercado (blueprint) |
| [[armas/secundarias/akstiletto_prime.md\|Akstiletto Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[armas/secundarias/akvasto.md\|Akvasto]] | Pistolas Duplas | Mercado (2× Vasto) |
| [[armas/secundarias/akvasto_prime.md\|Akvasto Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[armas/secundarias/akzani.md\|Akzani]] | Pistolas Duplas | Pesquisa de Clã (Cetus) |
| [[armas/secundarias/arca_scisco.md\|Arca Scisco]] | Pistola | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/athodai.md\|Athodai]] | Pistola | Fortuna (Old Mate, rank 5) |
| [[armas/secundarias/atomos.md\|Atomos]] | Especial | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/azima.md\|Azima]] | Especial | Nightwave / Evento |
| [[armas/secundarias/ballistica.md\|Ballistica]] | Arco Secundário | Mercado (blueprint) |
| [[armas/secundarias/ballistica_prime.md\|Ballistica Prime]] | Arco Secundário | Relíquias (Prime) |
| [[armas/secundarias/bolto.md\|Bolto]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/brakk.md\|Brakk]] | Pistola | Drop (Grustrag Three) / Invasões |
| [[armas/secundarias/bronco.md\|Bronco]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/bronco_prime.md\|Bronco Prime]] | Pistola | Relíquias (Prime) |
| [[armas/secundarias/bubonico.md\|Bubonico]] | Canhão de Braço | Pesquisa de Clã (Entrati) |
| [[armas/secundarias/castanas.md\|Castanas]] | Arremesso | Mercado (blueprint) |
| [[armas/secundarias/catchmoon.md\|Catchmoon]] | Kitgun | Kitgun (Fortuna) |
| [[armas/secundarias/cyanex.md\|Cyanex]] | Especial | Pesquisa de Clã (Entrati) |
| [[armas/secundarias/despair.md\|Despair]] | Arremesso | Drop (Stalker) |
| [[armas/secundarias/detron.md\|Detron]] | Pistola | Drop (Corrupted, Void) |
| [[armas/secundarias/dex_furis.md\|Dex Furis]] | Pistola | Evento (Aniversário DE) |
| [[armas/secundarias/embolist.md\|Embolist]] | Especial | Pesquisa de Clã (Grineer) |
| [[armas/secundarias/epitaph.md\|Epitaph]] | Pistola | Pesquisa de Clã (Entrati) |
| [[armas/secundarias/euphona_prime.md\|Euphona Prime]] | Pistola | Relíquias (Prime) |
| [[armas/secundarias/furis.md\|Furis]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/fusilai.md\|Fusilai]] | Arremesso | Nakak, Cetus (caça) |
| [[armas/secundarias/gammacor.md\|Gammacor]] | Especial | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/gaze.md\|Gaze]] | Kitgun | Kitgun (Fortuna) |
| [[armas/secundarias/hikou.md\|Hikou]] | Arremesso | Mercado (blueprint) |
| [[armas/secundarias/hikou_prime.md\|Hikou Prime]] | Arremesso | Relíquias (Prime) |
| [[armas/secundarias/knell.md\|Knell]] | Pistola | Pesquisa de Clã (Quills, Cetus) |
| [[armas/secundarias/knell_prime.md\|Knell Prime]] | Pistola | Relíquias (Prime) |
| [[armas/secundarias/kohmak.md\|Kohmak]] | Especial | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/kompressa.md\|Kompressa]] | Especial | Pesquisa de Clã (Entrati) |
| [[armas/secundarias/kulstar.md\|Kulstar]] | Especial | Pesquisa de Clã (Grineer) |
| [[armas/secundarias/kuva_brakk.md\|Kuva Brakk]] | Pistola | Kuva Lich |
| [[armas/secundarias/kuva_nukor.md\|Kuva Nukor]] | Pistola | Kuva Lich |
| [[armas/secundarias/kuva_seer.md\|Kuva Seer]] | Pistola | Kuva Lich |
| [[armas/secundarias/kuva_twin_stubbas.md\|Kuva Twin Stubbas]] | Pistolas Duplas | Kuva Lich |
| [[armas/secundarias/laetum.md\|Laetum]] | Incarnon | Incarnon (Duviri) |
| [[armas/secundarias/lato.md\|Lato]] | Pistola | Starter / Mercado |
| [[armas/secundarias/lato_prime.md\|Lato Prime]] | Pistola | Indisponível (Founder's Pack, 2013) |
| [[armas/secundarias/lato_vandal.md\|Lato Vandal]] | Pistola | Nightwave / Evento |
| [[armas/secundarias/lex.md\|Lex]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/lex_prime.md\|Lex Prime]] | Pistola | Relíquias (Prime) |
| [[armas/secundarias/magnus.md\|Magnus]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/magnus_prime.md\|Magnus Prime]] | Pistola | Relíquias (Prime) |
| [[armas/secundarias/mara_detron.md\|Mara Detron]] | Pistola | Baro Ki'Teer |
| [[armas/secundarias/nukor.md\|Nukor]] | Pistola | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/ocucor.md\|Ocucor]] | Especial | Pesquisa de Clã (Entrati) |
| [[armas/secundarias/pandero.md\|Pandero]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/pandero_prime.md\|Pandero Prime]] | Pistola | Relíquias (Prime) |
| [[armas/secundarias/rattleguts.md\|Rattleguts]] | Kitgun | Kitgun (Fortuna) |
| [[armas/secundarias/sancti_castanas.md\|Sancti Castanas]] | Arremesso | Sindicato (New Loka) |
| [[armas/secundarias/seer.md\|Seer]] | Pistola | Drop (Vor, Mercury — Tolstoj) |
| [[armas/secundarias/sicarus.md\|Sicarus]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/sicarus_prime.md\|Sicarus Prime]] | Pistola | Relíquias (Prime) |
| [[armas/secundarias/sonicor.md\|Sonicor]] | Especial | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/spira.md\|Spira]] | Arremesso | Mercado (blueprint) |
| [[armas/secundarias/spira_prime.md\|Spira Prime]] | Arremesso | Relíquias (Prime) |
| [[armas/secundarias/staticor.md\|Staticor]] | Especial | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/stubba.md\|Stubba]] | Especial | Pesquisa de Clã (Grineer) |
| [[armas/secundarias/stug.md\|Stug]] | Especial | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/synoid_gammacor.md\|Synoid Gammacor]] | Especial | Sindicato (Cephalon Suda) |
| [[armas/secundarias/tenet_agendus.md\|Tenet Agendus]] | Especial | Irmãs de Parvos |
| [[armas/secundarias/tenet_cycron.md\|Tenet Cycron]] | Especial | Irmãs de Parvos |
| [[armas/secundarias/tenet_detron.md\|Tenet Detron]] | Pistola | Irmãs de Parvos |
| [[armas/secundarias/tenet_diplos.md\|Tenet Diplos]] | Pistolas Duplas | Irmãs de Parvos |
| [[armas/secundarias/tenet_plinx.md\|Tenet Plinx]] | Pistola | Irmãs de Parvos |
| [[armas/secundarias/tenet_spirex.md\|Tenet Spirex]] | Especial | Irmãs de Parvos |
| [[armas/secundarias/tombfinger.md\|Tombfinger]] | Kitgun | Kitgun (Fortuna) |
| [[armas/secundarias/twin_grakata.md\|Twin Grakata]] | Pistolas Duplas | Mercado (blueprint) |
| [[armas/secundarias/twin_vipers.md\|Twin Vipers]] | Pistolas Duplas | Mercado (blueprint) |
| [[armas/secundarias/twin_vipers_wraith.md\|Twin Vipers Wraith]] | Pistolas Duplas | Nightwave / Evento |
| [[armas/secundarias/vasto.md\|Vasto]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/vasto_prime.md\|Vasto Prime]] | Pistola | Relíquias (Prime) |
| [[armas/secundarias/velox.md\|Velox]] | Pistola | Drop (Corpus, Orb Vallis) |
| [[armas/secundarias/viper.md\|Viper]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/viper_wraith.md\|Viper Wraith]] | Pistola | Nightwave / Evento |
| [[armas/secundarias/zakti.md\|Zakti]] | Arremesso | Mercado (blueprint) |
| [[armas/secundarias/zakti_prime.md\|Zakti Prime]] | Arremesso | Relíquias (Prime) |
| [[armas/secundarias/zylok.md\|Zylok]] | Pistola | Nightwave / Evento |


### Brancas — Melee (135)

| Arma | Tipo | Fonte |
|---|---|---|
| [[armas/brancas/ack_and_brunt.md\|Ack e Brunt]] | Espada e Escudo | Pesquisa de Clã (Grineer) |
| [[armas/brancas/anku.md\|Anku]] | Foice | Pesquisa de Clã (Grineer) |
| [[armas/brancas/arca_titron.md\|Arca Titron]] | Martelo | Pesquisa de Clã (Corpus) |
| [[armas/brancas/arum_spinosa.md\|Arum Spinosa]] | Lâmina e Chicote | Pesquisa de Clã (Entrati) |
| [[armas/brancas/atterax.md\|Atterax]] | Chicote | Mercado (blueprint) |
| [[armas/brancas/bo.md\|Bo]] | Cajado | Mercado (blueprint) |
| [[armas/brancas/bo_prime.md\|Bo Prime]] | Cajado | Relíquias (Prime) |
| [[armas/brancas/boltace.md\|Boltace]] | Espadas Duplas | Pesquisa de Clã (Corpus) |
| [[armas/brancas/broken_sword.md\|Broken Sword]] | Espada | Drop (Stalker) |
| [[armas/brancas/broken_war.md\|Broken War]] | Espada | Drop (Stalker — partes de War) |
| [[armas/brancas/ceramic_dagger.md\|Ceramic Dagger]] | Adaga | Mercado (blueprint) |
| [[armas/brancas/cobra_and_crane.md\|Cobra e Crane]] | Espada e Escudo | Pesquisa de Clã (Grineer) |
| [[armas/brancas/cronus.md\|Cronus]] | Espada | Drop (Ambulas, Pluto) |
| [[armas/brancas/dakra_prime.md\|Dakra Prime]] | Espada | Relíquias (Prime) |
| [[armas/brancas/dark_dagger.md\|Dark Dagger]] | Adaga | Mercado (blueprint) |
| [[armas/brancas/dark_split_sword.md\|Dark Split-Sword]] | Espada Pesada / Dupla | Mercado (blueprint) |
| [[armas/brancas/dark_sword.md\|Dark Sword]] | Espada | Mercado (blueprint) |
| [[armas/brancas/destreza.md\|Destreza]] | Espadim | Mercado (blueprint) |
| [[armas/brancas/destreza_prime.md\|Destreza Prime]] | Espadim | Relíquias (Prime) |
| [[armas/brancas/dragon_nikana.md\|Dragon Nikana]] | Espada | Mercado (blueprint + componentes Clã) |
| [[armas/brancas/dual_cleavers.md\|Dual Cleavers]] | Espadas Duplas | Mercado (blueprint) |
| [[armas/brancas/dual_ether.md\|Dual Ether]] | Espadas Duplas | Mercado (blueprint) |
| [[armas/brancas/dual_heat_swords.md\|Dual Heat Swords]] | Espadas Duplas | Mercado (blueprint) |
| [[armas/brancas/dual_ichor.md\|Dual Ichor]] | Espadas Duplas | Mercado (blueprint) |
| [[armas/brancas/dual_kamas.md\|Dual Kamas]] | Espadas Duplas | Mercado (blueprint) |
| [[armas/brancas/dual_kamas_prime.md\|Dual Kamas Prime]] | Espadas Duplas | Relíquias (Prime) |
| [[armas/brancas/dual_skana.md\|Dual Skana]] | Espadas Duplas | Mercado (blueprint) |
| [[armas/brancas/dual_zoren.md\|Dual Zoren]] | Espadas Duplas | Mercado (blueprint) |
| [[armas/brancas/ether_daggers.md\|Ether Daggers]] | Adagas Duplas | Mercado (blueprint) |
| [[armas/brancas/ether_reaper.md\|Ether Reaper]] | Foice | Mercado (blueprint) |
| [[armas/brancas/ether_sword.md\|Ether Sword]] | Espada | Mercado (blueprint) |
| [[armas/brancas/fang.md\|Fang]] | Espadas Duplas | Mercado (blueprint) |
| [[armas/brancas/fang_prime.md\|Fang Prime]] | Espadas Duplas | Relíquias (Prime) |
| [[armas/brancas/fragor.md\|Fragor]] | Martelo | Mercado (blueprint) |
| [[armas/brancas/fragor_prime.md\|Fragor Prime]] | Martelo | Relíquias (Prime) |
| [[armas/brancas/furax.md\|Furax]] | Garras | Mercado (blueprint) |
| [[armas/brancas/furax_wraith.md\|Furax Wraith]] | Garras | Nightwave / Evento |
| [[armas/brancas/galatine.md\|Galatine]] | Espada Pesada | Mercado (blueprint) |
| [[armas/brancas/galatine_prime.md\|Galatine Prime]] | Espada Pesada | Relíquias (Prime) |
| [[armas/brancas/galvacord.md\|Galvacord]] | Chicote | Pesquisa de Clã (Grineer) |
| [[armas/brancas/glaive.md\|Glaive]] | Glaive | Mercado (blueprint) |
| [[armas/brancas/glaive_prime.md\|Glaive Prime]] | Glaive | Relíquias (Prime) |
| [[armas/brancas/gram.md\|Gram]] | Espada Pesada | Mercado (blueprint) |
| [[armas/brancas/gram_prime.md\|Gram Prime]] | Espada Pesada | Relíquias (Prime) |
| [[armas/brancas/guandao.md\|Guandao]] | Lança | Mercado (blueprint) |
| [[armas/brancas/guandao_prime.md\|Guandao Prime]] | Lança | Relíquias (Prime) |
| [[armas/brancas/halikar.md\|Halikar]] | Glaive | Mercado (blueprint) |
| [[armas/brancas/halikar_wraith.md\|Halikar Wraith]] | Glaive | Nightwave / Evento |
| [[armas/brancas/hate.md\|Hate]] | Foice | Drop (Stalker) |
| [[armas/brancas/heat_sword.md\|Heat Sword]] | Espada | Mercado (blueprint) |
| [[armas/brancas/hirudo.md\|Hirudo]] | Garras | Pesquisa de Clã (Grineer) |
| [[armas/brancas/innodem.md\|Innodem]] | Espada | Pesquisa de Clã (Entrati) |
| [[armas/brancas/jat_kittag.md\|Jat Kittag]] | Martelo | Mercado (blueprint) |
| [[armas/brancas/jat_kusar.md\|Jat Kusar]] | Cajado | Pesquisa de Clã (Corpus) |
| [[armas/brancas/jaw_sword.md\|Jaw Sword]] | Espada | Mercado (blueprint) |
| [[armas/brancas/karyst.md\|Karyst]] | Adaga | Mercado (blueprint) |
| [[armas/brancas/karyst_prime.md\|Karyst Prime]] | Adaga | Relíquias (Prime) |
| [[armas/brancas/kesheg.md\|Kesheg]] | Lança | Pesquisa de Clã (Grineer) |
| [[armas/brancas/kestrel.md\|Kestrel]] | Glaive | Mercado (blueprint) |
| [[armas/brancas/krohkur.md\|Krohkur]] | Espada | Mercado (blueprint) |
| [[armas/brancas/kronen.md\|Kronen]] | Tonfa | Pesquisa de Clã (Corpus) |
| [[armas/brancas/kronen_prime.md\|Kronen Prime]] | Tonfa | Relíquias (Prime) |
| [[armas/brancas/kuva_shildeg.md\|Kuva Shildeg]] | Martelo | Kuva Lich |
| [[armas/brancas/lacera.md\|Lacera]] | Lâmina e Chicote | Pesquisa de Clã (Corpus) |
| [[armas/brancas/lecta.md\|Lecta]] | Chicote | Mercado (blueprint) |
| [[armas/brancas/lesion.md\|Lesion]] | Lança | Pesquisa de Clã (Entrati) |
| [[armas/brancas/machete.md\|Machete]] | Facão | Mercado (blueprint) |
| [[armas/brancas/machete_wraith.md\|Machete Wraith]] | Facão | Nightwave / Evento |
| [[armas/brancas/magistar.md\|Magistar]] | Martelo | Pesquisa de Clã (Grineer) |
| [[armas/brancas/magistar_wraith.md\|Magistar Wraith]] | Martelo | Nightwave / Evento |
| [[armas/brancas/mios.md\|Mios]] | Lâmina e Chicote | Pesquisa de Clã (Entrati) |
| [[armas/brancas/mire.md\|Mire]] | Espada | Drop (Ambulas, Pluto) |
| [[armas/brancas/nami_duo.md\|Nami Duo]] | Espadas Duplas | Pesquisa de Clã (Corpus) |
| [[armas/brancas/nami_solo.md\|Nami Solo]] | Espada | Pesquisa de Clã (Corpus) |
| [[armas/brancas/nikana.md\|Nikana]] | Espada | Mercado (blueprint) |
| [[armas/brancas/nikana_prime.md\|Nikana Prime]] | Espada | Relíquias (Prime) |
| [[armas/brancas/ninkondi.md\|Ninkondi]] | Nunchaku | Pesquisa de Clã (Corpus) |
| [[armas/brancas/ninkondi_prime.md\|Ninkondi Prime]] | Nunchaku | Relíquias (Prime) |
| [[armas/brancas/ohma.md\|Ohma]] | Tonfa | Pesquisa de Clã (Corpus) |
| [[armas/brancas/okina.md\|Okina]] | Espadas Duplas | Pesquisa de Clã (Corpus) |
| [[armas/brancas/okina_prime.md\|Okina Prime]] | Espadas Duplas | Relíquias (Prime) |
| [[armas/brancas/orthos.md\|Orthos]] | Lança | Mercado (blueprint) |
| [[armas/brancas/orthos_prime.md\|Orthos Prime]] | Lança | Relíquias (Prime) |
| [[armas/brancas/orvius.md\|Orvius]] | Glaive | Quest (Chains of Harrow) |
| [[armas/brancas/pangolin_prime.md\|Pangolin Prime]] | Espada | Relíquias (Prime) |
| [[armas/brancas/pangolin_sword.md\|Pangolin Sword]] | Espada | Mercado (blueprint) |
| [[armas/brancas/paracesis.md\|Paracesis]] | Espada Pesada | Quest (The Sacrifice) |
| [[armas/brancas/pennant.md\|Pennant]] | Espada Pesada | Pesquisa de Clã (Entrati) |
| [[armas/brancas/plasma_sword.md\|Plasma Sword]] | Espada | Mercado (blueprint) |
| [[armas/brancas/praedos.md\|Praedos]] | Tonfa | Pesquisa de Clã (Entrati) |
| [[armas/brancas/prisma_dual_cleavers.md\|Prisma Dual Cleavers]] | Espadas Duplas | Baro Ki'Teer |
| [[armas/brancas/prisma_skana.md\|Prisma Skana]] | Espada | Baro Ki'Teer |
| [[armas/brancas/prova.md\|Prova]] | Lança | Pesquisa de Clã (Corpus) |
| [[armas/brancas/prova_vandal.md\|Prova Vandal]] | Lança | Nightwave / Evento |
| [[armas/brancas/pulmonars.md\|Pulmonars]] | Leques | Pesquisa de Clã (Entrati) |
| [[armas/brancas/rakta_dark_dagger.md\|Rakta Dark Dagger]] | Adaga | Sindicato (Red Veil) |
| [[armas/brancas/reaper_prime.md\|Reaper Prime]] | Foice | Relíquias (Prime) |
| [[armas/brancas/redeemer.md\|Redeemer]] | Espingarda Melee | Pesquisa de Clã (Tenno) |
| [[armas/brancas/redeemer_prime.md\|Redeemer Prime]] | Espingarda Melee | Relíquias (Prime) |
| [[armas/brancas/ripkas.md\|Ripkas]] | Garras | Pesquisa de Clã (Grineer) |
| [[armas/brancas/sarpa.md\|Sarpa]] | Espingarda Melee | Pesquisa de Clã (Tenno) |
| [[armas/brancas/scoliac.md\|Scoliac]] | Chicote | Pesquisa de Clã (Grineer) |
| [[armas/brancas/secura_lecta.md\|Secura Lecta]] | Chicote | Sindicato (Perrin Sequence) |
| [[armas/brancas/shaku.md\|Shaku]] | Cajado | Pesquisa de Clã (Corpus) |
| [[armas/brancas/sheev.md\|Sheev]] | Adaga | Pesquisa de Clã (Grineer) |
| [[armas/brancas/sigma_and_octantis.md\|Sigma e Octantis]] | Espada e Escudo | Evento (Aniversário DE) |
| [[armas/brancas/silva_and_aegis.md\|Silva e Aegis]] | Espada e Escudo | Mercado (blueprint) |
| [[armas/brancas/silva_and_aegis_prime.md\|Silva e Aegis Prime]] | Espada e Escudo | Relíquias (Prime) |
| [[armas/brancas/skana.md\|Skana]] | Espada | Starter / Mercado |
| [[armas/brancas/skana_prime.md\|Skana Prime]] | Espada | Relíquias (Prime) |
| [[armas/brancas/skiajati.md\|Skiajati]] | Espada | Quest (The Sacrifice) |
| [[armas/brancas/stiletto_prime.md\|Stiletto Prime]] | Adaga | Relíquias (Prime) |
| [[armas/brancas/stropha.md\|Stropha]] | Espingarda Melee | Pesquisa de Clã (Tenno) |
| [[armas/brancas/sydon.md\|Sydon]] | Lança | Pesquisa de Clã (Grineer) |
| [[armas/brancas/tatsu.md\|Tatsu]] | Espada Pesada | Pesquisa de Clã (Entrati) |
| [[armas/brancas/tatsu_prime.md\|Tatsu Prime]] | Espada Pesada | Relíquias (Prime) |
| [[armas/brancas/tekko.md\|Tekko]] | Garras | Mercado (blueprint) |
| [[armas/brancas/tekko_prime.md\|Tekko Prime]] | Garras | Relíquias (Prime) |
| [[armas/brancas/telos_boltace.md\|Telos Boltace]] | Espadas Duplas | Sindicato (Arbiters of Hexis) |
| [[armas/brancas/tenet_exec.md\|Tenet Exec]] | Espada Pesada | Irmãs de Parvos |
| [[armas/brancas/tenet_grigori.md\|Tenet Grigori]] | Foice | Irmãs de Parvos |
| [[armas/brancas/tenet_livia.md\|Tenet Livia]] | Espadim | Irmãs de Parvos |
| [[armas/brancas/tipedo.md\|Tipedo]] | Lança | Mercado (blueprint) |
| [[armas/brancas/tipedo_prime.md\|Tipedo Prime]] | Lança | Relíquias (Prime) |
| [[armas/brancas/tonbo.md\|Tonbo]] | Lança | Pesquisa de Clã (Grineer) |
| [[armas/brancas/twin_basolk.md\|Twin Basolk]] | Adagas Duplas | Pesquisa de Clã (Grineer) |
| [[armas/brancas/vastilok.md\|Vastilok]] | Espingarda Melee | Pesquisa de Clã (Tenno) |
| [[armas/brancas/vaykor_sydon.md\|Vaykor Sydon]] | Lança | Sindicato (Steel Meridian) |
| [[armas/brancas/venka.md\|Venka]] | Garras | Pesquisa de Clã (Grineer) |
| [[armas/brancas/venka_prime.md\|Venka Prime]] | Garras | Relíquias (Prime) |
| [[armas/brancas/vitrica.md\|Vitrica]] | Espada Pesada | Pesquisa de Clã (Entrati) |
| [[armas/brancas/volnus.md\|Volnus]] | Martelo | Pesquisa de Clã (Corpus) |
| [[armas/brancas/volnus_prime.md\|Volnus Prime]] | Martelo | Relíquias (Prime) |
| [[armas/brancas/war.md\|War]] | Espada Pesada | Drop (Stalker) |
| [[armas/brancas/xoris.md\|Xoris]] | Glaive | Quest (The Deadlock Protocol) |


### Archwing (23)

| Arma | Tipo | Fonte |
|---|---|---|
| [[armas/archwing/centaur.md\|Centaur]] | Arch-Melee | Pesquisa de Clã (Tenno) |
| [[armas/archwing/cortege.md\|Cortege]] | Arch-Gun | Pesquisa de Clã (Entrati) |
| [[armas/archwing/corvas.md\|Corvas]] | Arch-Gun | Pesquisa de Clã (Grineer) |
| [[armas/archwing/corvas_prime.md\|Corvas Prime]] | Arch-Gun | Relíquias (Prime) |
| [[armas/archwing/cyngas.md\|Cyngas]] | Arch-Gun | Pesquisa de Clã (Corpus) |
| [[armas/archwing/dual_decurion.md\|Dual Decurion]] | Arch-Gun | Pesquisa de Clã (Corpus) |
| [[armas/archwing/fluctus.md\|Fluctus]] | Arch-Gun | Pesquisa de Clã (Corpus) |
| [[armas/archwing/grattler.md\|Grattler]] | Arch-Gun | Pesquisa de Clã (Grineer) |
| [[armas/archwing/imperator.md\|Imperator]] | Arch-Gun | Mercado (blueprint) / Starter |
| [[armas/archwing/imperator_vandal.md\|Imperator Vandal]] | Arch-Gun | Drop (Archwing missions) / Baro Ki'Teer |
| [[armas/archwing/kaszas.md\|Kaszas]] | Arch-Melee | Pesquisa de Clã (Grineer) |
| [[armas/archwing/knux.md\|Knux]] | Arch-Melee | Pesquisa de Clã (Corpus) |
| [[armas/archwing/kuva_ayanga.md\|Kuva Ayanga]] | Arch-Gun | Kuva Lich |
| [[armas/archwing/kuva_grattler.md\|Kuva Grattler]] | Arch-Gun | Kuva Lich |
| [[armas/archwing/larkspur.md\|Larkspur]] | Arch-Gun | Pesquisa de Clã (Entrati) |
| [[armas/archwing/larkspur_prime.md\|Larkspur Prime]] | Arch-Gun | Relíquias (Prime) |
| [[armas/archwing/mausolon.md\|Mausolon]] | Arch-Gun | Pesquisa de Clã (Entrati) |
| [[armas/archwing/morgha.md\|Morgha]] | Arch-Gun | Pesquisa de Clã (Entrati) |
| [[armas/archwing/onorix.md\|Onorix]] | Arch-Melee | Pesquisa de Clã (Grineer) |
| [[armas/archwing/phaedra.md\|Phaedra]] | Arch-Gun | Pesquisa de Clã (Corpus) |
| [[armas/archwing/prisma_veritux.md\|Prisma Veritux]] | Arch-Melee | Baro Ki'Teer |
| [[armas/archwing/velocitus.md\|Velocitus]] | Arch-Gun | Pesquisa de Clã (Corpus) |
| [[armas/archwing/veritux.md\|Veritux]] | Arch-Melee | Pesquisa de Clã (Tenno) |


## Por Tipo — Warframe — Segunda Mente


### Primárias
**Rifles de Assalto:** [[armas/primarias/braton.md|Braton]] · [[armas/primarias/soma.md|Soma]] · [[armas/primarias/boltor.md|Boltor]] · [[armas/primarias/tiberon.md|Tiberon]] · [[armas/primarias/grakata.md|Grakata]] · [[armas/primarias/tenora.md|Tenora]] · [[armas/primarias/acceltra.md|Acceltra]] · [[armas/primarias/stradavar.md|Stradavar]] · [[armas/primarias/baza.md|Baza]] · [[armas/primarias/karak.md|Karak]] · [[armas/primarias/hind.md|Hind]] · [[armas/primarias/supra.md|Supra]] · [[armas/primarias/gorgon.md|Gorgon]] · [[armas/primarias/amprex.md|Amprex]] · [[armas/primarias/battacor.md|Battacor]] · [[armas/primarias/panthera.md|Panthera]] · [[armas/primarias/veldt.md|Veldt]] · [[armas/primarias/stahlta.md|Stahlta]] · [[armas/primarias/dera.md|Dera]] · [[armas/primarias/glaxion.md|Glaxion]] · [[armas/primarias/flux_rifle.md|Flux Rifle]] · [[armas/primarias/buzlok.md|Buzlok]]

**Espingardas:** [[armas/primarias/hek.md|Hek]] · [[armas/primarias/sobek.md|Sobek]] · [[armas/primarias/corinth.md|Corinth]] · [[armas/primarias/tigris.md|Tigris]] · [[armas/primarias/arca_plasmor.md|Arca Plasmor]] · [[armas/primarias/cedo.md|Cedo]] · [[armas/primarias/kohm.md|Kohm]] · [[armas/primarias/astilla.md|Astilla]] · [[armas/primarias/phantasma.md|Phantasma]] · [[armas/primarias/drakgoon.md|Drakgoon]] · [[armas/primarias/exergis.md|Exergis]] · [[armas/primarias/convectrix.md|Convectrix]] · [[armas/primarias/strun.md|Strun]] · [[armas/primarias/vermisplicer.md|Vermisplicer]]

**Snipers:** [[armas/primarias/rubico.md|Rubico]] · [[armas/primarias/lanka.md|Lanka]] · [[armas/primarias/vectis.md|Vectis]] · [[armas/primarias/opticor.md|Opticor]] · [[armas/primarias/komorex.md|Komorex]] · [[armas/primarias/vulkar.md|Vulkar]] · [[armas/primarias/snipetron.md|Snipetron]] · [[armas/primarias/kuva_chakkhurr.md|Kuva Chakkhurr]]

**Arcos:** [[armas/primarias/paris.md|Paris]] · [[armas/primarias/cernos.md|Cernos]] · [[armas/primarias/daikyu.md|Daikyu]] · [[armas/primarias/nataruk.md|Nataruk]] · [[armas/primarias/lenz.md|Lenz]] · [[armas/primarias/zhuge.md|Zhuge]] · [[armas/primarias/attica.md|Attica]] · [[armas/primarias/sporothrix.md|Sporothrix]] · [[armas/primarias/rakta_cernos.md|Rakta Cernos]] · [[armas/primarias/proboscis_cernos.md|Proboscis Cernos]] · [[armas/primarias/kuva_bramma.md|Kuva Bramma]]

**Lançadores:** [[armas/primarias/ogris.md|Ogris]] · [[armas/primarias/tonkor.md|Tonkor]] · [[armas/primarias/zarr.md|Zarr]] · [[armas/primarias/penta.md|Penta]] · [[armas/primarias/simulor.md|Simulor]] · [[armas/primarias/quanta.md|Quanta]] · [[armas/primarias/tenet_envoy.md|Tenet Envoy]] · [[armas/primarias/trumna.md|Trumna]] · [[armas/primarias/scourge.md|Scourge]] · [[armas/primarias/javlok.md|Javlok]] · [[armas/primarias/mutalist_quanta.md|Mutalist Quanta]] · [[armas/primarias/miter.md|Miter]]

**Especiais/Incarnon:** [[armas/primarias/ignis.md|Ignis]] · [[armas/primarias/ferrox.md|Ferrox]] · [[armas/primarias/fulmin.md|Fulmin]] · [[armas/primarias/shedu.md|Shedu]] · [[armas/primarias/phenmor.md|Phenmor]] · [[armas/primarias/felarx.md|Felarx]] · [[armas/primarias/ambassador.md|Ambassador]] · [[armas/primarias/paracyst.md|Paracyst]] · [[armas/primarias/harpak.md|Harpak]]

### Secundárias
**Pistolas:** [[armas/secundarias/lex.md|Lex]] · [[armas/secundarias/magnus.md|Magnus]] · [[armas/secundarias/vasto.md|Vasto]] · [[armas/secundarias/sicarus.md|Sicarus]] · [[armas/secundarias/bronco.md|Bronco]] · [[armas/secundarias/detron.md|Detron]] · [[armas/secundarias/seer.md|Seer]] · [[armas/secundarias/nukor.md|Nukor]] · [[armas/secundarias/pandero.md|Pandero]] · [[armas/secundarias/knell.md|Knell]] · [[armas/secundarias/epitaph.md|Epitaph]] · [[armas/secundarias/laetum.md|Laetum]] · [[armas/secundarias/athodai.md|Athodai]] · [[armas/secundarias/brakk.md|Brakk]] · [[armas/secundarias/lato.md|Lato]]

**Pistolas Duplas:** [[armas/secundarias/aklex.md|Aklex]] · [[armas/secundarias/akbolto.md|Akbolto]] · [[armas/secundarias/akstiletto.md|Akstiletto]] · [[armas/secundarias/aksomati.md|Aksomati]] · [[armas/secundarias/akjagara.md|Akjagara]] · [[armas/secundarias/akvasto.md|Akvasto]] · [[armas/secundarias/twin_vipers.md|Twin Vipers]] · [[armas/secundarias/twin_grakata.md|Twin Grakata]] · [[armas/secundarias/akzani.md|Akzani]] · [[armas/secundarias/akarius.md|Akarius]] · [[armas/secundarias/tenet_diplos.md|Tenet Diplos]] · [[armas/secundarias/kuva_twin_stubbas.md|Kuva Twin Stubbas]]

**Arremesso:** [[armas/secundarias/despair.md|Despair]] · [[armas/secundarias/hikou.md|Hikou]] · [[armas/secundarias/spira.md|Spira]] · [[armas/secundarias/fusilai.md|Fusilai]] · [[armas/secundarias/castanas.md|Castanas]] · [[armas/secundarias/zakti.md|Zakti]]

**Kitguns:** [[armas/secundarias/rattleguts.md|Rattleguts]] · [[armas/secundarias/catchmoon.md|Catchmoon]] · [[armas/secundarias/tombfinger.md|Tombfinger]] · [[armas/secundarias/gaze.md|Gaze]]

**Especiais/Incarnon:** [[armas/secundarias/gammacor.md|Gammacor]] · [[armas/secundarias/staticor.md|Staticor]] · [[armas/secundarias/sonicor.md|Sonicor]] · [[armas/secundarias/cyanex.md|Cyanex]] · [[armas/secundarias/kompressa.md|Kompressa]] · [[armas/secundarias/tenet_cycron.md|Tenet Cycron]] · [[armas/secundarias/ocucor.md|Ocucor]] · [[armas/secundarias/atomos.md|Atomos]] · [[armas/secundarias/bubonico.md|Bubonico]] · [[armas/secundarias/kulstar.md|Kulstar]] · [[armas/secundarias/acrid.md|Acrid]] · [[armas/secundarias/embolist.md|Embolist]]

### Brancas
**Espadas:** [[armas/brancas/skana.md|Skana]] · [[armas/brancas/nikana.md|Nikana]] · [[armas/brancas/destreza.md|Destreza]] · [[armas/brancas/pangolin_sword.md|Pangolin]] · [[armas/brancas/mire.md|Mire]] · [[armas/brancas/innodem.md|Innodem]] · [[armas/brancas/krohkur.md|Krohkur]] · [[armas/brancas/dakra_prime.md|Dakra Prime]]

**Espadas Pesadas:** [[armas/brancas/galatine.md|Galatine]] · [[armas/brancas/gram.md|Gram]] · [[armas/brancas/paracesis.md|Paracesis]] · [[armas/brancas/skiajati.md|Skiajati]] · [[armas/brancas/pennant.md|Pennant]] · [[armas/brancas/vitrica.md|Vitrica]] · [[armas/brancas/tatsu.md|Tatsu]] · [[armas/brancas/war.md|War]] · [[armas/brancas/tenet_exec.md|Tenet Exec]]

**Espadas Duplas:** [[armas/brancas/dual_kamas.md|Dual Kamas]] · [[armas/brancas/dual_ichor.md|Dual Ichor]] · [[armas/brancas/boltace.md|Boltace]] · [[armas/brancas/okina.md|Okina]] · [[armas/brancas/fang.md|Fang]] · [[armas/brancas/dual_ether.md|Dual Ether]]

**Lanças:** [[armas/brancas/guandao.md|Guandao]] · [[armas/brancas/orthos.md|Orthos]] · [[armas/brancas/lesion.md|Lesion]] · [[armas/brancas/tipedo.md|Tipedo]] · [[armas/brancas/sydon.md|Sydon]] · [[armas/brancas/tonbo.md|Tonbo]] · [[armas/brancas/kesheg.md|Kesheg]] · [[armas/brancas/prova.md|Prova]]

**Cajados / Nunchaku:** [[armas/brancas/bo.md|Bo]] · [[armas/brancas/jat_kusar.md|Jat Kusar]] · [[armas/brancas/shaku.md|Shaku]] · [[armas/brancas/ninkondi.md|Ninkondi]]

**Martelos:** [[armas/brancas/fragor.md|Fragor]] · [[armas/brancas/jat_kittag.md|Jat Kittag]] · [[armas/brancas/magistar.md|Magistar]] · [[armas/brancas/volnus.md|Volnus]] · [[armas/brancas/arca_titron.md|Arca Titron]] · [[armas/brancas/kuva_shildeg.md|Kuva Shildeg]]

**Foices / Glaives:** [[armas/brancas/hate.md|Hate]] · [[armas/brancas/reaper_prime.md|Reaper Prime]] · [[armas/brancas/anku.md|Anku]] · [[armas/brancas/glaive.md|Glaive]] · [[armas/brancas/orvius.md|Orvius]] · [[armas/brancas/xoris.md|Xoris]] · [[armas/brancas/halikar.md|Halikar]] · [[armas/brancas/tenet_grigori.md|Tenet Grigori]]

**Garras / Socos:** [[armas/brancas/venka.md|Venka]] · [[armas/brancas/tekko.md|Tekko]] · [[armas/brancas/furax.md|Furax]] · [[armas/brancas/hirudo.md|Hirudo]] · [[armas/brancas/ripkas.md|Ripkas]]

**Tonfas:** [[armas/brancas/kronen.md|Kronen]] · [[armas/brancas/ohma.md|Ohma]] · [[armas/brancas/praedos.md|Praedos]]

**Chicotes / Lâmina e Chicote:** [[armas/brancas/atterax.md|Atterax]] · [[armas/brancas/scoliac.md|Scoliac]] · [[armas/brancas/lecta.md|Lecta]] · [[armas/brancas/galvacord.md|Galvacord]] · [[armas/brancas/lacera.md|Lacera]] · [[armas/brancas/mios.md|Mios]] · [[armas/brancas/arum_spinosa.md|Arum Spinosa]]

**Espingardas Melee:** [[armas/brancas/redeemer.md|Redeemer]] · [[armas/brancas/stropha.md|Stropha]] · [[armas/brancas/sarpa.md|Sarpa]] · [[armas/brancas/vastilok.md|Vastilok]]

**Espada e Escudo:** [[armas/brancas/silva_and_aegis.md|Silva e Aegis]] · [[armas/brancas/sigma_and_octantis.md|Sigma e Octantis]] · [[armas/brancas/ack_and_brunt.md|Ack e Brunt]]

### Archwing
**Arch-Guns:** [[armas/archwing/mausolon.md|Mausolon]] · [[armas/archwing/larkspur.md|Larkspur]] · [[armas/archwing/imperator.md|Imperator]] · [[armas/archwing/velocitus.md|Velocitus]] · [[armas/archwing/phaedra.md|Phaedra]] · [[armas/archwing/fluctus.md|Fluctus]] · [[armas/archwing/grattler.md|Grattler]] · [[armas/archwing/cyngas.md|Cyngas]] · [[armas/archwing/corvas.md|Corvas]] · [[armas/archwing/cortege.md|Cortege]] · [[armas/archwing/morgha.md|Morgha]] · [[armas/archwing/dual_decurion.md|Dual Decurion]] · [[armas/archwing/kuva_ayanga.md|Kuva Ayanga]] · [[armas/archwing/kuva_grattler.md|Kuva Grattler]]

**Arch-Melee:** [[armas/archwing/onorix.md|Onorix]] · [[armas/archwing/veritux.md|Veritux]] · [[armas/archwing/kaszas.md|Kaszas]] · [[armas/archwing/knux.md|Knux]] · [[armas/archwing/centaur.md|Centaur]] · [[armas/archwing/prisma_veritux.md|Prisma Veritux]]


## 💡 Curiosidades — Warframe — Segunda Mente


- Braton foi a primeira arma primária disponível no jogo — acompanha o Excalibur no tutorial desde 2013.
- O Ignis Wraith foi distribuído via evento e só pode ser obtido por troca com outros jogadores ou pesquisa de clã — nunca volta ao mercado diretamente.
- Paracesis é a única arma com dano percentual contra Sentients — foi projetada especificamente para a quest The Sacrifice.
- A Nataruk é o único arco obtido inteiramente por gameplay de caça/pesca — disponível em Cetus após The New War.
- War e Broken War têm origem narrativa no lore — War pertencia ao Stalker e foi fragmentada durante The Second Dream.
- O Xoris foi introduzido com a quest The Deadlock Protocol e tem interação única com a habilidade Specter de Protea.
- Kuva Nukor foi por muito tempo a Secundária com maior status chance do jogo — central em builds de Condition Overload.
- O sistema de Kitguns (Fortuna) e Zaws (Cetus) permite criar armas únicas com stats personalizados via componentes modulares.
- Mausolon foi a primeira Arch-Gun de fogo automático projetada para uso terrestre via Zenith Crown.
- Skiajati é a espada pessoal do Umbra — dropa apenas em The Sacrifice e tem efeito de invisibilidade ao executar inimigos.


## 🔗 Relacionados — Warframe — Segunda Mente


| Índice | Relação |
|---|---|
| [[armas/primarias/_Armas _Primarias _Indice.md\|Primárias]] | Modos de disparo, munição, mecânicas exclusivas de primárias |
| [[armas/secundarias/_Armas _Secundarias _Indice.md\|Secundárias]] | Kitguns, dual-wield, mecânicas exclusivas de secundárias |
| [[armas/brancas/_Armas _Brancas _Indice.md\|Brancas]] | Stances por tipo, combo counter, heavy attacks |
| [[armas/archwing/_Armas _Archwing _Indice.md\|Archwing]] | Modos espacial/terrestre, deployer, pool de mods |
| [[mods/_Mods _Indice.md\|Mods]] | Mods que modificam stats de armas |
| [[recursos/_Recursos _Indice.md\|Recursos]] | Materiais usados no craft de armas |
| [[locais/_Locais _Indice.md\|Locais]] | Planetas onde drops e fontes ocorrem |
| [[warframes/_Warframes _Indice.md\|Warframes]] | Frames que amplificam armas por habilidades |

----------------------------------------

## Seção: armas\primarias — Warframe — Segunda Mente

### 📄 arquivo: _Armas _Primarias _Indice.md

# Armas Primárias — Índice

> [!quote]
> *"A escolha da primária define o alcance do Tenno antes do inimigo chegar ao corpo-a-corpo."*


## 📊 Visão Geral — Warframe — Segunda Mente


Armas primárias ocupam o slot principal do Tenno e são a primeira linha de combate à distância. São as armas com maior variedade de mecânicas do jogo — de rifles automáticos a arcos de carga, lança-chamas, snipers e lançadores de projéteis explosivos.

**Slot:** Primário · **Mods:** 8 slots + Exilus (com adaptador) + Arcane (com adaptador)


## Modos de Disparo — Warframe — Segunda Mente


| Modo | Descrição | Exemplos |
|---|---|---|
| **Automático** | Disparo contínuo enquanto o gatilho é pressionado | Braton, Soma, Grakata, Gorgon, Karak |
| **Semi-Auto** | Um disparo por clique | Latron, Sybaris, Vectis |
| **Burst** | Rajada de N projéteis por clique | Tiberon (modo burst), Hind |
| **Carga (Charge)** | Segurar para acumular dano antes de disparar | Lanka, Opticor, Nataruk, Daikyu |
| **Contínuo (Beam)** | Feixe de energia sem projéteis discretos | Amprex, Flux Rifle, Glaxion, Ignis |
| **Progressivo (Ramp-up)** | Fire rate aumenta com o tempo de disparo | Soma Prime, Kohm, Tenora |
| **Explosivo (AoE)** | Projéteis com raio de explosão ao impacto | Ogris, Tonkor, Kuva Bramma, Zarr, Penta |
| **Múltiplos Modos** | Alterna entre dois modos via input | Tiberon, Stradavar, Panthera, Fulmin |

> [!note] Beam weapons e Status
> Armas de feixe (beam) aplicam status a cada tick de dano por segundo, não por projétil. A status chance é calculada de forma diferente — 100% de status em beam significa proc garantido a cada tick.


## Tipos de Munição — Warframe — Segunda Mente


| Tipo | Armas que Usam | Observações |
|---|---|---|
| **Rifle** | Rifles de assalto, semi-auto, lança-chamas, beam | Mais abundante — dropa de maioria dos inimigos |
| **Espingarda** | Todas as espingardas (shotguns) | Pool separado do rifle |
| **Sniper** | Snipers (Rubico, Lanka, Vectis, Vulkar) | Pool pequeno — poucos drops por missão |
| **Arco** | Arcos (Paris, Cernos, Daikyu, Nataruk) | Projéteis físicos, alguns recuperáveis |
| **Especial** | Varia por arma (Lançadores, Rifles Especiais) | Depende da arma específica |


## Mecânicas Especiais — Warframe — Segunda Mente


**Punch-Through:** Projétil atravessa inimigos e/ou objetos. Inato em algumas armas (Boltor, Ferrox). Adicionável via mods: Shred, Metal Auger, Terminal Velocity.

**Espingardas e Status por Projétil:** Espingardas disparam múltiplos pellets por tiro. Cada pellet tem sua própria chance de status — na prática, armas com alta status chance e múltiplos pellets aplicam vários procs por disparo.

**Críticos em Arcos:** Arcos têm Headshot Multiplier inato — tiros na cabeça multiplicam o dano crítico. Ideal para builds de crit com Lanka, Rubico Prime.

**Incarnon Genesis:** Felarx e Phenmor possuem modo Incarnon. Ao cumprir um objetivo de evolução em combate (ex: 50 headshots), a arma se transforma temporariamente em uma forma alternativa mais poderosa com mecânicas distintas. Obtidas via Duviri Paradox.

**Rifles com Múltiplos Modos:** Algumas armas alternam modo de disparo — Tiberon alterna Auto/Burst/Semi, Stradavar alterna Auto/Semi, Fulmin alterna automático elétrico/disparo único.


## Lista Completa (129) — Warframe — Segunda Mente


| Arma | Tipo | Fonte |
|---|---|---|
| [[armas/primarias/acceltra.md\|Acceltra]] | Rifle de Assalto | Drop (Demolyst Manic, Steel Path) |
| [[armas/primarias/acceltra_prime.md\|Acceltra Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/ambassador.md\|Ambassador]] | Rifle de Assalto | Drop (Amalgam, Jupiter) |
| [[armas/primarias/amprex.md\|Amprex]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[armas/primarias/arca_plasmor.md\|Arca Plasmor]] | Espingarda | Pesquisa de Clã (Corpus) |
| [[armas/primarias/astilla.md\|Astilla]] | Espingarda | Pesquisa de Clã (Corpus) |
| [[armas/primarias/astilla_prime.md\|Astilla Prime]] | Espingarda | Relíquias (Prime) |
| [[armas/primarias/attica.md\|Attica]] | Arco | Mercado (blueprint) |
| [[armas/primarias/battacor.md\|Battacor]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[armas/primarias/baza.md\|Baza]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/baza_prime.md\|Baza Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/boltor.md\|Boltor]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/boltor_prime.md\|Boltor Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/braton.md\|Braton]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/braton_prime.md\|Braton Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/braton_vandal.md\|Braton Vandal]] | Rifle de Assalto | Evento / Drop (Acolytes) |
| [[armas/primarias/buzlok.md\|Buzlok]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/cedo.md\|Cedo]] | Espingarda | Pesquisa de Clã (Entrati) |
| [[armas/primarias/cernos.md\|Cernos]] | Arco | Mercado (blueprint) |
| [[armas/primarias/cernos_prime.md\|Cernos Prime]] | Arco | Relíquias (Prime) |
| [[armas/primarias/convectrix.md\|Convectrix]] | Espingarda | Pesquisa de Clã (Corpus) |
| [[armas/primarias/corinth.md\|Corinth]] | Espingarda | Mercado (blueprint) |
| [[armas/primarias/corinth_prime.md\|Corinth Prime]] | Espingarda | Relíquias (Prime) |
| [[armas/primarias/daikyu.md\|Daikyu]] | Arco | Mercado (blueprint) |
| [[armas/primarias/dera.md\|Dera]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/dera_vandal.md\|Dera Vandal]] | Rifle de Assalto | Nightwave / Evento |
| [[armas/primarias/dex_sybaris.md\|Dex Sybaris]] | Rifle Semi-Auto | Evento (Aniversário DE) |
| [[armas/primarias/drakgoon.md\|Drakgoon]] | Espingarda | Mercado (blueprint) |
| [[armas/primarias/exergis.md\|Exergis]] | Espingarda | Pesquisa de Clã (Corpus) |
| [[armas/primarias/felarx.md\|Felarx]] | Incarnon | Incarnon (Duviri) |
| [[armas/primarias/ferrox.md\|Ferrox]] | Rifle Especial | Mercado (blueprint) |
| [[armas/primarias/flux_rifle.md\|Flux Rifle]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[armas/primarias/fulmin.md\|Fulmin]] | Rifle Especial | Drop (Amalgam, Jupiter) |
| [[armas/primarias/fulmin_prime.md\|Fulmin Prime]] | Rifle Especial | Relíquias (Prime) |
| [[armas/primarias/glaxion.md\|Glaxion]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[armas/primarias/glaxion_vandal.md\|Glaxion Vandal]] | Rifle de Assalto | Nightwave / Evento |
| [[armas/primarias/gorgon.md\|Gorgon]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/gorgon_wraith.md\|Gorgon Wraith]] | Rifle de Assalto | Nightwave / Evento |
| [[armas/primarias/grakata.md\|Grakata]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/harpak.md\|Harpak]] | Rifle Especial | Mercado (blueprint) |
| [[armas/primarias/hek.md\|Hek]] | Espingarda | Mercado (blueprint) |
| [[armas/primarias/hind.md\|Hind]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/ignis.md\|Ignis]] | Lança-Chamas | Pesquisa de Clã (Grineer) |
| [[armas/primarias/ignis_wraith.md\|Ignis Wraith]] | Lança-Chamas | Pesquisa de Clã (blueprint tradável) / Evento |
| [[armas/primarias/javlok.md\|Javlok]] | Lançador | Mercado (blueprint) |
| [[armas/primarias/karak.md\|Karak]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/karak_wraith.md\|Karak Wraith]] | Rifle de Assalto | Evento / Drop (Acolytes) |
| [[armas/primarias/kohm.md\|Kohm]] | Espingarda | Mercado (blueprint) |
| [[armas/primarias/komorex.md\|Komorex]] | Sniper | Pesquisa de Clã (Corpus) |
| [[armas/primarias/kuva_bramma.md\|Kuva Bramma]] | Lançador | Kuva Lich |
| [[armas/primarias/kuva_chakkhurr.md\|Kuva Chakkhurr]] | Sniper | Kuva Lich |
| [[armas/primarias/kuva_hek.md\|Kuva Hek]] | Espingarda | Kuva Lich |
| [[armas/primarias/kuva_ogris.md\|Kuva Ogris]] | Lançador | Kuva Lich |
| [[armas/primarias/kuva_quartakk.md\|Kuva Quartakk]] | Rifle de Assalto | Kuva Lich |
| [[armas/primarias/kuva_tonkor.md\|Kuva Tonkor]] | Lançador | Kuva Lich |
| [[armas/primarias/kuva_zarr.md\|Kuva Zarr]] | Lançador | Kuva Lich |
| [[armas/primarias/lanka.md\|Lanka]] | Sniper | Mercado (blueprint) |
| [[armas/primarias/latron.md\|Latron]] | Rifle Semi-Auto | Mercado (blueprint) |
| [[armas/primarias/latron_prime.md\|Latron Prime]] | Rifle Semi-Auto | Relíquias (Prime) |
| [[armas/primarias/latron_wraith.md\|Latron Wraith]] | Rifle Semi-Auto | Nightwave / Evento |
| [[armas/primarias/lenz.md\|Lenz]] | Arco | Mercado (blueprint) |
| [[armas/primarias/miter.md\|Miter]] | Lançador | Mercado (blueprint) |
| [[armas/primarias/mk1_braton.md\|MK1-Braton]] | Rifle de Assalto | Starter / Mercado |
| [[armas/primarias/mutalist_quanta.md\|Mutalist Quanta]] | Lançador | Drop (Invasões Infested, Eris) |
| [[armas/primarias/nataruk.md\|Nataruk]] | Arco | Nakak, Cetus (pós The New War) |
| [[armas/primarias/ogris.md\|Ogris]] | Lançador | Mercado (blueprint) |
| [[armas/primarias/opticor.md\|Opticor]] | Sniper | Pesquisa de Clã (Corpus) |
| [[armas/primarias/opticor_vandal.md\|Opticor Vandal]] | Sniper | Nightwave / Evento |
| [[armas/primarias/panthera.md\|Panthera]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[armas/primarias/panthera_prime.md\|Panthera Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/paracyst.md\|Paracyst]] | Rifle Especial | Mercado (blueprint) |
| [[armas/primarias/paris.md\|Paris]] | Arco | Mercado (blueprint) |
| [[armas/primarias/paris_prime.md\|Paris Prime]] | Arco | Relíquias (Prime) |
| [[armas/primarias/penta.md\|Penta]] | Lançador | Mercado (blueprint) |
| [[armas/primarias/phantasma.md\|Phantasma]] | Espingarda | Pesquisa de Clã (Entrati) |
| [[armas/primarias/phantasma_prime.md\|Phantasma Prime]] | Espingarda | Relíquias (Prime) |
| [[armas/primarias/phenmor.md\|Phenmor]] | Incarnon | Incarnon (Duviri) |
| [[armas/primarias/prisma_grakata.md\|Prisma Grakata]] | Rifle de Assalto | Baro Ki'Teer / Nightwave |
| [[armas/primarias/proboscis_cernos.md\|Proboscis Cernos]] | Arco | Pesquisa de Clã (Entrati) |
| [[armas/primarias/quanta.md\|Quanta]] | Lançador | Pesquisa de Clã (Corpus) |
| [[armas/primarias/quanta_vandal.md\|Quanta Vandal]] | Lançador | Nightwave / Evento |
| [[armas/primarias/rakta_cernos.md\|Rakta Cernos]] | Arco | Sindicato (Red Veil) |
| [[armas/primarias/rubico.md\|Rubico]] | Sniper | Mercado (blueprint) |
| [[armas/primarias/rubico_prime.md\|Rubico Prime]] | Sniper | Relíquias (Prime) |
| [[armas/primarias/sancti_tigris.md\|Sancti Tigris]] | Espingarda | Sindicato (New Loka) |
| [[armas/primarias/scourge.md\|Scourge]] | Lançador | Pesquisa de Clã (Entrati) |
| [[armas/primarias/scourge_prime.md\|Scourge Prime]] | Lançador | Relíquias (Prime) |
| [[armas/primarias/secura_penta.md\|Secura Penta]] | Lançador | Sindicato (Perrin Sequence) |
| [[armas/primarias/shedu.md\|Shedu]] | Rifle Especial | Drop (Sentients, Murex — Empyrean) |
| [[armas/primarias/simulor.md\|Simulor]] | Lançador | Pesquisa de Clã (Corpus) |
| [[armas/primarias/snipetron.md\|Snipetron]] | Sniper | Baro Ki'Teer |
| [[armas/primarias/snipetron_vandal.md\|Snipetron Vandal]] | Sniper | Evento |
| [[armas/primarias/sobek.md\|Sobek]] | Espingarda | Mercado (blueprint) |
| [[armas/primarias/soma.md\|Soma]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/soma_prime.md\|Soma Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/sporothrix.md\|Sporothrix]] | Arco | Pesquisa de Clã (Entrati) |
| [[armas/primarias/stahlta.md\|Stahlta]] | Rifle de Assalto | Pesquisa de Clã (Entrati) |
| [[armas/primarias/stradavar.md\|Stradavar]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/stradavar_prime.md\|Stradavar Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/strun.md\|Strun]] | Espingarda | Mercado (blueprint) |
| [[armas/primarias/strun_wraith.md\|Strun Wraith]] | Espingarda | Nightwave / Evento |
| [[armas/primarias/supra.md\|Supra]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[armas/primarias/supra_vandal.md\|Supra Vandal]] | Rifle de Assalto | Nightwave / Evento |
| [[armas/primarias/sybaris.md\|Sybaris]] | Rifle Semi-Auto | Mercado (blueprint) |
| [[armas/primarias/sybaris_prime.md\|Sybaris Prime]] | Rifle Semi-Auto | Relíquias (Prime) |
| [[armas/primarias/synoid_simulor.md\|Synoid Simulor]] | Lançador | Sindicato (Cephalon Suda) |
| [[armas/primarias/telos_boltor.md\|Telos Boltor]] | Rifle de Assalto | Sindicato (Arbiters of Hexis) |
| [[armas/primarias/tenet_arca_plasmor.md\|Tenet Arca Plasmor]] | Espingarda | Irmãs de Parvos |
| [[armas/primarias/tenet_envoy.md\|Tenet Envoy]] | Lançador | Irmãs de Parvos |
| [[armas/primarias/tenet_ferrox.md\|Tenet Ferrox]] | Rifle Especial | Irmãs de Parvos |
| [[armas/primarias/tenet_flux_rifle.md\|Tenet Flux Rifle]] | Rifle de Assalto | Irmãs de Parvos |
| [[armas/primarias/tenora.md\|Tenora]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/tenora_prime.md\|Tenora Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/tiberon.md\|Tiberon]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/tiberon_prime.md\|Tiberon Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[armas/primarias/tigris.md\|Tigris]] | Espingarda | Mercado (blueprint) |
| [[armas/primarias/tigris_prime.md\|Tigris Prime]] | Espingarda | Relíquias (Prime) |
| [[armas/primarias/tonkor.md\|Tonkor]] | Lançador | Mercado (blueprint) |
| [[armas/primarias/trumna.md\|Trumna]] | Lançador | Pesquisa de Clã (Entrati) |
| [[armas/primarias/vaykor_hek.md\|Vaykor Hek]] | Espingarda | Sindicato (Steel Meridian) |
| [[armas/primarias/vectis.md\|Vectis]] | Sniper | Mercado (blueprint) |
| [[armas/primarias/vectis_prime.md\|Vectis Prime]] | Sniper | Relíquias (Prime) |
| [[armas/primarias/veldt.md\|Veldt]] | Rifle de Assalto | Mercado (blueprint) |
| [[armas/primarias/vermisplicer.md\|Vermisplicer]] | Espingarda | Pesquisa de Clã (Entrati) |
| [[armas/primarias/vulkar.md\|Vulkar]] | Sniper | Mercado (blueprint) |
| [[armas/primarias/vulkar_wraith.md\|Vulkar Wraith]] | Sniper | Nightwave / Evento |
| [[armas/primarias/zarr.md\|Zarr]] | Lançador | Mercado (blueprint) |
| [[armas/primarias/zhuge.md\|Zhuge]] | Arco | Mercado (blueprint) |
| [[armas/primarias/zhuge_prime.md\|Zhuge Prime]] | Arco | Relíquias (Prime) |


## 🔗 Relacionados — Warframe — Segunda Mente


| Índice | Relação |
|---|---|
| [[armas/_Armas _Indice.md\|Armas]] | Índice geral — todas as categorias de arma |
| [[mods/armas/_Mods Armas _Indice.md\|Mods de Armas]] | Mods de rifle, espingarda, sniper e arco |
| [[recursos/_Recursos _Indice.md\|Recursos]] | Materiais para crafting de primárias |
| [[locais/_Locais _Indice.md\|Locais]] | Planetas onde drops de primárias ocorrem |

----------------------------------------

## Seção: armas\secundarias — Warframe — Segunda Mente

### 📄 arquivo: _Armas _Secundarias _Indice.md

# Armas Secundárias — Índice

> [!quote]
> *"Quando a primária cai, a secundária define quem sobrevive."*


## 📊 Visão Geral — Warframe — Segunda Mente


Armas secundárias ocupam o slot de pistola do Tenno. São mais compactas que as primárias mas cobrem funções diversas — pistolas de precisão, armas de arremesso, espingardas secundárias, kits modulares e canhões de braço.

**Slot:** Secundário · **Mods:** 8 slots + Exilus (com adaptador) + Arcane (com adaptador)


## Sistema Kitgun — Warframe — Segunda Mente


Kitguns são secundárias modulares montadas em Fortuna (Orb Vallis, Vênus) pela NPC **Rude Zuud**. Combinam três componentes independentes:

| Componente | Função | Exemplos |
|---|---|---|
| **Chamber** | Define o tipo de disparo e mecânica central | Rattleguts, Catchmoon, Tombfinger, Gaze |
| **Grip** | Afeta dano base, crit chance e alcance | Gibber, Ramble, Lovetap, Haymaker, Rattler |
| **Loader** | Afeta status chance, magazine e reload speed | Zipneedle, Thunderdrum, Slap, Deepbreath |

> [!important] Gilding obrigatório
> Kitguns precisam ser **gildadas** (rank 30 + custo em Ostron Standing) para:
> - Receber o nome permanente e contribuir com Mastery
> - Ativar o bônus passivo exclusivo da Chamber


## Armas de Arremesso (Thrown) — Warframe — Segunda Mente


Armas como Hikou, Spira, Despair, Fusilai, Zakti e Castanas são arremessadas em vez de disparadas. Mecânicas únicas:

| Mecânica | Detalhe |
|---|---|
| **Status por projétil** | Cada projétil arremessado tem chance independente de status |
| **Multishot** | Adiciona projéteis arremessados simultâneos por lançamento |
| **Recuperação** | A maioria não recupera projéteis — consome ammo normalmente |
| **Explosivas** | Castanas e Sancti Castanas explodem por timer ou contato |


## Prefixo Ak- (Dual-Wield) — Warframe — Segunda Mente


Armas com prefixo **Ak-** são versões dual-wield construídas usando **duas unidades** da pistola base como componente de crafting:

| Pistola Base | Versão Dual | Craft |
|---|---|---|
| Lex | Aklex | 2× Lex |
| Bolto | Akbolto | 2× Bolto |
| Vasto | Akvasto | 2× Vasto |
| Jagara | Akjagara | 2× Jagara |
| Somati | Aksomati | Pesquisa de Clã |
| Stiletto | Akstiletto | Mercado |
| Zani | Akzani | Pesquisa de Clã (Cetus) |

> [!note]
> Versões Ak- têm fire rate maior mas magazine dobrado e reload mais lento. Exigem que as armas base já estejam construídas (ou compradas) antes do craft.


## Incarnon Genesis — Warframe — Segunda Mente


**Laetum** é a única secundária Incarnon do Duviri Paradox. Evolui durante a missão ao cumprir um objetivo de evolução — transforma-se em uma forma alternativa mais poderosa com mecânica de disparo distinta. Obtida via missões do Duviri Circuit.


## Lista Completa (93) — Warframe — Segunda Mente


| Arma | Tipo | Fonte |
|---|---|---|
| [[armas/secundarias/acrid.md\|Acrid]] | Especial | Drop (Invasões Infested) |
| [[armas/secundarias/akarius.md\|Akarius]] | Pistolas Duplas | Pesquisa de Clã (Entrati) |
| [[armas/secundarias/akbolto.md\|Akbolto]] | Pistolas Duplas | Mercado (2× Bolto) |
| [[armas/secundarias/akbolto_prime.md\|Akbolto Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[armas/secundarias/akjagara.md\|Akjagara]] | Pistolas Duplas | Mercado (blueprint) |
| [[armas/secundarias/akjagara_prime.md\|Akjagara Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[armas/secundarias/aklex.md\|Aklex]] | Pistolas Duplas | Mercado (2× Lex) |
| [[armas/secundarias/aklex_prime.md\|Aklex Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[armas/secundarias/aksomati.md\|Aksomati]] | Pistolas Duplas | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/aksomati_prime.md\|Aksomati Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[armas/secundarias/akstiletto.md\|Akstiletto]] | Pistolas Duplas | Mercado (blueprint) |
| [[armas/secundarias/akstiletto_prime.md\|Akstiletto Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[armas/secundarias/akvasto.md\|Akvasto]] | Pistolas Duplas | Mercado (2× Vasto) |
| [[armas/secundarias/akvasto_prime.md\|Akvasto Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[armas/secundarias/akzani.md\|Akzani]] | Pistolas Duplas | Pesquisa de Clã (Cetus) |
| [[armas/secundarias/arca_scisco.md\|Arca Scisco]] | Pistola | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/athodai.md\|Athodai]] | Pistola | Fortuna (Old Mate, rank 5) |
| [[armas/secundarias/atomos.md\|Atomos]] | Especial | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/azima.md\|Azima]] | Especial | Nightwave / Evento |
| [[armas/secundarias/ballistica.md\|Ballistica]] | Arco Secundário | Mercado (blueprint) |
| [[armas/secundarias/ballistica_prime.md\|Ballistica Prime]] | Arco Secundário | Relíquias (Prime) |
| [[armas/secundarias/bolto.md\|Bolto]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/brakk.md\|Brakk]] | Pistola | Drop (Grustrag Three) / Invasões |
| [[armas/secundarias/bronco.md\|Bronco]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/bronco_prime.md\|Bronco Prime]] | Pistola | Relíquias (Prime) |
| [[armas/secundarias/bubonico.md\|Bubonico]] | Canhão de Braço | Pesquisa de Clã (Entrati) |
| [[armas/secundarias/castanas.md\|Castanas]] | Arremesso | Mercado (blueprint) |
| [[armas/secundarias/catchmoon.md\|Catchmoon]] | Kitgun | Kitgun (Fortuna) |
| [[armas/secundarias/cyanex.md\|Cyanex]] | Especial | Pesquisa de Clã (Entrati) |
| [[armas/secundarias/despair.md\|Despair]] | Arremesso | Drop (Stalker) |
| [[armas/secundarias/detron.md\|Detron]] | Pistola | Drop (Corrupted, Void) |
| [[armas/secundarias/dex_furis.md\|Dex Furis]] | Pistola | Evento (Aniversário DE) |
| [[armas/secundarias/embolist.md\|Embolist]] | Especial | Pesquisa de Clã (Grineer) |
| [[armas/secundarias/epitaph.md\|Epitaph]] | Pistola | Pesquisa de Clã (Entrati) |
| [[armas/secundarias/euphona_prime.md\|Euphona Prime]] | Pistola | Relíquias (Prime) |
| [[armas/secundarias/furis.md\|Furis]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/fusilai.md\|Fusilai]] | Arremesso | Nakak, Cetus (caça) |
| [[armas/secundarias/gammacor.md\|Gammacor]] | Especial | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/gaze.md\|Gaze]] | Kitgun | Kitgun (Fortuna) |
| [[armas/secundarias/hikou.md\|Hikou]] | Arremesso | Mercado (blueprint) |
| [[armas/secundarias/hikou_prime.md\|Hikou Prime]] | Arremesso | Relíquias (Prime) |
| [[armas/secundarias/knell.md\|Knell]] | Pistola | Pesquisa de Clã (Quills, Cetus) |
| [[armas/secundarias/knell_prime.md\|Knell Prime]] | Pistola | Relíquias (Prime) |
| [[armas/secundarias/kohmak.md\|Kohmak]] | Especial | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/kompressa.md\|Kompressa]] | Especial | Pesquisa de Clã (Entrati) |
| [[armas/secundarias/kulstar.md\|Kulstar]] | Especial | Pesquisa de Clã (Grineer) |
| [[armas/secundarias/kuva_brakk.md\|Kuva Brakk]] | Pistola | Kuva Lich |
| [[armas/secundarias/kuva_nukor.md\|Kuva Nukor]] | Pistola | Kuva Lich |
| [[armas/secundarias/kuva_seer.md\|Kuva Seer]] | Pistola | Kuva Lich |
| [[armas/secundarias/kuva_twin_stubbas.md\|Kuva Twin Stubbas]] | Pistolas Duplas | Kuva Lich |
| [[armas/secundarias/laetum.md\|Laetum]] | Incarnon | Incarnon (Duviri) |
| [[armas/secundarias/lato.md\|Lato]] | Pistola | Starter / Mercado |
| [[armas/secundarias/lato_prime.md\|Lato Prime]] | Pistola | Indisponível (Founder's Pack, 2013) |
| [[armas/secundarias/lato_vandal.md\|Lato Vandal]] | Pistola | Nightwave / Evento |
| [[armas/secundarias/lex.md\|Lex]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/lex_prime.md\|Lex Prime]] | Pistola | Relíquias (Prime) |
| [[armas/secundarias/magnus.md\|Magnus]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/magnus_prime.md\|Magnus Prime]] | Pistola | Relíquias (Prime) |
| [[armas/secundarias/mara_detron.md\|Mara Detron]] | Pistola | Baro Ki'Teer |
| [[armas/secundarias/nukor.md\|Nukor]] | Pistola | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/ocucor.md\|Ocucor]] | Especial | Pesquisa de Clã (Entrati) |
| [[armas/secundarias/pandero.md\|Pandero]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/pandero_prime.md\|Pandero Prime]] | Pistola | Relíquias (Prime) |
| [[armas/secundarias/rattleguts.md\|Rattleguts]] | Kitgun | Kitgun (Fortuna) |
| [[armas/secundarias/sancti_castanas.md\|Sancti Castanas]] | Arremesso | Sindicato (New Loka) |
| [[armas/secundarias/seer.md\|Seer]] | Pistola | Drop (Vor, Mercury — Tolstoj) |
| [[armas/secundarias/sicarus.md\|Sicarus]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/sicarus_prime.md\|Sicarus Prime]] | Pistola | Relíquias (Prime) |
| [[armas/secundarias/sonicor.md\|Sonicor]] | Especial | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/spira.md\|Spira]] | Arremesso | Mercado (blueprint) |
| [[armas/secundarias/spira_prime.md\|Spira Prime]] | Arremesso | Relíquias (Prime) |
| [[armas/secundarias/staticor.md\|Staticor]] | Especial | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/stubba.md\|Stubba]] | Especial | Pesquisa de Clã (Grineer) |
| [[armas/secundarias/stug.md\|Stug]] | Especial | Pesquisa de Clã (Corpus) |
| [[armas/secundarias/synoid_gammacor.md\|Synoid Gammacor]] | Especial | Sindicato (Cephalon Suda) |
| [[armas/secundarias/tenet_agendus.md\|Tenet Agendus]] | Especial | Irmãs de Parvos |
| [[armas/secundarias/tenet_cycron.md\|Tenet Cycron]] | Especial | Irmãs de Parvos |
| [[armas/secundarias/tenet_detron.md\|Tenet Detron]] | Pistola | Irmãs de Parvos |
| [[armas/secundarias/tenet_diplos.md\|Tenet Diplos]] | Pistolas Duplas | Irmãs de Parvos |
| [[armas/secundarias/tenet_plinx.md\|Tenet Plinx]] | Pistola | Irmãs de Parvos |
| [[armas/secundarias/tenet_spirex.md\|Tenet Spirex]] | Especial | Irmãs de Parvos |
| [[armas/secundarias/tombfinger.md\|Tombfinger]] | Kitgun | Kitgun (Fortuna) |
| [[armas/secundarias/twin_grakata.md\|Twin Grakata]] | Pistolas Duplas | Mercado (blueprint) |
| [[armas/secundarias/twin_vipers.md\|Twin Vipers]] | Pistolas Duplas | Mercado (blueprint) |
| [[armas/secundarias/twin_vipers_wraith.md\|Twin Vipers Wraith]] | Pistolas Duplas | Nightwave / Evento |
| [[armas/secundarias/vasto.md\|Vasto]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/vasto_prime.md\|Vasto Prime]] | Pistola | Relíquias (Prime) |
| [[armas/secundarias/velox.md\|Velox]] | Pistola | Drop (Corpus, Orb Vallis) |
| [[armas/secundarias/viper.md\|Viper]] | Pistola | Mercado (blueprint) |
| [[armas/secundarias/viper_wraith.md\|Viper Wraith]] | Pistola | Nightwave / Evento |
| [[armas/secundarias/zakti.md\|Zakti]] | Arremesso | Mercado (blueprint) |
| [[armas/secundarias/zakti_prime.md\|Zakti Prime]] | Arremesso | Relíquias (Prime) |
| [[armas/secundarias/zylok.md\|Zylok]] | Pistola | Nightwave / Evento |


## 🔗 Relacionados — Warframe — Segunda Mente


| Índice | Relação |
|---|---|
| [[armas/_Armas _Indice.md\|Armas]] | Índice geral — todas as categorias de arma |
| [[mods/armas/_Mods Armas _Indice.md\|Mods de Armas]] | Mods de pistola e secundária |
| [[recursos/_Recursos _Indice.md\|Recursos]] | Materiais para crafting de secundárias |
| [[locais/_Locais _Indice.md\|Locais]] | Planetas onde drops de secundárias ocorrem |

----------------------------------------

## Seção: armas\brancas — Warframe — Segunda Mente

### 📄 arquivo: _Armas _Brancas _Indice.md

# Armas Brancas — Índice

> [!quote]
> *"O verdadeiro poder do Tenno não está na arma — está nas mãos que a empunham."*


## 📊 Visão Geral — Warframe — Segunda Mente


Armas brancas (melee) são o slot de combate corpo-a-corpo do Tenno. São as armas com mecânicas mais profundas do jogo — **stances** que substituem completamente os ataques básicos, um **combo counter** que amplifica o dano progressivamente e **heavy attacks** devastadores que consomem o contador acumulado.

**Slot:** Melee · **Mods:** 8 slots + slot de Stance (exclusivo) + Exilus (com adaptador)


## Sistema de Stances — Warframe — Segunda Mente


Stances são **mods exclusivos de armas brancas** que substituem completamente os ataques normais por sequências de combos específicos da arma. São o sistema mais importante para entender o melee.

| Propriedade | Detalhe |
|---|---|
| **Slot exclusivo** | Stances ocupam um slot próprio — não contam nos 8 mods normais |
| **Capacidade de mods** | Cada stance tem um multiplicador (ex: 2×, 4×) que aumenta a capacidade total da arma |
| **Compatibilidade** | Cada stance é exclusiva de um tipo de arma (não intercambiável entre tipos) |
| **Fontes** | Drops de inimigos, Nightwave, pesquisa de clã, Cephalon Simaris |

### Stances por Tipo de Arma

| Tipo de Arma | Stances Disponíveis |
|---|---|
| Espada | Crimson Dervish · Swooping Falcon · Iron Phoenix · Vengeful Revenant · Blind Justice |
| Nikana | Tranquil Cleave · Decisive Judgement · Blind Justice |
| Espadim (Rapier) | Eleventh Storm · Pointed Wind |
| Espada Pesada | Rending Crane · Tempo Royale · Cleaving Whirlwind |
| Espadas Duplas | Swirling Tiger · Crossing Snakes · Dividing Blades |
| Adaga | Homing Fang · Pointed Wind |
| Adagas Duplas | Gnashing Payara · Spinning Needle |
| Lança (Polearm) | Shimmering Blight · Bleeding Willow · Typhoon's Edge |
| Cajado (Staff) | Clashing Forest · Flailing Branch |
| Nunchaku | Atlantas Struggle |
| Tonfa | Gemini Cross · Sovereign Outcast |
| Martelo | Crushing Ruin · Shattering Storm |
| Garras (Claws) | Vermillion Storm · Seismic Palm · Brutal Tide |
| Foice (Scythe) | Reaping Spiral · Stalking Fan |
| Glaive | Astral Twilight |
| Chicote (Whip) | Defiled Snapdragon · Burning Wasp |
| Lâmina e Chicote | Wise Razor |
| Espada e Escudo | Final Harbinger |
| Espingarda Melee (Gunblade) | Bullet Dance · High Noon |
| Leques (Warfan) | Slicing Feathers |


## Combo Counter — Warframe — Segunda Mente


O **Combo Counter** é um multiplicador que aumenta a cada golpe acertado e diminui após um período sem ataques (padrão: 5 segundos).

| Multiplicador | Golpes Necessários |
|---|---|
| 1.0× | 0 |
| 1.5× | 5 |
| 2.0× | 10 |
| 3.0× | 20 |

**Mods de Combo relevantes:**

| Mod | Efeito |
|---|---|
| **Blood Rush** | Aumenta crit chance com o multiplicador de combo |
| **Drifting Contact** | Aumenta a duração do combo counter (padrão 5s → até 15s) |
| **Weeping Wounds** | Aumenta status chance com o multiplicador de combo |
| **Berserker Fury** | Aumenta attack speed após acerto crítico |
| **Killing Blow** | Aumenta dano de heavy attack |


## Heavy Attacks — Warframe — Segunda Mente


Heavy attacks (botão de ataque segurado) **consomem todo o combo counter** para desferir um golpe de alto dano multiplicado:

- **Dano:** Proporcional ao multiplicador do combo consumido
- **Spin Attack (Heavy aéreo):** Versão rotacional com AoE — executado no ar
- **Weeping Wounds:** Funciona com heavy attacks (combo escala status)

> [!warning] Perda total do Combo
> Heavy attacks **zeram o combo counter imediatamente**. Builds que usam Blood Rush geralmente evitam heavy attacks para manter o multiplicador alto.


## Ataques Especiais — Warframe — Segunda Mente


| Tipo | Gatilho | Efeito |
|---|---|---|
| **Slam Attack** | Pular + heavy attack ao aterrissar | AoE radial proporcional ao combo |
| **Finisher (pé)** | Inimigo derrubado / vulnerável | Alto dano fixo + animação de execução |
| **Ground Finisher** | Inimigo no chão | Dano alto com animação específica |
| **Wall Attack** | Corrida em parede + ataque | Ataque durante parkour vertical |


## Zaws — Armas Brancas Modulares — Warframe — Segunda Mente


Zaws são brancas modulares montadas em **Cetus** (Planície de Eidolon) pelo NPC **Hok**. Três componentes:

| Componente | Função |
|---|---|
| **Strike** | Define o tipo da arma e dano base |
| **Grip** | Afeta dano e velocidade de ataque |
| **Link** | Afeta crit/status e capacidade de mods |

> [!tip]
> Zaws também precisam ser gildados (rank 30 + Ostron Standing) para receber o nome permanente e contribuir com Mastery.


## Lista Completa (135) — Warframe — Segunda Mente


| Arma | Tipo | Fonte |
|---|---|---|
| [[armas/brancas/ack_and_brunt.md\|Ack e Brunt]] | Espada e Escudo | Pesquisa de Clã (Grineer) |
| [[armas/brancas/anku.md\|Anku]] | Foice | Pesquisa de Clã (Grineer) |
| [[armas/brancas/arca_titron.md\|Arca Titron]] | Martelo | Pesquisa de Clã (Corpus) |
| [[armas/brancas/arum_spinosa.md\|Arum Spinosa]] | Lâmina e Chicote | Pesquisa de Clã (Entrati) |
| [[armas/brancas/atterax.md\|Atterax]] | Chicote | Mercado (blueprint) |
| [[armas/brancas/bo.md\|Bo]] | Cajado | Mercado (blueprint) |
| [[armas/brancas/bo_prime.md\|Bo Prime]] | Cajado | Relíquias (Prime) |
| [[armas/brancas/boltace.md\|Boltace]] | Espadas Duplas | Pesquisa de Clã (Corpus) |
| [[armas/brancas/broken_sword.md\|Broken Sword]] | Espada | Drop (Stalker) |
| [[armas/brancas/broken_war.md\|Broken War]] | Espada | Drop (Stalker — partes de War) |
| [[armas/brancas/ceramic_dagger.md\|Ceramic Dagger]] | Adaga | Mercado (blueprint) |
| [[armas/brancas/cobra_and_crane.md\|Cobra e Crane]] | Espada e Escudo | Pesquisa de Clã (Grineer) |
| [[armas/brancas/cronus.md\|Cronus]] | Espada | Drop (Ambulas, Pluto) |
| [[armas/brancas/dakra_prime.md\|Dakra Prime]] | Espada | Relíquias (Prime) |
| [[armas/brancas/dark_dagger.md\|Dark Dagger]] | Adaga | Mercado (blueprint) |
| [[armas/brancas/dark_split_sword.md\|Dark Split-Sword]] | Espada Pesada / Dupla | Mercado (blueprint) |
| [[armas/brancas/dark_sword.md\|Dark Sword]] | Espada | Mercado (blueprint) |
| [[armas/brancas/destreza.md\|Destreza]] | Espadim | Mercado (blueprint) |
| [[armas/brancas/destreza_prime.md\|Destreza Prime]] | Espadim | Relíquias (Prime) |
| [[armas/brancas/dragon_nikana.md\|Dragon Nikana]] | Nikana | Mercado (blueprint + componentes Clã) |
| [[armas/brancas/dual_cleavers.md\|Dual Cleavers]] | Espadas Duplas | Mercado (blueprint) |
| [[armas/brancas/dual_ether.md\|Dual Ether]] | Espadas Duplas | Mercado (blueprint) |
| [[armas/brancas/dual_heat_swords.md\|Dual Heat Swords]] | Espadas Duplas | Mercado (blueprint) |
| [[armas/brancas/dual_ichor.md\|Dual Ichor]] | Espadas Duplas | Mercado (blueprint) |
| [[armas/brancas/dual_kamas.md\|Dual Kamas]] | Espadas Duplas | Mercado (blueprint) |
| [[armas/brancas/dual_kamas_prime.md\|Dual Kamas Prime]] | Espadas Duplas | Relíquias (Prime) |
| [[armas/brancas/dual_skana.md\|Dual Skana]] | Espadas Duplas | Mercado (blueprint) |
| [[armas/brancas/dual_zoren.md\|Dual Zoren]] | Espadas Duplas | Mercado (blueprint) |
| [[armas/brancas/ether_daggers.md\|Ether Daggers]] | Adagas Duplas | Mercado (blueprint) |
| [[armas/brancas/ether_reaper.md\|Ether Reaper]] | Foice | Mercado (blueprint) |
| [[armas/brancas/ether_sword.md\|Ether Sword]] | Espada | Mercado (blueprint) |
| [[armas/brancas/fang.md\|Fang]] | Espadas Duplas | Mercado (blueprint) |
| [[armas/brancas/fang_prime.md\|Fang Prime]] | Espadas Duplas | Relíquias (Prime) |
| [[armas/brancas/fragor.md\|Fragor]] | Martelo | Mercado (blueprint) |
| [[armas/brancas/fragor_prime.md\|Fragor Prime]] | Martelo | Relíquias (Prime) |
| [[armas/brancas/furax.md\|Furax]] | Garras | Mercado (blueprint) |
| [[armas/brancas/furax_wraith.md\|Furax Wraith]] | Garras | Nightwave / Evento |
| [[armas/brancas/galatine.md\|Galatine]] | Espada Pesada | Mercado (blueprint) |
| [[armas/brancas/galatine_prime.md\|Galatine Prime]] | Espada Pesada | Relíquias (Prime) |
| [[armas/brancas/galvacord.md\|Galvacord]] | Chicote | Pesquisa de Clã (Grineer) |
| [[armas/brancas/glaive.md\|Glaive]] | Glaive | Mercado (blueprint) |
| [[armas/brancas/glaive_prime.md\|Glaive Prime]] | Glaive | Relíquias (Prime) |
| [[armas/brancas/gram.md\|Gram]] | Espada Pesada | Mercado (blueprint) |
| [[armas/brancas/gram_prime.md\|Gram Prime]] | Espada Pesada | Relíquias (Prime) |
| [[armas/brancas/guandao.md\|Guandao]] | Lança | Mercado (blueprint) |
| [[armas/brancas/guandao_prime.md\|Guandao Prime]] | Lança | Relíquias (Prime) |
| [[armas/brancas/halikar.md\|Halikar]] | Glaive | Mercado (blueprint) |
| [[armas/brancas/halikar_wraith.md\|Halikar Wraith]] | Glaive | Nightwave / Evento |
| [[armas/brancas/hate.md\|Hate]] | Foice | Drop (Stalker) |
| [[armas/brancas/heat_sword.md\|Heat Sword]] | Espada | Mercado (blueprint) |
| [[armas/brancas/hirudo.md\|Hirudo]] | Garras | Pesquisa de Clã (Grineer) |
| [[armas/brancas/innodem.md\|Innodem]] | Espada | Pesquisa de Clã (Entrati) |
| [[armas/brancas/jat_kittag.md\|Jat Kittag]] | Martelo | Mercado (blueprint) |
| [[armas/brancas/jat_kusar.md\|Jat Kusar]] | Cajado | Pesquisa de Clã (Corpus) |
| [[armas/brancas/jaw_sword.md\|Jaw Sword]] | Espada | Mercado (blueprint) |
| [[armas/brancas/karyst.md\|Karyst]] | Adaga | Mercado (blueprint) |
| [[armas/brancas/karyst_prime.md\|Karyst Prime]] | Adaga | Relíquias (Prime) |
| [[armas/brancas/kesheg.md\|Kesheg]] | Lança | Pesquisa de Clã (Grineer) |
| [[armas/brancas/kestrel.md\|Kestrel]] | Glaive | Mercado (blueprint) |
| [[armas/brancas/krohkur.md\|Krohkur]] | Espada | Mercado (blueprint) |
| [[armas/brancas/kronen.md\|Kronen]] | Tonfa | Pesquisa de Clã (Corpus) |
| [[armas/brancas/kronen_prime.md\|Kronen Prime]] | Tonfa | Relíquias (Prime) |
| [[armas/brancas/kuva_shildeg.md\|Kuva Shildeg]] | Martelo | Kuva Lich |
| [[armas/brancas/lacera.md\|Lacera]] | Lâmina e Chicote | Pesquisa de Clã (Corpus) |
| [[armas/brancas/lecta.md\|Lecta]] | Chicote | Mercado (blueprint) |
| [[armas/brancas/lesion.md\|Lesion]] | Lança | Pesquisa de Clã (Entrati) |
| [[armas/brancas/machete.md\|Machete]] | Facão | Mercado (blueprint) |
| [[armas/brancas/machete_wraith.md\|Machete Wraith]] | Facão | Nightwave / Evento |
| [[armas/brancas/magistar.md\|Magistar]] | Martelo | Pesquisa de Clã (Grineer) |
| [[armas/brancas/magistar_wraith.md\|Magistar Wraith]] | Martelo | Nightwave / Evento |
| [[armas/brancas/mios.md\|Mios]] | Lâmina e Chicote | Pesquisa de Clã (Entrati) |
| [[armas/brancas/mire.md\|Mire]] | Espada | Drop (Ambulas, Pluto) |
| [[armas/brancas/nami_duo.md\|Nami Duo]] | Espadas Duplas | Pesquisa de Clã (Corpus) |
| [[armas/brancas/nami_solo.md\|Nami Solo]] | Espada | Pesquisa de Clã (Corpus) |
| [[armas/brancas/nikana.md\|Nikana]] | Nikana | Mercado (blueprint) |
| [[armas/brancas/nikana_prime.md\|Nikana Prime]] | Nikana | Relíquias (Prime) |
| [[armas/brancas/ninkondi.md\|Ninkondi]] | Nunchaku | Pesquisa de Clã (Corpus) |
| [[armas/brancas/ninkondi_prime.md\|Ninkondi Prime]] | Nunchaku | Relíquias (Prime) |
| [[armas/brancas/ohma.md\|Ohma]] | Tonfa | Pesquisa de Clã (Corpus) |
| [[armas/brancas/okina.md\|Okina]] | Espadas Duplas | Pesquisa de Clã (Corpus) |
| [[armas/brancas/okina_prime.md\|Okina Prime]] | Espadas Duplas | Relíquias (Prime) |
| [[armas/brancas/orthos.md\|Orthos]] | Lança | Mercado (blueprint) |
| [[armas/brancas/orthos_prime.md\|Orthos Prime]] | Lança | Relíquias (Prime) |
| [[armas/brancas/orvius.md\|Orvius]] | Glaive | Quest (Chains of Harrow) |
| [[armas/brancas/pangolin_prime.md\|Pangolin Prime]] | Espada | Relíquias (Prime) |
| [[armas/brancas/pangolin_sword.md\|Pangolin Sword]] | Espada | Mercado (blueprint) |
| [[armas/brancas/paracesis.md\|Paracesis]] | Espada Pesada | Quest (The Sacrifice) |
| [[armas/brancas/pennant.md\|Pennant]] | Espada Pesada | Pesquisa de Clã (Entrati) |
| [[armas/brancas/plasma_sword.md\|Plasma Sword]] | Espada | Mercado (blueprint) |
| [[armas/brancas/praedos.md\|Praedos]] | Tonfa | Pesquisa de Clã (Entrati) |
| [[armas/brancas/prisma_dual_cleavers.md\|Prisma Dual Cleavers]] | Espadas Duplas | Baro Ki'Teer |
| [[armas/brancas/prisma_skana.md\|Prisma Skana]] | Espada | Baro Ki'Teer |
| [[armas/brancas/prova.md\|Prova]] | Lança | Pesquisa de Clã (Corpus) |
| [[armas/brancas/prova_vandal.md\|Prova Vandal]] | Lança | Nightwave / Evento |
| [[armas/brancas/pulmonars.md\|Pulmonars]] | Leques | Pesquisa de Clã (Entrati) |
| [[armas/brancas/rakta_dark_dagger.md\|Rakta Dark Dagger]] | Adaga | Sindicato (Red Veil) |
| [[armas/brancas/reaper_prime.md\|Reaper Prime]] | Foice | Relíquias (Prime) |
| [[armas/brancas/redeemer.md\|Redeemer]] | Espingarda Melee | Pesquisa de Clã (Tenno) |
| [[armas/brancas/redeemer_prime.md\|Redeemer Prime]] | Espingarda Melee | Relíquias (Prime) |
| [[armas/brancas/ripkas.md\|Ripkas]] | Garras | Pesquisa de Clã (Grineer) |
| [[armas/brancas/sarpa.md\|Sarpa]] | Espingarda Melee | Pesquisa de Clã (Tenno) |
| [[armas/brancas/scoliac.md\|Scoliac]] | Chicote | Pesquisa de Clã (Grineer) |
| [[armas/brancas/secura_lecta.md\|Secura Lecta]] | Chicote | Sindicato (Perrin Sequence) |
| [[armas/brancas/shaku.md\|Shaku]] | Cajado | Pesquisa de Clã (Corpus) |
| [[armas/brancas/sheev.md\|Sheev]] | Adaga | Pesquisa de Clã (Grineer) |
| [[armas/brancas/sigma_and_octantis.md\|Sigma e Octantis]] | Espada e Escudo | Evento (Aniversário DE) |
| [[armas/brancas/silva_and_aegis.md\|Silva e Aegis]] | Espada e Escudo | Mercado (blueprint) |
| [[armas/brancas/silva_and_aegis_prime.md\|Silva e Aegis Prime]] | Espada e Escudo | Relíquias (Prime) |
| [[armas/brancas/skana.md\|Skana]] | Espada | Starter / Mercado |
| [[armas/brancas/skana_prime.md\|Skana Prime]] | Espada | Relíquias (Prime) |
| [[armas/brancas/skiajati.md\|Skiajati]] | Nikana | Quest (The Sacrifice) |
| [[armas/brancas/stiletto_prime.md\|Stiletto Prime]] | Adaga | Relíquias (Prime) |
| [[armas/brancas/stropha.md\|Stropha]] | Espingarda Melee | Pesquisa de Clã (Tenno) |
| [[armas/brancas/sydon.md\|Sydon]] | Lança | Pesquisa de Clã (Grineer) |
| [[armas/brancas/tatsu.md\|Tatsu]] | Espada Pesada | Pesquisa de Clã (Entrati) |
| [[armas/brancas/tatsu_prime.md\|Tatsu Prime]] | Espada Pesada | Relíquias (Prime) |
| [[armas/brancas/tekko.md\|Tekko]] | Garras | Mercado (blueprint) |
| [[armas/brancas/tekko_prime.md\|Tekko Prime]] | Garras | Relíquias (Prime) |
| [[armas/brancas/telos_boltace.md\|Telos Boltace]] | Espadas Duplas | Sindicato (Arbiters of Hexis) |
| [[armas/brancas/tenet_exec.md\|Tenet Exec]] | Espada Pesada | Irmãs de Parvos |
| [[armas/brancas/tenet_grigori.md\|Tenet Grigori]] | Foice | Irmãs de Parvos |
| [[armas/brancas/tenet_livia.md\|Tenet Livia]] | Espadim | Irmãs de Parvos |
| [[armas/brancas/tipedo.md\|Tipedo]] | Lança | Mercado (blueprint) |
| [[armas/brancas/tipedo_prime.md\|Tipedo Prime]] | Lança | Relíquias (Prime) |
| [[armas/brancas/tonbo.md\|Tonbo]] | Lança | Pesquisa de Clã (Grineer) |
| [[armas/brancas/twin_basolk.md\|Twin Basolk]] | Adagas Duplas | Pesquisa de Clã (Grineer) |
| [[armas/brancas/vastilok.md\|Vastilok]] | Espingarda Melee | Pesquisa de Clã (Tenno) |
| [[armas/brancas/vaykor_sydon.md\|Vaykor Sydon]] | Lança | Sindicato (Steel Meridian) |
| [[armas/brancas/venka.md\|Venka]] | Garras | Pesquisa de Clã (Grineer) |
| [[armas/brancas/venka_prime.md\|Venka Prime]] | Garras | Relíquias (Prime) |
| [[armas/brancas/vitrica.md\|Vitrica]] | Espada Pesada | Pesquisa de Clã (Entrati) |
| [[armas/brancas/volnus.md\|Volnus]] | Martelo | Pesquisa de Clã (Corpus) |
| [[armas/brancas/volnus_prime.md\|Volnus Prime]] | Martelo | Relíquias (Prime) |
| [[armas/brancas/war.md\|War]] | Espada Pesada | Drop (Stalker) |
| [[armas/brancas/xoris.md\|Xoris]] | Glaive | Quest (The Deadlock Protocol) |


## 🔗 Relacionados — Warframe — Segunda Mente


| Índice | Relação |
|---|---|
| [[armas/_Armas _Indice.md\|Armas]] | Índice geral — todas as categorias de arma |
| [[mods/_Mods _Indice.md\|Mods]] | Stances são mods — encontrados no índice de mods |
| [[mods/armas/_Mods Armas _Indice.md\|Mods de Armas]] | Mods de melee (Blood Rush, Weeping Wounds etc.) |
| [[locais/_Locais _Indice.md\|Locais]] | Planetas onde inimigos dropam stances e brancas |

----------------------------------------

## Seção: armas\archwing — Warframe — Segunda Mente

### 📄 arquivo: _Armas _Archwing _Indice.md

# Armas Archwing — Índice

> [!quote]
> *"No vácuo do espaço, nenhuma arma convencional importa."*


## 📊 Visão Geral — Warframe — Segunda Mente


Armas Archwing são equipamentos exclusivos para combate espacial e atmosférico, equipados no exoesqueleto Archwing. Dividem-se em **Arch-Guns** (ranged) e **Arch-Melee** (corpo-a-corpo). Possuem pool de mods completamente separado das armas terrestres.

**Slot Arch-Gun:** Slot de arma principal do Archwing
**Slot Arch-Melee:** Slot melee exclusivo do Archwing
**Mods:** 8 slots exclusivos — mods de Arch-Gun ou Arch-Melee (não compartilhados com armas terrestres)


## Modos de Uso — Warframe — Segunda Mente


| Modo | Contexto | Como Acessar |
|---|---|---|
| **Espaço (Space)** | Missões Archwing no vácuo — planetas com anel orbital | Ativar Archwing automaticamente ao iniciar missão espacial |
| **Atmosfera** | Combate externo do Railjack em missões de alto nível | Sair pela escotilha traseira do Railjack durante missão |
| **Terrestre (Ground)** | Missões terrestres normais via item especial | Archgun Deployer ou Zenith Crown (ver seção abaixo) |


## Uso Terrestre de Arch-Guns — Warframe — Segunda Mente


Arch-Guns podem ser convocadas em missões terrestres com dois métodos:

| Método | Como Obter | Limitação |
|---|---|---|
| **Archgun Deployer** | Recompensa de bounty em Fortuna (Orb Vallis) | Cargas limitadas — recarrega com tempo real (fora de missão) |
| **Zenith Crown** | Oferta sazonal da Nightwave | Convocação ilimitada — exclusivo para Mausolon |

> [!important] Arch-Melee não é usável no solo
> **Arch-Melee** é exclusiva de combate espacial e atmosférico — não pode ser convocada em missões terrestres com nenhum método disponível.


## Pool de Mods Exclusivo — Warframe — Segunda Mente


Armas Archwing usam mods que **não se aplicam a armas terrestres** e vice-versa:

| Categoria | Exemplos de Mods Exclusivos |
|---|---|
| **Arch-Gun** | Dual Rounds, Automatic Trigger, Charged Bullets, Explosive Payload, Hollowed Bullets |
| **Arch-Melee** | Orokin Reach, Elec Drain, Whirlwind, Astral Slash |

**Fontes de mods Archwing:**
- Drops de inimigos em missões Archwing (Uranus, Lua, Railjack)
- Recompensas de rotação de missões Archwing
- Cephalon Suda / Steel Meridian (sindicatos)

> [!tip]
> O mod **Serration** do slot primário **não funciona** em Arch-Guns. Os equivalentes Archwing têm nomes e pools diferentes.


## Pesquisa de Clã para Archwing — Warframe — Segunda Mente


A maioria das Arch-Guns está bloqueada atrás de pesquisa de clã em laboratórios específicos:

| Facção | Laboratório | Armas Disponíveis |
|---|---|---|
| **Tenno** | Tenno Lab | Centaur, Veritux |
| **Grineer** | Grineer Lab | Corvas, Grattler, Kaszas, Onorix |
| **Corpus** | Corpus Lab | Cyngas, Dual Decurion, Fluctus, Knux, Phaedra, Velocitus |
| **Entrati** | Entrati Lab | Cortege, Larkspur, Mausolon, Morgha |


## Lista Completa (23) — Warframe — Segunda Mente


| Arma | Tipo | Uso Terrestre | Fonte |
|---|---|---|---|
| [[armas/archwing/centaur.md\|Centaur]] | Arch-Melee | Não | Pesquisa de Clã (Tenno) |
| [[armas/archwing/cortege.md\|Cortege]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Entrati) |
| [[armas/archwing/corvas.md\|Corvas]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Grineer) |
| [[armas/archwing/corvas_prime.md\|Corvas Prime]] | Arch-Gun | Sim (Deployer) | Relíquias (Prime) |
| [[armas/archwing/cyngas.md\|Cyngas]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Corpus) |
| [[armas/archwing/dual_decurion.md\|Dual Decurion]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Corpus) |
| [[armas/archwing/fluctus.md\|Fluctus]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Corpus) |
| [[armas/archwing/grattler.md\|Grattler]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Grineer) |
| [[armas/archwing/imperator.md\|Imperator]] | Arch-Gun | Sim (Deployer) | Mercado (blueprint) / Starter |
| [[armas/archwing/imperator_vandal.md\|Imperator Vandal]] | Arch-Gun | Sim (Deployer) | Drop (Archwing missions) / Baro Ki'Teer |
| [[armas/archwing/kaszas.md\|Kaszas]] | Arch-Melee | Não | Pesquisa de Clã (Grineer) |
| [[armas/archwing/knux.md\|Knux]] | Arch-Melee | Não | Pesquisa de Clã (Corpus) |
| [[armas/archwing/kuva_ayanga.md\|Kuva Ayanga]] | Arch-Gun | Sim (Deployer) | Kuva Lich |
| [[armas/archwing/kuva_grattler.md\|Kuva Grattler]] | Arch-Gun | Sim (Deployer) | Kuva Lich |
| [[armas/archwing/larkspur.md\|Larkspur]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Entrati) |
| [[armas/archwing/larkspur_prime.md\|Larkspur Prime]] | Arch-Gun | Sim (Deployer) | Relíquias (Prime) |
| [[armas/archwing/mausolon.md\|Mausolon]] | Arch-Gun | Sim (Deployer / Zenith Crown) | Pesquisa de Clã (Entrati) |
| [[armas/archwing/morgha.md\|Morgha]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Entrati) |
| [[armas/archwing/onorix.md\|Onorix]] | Arch-Melee | Não | Pesquisa de Clã (Grineer) |
| [[armas/archwing/phaedra.md\|Phaedra]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Corpus) |
| [[armas/archwing/prisma_veritux.md\|Prisma Veritux]] | Arch-Melee | Não | Baro Ki'Teer |
| [[armas/archwing/velocitus.md\|Velocitus]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Corpus) |
| [[armas/archwing/veritux.md\|Veritux]] | Arch-Melee | Não | Pesquisa de Clã (Tenno) |


## 🔗 Relacionados — Warframe — Segunda Mente


| Índice | Relação |
|---|---|
| [[armas/_Armas _Indice.md\|Armas]] | Índice geral — todas as categorias de arma |
| [[mods/_Mods _Indice.md\|Mods]] | Mods de Arch-Gun e Arch-Melee |
| [[locais/_Locais _Indice.md\|Locais]] | Planetas com missões Archwing (Uranus, Lua, Railjack) |
| [[warframes/_Warframes _Indice.md\|Warframes]] | Não confundir com Archwing (exoesqueleto) — são sistemas separados |

----------------------------------------

## Seção: companheiros — Warframe — Segunda Mente

### 📄 arquivo: _Companheiros _Indice.md

> [!quote]
> *"Um Tenno nunca luta verdadeiramente sozinho."*


## O que são Companheiros? — Warframe — Segunda Mente


Companheiros são criaturas e unidades que acompanham o Tenno em missões. Cada tipo tem comportamentos, habilidades e slots de mod distintos. Apenas um companheiro pode ser equipado por vez.

Todos os companheiros têm:
- **Slot de companheiro** independente do loadout de armas/warframe
- **Sistema de mods próprio** à Companion mods e mods de arma de companheiro
- **Afeto:** substituiu a morte permanente (antes da rework de 2023) à companheiros não morrem mais de forma permanente


## Tipos de Companheiro — Warframe — Segunda Mente


| Tipo           | Origem                               | Características                                                                          |
| -------------- | ------------------------------------ | ----------------------------------------------------------------------------------------- |
| **Sentinel**   | Mercado / Relí­quias                 | Robô flutuantes; não entram em combate direto; habilidades passivas e ativas via precepts |
| **Kubrow**     | Incubação de ovos (Plains / Mercado) | Caninos; comportamento agressivo ou utilitário conforme a raça                            |
| **Kavat**      | Incubação de DNA felino              | Felinos; buffs e utilidade; Smeeta à o mais usado em farm                                 |
| **MOA**        | Modular dê Fortuna (Solaris United)  | Robôs modulares; customizáveis com diferentes modelos e precepts                          |
| **Hound**      | Irmãs de Parvos                      | Robôs de combate; obtidos apás derrotar uma Irmã de Parvos                               |
| **Vulpaphyla** | Deimos (Entrati)                     | Raposas infestadas; ressuscitam automaticamente se morrerem                               |
| **Predasite**  | Deimos (Entrati)                     | Felinos infestados; habilidades de debuff e controle                                      |


## Mastery — Warframe — Segunda Mente


Companheiros contribuem com **Affinity de Mastery** ao atingir Rank 30:
- Sentinels, Kubrows, Kavats, MOAs, Hounds: **3.000 pontos** cada
- Versões Prime de Sentinels: **6.000 pontos** (contam separado da versão base)


## 📋 Lista Completa — Warframe — Segunda Mente


> [!info] Status
> `nao-obtido` · `incubado` · `maximizado` · `vendido`

### Sentinels (16)

| Companheiro | Status |
|---|---|
| [[companheiros/sentinel/carrier.md\|Carrier]] | nao-obtido |
| [[companheiros/sentinel/carrier_prime.md\|Carrier Prime]] | nao-obtido |
| [[companheiros/sentinel/dethcube.md\|Dethcube]] | nao-obtido |
| [[companheiros/sentinel/dethcube_prime.md\|Dethcube Prime]] | nao-obtido |
| [[companheiros/sentinel/diriga.md\|Diriga]] | nao-obtido |
| [[companheiros/sentinel/djinn.md\|Djinn]] | nao-obtido |
| [[companheiros/sentinel/helios.md\|Helios]] | nao-obtido |
| [[companheiros/sentinel/helios_prime.md\|Helios Prime]] | nao-obtido |
| [[companheiros/sentinel/nautilus.md\|Nautilus]] | nao-obtido |
| [[companheiros/sentinel/nautilus_prime.md\|Nautilus Prime]] | nao-obtido |
| [[companheiros/sentinel/oxylus.md\|Oxylus]] | nao-obtido |
| [[companheiros/sentinel/shade.md\|Shade]] | nao-obtido |
| [[companheiros/sentinel/shade_prime.md\|Shade Prime]] | nao-obtido |
| [[companheiros/sentinel/taxon.md\|Taxon]] | nao-obtido |
| [[companheiros/sentinel/wyrm.md\|Wyrm]] | nao-obtido |
| [[companheiros/sentinel/wyrm_prime.md\|Wyrm Prime]] | nao-obtido |


### Kubrows (6)

| Companheiro | Status |
|---|---|
| [[companheiros/kubrow/chesa.md\|Chesa Kubrow]] | nao-obtido |
| [[companheiros/kubrow/helminth_charger.md\|Helminth Charger]] | nao-obtido |
| [[companheiros/kubrow/huras.md\|Huras Kubrow]] | nao-obtido |
| [[companheiros/kubrow/raksa.md\|Raksa Kubrow]] | nao-obtido |
| [[companheiros/kubrow/sahasa.md\|Sahasa Kubrow]] | nao-obtido |
| [[companheiros/kubrow/sunika.md\|Sunika Kubrow]] | nao-obtido |


### Kavats, Vulpaphylas e Predasites (10)

| Companheiro | Status |
|---|---|
| [[companheiros/kavat/adarza.md\|Adarza Kavat]] | nao-obtido |
| [[companheiros/kavat/crescent_vulpaphyla.md\|Crescent Vulpaphyla]] | nao-obtido |
| [[companheiros/kavat/hyena_predasite.md\|Hyena Predasite]] | nao-obtido |
| [[companheiros/kavat/medjay_predasite.md\|Medjay Predasite]] | nao-obtido |
| [[companheiros/kavat/panzer_vulpaphyla.md\|Panzer Vulpaphyla]] | nao-obtido |
| [[companheiros/kavat/pharaoh_vulpaphyla.md\|Pharaoh Vulpaphyla]] | nao-obtido |
| [[companheiros/kavat/smeeta.md\|Smeeta Kavat]] | nao-obtido |
| [[companheiros/kavat/vasca.md\|Vasca Kavat]] | nao-obtido |
| [[companheiros/kavat/venari.md\|Venari]] | nao-obtido |
| [[companheiros/kavat/vizier_predasite.md\|Vizier Predasite]] | nao-obtido |


### MOAs — Modulares (6)

> MOAs são construídos em Fortuna com modelos intercambiáveis. Cada entrada representa um modelo base.

| Companheiro | Status |
|---|---|
| [[companheiros/moa/balla.md\|Balla MOA]] | nao-obtido |
| [[companheiros/moa/drex.md\|Drex MOA]] | nao-obtido |
| [[companheiros/moa/lambeo.md\|Lambeo MOA]] | nao-obtido |
| [[companheiros/moa/oloro.md\|Oloro MOA]] | nao-obtido |
| [[companheiros/moa/para.md\|Para MOA]] | nao-obtido |
| [[companheiros/moa/stratus.md\|Stratus MOA]] | nao-obtido |


### Hounds — Irmãs de Parvos (7)

> Hounds são obtidos ao derrotar Irmãs de Parvos. Cada entrada representa um tipo de Hound.

| Companheiro | Status |
|---|---|
| [[companheiros/hound/bhaira.md\|Bhaira Hound]] | nao-obtido |
| [[companheiros/hound/dorma.md\|Dorma Hound]] | nao-obtido |
| [[companheiros/hound/hec.md\|Hec Hound]] | nao-obtido |
| [[companheiros/hound/lega.md\|Lega Hound]] | nao-obtido |
| [[companheiros/hound/orm.md\|Orm Hound]] | nao-obtido |
| [[companheiros/hound/tauga.md\|Tauga Hound]] | nao-obtido |
| [[companheiros/hound/voca.md\|Voca Hound]] | nao-obtido |


## Por Função — Warframe — Segunda Mente


### Utilidade e Farm
[[companheiros/kavat/smeeta.md|Smeeta Kavat]] · [[companheiros/sentinel/carrier.md|Carrier]] · [[companheiros/sentinel/carrier_prime.md|Carrier Prime]] · [[companheiros/kubrow/sahasa.md|Sahasa Kubrow]] · [[companheiros/kubrow/chesa.md|Chesa Kubrow]] · [[companheiros/sentinel/oxylus.md|Oxylus]] · [[companheiros/sentinel/taxon.md|Taxon]]

### Buffs e Dano
[[companheiros/kavat/adarza.md|Adarza Kavat]] · [[companheiros/kavat/panzer_vulpaphyla.md|Panzer Vulpaphyla]] · [[companheiros/sentinel/helios.md|Helios]] · [[companheiros/sentinel/helios_prime.md|Helios Prime]] · [[companheiros/sentinel/dethcube.md|Dethcube]] · [[companheiros/sentinel/dethcube_prime.md|Dethcube Prime]]

### Defesa e Sobrevivência
[[companheiros/kubrow/raksa.md|Raksa Kubrow]] · [[companheiros/kubrow/huras.md|Huras Kubrow]] · [[companheiros/sentinel/djinn.md|Djinn]] · [[companheiros/sentinel/nautilus.md|Nautilus]] · [[companheiros/sentinel/nautilus_prime.md|Nautilus Prime]] · [[companheiros/kavat/vasca.md|Vasca Kavat]]

### Furtividade
[[companheiros/kubrow/huras.md|Huras Kubrow]] · [[companheiros/sentinel/shade.md|Shade]] · [[companheiros/sentinel/shade_prime.md|Shade Prime]]

### Combate Agressivo
[[companheiros/kubrow/sunika.md|Sunika Kubrow]] · [[companheiros/kavat/venari.md|Venari]] · [[companheiros/sentinel/wyrm.md|Wyrm]] · [[companheiros/sentinel/wyrm_prime.md|Wyrm Prime]]

### Modulares (Fortuna / Parvos)
[[companheiros/moa/lambeo.md|Lambeo MOA]] · [[companheiros/moa/oloro.md|Oloro MOA]] · [[companheiros/moa/para.md|Para MOA]] · [[companheiros/moa/stratus.md|Stratus MOA]] · [[companheiros/moa/balla.md|Balla MOA]] · [[companheiros/moa/drex.md|Drex MOA]] · [[companheiros/hound/bhaira.md|Bhaira Hound]] · [[companheiros/hound/lega.md|Lega Hound]] · [[companheiros/hound/orm.md|Orm Hound]]

### Deimos (Infestados)
[[companheiros/kavat/panzer_vulpaphyla.md|Panzer Vulpaphyla]] · [[companheiros/kavat/crescent_vulpaphyla.md|Crescent Vulpaphyla]] · [[companheiros/kavat/pharaoh_vulpaphyla.md|Pharaoh Vulpaphyla]] · [[companheiros/kavat/medjay_predasite.md|Medjay Predasite]] · [[companheiros/kavat/vizier_predasite.md|Vizier Predasite]] · [[companheiros/kavat/hyena_predasite.md|Hyena Predasite]]


## 💡 Curiosidades — Warframe — Segunda Mente


- Carrier Prime foi por anos o sentinel padrão do end-game por carregar munição automaticamente — só perdeu relevância com o sistema de Infinite Ammo de alguns frames.
- Smeeta Kavat tem uma habilidade chamada Charm que pode dobrar drops, créditos e affinity — central em qualquer sessão de farm intenso.
- Venari é exclusiva de Khora e não pode ser equip ada por outros frames — funciona como uma habilidade disfarçada de companheiro.
- Huras Kubrow era o único companheiro capaz de deixar o operador invisível antes das reworks de furtividade.
- Panzer Vulpaphyla aplica Viral automaticamente em inimigos via espinhos — compatível com builds de Condition Overload sem esforço do jogador.
- MOAs podem ser configurados com diferentes combinações de modelo, arma e suporte — o Oloro MOA com precept de escudo é popular em missões de alto nível.
- Djinn tem a habilidade Reawaken que o ressuscita automaticamente a cada 90 segundos após a morte — único sentinel com autorreavivamento antes da rework geral.
- Nautilus foi introduzido com Railjack e pode implantar âncoras de void que restringem inimigos — útil em missões de defesa.
- Vasca Kavat tem habilidades relacionadas a vampirismo e pode transferir parte da vida dela para o Tenno quando a saúde está crítica.
- Predasites e Vulpaphylas de Deimos precisam de tags de conservação do bioma para serem obtidos — único método de aquisição por caça no open world.

----------------------------------------

## Seção: cosmeticos — Warframe — Segunda Mente

### 📄 arquivo: _Cosmeticos _Indice.md

> [!quote]
> *"A aparência do Tenno é sua assinatura no Sistema Solar."*


## O Sistema de Estilização — Warframe — Segunda Mente


Warframe tem um dos sistemas de customização visual mais abrangentes entre jogos live-service. Cada Warframe, arma e companheiro tem múltiplas camadas de personalização independentes — todas 100% estéticas, sem impacto em gameplay.

O jogo divide os cosméticos em **camadas de customização**:

| Camada | O que cobre |
|---|---|
| **Forma base** | Skin do Warframe / Capacete alternativo |
| **Dorso** | Syandana (capa/ornamento) |
| **Armadura** | Anexos nos slots de ombro, peito, braço e perna |
| **Efeito passivo** | Efemera (aura / trilha visual) |
| **Cor** | Paleta de cores em todos os canais |
| **Identidade** | Sigil (peito/costas) e Emblema (ombro) |
| **Gesto** | Animações idle e emotes |
| **Arma melee** | Sugatra (ornamento do punho) |
| **Ambiente** | Decorações do Orbiter e Dojo |


## Fontes de Cosméticos — Warframe — Segunda Mente


| Fonte | Tipo de Item |
|---|---|
| **Platinum (Mercado)** | Skins, syandanas, anexos, capacetes, animações |
| **Steam (Tennogen)** | Skins, capacetes, syandanas, animações criadas pela comunidade |
| **Prime Access / Prime Vault** | Pacotes com skin Prime, syandana, acessórios e estátua |
| **Nightwave** | Paletas, emotes, sigils, skins ocasionais |
| **Eventos sazonais** | Paletas, sigils, decorações, emotes exclusivos |
| **Kuva Liches** | Efemeras Vengeful (drop direto do Lich) |
| **Sisters of Parvos** | Tenet Efemera (drop direto da Irmã) |
| **Eidolons / Orb Bosses** | Efemeras de boss (Blazing Step, Eidolon etc.) |
| **Steel Path** | Galvanized Efemera |
| **Sindicatos** | Sigils de afiliação, algumas paletas |
| **Conservação (Open Worlds)** | Troféus de bestas para o Orbiter |


## Arquivos de Referência — Warframe — Segunda Mente


| Cosmético | Arquivo | Descrição |
|---|---|---|
| [[cosmeticos/skins.md\|Skins]] | skins.md | Warframe skins, weapon skins — Tennogen, Deluxe, Prime |
| [[cosmeticos/capacetes.md\|Capacetes]] | capacetes.md | Helmets alternativos por frame |
| [[cosmeticos/syandanas.md\|Syandanas]] | syandanas.md | Capas e ornamentos dorsais |
| [[cosmeticos/anexos.md\|Anexos]] | nexos.md | Armor pieces — ombro, peito, braço, perna |
| [[cosmeticos/efemeras.md\|Efemeras]] | efemeras.md | Efeitos visuais passivos no frame |
| [[cosmeticos/paletas.md\|Paletas de Cores]] | paletas.md | Conjuntos de cores para customização |
| [[cosmeticos/animacoes.md\|Animações e Emotes]] | nimacoes.md | Idle animations e gestos sociais |
| [[cosmeticos/brasoes_emblemas.md\|Brasões e Emblemas]] | rasoes_emblemas.md | Sigils e badges de identidade |
| [[cosmeticos/sugatras.md\|Sugatras]] | sugatras.md | Ornamentos pendurados em armas brancas |
| [[cosmeticos/decoracoes.md\|Decorações do Orbiter]] | decoracoes.md | Itens para o Orbiter e Dojo |


## Tennogen — Warframe — Segunda Mente


Tennogen é o programa de criação comunitária da Digital Extremes. Jogadores enviam designs via Steam Workshop — os aprovados são vendidos na Steam com divisão de royalties entre o criador e a DE.

**Regras do Tennogen:**
- Disponível principalmente no **PC via Steam** — consoles têm acesso limitado e via Platinum
- Não pode ser comprado com Platinum no PC — exige compra separada em dinheiro real
- Qualidade altamente variável — os mais populares têm votação massiva da comunidade


## Prime Access e Prime Vault — Warframe — Segunda Mente


Cada Prime Access inclui um pacote cosmético completo:
- Skin/visual Prime do frame (via acesso antecipado)
- Syandana Prime exclusiva
- Armor set Prime
- Estátua para o Orbiter
- Efemera (em alguns pacotes recentes)

Prime Vault retorna frames Prime antigos com seus pacotes cosméticos originais.


## 💡 Curiosidades — Warframe — Segunda Mente


- Warframe foi pioneiro em Tennogen — um dos primeiros jogos a formalizar royalties para criadores de conteúdo cosmético.
- O sistema de cores tem mais de 30 paletas disponíveis — incluindo tons que não existem na paleta padrão.
- Efemeras de Lich são farmadas intencionalmente pela comunidade — alguns elementos como Toxin Vengeful são raros e valiosos no trading.
- O modo Captura (Fashion Frame) tem comunidade própria dentro do jogo — jogadores criam poses e tiram screenshots com iluminação customizada.
- A Digital Extremes lançou skins colaborativas com franquias externas (Neon Genesis Evangelion, entre outras) — mostrando o alcance do sistema.
- Alguns jogadores chamam o sistema de customização de ''Fashion Frame'' — considerado por parte da comunidade o verdadeiro end-game do jogo.
- Sigils de sindicato contribuem passivamente com standing apenas ao serem usados em missões — mechânica pouco conhecida por iniciantes.

----------------------------------------

## Seção: cosmeticos — Warframe — Segunda Mente

### 📄 arquivo: efemeras.md

﻿---
title: Efemeras
tipo: cosmetico
tags:
  - cosmetico
  - efemera
atualizado: 2026-04-19

## O que são Efemeras? — Warframe — Segunda Mente


Efemeras são efeitos visuais passivos aplicados ao Warframe — trilhas de luz, auras elementais, partículas e distorções que seguem o frame durante o movimento.


## Exemplos de Tipos — Warframe — Segunda Mente


| Efemera | Efeito Visual |
|---|---|
| **Smoking Body** | Fumaça escura saindo do frame |
| **Eidolon Efemera** | Efeito azul de void — drop de Teralyst |
| **Kuva Efemera** | Aura de Kuva vermelho — drop de Kuva Lich |
| **Vengeful** series | Efemeras elementais — drops de Kuva Liches específicos |
| **Tenet Efemera** | Aura de Corpus — drop de Sisters of Parvos |
| **Galvanized Efemera** | Drop de Steel Path |
| **Umbra Efemera** | Efeito de Void ligado ao Umbra |
| **Blazing Step** | Fogo nas passadas — drop de Profit-Taker |
| **Shocking Step** | Eletricidade nas passadas — drop de Exploiter Orb |


## 🌍 Onde Conseguir — Warframe — Segunda Mente


| Fonte | Exemplos |
|---|---|
| **Kuva Liches** | Efemeras Vengeful (7 variantes elementais) |
| **Sisters of Parvos** | Tenet Efemera |
| **Eidolons** | Efemera de Teralyst, Hydrolyst, Gantulyst |
| **Orb Vallis Bosses** | Blazing Step, Shocking Step, Freezing Step |
| **Steel Path** | Galvanized Efemera |
| **Eventos / Login** | Exclusivas por tempo limitado |
| **Prime Access** | Algumas Prime Access incluem efemeras |


## 📝 Observações — Warframe — Segunda Mente


- Efemeras de Lich/Sister são as mais farmadas — exigem criar e derrotar liches com o elemento correto
- Algumas efemeras são extremamente raras e valiosas no trading
- Apenas uma efemera pode ser equipada por vez
- Efeitos são visíveis por todos os jogadores na missão

----------------------------------------

## Seção: cosmeticos — Warframe — Segunda Mente

### 📄 arquivo: skins.md

﻿---
title: Skins
tipo: cosmetico
tags:
  - cosmetico
  - skin
atualizado: 2026-04-19

## O que são Skins? — Warframe — Segunda Mente


Skins substituem completamente a aparência visual de um Warframe ou arma, mantendo os stats e habilidades intactos. São puramente estéticos.


## Tipos de Skin — Warframe — Segunda Mente


| Tipo | Descrição |
|---|---|
| **Tennogen** | Criadas pela comunidade via Steam Workshop; compradas com dinheiro real via Steam |
| **Prime Accessories** | Skin + Syandana incluídos em pacotes de Prime Access |
| **Deluxe Bundles** | Skins oficiais de alta qualidade vendidas por Platinum |
| **Graxx / Feyarch** | Skins temáticas de sindicatos ou eventos |
| **Umbra Tennogen** | Skins compatíveis com Excalibur Umbra (limitadas) |
| **Weapon Skins** | Substituem o visual de armas específicas ou categorias inteiras |


## 🌍 Onde Conseguir — Warframe — Segunda Mente


- **Mercado** (Platinum) — Deluxe Bundles, weapon skins oficiais
- **Steam** (dinheiro real) — Tennogen exclusivo de PC
- **Prime Access / Prime Vault** — incluídos em pacotes premium
- **Nightwave** — ocasionalmente oferecidas como recompensas de rank
- **Eventos** — skins exclusivas por tempo limitado


## 📝 Observações — Warframe — Segunda Mente


- Tennogen **não está disponível** em consoles via Steam — consoles têm seleção reduzida via Platinum
- Skins de Warframe não substituem o capacete — precisam do capacete default ou de um capacete compatível
- Algumas skins de arma cobrem categorias inteiras (ex: skin para todas as espadas simples)

----------------------------------------

## Seção: cosmeticos — Warframe — Segunda Mente

### 📄 arquivo: paletas.md

﻿---
title: Paletas de Cores
tipo: cosmetico
tags:
  - cosmetico
  - paleta
  - cor
atualizado: 2026-04-19

## O que são Paletas? — Warframe — Segunda Mente


Paletas são conjuntos de cores usados para customizar Warframes, armas, companheiros, veículos e decorações do Orbiter. Cada paleta adiciona um conjunto de tons ao editor de cores.


## Paletas Notáveis — Warframe — Segunda Mente


| Paleta | Como Obter |
|---|---|
| **Classic Saturated** | 75.000 Créditos — paleta base acessível |
| **Tenno** | Platinum — tons variados |
| **Dojo / Syndicate** | Algumas paletas exclusivas de pesquisa de clã |
| **Event Palettes** | Drops de eventos sazonais (Frostfall, Plague Star etc.) |
| **Nightwave** | Periodicamente como recompensa de rank |
| **Twitch Drops** | Paletas distribuídas via drops de streams oficiais |
| **Paleta Prime** | Incluída em alguns Prime Access |


## Canais de Cor — Warframe — Segunda Mente


Cada item tem múltiplos canais de cor independentes:

| Canal | Área Colorida |
|---|---|
| **Primário** | Cor dominante do item |
| **Secundário** | Cor de contraste |
| **Terciário** | Detalhes menores |
| **Quaternário** | Acentos e brilhos |
| **Energia** | Cor dos efeitos de habilidade e energia |


## 📝 Observações — Warframe — Segunda Mente


- A paleta **Classic Saturated** é considerada essencial — cobre a maioria dos tons básicos com intensidade
- Cor de Energia afeta partículas de habilidade, olhos do frame e alguns efeitos visuais
- Paletas de evento são as mais difíceis de reobter — muitas nunca voltam
- A **Iguais** (Equals) paleta é uma das mais populares por incluir tons neutros e pretos reais

----------------------------------------

## Seção: cosmeticos — Warframe — Segunda Mente

### 📄 arquivo: syandanas.md

﻿---
title: Syandanas
tipo: cosmetico
tags:
  - cosmetico
  - syandana
atualizado: 2026-04-19

## O que são Syandanas? — Warframe — Segunda Mente


Syandanas são capas, véus e ornamentos dorsais equipados no Warframe. Vão desde capas simples até estruturas elaboradas com físicas e efeitos de partícula.


## Categorias Visuais — Warframe — Segunda Mente


| Estilo | Exemplos |
|---|---|
| **Capas longas** | Asa de anjo, tecidos fluídos |
| **Estruturais** | Asas mecânicas, estruturas rígidas |
| **Com efeitos** | Syandanas com partículas, luz, fogo, void |
| **Prime** | Incluídas em Prime Access — geralmente douradas com design elaborado |
| **Tennogen** | Criadas pela comunidade |
| **Sindicato** | Algumas syandanas são recompensas de standing de sindicatos |


## 🌍 Onde Conseguir — Warframe — Segunda Mente


- **Mercado** (Platinum) — maioria das syandanas
- **Prime Access / Prime Vault** — sempre incluem uma syandana Prime exclusiva
- **Tennogen** (Steam) — syandanas criadas por jogadores
- **Nightwave** — rotação periódica como recompensa
- **Eventos e Login Rewards** — ocasionalmente


## 📝 Observações — Warframe — Segunda Mente


- Syandanas têm física simulada — reagem ao movimento e parkour do frame
- Algumas são exclusivas de pacotes e nunca voltam ao mercado individualmente
- A syandana é o cosmético mais visível durante gameplay — grande peso na identidade visual do personagem

----------------------------------------

## Seção: cosmeticos — Warframe — Segunda Mente

### 📄 arquivo: animacoes.md

## O que são Animações e Emotes? — Warframe — Segunda Mente


Animações customizam a postura idle do Warframe (como ele fica parado) e emotes são gestos executados manualmente para interação social ou expressão.


## Tipos — Warframe — Segunda Mente


| Tipo | Descrição |
|---|---|
| **Idle Animation** | Substitui a animação de espera padrão do frame |
| **Emote** | Gesto ativado manualmente (dança, saudação, etc.) |
| **Stance Emotes** | Posturas alternativas que o frame assume |
| **Captura Animations** | Usadas em modo Captura para poses fotográficas |


## Exemplos — Warframe — Segunda Mente


| Animação / Emote | Origem |
|---|---|
| **Limbo Agony** | Icônica dança de Limbo — muito popular |
| **Tennogen Idles** | Packs de animação criados pela comunidade |
| **Harka Stance** | Postura guerreira — Nightwave |
| **Emotes de Saudação** | Pack inicial ou Mercado |
| **Dança do Cetus** | Evento / Nightwave |


## 🌍 Onde Conseguir — Warframe — Segunda Mente


- **Mercado** (Platinum) — packs de emotes e idles individuais
- **Tennogen** (Steam) — animation packs criados pela comunidade
- **Nightwave** — emotes como recompensas de rank
- **Eventos** — emotes exclusivos de eventos sazonais
- **Login Rewards** — ocasionalmente


## 📝 Observações — Warframe — Segunda Mente


- Idle animations são visíveis apenas quando o frame está parado — grande impacto em Captura (modo fotográfico)
- Emotes são acessados via roda de comandos rápidos
- Alguns emotes sincronizam com outros jogadores próximos

----------------------------------------

## Seção: cosmeticos — Warframe — Segunda Mente

### 📄 arquivo: capacetes.md

﻿---
title: Capacetes
tipo: cosmetico
tags:
  - cosmetico
  - capacete
atualizado: 2026-04-19

## O que são Capacetes? — Warframe — Segunda Mente


Capacetes são variantes visuais do elmo de cada Warframe. Cada frame tem ao menos um capacete alternativo além do padrão. São 100% estéticos — nenhum capacete altera stats desde a rework de 2013.


## 🌍 Onde Conseguir — Warframe — Segunda Mente


| Fonte | Método |
|---|---|
| **Mercado** | Compra direta por Platinum |
| **Alerts / Invasions** (antigo) | Eram drops de alertas antes do Nightwave substituir o sistema |
| **Tennogen** | Alguns capacetes alternativos via Steam Workshop |
| **Prime Accessories** | Capacetes Prime incluídos em pacotes de Prime Access |
| **Crafting** | Blueprints de capacetes podiam ser adquiridos e construídos na Fundição (sistema descontinuado) |


## 📝 Observações — Warframe — Segunda Mente


- Capacetes **Prime** têm design mais elaborado e são obtidos via Prime Accessories, não via Relíquias
- Capacetes Tennogen têm qualidade variável — alguns são altamente votados pela comunidade
- A escolha do capacete não afeta gameplay — apenas aparência e preferência visual

----------------------------------------

## Seção: cosmeticos — Warframe — Segunda Mente

### 📄 arquivo: anexos.md

## O que são Anexos? — Warframe — Segunda Mente


Anexos são peças de armadura decorativas fixadas em partes específicas do Warframe. Não alteram stats — apenas aparência.


## Slots de Anexo — Warframe — Segunda Mente


| Slot | Localização |
|---|---|
| **Ombro esquerdo** | Pauldron esquerdo |
| **Ombro direito** | Pauldron direito |
| **Peito** | Placa peitoral |
| **Perna esquerda** | Greave esquerda |
| **Perna direita** | Greave direita |
| **Braço** | Gauntlet (punho/antebraço) |


## Tipos de Anexo — Warframe — Segunda Mente


| Tipo | Característica |
|---|---|
| **Armor Sets** | Conjuntos temáticos que cobrem todos os slots com design unificado |
| **Prime Accessories** | Geralmente incluem arm/chest/leg armor junto com syandana |
| **Tennogen** | Peças individuais criadas pela comunidade |
| **Sindicato** | Itens de standing de alguns sindicatos |


## 🌍 Onde Conseguir — Warframe — Segunda Mente


- **Mercado** (Platinum) — armor sets e peças individuais
- **Prime Access / Prime Vault** — Prime Accessories sempre incluem peças de armadura
- **Tennogen** (Steam) — peças individuais votadas pela comunidade
- **Nightwave** — periodicamente como recompensa de rank


## 📝 Observações — Warframe — Segunda Mente


- Cada slot aceita apenas uma peça por vez
- É possível misturar peças de sets diferentes para criar looks únicos
- Algumas peças têm física simulada ou efeitos de partícula

----------------------------------------

## Seção: cosmeticos — Warframe — Segunda Mente

### 📄 arquivo: brasoes_emblemas.md

﻿---
title: Brasões e Emblemas
tipo: cosmetico
tags:
  - cosmetico
  - brasao
  - emblema
  - sigil
atualizado: 2026-04-19

## O que são Brasões e Emblemas? — Warframe — Segunda Mente


**Sigils (Brasões)** são marcas decorativas aplicadas no peito ou nas costas do Warframe. **Emblemas** são pequenos badges menores aplicados no ombro.


## Tipos — Warframe — Segunda Mente


| Tipo | Localização | Descrição |
|---|---|---|
| **Sigil** | Peito / Costas | Marca grande, personalizável em posição e tamanho |
| **Emblema** | Ombro esquerdo / direito | Badge menor, geralmente de clã ou evento |


## Sigils de Sindicato — Warframe — Segunda Mente


Cada sindicato tem um sigil próprio que demonstra afiliação:

| Sindicato | Sigil |
|---|---|
| Steel Meridian | Caveira com espinhos vermelhos |
| Arbiters of Hexis | Escala dourada |
| Cephalon Suda | Forma abstrata cian |
| Red Veil | Máscara sangrenta |
| New Loka | Flor branca |
| Perrin Sequence | Símbolo de crédito dourado |

> Sigils de sindicato ganham XP ao serem usados em missões — não é obrigatório mas acelera o standing visual.


## 🌍 Onde Conseguir — Warframe — Segunda Mente


| Fonte | Tipo |
|---|---|
| **Sindicatos** | Sigils de afiliação (gratuitos com rank) |
| **Eventos** | Sigils exclusivos por participação |
| **Mercado** (Platinum) | Sigils decorativos sem vínculo de sindicato |
| **Clãs** | Emblemas personalizados com o logo do clã |
| **Nightwave** | Sigils como recompensas de rank |
| **Conquistas** | Alguns sigils desbloqueiam por milestones (MR máximo, etc.) |


## 📝 Observações — Warframe — Segunda Mente


- Emblemas de clã são criados pelo Warlord ou líderes e aplicados a todos os membros
- Sigils podem ser redimensionados e reposicionados livremente na tela de customização
- Usar sigil de sindicato durante missões contribui passivamente para o standing daquele sindicato

----------------------------------------

## Seção: cosmeticos — Warframe — Segunda Mente

### 📄 arquivo: decoracoes.md

﻿---
title: Decorações do Orbiter
tipo: cosmetico
tags:
  - cosmetico
  - decoracao
  - orbiter
  - dojo
atualizado: 2026-04-19

## O que são Decorações? — Warframe — Segunda Mente


Decorações são itens colocados no interior do Orbiter (nave base do Tenno) e no Dojo (sede do clã). Permitem personalizar os ambientes de forma livre.


## Tipos de Decoração — Warframe — Segunda Mente


| Tipo | Local | Exemplos |
|---|---|---|
| **Estátuas de Frame** | Orbiter | Estátuas Prime obtidas em Prime Access |
| **Troféus / Plaques** | Orbiter | Registram conquistas (MR, Eidolons etc.) |
| **Objetos temáticos** | Orbiter / Dojo | Plantas, móveis, artefatos Orokin |
| **Captura de Bestas** | Orbiter | Troféus de conservação (Plains, Vallis, Deimos) |
| **Decorações Sazonais** | Orbiter | Eventos como Frostfall e Naberus |
| **Dojo Rooms** | Dojo | Salas inteiras decoráveis: arenas, jardins, galerias |


## 🌍 Onde Conseguir — Warframe — Segunda Mente


| Fonte | Itens |
|---|---|
| **Mercado** (Platinum) | Packs de decoração, estátuas |
| **Prime Access** | Estátua Prime exclusiva do pacote |
| **Conservação** | Troféus de criaturas capturadas vivas |
| **Eventos** | Decorações sazonais por participação |
| **Nightwave** | Decorações como recompensa de rank |
| **Pesquisa de Clã** | Decorações específicas do Dojo |


## Sistema de Decoração do Orbiter — Warframe — Segunda Mente


- Decorações são posicionadas livremente em modo de edição
- Itens têm limites de capacidade (decoration cap) no Orbiter
- O Dojo tem sistema próprio com capacidade muito maior e ferramentas avançadas de construção


## 📝 Observações — Warframe — Segunda Mente


- Estátuas Prime são consideradas itens de prestígio — indicam participação em Prime Access no lançamento
- O sistema de Dojo permite construções elaboradas — alguns clãs criam réplicas de cenários e obras de arte
- Troféus de conservação encorajam o modo de jogo de caça passiva nos open worlds

----------------------------------------

## Seção: cosmeticos — Warframe — Segunda Mente

### 📄 arquivo: sugatras.md

﻿---
title: Sugatras
tipo: cosmetico
tags:
  - cosmetico
  - sugatra
atualizado: 2026-04-19

## O que são Sugatras? — Warframe — Segunda Mente


Sugatras são ornamentos decorativos pendurados no punho ou pommel de armas brancas (melee). São análogos aos amuletos de espada em culturas orientais — puramente estéticos.


## Características — Warframe — Segunda Mente


- Equipadas no slot de **Sugatra** de qualquer arma branca
- Ficam penduradas no punho/cabo da arma durante gameplay e animações
- Têm física simulada — balançam durante o movimento
- Uma por arma, no slot dedicado


## 🌍 Onde Conseguir — Warframe — Segunda Mente


| Fonte | Observação |
|---|---|
| **Mercado** (Platinum) | Maioria das sugatras disponíveis |
| **Prime Access** | Algumas inclusas em pacotes Prime |
| **Nightwave** | Periodicamente como recompensa |
| **Eventos** | Sugatras exclusivas por participação |
| **Sindicatos** | Algumas disponíveis via standing |
| **Missões especiais** | Raras — drops ou recompensas de quest |


## 📝 Observações — Warframe — Segunda Mente


- São o cosmético de menor impacto visual geral — visíveis apenas em animações de melee e câmeras próximas
- Populares entre jogadores que investem em builds de melee puro
- Algumas sugatras Prime têm efeitos de partícula sutis

----------------------------------------

## Seção: locais — Warframe — Segunda Mente

### 📄 arquivo: _Locais _Indice.md

> [!quote]
> *"O Sistema Origem é vasto. E cada canto dele ainda sangra."*


## O Sistema Origem — Warframe — Segunda Mente


O Sistema Origem é o nome dado ao Sistema Solar no universo de Warframe — o palco de todas as guerras, descobertas e tragédias que compõem a narrativa do jogo. Cada planeta e região tem história própria: cicatrizes do Império Orokin, territórios disputados por Grineer e Corpus, anomalias do Void e ruínas que guardam segredos de civilizações extintas. Navegar o mapa estelar é tanto progressão mecânica quanto exploração de um universo com milhares de anos de história acumulada.

A estrutura do mapa estelar é linear na progressão inicial — planetas são desbloqueados sequencialmente via Junctions — mas se abre completamente ao longo do jogo. Cada planeta tem facção dominante, boss exclusivo, conjunto de recursos nativos e tipos de missão disponíveis. A dificuldade escala com a posição no mapa: Mercúrio começa com inimigos de nível 1–10, enquanto Sedna e Eris chegam a 40–60 no modo normal e centenas no Steel Path.

Os Open Worlds são regiões especiais que expandem um planeta com um mapa aberto e persistente — distinto do tile set procedural das missões normais. Cada Open World tem seu próprio ecossistema, sindicato, mecânicas exclusivas e narrativa interna. São o conteúdo mais rico em termos de profundidade de sistema dentro de um único local.


## Mapa Estelar — Warframe — Segunda Mente


### Planetas Principais

| Planeta | Facção | Boss | Nível (Normal) | Recursos Nativos |
|---|---|---|---|---|
| [[locais/planetas/mercurio.md\|Mercúrio]] | Grineer | Captain Vor | 1–15 | Ferrite, Polymer Bundle |
| [[locais/planetas/venus.md\|Vênus]] | Corpus | Jackal | 3–15 | Alloy Plate, Circuits, Polymer Bundle |
| [[locais/planetas/terra.md\|Terra]] | Grineer | Vay Hek | 8–22 | Ferrite, Rubedo, Neurodes |
| [[locais/planetas/marte.md\|Marte]] | Grineer / Corpus | Lech Kril | 10–25 | Salvage, Gallium, Morphics |
| [[locais/planetas/phobos.md\|Phobos]] | Corpus | Lech Kril + Vor | 15–25 | Alloy Plate, Rubedo, Morphics |
| [[locais/planetas/ceres.md\|Ceres]] | Grineer | Sargas Ruk | 18–28 | Alloy Plate, Circuits, Orokin Cell |
| [[locais/planetas/jupiter.md\|Júpiter]] | Corpus | Alad V | 20–30 | Alloy Plate, Salvage, Hexenon |
| [[locais/planetas/europa.md\|Europa]] | Corpus | Raptors | 25–35 | Rubedo, Control Module, Morphics |
| [[locais/planetas/saturno.md\|Saturno]] | Grineer | General Sargas Ruk | 28–38 | Alloy Plate, Plastids, Orokin Cell |
| [[locais/planetas/urano.md\|Urano]] | Grineer | Tyl Regor | 30–40 | Polymer Bundle, Plastids, Tellurium |
| [[locais/planetas/neptuno.md\|Netuno]] | Corpus | Hyena Pack | 33–43 | Ferrite, Nano Spores, Neural Sensors |
| [[locais/planetas/plutao.md\|Plutão]] | Corpus | Ambulas | 35–45 | Alloy Plate, Nano Spores, Argon Crystal |
| [[locais/planetas/sedna.md\|Sedna]] | Grineer | Kela de Thaym | 37–47 | Alloy Plate, Nano Spores, Orokin Cell |
| [[locais/planetas/eris.md\|Eris]] | Infested | Infested Alad V / Phorid | 38–48 | Nano Spores, Neurodes, Mutagen Sample |

### Áreas Especiais

| Local | Facção | Nível (Normal) | Acesso | Destaque |
|---|---|---|---|---|
| [[locais/planetas/void.md\|Void]] | Orokin | 25–40 | Junction de Phobos | Void Relics, Corrupted Vor, tileset Orokin |
| [[locais/planetas/lua.md\|Lua]] | Orokin / Sentient | 25–35 | The Second Dream (quest) | Spy avançado, tileset único, lore denso |
| [[locais/planetas/deimos.md\|Deimos]] | Infested / Entrati | 25–40 | Heart of Deimos (quest) | Família Entrati, Iso Vaults, Cambion Drift |
| [[locais/planetas/zariman.md\|Zariman Ten Zero]] | Void / Grineer antigo | 40–60 | Angels of the Zariman (quest) | Void Angels, The Holdfasts, Voidplumes |
| [[locais/planetas/kuva_fortress.md\|Fortaleza Kuva]] | Grineer | 25–35 | The War Within (quest) | Kuva Siphon, Kuva Flood, Kuva farm |


## Open Worlds — Warframe — Segunda Mente


Regiões de mapa aberto com ecossistemas, sindicatos e mecânicas exclusivas. Cada uma expande um planeta existente com camadas de conteúdo que vão muito além das missões convencionais.

| Open World | Planeta Base | Sindicato | Lançamento | Warframe Exclusivo |
|---|---|---|---|---|
| [[locais/open-worlds/cetus.md\|Planícies de Eidolon]] | Terra | Ostron (Cetus) | Out 2017 | Gara |
| [[locais/open-worlds/fortuna.md\|Orbe Vallis]] | Vênus | Solaris United (Fortuna) | Nov 2018 | Baruuk |
| [[locais/open-worlds/deimos.md\|Câmbion Drift]] | Deimos | Entrati (Necralisk) | Ago 2020 | Xaku, Lavos |
| [[locais/open-worlds/zariman.md\|Zariman Ten Zero]] | — (nave perdida) | The Holdfasts (Chrysalith) | Abr 2022 | Gyre |
| [[locais/open-worlds/duviri.md\|Duviri]] | — (dimensão do Void) | Kaithe (Drifter's Camp) | Abr 2023 | Kullervo |

### Planícies de Eidolon
*Terra · Ostron · Caça de Eidolons à noite, pesca, mineração*

O primeiro Open World do jogo — lançado em 2017, reformulou o que era possível em um jogo de missões procedurais. Durante o dia as Planícies são controladas por Grineer com bounties normais. À noite os Vomvalysts emergem e os Eidolons caminham — encontros de alto risco que exigem builds de Operator especializadas e coordenação de squad para derrotar os três Eidolons em uma única noite.

### Orbe Vallis
*Vênus · Solaris United · K-Drive, Profit-Taker, Thermia Fractures*

Mapa aberto ambientado em uma planície fria de Vênus ocupada pela Corpus. A narrativa gira em torno da dívida imposta aos Solaris — trabalhadores cujos corpos foram modificados como garantia de pagamento. O conteúdo end-game inclui o Profit-Taker Orb, boss de alta dificuldade que requer Mech ou squad especializado.

### Câmbion Drift
*Deimos · Entrati · Iso Vaults, Necramechs, ciclo Fass/Vome*

A superfície Infestada de Deimos — o terceiro Open World, ambientado em uma lua completamente consumida pelo vírus Technocyte. O ciclo dia/noite (Fass e Vome) muda os tipos de inimigos e recursos disponíveis. Os Iso Vaults são o conteúdo principal — missões de três andares desbloqueadas progressivamente que recompensam com partes de Necramech.

### Zariman Ten Zero
*Nave perdida no Void · The Holdfasts · Void Angels, missões Void*

Uma nave escolar Grineer que ficou presa no Void por décadas — os sobreviventes foram alterados pela exposição prolongada. O ambiente mistura arquitetura de nave com distorções do Void. Os Void Angels são os bosses da região — entidades que foram humanos antes da corrupção.

### Duviri
*Dimensão do Void · Kaithe · Modo roguelike, The Circuit, Kullervo*

Uma dimensão do Void governada pela psique fragmentada de Dominus Thrax — um reino de impossibilidades visuais e regras que mudam a cada run. O Duviri introduziu o primeiro modo roguelike do jogo: cada Testemunho começa com Warframe e armas aleatórias definidas pelo Decret ativo. The Circuit é o modo de farm de Incarnon Adapters, com rotação semanal de armas disponíveis.


## 💡 Curiosidades — Warframe — Segunda Mente


- Mercúrio é tecnicamente o planeta mais próximo do Sol no Sistema Origem, mas não é o primeiro desbloqueado — o jogo começa na Terra e Mercúrio é uma divergência lateral, refletindo a ordem de desenvolvimento do jogo.
- A Lua ficou inacessível por anos de jogo até The Second Dream em 2015 — o tileset foi construído especificamente para a revelação narrativa da quest, e voltar à Lua após completá-la tem um peso completamente diferente.
- As Planícies de Eidolon foram o maior mapa do jogo por anos — maiores que qualquer mapa de missão convencional em ordens de magnitude. A chegada do Orbe Vallis em 2018 a superou em área.
- Deimos é o único planeta do mapa estelar completamente coberto por Infested — não há facções convencionais na superfície, apenas a biomassa e os inimigos da família Entrati.
- O Duviri foi o primeiro local do jogo a não ser baseado em nenhum corpo celeste real do Sistema Solar — é uma dimensão do Void com leis físicas próprias, o que permitiu à DE criar a estética visual mais distinta da história do jogo.
- A Fortaleza Kuva era considerada irrelevante por anos antes de The War Within — após a quest, tornou-se destino regular de farm por Kuva e o único lugar com Siphons e Floods.
- Zariman foi o nome da nave antes de ser um local jogável — mencionado no lore desde o início do jogo como o evento que criou os Tenno. Chegar fisicamente à nave em 2022 foi um momento de fechamento narrativo para veteranos.
- O Void é o único bioma que não tem facção dominante no sentido convencional — os Corrupted são Orokin reanimados controlados pelo próprio ambiente, não uma civilização organizada.

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: ceres.md

# Ceres

> [!info] Visão Geral
> Cinturão de asteroides com bases Grineer pesadas

## Facção Principal — Warframe — Segunda Mente

- Grineer
- Inimigos: Lancers, Napalms, Bombards

## Missões Disponíveis — Warframe — Segunda Mente

- Exterminate, Defense, Survival, Sabotage

## Chefe — Warframe — Segunda Mente

- [[lore/chefes/lech_kril.md|Lech Kril (Exta)]] — recompensa: [[warframes/regular/frost.md|Frost]] partes

## Recursos Notáveis — Warframe — Segunda Mente

- Alloy Plate
- Ferrite
- Orokin Cell

## 🔗 Relacionados — Warframe — Segunda Mente

- Chefe: [[lore/chefes/lech_kril.md|Lech Kril]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: deimos.md

# Deimos / Cambion Drift

> [!info] O que é
> Terceiro Open World — lua infestada de Marte. Necralisk é o hub e Cambion Drift é o exterior infestado.

## 🌍 Onde Conseguir — Warframe — Segunda Mente

- Pré-requisito: Heart of Deimos (quest)
- Rota: Marte → nó Deimos

## O que fazer aqui — Warframe — Segunda Mente

- Bounties com Son/Grandmother
- Caça a Necramechs
- Criação de Necramechs
- Conservação de animais

## Facção: Entrati — Warframe — Segunda Mente

- Moeda: Entrati Standing
- Cap diário de standing: MR × 1.000

## Recursos Exclusivos — Warframe — Segunda Mente

- Bile
- Spinal Core Section
- Thaumic Distillate

## Recompensas de Bounty — Warframe — Segunda Mente

- Partes de Necramech
- mods Deimos
- Xaku blueprint

## 🔗 Relacionados — Warframe — Segunda Mente

- Boss: [[lore/chefes/zealoid_prelate.md|Zealoid Prelate]]
- Sindicato: [[mecanicas/sindicatos/entrati.md|Entrati]]
- Open World: [[locais/open-worlds/deimos.md|Câmbion Drift]]
- Warframes: [[warframes/regular/xaku.md|Xaku]], [[warframes/regular/lavos.md|Lavos]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: eris.md

# Eris

> [!info] Visão Geral
> Planeta completamente infestado, origem do Technocyte

## Facção Principal — Warframe — Segunda Mente

- Infested
- Inimigos: Chargers, Ancients, Crawlers, Infested Corpus

## Missões Disponíveis — Warframe — Segunda Mente

- Exterminate, Survival, Defense, Infested Salvage

## Chefe — Warframe — Segunda Mente

- [[lore/chefes/jordas_golem.md|Jordas Golem]] / [[lore/chefes/phorid.md|Phorid]] — recompensa: [[warframes/regular/atlas.md|Atlas]] (quest), [[warframes/regular/nyx.md|Nyx]] (Phorid)

## Recursos Notáveis — Warframe — Segunda Mente

- Nano Spores
- Plastids
- Neurodes

## 🔗 Relacionados — Warframe — Segunda Mente

- Chefe: [[lore/chefes/jordas_golem.md|Jordas Golem]] · [[lore/chefes/phorid.md|Phorid]]
- Recursos: [[recursos/]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: europa.md

# Europa

> [!info] Visão Geral
> Lua gelada com bases subaquáticas

## Facção Principal — Warframe — Segunda Mente

- Corpus
- Inimigos: Crewmen, MOAs, Ospreys

## Missões Disponíveis — Warframe — Segunda Mente

- Defense, Survival, Mobile Defense, Exterminate

## Chefe — Warframe — Segunda Mente

- [[lore/chefes/raptors.md|Raptors (Naamah)]] — recompensa: Nova partes

## Recursos Notáveis — Warframe — Segunda Mente

- Ferrite
- Salvage
- Control Module

## 🔗 Relacionados — Warframe — Segunda Mente

- Chefe: [[lore/chefes/raptors.md|Raptors]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: jupiter.md

# Júpiter

> [!info] Visão Geral
> Gigante gasoso com instalações flutuantes Corpus

## Facção Principal — Warframe — Segunda Mente

- Corpus
- Inimigos: Crewmen, MOAs, Amalgams

## Missões Disponíveis — Warframe — Segunda Mente

- Exterminate, Spy, Capture, Junction

## Chefe — Warframe — Segunda Mente

- [[lore/chefes/alad_v.md|Alad V (Themisto)]] — recompensa: [[warframes/regular/nyx.md|Nyx]] partes

## Recursos Notáveis — Warframe — Segunda Mente

- Circuits
- Oxium
- Salvage

## 🔗 Relacionados — Warframe — Segunda Mente

- Chefe: [[lore/chefes/alad_v.md|Alad V]]
- Boss especial: [[lore/chefes/ropalolyst.md|Ropalolyst]] — recompensa: [[warframes/regular/wisp.md|Wisp]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: kuva_fortress.md


----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: lua.md

# Lua

> [!info] Visão Geral
> Instalações Orokin na Lua, desbloqueada após The Second Dream

## Facção Principal — Warframe — Segunda Mente

- Orokin/Sentient
- Inimigos: Corrupted, Sentients

## Missões Disponíveis — Warframe — Segunda Mente

- Exterminate, Spy, Rescue, Survival, Crossfire

## Chefe — Warframe — Segunda Mente

- [[lore/chefes/corrupted_vor.md|Vor Corrompido (Tycho)]] — recompensa: Mods Lua raros

## Recursos Notáveis — Warframe — Segunda Mente

- Oxium
- Neural Sensors
- mods Lua

## 🔗 Relacionados — Warframe — Segunda Mente

- Chefe: [[lore/chefes/corrupted_vor.md|Vor Corrompido]]
- Recursos: [[recursos/]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: marte.md

# Marte

> [!info] Visão Geral
> Planeta árido com territórios disputados

## Facção Principal — Warframe — Segunda Mente

- Grineer/Corpus
- Inimigos: Lancers, Crewmen, Hyenas

## Missões Disponíveis — Warframe — Segunda Mente

- Exterminate, Defense, Spy, Mobile Defense

## Chefe — Warframe — Segunda Mente

- [[lore/chefes/lech_kril.md|Lech Kril & Vor (War)]] — recompensa: [[warframes/regular/excalibur.md|Excalibur]] partes

## Recursos Notáveis — Warframe — Segunda Mente

- Morphics
- Gallium
- Rubedo

## 🔗 Relacionados — Warframe — Segunda Mente

- Chefe: [[lore/chefes/lech_kril.md|Lech Kril]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: mercurio.md

# Mercúrio

> [!info] Visão Geral
> Primeiro planeta, tutorial do sistema solar

## Facção Principal — Warframe — Segunda Mente

- Grineer
- Inimigos: Lancers, Troopers, Commanders

## Missões Disponíveis — Warframe — Segunda Mente

- Exterminate, Mobile Defense, Spy, Capture

## Chefe — Warframe — Segunda Mente

- [[lore/chefes/captain_vor.md|Captain Vor (Tolstoj)]] — recompensa: Morphics, créditos

## Recursos Notáveis — Warframe — Segunda Mente

- Ferrite
- Polymer Bundle
- Morphics

## 🔗 Relacionados — Warframe — Segunda Mente

- Chefe: [[lore/chefes/captain_vor.md|Captain Vor]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: neptuno.md

# Netuno

> [!info] Visão Geral
> Profundezas oceânicas com refinarias Corpus

## Facção Principal — Warframe — Segunda Mente

- Corpus
- Inimigos: Crewmen, MOAs, Hyenas

## Missões Disponíveis — Warframe — Segunda Mente

- Exterminate, Capture, Spy, Hijack

## Chefe — Warframe — Segunda Mente

- [[lore/chefes/hyena_pack.md|Hyena Pack (Psamathe)]] — recompensa: [[warframes/regular/loki.md|Loki]] partes

## Recursos Notáveis — Warframe — Segunda Mente

- Nano Spores
- Ferrite
- Control Module

## 🔗 Relacionados — Warframe — Segunda Mente

- Chefe: [[lore/chefes/hyena_pack.md|Hyena Pack]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: phobos.md

# Phobos

> [!info] Visão Geral
> Lua de Marte com instalações Corpus em ruínas

## Facção Principal — Warframe — Segunda Mente

- Corpus
- Inimigos: Crewmen, MOAs, Ospreys

## Missões Disponíveis — Warframe — Segunda Mente

- Exterminate, Capture, Mobile Defense, Rescue

## Chefe — Warframe — Segunda Mente

- [[lore/chefes/lech_kril.md|Lech Kril & Vor (Iliad)]] — recompensa: [[warframes/regular/frost.md|Frost]] partes

## Recursos Notáveis — Warframe — Segunda Mente

- Morphics
- Salvage
- Circuits

## 🔗 Relacionados — Warframe — Segunda Mente

- Chefe: [[lore/chefes/lech_kril.md|Lech Kril]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: plutao.md

# Plutão

> [!info] Visão Geral
> Mundo frio e distante com laboratórios Corpus

## Facção Principal — Warframe — Segunda Mente

- Corpus
- Inimigos: Crewmen, MOAs, Ospreys

## Missões Disponíveis — Warframe — Segunda Mente

- Exterminate, Defense, Survival, Interception

## Chefe — Warframe — Segunda Mente

- [[lore/chefes/ambulas.md|Ambulas (Hades)]] — recompensa: [[warframes/regular/mesa.md|Mesa]] partes

## Recursos Notáveis — Warframe — Segunda Mente

- Nano Spores
- Plastids
- Circuits

## 🔗 Relacionados — Warframe — Segunda Mente

- Chefe: [[lore/chefes/ambulas.md|Ambulas]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: saturno.md

# Saturno

> [!info] Visão Geral
> Anel planetário com fortalezas Grineer massivas

## Facção Principal — Warframe — Segunda Mente

- Grineer
- Inimigos: Lancers, Napalms, Bombards, Corrupted

## Missões Disponíveis — Warframe — Segunda Mente

- Exterminate, Defense, Survival, Spy

## Chefe — Warframe — Segunda Mente

- [[lore/chefes/sargas_ruk.md|Sargas Ruk (Tethys)]] — recompensa: [[warframes/regular/ember.md|Ember]] partes

## Recursos Notáveis — Warframe — Segunda Mente

- Alloy Plate
- Nano Spores
- Orokin Cell

## 🔗 Relacionados — Warframe — Segunda Mente

- Chefe: [[lore/chefes/sargas_ruk.md|Sargas Ruk]]
- Recursos: [[recursos/]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: sedna.md

# Sedna

> [!info] Visão Geral
> Planeta distante com arenas Grineer (Rathuum)

## Facção Principal — Warframe — Segunda Mente

- Grineer
- Inimigos: Lancers, Bombards, Executioners (Rathuum)

## Missões Disponíveis — Warframe — Segunda Mente

- Exterminate, Defense, Survival, Rathuum (Arena)

## Chefe — Warframe — Segunda Mente

- [[lore/chefes/kela_de_thaym.md|Kela de Thaym (Merrow)]] — recompensa: [[warframes/regular/saryn.md|Saryn]] partes

## Recursos Notáveis — Warframe — Segunda Mente

- Nano Spores
- Plastids
- Rubedo

## 🔗 Relacionados — Warframe — Segunda Mente

- Chefe: [[lore/chefes/kela_de_thaym.md|Kela de Thaym]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: terra.md

# Terra

> [!info] Visão Geral
> Planeta natal dos humanos, agora dominado pelo Grineer

## Facção Principal — Warframe — Segunda Mente

- Grineer
- Inimigos: Lancers, Scorpions, Ballistas

## Missões Disponíveis — Warframe — Segunda Mente

- Exterminate, Rescue, Spy, Sabotage

## Chefe — Warframe — Segunda Mente

- [[lore/chefes/vay_hek.md|Vay Hek (Oro)]] — recompensa: [[warframes/regular/hydroid.md|Hydroid]] partes

## Recursos Notáveis — Warframe — Segunda Mente

- Neurodes
- Ferrite
- Rubedo

## 🔗 Relacionados — Warframe — Segunda Mente

- Chefe: [[lore/chefes/vay_hek.md|Vay Hek]]
- Open World: [[locais/open-worlds/cetus.md|Planícies de Eidolon (Cetus)]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: urano.md

# Urano

> [!info] Visão Geral
> Planeta inclinado com shipyards subaquáticos

## Facção Principal — Warframe — Segunda Mente

- Grineer
- Inimigos: Lancers, Scorch, Hellions

## Missões Disponíveis — Warframe — Segunda Mente

- Exterminate, Sabotage, Spy, Survival

## Chefe — Warframe — Segunda Mente

- [[lore/chefes/tyl_regor.md|Tyl Regor (Titania)]] — recompensa: [[warframes/regular/equinox.md|Equinox]] partes

## Recursos Notáveis — Warframe — Segunda Mente

- Alloy Plate
- Plastids
- Tellurium

## 🔗 Relacionados — Warframe — Segunda Mente

- Chefe: [[lore/chefes/tyl_regor.md|Tyl Regor]]
- Recursos: [[recursos/]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: venus.md

# Vênus

> [!info] Visão Geral
> Planeta Corpus com ambientes frios e interiores corporativos

## Facção Principal — Warframe — Segunda Mente

- Corpus
- Inimigos: Crewmen, MOAs, Ospreys

## Missões Disponíveis — Warframe — Segunda Mente

- Exterminate, Capture, Spy, Defense

## Chefe — Warframe — Segunda Mente

- [[lore/chefes/jackal.md|Jackal (Fossa)]] — recompensa: [[warframes/regular/rhino.md|Rhino]] partes

## Recursos Notáveis — Warframe — Segunda Mente

- Polymer Bundle
- Circuits
- Rubedo

## 🔗 Relacionados — Warframe — Segunda Mente

- Chefe: [[lore/chefes/jackal.md|Jackal]]
- Open World: [[locais/open-worlds/fortuna.md|Orbe Vallis (Fortuna)]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: void.md

# Void

> [!info] Visão Geral
> Dimensão Orokin com Torres e missões Fissure

## Facção Principal — Warframe — Segunda Mente

- Orokin
- Inimigos: Corrupted enemies (versões corrompidas de Grineer e Corpus)

## Missões Disponíveis — Warframe — Segunda Mente

- Exterminate, Defense, Survival, Sabotage, Capture (Fissure missions)

## Chefe — Warframe — Segunda Mente

- [[lore/chefes/corrupted_vor.md|Corrupted Vor]] — recompensa: mods Orokin, Argon Crystal

## Recursos Notáveis — Warframe — Segunda Mente

- Argon Crystal
- Forma
- mods raros

## 🔗 Relacionados — Warframe — Segunda Mente

- Chefe: [[lore/chefes/corrupted_vor.md|Corrupted Vor]]

----------------------------------------

## Seção: locais\planetas — Warframe — Segunda Mente

### 📄 arquivo: zariman.md

# Zariman Ten Zero

> [!info] O que é
> Nave Orokin fantasma presa no Void. Chrysalith é o hub e os andares da nave são as missões.

## 🌍 Onde Conseguir — Warframe — Segunda Mente

- Pré-requisito: Angels of the Zariman (quest)
- Rota: Via menu de missões após a quest

## O que fazer aqui — Warframe — Segunda Mente

- Bounties com Cavalero
- Farming de Incarnon Adapters
- Missões Void especiais

## Facção: The Holdfasts — Warframe — Segunda Mente

- Moeda: Voidplume / Holdfasts Standing
- Cap diário de standing: MR × 1.000

## Recursos Exclusivos — Warframe — Segunda Mente

- Voidplume
- Calx
- Aggristone

## Recompensas de Bounty — Warframe — Segunda Mente

- Incarnon Adapters
- mods Incarnon Genesis
- Styanax blueprint

## 🔗 Relacionados — Warframe — Segunda Mente

- Boss: [[lore/chefes/void_angel.md|Void Angel]]
- Sindicato: [[mecanicas/sindicatos/the_holdfasts.md|The Holdfasts]]
- Warframes: [[warframes/regular/voruna.md|Voruna]], [[warframes/regular/gyre.md|Gyre]]

----------------------------------------

## Seção: locais\open-worlds — Warframe — Segunda Mente

### 📄 arquivo: cetus.md

# Cetus / Plains of Eidolon

> [!info] O que é
> Primeiro Open World. Cetus é a cidade hub e Plains of Eidolon é o campo aberto na Terra.

## 🌍 Onde Conseguir — Warframe — Segunda Mente

- Pré-requisito: The Second Dream
- Rota: Terra → nó Cetus

## O que fazer aqui — Warframe — Segunda Mente

- Bounties com Konzu
- Caça aos Eidolons (noite)
- Pescaria
- Mineração
- Crafting de Amps

## Facção: Ostron — Warframe — Segunda Mente

- Moeda: Ostron Standing
- Cap diário de standing: MR × 1.000

## Recursos Exclusivos — Warframe — Segunda Mente

- Cetus Wisps
- Iradite
- Grokdrul
- Nistlepod

## Recompensas de Bounty — Warframe — Segunda Mente

- Partes de Amp
- mods Vigilante Set
- blueprints de [[warframes/regular/gara.md|Gara]]

## 🔗 Relacionados — Warframe — Segunda Mente

- Sistema: [[sistemas/plains-e-bounties|Plains & Bounties]]

----------------------------------------

## Seção: locais\open-worlds — Warframe — Segunda Mente

### 📄 arquivo: deimos.md


----------------------------------------

## Seção: locais\open-worlds — Warframe — Segunda Mente

### 📄 arquivo: duviri.md

# Duviri

> [!info] O que é
> Mundo surreal dentro do Void governado por Thrax. Roguelite com Warframes aleatórios.

## 🌍 Onde Conseguir — Warframe — Segunda Mente

- Pré-requisito: The Duviri Paradox (quest)
- Rota: Via menu de missões após a quest

## O que fazer aqui — Warframe — Segunda Mente

- The Circuit (roguelite)
- Duviri Proper (mundo aberto)
- coleta de Intrinsics

## Facção: — (Dominus Thrax) — Warframe — Segunda Mente

- Moeda: Duviri Intrinsic
- Cap diário de standing: MR × 1.000

## Recursos Exclusivos — Warframe — Segunda Mente

- Pathos Clamp
- Solaris United Toroids

## Recompensas de Bounty — Warframe — Segunda Mente

- Incarnon Genesis mods
- Archon Shards
- Kullervo blueprint

## 🔗 Relacionados — Warframe — Segunda Mente

- Sistema: [[sistemas/plains-e-bounties|Plains & Bounties]]

----------------------------------------

## Seção: locais\open-worlds — Warframe — Segunda Mente

### 📄 arquivo: fortuna.md

# Fortuna / Orb Vallis

> [!info] O que é
> Segundo Open World em Vênus. Fortuna é o hub subterrâneo e Orb Vallis é o ambiente frio exterior.

## 🌍 Onde Conseguir — Warframe — Segunda Mente

- Pré-requisito: Vênus desbloqueado
- Rota: Vênus → nó Fortuna

## O que fazer aqui — Warframe — Segunda Mente

- Bounties com Eudico
- K-Drive races
- Crafting de Kitguns/Moas
- Caça às Orb Mothers

## Facção: Solaris United — Warframe — Segunda Mente

- Moeda: Solaris United Standing
- Cap diário de standing: MR × 1.000

## Recursos Exclusivos — Warframe — Segunda Mente

- Debt-Bonds
- Toroids
- Thermia

## Recompensas de Bounty — Warframe — Segunda Mente

- Kitguns
- Moa companions
- mods especiais
- Garuda partes

## 🔗 Relacionados — Warframe — Segunda Mente

- Sistema: [[sistemas/plains-e-bounties|Plains & Bounties]]

----------------------------------------

## Seção: locais\open-worlds — Warframe — Segunda Mente

### 📄 arquivo: zariman.md


----------------------------------------

## Seção: lore — Warframe — Segunda Mente

### 📄 arquivo: _Lore _Indice.md

> [!quote]
> *"Você sabe o que está dentro desses Warframes, Tenno? Você sabe o que você é?"*
> — Lotus

> [!warning] Esta seção contém spoilers das quests principais. Preencha cada arquivo após completar a quest correspondente.


## O Universo de Warframe — Warframe — Segunda Mente


O universo de Warframe se passa em um futuro distante dentro do Sistema Solar — chamado de Sistema Origem — milhares de anos após o colapso de uma civilização avançada conhecida como Orokin. O que os jogadores encontram ao chegar é um sistema fragmentado: guerras antigas ainda em curso, facções que disputam os destroços do passado, e uma verdade sobre a natureza do próprio personagem que só se revela lentamente através das quests.

A lore do jogo não é apresentada de forma direta. Ela está espalhada em fragmentos: diálogos durante missões, arquivos de codex, esculturas Ayatan, coleções de Cephalon e — principalmente — nas Jornadas. Cada quest principal desvela uma camada da história, e algumas revelações fundamentais só chegam após dezenas ou centenas de horas de jogo. O jogador que ignora a narrativa e foca apenas no gameplay perde uma das histórias de ficção científica mais elaboradas dos jogos modernos.

A narrativa central gira em torno de uma pergunta que o jogo demora anos para responder completamente: *quem é o Tenno?* A resposta, revelada progressivamente desde The Second Dream até 1999, redefine tudo — a relação com os Warframes, com a Lotus, com o próprio corpo do personagem. Entender a lore é entender por que cada sistema de jogo existe.


## Cronologia — Warframe — Segunda Mente


A história do universo Warframe se divide em eras definidas por eventos catastróficos. A cronologia completa está documentada em [[lore/cronologia/cronologia.md|Cronologia do Universo]].

| Era | Período | Evento Central |
|---|---|---|
| [[lore/cronologia/era_orokin.md\|Era Orokin]] | Passado distante | Apogeu da civilização Orokin — conquista do Sistema Origem e expansão ao Tau |
| [[lore/cronologia/antiga_guerra.md\|A Antiga Guerra]] | Passado distante | Rebelião dos Sentient contra os Orokin — o início do fim |
| [[lore/cronologia/o_colapso.md\|O Colapso]] | Passado distante | Traição dos Tenno — queda do Império Orokin e colapso da civilização |
| [[lore/cronologia/era_do_despertar.md\|Era do Despertar]] | Presente do jogo | Tenno acordam — guerras entre Grineer, Corpus e Infested pelo Sistema Origem |
| [[lore/cronologia/a_nova_guerra.md\|A Nova Guerra]] | Presente do jogo | Invasão Sentient liderada por Ballas — o conflito que define o fim do mundo conhecido |
| [[lore/cronologia/ecos_do_vazio.md\|Ecos do Void]] | Presente do jogo | Pós-guerra — Zariman, Duviri, Sanctum e as consequências da Nova Guerra |


## Facções — Warframe — Segunda Mente


As facções são os grupos que habitam, combatem e sobrevivem no Sistema Origem. Cada uma tem origem, motivação e papel narrativo distintos — e todas têm conexão direta com o legado Orokin.

| Facção | Origem | Papel no Universo |
|---|---|---|
| [[lore/faccoes/orokin.md\|Orokin]] | Civilização ancestral | Criadores dos Warframes, Tenno, Sentient e praticamente toda a tecnologia avançada do universo |
| [[lore/faccoes/tenno.md\|Tenno]] | Sobreviventes da tragédia Zariman | Guerreiros ligados aos Warframes via Transference — protagonistas da história |
| [[lore/faccoes/sentient.md\|Sentient]] | IA criada pelos Orokin | Enviados ao sistema Tau, se rebelaram e retornaram para destruir seus criadores |
| [[lore/faccoes/grineer.md\|Grineer]] | Clones degradados de trabalhadores Orokin | Império militarista em expansão — domina metade do Sistema Origem |
| [[lore/faccoes/corpus.md\|Corpus]] | Corporação mercantil | Escavam e revendem tecnologia Orokin — movidos por lucro e doutrina do Dinheiro como divindade |
| [[lore/faccoes/infested.md\|Infested]] | Vítimas do vírus Technocyte | Biomassa parasitária que consome tudo — não têm hierarquia organizada, apenas fome |
| [[lore/faccoes/dax.md\|Dax]] | Soldados de elite Orokin | Guardiões dos Orokin condicionados pela Continuidade — alguns sobreviveram ao Colapso |
| [[lore/faccoes/murmur.md\|Murmur]] | Entidades do Void | Criações de Albrecht Entrati — emergem do Sanctum Anatomica como ameaça pós-New War |


## Personagens — Warframe — Segunda Mente


### Figuras Centrais

Personagens com papel narrativo direto na história principal — presentes em múltiplas quests ou responsáveis por revelações fundamentais.

| Personagem | Facção | Papel |
|---|---|---|
| [[lore/personagens/lotus.md\|Lotus / Natah]] | Sentient / Tenno | Guia dos Tenno — sua verdadeira identidade é o núcleo da narrativa |
| [[lore/personagens/teshin.md\|Teshin]] | Dax | Guardião Dax que sobreviveu ao Colapso — mentor e antagonista em diferentes momentos |
| [[lore/personagens/ballas.md\|Ballas]] | Orokin | Executor Orokin traidor — criador dos Warframes modernos, villain central |
| [[lore/personagens/hunhow.md\|Hunhow]] | Sentient | Pai de Natah — general Sentient que ameaça destruir os Tenno de dentro |
| [[lore/personagens/erra.md\|Erra]] | Sentient | Irmão de Natah — general que lidera a invasão da Nova Guerra |
| [[lore/personagens/albrecht_entrati.md\|Albrecht Entrati]] | Orokin | Cientista que descobriu o Void — sua pesquisa é a origem de quase tudo |
| [[lore/personagens/margulis.md\|Margulis]] | Orokin (dissidente) | Cientista que salvou e educou os Tenno — executada pelos Orokin por isso |
| [[lore/personagens/the_drifter.md\|The Drifter]] | Tenno | Versão alternativa do Operador — protagonista do Duviri e do arco de 1999 |

### Aliados e NPCs

Personagens recorrentes que apoiam, guiam ou fornecem contexto narrativo ao longo do jogo.

| Personagem | Contexto | Papel |
|---|---|---|
| [[lore/personagens/ordis.md\|Ordis]] | Nave do jogador | Cephalon da nave — IA com memórias fragmentadas de um passado violento |
| [[lore/personagens/cephalon_simaris.md\|Cephalon Simaris]] | Relays | Cephalon obcecado por preservar conhecimento — gerencia o Sanctuary |
| [[lore/personagens/cephalon_cy.md\|Cephalon Cy]] | Railjack | Cephalon militar que comanda a nave Railjack — sarcástico e pragmático |
| [[lore/personagens/nora_night.md\|Nora Night]] | Nightwave | Apresentadora de rádio misteriosa — voz do Nightwave e comentarista do Sistema Origem |
| [[lore/personagens/baro_kiteer.md\|Baro Ki'Teer]] | Relays | Comerciante de itens Prime — sua obsessão por tecnologia Orokin tem raízes narrativas |
| [[lore/personagens/eudico.md\|Eudico]] | Fortuna | Líder de fato dos Solaris United — carrega implante de dívida Corpus |
| [[lore/personagens/little_duck.md\|Little Duck]] | Vox Solaris | Agente clandestina de Fortuna — conecta ao conteúdo de Orb Mothers |
| [[lore/personagens/loid.md\|Loid e Otak]] | Necralisk | Synovia Entrati dividido em duas personalidades — guia do Câmbion Drift |
| [[lore/personagens/onkko.md\|Onkko / The Quills]] | Planícies de Eidolon | Líder dos Quills — revelado como versão alternativa de Teshin em outra linha do tempo |
| [[lore/personagens/cavalero.md\|Cavalero]] | Duviri | Fabricante de armas no Duviri — figura central das recompensas do circuito |
| [[lore/personagens/dominus_thrax.md\|Dominus Thrax]] | Duviri | Rei do Duviri — sua psique fragmentada é o próprio reino |
| [[lore/personagens/arthur.md\|Arthur]] | 1999 | Protagonista do arco 1999 — conexão entre o passado pré-Orokin e o presente |

### Antagonistas

| Personagem | Facção | Papel |
|---|---|---|
| [[lore/personagens/vor.md\|Vor]] | Grineer | Primeiro antagonista do jogo — comandante que desperta o Tenno com a Janus Key |
| [[lore/personagens/grandmother_entrati.md\|Avó Entrati]] | Entrati | Matriarca da família — guarda segredos sobre Albrecht e o Void |
| [[lore/personagens/father_entrati.md\|Pai Entrati]] | Entrati | Filho de Albrecht — fragmentado pelo Void, manufatura Necramechs |
| [[lore/personagens/son_entrati.md\|Filho Entrati]] | Entrati | Responsável pelos companheiros Infestados — Son Tokens |
| [[lore/personagens/daughter_entrati.md\|Filha Entrati]] | Entrati | Especialista em pesca Infestada — Daughter Tokens |
| [[lore/personagens/mother_entrati.md\|Mãe Entrati]] | Entrati | Portal entre mundos — distribui bounties do Câmbion Drift |


## Chefes — Warframe — Segunda Mente


### Bosses de Planeta

Cada planeta tem um boss fixo desbloqueado após completar a Junction correspondente. São a principal fonte de partes de Warframe.

| Boss | Planeta | Facção | Warframe que Dropa |
|---|---|---|---|
| [[lore/chefes/captain_vor.md\|Captain Vor]] | Mercúrio | Grineer | — (Vor's Prize) |
| [[lore/chefes/jackal.md\|Jackal]] | Vênus | Corpus | Rhino |
| [[lore/chefes/vay_hek.md\|Vay Hek]] | Terra | Grineer | Hydroid |
| [[lore/chefes/lech_kril.md\|Lech Kril]] | Marte / Ceres | Grineer | Excalibur / Frost |
| [[lore/chefes/sargas_ruk.md\|Sargas Ruk]] | Saturno | Grineer | Ember |
| [[lore/chefes/alad_v.md\|Alad V]] | Júpiter | Corpus | Nyx |
| [[lore/chefes/raptors.md\|Raptors]] | Europa | Corpus | Nova |
| [[lore/chefes/tyl_regor.md\|Tyl Regor]] | Urano | Grineer | Equinox |
| [[lore/chefes/ambulas.md\|Ambulas]] | Plutão | Corpus | Mesa |
| [[lore/chefes/kela_de_thaym.md\|Kela de Thaym]] | Sedna | Grineer | Saryn |
| [[lore/chefes/phorid.md\|Phorid]] | Eris (invasão) | Infested | Nyx (alternativo) |
| [[lore/chefes/hyena_pack.md\|Hyena Pack]] | Netuno | Corpus | Loki |
| [[lore/chefes/corrupted_vor.md\|Corrupted Vor]] | Void | Orokin corrompido | — (loot de Void) |
| [[lore/chefes/jordas_golem.md\|Jordas Golem]] | Eris | Infested | Atlas (quest) |
| [[lore/chefes/zealoid_prelate.md\|Zealoid Prelate]] | Deimos | Infested | Harrow Systems |

### Bosses Especiais e End-Game

| Boss | Contexto | Recompensa Principal |
|---|---|---|
| [[lore/chefes/stalker.md\|Stalker / Shadow Stalker]] | Assassino que persegue o Tenno | Mods Stalker exclusivos, Dread / Despair / Hate |
| [[lore/chefes/eidolon_teralyst.md\|Eidolon Teralyst]] | Planícies — noite | Eidolon Shard, Arcanes |
| [[lore/chefes/eidolon_gantulyst.md\|Eidolon Gantulyst]] | Planícies — noite (Tridolon) | Brilliant Eidolon Shard, Arcanes superiores |
| [[lore/chefes/eidolon_hydrolyst.md\|Eidolon Hydrolyst]] | Planícies — noite (Tridolon) | Radiant Eidolon Shard, melhores Arcanes |
| [[lore/chefes/profit_taker.md\|Profit-Taker Orb]] | Orbe Vallis — fase 4 | Toroids raros, Arcanes, Atmo Systems |
| [[lore/chefes/exploiter_orb.md\|Exploiter Orb]] | Orbe Vallis — missão especial | Diluted Thermia, mods exclusivos |
| [[lore/chefes/ropalolyst.md\|Ropalolyst]] | Júpiter — Junction | Wisp blueprints |
| [[lore/chefes/hemocyte.md\|Hemocyte]] | Evento Plague Star | Helminth Charger, mods exclusivos |
| [[lore/chefes/archon_boreal.md\|Archon Boreal]] | Archon Hunt semanal | Archon Shard Azure |
| [[lore/chefes/archon_amar.md\|Archon Amar]] | Archon Hunt semanal | Archon Shard Crimson |
| [[lore/chefes/archon_nira.md\|Archon Nira]] | Archon Hunt semanal | Archon Shard Teal |
| [[lore/chefes/kullervo.md\|Kullervo]] | Duviri — boss fixo | Kullervo blueprints |
| [[lore/chefes/void_angel.md\|Void Angel]] | Zariman — boss de área | Voidplume Intact, Arcanes Zariman |


## 💡 Curiosidades — Warframe — Segunda Mente


- A revelação de The Second Dream em 2015 foi um momento cultural para a comunidade — jogadores relataram parar de jogar por minutos ao perceber a verdade sobre o Tenno, e o jogo ganhou milhares de novos jogadores apenas por boca a boca sobre a twist.
- Ballas foi introduzido como narrador misterioso dos Codex muito antes de aparecer fisicamente no jogo — veteranos que leram os fragmentos reconheceram sua voz em The Sacrifice imediatamente.
- O lore de Albrecht Entrati, revelado em Whispers in the Walls, recontextualiza eventos que aconteceram milhares de anos antes dos Grineer e Corpus existirem — tornando-o o personagem com o maior impacto retroativo na narrativa.
- Ordis foi originalmente um guerreiro chamado Ordan Karris — um dos assassinos mais temidos da era Orokin. Sua transformação em Cephalon foi uma punição, e fragmentos de sua personalidade original vazam em certas falas.
- O Stalker nunca foi explicado completamente em uma única quest — sua história é construída através de fragmentos, drops de mods e o lore de The Second Dream, The Sacrifice e a quest A Man of Few Words.
- A família Entrati é uma das adições narrativas mais aclamadas do jogo — cada membro representa uma fase do luto e da disfunção familiar, e o jogador precisa navegar essa dinâmica para progredir em Deimos.
- Nora Night é amplamente teorizada como sendo a própria Lotus em uma forma alternativa, ou uma entidade do Void — a DE nunca confirmou sua verdadeira identidade, mantendo o mistério como parte do personagem.
- O Duviri Paradox revelou que o Drifter e o Operador são a mesma pessoa em linhas do tempo diferentes — uma das estruturas narrativas mais ambiciosas já implementadas em um jogo live-service.

----------------------------------------

## Seção: lore\cronologia — Warframe — Segunda Mente

### 📄 arquivo: antiga_guerra.md

# A Antiga Guerra

> [!info] A Rebelião das máquinas e a batalha sangrenta das criações que testou o Império Dourado.

## O Projeto Terraformador — Warframe — Segunda Mente

[Inserir explicação sobre os Sentients, máquinas capazes de se adaptar aos danos físicos, enviados para preparar o sistema em Tau.]

## O Retorno de Tau — Warframe — Segunda Mente

[A rebelião dos Sentients, o descarte de restrições robóticas e o retorno focado em aniquilar a praga que são seus criadores (os Orokin).]

## A Criação Tardia: Warframes — Warframe — Segunda Mente

[Os experimentos sombrios do Executor Ballas manipulando a Muta-cepa Helminth em infantes e grandes guerreiros Dax decaídos.]

## A Simbiose Perfeita (Tenno e Frames) — Warframe — Segunda Mente

[A intervenção de Margulis / Lotus e o uso da *Transferência* para controlar as armaduras incontroláveis de Infestação. A virada bélica contra as Frotas Sentients.]

----------------------------------------

## Seção: lore\cronologia — Warframe — Segunda Mente

### 📄 arquivo: a_nova_guerra.md

# A Nova Guerra

> [!info] A Invasão irredutível contra o Sistema Origem e o governo absoluto das Sombras e "Falsificações" pelo império Narmer.

## A Invasão Sentient — Warframe — Segunda Mente

[A investida monumental da Armada Sentient (conduzida pelo renascido Erra) que penetrou todos os planetas, escravizando e obliterando fileiras de Corpus, Grineer e Tenno igualmente.]

## A Queda (Ballas e A Máscara de Narmer) — Warframe — Segunda Mente

[Sem a proteção da Lua ou Lotus, fomos obliterados. Ballas e Erra subjugam todo o Sistema Origem criando uma seita divina mental universal através dos véus: O governo indissolúvel de **Narmer**. Todos que usam o véu não veem o horror, apenas glória iluminada e um sol gentil.]

## O Despertar do Derivante (Drifter) — Warframe — Segunda Mente

[A introdução das paradoxais leis do temporal e multiversal: A versão do passageiro que não aceitou a barganha no Vazio ressurge, empunhando apenas de táticas "mortais", resgatando os destroços de um sistema em agonia contra os Diáconos. Destacando suporte do Herói Grineer independente que formou O Acampamento, Kahl-175.]

## O Colapso do Falso Deus Divino — Warframe — Segunda Mente

[A união final entre as partes somáticas (Drifter e Operador) resgatando Praghasa e derrotando os desígnios manipuladores de Ballas frente a Margulis e a Natah originais. O sistema livre – mas eternamente machucado pelas cicatrizes físicas e sociais que as cascas de Narmer deixaram nos habitantes.]

----------------------------------------

## Seção: lore\cronologia — Warframe — Segunda Mente

### 📄 arquivo: cronologia.md

# Cronologia do Universo Warframe

> [!warning] Spoilers de todas as quests principais. Preencher progressivamente conforme completar as quests.

## Era Orokin (passado distante) — Warframe — Segunda Mente


> Preencher após completar [[missoes/jornadas/principais/the_sacrifice.md|The Sacrifice]] e [[missoes/jornadas/principais/the_new_war.md|The New War]].

- Os [[lore/faccoes/orokin.md|Orokin]] dominam o Sistema Solar
- Projeto Zariman: crianças enviadas ao Void retornam como Tenno
- [[lore/personagens/margulis.md|Margulis]] protege as crianças Tenno do extermínio
- Criação dos primeiros Warframes como armas de guerra
- Envio dos Sentient ao Sistema Tau para terraformação
- Rebelião dos Sentient: retornam corrompidos pelo Void
- Rebelião dos Tenno: queda do Império Orokin

## Era Atual (eventos do jogo) — Warframe — Segunda Mente


- Grineer e Corpus dividem o Sistema Solar após colapso Orokin
- [[lore/personagens/lotus.md|Lotus]] desperta os Tenno do criostasis
- Eventos das quests se desenrolam em ordem

## Linha do Tempo das Quests — Warframe — Segunda Mente


| Evento | Quest |
|--------|-------|
| Despertar dos Tenno | [[missoes/jornadas/principais/vors_prize.md\|Vor's Prize]] |
| Revelação do Operator | [[missoes/jornadas/principais/the_second_dream.md\|The Second Dream]] ⭐ |
| Origem dos Warframes | [[missoes/jornadas/principais/the_sacrifice.md\|The Sacrifice]] ⭐ |
| Invasão Sentient | [[missoes/jornadas/principais/the_new_war.md\|The New War]] ⭐ |
| Zariman descoberta | [[missoes/jornadas/principais/angels_of_the_zariman.md\|Angels of the Zariman]] |
| Duviri revelado | [[missoes/jornadas/principais/the_duviri_paradox.md\|The Duviri Paradox]] |
| Laboratórios de Albrecht | [[missoes/jornadas/principais/whispers_in_the_walls.md\|Whispers in the Walls]] |

----------------------------------------

## Seção: lore\cronologia — Warframe — Segunda Mente

### 📄 arquivo: ecos_do_vazio.md

# Ecos do Vazio (e Paradoxo Duviri)

> [!info] O Olhar para o abismo te devolve o Olhar – "Rap. Tap. Tap." As revelações dos últimos confins da história que brincam com o conceito de realidade, ficção e tempo de uma forma apocalíptica.

## O Paradoxo de Duviri — Warframe — Segunda Mente

[O refúgio mental construído a partir de histórias de ficção infantil ganha forma manifesta no Vazio, sustentando a estada paradoxal do Drifter (O Derivante) dentro das cinco oscilações emocionais espirais de um reino despótico governado por Dominus Thrax.]

## Os Arquivos Subterrâneos de Entrati — Warframe — Segunda Mente

[Descobrimento do Sanctum Anatomica cravado nas profundezas de Necralisk. Os Laboratórios gigantes que outrora pertenceram a Albrecht Entrati focados rigorosamente nos experimentos temporais, somáticos e do coração primordial do Cavia para adentrar reinos intocados.]

## Sussurros das Paredes & O Murmúrio — Warframe — Segunda Mente

[A manifestação física da apatia multiversal. Aquela Barganha antiga cobra seu preço. "O Homem na Parede" expõe as criações de areia do Murmúrio que defendem uma realidade incompreensível vazando por fendas espaciotemporais. Entidade sem rosto tentando colapsar a existência em sua imagem indiferente.]

## Warframe: 1999 — Warframe — Segunda Mente

[A viagem de volta ao momento que originou da concepção embrionária de infecção que antecede os próprios Sentients, ou os Warframes: A exploração na cidade murada e sombria de Hollvania no ano-calendário de exatos 1999 no planeta Terra – um evento orquestrado pelo próprio desaparecido Albrecht que busca infectar humanos usando proto-fótons da Mutação Infestada em Arthur, Aoi e Letie...]

----------------------------------------

## Seção: lore\cronologia — Warframe — Segunda Mente

### 📄 arquivo: era_do_despertar.md

# A Era do Despertar

> [!info] A história contemporânea: de onde o jogo efetivamente começa. O despertar dos Tenno nos dias modernos do Sistema Origem.

## O Chamado de Vor — Warframe — Segunda Mente

[O despertar milenar por ordem reativada da Lotus e o embate imediato contra as frotas de Vor, salvando o próprio chassi no momento do Despertar.]

## Um Sistema Fragmentado — Warframe — Segunda Mente

[Mapeamento dos confrontos diretos contra Vay Hek, Sargus Ruk (Grineer) e Alad V e Nef Anyo (Corpus), além dos constantes Surto Infestados recuperando o mapa estelar.]

## O Segundo Sonho — Warframe — Segunda Mente

[A exposição da verdadeira natureza do Operador. A Lua que estava escondida no Vazio sendo trazida de volta pelo Stalker e Erra/Hunhow para o espaço real, quebrando o sonho somático de infância.]

## A Guerra Interior e O Sacrifício — Warframe — Segunda Mente

[O aprendizado sob o manto das Montanhas, as intrigas do Executor Ballas ressurgindo da morte iminente de outrora, e o resgate da memória e origem do próprio Excalibur Umbra para a perseguição à antiga mãe, a Lotus.]

----------------------------------------

## Seção: lore\cronologia — Warframe — Segunda Mente

### 📄 arquivo: era_orokin.md

# A Era Orokin

> [!info] O auge da humanidade no Sistema Origem e o domínio absoluto do Império Esplêndido.

## A Formação do Império — Warframe — Segunda Mente

[Inserir texto sobre o ápice da raça humana governada sob a elite Orokin e suas leis de simetria e poder.]

## A Descoberta do Vazio — Warframe — Segunda Mente

[Inserir detalhes sobre o gênio Albrecht Entrati e a exploração do multiverso e das barreiras dimensionais.]

## O Incidente Zariman Ten Zero — Warframe — Segunda Mente

[Inserir a tragédia da expedição perdida à Tau, os pactos com "O Homem na Parede" e o surgimento das crianças irradiadas pelo Vazio (os Tenno).]

## As Ferramentas do Império — Warframe — Segunda Mente

- **Grineers:** Desenvolvimento da mão de obra escrava clonada.
- **Corpus:** O cartel sectário mercantil que financiava os avanços.
- **Biologia Infestada:** Criação precursora de armas parasíticas como armamentos.

----------------------------------------

## Seção: lore\cronologia — Warframe — Segunda Mente

### 📄 arquivo: o_colapso.md

# O Colapso

> [!info] A grande traição pós-guerra e a queda inevitável de todo um ecossistema estelar.

## O Sangue Dourado Derramado (Os Tambores de Vitória) — Warframe — Segunda Mente

[Momentos após a vitória iminente contra os Sentients, onde os Tenno viraram as costas e as lâminas contra a arrogante e corrupta elite Orokin.]

## A Dispersão Bélica — Warframe — Segunda Mente

- **Revolta Grineer:** Clones antes oprimidos que passaram a dominar territórios pelo Sistema Origem pela força massiva e violência estrutural.
- **A Ganância Corpus:** O ressurgimento do grupo focado no capital comercial para monopolizar a escassa tecnologia pós-Colapso.
- **O Surto Tecnossmótico:** A Infestação fugiu do controle biológico e tomou luas, naves e ecossistemas inteiros.

## O Longo Sono (Estase) — Warframe — Segunda Mente

[A decisão protetiva da Lotus em esconder a Lua dentro do Vazio para afastar o corpo dos Tenno e mergulhá-los em milênios de Sono Criogênico ininterrupto.]

----------------------------------------

## Seção: lore\chefes — Warframe — Segunda Mente

### 📄 arquivo: _Chefes _Indice.md

# Assassinatos (Os Chefes do Sistema)

> [!info] Missões singulares, nodos de planeta que culminam numa batalha elaborada e roteirizada que garantem na maioria recursos preciosos in-game ou espólios únicos de chefão.

## 🟩 Chefões da Tropa Grineer — Warframe — Segunda Mente

- **[[lore/chefes/captain_vor.md|Capitão Vor]]** (Mercúrio, "Tolstoj")
- **[[lore/chefes/vay_hek.md|Conselheiro Vay Hek]]** (Terra, "Oro")
- **[[lore/chefes/lech_kril.md|Tenente Lech Kril]]** (Marte/Ceres)
- **[[lore/chefes/kela_de_thaym.md|Kela De Thaym]]** (Sedna, "Merrow")
- **[[lore/chefes/tyl_regor.md|Tyl Regor]]** (Urano, "Titania")

## 🟦 Consócios Corporativos Corpus — Warframe — Segunda Mente

- **[[lore/chefes/jackal.md|O Chacal]]** (Vênus, "Fossa")
- **[[sargento|O Sargento]]** (Fobos, "Iliad")
- **[[lore/chefes/alad_v.md|Alad V Original e Zanuka]]** (Júpiter, "Themisto")
- **[[lore/chefes/raptors.md|Raptor]]** (Europa, "Naamah")
- **[[lore/chefes/hyena_pack.md|Matilha Hyena]]** (Netuno, "Psamathe")
- **[[lore/chefes/ambulas.md|Ambulas, sob Nef Anyo]]** (Plutão, "Hades")

## 🟥 Aglomerados Infestados — Warframe — Segunda Mente

- **[[lore/chefes/phorid.md|O Phorid]]** (Dinossauro deformado espalhando Surto Infestado aleatoriamente)
- **[[lephantis|Lephantis]]** (Deimos, Magnicídio Derelict)
- **[[lore/chefes/jordas_golem.md|O Golem Jordas]]** (Eris, Chefe em modo Archwing)

----------------------------------------

## Seção: lore\chefes — Warframe — Segunda Mente

### 📄 arquivo: jackal.md

# Jackal

> [!info] Visão Geral
> Quadrúpede robótico Corpus com ataques de laser e stomping. Primeiro chefe significativo.

## Localização — Warframe — Segunda Mente

- Planeta: [[locais/planetas/venus.md|Vênus]]
- Nó: Fossa

## ⚙️ Como Funciona — Warframe — Segunda Mente

1. Destrua as 4 pernas (painéis amarelos)
2. Com pernas destruídas, ataque o corpo exposto
3. Painéis amarelos nas pernas — foco de dano

## 🎁 Recompensas — Warframe — Segunda Mente

- Rhino Neuroptics, Chassis, Systems (rotação)

## 💡 Dicas — Warframe — Segunda Mente

- Fique em movimento constante para evitar o laser de rastreamento
- [[warframes/regular/rhino.md|Rhino]] é obtido aqui

## 🔗 Relacionados — Warframe — Segunda Mente

- Local: [[locais/planetas/venus.md|Vênus]]
- Recompensa: [[warframes/regular/rhino.md|Rhino]]

----------------------------------------

## Seção: lore\chefes — Warframe — Segunda Mente

### 📄 arquivo: lech_kril.md

# Lech Kril

> [!info] Visão Geral
> Comandante Grineer congelante com martelo e sistema de resfriamento nas costas.

## Localização — Warframe — Segunda Mente

- Planeta: [[locais/planetas/ceres.md|Ceres]]
- Nó: Exta (também em Marte - War com Vor)

## ⚙️ Como Funciona — Warframe — Segunda Mente

1. Ataque o tubo de resfriamento nas costas para deixá-lo vulnerável
2. Com tubo destruído, ataque o corpo aquecido
3. Tubo de resfriamento nas costas — use Heat para superar o congelamento

## 🎁 Recompensas — Warframe — Segunda Mente

- Ember/Frost partes em Ceres; Excalibur partes com Vor em Marte

## 💡 Dicas — Warframe — Segunda Mente

- Fique atrás dele para atacar o tubo
- Dano de Heat é mais eficaz quando vulnerável

## 🔗 Relacionados — Warframe — Segunda Mente

- Local: [[locais/planetas/ceres.md|Ceres]]
- Recompensa: [[warframes/regular/ember.md|Ember]] · [[warframes/regular/frost.md|Frost]] · [[warframes/regular/excalibur.md|Excalibur]]

----------------------------------------

## Seção: lore\chefes — Warframe — Segunda Mente

### 📄 arquivo: profit_taker.md

# Profit-Taker Orb

> [!info] Visão Geral
> Aranha Corpus colossal em Orb Vallis. Uma das fontes principais de Arcanes endgame.

## Localização — Warframe — Segunda Mente

- Planeta: [[locais/open-worlds/fortuna.md|Fortuna / Orb Vallis]]
- Nó: Phase 4 da Heist de Fortuna

## ⚙️ Como Funciona — Warframe — Segunda Mente

1. Destrua os escudos com tipos de dano que aparecem nas pernas
2. Ataque o núcleo exposto com dano Archgun
3. Os tipos de dano para os escudos rotacionam aleatoriamente — precisa de variedade de elementos

## 🎁 Recompensas — Warframe — Segunda Mente

- Arcane Energize, Guardian, Avenger e outros arcanes raros

## 💡 Dicas — Warframe — Segunda Mente

- Leve múltiplos tipos de dano elemental ou use Operator para Void damage
- Principal fonte de Arcanes endgame — vale repetir

## 🔗 Relacionados — Warframe — Segunda Mente

- Local: [[locais/open-worlds/fortuna.md|Fortuna]]
- Recompensa: [[sistemas/arcanes|Arcanes]]

----------------------------------------

## Seção: lore\chefes — Warframe — Segunda Mente

### 📄 arquivo: ropalolyst.md

# Ropalolyst

> [!info] Visão Geral
> Chefe Sentient que paira no ar e usa ataques de energia. Requer The Sacrifice para acessar.

## Localização — Warframe — Segunda Mente

- Planeta: [[locais/planetas/jupiter.md|Júpiter]]
- Nó: Wisp boss node (desbloqueado após The Sacrifice)

## ⚙️ Como Funciona — Warframe — Segunda Mente

1. Conduza o Ropalolyst por cabos elétricos para danificá-lo
2. Escale para cima e ataque diretamente o ponto fraco
3. Deve ser conduzido por relâmpagos específicos no mapa

## 🎁 Recompensas — Warframe — Segunda Mente

- Wisp Blueprint (único — não são partes, é o blueprint completo)

## 💡 Dicas — Warframe — Segunda Mente

- Aprenda o layout da arena antes de lutar
- [[warframes/regular/wisp.md|Wisp]] blueprint completo — raro, pois não são partes separadas

## 🔗 Relacionados — Warframe — Segunda Mente

- Local: [[locais/planetas/jupiter.md|Júpiter]]
- Recompensa: [[warframes/regular/wisp.md|Wisp]]

----------------------------------------

## Seção: lore\chefes — Warframe — Segunda Mente

### 📄 arquivo: alad_v.md

# Alad V

> [!info] Visão Geral
> CEO Corpus obsessivo que usa um Warframe Zanuka como guarda-costas.

## Localização — Warframe — Segunda Mente

- Planeta: [[locais/planetas/jupiter.md|Júpiter]]
- Nó: Themisto

## ⚙️ Como Funciona — Warframe — Segunda Mente

1. Destrua o Zanuka guardião primeiro
2. Ataque Alad V diretamente
3. Alad V tem escudo baixo — dano Magnetic ou Toxin eficaz

## 🎁 Recompensas — Warframe — Segunda Mente

- Mesa Neuroptics, Chassis, Systems

## 💡 Dicas — Warframe — Segunda Mente

- Destrua o Zanuka rapidamente para focar em Alad V
- [[warframes/regular/mesa.md|Mesa]] é obtida aqui

## 🔗 Relacionados — Warframe — Segunda Mente

- Local: [[locais/planetas/jupiter.md|Júpiter]]
- Recompensa: [[warframes/regular/mesa.md|Mesa]]

----------------------------------------

## Seção: lore\chefes — Warframe — Segunda Mente

### 📄 arquivo: ambulas.md

# Ambulas

> [!info] Visão Geral
> Corpus Moa gigante aprimorado com habilidades de cura e dano de área massivo.

## Localização — Warframe — Segunda Mente

- Planeta: [[locais/planetas/plutao.md|Plutão]]
- Nó: Hades

## ⚙️ Como Funciona — Warframe — Segunda Mente

1. Damage Ambulas até ele chamar Condors (naves de resgate)
2. Destrua as naves de resgate para impedir a cura
3. Condors de resgate devem ser destruídas para evitar que cure Ambulas

## 🎁 Recompensas — Warframe — Segunda Mente

- Ash Neuroptics, Chassis, Systems

## 💡 Dicas — Warframe — Segunda Mente

- Foque nas Condors assim que aparecerem
- [[warframes/regular/ash.md|Ash]] é obtido aqui

## 🔗 Relacionados — Warframe — Segunda Mente

- Local: [[locais/planetas/plutao.md|Plutão]]
- Recompensa: [[warframes/regular/ash.md|Ash]]

----------------------------------------

## Seção: lore\chefes — Warframe — Segunda Mente

### 📄 arquivo: kela_de_thaym.md

# Kela de Thaym

> [!info] Visão Geral
> Gladiadora Grineer que luta em arena com plateias e mecânicas de espetáculo.

## Localização — Warframe — Segunda Mente

- Planeta: [[locais/planetas/sedna.md|Sedna]]
- Nó: Merrow

## ⚙️ Como Funciona — Warframe — Segunda Mente

1. Destrua os drones de transmissão na arena
2. Ataque Kela quando os escudos caírem
3. Precisa desativar transmissores antes de causar dano a ela

## 🎁 Recompensas — Warframe — Segunda Mente

- Saryn Neuroptics, Chassis, Systems

## 💡 Dicas — Warframe — Segunda Mente

- Priorize os transmissores antes de focar nela
- [[warframes/regular/saryn.md|Saryn]] é obtida aqui

## 🔗 Relacionados — Warframe — Segunda Mente

- Local: [[locais/planetas/sedna.md|Sedna]]
- Recompensa: [[warframes/regular/saryn.md|Saryn]]

----------------------------------------

## Seção: lore\chefes — Warframe — Segunda Mente

### 📄 arquivo: raptors.md

# Raptors

> [!info] Visão Geral
> Três drones voadores Corpus que atacam em ondas sucessivas.

## Localização — Warframe — Segunda Mente

- Planeta: [[locais/planetas/europa.md|Europa]]
- Nó: Naamah

## ⚙️ Como Funciona — Warframe — Segunda Mente

1. Destrua o primeiro Raptor
2. Dois Raptors aparecem simultaneamente
3. Escudos Corpus — Magnetic ou Toxin eficaz

## 🎁 Recompensas — Warframe — Segunda Mente

- Nova Neuroptics, Chassis, Systems

## 💡 Dicas — Warframe — Segunda Mente

- Use armas de alto DPS para eliminar cada um rapidamente
- [[warframes/regular/nova.md|Nova]] é obtida aqui

## 🔗 Relacionados — Warframe — Segunda Mente

- Local: [[locais/planetas/europa.md|Europa]]
- Recompensa: [[warframes/regular/nova.md|Nova]]

----------------------------------------

## Seção: mecanicas — Warframe — Segunda Mente

### 📄 arquivo: _Mecanicas _Indice.md

> [!quote]
> *"Warframe não é um jogo que você aprende em horas. É um jogo que você aprende em anos."*


## O que são Mecânicas? — Warframe — Segunda Mente


Mecânicas são os sistemas transversais do Warframe — camadas de jogo que se aplicam a todo o conteúdo independentemente de planeta, missão ou Warframe escolhido. Enquanto recursos pertencem a planetas e mods pertencem a equipamentos, as mecânicas definem as regras fundamentais de como o jogo funciona: como o dano é calculado, como a progressão vertical se aprofunda, como a economia gira e como os sistemas sociais operam.

Compreender as mecânicas é o que separa um jogador intermediário de um veterano. Um Warframe com o mod certo no slot errado, uma build que ignora o sistema de combinações elementais, ou uma gestão ineficiente de standing e trading podem transformar centenas de horas de farm em progresso desperdiçado. Cada mecânica documentada aqui é independente — pode ser consultada isoladamente — mas todas interagem entre si em construções de alto nível.

Mecânicas específicas de Open Worlds, Railjack, Archwing ou conteúdo end-game localizado estão documentadas dentro dos arquivos de seus respectivos contextos, evitando duplicação. Este índice cobre apenas os sistemas verdadeiramente transversais.


## ⚔️ Combate — Warframe — Segunda Mente


Sistemas que definem como o dano é calculado, aplicado e amplificado em qualquer situação de combate.

| Mecânica | Descrição |
|---|---|
| [[mecanicas/dano_e_status.md\|Dano e Status]] | Tipos de dano físico e elemental, combinações, procs e interações com facções |
| [[mecanicas/critico.md\|Crítico]] | Yellow crit, Orange crit, Red crit — como chance e multiplicador se relacionam |
| [[mecanicas/combo_counter.md\|Combo Counter]] | Acumulação de combo em armas brancas e como escala mods como Blood Rush |
| [[mecanicas/parkour.md\|Parkour]] | Bullet jump, wall latch, aim glide, double jump — o sistema de mobilidade |
| [[mecanicas/stealth_e_finishers.md\|Stealth e Finishers]] | Multiplicadores de dano furtivo, finishers e interações com frames de invisibilidade |
| [[mecanicas/augments.md\|Augments]] | Mods de habilidade exclusivos por Warframe — alteram ou expandem habilidades específicas |


## Forja e Crafting — Warframe — Segunda Mente


| Mecânica | Descrição |
|---|---|
| [[mecanicas/forja.md\|Forja]] | Sistema de crafting — blueprints, timers, slots, rush com Platinum e gestão de produção |


## Progressão — Warframe — Segunda Mente


Sistemas que controlam o avanço vertical do jogador — poder, flexibilidade e desbloqueios permanentes.

| Mecânica | Descrição |
|---|---|
| [[mecanicas/mastery_rank.md\|Mastery Rank]] | Como o MR funciona, testes por rank, benefícios e itens bloqueados por nível |
| [[mecanicas/forma_e_polaridades.md\|Forma e Polaridades]] | Polarização de slots, reset de rank, como planejar builds a longo prazo |
| [[mecanicas/operator_e_focus.md\|Operator e Focus]] | As cinco escolas de Focus, Void Mode, Amps e progressão do Operator |
| [[mecanicas/helminth.md\|Helminth]] | Subsumar habilidades entre Warframes — custo, restrições e sinergias |
| [[mecanicas/incarnon.md\|Incarnon]] | Adapters Incarnon — como ativar, evoluir e quais armas suportam |
| [[mecanicas/steel_path.md\|Steel Path]] | Modo de dificuldade +100 nível — desbloqueios, recompensas e Steel Essence |
| [[mecanicas/arbitrations.md\|Arbitrations]] | Missões sem revive com drones de escudo — recompensas e como funciona a rotação |
| [[mecanicas/nightwave.md\|Nightwave]] | Passe de temporada — desafios semanais, créditos e recompensas exclusivas |


## Economia e Social — Warframe — Segunda Mente


Sistemas que governam a circulação de recursos, moedas e interações entre jogadores.

| Mecânica | Descrição |
|---|---|
| [[mecanicas/platinum.md\|Platinum]] | A moeda premium — como obter sem pagar, conversão e o que vale comprar |
| [[mecanicas/trading.md\|Trading]] | Sistema de trocas — limites por MR, Trade Tax, itens negociáveis e Trade Chat |
| [[mecanicas/baro_ki_teer.md\|Baro Ki'Teer]] | O Void Trader — rotação quinzenal, histórico, Ducats e como se preparar |
| [[mecanicas/cla_e_dojo.md\|Clã e Dojo]] | Criação e gestão de clã, pesquisa de Dojo, salas e decoração |
| [[mecanicas/sindicatos/_Sindicatos _Indice.md\|Sindicatos]] | Os seis sindicatos principais + Open Worlds — reputação, recompensas e alianças |


## Eventos — Warframe — Segunda Mente


Conteúdo de tempo limitado que retorna periodicamente com mecânicas próprias e recompensas exclusivas.

| Evento | Tipo | Recompensa Principal |
|---|---|---|
| [[mecanicas/eventos/plague_star.md\|Plague Star]] | Operação sazonal — Eidolon | Helminth Charger, mods exclusivos |
| [[mecanicas/eventos/thermia_fractures.md\|Thermia Fractures]] | Operação sazonal — Orbe Vallis | Diluted Thermia, Opticor Vandal |
| [[mecanicas/eventos/razorback_armada.md\|Razorback Armada]] | Alerta de invasão Corpus | Brakk receiver, créditos |
| [[mecanicas/eventos/balor_fomorian.md\|Balor Fomorian]] | Alerta de invasão Grineer | Imperator Vandal, créditos |
| [[mecanicas/eventos/nights_of_naberus.md\|Nights of Naberus]] | Evento de Halloween | Cosméticos exclusivos da temporada |
| [[mecanicas/eventos/anniversary.md\|Anniversary]] | Aniversário do jogo — março | Itens comemorativas, Dex weapons |
| [[mecanicas/eventos/tennobaum.md\|Tennobaum]] | Evento de fim de ano | Cosméticos, bênçãos de comunidade |


## 💡 Curiosidades — Warframe — Segunda Mente


- O sistema de dano do Warframe passou por uma reformulação completa em 2013 (Damage 2.0) que introduziu os tipos elementais combinados — antes existiam apenas danos físicos básicos.
- O Focus System foi adicionado em 2015 com The Second Dream e ficou praticamente sem atualização por anos antes de ser reformulado em 2021 com o sistema de Operator mais profundo.
- Helminth foi controverso no lançamento em 2020 — a comunidade ficou dividida sobre subsumar habilidades de Warframes que outros jogadores precisariam farmar para obter, e a DE restringiu quais habilidades podiam ser transferidas.
- O MR30 era considerado o teto absoluto do jogo por anos — a DE adicionou MR 31 a 40 em 2023 com os testes de Exemplar, dando aos veteranos uma meta de progressão de longo prazo inédita.
- Baro Ki'Teer visita o jogo desde 2014 — veteranos rastreiam o histórico completo de suas visitas em planilhas da comunidade para prever quais mods Primed voltarão.
- O sistema de Trading existe desde 2014 mas o Trade Chat é infame pelo volume de spam — ferramentas externas como warframe.market foram criadas pela comunidade para tornar o processo suportável.
- Nightwave substituiu o sistema de Alerts em 2019 — a mudança foi controversa porque Alerts permitiam farm direto de itens raros em momentos específicos, enquanto Nightwave distribui as recompensas ao longo de semanas.
- Steel Path foi adicionado em 2020 após anos de pedidos da comunidade por conteúdo mais difícil — a ironia é que a maioria dos veteranos o considera fácil com builds otimizadas, mas permanece útil como fonte de Steel Essence.

----------------------------------------

## Seção: mecanicas\sindicatos — Warframe — Segunda Mente

### 📄 arquivo: _Sindicatos _Indice.md

> [!quote]
> *"Todo sindicato quer algo de você. A questão é se o que oferecem vale o preço."*


## O que são Sindicatos? — Warframe — Segunda Mente


Sindicatos são facções aliadas com as quais o Tenno pode construir reputação ao longo do jogo. Cada sindicato tem uma filosofia, um conjunto de recompensas exclusivas e um limite diário de standing que pode ser ganho. A reputação é acumulada completando missões com o emblema do sindicato equipado no ombro — cada missão contribui com standing proporcional à quantidade de Afinidade gerada durante a run.

Os sindicatos principais são seis facções ideológicas que disputam influência no Sistema Origem. Eles formam duas coalizões opostas: aliados no mesmo grupo concedem acesso aos mods uns dos outros a custo maior, enquanto sindicatos rivais perdem reputação quando você ganha com o oposto. Escolher bem com quais se alinhar no início do jogo evita retrabalho de reputação mais tarde.

Além dos seis principais, existem sindicatos de Open World vinculados a cada região do mapa — Ostron nas Planícies, Solaris United na Vallis, Entrati em Deimos, The Holdfasts no Zariman, Kaithe no Duviri e Cavia no Sanctum Anatomica. Esses sindicatos funcionam de forma independente — a reputação é ganha por atividades dentro da própria área — e desbloqueiam acesso a Warframes, armas e equipamentos exclusivos de cada mundo.


## Como Funciona a Reputação — Warframe — Segunda Mente


| Aspecto | Detalhe |
|---|---|
| **Limite diário** | Calculado como 1.000 × MR do jogador — aumenta a cada rank ganho |
| **Como ganhar** | Missões com emblema do sindicato equipado no slot de ombro |
| **Fonte** | Afinidade gerada na missão é convertida em standing proporcional |
| **Ranks** | Cada sindicato tem 5 ranks (Iniciado → Campeão) com recompensas por promoção |
| **Custo de promoção** | Cada rank exige entregar itens específicos (recursos, componentes) além do standing |
| **Rivais** | Ganhar standing com um sindicato rival reduz o standing de sindicatos opostos |
| **Sindicatos OW** | Têm seu próprio limite diário e sistema de ranks — independente dos seis principais |


## Alianças e Rivalidades — Warframe — Segunda Mente


Os seis sindicatos se organizam em duas coalizões. Dentro de cada coalizão os sindicatos são aliados — acesso cruzado a mods com custo adicional. Entre coalizões opostas são neutros ou rivais.

| Coalizão A | Coalizão B |
|---|---|
| Steel Meridian | Red Veil |
| Arbiters of Hexis | Cephalon Suda |
| New Loka | Perrin Sequence |

> [!info] **Alianças**
> Steel Meridian ↔ Red Veil (aliados) · Arbiters ↔ Cephalon Suda (aliados) · New Loka ↔ Perrin Sequence (aliados)
>
> **Rivalidades**
> Steel Meridian ✕ Perrin Sequence · New Loka ✕ Cephalon Suda · Arbiters of Hexis ✕ Red Veil


## Sindicatos Principais — Warframe — Segunda Mente


| Sindicato | Filosofia | Mods Exclusivos Destaque | Warframe Associado |
|---|---|---|---|
| [[mecanicas/sindicatos/steel_meridian.md\|Steel Meridian]] | Proteção dos colonos Grineer dissidentes | Hunter Munitions, Hunter Adrenaline, Empowered Blades | — |
| [[mecanicas/sindicatos/arbiters_of_hexis.md\|Arbiters of Hexis]] | Transcendência e maestria do Tenno | Master's Edge, Winds of Purity, Justice Blades | — |
| [[mecanicas/sindicatos/cephalon_suda.md\|Cephalon Suda]] | Preservação do conhecimento e evolução | Growing Power, Entropy Burst, Lethal Torrent | — |
| [[mecanicas/sindicatos/new_loka.md\|New Loka]] | Pureza da humanidade original | Growing Power, Frostbite, Smite Infusion | — |
| [[mecanicas/sindicatos/red_veil.md\|Red Veil]] | Purificação através da destruição | Thermite Rounds, Scorch, Firewalk | — |
| [[mecanicas/sindicatos/perrin_sequence.md\|Perrin Sequence]] | Controle econômico e prosperidade Corpus | High Voltage, mods de pistola | — |


## Sindicatos de Open World — Warframe — Segunda Mente


| Sindicato | Região | Como Ganhar Standing | Warframe Exclusivo |
|---|---|---|---|
| [[mecanicas/sindicatos/ostron.md\|Ostron]] | Planícies de Eidolon (Cetus) | Bounties, vender partes de peixe e minerais | Gara |
| [[mecanicas/sindicatos/solaris_united.md\|Solaris United]] | Orbe Vallis (Fortuna) | Bounties, vender peixes e minerais da Vallis | Baruuk |
| [[mecanicas/sindicatos/entrati.md\|Entrati]] | Câmbion Drift (Necralisk) | Bounties, oferendas de recursos Infestados | Xaku, Lavos |
| [[mecanicas/sindicatos/the_holdfasts.md\|The Holdfasts]] | Zariman Ten Zero | Missões Zariman, vender Voidplumes | Gyre |
| [[mecanicas/sindicatos/kaithe.md\|Kaithe]] | Duviri (Drifter's Camp) | Testemunhos, exploração e bosses do Duviri | Kullervo |
| [[mecanicas/sindicatos/cavia.md\|Cavia]] | Sanctum Anatomica (Deimos) | Missões Sanctum, oferendas de Tagfer e Vome | Qorvex, Dante |


## Outros Sindicatos — Warframe — Segunda Mente


| Sindicato | Contexto | Como Acessar |
|---|---|---|
| **[[mecanicas/nightwave.md\|Nightwave (Nora Night)]]** | Passe de temporada rotativo | Automático — desafios semanais e diários | 
| **[[mecanicas/sindicatos/the_quills.md\|The Quills]]** | Progressão do Operator — Amp e Focus | Planícies de Eidolon, pós-The Second Dream |
| **[[mecanicas/sindicatos/vox_solaris.md\|Vox Solaris]]** | Progressão de Amp avançada e Orb Mothers | Fortuna, pós-rank com Solaris United |
| **[[mecanicas/sindicatos/necraloid.md\|Necraloid]]** | Pesquisa e progressão de Necramech | Necralisk (Deimos) |
| **[[mecanicas/sindicatos/operational_supply.md\|Operational Supply (Tenshin)]]** | Missões Kahl — pós-Veilbreaker | Albrecht's Laboratories |
| **[[mecanicas/sindicatos/cephalon_simaris.md\|Cephalon Simaris]]** | Sanctuary Onslaught e scanner | Relay — disponível desde o início |
| **[[mecanicas/sindicatos/conclave.md\|Conclave (Teshin)]]** | PvP entre Tennos | Relay — acesso livre |


## 💡 Curiosidades — Warframe — Segunda Mente


- O sistema de sindicatos foi adicionado em 2014 e inicialmente causou divisão — jogadores temiam que se alinhar com um sindicato bloqueasse conteúdo permanentemente. A DE depois tornou mais fácil mudar de aliança.
- Red Veil e Steel Meridian são aliados apesar de filosofias opostas — ambos focam em ação direta, o que os une pragmaticamente contra inimigos comuns.
- New Loka é frequentemente citada como o sindicato com a narrativa mais sombria — a "pureza da humanidade" que pregam carrega conotações que a comunidade debateu extensamente.
- Cephalon Suda é tecnicamente uma inteligência artificial, o que torna sua presença como líder de sindicato humanizado uma curiosidade narrativa do universo.
- O limite diário de standing vinculado ao MR foi uma decisão deliberada da DE para incentivar a progressão de Mastery — jogadores de MR baixo que farmariam sindicatos compulsivamente eram redirecionados para diversificar o equipamento primeiro.
- Vox Solaris é o sindicato mais difícil de rankear dos Open Worlds — requer standing máximo com Solaris United como pré-requisito antes mesmo de começar.
- The Quills permaneceu misterioso por muito tempo na narrativa — seu líder Onkko é revelado como o operador de Teshin em uma linha do tempo alternativa, detalhe que poucos jogadores percebem sem ler o lore.

----------------------------------------

## Seção: missoes — Warframe — Segunda Mente

### 📄 arquivo: _Missoes _Indice.md

> [!quote]
> *"Cada missão é um contrato. Cada contrato, uma oportunidade de crescer."*


## O que são Missões? — Warframe — Segunda Mente


Missões são a unidade fundamental de jogo no Warframe. Cada nó do mapa estelar representa uma missão com tipo, facção e nível de inimigos definidos. O jogador entra sozinho ou em squad de até 4 Tennos, completa o objetivo e extrai — colhendo recursos, experiência de Afinidade e recompensas de rotação. A progressão no jogo é estruturada em torno de desbloquear novos nós, derrotar bosses de planeta e completar Junctions para avançar ao próximo sistema.

O tipo da missão determina o estilo de jogo: algumas pedem rapidez e furtividade, outras resistência prolongada. A escolha do tipo influencia diretamente o que pode ser farmado — recursos, mods, partes Prime e XP acumulam de formas distintas dependendo do objetivo em campo. Missões de sobrevivência e defesa são as mais populares para farm por volume, enquanto missões de espionagem e captura são preferidas quando o objetivo é velocidade e eficiência de rotação.

Além das missões do mapa estelar, o jogo oferece camadas adicionais de conteúdo: Jornadas (quests) que avançam a narrativa, Junctions que conectam planetas, e Bounties nos Open Worlds que funcionam como missões em cadeia dentro de um mapa aberto. Cada camada tem ritmo, recompensas e contexto narrativo próprios.


## Tipos de Missão — Warframe — Segunda Mente


O jogo conta com mais de 20 tipos distintos de missão, organizados entre missões convencionais do mapa estelar, modos especiais de alto risco e missões exclusivas de sistemas avançados como Railjack e Archwing.

### Missões Convencionais

| Tipo | Objetivo | Recomendado Para | Disponível Em |
|---|---|---|---|
| [[missoes/tipos/exterminate.md\|Exterminate]] | Matar todos os inimigos ou atingir a cota de eliminações | Farm rápido de recursos, XP inicial | Todos os planetas |
| [[missoes/tipos/capture.md\|Capture]] | Capturar o alvo vivo e extrair | Rotação veloz, loot de captura | Todos os planetas |
| [[missoes/tipos/rescue.md\|Rescue]] | Resgatar prisioneiro e extrair sem matá-lo | Farm de mods, rotação rápida | Todos os planetas |
| [[missoes/tipos/sabotage.md\|Sabotage]] | Destruir reator ou objetivo central do mapa | Farm de recursos específicos do planeta | Todos os planetas |
| [[missoes/tipos/mobile_defense.md\|Mobile Defense]] | Defender três terminais sequencialmente | Farm de mods e recursos | Todos os planetas |
| [[missoes/tipos/defense.md\|Defense]] | Sobreviver 5/10/20+ ondas protegendo um ponto | Farm de mods, partes Prime, XP em squad | Todos os planetas |
| [[missoes/tipos/survival.md\|Survival]] | Sobreviver mantendo suprimento de Oxigênio ativo | Farm de volume — recursos, mods, XP | Todos os planetas |
| [[missoes/tipos/excavation.md\|Excavation]] | Ativar e proteger escavadoras para coletar Cryotic | Farm de Cryotic e recompensas de rotação | Todos os planetas |
| [[missoes/tipos/spy.md\|Spy]] | Hackear 3 cofres de dados sem acionar alarmes | Farm de Vaultrun — Warframe blueprints, mods raros | Todos os planetas |
| [[missoes/tipos/assassination.md\|Assassination]] | Derrotar o boss do planeta | Farm de partes de Warframe e mods de boss | Um nó por planeta |
| [[missoes/tipos/interception.md\|Interception]] | Capturar e manter 4 torres de sinal | Farm de recompensas de rotação, XP | Todos os planetas |
| [[missoes/tipos/hijack.md\|Hijack]] | Conduzir veículo blindado até a zona de extração | Desafio tático — dano ao veículo drena HP | Planetas específicos |
| [[missoes/tipos/defection.md\|Defection]] | Escolta de colonos Grineer em fuga por checkpoints | Farm de mod Harrow Neuroptics | Eris |
| [[missoes/tipos/infested_salvage.md\|Infested Salvage]] | Manter suprimentos de antídoto contra névoa infestada | Farm de blueprint do Nidus | Eris |
| [[missoes/tipos/disruption.md\|Disruption]] | Inserir chaves em consoles e protegê-los de Demolysts | Farm de partes de Warframe, mods Acolyte | Júpiter e outros |
| [[missoes/tipos/assault.md\|Assault]] | Missão longa de múltiplos objetivos em sequência | Recompensas únicas — sem opção de farm em loop | Missões especiais |
| [[missoes/tipos/rush.md\|Rush]] | Chegar ao ponto de extração no menor tempo possível | Não usado para farm — missão de habilidade | Competitivo |
| [[missoes/tipos/pursuit.md\|Pursuit]] | Destruir nave Grineer Balor Fomorian em campo Archwing | Eventos sazonais, recompensas únicas | Archwing |

### Missões de Alto Risco e Conteúdo Especial

| Tipo | Descrição | Requisito | Recompensa Principal |
|---|---|---|---|
| [[missoes/tipos/sortie.md\|Sortie]] | 3 missões encadeadas com modificadores de dificuldade | Conclusão de The War Within | Riven Mod, Anasa Sculpture, mods raros |
| [[missoes/tipos/archon_hunt.md\|Archon Hunt]] | 3 missões com boss Archon semanal — dificuldade extrema | Conclusão de The New War | Archon Shards, mods Archon |
| [[missoes/tipos/arbitration.md\|Arbitration]] | Survival/Defense sem revive — inimigos com escudos de drone | MR10+ e todos os nós do mapa estelar desbloqueados | Mods de Arbitration, Ayatan, Endo |
| [[missoes/tipos/nightmare.md\|Nightmare]] | Missão com dois modificadores negativos simultâneos | Desbloquear o nó normal equivalente | Mods Nightmare exclusivos |
| [[missoes/tipos/void_fissure.md\|Void Fissure]] | Missão com Void Fissures — abre Relic para obter partes Prime | Ter uma Void Relic | Partes Prime e refinamento de Relics |
| [[missoes/tipos/steel_path.md\|Steel Path]] | Versão com inimigos nível +100 de todo o mapa estelar | Completar 100% do mapa estelar no modo normal | Arcanes, mods Steel Path, Steel Essence |
| [[missoes/tipos/sanctuary_onslaught.md\|Sanctuary Onslaught]] | Ondas infinitas em zonas do Cephalon Simaris — XP extremo | Acesso ao Simulacrum (MR8) | Mods de Onslaught, Khora chassis |
| [[missoes/tipos/elite_sanctuary_onslaught.md\|Elite Sanctuary Onslaught]] | Versão elite do Onslaught — inimigos muito mais fortes | Completar Sanctuary Onslaught | Khora sistema/neuroptics, mods Elite |
| [[missoes/tipos/void_cascade.md\|Void Cascade]] | Missão Zariman — purificar Exolizers antes de explodirem | Conclusão de Angels of the Zariman | Standing Holdfasts, mods Zariman |
| [[missoes/tipos/void_flood.md\|Void Flood]] | Missão Zariman — coletar Vitoplast antes do timer esgotar | Conclusão de Angels of the Zariman | Standing Holdfasts, mods Zariman |
| [[missoes/tipos/void_armageddon.md\|Void Armageddon]] | Defense no Zariman com mecânicas de Void | Conclusão de Angels of the Zariman | Standing Holdfasts |

### Missões Railjack (Proximas)

| Tipo | Objetivo | Proxima Disponível |
|---|---|---|
| [[missoes/tipos/skirmish.md\|Skirmish]] | Destruir esquadrões e cruzadores inimigos no espaço | Earth, Venus, Saturn, Neptune, Veil |
| [[missoes/tipos/volatile.md\|Volatile]] | Invadir cruzador, destruir motor e extrair antes da explosão | Saturn, Neptune, Veil |
| [[missoes/tipos/survival_railjack.md\|Survival (RJ)]] | Manter suporte de vida no espaço contra ondas inimigas | Saturn, Neptune |
| [[missoes/tipos/defense_railjack.md\|Defense (RJ)]] | Defender ponto estratégico contra vagas no espaço | Neptune, Veil |
| [[missoes/tipos/sabotage_railjack.md\|Sabotage (RJ)]] | Destruir estrutura estratégica inimiga no campo de asteroides | Earth, Venus |
| [[missoes/tipos/assassination_railjack.md\|Assassination (RJ)]] | Derrotar boss de Proxima — Lich, Sister, Corpus flagship | Todas as Proximas |


## Jornadas (Quests) — Warframe — Segunda Mente


Jornadas são as quests narrativas do Warframe — missões lineares com cutscenes, diálogos e revelações de lore que expandem a história do universo. Algumas desbloqueiam sistemas de jogo inteiros (como o Operator após The Second Dream), outras entregam Warframes, companheiros ou armas exclusivas. As jornadas de Warframe são quests curtas que fazem parte do loop de obtenção de um frame específico e podem ser iniciadas a qualquer momento sem dependência narrativa forte. A ordem de conclusão das quests principais importa: várias têm pré-requisitos rígidos e o jogo bloqueia o acesso sem eles.

### Jornadas Principais

| Jornada | Lançamento | Período Narrativo | Duração Est. | Pré-Requisito | Recompensa Principal |
|---|---|---|---|---|---|
| [[missoes/jornadas/principais/vors_prize.md\|Vor's Prize]] | Mar 2013 | Despertar do Tenno | ~20 min | — | Tutorial completo, Excalibur/Mag/Volt |
| [[missoes/jornadas/principais/once_awake.md\|Once Awake]] | 2013 | Pós-despertar | ~15 min | Vor's Prize | Acesso ao mercado |
| [[missoes/jornadas/principais/the_archwing.md\|The Archwing]] | Out 2014 | Expansão ao espaço | ~30 min | MR2, Vor's Prize | Blueprint do Archwing + Elytron |
| [[missoes/jornadas/principais/natah.md\|Natah]] | Jul 2015 | Revelação sobre a Lotus | ~1h | Acesso à Lua (Junction) | Acesso ao próximo capítulo |
| [[missoes/jornadas/principais/the_second_dream.md\|The Second Dream]] | Dez 2015 | Verdade sobre o Tenno | ~2h | Natah completa | Operator desbloqueado |
| [[missoes/jornadas/principais/the_war_within.md\|The War Within]] | Nov 2016 | Aprofundamento do Operator | ~3h | The Second Dream, MR5 | Poderes do Operator, Focus escolar |
| [[missoes/jornadas/principais/apostasy_prologue.md\|Apostasy Prologue]] | Out 2017 | Ponte narrativa — Lotus | ~10 min | The War Within | Lore, acesso ao próximo capítulo |
| [[missoes/jornadas/principais/chains_of_harrow.md\|Chains of Harrow]] | Jun 2017 | Horror e redenção | ~1h30 | The War Within, Sedna Junction | Blueprint do Harrow |
| [[missoes/jornadas/principais/octavias_anthem.md\|Octavia's Anthem]] | Mar 2017 | Música e Cephalon | ~1h | The War Within | Blueprint da Octavia |
| [[missoes/jornadas/principais/the_sacrifice.md\|The Sacrifice]] | Jun 2018 | Origem dos Warframes | ~2h | The War Within | Blueprint do Excalibur Umbra, Parazon |
| [[missoes/jornadas/principais/chimera_prologue.md\|Chimera Prologue]] | Out 2018 | Pós-Sacrifice | ~15 min | The Sacrifice | Lore Sentient |
| [[missoes/jornadas/principais/erra.md\|Erra]] | Dez 2019 | Invasão Sentient | ~20 min | Chimera Prologue | Lore, preparação para New War |
| [[missoes/jornadas/principais/rising_tide.md\|Rising Tide]] | Dez 2019 | Construção da nave | ~1h | MR8 | Dry Dock desbloqueado, acesso ao Railjack |
| [[missoes/jornadas/principais/the_deadlock_protocol.md\|The Deadlock Protocol]] | Jun 2020 | Herança Corpus | ~1h | MR8 | Blueprint do Protea |
| [[missoes/jornadas/principais/heart_of_deimos.md\|Heart of Deimos]] | Ago 2020 | Entrati e Infested | ~1h | The War Within | Acesso ao Câmbion Drift |
| [[missoes/jornadas/principais/the_waverider.md\|The Waverider]] | Dez 2020 | Corpus jovem e K-Drive | ~45 min | Heart of Deimos | Blueprint do Yareli |
| [[missoes/jornadas/principais/prelude_to_war.md\|Prelude to War]] | 2021 | Ponte pré-New War | ~15 min | Erra | Lore, acesso à New War |
| [[missoes/jornadas/principais/the_new_war.md\|The New War]] | Dez 2021 | Guerra total contra Sentient | ~4-5h | Erra, Heart of Deimos, MR5 | Caliban, poderes Operator expandidos |
| [[missoes/jornadas/principais/angels_of_the_zariman.md\|Angels of the Zariman]] | Abr 2022 | Tragédia da nave Zariman | ~1h30 | The New War | Acesso ao Zariman, Gyre |
| [[missoes/jornadas/principais/veilbreaker.md\|Veilbreaker]] | Set 2022 | Kahl-175 e libertação Grineer | ~1h | The New War | Styanax, acesso às missões Kahl |
| [[missoes/jornadas/principais/the_duviri_paradox.md\|The Duviri Paradox]] | Abr 2023 | Drifter e o reino caótico | ~2h | The New War | Acesso ao Duviri, Drifter jogável |
| [[missoes/jornadas/principais/whispers_in_the_walls.md\|Whispers in the Walls]] | Dez 2023 | Segredos Entrati e Albrecht | ~2h | The New War, Heart of Deimos | Acesso ao Sanctum Anatomica, Citrine |
| [[missoes/jornadas/principais/1999.md\|1999]] | Dez 2024 | Arthur e o passado pré-Orokin | ~3h | Whispers in the Walls | Acesso à Cidade 1999, Cyte-09 |

### Jornadas de Warframe e Companheiro

| Jornada | Lançamento | Duração Est. | Pré-Requisito | Recompensa Principal |
|---|---|---|---|---|
| [[missoes/jornadas/secundarios/howl_of_the_kubrow.md\|Howl of the Kubrow]] | Jun 2014 | ~30 min | Vor's Prize | Sistema de Kubrow desbloqueado, ovo de Kubrow |
| [[missoes/jornadas/secundarios/stolen_dreams.md\|Stolen Dreams]] | Dez 2014 | ~40 min | MR3 | Blueprint do Ash |
| [[missoes/jornadas/secundarios/hidden_messages.md\|Hidden Messages]] | Dez 2014 | ~30 min | MR4 | Blueprint da Mirage |
| [[missoes/jornadas/secundarios/patient_zero.md\|Patient Zero]] | Out 2014 | ~30 min | Vor's Prize | Blueprint da Mesa |
| [[missoes/jornadas/secundarios/the_new_strange.md\|The New Strange]] | Mar 2015 | ~45 min | Vor's Prize | Blueprint do Chroma |
| [[missoes/jornadas/secundarios/the_jordas_precept.md\|The Jordas Precept]] | Jun 2015 | ~1h | The New Strange | Blueprint do Atlas |
| [[missoes/jornadas/secundarios/the_limbo_theorem.md\|The Limbo Theorem]] | Jan 2015 | ~45 min | MR2 | Blueprint do Limbo |
| [[missoes/jornadas/secundarios/a_man_of_few_words.md\|A Man of Few Words]] | 2016 | ~20 min | The Second Dream | Lore do Stalker |
| [[missoes/jornadas/principais/sands_of_inaros.md\|Sands of Inaros]] | Mar 2016 | ~1h | MR5, The Second Dream | Blueprint do Inaros |
| [[missoes/jornadas/secundarios/the_silver_grove.md\|The Silver Grove]] | Ago 2016 | ~45 min | The Second Dream | Blueprint da Titania, sistema Apothics |
| [[missoes/jornadas/secundarios/the_index_preview.md\|The Index Preview]] | Out 2016 | ~20 min | MR5 | Acesso ao The Index |
| [[missoes/jornadas/secundarios/the_glast_gambit.md\|The Glast Gambit]] | Dez 2016 | ~1h | The War Within, MR5 | Blueprint do Nidus |
| [[missoes/jornadas/secundarios/mask_of_the_revenant.md\|Mask of the Revenant]] | Ago 2018 | ~45 min | The War Within | Blueprint do Revenant |


## Junctions — Warframe — Segunda Mente


Junctions são nós especiais do mapa estelar que conectam planetas. Para desbloquear o acesso a um novo planeta, o jogador deve completar uma série de desafios no planeta atual — missões, derrotas de boss e marcos de progressão. Ao concluir, recebe um Specter do planeta destino como recompensa de combate e o acesso é liberado permanentemente. As Junctions formam o esqueleto da progressão no mapa estelar e garantem que o jogador tenha um mínimo de desenvolvimento antes de avançar.

| Junction | De → Para | Desafios Principais | Recompensa |
|---|---|---|---|
| [[missoes/juncoes/venus_junction.md\|Venus Junction]] | Terra → Vênus | Completar 3 missões na Terra; derrotar Captain Vor em Mercúrio; ter Mastery Rank 1 | Specter de Vênus |
| [[missoes/juncoes/mercury_junction.md\|Mercury Junction]] | Terra → Mercúrio | Completar 3 missões na Terra; craftar 1 Warframe; craftar 1 arma primária | Specter de Mercúrio |
| [[missoes/juncoes/mars_junction.md\|Mars Junction]] | Terra → Marte | Completar Exterminate na Terra; completar missão Spy; 150 kills com rifle | Specter de Marte |
| [[missoes/juncoes/phobos_junction.md\|Phobos Junction]] | Marte → Phobos | Completar todas as missões em Marte; derrotar o boss de Marte (Ruk) | Specter de Phobos |
| [[missoes/juncoes/ceres_junction.md\|Ceres Junction]] | Marte → Ceres | Completar 3 missões em Marte; 100 kills com Warframe abilities | Specter de Ceres |
| [[missoes/juncoes/jupiter_junction.md\|Jupiter Junction]] | Ceres → Júpiter | Completar todas as missões em Ceres; derrotar boss de Ceres (Lech Kril); MR2 | Specter de Júpiter |
| [[missoes/juncoes/europa_junction.md\|Europa Junction]] | Júpiter → Europa | Completar missão Spy em Júpiter; 200 kills com pistola; craftar 3 mods | Specter de Europa |
| [[missoes/juncoes/saturn_junction.md\|Saturn Junction]] | Europa → Saturno | Completar Survival em Europa; craftar arma usando blueprint de recompensa | Specter de Saturno |
| [[missoes/juncoes/uranus_junction.md\|Uranus Junction]] | Saturno → Urano | Completar missão Rescue em Saturno; 1000 kills com Warframe; MR4 | Specter de Urano |
| [[missoes/juncoes/neptune_junction.md\|Neptune Junction]] | Urano → Netuno | Completar Interception em Urano; completar Archwing mission | Specter de Netuno |
| [[missoes/juncoes/pluto_junction.md\|Pluto Junction]] | Netuno → Plutão | Completar Defense em Netuno; derrotar Raptor em Europa; MR5 | Specter de Plutão |
| [[missoes/juncoes/sedna_junction.md\|Sedna Junction]] | Plutão → Sedna | Completar Spy em Plutão; completar missão Hijack; craftar Forma | Specter de Sedna |
| [[missoes/juncoes/eris_junction.md\|Eris Junction]] | Sedna → Eris | Completar Assassination em Sedna; 500 kills com branca; MR6 | Specter de Eris |
| [[missoes/juncoes/lua_junction.md\|Lua Junction]] | Eris → Lua | Completar The Second Dream (quest obrigatória); todas as missões em Eris | Specter da Lua |
| [[missoes/juncoes/kuva_fortress_junction.md\|Kuva Fortress Junction]] | Sedna → Fortaleza Kuva | Completar The War Within; MR5 | Acesso à Fortaleza Kuva |
| [[missoes/juncoes/void_junction.md\|Void Junction]] | Phobos → Void | Completar 3 missões em Phobos; usar Void Relic uma vez | Acesso ao Void |
| [[missoes/juncoes/deimos_junction.md\|Deimos Junction]] | Marte → Deimos | Completar Heart of Deimos (quest); todas as missões em Marte | Acesso ao Câmbion Drift |
| [[missoes/juncoes/zariman_junction.md\|Zariman Junction]] | — | Completar Angels of the Zariman (quest) | Acesso ao Zariman Ten Zero |


## Bounties (Open Worlds) — Warframe — Segunda Mente


Bounties são missões encadeadas oferecidas pelos sindicatos dos Open Worlds. Cada bounty é composto por 3 a 5 etapas sequenciais com objetivos variados — Defense, Capture, Sabotage, Assassination — que ocorrem dentro do mapa aberto sem tela de loading entre elas. Completar o bounty inteiro entrega as recompensas de todas as etapas mais um bônus final. As recompensas incluem standing com o sindicato local, itens exclusivos da área e partes de Warframes específicos de cada mundo. O nível de dificuldade é escolhido antes de iniciar, com tiers progressivos que determinam o nível dos inimigos e a qualidade das recompensas.

### [[missoes/bounties/eidolon.md|Planícies de Eidolon]]
*Sindicato: Ostron (Cetus) · Nível Base: Dia — inimigos comuns; Noite — Vomvalysts e Eidolons*

| Tier | Nível dos Inimigos | Recompensas Destaque | Melhor Para |
|---|---|---|---|
| **Tier 1** | 10–30 | Standing Ostron, Iradite, blueprints básicos | Início de jogo, farm de recursos comuns |
| **Tier 2** | 20–40 | Standing, Gara Neuroptics, Cetus Wisp | Farm de Gara e recursos incomuns |
| **Tier 3** | 30–50 | Standing, Gara Chassis, Cores Sentient | Farm de Gara e Sentient Cores |
| **Tier 4** | 40–60 | Standing, Gara Systems, Breath of the Eidolon | Farm de Gara Systems e materiais raros |
| **Tier 5** | 50–70+ | Standing máximo, recompensas raras, mods Ostron | Farm de standing e recompensas end-tier |
| **Caça Eidolon (Noite)** | 30–60 | Eidolon Shards, Brilliant/Radiant Shards, Arcanes | Farm de Arcanes e progressão do Operator |

### [[missoes/bounties/orbe_vallis.md|Orbe Vallis]]
*Sindicato: Solaris United (Fortuna) · Clima alterna entre quente e frio — afeta spawns e recursos*

| Tier | Nível dos Inimigos | Recompensas Destaque | Melhor Para |
|---|---|---|---|
| **Tier 1** | 10–30 | Standing Solaris, recursos básicos, Debt-Bonds | Início de jogo na Vallis |
| **Tier 2** | 20–40 | Standing, Baruuk Neuroptics, Gyromag Systems | Farm de Baruuk |
| **Tier 3** | 30–50 | Standing, Baruuk Chassis, Atmo Systems | Farm de Baruuk e sistemas de MOA |
| **Tier 4** | 40–60 | Standing, Baruuk Systems, Repeller Systems | Farm de Baruuk Systems |
| **Tier 5** | 50–70+ | Standing máximo, Toroids, mods Fortuna | Farm de Toroids e standing máximo |
| **Orb Mother (Profit-Taker)** | 60–80 | Toroids raros, Atmo/Repeller Systems, Arcanes | Farm de recursos de Mech e Arcanes |
| **Orb Mother (Exploiter)** | 40–60 | Diluted Thermia, recompensas sazonais | Farm de Thermia e drops exclusivos |

### [[missoes/bounties/cambion_drift.md|Câmbion Drift]]
*Sindicato: Entrati (Necralisk) · Ciclo dia (Fass) / noite (Vome) afeta recursos e spawns Infestados*

| Tier | Nível dos Inimigos | Recompensas Destaque | Melhor Para |
|---|---|---|---|
| **Tier 1** | 15–35 | Standing Entrati, Bile, Ganglion | Início no Deimos |
| **Tier 2** | 25–45 | Standing, Xaku Neuroptics, materiais Infestados | Farm de Xaku |
| **Tier 3** | 35–55 | Standing, Xaku Chassis, Namalon | Farm de Xaku e Necramech components |
| **Tier 4** | 45–65 | Standing, Xaku Systems, Pustulant Cerebrum | Farm de Xaku Systems |
| **Tier 5** | 55–75+ | Standing máximo, Necramech mods, recompensas raras | Farm de mods Necramech e standing |
| **Iso Vault** | 40–80 | Blueprints Necramech, Namalon, Voidrig/Bonewidow parts | Farm de Necramech completo |

### [[missoes/bounties/duviri.md|Duviri]]
*Sindicato: Kaithe (Drifter's Camp) · Mecânica roguelike — cada run tem armas e frames aleatórios do Decret*

| Tier | Nível dos Inimigos | Recompensas Destaque | Melhor Para |
|---|---|---|---|
| **Testemunho (Normal)** | 30–60 | Pathos Clamp, blueprints Duviri, mods | Introdução ao Duviri, farm de Pathos Clamp |
| **Testemunho (Hard)** | 60–100 | Cavalero's Burden, mods raros, Incarnon Genesis | Farm de Incarnon Adapters |
| **O Circuito** | Variável | Incarnon Genesis adapters por semana | Meta de farm — Incarnon para armas clássicas |
| **Kullervo** | 80–100 | Kullervo parts, Kullervo's Bane | Farm do Warframe Kullervo |

### [[missoes/bounties/zariman.md|Zariman Ten Zero]]
*Sindicato: The Holdfasts (Chrysalith) · Ambiente Void — inimigos Void Angels e Zariman enemies*

| Tier | Nível dos Inimigos | Recompensas Destaque | Melhor Para |
|---|---|---|---|
| **Tier 1** | 40–60 | Standing Holdfasts, Voidplume Pinion/Quill | Início no Zariman |
| **Tier 2** | 50–70 | Standing, Gyre Neuroptics, Voidplume Crest | Farm de Gyre |
| **Tier 3** | 60–80 | Standing, Gyre Chassis, Voidplume Drift | Farm de Gyre e recursos raros |
| **Tier 4** | 70–90 | Standing, Gyre Systems, Voidplume Down | Farm de Gyre Systems |
| **Tier 5** | 80–100+ | Standing máximo, Arcanes Zariman, Voidplume Intact | Farm de Arcanes e mods Zariman |
| **Void Angel** | 80–100 | Voidplume Intact, Arcanes raros | Recurso mais raro do Zariman |


## 💡 Curiosidades — Warframe — Segunda Mente


- The Second Dream é considerada a maior virada narrativa do jogo — a revelação sobre a natureza do Tenno mudou completamente a relação dos jogadores com o personagem que controlam há centenas de horas.
- The New War durou mais de 6 anos em desenvolvimento parcial e foi prometida múltiplas vezes antes de finalmente ser lançada em dezembro de 2021 — é a quest mais longa e cinematográfica da história do jogo, com segmentos jogáveis em três perspectivas diferentes.
- O sistema de Junctions foi adicionado para substituir os requisitos de MR puro que bloqueavam progressão — a intenção era que jogadores chegassem a cada planeta com equipamento e conhecimento adequados, não apenas nível.
- Arbitration foi projetada como modo de alto risco onde morte é permanente na run — a DE a criou como resposta à demanda por conteúdo desafiador sem ser endgame puro, mas o modo ainda é considerado acessível por veteranos.
- A missão Defection em Eris é amplamente considerada uma das piores do jogo — a IA dos colonos que precisam ser escoltados é notoriamente ruim, levando ao desenvolvimento de estratégias de "controle de dano" para compensar os erros deles.
- Sorties existem desde 2015 e por muito tempo foram a principal fonte de Rivens — até hoje mantêm a função, mas perderam prestígio com a adição de Archon Hunts e Arbitrations.
- O Duviri foi o primeiro modo do jogo a usar seleção aleatória de Warframe e armas para cada run — uma mudança filosófica significativa que inicialmente causou divisão na comunidade, mas foi bem recebida com o tempo.
- Spy é a missão com maior skill ceiling do jogo básico — cofres avançados em Lua e Kuva Fortress exigem rotas específicas e execução precisa para serem completados sem alarme, e existem guias dedicados a cada cofre individualmente.
- O Void foi o único bioma do jogo por muito tempo onde Warframes Prime podiam ser farmados — o sistema de Void Relics que o substituiu foi adicionado em 2016, tornando o acesso mais acessível mas retirando a exclusividade do Void como destino de farm.
- Caça de Eidolons à noite nas Planícies é um dos conteúdos mais elaborados do jogo em termos de coordenação — runs de Tridolon (três Eidolons em uma noite) exigem squads especializados com builds de Operator específicas, Arcanes de alta raridade e execução coordenada.

----------------------------------------

## Seção: mods — Warframe — Segunda Mente

### 📄 arquivo: _Mods _Indice.md

# Mods — Índice

> [!quote]
> *"Mods não são apenas upgrades. São a linguagem com que você reescreve um Warframe."*


## 📊 Visão Geral — Warframe — Segunda Mente


Mods são o **sistema central de progressão e customização** do Warframe. Cada mod é um cartão equipável que modifica atributos de Warframes, armas ou companheiros — aumentando dano, defesa, velocidade de habilidades, alcance e dezenas de outros parâmetros. Sem mods, um Warframe é apenas uma casca; com o conjunto certo, o mesmo frame pode ter desempenhos radicalmente diferentes dependendo do conteúdo.

Mods são obtidos de diversas fontes: drops de inimigos, recompensas de missão, sindicatos, Nightwave e vendedores especiais. Cada mod tem um **custo de capacidade** que consome o pool de mod capacity do equipamento — e pode ser rankiado com **Endo** e **Créditos** para aumentar seus efeitos (e custo) simultaneamente.


## Como Adquirir — Warframe — Segunda Mente


| Fonte | Mods Disponíveis |
|---|---|
| **Drop de inimigos** | Comuns e Incomuns — dropam ao longo de qualquer missão |
| **Drop de bosses** | Raros específicos de cada boss |
| **Void Relics** | Mods Prime via abertura de Relíquias |
| **Sindicatos** | Mods exclusivos por reputação |
| **Nightwave** | Mods raros por Créditos de temporada |
| **Baro Ki'Teer** | Mods Primed — rotação quinzenal por Ducats + Créditos |
| **Orokin Vault** | Mods Corrupted — requerem Dragon Key |
| **Arbitrations** | Mods exclusivos de alta dificuldade |
| **Steel Path** | Mods de end-game |
| **Sanctuary Onslaught** | Mods raros de drop exclusivo |
| **Sorties / Nightwave** | Rivens — mods com atributos aleatórios |
| **Transmutation** | Combinar 4 mods para chance de gerar mod raro |


## Raridades — Warframe — Segunda Mente


| Raridade | Borda | Descrição |
|---|---|---|
| **Comum** | Bronze | Drop em qualquer missão — base de qualquer build |
| **Incomum** | Prata | Drop moderado — cobre maioria dos slots intermediários |
| **Raro** | Ouro | Drop escasso — alguns só em bosses ou missões específicas |
| **Lendário** | Vermelho | Extremamente raros (ex: Amalgam Serration, Argon Scope) |
| **Primed** | Dourado especial | Versões superiores — Baro Ki'Teer ou Nightwave |
| **Umbral** | Dourado-branco | Série Umbral — alta capacidade, sinergia em set |
| **Corrupted** | Escuro | Dois efeitos opostos — poder alto com penalidade |
| **Syndicate** | Cor do sindicato | Exclusivos de sindicatos — proc especial adicional |
| **Riven** | Multicolor | Atributos aleatórios para arma específica |


## Sistema de Capacidade — Warframe — Segunda Mente


Cada equipamento tem um pool de **Mod Capacity** que limita quantos mods podem ser equipados simultaneamente.

| Conceito | Descrição |
|---|---|
| **Capacidade base** | Rank do equipamento = pontos disponíveis (max 30 ao rank 30) |
| **Orokin Reactor** | Dobra a capacidade de Warframes e companheiros (30 → 60) |
| **Orokin Catalyst** | Dobra a capacidade de armas (30 → 60) |
| **Polaridade** | Cada slot tem polaridade. Mod compatível custa **metade** dos pontos |
| **Forma** | Adiciona ou altera a polaridade de um slot — reseta o rank do equipamento para 0 |
| **Aura (Warframe)** | Slot especial de aura — seu valor é **somado** à capacidade total do frame |
| **Exilus** | Slot de utilidade — requer Exilus Adapter (armas) ou Exilus Warframe Adapter |

### Polaridades

| Nome | Símbolo | Mods Típicos |
|---|---|---|
| **Madurai** | V | Dano, Força de habilidades (Intensify, Serration) |
| **Vazarin** | D | Defesa, HP, Shields (Vitality, Redirection) |
| **Naramon** | — | Utilidade, velocidade (Rush, Natural Talent) |
| **Unairu** | ◊ | Armadura, mods de equilíbrio (Steel Fiber) |
| **Zenurik** | ~ | Energia, eficiência (Flow, Streamline) |
| **Penjaga** | = | Mods de Aura exclusivamente |
| **Umbra** | Ω | Mods Umbral exclusivamente |

> [!tip] Forma é o caminho mais impactante
> Cada Forma adiciona uma polaridade — um slot com polaridade compatível corta o custo pela metade, liberando pontos para mais mods. Frames e armas de end-game costumam ter 5–8 Formas instaladas.


## Sub-Índices — Warframe — Segunda Mente


| Sub-Índice | Conteúdo Exclusivo |
|---|---|
| [[mods/warframe/_Mods Warframe _Indice.md\|Mods de Warframe]] | Defesa, habilidades (4 pilares), aura, exilus, augments, set Umbral |
| [[mods/armas/_Mods Armas _Indice.md\|Mods de Armas]] | Primárias, secundárias, brancas, stances, archwing; combinações elementais |
| [[mods/companheiros/_Mods Companheiros _Indice.md\|Mods de Companheiros]] | Sentinels, kavats, kubrows, MOAs, hounds; precept mods |
| [[mods/especiais/_Mods Especiais _Indice.md\|Mods Especiais]] | Primed, Umbral, Corrupted (Orokin Vault), Syndicate, Rivens, Amalgam |


## 💡 Curiosidades — Warframe — Segunda Mente


- Vitality existe desde o Open Beta de 2013 e permanece útil em praticamente qualquer build de sobrevivência.
- Blind Rage tem o maior bônus de Strength do jogo, mas penaliza tanto a Eficiência que exige compensação com Fleeting Expertise.
- Vacuum era exclusivo do Carrier — após pressão da comunidade, a DE expandiu o efeito base para todos os companheiros.
- Baro Ki'Teer tem rotação quinzenal — rastrear o histórico de visitas é prática padrão entre veteranos para prever quais Primed virão.
- Blood Rush e Condition Overload reformularam o meta de arma branca ao lançamento — tornaram builds críticas e de status viáveis no end-game.
- Rivens têm economia própria no Trade Chat — os mais valiosos chegam a custar milhares de Platinum.
- A DE rebalanceia as Dispositions de Riven periodicamente — nerfs podem desvalorizar um Riven de uma atualização para outra.
- O único mod completamente único e intransferível é o Amalgam Serration — obtido na Junction de Marte, impossível de negociar.
- Narrow Minded + Overextended juntos criam o "zero waste" de alcance-duração — base de builds de Nidus, Revenant e frames que não dependem de Range.
- A Transmutation é o método menos eficiente — usada principalmente para desfazer duplicatas indesejadas. A chance de obter algo útil é baixa.


## 🔗 Relacionados — Warframe — Segunda Mente


| Índice | Relação |
|---|---|
| [[warframes/_Warframes _Indice.md\|Warframes]] | Frames que equipam os mods de warframe |
| [[armas/_Armas _Indice.md\|Armas]] | Armas que equipam os mods de arma |
| [[companheiros/_Companheiros _Indice.md\|Companheiros]] | Companheiros que equipam mods de companheiro |
| [[mecanicas/_Mecanicas _Indice.md\|Mecânicas]] | Sistemas de combate que os mods influenciam |
| [[mecanicas/sindicatos/_Sindicatos _Indice.md\|Sindicatos]] | Fonte de mods Syndicate |

----------------------------------------

## Seção: mods\armas — Warframe — Segunda Mente

### 📄 arquivo: _Mods Armas _Indice.md

# Mods de Armas — Índice

> [!quote]
> *"A arma é o veículo. Os mods são o motor."*


## 📊 Visão Geral — Warframe — Segunda Mente


Mods de armas modificam **dano, velocidade, crítico, status e elementos** de armas primárias, secundárias, brancas e archwing. Cada categoria de arma tem mods específicos — um mod de rifle não se aplica a pistolas, e stances são exclusivos de brancas.

**Slots:** 8 normais + 1 Exilus (requer Exilus Weapon Adapter) + 1 Arcane (armas com slot arcane)
**Capacidade base:** 30 (rank 30) → 60 com Orokin Catalyst


## Combinações de Dano Elemental — Warframe — Segunda Mente


A **ordem de equipamento** dos mods elementais determina quais elementos são combinados:

| Combinação | Resultado | Nota |
|---|---|---|
| Calor + Frio | **Blast** | Knockdown nos inimigos |
| Calor + Elétrico | **Radiação** | Confunde inimigos — eficaz contra Alloy Armor |
| Calor + Tóxico | **Gás** | Nuvem tóxica AoE — eficaz contra Corpus |
| Frio + Elétrico | **Magnético** | -Shield — eficaz contra Corpus |
| Frio + Tóxico | **Viral** | -HP máximo — universal, meta geral |
| Elétrico + Tóxico | **Corrosivo** | -Armor — eficaz contra Grineer |

> [!important] Ordem importa
> Mods elementais equipados primeiro no slot se combinam com o próximo da mesma pilha. Para evitar combinações indesejadas, coloque elementais que NÃO devem combinar em slots separados (slots com polaridade errada, por exemplo).


## Primárias — Dano e Crítico — Warframe — Segunda Mente


| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[mods/armas/serration.md\|Serration]] | Comum | +Dano base de rifle | Drop geral |
| [[mods/armas/primed_serration.md\|Primed Serration]] | Primed | +Dano base muito elevado | Baro Ki'Teer |
| [[mods/armas/split_chamber.md\|Split Chamber]] | Incomum | +Multishot — projéteis extras por disparo | Drop geral |
| [[mods/armas/vigilante_armaments.md\|Vigilante Armaments]] | Incomum | +Multishot + chance de upgrade de crítico | Drop geral (set Vigilante) |
| [[mods/armas/point_strike.md\|Point Strike]] | Incomum | +Chance de crítico | Drop geral |
| [[mods/armas/vital_sense.md\|Vital Sense]] | Incomum | +Multiplicador de crítico | Drop geral |
| [[mods/armas/argon_scope.md\|Argon Scope]] | Lendário | +Chance de crítico temporário ao dar headshot | Arbitrations |
| [[mods/armas/hunter_munitions.md\|Hunter Munitions]] | Raro | Críticos aplicam Slash — rifle | Syndicato (Steel Meridian) |
| [[mods/armas/heavy_caliber.md\|Heavy Caliber]] | Corrupted | +Dano muito alto / -Accuracy | Orokin Vault |
| [[mods/armas/critical_delay.md\|Critical Delay]] | Corrupted | +Chance de crítico alto / -Fire Rate | Orokin Vault |
| [[mods/armas/vile_acceleration.md\|Vile Acceleration]] | Corrupted | +Fire Rate muito alto / -Dano base | Orokin Vault |
| [[mods/armas/speed_trigger.md\|Speed Trigger]] | Incomum | +Fire Rate | Drop geral |
| [[mods/armas/shred.md\|Shred]] | Incomum | +Fire Rate + Punch Through | Drop geral |
| [[mods/armas/tainted_mag.md\|Tainted Mag]] | Corrupted | +Magazine Size / -Reload Speed | Orokin Vault |
| [[mods/armas/depleted_reload.md\|Depleted Reload]] | Corrupted | -Reload Time / -Magazine Size | Orokin Vault |


## Primárias — Elementais — Warframe — Segunda Mente


| Mod | Raridade | Elemento | Nota |
|---|---|---|---|
| [[mods/armas/hellfire.md\|Hellfire]] | Incomum | +Calor | Drop geral |
| [[mods/armas/cryo_rounds.md\|Cryo Rounds]] | Incomum | +Frio | Drop geral |
| [[mods/armas/stormbringer.md\|Stormbringer]] | Incomum | +Elétrico | Drop geral |
| [[mods/armas/infected_clip.md\|Infected Clip]] | Incomum | +Tóxico | Drop geral |
| [[mods/armas/primed_cryo_rounds.md\|Primed Cryo Rounds]] | Primed | +Frio muito elevado | Baro Ki'Teer |
| [[mods/armas/high_voltage.md\|High Voltage]] | Raro | +Elétrico + proc Elétrico | Syndicato (Perrin Sequence) |
| [[mods/armas/thermite_rounds.md\|Thermite Rounds]] | Raro | +Calor + proc Calor | Syndicato (Red Veil) |
| [[mods/armas/rime_rounds.md\|Rime Rounds]] | Incomum | +Frio — espingardas | Drop geral |
| [[mods/armas/seeking_force.md\|Seeking Force]] | Incomum | +Punch Through — espingardas | Drop geral |
| [[mods/armas/tainted_shell.md\|Tainted Shell]] | Corrupted | +Pellet Count / -Fire Rate — espingardas | Orokin Vault |


## Secundárias — Warframe — Segunda Mente


| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[mods/armas/hornet_strike.md\|Hornet Strike]] | Comum | +Dano base de pistola | Drop geral |
| [[mods/armas/barrel_diffusion.md\|Barrel Diffusion]] | Incomum | +Multishot de pistola | Drop geral |
| [[mods/armas/lethal_torrent.md\|Lethal Torrent]] | Raro | +Multishot + Fire Rate | Syndicato (Cephalon Suda) |
| [[mods/armas/pistol_gambit.md\|Pistol Gambit]] | Incomum | +Chance de crítico de pistola | Drop geral |
| [[mods/armas/target_cracker.md\|Target Cracker]] | Incomum | +Multiplicador de crítico de pistola | Drop geral |
| [[mods/armas/primed_pistol_gambit.md\|Primed Pistol Gambit]] | Primed | +Chance de crítico muito elevado | Baro Ki'Teer |
| [[mods/armas/primed_target_cracker.md\|Primed Target Cracker]] | Primed | +Multiplicador de crítico muito elevado | Baro Ki'Teer |
| [[mods/armas/anemic_agility.md\|Anemic Agility]] | Corrupted | +Fire Rate / -Dano base | Orokin Vault |
| [[mods/armas/convulsion.md\|Convulsion]] | Incomum | +Elétrico em pistola | Drop geral |
| [[mods/armas/deep_freeze.md\|Deep Freeze]] | Incomum | +Frio em pistola | Drop geral |
| [[mods/armas/heated_charge.md\|Heated Charge]] | Incomum | +Calor em pistola | Drop geral |
| [[mods/armas/pathogen_rounds.md\|Pathogen Rounds]] | Incomum | +Tóxico em pistola | Drop geral |
| [[mods/armas/frostbite.md\|Frostbite]] | Raro | +Frio + proc Frio em pistola | Syndicato (New Loka) |
| [[mods/armas/scorch.md\|Scorch]] | Raro | +Calor + proc Calor em pistola | Syndicato (Red Veil) |
| [[mods/armas/hemorrhage.md\|Hemorrhage]] | Raro | Procs de Impact → Slash em pistola | Syndicato (Steel Meridian) |
| [[mods/armas/augur_pact.md\|Augur Pact]] | Incomum | Gasto de Energia aumenta dano de pistola | Syndicatos (set Augur) |


## Brancas — Dano e Crítico — Warframe — Segunda Mente


| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[mods/armas/pressure_point.md\|Pressure Point]] | Comum | +Dano base branca | Drop geral |
| [[mods/armas/primed_pressure_point.md\|Primed Pressure Point]] | Primed | +Dano base muito elevado | Baro Ki'Teer |
| [[mods/armas/true_steel.md\|True Steel]] | Incomum | +Chance de crítico | Drop geral |
| [[mods/armas/organ_shatter.md\|Organ Shatter]] | Incomum | +Multiplicador de crítico | Drop geral |
| [[mods/armas/blood_rush.md\|Blood Rush]] | Raro | +Crítico escala com Combo Counter | Arbitrations |
| [[mods/armas/weeping_wounds.md\|Weeping Wounds]] | Raro | +Status escala com Combo Counter | Arbitrations |
| [[mods/armas/condition_overload.md\|Condition Overload]] | Raro | +Dano por status ativo no alvo | Drop geral |
| [[mods/armas/spoiled_strike.md\|Spoiled Strike]] | Corrupted | +Dano muito alto / -Attack Speed | Orokin Vault |
| [[mods/armas/berserker_fury.md\|Berserker Fury]] | Raro | +Attack Speed ao realizar crítico | Drop geral |
| [[mods/armas/quickening.md\|Quickening]] | Incomum | +Attack Speed + Combo Duration | Drop geral |
| [[mods/armas/body_count.md\|Body Count]] | Incomum | +Duração do Combo Counter | Drop geral |
| [[mods/armas/drifting_contact.md\|Drifting Contact]] | Corrupted | +Combo Duration / chance de Status | Orokin Vault |
| [[mods/armas/corrupt_charge.md\|Corrupt Charge]] | Corrupted | +Combo inicial alto / -Duração do Counter | Orokin Vault |
| [[mods/armas/life_strike.md\|Life Strike]] | Raro | Consume Combo → regenera HP | Drop geral |
| [[mods/armas/healing_return.md\|Healing Return]] | Raro | Regenera HP por hit em alvo com status ativo | Drop geral |
| [[mods/armas/primed_fever_strike.md\|Primed Fever Strike]] | Primed | +Tóxico muito elevado em brancas | Baro Ki'Teer |


## Brancas — Stances — Warframe — Segunda Mente


Stances são mods de slot exclusivo que substituem completamente os ataques normais da arma por combos específicos. Ver [[armas/brancas/_Armas _Brancas _Indice.md|Brancas — Stances por Tipo]] para a tabela completa de compatibilidade.

| Mod | Raridade | Tipo de Arma | Fonte |
|---|---|---|---|
| [[mods/armas/crimson_dervish.md\|Crimson Dervish]] | Raro | Espada | Drop geral |
| [[mods/armas/swooping_falcon.md\|Swooping Falcon]] | Raro | Espada | Drop geral |
| [[mods/armas/iron_phoenix.md\|Iron Phoenix]] | Incomum | Espada | Drop geral |
| [[mods/armas/vengeful_revenant.md\|Vengeful Revenant]] | Raro | Espada | Drop geral |
| [[mods/armas/blind_justice.md\|Blind Justice]] | Raro | Nikana / Espada | Drop geral |
| [[tranquil_cleave\|Tranquil Cleave]] | Incomum | Nikana | Drop geral |
| [[decisive_judgement\|Decisive Judgement]] | Raro | Nikana | Drop geral |
| [[mods/armas/eleventh_storm.md\|Eleventh Storm]] | Raro | Espadim (Rapier) | Drop geral |
| [[mods/armas/pointed_wind.md\|Pointed Wind]] | Incomum | Espadim / Adaga | Drop geral |
| [[mods/armas/tempo_royale.md\|Tempo Royale]] | Raro | Espada Pesada | Drop geral |
| [[mods/armas/rending_crane.md\|Rending Crane]] | Incomum | Espada Pesada | Drop geral |
| [[mods/armas/cleaving_whirlwind.md\|Cleaving Whirlwind]] | Raro | Espada Pesada | Drop geral |
| [[mods/armas/swirling_tiger.md\|Swirling Tiger]] | Raro | Espadas Duplas | Drop geral |
| [[crossing_snakes\|Crossing Snakes]] | Incomum | Espadas Duplas | Drop geral |
| [[dividing_blades\|Dividing Blades]] | Raro | Espadas Duplas | Drop geral |
| [[mods/armas/homing_fang.md\|Homing Fang]] | Raro | Adaga / Adagas Duplas | Drop geral |
| [[gnashing_payara\|Gnashing Payara]] | Raro | Adagas Duplas | Drop geral |
| [[mods/armas/spinning_needle.md\|Spinning Needle]] | Raro | Adagas Duplas | Drop geral |
| [[mods/armas/shimmering_blight.md\|Shimmering Blight]] | Incomum | Lança (Polearm) | Drop geral |
| [[mods/armas/bleeding_willow.md\|Bleeding Willow]] | Raro | Lança (Polearm) | Drop geral |
| [[typhoon_s_edge\|Typhoon's Edge]] | Raro | Lança (Polearm) | Drop geral |
| [[mods/armas/clashing_forest.md\|Clashing Forest]] | Incomum | Cajado (Staff) | Drop geral |
| [[mods/armas/flailing_branch.md\|Flailing Branch]] | Incomum | Cajado (Staff) | Drop geral |
| [[atlantas_struggle\|Atlantas Struggle]] | Raro | Nunchaku | Drop geral |
| [[mods/armas/gemini_cross.md\|Gemini Cross]] | Raro | Tonfa | Drop geral |
| [[mods/armas/sovereign_outcast.md\|Sovereign Outcast]] | Raro | Tonfa | Drop geral |
| [[mods/armas/crushing_ruin.md\|Crushing Ruin]] | Raro | Martelo | Drop geral |
| [[mods/armas/shattering_storm.md\|Shattering Storm]] | Incomum | Martelo | Drop geral |
| [[mods/armas/vermillion_storm.md\|Vermillion Storm]] | Raro | Garras | Drop geral |
| [[seismic_palm\|Seismic Palm]] | Incomum | Garras | Drop geral |
| [[brutal_tide\|Brutal Tide]] | Raro | Garras | Drop geral |
| [[mods/armas/reaping_spiral.md\|Reaping Spiral]] | Raro | Foice (Scythe) | Drop geral |
| [[mods/armas/stalking_fan.md\|Stalking Fan]] | Raro | Foice (Scythe) | Drop geral |
| [[astral_twilight\|Astral Twilight]] | Raro | Glaive | Drop geral |
| [[defiled_snapdragon\|Defiled Snapdragon]] | Raro | Chicote | Drop geral |
| [[burning_wasp\|Burning Wasp]] | Incomum | Chicote | Drop geral |
| [[mods/armas/wise_razor.md\|Wise Razor]] | Raro | Lâmina e Chicote | Drop geral |
| [[mods/armas/final_harbinger.md\|Final Harbinger]] | Raro | Espada e Escudo | Drop geral |
| [[bullet_dance\|Bullet Dance]] | Raro | Espingarda Melee | Drop geral |
| [[high_noon\|High Noon]] | Raro | Espingarda Melee | Drop geral |
| [[slicing_feathers\|Slicing Feathers]] | Raro | Leques (Warfan) | Drop geral |


## Archwing — Warframe — Segunda Mente


Mods de Archwing têm pool **completamente separado** — não se aplicam a armas terrestres e vice-versa.

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[dual_rounds\|Dual Rounds]] | Incomum | +Multishot — Arch-Gun | Drop Archwing |
| [[automatic_trigger\|Automatic Trigger]] | Incomum | +Fire Rate — Arch-Gun | Drop Archwing |
| [[charged_bullets\|Charged Bullets]] | Incomum | +Dano base — Arch-Gun | Drop Archwing |
| [[explosive_payload\|Explosive Payload]] | Incomum | +Status Chance — Arch-Gun | Drop Archwing |
| [[hollowed_bullets\|Hollowed Bullets]] | Raro | +Crit Chance — Arch-Gun | Drop Archwing |
| [[mods/armas/polar_coil.md\|Polar Coil]] | Incomum | +Frio — Arch-Gun | Drop Archwing |
| [[orokin_reach\|Orokin Reach]] | Incomum | +Alcance — Arch-Melee | Drop Archwing |
| [[elec_drain\|Elec Drain]] | Incomum | +Elétrico — Arch-Melee | Drop Archwing |
| [[astral_slash\|Astral Slash]] | Incomum | +Slash — Arch-Melee | Drop Archwing |


## 🔗 Relacionados — Warframe — Segunda Mente


| Índice | Relação |
|---|---|
| [[mods/_Mods _Indice.md\|Mods]] | Índice geral — sistema de mods |
| [[mods/especiais/_Mods Especiais _Indice.md\|Mods Especiais]] | Primed, Corrupted e Syndicate de armas |
| [[armas/_Armas _Indice.md\|Armas]] | Armas que equipam estes mods |
| [[armas/brancas/_Armas _Brancas _Indice.md\|Brancas]] | Stances por tipo de arma branca |
| [[armas/archwing/_Armas _Archwing _Indice.md\|Archwing]] | Armas archwing e seu pool de mods |

----------------------------------------

## Seção: mods\warframe — Warframe — Segunda Mente

### 📄 arquivo: _Mods Warframe _Indice.md

# Mods de Warframe — Índice

> [!quote]
> *"Quatro pilares sustentam qualquer build: Força, Duração, Alcance e Eficiência."*


## 📊 Visão Geral — Warframe — Segunda Mente


Mods de Warframe modificam as **habilidades e atributos base** do frame. Cada frame tem 8 slots normais + 1 slot de Aura + 1 slot Exilus. A Aura adiciona capacidade à capacidade total do frame.

**Slots:** 8 normais + 1 Aura + 1 Exilus (requer Warframe Exilus Adapter)
**Capacidade base:** 30 (rank 30) → 60 com Orokin Reactor


## Os 4 Pilares de Build — Warframe — Segunda Mente


As habilidades de todo Warframe são afetadas por quatro stats, cada um controlado por uma família de mods:

| Pilar | Stat | O que afeta | Mods base → Corrupted |
|---|---|---|---|
| **Strength** | Poder das habilidades | Dano, escudo, cura e qualquer valor numérico das skills | Intensify → Blind Rage, Transient Fortitude |
| **Duration** | Duração das habilidades | Quanto tempo habilidades persistem | Continuity → Narrow Minded |
| **Range** | Alcance das habilidades | Raio e distância de efeito | Stretch → Overextended |
| **Efficiency** | Custo de energia | Quanto menos energia as habilidades consomem | Streamline → Fleeting Expertise |

> [!note] Mods Corrupted e trade-offs
> Mods Corrupted (Orokin Vault) empurram um pilar ao limite com penalidade em outro. Ex: Blind Rage dá +Strength enorme mas drena -Efficiency. A arte do build é balancear esses trade-offs.


## Defesa e Sobrevivência — Warframe — Segunda Mente


| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[mods/warframe/vitality.md\|Vitality]] | Comum | +HP | Drop geral |
| [[mods/warframe/redirection.md\|Redirection]] | Comum | +Shield | Drop geral |
| [[mods/warframe/steel_fiber.md\|Steel Fiber]] | Incomum | +Armor | Drop geral |
| [[mods/warframe/primed_vigor.md\|Primed Vigor]] | Primed | +HP e +Shield combinados | Baro Ki'Teer |
| [[mods/warframe/umbral_vitality.md\|Umbral Vitality]] | Umbral | +HP muito elevado — set Umbral | Quest (The Sacrifice) |
| [[mods/warframe/adaptation.md\|Adaptation]] | Raro | Resistência ao tipo de dano recebido (acumula até 90%) | Arbitrations |
| [[mods/warframe/quick_thinking.md\|Quick Thinking]] | Raro | Usa Energia como buffer quando HP chega a zero | Drop geral |
| [[mods/warframe/rolling_guard.md\|Rolling Guard]] | Raro | Invencibilidade breve + remove status no dodge | Arbitrations |
| [[grace\|Grace]] | Raro | Regenera HP ao sair de estado crítico | Drop geral |
| [[mods/warframe/augur_accord.md\|Augur Accord]] | Incomum | Gasto de Energia restaura Shields | Syndicatos |


## 🔮 Habilidades — Warframe — Segunda Mente


### Strength

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[mods/warframe/intensify.md\|Intensify]] | Incomum | +Strength | Drop geral |
| [[mods/warframe/umbral_intensify.md\|Umbral Intensify]] | Umbral | +Strength muito elevado — set Umbral | Quest (The Sacrifice) |
| [[mods/warframe/transient_fortitude.md\|Transient Fortitude]] | Corrupted | +Strength alto / -Duration | Orokin Vault |
| [[mods/warframe/blind_rage.md\|Blind Rage]] | Corrupted | +Strength muito alto / -Efficiency | Orokin Vault |
| [[mods/warframe/energy_conversion.md\|Energy Conversion]] | Raro | +Strength temporário ao pegar orb de energia | Drop geral |
| [[mods/warframe/augur_secrets.md\|Augur Secrets]] | Incomum | Gasto de Energia +Strength temporário | Syndicatos |
| [[mods/warframe/power_drift.md\|Power Drift]] | Incomum | +Strength menor + knockdown resist | Junction |

### Duration

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[mods/warframe/continuity.md\|Continuity]] | Comum | +Duration | Drop geral |
| [[mods/warframe/constitution.md\|Constitution]] | Incomum | +Duration + -Knockdown Recovery | Drop geral |
| [[mods/warframe/primed_continuity.md\|Primed Continuity]] | Primed | +Duration muito elevado | Baro Ki'Teer |
| [[mods/warframe/narrow_minded.md\|Narrow Minded]] | Corrupted | +Duration muito alto / -Range | Orokin Vault |
| [[mods/warframe/augur_message.md\|Augur Message]] | Incomum | Gasto de Energia +Duration temporário | Syndicatos |

### Range

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[mods/warframe/stretch.md\|Stretch]] | Comum | +Range | Drop geral |
| [[mods/warframe/overextended.md\|Overextended]] | Corrupted | +Range muito alto / -Strength | Orokin Vault |
| [[mods/warframe/cunning_drift.md\|Cunning Drift]] | Incomum | +Range menor — slot Exilus | Drop geral |

### Efficiency

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[mods/warframe/streamline.md\|Streamline]] | Incomum | -Custo de Energia | Drop geral |
| [[mods/warframe/fleeting_expertise.md\|Fleeting Expertise]] | Corrupted | +Efficiency muito alto / -Duration | Orokin Vault |

### Energia

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[mods/warframe/flow.md\|Flow]] | Incomum | +Max Energia | Drop geral |
| [[mods/warframe/primed_flow.md\|Primed Flow]] | Primed | +Max Energia muito elevado | Baro Ki'Teer |
| [[mods/warframe/rage.md\|Rage]] | Raro | Dano em HP → Energia | Drop de Boss |
| [[mods/warframe/hunter_adrenaline.md\|Hunter Adrenaline]] | Raro | Dano em HP → Energia (mais eficiente) | Syndicato (Steel Meridian) |

### Velocidade e Utilidade

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[mods/warframe/natural_talent.md\|Natural Talent]] | Raro | -Cast Time de habilidades | Drop geral |


## Mods Umbral — Warframe — Segunda Mente


O **Set Umbral** consiste em três mods que se combinam para bônus extras quando dois ou mais estão equipados:

| Mod | Efeito Base | Bônus de Set |
|---|---|---|
| [[mods/warframe/umbral_vitality.md\|Umbral Vitality]] | +HP | +HP e +Umbral Damage (2 mods) |
| [[mods/warframe/umbral_intensify.md\|Umbral Intensify]] | +Strength | +Strength e +Umbral Damage (2 mods) |
| [[umbral_fiber\|Umbral Fiber]] | +Armor | +Armor e +Umbral Damage (2 mods) |

> [!note] Custo de Capacidade
> Mods Umbral têm custo de capacidade muito alto. Equipar o set completo exige frame com Orokin Reactor e várias Formas instaladas — na prática, reservados para frames com polaridade Umbra (ω) pré-instalada, como Excalibur Umbra.


## Augments de Frame — Warframe — Segunda Mente


Augments são mods **exclusivos por habilidade de frame específico** que modificam o comportamento de uma habilidade (ex: Seeking Shuriken modifica Ash, Roar de Rhino modifica outros frames via Helminth). Obtidos em:

- Sindicatos (maioria)
- Nightwave (rotação)
- Cephalon Simaris (alguns)

> [!important]
> Augments não aparecem neste índice individualmente — cada frame tem até 4 augments (um por habilidade). Consulte o arquivo individual do frame para os augments específicos.


## Aura — Warframe — Segunda Mente


Mods de Aura têm **polaridade Penjaga (=)** e ficam em slot exclusivo. O valor do mod é somado à capacidade total do frame — uma Aura de +18 aumenta a capacidade total de 30 para 48 (sem Reactor).

| Mod | Raridade | Efeito | Sinergias |
|---|---|---|---|
| [[mods/warframe/corrosive_projection.md\|Corrosive Projection]] | Incomum | -Armor dos inimigos | Meta contra Grineer (stack de 4 na squad) |
| [[mods/warframe/steel_charge.md\|Steel Charge]] | Comum | +Dano de arma branca | Builds de melee |
| [[mods/warframe/energy_siphon.md\|Energy Siphon]] | Incomum | Regeneração passiva de Energia (squad) | Frames com altas demandas de energia |
| [[mods/warframe/growing_power.md\|Growing Power]] | Incomum | +Strength ao aplicar Status | Syndicate (Cephalon Suda / New Loka) |
| [[mods/warframe/dead_eye.md\|Dead Eye]] | Incomum | +Dano de armas sniper | Builds sniper |
| [[mods/warframe/rifle_amp.md\|Rifle Amp]] | Comum | +Dano de rifles | Builds DPS |
| [[mods/warframe/pistol_amp.md\|Pistol Amp]] | Comum | +Dano de pistolas | Builds pistola |
| [[mods/warframe/rejuvenation.md\|Rejuvenation]] | Comum | Regeneração passiva de HP (squad) | Frames tanky |
| [[mods/warframe/enemy_radar.md\|Enemy Radar]] | Comum | Mostra inimigos no minimapa | QoL / stealth |
| [[mods/warframe/loot_detector.md\|Loot Detector]] | Incomum | Mostra recursos e drops no minimapa | Farm |
| [[mods/warframe/brief_respite.md\|Brief Respite]] | Incomum | Gasto de Energia restaura Shields | Shield-gating builds |
| [[mods/warframe/combat_discipline.md\|Combat Discipline]] | Raro | Kills de aliados +HP; mortes -HP | Builds específicas (suporte) |
| [[mods/warframe/empowered_blades.md\|Empowered Blades]] | Incomum | Status em branca aumentam dano | Syndicate (Steel Meridian) |
| [[mods/warframe/physique.md\|Physique]] | Comum | +HP da squad | Suporte |


## Exilus (Warframe) — Warframe — Segunda Mente


Slot Exilus de Warframe só aceita mods de **mobilidade e utilidade**. Requer **Warframe Exilus Adapter** para desbloquear.

| Mod | Raridade | Efeito |
|---|---|---|
| [[missoes/tipos/rush.md\|Rush]] | Comum | +Velocidade de corrida |
| [[mods/warframe/sprint_boost.md\|Sprint Boost]] | Comum | +Velocidade de sprint |
| [[mods/warframe/handspring.md\|Handspring]] | Comum | -Tempo de recuperação de knockdown |
| [[mods/warframe/mobilize.md\|Mobilize]] | Incomum | +Velocidade de parkour |
| [[mods/warframe/aviator.md\|Aviator]] | Incomum | -Dano recebido enquanto em ar |
| [[mods/warframe/cunning_drift.md\|Cunning Drift]] | Incomum | +Range de habilidades (menor que Stretch) |
| [[mods/warframe/power_drift.md\|Power Drift]] | Incomum | +Strength menor + knockdown resist |
| [[mods/warframe/coaction_drift.md\|Coaction Drift]] | Incomum | Amplifica efeito de Auras na squad |
| [[mods/warframe/vigilante_pursuit.md\|Vigilante Pursuit]] | Incomum | Radar de inimigos |


## 🔗 Relacionados — Warframe — Segunda Mente


| Índice | Relação |
|---|---|
| [[mods/_Mods _Indice.md\|Mods]] | Índice geral — sistema de mods |
| [[mods/especiais/_Mods Especiais _Indice.md\|Mods Especiais]] | Mods Corrupted, Primed, Umbral e Syndicate de warframe |
| [[warframes/_Warframes _Indice.md\|Warframes]] | Frames que equipam estes mods |
| [[mecanicas/sindicatos/_Sindicatos _Indice.md\|Sindicatos]] | Fonte de mods Syndicate e alguns Augments |

----------------------------------------

## Seção: mods\companheiros — Warframe — Segunda Mente

### 📄 arquivo: _Mods Companheiros _Indice.md

# Mods de Companheiros — Índice

> [!quote]
> *"Um companheiro bem modado vale mais que um segundo warframe."*


## 📊 Visão Geral — Warframe — Segunda Mente


Mods de companheiros modificam os **atributos e comportamentos** de Sentinels, Kavats, Kubrows, MOAs e Hounds. Cada tipo de companheiro tem um conjunto de mods exclusivos chamados **Precept Mods** que controlam suas ações autônomas em combate.

**Slots:** 8 slots normais (companheiro) + 10 slots de arma do companheiro
**Capacidade base:** 30 → 60 com Orokin Reactor (companheiro) ou Orokin Catalyst (arma do companheiro)


## Precept Mods — Warframe — Segunda Mente


Precept mods são **instruções comportamentais** — definem o que o companheiro faz autonomamente. Estão ligados a um tipo específico de companheiro e ocupam slots normais.

| Tipo de Precept | Exemplos | Efeito |
|---|---|---|
| **Comportamento ativo** | Assault Mode, Striker | Companheiro ataca inimigos próximos |
| **Comportamento defensivo** | Guardian, Regen | Companheiro protege ou ressuscita o operador |
| **Comportamento de suporte** | Medi-Ray, Pack Leader | Companheiro cura o operador ou a si mesmo |
| **Comportamento de loot** | Vacuum, Fetch | Companheiro atrai itens automaticamente |

> [!tip] Vacuum / Fetch são obrigatórios
> **Vacuum** (Sentinels) e **Fetch** (outros companheiros) atraem itens próximos automaticamente. São os mods de maior impacto de QoL no jogo — considerados quase obrigatórios em qualquer build.


## Mods Universais (qualquer companheiro) — Warframe — Segunda Mente


| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[mods/companheiros/link_health.md\|Link Health]] | Incomum | HP do companheiro escala com HP do operador | Drop geral |
| [[mods/companheiros/link_shields.md\|Link Shields]] | Incomum | Shield do companheiro escala com Shield do operador | Drop geral |
| [[mods/companheiros/link_armor.md\|Link Armor]] | Incomum | Armor do companheiro escala com Armor do operador | Drop geral |
| [[mods/companheiros/animal_instinct.md\|Animal Instinct]] | Incomum | Radar de inimigos e loot no minimapa | Drop geral |
| [[mods/companheiros/primed_animal_instinct.md\|Primed Animal Instinct]] | Primed | Radar — raio muito maior | Baro Ki'Teer |


## Sentinels — Warframe — Segunda Mente


| Mod | Raridade | Tipo | Efeito | Fonte |
|---|---|---|---|---|
| [[mods/companheiros/vacuum.md\|Vacuum]] | Incomum | Precept | Atrai itens próximos automaticamente | Drop geral / mercado |
| [[mods/companheiros/primed_regen.md\|Primed Regen]] | Primed | Precept | Múltiplas ressurreições por missão | Baro Ki'Teer |
| [[mods/companheiros/regen.md\|Regen]] | Raro | Precept | Ressurreição do Sentinel uma vez por missão | Drop geral |
| [[mods/companheiros/guardian.md\|Guardian]] | Raro | Precept | Regenera Shields do operador quando ativado | Drop geral |
| [[mods/companheiros/medi_ray.md\|Medi-Ray]] | Incomum | Precept | Cura o operador periodicamente | Drop geral |
| [[mods/companheiros/striker.md\|Striker]] | Incomum | Precept | Sentinel ataca inimigos próximos | Drop geral |
| [[mods/companheiros/assault_mode.md\|Assault Mode]] | Incomum | Precept | Persegue e ataca alvos ativamente | Drop geral |
| [[mods/companheiros/sweeper.md\|Sweeper]] | Incomum | Arma | Shotgun equipada no Sentinel | Drop geral |
| [[mods/companheiros/calculated_shot.md\|Calculated Shot]] | Raro | Arma | +Crítico da arma do Sentinel | Drop geral |
| [[mods/companheiros/spare_parts.md\|Spare Parts]] | Raro | Loot | Drop de recurso raro ao Sentinel morrer | Drop geral |
| [[mods/companheiros/synth_deconstruct.md\|Synth Deconstruct]] | Incomum | Loot | Drop de orb de saúde ao matar — set Synth | Drop geral |
| [[mods/companheiros/synth_fiber.md\|Synth Fiber]] | Incomum | Defesa | Overshields ao pegar orb de saúde — set Synth | Drop geral |
| [[mods/companheiros/enemy_sense.md\|Enemy Sense]] | Incomum | Utilidade | Radar de inimigos | Drop geral |

> [!note] Sentinels populares
> **Carrier** com Vacuum + Primed Regen é o setup mais comum. **Helios** escaneia inimigos para o Codex automaticamente. **Wyrm** usa Crowd Dispersion para knockback.


## Kavats — Warframe — Segunda Mente


| Mod | Raridade | Tipo | Efeito | Fonte |
|---|---|---|---|---|
| [[mods/companheiros/fetch.md\|Fetch]] | Incomum | Precept | Atrai itens — equivalente ao Vacuum | Drop geral |
| [[mods/companheiros/charm.md\|Charm]] | Raro | Precept | **Smeeta Kavat** — buff aleatório incluindo duplicação de recursos | Drop geral |
| [[mods/companheiros/mischief.md\|Mischief]] | Incomum | Precept | Smeeta — distrai inimigos | Drop geral |
| [[mods/companheiros/tek_enhance.md\|Tek Enhance]] | Incomum | Precept | Smeeta — aumenta duração dos buffs de Charm | Drop geral |
| [[mods/companheiros/sharpened_claws.md\|Sharpened Claws]] | Raro | Precept | **Adarza Kavat** — remove armor ao atacar inimigos | Drop geral |
| [[reflect\|Reflect]] | Raro | Precept | Adarza — reflete dano recebido | Drop geral |
| [[cat_s_eye\|Cat's Eye]] | Raro | Precept | Adarza — +Crit Chance para o operador por buffs | Drop geral |
| [[mods/companheiros/bite.md\|Bite]] | Raro | Combate | +Crítico do Kavat | Drop geral |
| [[mods/companheiros/pack_leader.md\|Pack Leader]] | Incomum | Cura | Finishers do operador curam o companheiro | Drop geral |

> [!tip] Smeeta para Farm
> O buff **Charm** da Smeeta Kavat pode duplicar drops de recursos, orbs de energia e até relíquias abertas. É o companheiro mais usado em sessões de farm intensivo.


## Kubrows — Warframe — Segunda Mente


| Mod | Raridade | Tipo | Efeito | Fonte |
|---|---|---|---|---|
| [[mods/companheiros/fetch.md\|Fetch]] | Incomum | Precept | Atrai itens — equivalente ao Vacuum | Drop geral |
| [[mods/companheiros/maul.md\|Maul]] | Incomum | Precept | **Raksa Kubrow** — +Dano do Kubrow | Drop geral |
| [[protect\|Protect]] | Raro | Precept | Raksa — regenera Shields ao sofrer dano | Drop geral |
| [[howl\|Howl]] | Incomum | Precept | Raksa — amedronta inimigos próximos | Drop geral |
| [[dig\|Dig]] | Raro | Precept | **Sahasa Kubrow** — escava itens e recursos | Drop geral |
| [[mods/companheiros/loyal_companion.md\|Loyal Companion]] | Raro | Precept | Kubrow revive o operador uma vez por missão | Drop geral |
| [[hunt\|Hunt]] | Incomum | Precept | **Sunika Kubrow** — persegue inimigos em fuga | Drop geral |
| [[mods/companheiros/bite.md\|Bite]] | Raro | Combate | +Crítico do Kubrow | Drop geral |
| [[mods/companheiros/pack_leader.md\|Pack Leader]] | Incomum | Cura | Finishers do operador curam o companheiro | Drop geral |


## MOAs — Warframe — Segunda Mente


| Mod | Raridade | Tipo | Efeito | Fonte |
|---|---|---|---|---|
| [[mods/companheiros/fetch.md\|Fetch]] | Incomum | Precept | Atrai itens — equivalente ao Vacuum | Drop geral |
| [[mods/companheiros/security_override.md\|Security Override]] | Incomum | Precept | Hackeia consoles e câmeras automaticamente | Drop Fortuna |
| [[mods/companheiros/thumper.md\|Thumper]] | Incomum | Precept | Derruba inimigos no chão | Drop Fortuna |
| [[mods/companheiros/targeting_receptor.md\|Targeting Receptor]] | Incomum | Precept | +Dano em alvos marcados | Drop Fortuna |
| [[mods/companheiros/anti_grav_array.md\|Anti-Grav Array]] | Incomum | Precept | Suspende inimigos no ar | Drop Fortuna |
| [[shockwave_actuator\|Shockwave Actuator]] | Incomum | Precept | Onda de choque radial ao aterrissar | Drop Fortuna |

> [!note] MOAs modulares
> MOAs são montados em Fortuna com componentes (Brace, Gyro, Loader, Weapon) — o conjunto de precepts disponíveis depende do Gyro selecionado.


## Hounds — Warframe — Segunda Mente


| Mod | Raridade | Tipo | Efeito | Fonte |
|---|---|---|---|---|
| [[mods/companheiros/fetch.md\|Fetch]] | Incomum | Precept | Atrai itens — equivalente ao Vacuum | Drop geral |
| [[mods/companheiros/hound_bite.md\|Hound Bite]] | Incomum | Precept | Aplica status ao morder | Drop Parvos |
| [[mods/companheiros/coda_defiance.md\|Coda Defiance]] | Incomum | Precept | Resistência a efeitos de status | Drop Parvos |
| [[tenacious_bond\|Tenacious Bond]] | Raro | Precept | +Crit Chance das armas ao companheiro estar cheio de HP | Drop Parvos |

> [!note] Hounds modulares
> Hounds são obtidos como subproduto do sistema de Irmãs de Parvos — cada Hound tem precepts determinados pela Irmã que o acompanhava.


## 🔗 Relacionados — Warframe — Segunda Mente


| Índice | Relação |
|---|---|
| [[mods/_Mods _Indice.md\|Mods]] | Índice geral — sistema de mods |
| [[companheiros/_Companheiros _Indice.md\|Companheiros]] | Tipos de companheiros que equipam estes mods |
| [[locais/_Locais _Indice.md\|Locais]] | Fortuna (MOAs, Hounds), Cetus (Kavats, Kubrows) |

----------------------------------------

## Seção: mods\especiais — Warframe — Segunda Mente

### 📄 arquivo: _Mods Especiais _Indice.md

# Mods Especiais — Índice

> [!quote]
> *"Primed para os veteranos. Corrupted para os ousados. Rivens para os obcecados."*


## 📊 Visão Geral — Warframe — Segunda Mente


Mods Especiais são categorias de mods com **origens e mecânicas distintas** das variantes comuns. Representam o topo da progressão de build — mais poderosos, mais raros e mais custosos em capacidade.

| Categoria | Origem | Característica |
|---|---|---|
| **Primed** | Baro Ki'Teer / Nightwave | Versões superiores de mods comuns — mesmo efeito, mais pontos |
| **Umbral** | Quest (The Sacrifice) | Set exclusivo com bônus sinérgico — custo de capacidade muito alto |
| **Corrupted** | Orokin Vault (Derelict) | Dois efeitos opostos — poder alto com penalidade |
| **Syndicate** | Seis Sindicatos | Efeito especial adicional — proc único ao matar |
| **Amalgam** | Drop de inimigos Amalgam | Set mods com bônus exclusivo de mecânica de jogo |
| **Riven** | Sorties / Nightwave | Atributos aleatórios por arma específica |


## Mods Primed — Warframe — Segunda Mente


Versões amplificadas de mods comuns obtidas **exclusivamente de Baro Ki'Teer** (por Ducats + Créditos) em rotação quinzenal, ou de temporadas da **Nightwave**.

> [!important] Rastreie visitas do Baro
> Cada visita de Baro traz um inventário diferente. Mods Primed não voltam necessariamente na próxima visita. Veteranos monitoram o histórico de visitas para saber quando determinado Primed vai reaparecer.

### Primed de Warframe

| Mod | Equivalente Comum | Melhoria | Fonte |
|---|---|---|---|
| [[mods/warframe/primed_vigor.md\|Primed Vigor]] | Vigor | +HP e +Shield muito elevados | Baro Ki'Teer |
| [[mods/warframe/primed_continuity.md\|Primed Continuity]] | Continuity | +Duration muito elevado | Baro Ki'Teer |
| [[mods/warframe/primed_flow.md\|Primed Flow]] | Flow | +Max Energia muito elevado | Baro Ki'Teer |

### Primed de Armas (Primárias)

| Mod | Equivalente Comum | Melhoria | Fonte |
|---|---|---|---|
| [[mods/armas/primed_serration.md\|Primed Serration]] | Serration | +Dano base muito elevado — rifle | Baro Ki'Teer |
| [[mods/armas/primed_cryo_rounds.md\|Primed Cryo Rounds]] | Cryo Rounds | +Frio muito elevado — rifle | Baro Ki'Teer |

### Primed de Armas (Secundárias)

| Mod | Equivalente Comum | Melhoria | Fonte |
|---|---|---|---|
| [[mods/armas/primed_pistol_gambit.md\|Primed Pistol Gambit]] | Pistol Gambit | +Crit Chance muito elevado — pistola | Baro Ki'Teer |
| [[mods/armas/primed_target_cracker.md\|Primed Target Cracker]] | Target Cracker | +Crit Multiplier muito elevado — pistola | Baro Ki'Teer |

### Primed de Armas (Brancas)

| Mod | Equivalente Comum | Melhoria | Fonte |
|---|---|---|---|
| [[mods/armas/primed_pressure_point.md\|Primed Pressure Point]] | Pressure Point | +Dano base muito elevado — branca | Baro Ki'Teer |
| [[mods/armas/primed_fever_strike.md\|Primed Fever Strike]] | Fever Strike | +Tóxico muito elevado — branca | Baro Ki'Teer |

### Primed de Companheiros

| Mod | Equivalente Comum | Melhoria | Fonte |
|---|---|---|---|
| [[mods/companheiros/primed_animal_instinct.md\|Primed Animal Instinct]] | Animal Instinct | Radar de raio muito maior | Baro Ki'Teer |
| [[mods/companheiros/primed_regen.md\|Primed Regen]] | Regen | Múltiplas ressurreições por missão | Baro Ki'Teer |


## Mods Umbral — Warframe — Segunda Mente


Set de três mods obtidos em **The Sacrifice** (quest) e em raids. Têm custo de capacidade muito alto mas se potencializam mutuamente quando dois ou mais estão equipados.

| Mod | Efeito | Bônus de Set (2+ mods) |
|---|---|---|
| [[mods/warframe/umbral_vitality.md\|Umbral Vitality]] | +HP elevado | +HP e +Umbral Damage |
| [[mods/warframe/umbral_intensify.md\|Umbral Intensify]] | +Strength elevado | +Strength e +Umbral Damage |
| [[umbral_fiber\|Umbral Fiber]] | +Armor elevado | +Armor e +Umbral Damage |

> [!note] Slot Umbra (Ω)
> Frames com polaridade Umbra pré-instalada (ex: Excalibur Umbra) reduzem o custo dos mods Umbral pela metade. Outros frames precisam de muitas Formas para viabilizar o set completo.


## Mods Corrupted — Warframe — Segunda Mente


Obtidos em **Orokin Vaults** dentro das missões Orokin Derelict (Deimos). Cada vault exige uma **Dragon Key** específica equipada no companheiro — a chave penaliza o operador enquanto equipada.

| Dragon Key | Penalidade ao Operador |
|---|---|
| Broken Swords | -75% Dano |
| Extinguished Dragon Key | -75% Velocidade de Holster |
| Hobbled Dragon Key | -50% Velocidade de Movimento |
| Bleeding Dragon Key | -75% HP |

> [!tip] Squad de 4 para Vault Run
> Uma squad de 4 pode carregar cada Dragon Key diferente simultaneamente — qualquer membro abre o vault independente de qual key está equipada. Ideal para coletar múltiplos Corrupted por missão.

### Corrupted de Warframe

| Mod | Efeito Positivo | Penalidade | Pilar |
|---|---|---|---|
| [[mods/warframe/blind_rage.md\|Blind Rage]] | +Strength muito alto | -Efficiency | Strength |
| [[mods/warframe/transient_fortitude.md\|Transient Fortitude]] | +Strength alto | -Duration | Strength |
| [[mods/warframe/fleeting_expertise.md\|Fleeting Expertise]] | +Efficiency muito alto | -Duration | Efficiency |
| [[mods/warframe/narrow_minded.md\|Narrow Minded]] | +Duration muito alto | -Range | Duration |
| [[mods/warframe/overextended.md\|Overextended]] | +Range muito alto | -Strength | Range |

### Corrupted de Armas

| Mod | Efeito Positivo | Penalidade | Tipo |
|---|---|---|---|
| [[mods/armas/heavy_caliber.md\|Heavy Caliber]] | +Dano muito alto | -Accuracy | Rifle |
| [[mods/armas/vile_acceleration.md\|Vile Acceleration]] | +Fire Rate muito alto | -Dano base | Rifle |
| [[mods/especiais/vile_precision.md\|Vile Precision]] | -Recoil muito alto | -Fire Rate | Rifle |
| [[mods/armas/critical_delay.md\|Critical Delay]] | +Crit Chance alto | -Fire Rate | Rifle |
| [[mods/especiais/hollow_point.md\|Hollow Point]] | +Crit Multiplier | -Dano base | Rifle |
| [[mods/armas/tainted_mag.md\|Tainted Mag]] | +Magazine Size | -Reload Speed | Rifle |
| [[mods/armas/depleted_reload.md\|Depleted Reload]] | -Reload Time | -Magazine Size | Rifle |
| [[mods/armas/tainted_shell.md\|Tainted Shell]] | +Pellet Count | -Fire Rate | Espingarda |
| [[mods/armas/anemic_agility.md\|Anemic Agility]] | +Fire Rate | -Dano base | Pistola |
| [[mods/armas/spoiled_strike.md\|Spoiled Strike]] | +Dano muito alto | -Attack Speed | Branca |
| [[mods/armas/corrupt_charge.md\|Corrupt Charge]] | +Combo inicial alto | -Duração do Counter | Branca |
| [[mods/armas/drifting_contact.md\|Drifting Contact]] | +Combo Duration | chance de Status | Branca |


## Mods Syndicate — Warframe — Segunda Mente


Exclusivos dos **seis sindicatos principais**. Adicionam um **proc especial** (explosão, buff, efeito) às ações do equipamento além do bônus normal do mod.

> [!note] Aliados e Inimigos
> Cada sindicato tem aliados e inimigos. Mods de sindicatos aliados também ficam disponíveis para compra, mas a custo maior de reputação.

### Aura de Sindicato

| Mod | Sindicato | Efeito |
|---|---|---|
| [[mods/warframe/growing_power.md\|Growing Power]] | Cephalon Suda / New Loka | +Strength ao aplicar Status — Aura |
| [[mods/warframe/empowered_blades.md\|Empowered Blades]] | Steel Meridian | Status em branca aumentam dano — Aura |
| [[mods/warframe/masters_edge.md\|Master's Edge]] | Arbiters of Hexis | +Efficiency de habilidades — Aura |

### Mods de Armas de Sindicato

| Mod | Sindicato | Tipo | Efeito |
|---|---|---|---|
| [[mods/armas/hunter_munitions.md\|Hunter Munitions]] | Steel Meridian | Rifle | Críticos aplicam Slash |
| [[mods/warframe/hunter_adrenaline.md\|Hunter Adrenaline]] | Steel Meridian | Warframe | Dano em HP → Energia |
| [[mods/armas/lethal_torrent.md\|Lethal Torrent]] | Cephalon Suda | Pistola | +Multishot + Fire Rate |
| [[mods/armas/high_voltage.md\|High Voltage]] | Perrin Sequence | Rifle | +Elétrico + proc Elétrico |
| [[mods/armas/thermite_rounds.md\|Thermite Rounds]] | Red Veil | Rifle | +Calor + proc Calor |
| [[mods/armas/frostbite.md\|Frostbite]] | New Loka | Pistola | +Frio + proc Frio |
| [[mods/armas/scorch.md\|Scorch]] | Red Veil | Pistola | +Calor + proc Calor |
| [[mods/armas/hemorrhage.md\|Hemorrhage]] | Steel Meridian | Pistola | Procs de Impact → Slash |
| [[mods/especiais/smite_infusion.md\|Smite Infusion]] | New Loka | Branca | +Radiação + explosão ao matar |
| [[mods/especiais/firewalk.md\|Firewalk]] | Red Veil | Branca | Kills criam rastro de fogo |
| [[mods/especiais/winds_of_purity.md\|Winds of Purity]] | Arbiters of Hexis | Branca | Kills de finisher → Energia e HP |
| [[mods/especiais/entropy_burst.md\|Entropy Burst]] | Cephalon Suda | Branca | Kills disparam explosão de Radiação |
| [[mods/especiais/justice_blades.md\|Justice Blades]] | Arbiters of Hexis | Branca | Kills têm chance de explosão |


## Mods Amalgam — Warframe — Segunda Mente


Obtidos de **inimigos Amalgam** (Jupiter — Ropalolyst, Disruption) e de missões especiais. São **Set Mods** — bônus extras ao equipar dois ou mais da mesma série.

| Mod | Efeito | Bônus de Set |
|---|---|---|
| [[amalgam_serration\|Amalgam Serration]] | +Dano base de rifle (menor que Serration normal) | +Velocidade de Sprint | Junction Marte — não negociável |
| [[amalgam_barrel_diffusion\|Amalgam Barrel Diffusion]] | +Multishot de pistola | +Dodge Speed | Drop Amalgam |
| [[amalgam_organ_shatter\|Amalgam Organ Shatter]] | +Crit Multiplier branca | -Charge Attack Time | Drop Amalgam |
| [[amalgam_daikyu_target_acquired\|Amalgam Daikyu Target Acquired]] | Exclusivo Daikyu | Sliding aumenta dano | Drop Amalgam |


## Rivens — Warframe — Segunda Mente


Mods com **atributos aleatórios vinculados a uma arma específica**. Representam o topo da customização de armas mas com grande variação de valor.

| Aspecto | Detalhe |
|---|---|
| **Origem** | Sorties (recompensa final), Nightwave, trades |
| **Tipos** | Rifle · Pistola · Shotgun · Melee · Archgun |
| **Atributos** | 2–4 positivos + 0–1 negativo, aleatórios |
| **Unveil** | Riven velado exige completar desafio antes de revelar a arma |
| **Disposition** | Escala 1–5 estrelas por arma — define o teto dos atributos rolados |
| **Reroll** | Usa Kuva para rerollar — custo cresce a cada roll (550 → 4.000 Kuva) |
| **Troca** | Altamente negociáveis no Trade Chat — preço varia por arma e atributos |

### Disposition e Disponibilidade

| Disposition | Estrelas | Significado |
|---|---|---|
| Very High | ●●●●● | Arma pouco usada — atributos muito altos |
| High | ●●●●○ | Arma moderadamente usada |
| Medium | ●●●○○ | Equilíbrio |
| Low | ●●○○○ | Arma popular — atributos moderados |
| Very Low | ●○○○○ | Arma meta dominante — atributos fracos |

> [!warning] Rebalanceamento periódico
> A DE ajusta as Dispositions com cada update major. Nerfs em armas populares podem reduzir drasticamente o valor e eficácia de Rivens existentes.


## 🔗 Relacionados — Warframe — Segunda Mente


| Índice | Relação |
|---|---|
| [[mods/_Mods _Indice.md\|Mods]] | Índice geral — sistema de mods |
| [[mods/warframe/_Mods Warframe _Indice.md\|Mods de Warframe]] | Primed e Corrupted de warframe em contexto de build |
| [[mods/armas/_Mods Armas _Indice.md\|Mods de Armas]] | Primed e Corrupted de armas em contexto de build |
| [[mecanicas/sindicatos/_Sindicatos _Indice.md\|Sindicatos]] | Como ganhar reputação para comprar mods Syndicate |
| [[mecanicas/_Mecanicas _Indice.md\|Mecânicas]] | Sorties — fonte de Rivens |

----------------------------------------

## Seção: recursos — Warframe — Segunda Mente

### 📄 arquivo: _Recursos _Indice.md

# Recursos — Índice

> [!quote]
> *"O Sistema Origem é rico em materiais. Saber onde procurar é metade da batalha."*


## 📊 Visão Geral — Warframe — Segunda Mente


Recursos são materiais coletados em missões e usados na **Fundição** para craftar Warframes, armas, componentes e itens de progressão. Cada recurso tem origem específica — planeta, facção ou modo de jogo — e uma raridade que determina com que frequência dropa.

O loop de progressão depende diretamente dos recursos: toda peça craftável exige uma combinação específica, e receitas avançadas frequentemente pedem materiais de várias regiões diferentes. Recursos são coletados automaticamente ao passar sobre eles no mapa. Cada planeta tem um conjunto de recursos nativos com drop mais frequente, mais um pool de raros compartilhados. Alguns recursos especiais só existem em sistemas específicos — Open Worlds, Nightwave, Sorties — e não aparecem em missões convencionais.


## Como Farmar — Warframe — Segunda Mente


Recursos dropam de inimigos, containers e lockers nos mapas de missão. Missões de **Survival** e **Defense** são as mais eficientes por volume — quanto mais tempo dentro, mais inimigos spawnam e mais material acumula.

| Método | Efeito |
|---|---|
| **[[warframes/regular/nekros.md\|Nekros]] (Desecrate)** | Rola drops adicionais em cadáveres — duplica efetivamente a taxa de drop |
| **[[warframes/regular/hydroid.md\|Hydroid]] (Pilfering Swarm)** | Chance de drop extra em inimigos afetados pelo Tentacle Swarm |
| **[[warframes/regular/khora.md\|Khora]] (Pilfering Strangledome)** | Chance de drop extra em inimigos presos no Strangledome |
| **Resource Booster** | Dobra todos os recursos coletados por 3 ou 7 dias |
| **Resource Drop Chance Booster** | Aumenta a chance de inimigos droparem recursos |
| **Smeeta Kavat (Charm)** | Buff aleatório que pode dobrar recursos coletados temporariamente |

O setup padrão de farm eficiente combina Nekros + Resource Booster + Smeeta Kavat — podendo quadruplicar o volume coletado por corrida.


## Categorias de Raridade — Warframe — Segunda Mente


| Raridade | Descrição |
|---|---|
| **Comum** | Drop abundante em quase qualquer missão do planeta de origem. Pode exigir grandes quantidades em crafts avançados. |
| **Incomum** | Drop moderado — presente no planeta certo, mas em volume menor. Gargalo em fases intermediárias. |
| **Raro** | Drop escasso. Requer farm dedicado no planeta ou missão certa, frequentemente com Warframe de loot. |
| **Especial** | Não dropa em missões convencionais. Obtido via Nightwave, Sorties, Void Relics ou eventos sazonais. |


## Recursos Comuns — Warframe — Segunda Mente


| Recurso | Planeta / Origem | Método | Notas |
|---|---|---|---|
| [[recursos/raridades/comum/alloy_plate.md\|Alloy Plate]] | Vênus, Júpiter, Sedna, Ceres, Phobos | Drop geral | Um dos recursos mais abundantes do jogo |
| [[recursos/raridades/comum/circuits.md\|Circuits]] | Vênus, Ceres | Containers e inimigos | — |
| [[recursos/raridades/comum/detonite_ampule.md\|Detonite Ampule]] | Qualquer planeta Grineer | Drop de inimigos | Acumulado para craftar Detonite Injector (pesquisa de Clã) |
| [[recursos/raridades/comum/ferrite.md\|Ferrite]] | Mercúrio, Terra, Netuno, Void | Drop geral | Essencial para builds iniciais |
| [[recursos/raridades/comum/fieldron_sample.md\|Fieldron Sample]] | Qualquer planeta Corpus | Drop de inimigos | Acumulado para craftar Fieldron (pesquisa de Clã) |
| [[recursos/raridades/comum/mutagen_sample.md\|Mutagen Sample]] | Eris, Deimos, Orokin Derelict | Drop Infestado | Acumulado para craftar Mutagen Mass (pesquisa de Clã) |
| [[recursos/raridades/comum/nano_spores.md\|Nano Spores]] | Saturno, Netuno, Eris, Deimos | Drop geral | Acumula rápido em Survival |
| [[recursos/raridades/comum/polymer_bundle.md\|Polymer Bundle]] | Mercúrio, Vênus, Urano | Containers e inimigos | — |
| [[recursos/raridades/comum/rubedo.md\|Rubedo]] | Phobos, Terra, Sedna, Europa, Void | Containers e lockers | — |
| [[recursos/raridades/comum/salvage.md\|Salvage]] | Marte, Júpiter, Sedna | Drop geral | Necessário em grande volume para Vauban e pesquisas de Clã |


## Recursos Incomuns — Warframe — Segunda Mente


| Recurso | Planeta / Origem | Método | Notas |
|---|---|---|---|
| [[recursos/raridades/incomum/hexenon.md\|Hexenon]] | Júpiter | Inimigos Amalgam e Gas City | Usado para craftar Wisp e componentes de Clã |
| [[recursos/raridades/incomum/oxium.md\|Oxium]] | Júpiter | Drop de Oxium Osprey | Inimigo se autodestrói se não morto rápido — farm exige atenção |
| [[recursos/raridades/incomum/plastids.md\|Plastids]] | Saturno, Urano, Phobos, Plutão, Eris | Drop geral | Essencial para Nidus e frames de temática Infestada |


## Recursos Raros — Warframe — Segunda Mente


| Recurso | Planeta / Origem | Método | Notas |
|---|---|---|---|
| [[recursos/raridades/raro/argon_crystal.md\|Argon Crystal]] | Void | Drop geral | **Decai em 24h** após encerrar sessão — farmear próximo do uso |
| [[recursos/raridades/raro/control_module.md\|Control Module]] | Europa, Netuno | Bosses e containers | — |
| [[recursos/raridades/raro/cryotic.md\|Cryotic]] | Qualquer planeta | Missões Excavation | Exclusivo de Excavation — 100 por escavador completado |
| [[recursos/raridades/raro/gallium.md\|Gallium]] | Marte, Urano | Bosses e containers | — |
| [[recursos/raridades/raro/kuva.md\|Kuva]] | Fortaleza Kuva | Siphon / Flood | Usada para rolar e melhorar Riven Mods |
| [[recursos/raridades/raro/morphics.md\|Morphics]] | Mercúrio, Marte, Phobos, Europa | Drop de bosses | — |
| [[recursos/raridades/raro/neural_sensors.md\|Neural Sensors]] | Júpiter, Fortaleza Kuva | Drop do boss Alad V | — |
| [[recursos/raridades/raro/neurodes.md\|Neurodes]] | Terra, Eris, Lua, Deimos | Drop de bosses | — |
| [[recursos/raridades/raro/nitain_extract.md\|Nitain Extract]] | Nightwave, Ghoul Purge | Recompensa de temporada | Não dropa em missões normais |
| [[recursos/raridades/raro/orokin_cell.md\|Orokin Cell]] | Saturno, Ceres, Deimos | Drop de bosses | Frequente gargalo em crafts de Warframes Prime |
| [[recursos/raridades/raro/tellurium.md\|Tellurium]] | Urano, missões Archwing | Drop de inimigos | Melhor farmado em Archwing Interception em Urano |


## Recursos Especiais — Warframe — Segunda Mente


Itens obtidos via sistemas específicos — não dropam em farm convencional. Representam progressão vertical: aumentam poder ou flexibilidade do equipamento sem serem consumidos em receitas de crafting comuns.

| Recurso | Origem | Função |
|---|---|---|
| [[recursos/raridades/especial/forma.md\|Forma]] | Relíquias do Void, Sorties, Nightwave | Reseta rank e adiciona polaridade ao equipamento |
| [[recursos/raridades/especial/aura_forma.md\|Aura Forma]] | Nightwave, Sorties | Permite qualquer polaridade no slot de Aura |
| [[recursos/raridades/especial/umbral_forma.md\|Umbral Forma]] | Nightwave, end-game | Slot Umbral — compatível com mods da série Umbra |
| [[recursos/raridades/especial/orokin_catalyst.md\|Orokin Catalyst]] | Sorties, Alerts, Login Reward | Dobra capacidade de mod de armas ("potato azul") |
| [[recursos/raridades/especial/orokin_reactor.md\|Orokin Reactor]] | Sorties, Alerts, Login Reward | Dobra capacidade de mod de Warframes ("potato dourado") |
| [[recursos/raridades/especial/exilus_adapter.md\|Exilus Adapter]] | Sindicatos, Nightwave, Sorties | Desbloqueia slot Exilus em armas |
| [[recursos/raridades/especial/warframe_exilus_adapter.md\|Warframe Exilus Adapter]] | Sindicatos, Nightwave | Desbloqueia slot Exilus em Warframes |
| [[recursos/raridades/especial/endo.md\|Endo]] | Arbitrations, Ayatan Sculptures, Missões | Moeda para rankear mods |
| [[recursos/raridades/especial/ayatan_sculpture.md\|Ayatan Sculpture]] | Missões aleatórias, Maroo's Bazaar | Convertida em Endo ou usada como decoração |
| [[recursos/raridades/especial/ayatan_amber_star.md\|Ayatan Amber Star]] | Drop aleatório em missões | Inserida em Sculptures para aumentar valor em Endo |
| [[recursos/raridades/especial/ayatan_cyan_star.md\|Ayatan Cyan Star]] | Drop aleatório em missões | Inserida em Sculptures para aumentar valor em Endo |
| [[recursos/raridades/especial/void_traces.md\|Void Traces]] | Missões de Void Fissure | Refina Relíquias do Void — aumenta raridade das recompensas |
| [[recursos/raridades/especial/archon_shard_teal.md\|Archon Shard (Teal)]] | Archon Hunts semanais | Empowerment permanente — atributo de habilidade |
| [[recursos/raridades/especial/archon_shard_crimson.md\|Archon Shard (Crimson)]] | Archon Hunts semanais | Empowerment permanente — atributo de força/vida |
| [[recursos/raridades/especial/archon_shard_azure.md\|Archon Shard (Azure)]] | Archon Hunts semanais | Empowerment permanente — atributo de energia/escudo |
| [[recursos/raridades/especial/archon_shard_amber.md\|Archon Shard (Amber)]] | Archon Hunts semanais | Empowerment permanente — atributo de eficiência/duração |
| [[recursos/raridades/especial/archon_shard_topaz.md\|Archon Shard (Topaz)]] | Archon Hunts semanais | Empowerment permanente — atributo de alcance |
| [[recursos/raridades/especial/archon_shard_violet.md\|Archon Shard (Violet)]] | Archon Hunts semanais | Empowerment permanente — atributo combinado |
| [[recursos/raridades/especial/riven_mod.md\|Riven Mod]] | Sorties, Nightwave | Mod com atributos aleatórios vinculado a uma arma específica |
| [[recursos/raridades/especial/orokin_ducats.md\|Orokin Ducats]] | Troca de peças Prime (quiosque de Baro) | Moeda exclusiva de Baro Ki'Teer — sem outra fonte |
| [[recursos/raridades/especial/aya.md\|Aya]] | Drop aleatório em missões regulares | Usada no sistema Prime Resurgence |
| [[recursos/raridades/especial/regal_aya.md\|Regal Aya]] | Compra com Platinum | Acesso imediato a qualquer item Prime Resurgence |
| [[recursos/raridades/especial/cephalon_fragment.md\|Cephalon Fragment]] | Exploração de planetas | Revela lore ao completar conjuntos por planeta |


## Recursos de Open Worlds — Warframe — Segunda Mente


Cada Open World tem ecossistema próprio — coletados por coleta manual, mineração, pesca ou drops de inimigos exclusivos. Usados para reputação com sindicatos locais e crafting de equipamentos exclusivos de cada mundo.


### Planícies de Eidolon (Terra)
*Sindicato: Ostron (Cetus) · Ferramentas: Nosam Cutter (mineração), Fishing Spear (pesca)*

| Recurso | Raridade | Método | Notas |
|---|---|---|---|
| [[recursos/open_worlds/eidolon/iradite.md\|Iradite]] | Comum | Coleta em campo | Alta concentração à noite |
| [[recursos/open_worlds/eidolon/grokdrul.md\|Grokdrul]] | Comum | Containers Grineer | Espalhados pelo mapa |
| [[recursos/open_worlds/eidolon/nistlepod.md\|Nistlepod]] | Comum | Plantas | Comum em toda a planície |
| [[recursos/open_worlds/eidolon/maprico.md\|Maprico]] | Comum | Plantas | Afloramentos rochosos |
| [[recursos/open_worlds/eidolon/coprite.md\|Coprite]] | Comum | Mineração | Minério básico |
| [[recursos/open_worlds/eidolon/fersteel.md\|Fersteel]] | Comum | Mineração | Minério básico |
| [[recursos/open_worlds/eidolon/intact_sentient_core.md\|Intact Sentient Core]] | Comum | Vomvalysts | Drop básico de Sentient pequeno |
| [[recursos/open_worlds/eidolon/murkray_liver.md\|Murkray Liver]] | Comum | Pesca — Murkray | — |
| [[recursos/open_worlds/eidolon/murkray_bladder.md\|Murkray Bladder]] | Comum | Pesca — Murkray | — |
| [[recursos/open_worlds/eidolon/sharrac_tegmen.md\|Sharrac Tegmen]] | Comum | Pesca — Sharrac | — |
| [[recursos/open_worlds/eidolon/yogwun_stomach.md\|Yogwun Stomach]] | Comum | Pesca — Yogwun | — |
| [[recursos/open_worlds/eidolon/karkina_antenna.md\|Karkina Antenna]] | Comum | Pesca — Karkina | — |
| [[recursos/open_worlds/eidolon/tralok_eyes.md\|Tralok Eyes]] | Comum | Pesca — Tralok | — |
| [[recursos/open_worlds/eidolon/ruks_claw.md\|Ruk's Claw]] | Incomum | Plantas | Encostas e terreno elevado |
| [[recursos/open_worlds/eidolon/lunar_pitcher.md\|Lunar Pitcher]] | Incomum | Plantas | Perto de ruínas |
| [[recursos/open_worlds/eidolon/azurite.md\|Azurite]] | Incomum | Mineração | — |
| [[recursos/open_worlds/eidolon/ferros.md\|Ferros]] | Incomum | Mineração | — |
| [[recursos/open_worlds/eidolon/pyrol.md\|Pyrol]] | Incomum | Mineração | — |
| [[recursos/open_worlds/eidolon/exceptional_sentient_core.md\|Exceptional Sentient Core]] | Incomum | Vomvalysts | Versão superior do Core |
| [[recursos/open_worlds/eidolon/cuthol_tendon.md\|Cuthol Tendon]] | Incomum | Pesca — Cuthol | — |
| [[recursos/open_worlds/eidolon/norg_brain.md\|Norg Brain]] | Incomum | Pesca — Norg | — |
| [[recursos/open_worlds/eidolon/cetus_wisp.md\|Cetus Wisp]] | Raro | Coleta em campo | Flutua perto da água — exclusivamente à noite |
| [[recursos/open_worlds/eidolon/auron.md\|Auron]] | Raro | Mineração | — |
| [[recursos/open_worlds/eidolon/devar.md\|Devar]] | Raro | Mineração | — |
| [[recursos/open_worlds/eidolon/flawless_sentient_core.md\|Flawless Sentient Core]] | Raro | Vomvalysts | — |
| [[recursos/open_worlds/eidolon/radiant_sentient_core.md\|Radiant Sentient Core]] | Raro | Vomvalysts | Versão mais rara |
| [[recursos/open_worlds/eidolon/eidolon_shard.md\|Eidolon Shard]] | Raro | Teralyst | Progressão do Operator |
| [[recursos/open_worlds/eidolon/brilliant_eidolon_shard.md\|Brilliant Eidolon Shard]] | Raro | Gantulyst | Versão superior |
| [[recursos/open_worlds/eidolon/radiant_eidolon_shard.md\|Radiant Eidolon Shard]] | Raro | Hydrolyst | Versão mais poderosa |
| [[recursos/open_worlds/eidolon/breath_of_the_eidolon.md\|Breath of the Eidolon]] | Raro | Todos os Eidolons | Crafting avançado |
| [[recursos/open_worlds/eidolon/mawfish_bones.md\|Mawfish Bones]] | Raro | Pesca — Mawfish | Peixe raro |
| [[recursos/open_worlds/eidolon/glappid_scale.md\|Glappid Scale]] | Raro | Pesca — Glappid | Peixe de isca especial |


### Orbe Vallis (Vênus)
*Sindicato: Solaris United (Fortuna) · Ferramentas: Mining Laser (mineração), Fishing Spear (pesca)*

| Recurso | Raridade | Método | Notas |
|---|---|---|---|
| [[recursos/open_worlds/orbe_vallis/venerdo.md\|Venerdo]] | Comum | Coleta em campo | Espalhado pela Vallis |
| [[recursos/open_worlds/orbe_vallis/gorgaricus_spore.md\|Gorgaricus Spore]] | Comum | Coleta em campo | Fungos específicos |
| [[recursos/railjack/aucrumite.md\|Aucrumite]] | Comum | Mineração | Minério básico |
| [[recursos/railjack/coprun.md\|Coprun]] | Comum | Mineração | Minério básico |
| [[recursos/open_worlds/orbe_vallis/training_debt_bond.md\|Training Debt-Bond]] | Comum | Bounties (Fortuna) | Nível mais baixo de Debt-Bond |
| [[recursos/open_worlds/orbe_vallis/tromyzon_fragment.md\|Tromyzon Fragment]] | Comum | Pesca — Tromyzon | Servofish comum |
| [[recursos/open_worlds/orbe_vallis/charamote_shard.md\|Charamote Shard]] | Comum | Pesca — Charamote | Servofish comum |
| [[recursos/open_worlds/orbe_vallis/thermal_sludge.md\|Thermal Sludge]] | Incomum | Containers Corpus | — |
| [[recursos/open_worlds/orbe_vallis/hespazym_alloy.md\|Hespazym Alloy]] | Incomum | Mineração | — |
| [[recursos/open_worlds/orbe_vallis/nyth.md\|Nyth]] | Incomum | Mineração | — |
| [[recursos/open_worlds/orbe_vallis/sentirum.md\|Sentirum]] | Incomum | Mineração | — |
| [[recursos/open_worlds/orbe_vallis/gyromag_systems.md\|Gyromag Systems]] | Incomum | Coolant Raknoids | Drop de Raknoid menor |
| [[recursos/open_worlds/orbe_vallis/shelter_debt_bond.md\|Shelter Debt-Bond]] | Incomum | Bounties (Fortuna) | — |
| [[recursos/open_worlds/orbe_vallis/medical_debt_bond.md\|Medical Debt-Bond]] | Incomum | Bounties (Fortuna) | — |
| [[recursos/open_worlds/orbe_vallis/synathid_casing.md\|Synathid Casing]] | Incomum | Pesca — Synathid | — |
| [[recursos/open_worlds/orbe_vallis/scrubber_exa_brain.md\|Scrubber Exa Brain]] | Incomum | Pesca — Scrubber Exa | — |
| [[recursos/open_worlds/orbe_vallis/echowinder_shell.md\|Echowinder Shell]] | Incomum | Pesca — Echowinder | — |
| [[recursos/open_worlds/orbe_vallis/amarast.md\|Amarast]] | Raro | Mineração | — |
| [[recursos/open_worlds/orbe_vallis/marquise_thyst.md\|Marquise Thyst]] | Raro | Mineração | — |
| [[recursos/open_worlds/orbe_vallis/calda_toroid.md\|Calda Toroid]] | Raro | Inimigos — Enrichment Labs | Alta demanda para builds de Mech |
| [[recursos/open_worlds/orbe_vallis/crisma_toroid.md\|Crisma Toroid]] | Raro | Inimigos — Temple of Profit | Alta demanda para builds de Mech |
| [[recursos/open_worlds/orbe_vallis/sola_toroid.md\|Sola Toroid]] | Raro | Inimigos — Spaceport | Alta demanda para builds de Mech |
| [[recursos/open_worlds/orbe_vallis/vega_toroid.md\|Vega Toroid]] | Raro | Thermia Fractures | Alta demanda para builds de Mech |
| [[recursos/open_worlds/orbe_vallis/atmo_systems.md\|Atmo Systems]] | Raro | Exploiter Orb | — |
| [[recursos/open_worlds/orbe_vallis/repeller_systems.md\|Repeller Systems]] | Raro | Exploiter Orb | Recompensa principal do Exploiter |
| [[recursos/open_worlds/orbe_vallis/advances_debt_bond.md\|Advances Debt-Bond]] | Raro | Bounties (Fortuna) | — |
| [[recursos/open_worlds/orbe_vallis/familial_debt_bond.md\|Familial Debt-Bond]] | Raro | Bounties (Fortuna) | Nível mais raro de Debt-Bond |
| [[recursos/open_worlds/orbe_vallis/recaster_mucus.md\|Recaster Mucus]] | Raro | Pesca — Recaster | — |
| [[recursos/open_worlds/orbe_vallis/sapcaddy_bladder.md\|Sapcaddy Bladder]] | Raro | Pesca — Sapcaddy | — |


### Câmbion Drift (Deimos)
*Sindicato: Entrati (Necralisk) · Ferramentas: Sunpoint Plasma Drill (mineração), Fishing Spear Infested (pesca)*

| Recurso | Raridade | Método | Notas |
|---|---|---|---|
| [[recursos/open_worlds/cambion_drift/mytocardin.md\|Mytocardin]] | Comum | Coleta em campo | Plantas Infestadas |
| [[recursos/open_worlds/cambion_drift/embolos_spore.md\|Embolos Spore]] | Comum | Coleta em campo | Formações Infestadas |
| [[recursos/open_worlds/cambion_drift/sporulate_sac.md\|Sporulate Sac]] | Comum | Inimigos Infestados | Drop geral |
| [[recursos/open_worlds/cambion_drift/thaumica.md\|Thaumica]] | Comum | Mineração | Minério básico |
| [[recursos/open_worlds/cambion_drift/ganglion.md\|Ganglion]] | Comum | Carnis / Carnis Rex | — |
| [[recursos/open_worlds/cambion_drift/bile.md\|Bile]] | Comum | Jugulus e Infestados | — |
| [[recursos/open_worlds/zariman/vitreospina_fillet.md\|Vitreospina Fillet]] | Comum | Pesca — Vitreospina | — |
| [[recursos/open_worlds/zariman/glutinox_fillet.md\|Glutinox Fillet]] | Comum | Pesca — Glutinox | — |
| [[recursos/open_worlds/cambion_drift/longwinder_fillet.md\|Longwinder Fillet]] | Comum | Pesca — Longwinder | — |
| [[recursos/open_worlds/cambion_drift/infested_nacelle.md\|Infested Nacelle]] | Incomum | Containers / Inimigos | — |
| [[recursos/open_worlds/cambion_drift/pustulite.md\|Pustulite]] | Incomum | Containers / Inimigos | — |
| [[recursos/open_worlds/cambion_drift/lucent_terrogel.md\|Lucent Terrogel]] | Incomum | Mineração | — |
| [[recursos/open_worlds/cambion_drift/pheromones.md\|Pheromones]] | Incomum | Resíduos de Fass / Vome | Poças no campo — ciclo dia/noite |
| [[recursos/open_worlds/cambion_drift/cabochon_embolos.md\|Cabochon Embolos]] | Incomum | Jugulus | — |
| [[recursos/open_worlds/cambion_drift/bracoid.md\|Bracoid]] | Incomum | Carnis | — |
| [[recursos/open_worlds/cambion_drift/duroid_fillet.md\|Duroid Fillet]] | Incomum | Pesca — Duroid | — |
| [[recursos/open_worlds/cambion_drift/flagellocanth_fillet.md\|Flagellocanth Fillet]] | Incomum | Pesca — Flagellocanth | — |
| [[recursos/open_worlds/cambion_drift/trabeculum.md\|Trabeculum]] | Raro | Mineração | — |
| [[recursos/open_worlds/cambion_drift/pustulant_cerebrum.md\|Pustulant Cerebrum]] | Raro | Jugulus Rex | — |
| [[recursos/open_worlds/cambion_drift/namalon.md\|Namalon]] | Raro | Necramechs / Iso Vault | Essencial para crafting de Necramech |
| [[recursos/open_worlds/cambion_drift/lobotriscid_fillet.md\|Lobotriscid Fillet]] | Raro | Pesca — Lobotriscid | — |
| [[recursos/open_worlds/zariman/chondricord_fillet.md\|Chondricord Fillet]] | Raro | Pesca — Chondricord | — |
| [[recursos/open_worlds/cambion_drift/cryptosuctus_fillet.md\|Cryptosuctus Fillet]] | Raro | Pesca — Cryptosuctus | Peixe raro |


### Duviri
*Sindicato: Kaithe (Drifter's Camp)*

| Recurso | Raridade | Método | Notas |
|---|---|---|---|
| [[recursos/open_worlds/duviri/pathos_clamp.md\|Pathos Clamp]] | Comum | Missões, exploração, bosses | Principal recurso do Duviri — crafta frames e armas exclusivos |
| [[recursos/open_worlds/duviri/cavaleros_burden.md\|Cavalero's Burden]] | Raro | Drop de bosses do circuito | Usado em trocas com Cavalero |
| [[recursos/open_worlds/duviri/kullervo_bane.md\|Kullervo's Bane]] | Raro | Boss Kullervo | Drop específico do encontro |


### Zariman Ten Zero
*Sindicato: The Holdfasts (Chrysalith) · Ferramentas: Fishing Spear Void (pesca)*

| Recurso | Raridade | Método | Notas |
|---|---|---|---|
| [[recursos/open_worlds/zariman/voidplume_pinion.md\|Voidplume Pinion]] | Comum | Coleta em campo | — |
| [[recursos/open_worlds/zariman/voidplume_quill.md\|Voidplume Quill]] | Comum | Coleta em campo | — |
| [[recursos/open_worlds/zariman/chondricord_fillet.md\|Chondricord Fillet]] | Comum | Pesca — Chondricord | — |
| [[recursos/open_worlds/zariman/glutinox_fillet.md\|Glutinox Fillet]] | Comum | Pesca — Glutinox | — |
| [[recursos/open_worlds/zariman/voidplume_crest.md\|Voidplume Crest]] | Incomum | Coleta em campo / missões | — |
| [[recursos/open_worlds/zariman/voidplume_drift.md\|Voidplume Drift]] | Incomum | Coleta em campo / missões | — |
| [[recursos/open_worlds/eidolon/mawfish_bones.md\|Mawfish Bones]] | Incomum | Pesca — Mawfish | — |
| [[recursos/open_worlds/zariman/vitreospina_fillet.md\|Vitreospina Fillet]] | Incomum | Pesca — Vitreospina | — |
| [[recursos/open_worlds/zariman/voidplume_down.md\|Voidplume Down]] | Raro | Missões / Void Angels | — |
| [[recursos/open_worlds/zariman/voidplume_wisp.md\|Voidplume Wisp]] | Raro | Missões / Void Angels | — |
| [[recursos/open_worlds/zariman/voidplume_intact.md\|Voidplume Intact]] | Raro | Drop de Void Angels | Muito raro — requer derrotar Void Angel |


### Railjack (Proximas)
*Recursos minerados de asteroides — usados para craftar e atualizar componentes da nave.*

| Recurso | Raridade | Proxima | Notas |
|---|---|---|---|
| [[recursos/railjack/asterite.md\|Asterite]] | Comum | Todas | Recurso universal — base de quase todo crafting Railjack |
| [[recursos/railjack/pustrels.md\|Pustrels]] | Comum | Earth Proxima | — |
| [[recursos/railjack/coprun.md\|Coprun]] | Comum | Earth Proxima | — |
| [[recursos/railjack/lucum.md\|Lucum]] | Comum | Earth Proxima | — |
| [[recursos/railjack/aucrumite.md\|Aucrumite]] | Comum | Earth / Venus Proxima | — |
| [[recursos/railjack/fresnite.md\|Fresnite]] | Comum | Venus Proxima | — |
| [[recursos/railjack/heciphron.md\|Heciphron]] | Incomum | Earth / Mercury Proxima | — |
| [[recursos/railjack/isos.md\|Isos]] | Incomum | Deimos Proxima | — |
| [[recursos/railjack/radian_sentirum.md\|Radian Sentirum]] | Incomum | Venus Proxima | — |
| [[recursos/railjack/carbides.md\|Carbides]] | Incomum | Jupiter Proxima | — |
| [[recursos/railjack/noctrul.md\|Noctrul]] | Incomum | Saturn Proxima | — |
| [[recursos/railjack/goblite_tears.md\|Goblite Tears]] | Incomum | Neptune Proxima | — |
| [[recursos/railjack/adramal_alloy.md\|Adramal Alloy]] | Raro | Saturn Proxima | — |
| [[recursos/railjack/gallos_rod.md\|Gallos Rod]] | Raro | Veil Proxima | — |
| [[recursos/railjack/magnum_khra.md\|Magnum Khra]] | Raro | Veil Proxima | Recurso mais raro do Railjack |


## 🔗 Relacionados — Warframe — Segunda Mente


| Sistema | Índice |
|---|---|
| Warframes de farm (Nekros, Hydroid, Khora) | [[warframes/_Warframes _Indice.md\|Warframes]] |
| Locais de coleta por planeta | [[locais/_Locais _Indice.md\|Locais]] |
| Missões eficientes por tipo (Survival, Excavation) | [[missoes/_Missoes _Indice.md\|Missões]] |
| Sindicatos dos Open Worlds | [[mecanicas/sindicatos/_Sindicatos _Indice.md\|Sindicatos]] |
| Mecânicas de Boosters e Nightwave | [[mecanicas/_Mecanicas _Indice.md\|Mecânicas]] |


## 💡 Curiosidades — Warframe — Segunda Mente


- Argon Crystal é o único recurso perecível do jogo — sua mecânica de decaimento foi adicionada para forçar o uso logo após o farm.
- Nitain Extract foi por muito tempo o recurso mais odiado da comunidade — obtido apenas via Nightwave ou eventos de tempo limitado.
- Forma foi inicialmente não-craftável — era apenas recompensa de missão. A receita craftável foi adicionada após pressão da comunidade.
- Orokin Cell é frequentemente o gargalo de builds de Warframes Prime — necessária em grande quantidade e com drop concentrado em apenas alguns planetas.
- Tellurium tem uma das piores taxas de drop do jogo convencional — missões Archwing em Urano são virtualmente a única fonte eficiente.
- Kuva foi introduzida com o sistema de Riven Mods — tornou a Fortaleza Kuva, antes irrelevante no end-game, em destino regular de farm.
- Toroids na Orbe Vallis eram notoriamente difíceis no lançamento — a comunidade desenvolveu estratégias específicas de farm em cavernas com alert level máximo.
- Oxium Osprey foi inimigo infame por anos — o Osprey se autodestrói se não morto rápido, forçando a comunidade a desenvolver técnicas dedicadas para matar o grupo inteiro antes da explosão.

----------------------------------------
