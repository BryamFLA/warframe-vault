---
title: Warframe — Segunda Mente
tipo: home
tags:
  - home
  - index
  - warframe
  - guia-ia
  - agente
jogo: Warframe
produtora: Digital Extremes
distribuidora: Digital Extremes
plataformas:
  - PC
  - PlayStation 4
  - PlayStation 5
  - Xbox One
  - Xbox Series X/S
  - Nintendo Switch
modelo: free-to-play
genero:
  - third-person shooter
  - action RPG
  - looter shooter
lancamento: 2013-03-25
modo: multiplayer cooperativo (1–4 jogadores)
motor: Evolution Engine
site: https://www.warframe.com
wiki: https://wiki.warframe.com
idioma: pt-BR
arquivo_raiz: true
autossuficiente: true
descricao: Arquivo único de apresentação e consulta do vault Warframe — Segunda Mente. Contém a visão geral do projeto, o protocolo operacional para agentes de IA e o dump consolidado de todo o conteúdo do vault.
atualizado: 2026-09-08
---

# 🧠 Warframe — Segunda Mente

> [!quote]
> *"O Tenno não esquece. O Tenno organiza."*

---

## ⚡ Leia primeiro

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

---

## Sobre o Jogo

Warframe é um TPS cooperativo free-to-play ambientado no Sistema Origem — versão futurista do Sistema Solar. O jogador controla um Tenno, guerreiro antigo reanimado, operando dentro de exoesqueletos biomecânicos chamados Warframes. O jogo é construído em torno de farmear recursos, craftar equipamentos e dominar sistemas de build cada vez mais profundos.

**Ciclo central:** missões procedurais → recursos → crafting → novos frames e armas → Mastery Rank → conteúdo end-game.

**Modelo de conteúdo:** expansões gratuitas chamadas *Updates* adicionam novos Warframes, quests, open worlds e modos de jogo continuamente desde 2013.

---

## Arquitetura do Vault

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

---

## Índices do Sistema

| Índice                                  | Responde perguntas sobre                                                 | Sub-índices                                                                                                                                                             |
| --------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [[_Warframes _Indice\|Warframes]]       | Frames, funções, bosses associados, onde obter, pré-requisitos de acesso | —                                                                                                                                                                       |
| [[_Armas _Indice\|Armas]]               | Slots, tipos, fontes, facções e sistemas de origem                       | [[_Armas _Primarias _Indice\|Primárias]] · [[_Armas _Secundarias _Indice\|Secundárias]] · [[_Armas _Brancas _Indice\|Brancas]] · [[_Armas _Archwing _Indice\|Archwing]] |
| [[_Mods _Indice\|Mods]]                 | Raridades, categorias, efeitos resumidos, fontes de obtenção             | [[_Mods Warframe _Indice\|Warframe]] · [[_Mods Armas _Indice\|Armas]] · [[_Mods Companheiros _Indice\|Companheiros]] · [[_Mods Especiais _Indice\|Especiais]]           |
| [[_Recursos _Indice\|Recursos]]         | Materiais, raridades, planetas de origem, métodos de coleta              | —                                                                                                                                                                       |
| [[_Companheiros _Indice\|Companheiros]] | Tipos, funções, fontes de obtenção, sistemas de origem                   | —                                                                                                                                                                       |
| [[_Missoes _Indice\|Missões]]           | Tipos de missão, objetivos, jornadas, junctions e bounties               | —                                                                                                                                                                       |
| [[_Mecanicas _Indice\|Mecânicas]]       | Sistemas de combate, progressão, economia e social                       | [[_Sindicatos _Indice\|Sindicatos]] · [[_Eventos _Indice\|Eventos]]                                                                                                     |
| [[_Locais _Indice\|Locais]]             | Planetas, facções dominantes, bosses, recursos nativos, como acessar     | —                                                                                                                                                                       |
| [[_Lore _Indice\|Lore]]                 | Facções, personagens, chefes, cronologia do universo                     | [[_Faccoes _Indice\|Facções]] · [[_Personagens _Indice\|Personagens]] · [[_Chefes _Indice\|Chefes]]                                                                     |
| [[_Cosmeticos _Indice\|Cosméticos]]     | Tipos de cosmético, fontes, exclusividade, sistema Tennogen              | —                                                                                                                                                                       |

---

## História do Jogo

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

---

## Curiosidades

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

## Visão Geral do Projeto
- Este é um vault Obsidian que serve como uma wiki pessoal de Warframe.
- **Propósito:** Responder a perguntas, planejar builds, acompanhar o progresso e documentar a lore do jogo.
- **Idioma:** Escrito em Português do Brasil, utilizando YAML frontmatter para metadados.
- **Arquivo Raiz:** `_Warframe _Segunda _Mente.md` — este próprio arquivo, que também é o ponto de entrada para agentes.
- **Volumetria das pastas:** ver a tabela *Arquitetura do Vault* na seção de apresentação acima.

## Estado de Completude
| Nível | Descrição | Exemplos |
|-------|-----------|----------|
| 🟢 Gold Standard (11-38KB) | Artigos completos, detalhados e bem estruturados. | ash.md, atlas.md, ash_prime.md, todos os 14 índices. |
| 🟡 Ficha Básica (600B-1.8KB) | Estrutura principal preenchida com dados essenciais. | excalibur, volt, mag, planetas, alguns chefes, cosméticos. |
| 🟠 Template Vazio (400-900B) | Possui a estrutura base, mas os valores estão em branco ou placeholders básicos. | ~53 warframes regulares. |
| 🔴 Stub/Placeholder (0-130B) | Apenas arquivos criados ou com informações mínimas/nulas. | A maioria das armas, companheiros, mods, facções, personagens e mecânicas. |

**Progresso Geral Estimado:** ~5-8%

## Padrões e Convenções
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

## Regras para o Agente
- **Consulta:** Comece sempre procurando informações nos índices relevantes (ou nas seções correspondentes da Parte 2 deste arquivo). Use Português do Brasil nas respostas. Informe o usuário se o conteúdo não estiver presente ou estiver incompleto (🔴 Stub ou 🟠 Template Vazio).
- **Edição:** Siga rigorosamente o padrão "Gold Standard" visto em `ash.md`. Preserve as seções do YAML, mantenha o uso dos emojis nos cabeçalhos e atualize as datas ao modificar arquivos.
- **Planejamento:** Faça referências cruzadas entre seções (ex: relacionando armas com warframes ou missões com recursos). Considere Maestria (MR) e pré-requisitos ao recomendar planos. Use tabelas e checklists sempre que possível para facilitar a leitura.

## Como navegar a Parte 2
- A Parte 2 é um dump linear do vault, agrupado por `## Seção: <pasta>` e, dentro dela, por `### 📄 arquivo: <nome>.md`.
- Para localizar uma entidade, busque pelo nome do arquivo (ex: `arquivo: ash_prime.md`) ou pelo título da nota.
- A seção raiz não é repetida na Parte 2 — o conteúdo dela é justamente a apresentação no topo deste documento.

## Prioridades de Expansão
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


## Seção: warframes
### 📄 arquivo: _Warframes _Indice.md

# Warframes — Índice

> [!quote]
> *"Nós construímos um quadro ao redor da Infestação... canalizamos sua aflição... a transformamos em força."* — Ballas

---

## Visão Geral

Warframes são exoesqueletos biomecânicos letais controlados pelos **Tenno** através de uma simbiose chamada **Transferência**. Forjados a partir do vírus Helminth combinado à tecnologia Orokin, surgiram durante a Antiga Guerra como resposta contra os Sentients. Cada frame canaliza energias elementais, distorcionais ou físicas únicas — definindo um papel distinto em combate.

---

## Aquisição e Forja

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

---

## Mecânicas Base

| Atributo | Função |
|---|---|
| **Vida** | Barra principal — não regenera sozinha. Recuperada com Orbes Vermelhos ou habilidades de cura |
| **Escudos** | Primeira linha de defesa — regeneram automaticamente. Quebrar ativa Shield Gating (invulnerabilidade breve) |
| **Armadura** | Reduz dano recebido na Vida (não nos Escudos, salvo exceções) |
| **Energia** | Combustível das habilidades — recuperada com Orbes Azuis ou passivas de Aura |

---

## Mods e Polaridades

O poder real de um Warframe vem dos **Mods** equipados, não do nível base. Quatro vetores de customização:

| Vetor | Efeito |
|---|---|
| **Força** | Amplifica o potencial das habilidades |
| **Alcance** | Expande a área de efeito |
| **Duração** | Prolonga efeitos temporais |
| **Eficiência** | Reduz o custo de Energia |

**Formas e Polaridades:** aplicar uma Forma reseta o rank para 0 mas adiciona uma polaridade ao slot. Mods na polaridade correta custam metade da capacidade. O slot de **Aura**, quando alinhado, concede capacidade extra em vez de consumir.

---

## Lista Completa

### Warframes Base

| Warframe | Função | Fonte | Local | Pré-requisito |
|---|---|---|---|---|
| [[ash\|Ash]] | DPS furtivo | Manics (inimigo especial Grineer) | Sedna e outros | — |
| [[atlas\|Atlas]] | Melee / Terra | Quest — The Jordas Precept | Eris | The New Strange |
| [[banshee\|Banshee]] | Amplificador de dano | Pesquisa de Clã (Bio Lab) | Dojo | — |
| [[baruuk\|Baruuk]] | Pacifista / Melee | Bounties — Orbe Vallis | Vênus | Rank Instrument (Solaris United) |
| [[caliban\|Caliban]] | Sentient híbrido | Quest — The New War | — | The New War |
| [[chroma\|Chroma]] | Elementar / Tanque | Quest — The New Strange | — | Vor's Prize |
| [[citrine\|Citrine]] | Suporte / Cristal | Drop — Sanctum Anatomica | Deimos | Whispers in the Walls |
| [[cyte_09\|Cyte-09]] | Tático / Franco-atirador | Missões — Cidade 1999 | 1999 | Quest 1999 |
| [[dagath\|Dagath]] | DPS / Amaldiçoada | Drop — inimigos Whispers in the Walls | Deimos | Whispers in the Walls |
| [[dante\|Dante]] | Suporte / DPS Mágico | Drop — Sanctum Anatomica | Deimos | Whispers in the Walls |
| [[ember\|Ember]] | DPS fogo | Assassinato — Sargas Ruk | Saturno | — |
| [[equinox\|Equinox]] | Dual-form DPS/suporte | Assassinato — Tyl Regor | Urano | — |
| [[excalibur\|Excalibur]] | Melee balanceado | Assassinato — Lech Kril | Marte | — |
| [[follie\|Follie]] | DPS / Suporte | A verificar | — | — |
| [[frost\|Frost]] | Controle / Defesa | Assassinato — Lech Kril | Ceres | — |
| [[gara\|Gara]] | Vidro / Controle | Bounties — Planícies de Eidolon | Terra | — |
| [[garuda\|Garuda]] | DPS sangue | Bounties — Orbe Vallis | Vênus | — |
| [[gauss\|Gauss]] | Velocidade | Disruption — Kelpie | Sedna | — |
| [[grendel\|Grendel]] | Tanque glutão | Missões tributo (3 nodos) | Europa / Lua / Fortaleza Kuva | The War Within |
| [[gyre\|Gyre]] | DPS elétrico | Bounties — Zariman | Zariman | Angels of the Zariman |
| [[harrow\|Harrow]] | Suporte / Buff | Defection + Void Fissure (Rotação C) | Eris / Void | Chains of Harrow |
| [[hildryn\|Hildryn]] | Tanque escudo | Vox Solaris (Fortuna) | Vênus | Rank Hand (Vox Solaris) |
| [[hydroid\|Hydroid]] | Controle / Loot | Assassinato — Vay Hek | Terra | — |
| [[inaros\|Inaros]] | Tanque HP | Quest — Sands of Inaros | — | MR5, The Second Dream |
| [[ivara\|Ivara]] | Furtivo / Loot | Spy — Rotação C | Lua / Corpus | — |
| [[jade\|Jade]] | Suporte angelical | Quest — Jade Shadows | — | Angels of the Zariman |
| [[khora\|Khora]] | DPS / Controle | Elite Sanctuary Onslaught | — | MR8 |
| [[koumei\|Koumei]] | Suporte / Sorte | The Circuit — Duviri | Duviri | The Duviri Paradox |
| [[kullervo\|Kullervo]] | Melee pesado | Kullervo's Hold | Duviri | The Duviri Paradox |
| [[lavos\|Lavos]] | Alquimista elemental | Pesquisa de Clã (Entrati Lab) | Câmbion Drift | Heart of Deimos |
| [[limbo\|Limbo]] | Controle dimensional | Quest — The Limbo Theorem | — | MR2 |
| [[loki\|Loki]] | Furtivo / Controle | Assassinato — Hyena Pack | Netuno | — |
| [[mag\|Mag]] | Magnético / Controle | Starter — Vor's Prize | — | — |
| [[mesa\|Mesa]] | DPS pistolas | Assassinato — Ambulas | Plutão | Patient Zero |
| [[mirage\|Mirage]] | DPS ilusão | Quest — Hidden Messages | — | MR4 |
| [[nekros\|Nekros]] | Necromante / Loot | Assassinato — Lephantis | Deimos | — |
| [[nezha\|Nezha]] | Suporte ágil | Pesquisa de Clã (Tenno Lab) | Dojo | — |
| [[nidus\|Nidus]] | Infestado / Tanque | Infested Salvage — Eris | Eris | The Glast Gambit |
| [[nokko\|Nokko]] | Suporte / Defesa | A verificar | — | — |
| [[nova\|Nova]] | Controle / DPS | Assassinato — Raptors | Europa | — |
| [[nyx\|Nyx]] | Controle mental | Assassinato — Alad V | Júpiter | — |
| [[oberon\|Oberon]] | Paladino / Suporte | Drop — Eximus (qualquer planeta) | Qualquer | — |
| [[octavia\|Octavia]] | Bardo / DPS | Caches — Orokin Derelict / Lua | Deimos / Lua | Octavia's Anthem |
| [[oraxia\|Oraxia]] | Controle / DPS | A verificar | — | — |
| [[protea\|Protea]] | Suporte / Turrets | Quest — The Deadlock Protocol | — | MR8 |
| [[qorvex\|Qorvex]] | Tanque radiação | Drop — Sanctum Anatomica | Deimos | Whispers in the Walls |
| [[revenant\|Revenant]] | Eidolon / Tanque | Bounties — Planícies (noite) | Terra | Mask of the Revenant |
| [[rhino\|Rhino]] | Tanque clássico | Assassinato — Jackal | Vênus | — |
| [[saryn\|Saryn]] | DPS veneno | Assassinato — Kela de Thaym | Sedna | — |
| [[sevagoth\|Sevagoth]] | Sombra / Drenagem | Void Storms — Railjack | Railjack | Rising Tide |
| [[styanax\|Styanax]] | Tanque / Suporte | Quest — Veilbreaker (gratuito) | — | The New War |
| [[temple\|Temple]] | Tanque / Melee | A verificar | — | — |
| [[titania\|Titania]] | Fada / Archwing | Quest — The Silver Grove | — | The Second Dream |
| [[trinity\|Trinity]] | Suporte / Cura | Assassinato — Phobos | Phobos | — |
| [[uriel\|Uriel]] | Suporte angelical | A verificar | — | — |
| [[valkyr\|Valkyr]] | Berserker melee | Assassinato — Alad V (Zanuka) | Júpiter | — |
| [[vauban\|Vauban]] | Suporte / Controle | Nightwave / Sorties | — | — |
| [[volt\|Volt]] | DPS elétrico / Velocidade | Starter / Pesquisa de Clã | Dojo | — |
| [[voruna\|Voruna]] | Furtivo / Assaltante | Assassinato — Lua | Lua | The Second Dream |
| [[wisp\|Wisp]] | Suporte / DPS | Assassinato — Ropalolyst | Júpiter | — |
| [[wukong\|Wukong]] | Clones / Sobrevivência | Pesquisa de Clã (Tenno Lab) | Dojo | — |
| [[xaku\|Xaku]] | Void / DPS | Bounties — Câmbion Drift | Deimos | Heart of Deimos |
| [[yareli\|Yareli]] | Aquático / K-Drive | Quest — The Waverider | — | Heart of Deimos |
| [[zephyr\|Zephyr]] | Aéreo / Mobilidade | Pesquisa de Clã (Tenno Lab) | Dojo | — |

---

### Warframes Prime

> [!info] Aquisição
> Todos os Warframes Prime são obtidos via **Relíquias do Void** em missões de **Fissura**. Relíquias com peças específicas podem ser refinadas com Void Traces para aumentar a raridade das recompensas. Frames em **Prime Vault** têm suas relíquias temporariamente fora de rotação — retornam periodicamente via Prime Resurgence.

| Warframe Prime                       | Função                    | Rotação                                |
| ------------------------------------ | ------------------------- | -------------------------------------- |
| [[ash_prime\|Ash Prime]]             | DPS furtivo               | Normal                                 |
| [[atlas_prime\|Atlas Prime]]         | Melee / Terra             | Normal                                 |
| [[banshee_prime\|Banshee Prime]]     | Amplificador de dano      | Normal                                 |
| [[baruuk_prime\|Baruuk Prime]]       | Pacifista / Melee         | Normal                                 |
| [[caliban_prime\|Caliban Prime]]     | Sentient híbrido          | Normal                                 |
| [[chroma_prime\|Chroma Prime]]       | Elementar / Tanque        | Prime Vault                            |
| [[ember_prime\|Ember Prime]]         | DPS fogo                  | Prime Vault                            |
| [[equinox_prime\|Equinox Prime]]     | Dual-form DPS/suporte     | Normal                                 |
| [[excalibur_prime\|Excalibur Prime]] | Melee balanceado          | **Indisponível** — Founder's Pack 2013 |
| [[frost_prime\|Frost Prime]]         | Controle / Defesa         | Prime Vault                            |
| [[gara_prime\|Gara Prime]]           | Vidro / Controle          | Normal                                 |
| [[garuda_prime\|Garuda Prime]]       | DPS sangue                | Normal                                 |
| [[gauss_prime\|Gauss Prime]]         | Velocidade                | Normal                                 |
| [[grendel_prime\|Grendel Prime]]     | Tanque glutão             | Normal                                 |
| [[gyre_prime\|Gyre Prime]]           | DPS elétrico              | Normal                                 |
| [[harrow_prime\|Harrow Prime]]       | Suporte / Buff            | Normal                                 |
| [[hildryn_prime\|Hildryn Prime]]     | Tanque escudo             | Normal                                 |
| [[hydroid_prime\|Hydroid Prime]]     | Controle / Loot           | Prime Vault                            |
| [[inaros_prime\|Inaros Prime]]       | Tanque HP                 | Normal                                 |
| [[ivara_prime\|Ivara Prime]]         | Furtivo / Loot            | Normal                                 |
| [[khora_prime\|Khora Prime]]         | DPS / Controle            | Normal                                 |
| [[lavos_prime\|Lavos Prime]]         | Alquimista elemental      | Normal                                 |
| [[limbo_prime\|Limbo Prime]]         | Controle dimensional      | Prime Vault                            |
| [[loki_prime\|Loki Prime]]           | Furtivo / Controle        | Prime Vault                            |
| [[mag_prime\|Mag Prime]]             | Magnético / Controle      | Prime Vault                            |
| [[mesa_prime\|Mesa Prime]]           | DPS pistolas              | Normal                                 |
| [[mirage_prime\|Mirage Prime]]       | DPS ilusão                | Prime Vault                            |
| [[nekros_prime\|Nekros Prime]]       | Necromante / Loot         | Prime Vault                            |
| [[nezha_prime\|Nezha Prime]]         | Suporte ágil              | Normal                                 |
| [[nidus_prime\|Nidus Prime]]         | Infestado / Tanque        | Normal                                 |
| [[nova_prime\|Nova Prime]]           | Controle / DPS            | Prime Vault                            |
| [[nyx_prime\|Nyx Prime]]             | Controle mental           | Prime Vault                            |
| [[oberon_prime\|Oberon Prime]]       | Paladino / Suporte        | Prime Vault                            |
| [[octavia_prime\|Octavia Prime]]     | Bardo / DPS               | Normal                                 |
| [[protea_prime\|Protea Prime]]       | Suporte / Turrets         | Normal                                 |
| [[revenant_prime\|Revenant Prime]]   | Eidolon / Tanque          | Normal                                 |
| [[rhino_prime\|Rhino Prime]]         | Tanque clássico           | Prime Vault                            |
| [[saryn_prime\|Saryn Prime]]         | DPS veneno                | Normal                                 |
| [[sevagoth_prime\|Sevagoth Prime]]   | Sombra / Drenagem         | Normal                                 |
| [[titania_prime\|Titania Prime]]     | Fada / Archwing           | Normal                                 |
| [[trinity_prime\|Trinity Prime]]     | Suporte / Cura            | Prime Vault                            |
| [[valkyr_prime\|Valkyr Prime]]       | Berserker melee           | Prime Vault                            |
| [[vauban_prime\|Vauban Prime]]       | Suporte / Controle        | Prime Vault                            |
| [[volt_prime\|Volt Prime]]           | DPS elétrico / Velocidade | Prime Vault                            |
| [[voruna_prime\|Voruna Prime]]       | Furtivo / Assaltante      | Normal                                 |
| [[wisp_prime\|Wisp Prime]]           | Suporte / DPS             | Normal                                 |
| [[wukong_prime\|Wukong Prime]]       | Clones / Sobrevivência    | Normal                                 |
| [[xaku_prime\|Xaku Prime]]           | Void / DPS                | Normal                                 |
| [[yareli_prime\|Yareli Prime]]       | Aquático / K-Drive        | Normal                                 |
| [[zephyr_prime\|Zephyr Prime]]       | Aéreo / Mobilidade        | Normal                                 |

---

### Warframe Umbra

> [!info] Aquisição
> Warframes Umbra são versões com consciência própria — operam de forma autônoma quando o Operador abandona o controle. Excalibur Umbra é o único existente e só pode ser obtido via quest.

| Warframe | Função | Fonte | Pré-requisito |
|---|---|---|---|
| [[excalibur_umbra\|Excalibur Umbra]] | Melee / Anti-Sentient | Quest — The Sacrifice | The War Within |

---

## Por Função

### Tanques e Bruisers
[[rhino\|Rhino]] · [[rhino_prime\|Rhino Prime]] · [[inaros\|Inaros]] · [[inaros_prime\|Inaros Prime]] · [[nidus\|Nidus]] · [[nidus_prime\|Nidus Prime]] · [[hildryn\|Hildryn]] · [[hildryn_prime\|Hildryn Prime]] · [[valkyr\|Valkyr]] · [[valkyr_prime\|Valkyr Prime]] · [[grendel\|Grendel]] · [[grendel_prime\|Grendel Prime]] · [[styanax\|Styanax]] · [[chroma\|Chroma]] · [[chroma_prime\|Chroma Prime]] · [[revenant\|Revenant]] · [[revenant_prime\|Revenant Prime]] · [[qorvex\|Qorvex]] · [[temple\|Temple]] · [[wukong\|Wukong]] · [[wukong_prime\|Wukong Prime]]

### DPS e Nukers
[[saryn\|Saryn]] · [[saryn_prime\|Saryn Prime]] · [[mesa\|Mesa]] · [[mesa_prime\|Mesa Prime]] · [[ember\|Ember]] · [[ember_prime\|Ember Prime]] · [[khora\|Khora]] · [[khora_prime\|Khora Prime]] · [[garuda\|Garuda]] · [[garuda_prime\|Garuda Prime]] · [[gyre\|Gyre]] · [[gyre_prime\|Gyre Prime]] · [[mirage\|Mirage]] · [[mirage_prime\|Mirage Prime]] · [[dagath\|Dagath]] · [[titania\|Titania]] · [[titania_prime\|Titania Prime]] · [[volt\|Volt]] · [[volt_prime\|Volt Prime]] · [[xaku\|Xaku]] · [[xaku_prime\|Xaku Prime]] · [[cyte_09\|Cyte-09]] · [[excalibur\|Excalibur]] · [[equinox\|Equinox]] · [[equinox_prime\|Equinox Prime]]

### Suporte e Buffers
[[trinity\|Trinity]] · [[trinity_prime\|Trinity Prime]] · [[wisp\|Wisp]] · [[wisp_prime\|Wisp Prime]] · [[harrow\|Harrow]] · [[harrow_prime\|Harrow Prime]] · [[protea\|Protea]] · [[protea_prime\|Protea Prime]] · [[oberon\|Oberon]] · [[oberon_prime\|Oberon Prime]] · [[nezha\|Nezha]] · [[nezha_prime\|Nezha Prime]] · [[citrine\|Citrine]] · [[dante\|Dante]] · [[jade\|Jade]] · [[koumei\|Koumei]] · [[nokko\|Nokko]] · [[uriel\|Uriel]] · [[octavia\|Octavia]] · [[octavia_prime\|Octavia Prime]]

### Controle de Grupo
[[frost\|Frost]] · [[frost_prime\|Frost Prime]] · [[limbo\|Limbo]] · [[limbo_prime\|Limbo Prime]] · [[nyx\|Nyx]] · [[nyx_prime\|Nyx Prime]] · [[vauban\|Vauban]] · [[vauban_prime\|Vauban Prime]] · [[gara\|Gara]] · [[gara_prime\|Gara Prime]] · [[mag\|Mag]] · [[mag_prime\|Mag Prime]] · [[nova\|Nova]] · [[nova_prime\|Nova Prime]] · [[hydroid\|Hydroid]] · [[hydroid_prime\|Hydroid Prime]] · [[yareli\|Yareli]] · [[yareli_prime\|Yareli Prime]] · [[zephyr\|Zephyr]] · [[zephyr_prime\|Zephyr Prime]] · [[oraxia\|Oraxia]] · [[lavos\|Lavos]] · [[lavos_prime\|Lavos Prime]] · [[nekros\|Nekros]] · [[nekros_prime\|Nekros Prime]]

### Furtivos e Táticos
[[loki\|Loki]] · [[loki_prime\|Loki Prime]] · [[ivara\|Ivara]] · [[ivara_prime\|Ivara Prime]] · [[ash\|Ash]] · [[ash_prime\|Ash Prime]] · [[voruna\|Voruna]] · [[voruna_prime\|Voruna Prime]] · [[banshee\|Banshee]] · [[banshee_prime\|Banshee Prime]]

### Melee e Híbridos
[[atlas\|Atlas]] · [[atlas_prime\|Atlas Prime]] · [[baruuk\|Baruuk]] · [[baruuk_prime\|Baruuk Prime]] · [[kullervo\|Kullervo]] · [[caliban\|Caliban]] · [[caliban_prime\|Caliban Prime]] · [[follie\|Follie]] · [[sevagoth\|Sevagoth]] · [[sevagoth_prime\|Sevagoth Prime]] · [[gauss\|Gauss]] · [[gauss_prime\|Gauss Prime]] · [[excalibur_umbra\|Excalibur Umbra]]

---

## Referências Cruzadas

| Sistema | Índice |
|---|---|
| Mods de Warframe | [[_Mods Warframe _Indice\|Mods — Warframe]] |
| Bosses e drops | [[_Chefes _Indice\|Chefes]] |
| Locais de obtenção | [[_Locais _Indice\|Locais]] |
| Missões e jornadas | [[_Missoes _Indice\|Missões]] |
| Sistemas de progressão | [[_Mecanicas _Indice\|Mecânicas]] |

---

## Curiosidades

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


## Seção: warframes\regular
### 📄 arquivo: ash.md

> *"A lenda diz que um predador letal ataca a partir das sombras. Ash não tem como alvo os olhos, mas sim as defesas de seus oponentes. Ele é conhecido como o patrono das lâminas imperturbáveis."* — **Códice, Warframe.com**

## 📖 História e Códice

Desenvolvido durante o [[lore/faccoes/orokin.md|Império Orokin]], Ash foi concebido como uma solução para missões que exigiam letalidade silenciosa e infiltração. Sua tecnologia modular e métodos de combate derivam da escola de assassinos conhecida como *Scoria*. Ao contrário de modelos criados para a linha de frente da Antiga Guerra contra os [[lore/faccoes/sentient|Sentient]], Ash especializou-se na eliminação de alvos de alto valor e na neutralização de traidores em ambientes restritos, executando táticas de extermínio sem detecção prévia.

## 🎮 Visão Geral e Gameplay

Ash é um Warframe focado em mobilidade, invisibilidade e dano direto focado. Sua eficácia principal reside na capacidade de infligir "Dano Verdadeiro" através da constante aplicação de status de Sangramento (Cortante/Slash). Essa mecânica permite que ele escale facilmente em curvas de dificuldade altas (como o [[sistemas/caminho_de_aco.md|Caminho de Aço]]), onde a armadura inimiga mitiga quase todo o dano padrão. O estilo de jogo recomendado é o reposicionamento contínuo, a manutenção cautelosa da habilidade de invisibilidade (Smoke Screen) e foco em eliminações chave utilizando suas habilidades letais em vez de assumir postura de defesa em área fixa.

## 💡 Curiosidades (Trivia)

Durante a fase de desenvolvimento alfa na Digital Extremes, Ash recebeu o nome inicial de "Ninja", o que justifica os elementos de design estético de sua armadura padrão, inspirados no folclore de armaduras lamelares e besouros.

No seu lançamento em 2013, o estilo anatômico do chassi foi considerado uma contraparte tática direta aos modelos focados em controle de multidão com magia elemental da época, como [[warframes/saryn.md|Saryn]] e [[warframes/nyx.md|Nyx]].

As quatro habilidades de Ash causam estritamente dano físico (frequentemente tipo Cortante), o que o torna uma exceção entre warframes de longo alcance que normalmente dependem de efeitos elementais para dano base.

## 🔮 Habilidades

* **Passiva (Hemorragia):** Efeitos de status Cortante (*Slash*) infligidos de qualquer fonte originada por Ash recebem **25% de Dano Adicional** e um **incremento de 50% em sua duração base**.

* **1. Shuriken (25 Energia):** Arremessa instantaneamente duas lâminas teleguiadas em alvos próximos. As lâminas rasgam armaduras e aplicam um efeito de sangramento imediato garantido.

* **2. Smoke Screen (35 Energia):** Derruba uma bomba de fumaça. Atordoa os inimigos dentro do raio de impacto inicial e concede invisibilidade a Ash.

* **3. Teleport (25 Energia):** Teletransporta Ash instantaneamente para o local do inimigo ou aliado focado. Ao surgir, o alvo fica suscetível a sofrer uma finalização de execução (*Finisher*) imediata.

* **4. Blade Storm (Drenagem Mirada):** Entra em um modo visual rastejante para aplicar marcas adversárias. Ao recativular a habilidade, clones invulneráveis do Ash avançarão pelas paredes para despachar alvos marcados em dano cortante concentrado.

## 🏗️ Aquisição e Fundição

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

## 📊 Estatísticas Matemáticas e Sobrevivência (Rank 0 -> 30)

| Atributo Oficial | Status Base (Rank 0) | Evolução Máxima (Rank 30) |
|------------------|----------------------|---------------------------|
| **Vida (Saúde)** | 150 | **450** |
| **Escudo**       | 100 | **300** |
| **Armadura**     | 100 | 100 |
| **Energia**      | 100 | **150** |
| **Vel. Sprint**  | 1.15 | 1.15 |

> **Polaridades Inatas Ocultas:** 2x Naramon (Traço -)
> **Slot de Aura Inata:** Naramon (Traço -)

## 🛠️ Guia Builds e Maximização

Os guias avançados centralizam no uso da mecânica do Warframe atrelada à invisibilidade defensiva enquanto priorizam melhorias ofensivas em Dano Verdadeiro. O end-game prescinde normalmente de mods massivos de resiliência e saúde crua. O viés ideal exige o aumento contínuo no status de Força (Strength) somado à estabilidade contínua entre as pausas automáticas das mecânicas ativas de execuções.

#### 🎛️ O Arsenal Essencial e Aquisições Core

| Ferramenta / Mod / Arcano                                | Categoria Original | Efeito Funcional da Configuração                                                                                                                                                          | Como Obter                                                                                                                                                                 |
| -------------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[[mods/fatal_teleport.md\|Fatal Teleport]]**           | Mod de Ampliação   | Habilita animações passivas e automáticas de execuções (*Finishers*) na Habilidade 3 e concede base aditiva de +200% de dano.                                                             | Associações dos Sindicatos Nativos (*[[lore/faccoes/sindicatos/veu_vermelho.md\|Véu Vermelho]]* ou *[[lore/faccoes/sindicatos/arbitros_de_hexis.md\|Árbitros de Hexis]]*). |
| **[[mods/rising_storm.md\|Rising Storm]]**               | Mod de Ampliação   | Permite aos clones invocados pela Habilidade 4 contribuírem ativamente com rebatidas no "Medidor de Combo Corpo A Corpo".                                                                 | Associações dos Sindicatos Nativos (*[[lore/faccoes/sindicatos/veu_vermelho.md\|Véu Vermelho]]* ou *[[lore/faccoes/sindicatos/arbitros_de_hexis.md\|Árbitros de Hexis]]*). |
| **[[mods/transient_fortitude.md\|Transient Fortitude]]** | Mod Corrompido     | Intensifica significativamente a Força de Habilidade bruta com sacrifício tático associado na estatística da Duração de Habilidades.                                                      | Abordagens dentro dos *Cofres Estelares ([[locais/deimos.md\|Deimos]] Vaults)* e transações em platina.                                                                    |
| **[[mods/arcane_trickery.md\|Arcane Trickery]]**         | Aprimoramento      | Garante que todas as execuções instintivas apliquem porcentagem limpa e passiva (15% chance por abate) de adicionar sobrecarga de **invisibilidade orgânica absoluta de 30s de duração**. | Conclusões primárias nos abates de bestas Eidolons em [[locais/cetus\|Cetus]] ou Trocas comerciais.                                                                        |

## 🧬 Subsunção e Acoplagem do Helminte

**Poder Cedido Base (Doação [[sistemas/helminte.md|Helminte]]):** **Shuriken**. Com a infecção e o descarte permanente de uma réplica do chassi na Enfermaria do Helminth da escotilha local, essa habilidade modular de atiradores perfurantes limpos está aberta para incorporação transversal de qualquer outro *warframe* na carga. 

## 🔗 Terrenos de Atuação, Sinergia e Lâminas Reais

#### 📍 Compatibilidade de Modalidades de Guerra:

* **Incursões End-Game Solo (Aço, [[missoes/exterminio.md|Extermínios]], [[missoes/sobrevivencia.md|Sobrevivência]]):** Considerável força e sobrevivência inata devida à invisibilidade e capacidade de escalonar "Damage real", ultrapassando defesas ativas de inimigos ultra blindados ([[sistemas/caminho_de_aco.md|Caminho de Aço]]).
* **Alvos Nativos Base (Assassinato/Hunt):** Utilidade crítica e cirúrgica limpa para destruir [[lich_de_kuva|Líches de Kuva]] ou [[chefes|Chefões]] robustos pela facilidade pura de penetrar o bloqueio da vida deles nativamente na fase orgânica de embate.
* **Contra-Indicação (Missões de Protetor Estático):** Fragilidade alta constatada para missões prolongadas focadas puramente na proteção de equipamentos desarmados abertos ao fogo cruzado, como Célio de Criogenia de [[missoes/defesa.md|Defesas]] ou Extratores ([[missoes/escavacao.md|Escavação]]), já que ele não abrange barreiras espaciais.

#### 🤝 Sinergia em Time:

* **[[warframes/banshee.md|Banshee]] (Meta Primordial Subsunção):** A utilidade cruzada com "Silence" (Silêncio) escalona drasticamente a utilidade. Se aliado à tática de esquadrão, a habilidade propõe paralisia. Injetada no painel modular dentro das rotas de Ash, essa adição de atordoamento propaga diretamente nas cópias animadas passivas, **acrescentando passivos fixos pesados de +300% de bônus adicional bruto em Finishers** contínuos durante os ciclos repetitivos de "Blade Storm".
* **[[warframes/harrow.md|Harrow]] / [[warframes/nova.md|Nova]]:** Aplicam efeitos passivos utilitários como contenção maciça ([[warframes/harrow.md|Harrow]]) ou lentidão massiva pesada ([[warframes/nova.md|Nova]]) na fenda dos corredores, dando mais espaço estático confortável para posicionamentos do extermínio orgânico limpo de Ash no fluxo biológico da partida regular. 

#### ⚔️ Conexões Canônicas com O Arsenal Furtivo:

O design do personagem invoca nativamente a associação canônica da classe original de ninjas aos atributos base em combates focados de Katanas, **[[armas/nikana.md|Nikanas]]** ou Lâminas Pequenas Brutais Furtivas. Usos extensivos com **[[armas/adagas.md|Adagas]]** modulares acopladas puramente na progressão de bônus diretos com a estampa mod de "[[mods/covert_lethality.md|Covert Lethality]]" garantem execuções completas e diretas de classe letal nos alvos atingidos. Além do alcance orgânico, snipers clássicas como a **[[armas/vectis_prime.md|Vectis Prime]]** cumprem com naturalidade as exigências visuais base como arsenal de tiro único seguro e furtivo na operação contínua coberta pelas próprias restrições densas estéticas e cinzas da bomba de fumaça primária dele (Smoke Screen).

## 🎨 Apresentação e Estilização (Fashion Frame)

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


## Seção: warframes\regular
### 📄 arquivo: atlas.md

> *"Este é Atlas, o lutador, o forte. Mover montanhas não é uma tarefa fácil, Tenno. Atlas resiste."* — **Códice, Warframe.com**

## 📖 História e Códice

A descoberta de Atlas remonta à aniquilação de uma ameaça cataclísmica direcionada à [[locais/terra.md|Terra]]. Durante os tempos remotos do [[lore/faccoes/orokin.md|Império Orokin]], a seita paramilitar fanática conhecida como [[lore/faccoes/temple_telamon.md|Temple Telamon]] redirecionou a trajetória de um asteroide massivo para colidir com o planeta, em prol de suas profecias apocalípticas de renascimento. Como último recurso tático para interceptar a estrutura geológica, os [[lore/faccoes/orokin.md|Orokin]] empregaram Atlas. 

Utilizando sua proficiência cinética e manipulação elementar terrena, Atlas interceptou o asteroide de forma solitária. Direcionando frequências de ressonância através de suas formações tectônicas, ele induziu a desintegração estrutural total do corpo celeste, neutralizando a insurgência Telamon definitivamente. Suas escórias estruturais foram posteriormente retidas no domínio de [[locais/eris.md|Eris]], caindo sob o controle biológico da [[lore/faccoes/infestados.md|Infestação]].

## 🎮 Visão Geral e Gameplay

A arquitetura biomecânica de Atlas foi desenhada para atuar como mitigador contínuo de dano e força impositiva em engajamentos de área fechada (Brawler). A base sistêmica operacional atua otimizando instâncias de sobrevivência a partir da aglomeração retroalimentativa de blindagem rochosa ([[mecanicas/rubble.md|Rubble]]). Aplicando índices devastadores através da otimização corpo a corpo (mecânica modular de contágio de atrito e [[mecanicas/stat_sticks.md|Stat Sticks]]), o chassi subjuga zonas de impacto ao aplicar controle restritivo via fossilização progressiva dos oponentes em seu perímetro visual.

Estes parâmetros atestam o chassi de Atlas como uma escolha primária no engajamento massivo de hordas blindadas em instâncias de durabilidade extrema, como incursões no [[sistemas/caminho_de_aco.md|Caminho de Aço]], consolidando-se como um baluarte ofensivo intransponível cuja eficiência escala passivamente com a aniquilação territorial contínua.

## 💡 Curiosidades (Trivia)

- Desenvolvido em ambientes de laboratório de *game design* da [[empresas/digital_extremes.md|Digital Extremes]] sob a alcunha referencial "Brawler", terminologia estruturante ainda rastreável nas nomenclaturas de pastas binárias do jogo.
- A natureza progressiva da paralisação induzida reflete as origens conceituais do mito basilar da [[lore/referencias/medusa.md|Górgona Medusa]] da cosmologia grega. A passiva inamovível espelha [[lore/referencias/antaeus.md|Antaeus]], combatente legendário indestrutível enquanto mantivesse convergência direta com o substrato fixo da terra.
- Consolida o escopo de primeiro Warframe do inventário original projetado desde o lançamento primário ostentando sinergia sistêmica canônica com um arsenal físico próprio listado: a arma [[armas/tekko.md|Tekko]].

## 🔮 Habilidades

* **Passiva (Imobilidade Tectônica):** Retém imunidade técnica absoluta a efeitos externos que promovam impactos de [[mecanicas/derrubada.md|Derrubada (Knockdown)]] ou paralisia gravitacional enquanto os sensores de nivelamento permanecerem contíguos a estratos rígidos da superfície.

* **1. Landslide (25 Energia):** Exerce propulsão avassaladora de deslocamento instantâneo resultando em ruptura física extrema por esmagamento. Reativações sequenciais acionam matrizes de impacto em progressão matemática geométrica de agressividade e raio de influência, decaindo as taxas exigidas da reserva de energia em cada novo engate acoplado.

* **2. Tectonics (50 Energia):** Condensa compostos do relevo adjacente na formulação estática de uma placa geométrica obstrutiva intransponível. Estimulações reativas da parede originam instabilidade estrutural, convertendo-a em projétil rochoso invasivo capaz de penetração múltipla de hordas invasoras em formato de esfera rolante.

* **3. Petrify (75 Energia):** Submete hordas em zona angular frontal a fluxos eletromagnéticos enrijecedores, comprometendo todas as malhas protetoras biológicas até a solidificação fóssil total e escalonando danos colaterais induzidos. Resíduos desintegrados de inimigos nesta contenção provêem sedimentos que curam o vetor principal ou convertem-se em carapaça ativa.

* **4. Rumblers (100 Energia):** Mobiliza acúmulos aglomerados do cenário em dois construtos táticos automatizados e perigosos. Estas unidades agem capturando focos isolados de opositores, irradiando restrições motoras nos vetores alvejados. Ao concluírem suas operações geológicas, os construtos colapsam em acúmulos massivos de rochas protetoras consumíveis.

## 🏗️ Aquisição e Fundição

#### Tabela de Fabricação Base

| Componente     | Fonter/Drop                                                        | Planeta        | Créditos | Recursos Extraordinários                                                                         | Tempo |
| -------------- | ------------------------------------------------------------------ | -------------- | -------- | ------------------------------------------------------------------------------------------------ | ----- |
| Diagrama Maior | Missão [[lore/jornadas/the_jordas_precept.md\|The Jordas Precept]] | [[locais/eris.md\|Eris]] | 50.000   | 100.000x [[recursos/alloy_plate.md\|Placa de Liga]]                                              | 72h   |
| Neurovisor     | Assassinato [[NPCs/chefes/jordas_golem.md\|Jordas Golem]]          | [[locais/eris.md\|Eris]] | 15.000   | 1.500x [[recursos/polymer_bundle.md\|Pacote de Polímero]], 1x [[recursos/sensores_neurais.md\|Sensor Neural]]                      | 12h   |
| Chassi         | Assassinato [[NPCs/chefes/jordas_golem.md\|Jordas Golem]]          | [[locais/eris.md\|Eris]] | 15.000   | 1.000x [[recursos/nano_spores.md\|Nano Esporos]], 2x [[recursos/extrato_de_nitain.md\|Extrato de Nitain]]                           | 12h   |
| Sistemas       | Assassinato [[NPCs/chefes/jordas_golem.md\|Jordas Golem]]          | [[locais/eris.md\|Eris]] | 15.000   | 1.500x [[recursos/polymer_bundle.md\|Pacote de Polímero]], 3x [[recursos/neurodes.md\|Neurodes]] | 12h   |

#### Vias Alternativas de Obtenção:
A matriz de Diagrama do núcleo arquitetônico é restaurada após falhas vitais no diretório isolado de [[NPCs/cephalon_simaris.md|Cephalon Simaris]]. Aquisições integrativas modulares da arquitetura se fazem operacionais através do preenchimento semanal em fases na dinâmica de [[sistemas/o_circuito.md|O Circuito]] atrelados à paisagem abstrata originária de [[locais/duviri.md|Duviri]]. Operações secundárias de intercâmbio rápido permanecem liberadas via negociação de contrato baseada em [[recursos/platina.md|Platina]].

## 📊 Estatísticas Matemáticas e Sobrevivência (Rank 0 -> 30)

| Atributo Oficial | Status Base (Rank 0) | Evolução Máxima (Rank 30) |
|------------------|----------------------|---------------------------|
| **Vida (Saúde)** | 100 | **270** |
| **Escudo**       | 100 | **270** |
| **Armadura**     | 475 | **475** |
| **Energia**      | 150 | **175** |
| **Vel. Sprint**  | 0.9 | 0.9 |

> **Polaridades Inatas Ocultas:** Traço D (Vazarin), Traço - (Naramon), Traço V (Madurai)
> **Slot de Aura Inata:** Traço V (Madurai)

## 🛠️ Guia Builds e Maximização

Os guias avançados centralizam no uso da mecânica do Warframe atrelada à fossilização defensiva e acúmulo de blindagem ([[mecanicas/rubble.md|Rubble]]) enquanto priorizam multiplicadores brutos de corpo-a-corpo. O end-game prescinde do balanceamento passivo defensivo garantido, migrando para sobreposições rigorosas para intensificar o impacto brutal da habilidade fundamental. O viés ideal exige foco direcionado em [[mecanicas/forca_de_habilidade.md|Força de Habilidade]] combinada à sinergia do arsenal através do uso meticuloso de [[mecanicas/stat_sticks.md|Stat Sticks]] customizados.

#### 🎛️ O Arsenal Essencial e Aquisições Core

| Ferramenta / Mod / Arcano                                | Categoria Original | Efeito Funcional da Configuração                                                                                                                                                             | Como Obter                                                                                                                                                                      |
| -------------------------------------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[[mods/path_of_statues.md\|Path of Statues]]**         | Mod de Ampliação   | Injeta fluídos petrificantes rastreáveis nas trilhas deixadas pela propulsão do Landslide, automatizando a contenção tática sem gasto adicional.                                             | Associações dos Sindicatos Nativos (*[[lore/faccoes/sindicatos/cephalon_suda.md\|Cephalon Suda]]* ou *[[lore/faccoes/sindicatos/veu_vermelho.md\|Véu Vermelho]]*).              |
| **[[mods/rubble_heap.md\|Rubble Heap]]**                 | Mod de Ampliação   | Anula o limite gravitacional de decaimento natural da blindagem extra. O custo do Landslide decai a zero e adquire velocidade pura extra após o teto de escombros batido.                    | Associações dos Sindicatos Nativos (*[[lore/faccoes/sindicatos/cephalon_suda.md\|Cephalon Suda]]* ou *[[lore/faccoes/sindicatos/veu_vermelho.md\|Véu Vermelho]]*).              |
| **[[mods/blind_rage.md\|Blind Rage]]**                   | Mod Corrompido     | Intensifica drasticamente a [[mecanicas/forca_de_habilidade.md\|Força de Habilidade]] com elevado sacrifício sobre a [[mecanicas/eficiencia.md\|Eficiência]] geral operacional.                                                           | Abordagens dentro dos *Cofres Estelares ([[locais/deimos.md\|Deimos]] Vaults)* e transações comerciais puras com platina.                                                       |
| **[[mods/arcane_avenger.md\|Arcane Avenger]]**           | Aprimoramento      | Garante que o recebimento contínuo de dano físico nativo incorra em acréscimos diretos e brutos massivos (+45%) na [[mecanicas/chance_critica.md\|Chance Crítica]] corporificante, maximizando agressões primárias.         | Capturas e Derrotas das bestas Eidolons ultra-resistentes na matriz aberta de [[locais/cetus.md\|Cetus]] ou em negociações p2p orgânicas entre contratantes.                    |

## 🧬 Subsunção e Acoplagem do Helminte

**Poder Cedido Base (Doação [[sistemas/helminte.md|Helminte]]):** **Petrify**. O algoritmo sistêmico de desestabilização biomolecular contida é permanentemente cimentado pela Helminte à extração modular livre, compartilhando sua vasta utilidade de controle impositivo de grupo maciço frontal e petrificação garantida para a infusão do painel modular tático em outros construtos e chasises adjacentes.

## 🔗 Terrenos de Atuação, Sinergia e Golems Reais

#### 📍 Compatibilidade de Modalidades de Guerra:

* **Incursões Fixas e Defesas (Zonas Estáticas, [[missoes/defesa.md|Defesa]]):** Considerável viabilidade como baluarte graças às concentrações de massas tectônicas geográficas e de obstrução puras (*Tectonics*) e golens de patrulha perimetral indestrutíveis (*Rumblers*).
* **Sobrevivências de Altíssimo Desgaste ([[sistemas/caminho_de_aco.md|Caminho de Aço]]):** Potência cirúrgica contra falanges e exércitos inteiros graças ao acúmulo contínuo sistêmico de sobrevida passiva e atrito físico propiciada pelo foco unicamente devotado em abates corporais massivos de curto alcance (via Landslide).
* **Contra-Indicação (Missões de Movimentos Rápido ou Abordagens):** Extrema e notória inadequabilidade utilitária tática para missões ativas baseadas que dependam de velocidade abstrata veloz natural e fugas temporais como Operações em [[missoes/espionagem.md|Espionagem]], devido fundamentalmente à completa ausência de mecânicas furtivas baseadas dentro do chassi pesado.

#### 🤝 Sinergia em Time:

* **[[warframes/wisp.md|Wisp]] / [[warframes/citrine.md|Citrine]]:** Impõem em zona contígua passiva seus suportes vitais focados puramente de base protetora ou amplificadores orgânicos para durabilidade celular que catalisam as propulsões terrestres do Atlas frente a exércitos de contenção extremamente densos e blindados sem recuos obrigatórios.
* **[[warframes/nidus.md|Nidus]] (Via Larva):** Atribui a conglomeração estendida de todos os oponentes num ponto focal. Essa aproximação via atração geométrica encurraladora compila um alvo fácil, tornando viável esmagar e apagar agrupamentos maciços brutalmente compactados simultaneamente utilizando-se de apenas a onda em arco expansivo central do Landslide.

#### ⚔️ Conexões Canônicas com O Arsenal Furtivo/Primordial:

Em observância estrutural dos primórdios operacionais originais do design focado em combate aproximado bruto, é possível atrelar o *status* da classe a partir do manejo imperativo orgânico de suas armas corpo-a-corpo focadas em furação (soqueiras perfurantes): **[[armas/tekko.md|Tekko]]** ou a variação superior letal natural de **[[armas/tekko_prime.md|Tekko Prime]]**. Esta escolha de infraestrutura resulta sistêmica organicativa base provendo de estampa acréscimos brutos de atributos puramente (+6% status adicional limpo base), maximizando a sinergia indissolúvel das lutas corpo-a-corpo sem interferência impura no meta game.

## 🎨 Apresentação e Estilização (Fashion Frame)

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


## Seção: warframes\regular
### 📄 arquivo: excalibur.md

# Excalibur

> [!info] Visão Geral
> Warframe inicial balanceado com espada exaltada poderosa

## Como Obter
- Fonte: Assassination (Lieutenant Lech Kril) ou Escolha Inicial
- Drop location: War, Marte
- Blueprint: Mercado (35,000 Créditos)

## Habilidades

| # | Nome | Custo | Descrição |
|---|------|-------|-----------|
| Passiva | Swordsmanship | — | +10% de Velocidade de Ataque e Dano ao usar espadas (Longswords, Dual Swords, Nikanas, Rapiers). |
| 1 | Slash Dash | 25 | Avança entre inimigos com a Exalted Blade, causando dano. |
| 2 | Radial Blind | 50 | Emite um flash brilhante, cegando inimigos próximos. |
| 3 | Radial Javelin | 75 | Lança dardos nos inimigos, causando dano massivo. |
| 4 | Exalted Blade | 25 inicial | Evoca uma espada de puro brilho que atira ondas de energia cortante. |

## Stats Base

| Stat | Valor |
|------|-------|
| HP | 100 (300 no Nv 30) |
| Escudo | 100 (300 no Nv 30) |
| Armadura | 250 |
| Energia | 100 (150 no Nv 30) |
| Sprint | 1.0 |
| Polaridades | 1 Madurai (V), 1 Vazarin (D) |

## Build Recomendada
> Preencher após obter o Warframe.
- [ ] 

## Minha Progressão
- [ ] Blueprint obtido
- [ ] Componentes farmados
- [ ] Craftado
- [ ] Rank 30
- [ ] Forma aplicado

## Conexões
- Sinergias: Mag (Magnetize + Radial Javelin), Volt (Speed)
- Recursos necessários: Plástidos, Célula Orokin, Rubedo, Restos
- Quests relacionadas: O Despertar (Tutorial), O Sacrifício (relacionada ao Excalibur Umbra)

----------------------------------------


## Seção: warframes\regular
### 📄 arquivo: volt.md

# Volt

> [!info] Visão Geral
> DPS elétrico versátil e escudo condutor

## Como Obter
- Fonte: Pesquisa do Dojo (Laboratório Tenno) ou Escolha Inicial
- Drop location: Dojo - Laboratório Tenno
- Blueprint: Mercado (35,000 Créditos) ou Dojo

## Habilidades

| # | Nome | Custo | Descrição |
|---|------|-------|-----------|
| Passiva | Eletricidade Estática | — | Movimentar-se pelo solo acumula carga elétrica, aplicável ao próximo ataque (até 1000 de dano extra). |
| 1 | Shock | 25 | Dispara um projétil elétrico que causa dano e se encadeia entre inimigos próximos. |
| 2 | Speed | 50 | Aumenta drasticamente a velocidade de movimento e ataque corpo a corpo dele e dos aliados. |
| 3 | Electric Shield | 50 | Posiciona um escudo de energia. Tiros aliados que o atravessam ganham dano elétrico e crítico. |
| 4 | Discharge | 100 | Paralisa inimigos com uma descarga elétrica que danifica e choca alvos próximos (Chain-Lightning). |

## Stats Base

| Stat | Valor |
|------|-------|
| HP | 100 (300 no Nv 30) |
| Escudo | 150 (450 no Nv 30) |
| Armadura | 15 |
| Energia | 100 (150 no Nv 30) |
| Sprint | 1.0 |
| Polaridades | 2 Naramon (Traço) |

## Build Recomendada
> Preencher após obter o Warframe.
- [ ] 

## Minha Progressão
- [ ] Blueprint obtido
- [ ] Componentes farmados
- [ ] Craftado
- [ ] Rank 30
- [ ] Forma aplicado

## Conexões
- Sinergias: Mag (Shock + Magnetize para área danosa), Titania/Gauss (Speed)
- Recursos necessários: Placas de Liga, Pacote de Polímero, Célula Orokin, Módulo de Controle
- Quests relacionadas: O Despertar (Tutorial)

----------------------------------------


## Seção: warframes\regular
### 📄 arquivo: mag.md

# Mag

> [!info] Visão Geral
> Controle magnético: atrai projéteis e implode escudos

## Como Obter
- Fonte: Assassination (The Sergeant) ou Escolha Inicial
- Drop location: Iliad, Fobos
- Blueprint: Mercado (25,000 Créditos)

## Habilidades

| # | Nome | Custo | Descrição |
|---|------|-------|-----------|
| Passiva | Atração Magnética | — | Atrai drops (recursos, mods, munição) ao realizar um Bullet Jump. |
| 1 | Pull | 25 | Puxa inimigos em direção à Mag, causando dano e derrubando-os. |
| 2 | Magnetize | 50 | Cria um campo magnético ao redor de um alvo, prendendo inimigos e atraindo projéteis. |
| 3 | Polarize | 75 | Emite um pulso que drena escudos e armaduras inimigas, restaurando os escudos dos aliados. |
| 4 | Crush | 100 | Magnetiza os ossos dos inimigos próximos, levantando-os e esmagando para causar dano. |

## Stats Base

| Stat | Valor |
|------|-------|
| HP | 75 (225 no Nv 30) |
| Escudo | 150 (450 no Nv 30) |
| Armadura | 65 |
| Energia | 175 (262.5 no Nv 30) |
| Sprint | 1.0 |
| Polaridades | 2 Naramon (Traço), Aura: Naramon (Traço) |

## Build Recomendada
> Preencher após obter o Warframe.
- [ ] 

## Minha Progressão
- [ ] Blueprint obtido
- [ ] Componentes farmados
- [ ] Craftado
- [ ] Rank 30
- [ ] Forma aplicado

## Conexões
- Sinergias: Excalibur (Radial Javelin + Magnetize), Armas de projétil (ex: Lanka, Nataruk)
- Recursos necessários: Placas de Liga, Circuitos, Módulo de Controle, Plástidos
- Quests relacionadas: O Despertar (Tutorial)

----------------------------------------


## Seção: warframes\primes
### 📄 arquivo: ash_prime.md

> *"Especialista na arte militar da distração e subterfúgio, Ash Prime ataca não visto, mas deixa para trás um rastro de letalidade inconfundível. Uma relíquia letal e aprimorada de uma era distante."* — **Códice, Warframe.com**

## 📖 História e Códice

Ash Prime é a variante ancestral e militarmente otimizada do chassi [[warframes/ash.md|Ash]] original, manufaturada durante o ápice do [[lore/faccoes/orokin.md|Império Orokin]]. Operava como o carrasco e a lâmina silenciosa dos Executores, empregado taticamente para fins de eliminação de alvos de alto valor e desestabilização de frentes sem ativar protocolos de alerta limitantes.

## 🎮 Visão Geral e Gameplay

O núcleo tático deste Warframe repousa no dano focado contínuo e imunidade tática através de furtividade ativa. Ash Prime anula alvos singulares extremamente blindados em conteúdos de alto nível (como o [[sistemas/caminho_de_aco.md|Caminho de Aço]]) ignorando a camada física defensiva via status inato de Sangramento (Corte). Exige precisão e controle operante de energia, priorizando extermínios rápidos e isolamento de ameaças sistêmicas no campo de batalha em abordagens majoritariamente solo.

## 💡 Curiosidades (Trivia)

Possui o design do capacete com inspiração militar restrita voltada no tradicional "Kabuto" dos samurais japoneses originais.

Apresenta caligrafia Orokin gráfica nativa em seu chassi equivalente à identificação serial: *"Tenno Model 24N - Serial 147H"*.

## 🔮 Habilidades

*   **Passiva (Hemorragia):** Efeitos de status Cortante (*Slash*) infligidos de qualquer fonte originada por Ash recebem **25% de Dano Adicional** e um **incremento de 50% em sua duração base**.

*   **1. Shuriken (25 Energia):** Dispara projéteis teleguiados de perfil afiado. Ao contato físico, empala e impõe garantidamente status punitivo severo de sangramento na integridade estática do alvo. 

*   **2. Smoke Screen (35 Energia):** Detonação de distração ao solo imediato. Interrompe ativamente quadros agressivos em um raio curto de atuação (Atordoamento base) e garante furtividade momentânea militar não-rastreável por unidades orgânicas ou robóticas.

*   **3. Teleport (25 Energia):** Relocação vetorial instantânea orientada para a geometria física do alvo travado em tela. Realiza uma aproximação letal tática, frequentemente atrelando finalizadores de retalhação automatizados (recupera parcialmente o custo base de energia em eliminações singulares).

*   **4. Blade Storm (12 Energia por Marcação):** Invoca hologramas sombrios de clones operantes que escalam independente do estado atual do chassi mestre para varredura de área. Marca alvos múltiplos na visão. A execução ignora inteiramente e de forma absoluta defesas de armaduras pesadas aplicando dano de Sangramento real puro.

## 🏗️ Aquisição e Fundição

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

## 📊 Estatísticas Matemáticas e Sobrevivência (Rank 0 -> 30)

| Atributo Oficial | Status Base (Rank 0) | Evolução Máxima (Rank 30) |
|------------------|----------------------|---------------------------|
| **Vida (Saúde)** | 150 | **455** |
| **Escudo**       | 125 | **365** |
| **Armadura**     | 185 | 185 |
| **Energia**      | 100 | **150** |
| **Vel. Sprint**  | 1.2  | 1.2 |

> **Polaridades Inatas Ocultas:** Naramon (Traço -), 2x Madurai (Traço V)
> **Slot de Aura Inata:** Madurai (Traço V)

## 🛠️ Guia Builds e Maximização

Os guias avançados centralizam no uso da mecânica do Warframe atrelada à invisibilidade defensiva enquanto priorizam melhorias ofensivas em Dano Verdadeiro. O end-game prescinde normalmente de mods massivos de resiliência e saúde crua. O viés ideal exige o aumento contínuo no status de Força (Strength) somado à estabilidade contínua entre as pausas automáticas das mecânicas ativas de execuções.

#### 🎛️ O Arsenal Essencial e Aquisições Core

| Ferramenta / Mod / Arcano | Categoria Original | Efeito Funcional da Configuração | Como Obter |
| :--- | :--- | :--- | :--- |
| **[[mods/seeking_shuriken.md\|Seeking Shuriken]]** | Mod de Ampliação | Alteração direta da Habilidade 1. Disparos cortantes degradam permanentemente armadura residual. | Origina-se do *[[lore/faccoes/sindicatos/veu_vermelho.md\|Véu Vermelho]]* ou *[[lore/faccoes/sindicatos/arbitros_de_hexis.md\|Árbitros de Hexis]]*. |
| **[[mods/fatal_teleport.md\|Fatal Teleport]]** | Mod de Ampliação | Aprimoramento da Habilidade 3. Adiciona multiplicador automático de +200% de dano finalizador puro. | Origina-se do *[[lore/faccoes/sindicatos/veu_vermelho.md\|Véu Vermelho]]* ou *[[lore/faccoes/sindicatos/arbitros_de_hexis.md\|Árbitros de Hexis]]*. |
| **[[mods/transient_fortitude.md\|Transient Fortitude]]** | Mod Corrompido | Intensifica significativamente a Força de Habilidade bruta com sacrifício tático associado na duração. | Cofres Estelares ([[locais/deimos.md\|Deimos]] Vaults). |

## 🧬 Subsunção e Acoplagem do Helminte

**Poder Cedido Base (Doação [[sistemas/helminte.md|Helminte]]):** **Shuriken**. Ao interagir no sacrifício, Ash Prime cede nativamente em doação permanente esta habilidade. 
Ao otimizar o próprio chassi no recebimento modular, este exemplar apresenta máxima eficiência absorvendo a injeção mecânica do **Silence** (da [[warframes/banshee.md|Banshee]]) encaixável rotacionalmente, acoplada para ativar multiplicadores de danos atordoando inimigos e protegendo os Clones do *Blade Storm*.

## 🔗 Terrenos de Atuação, Sinergia e Lâminas Reais

#### 📍 Compatibilidade de Modalidades de Guerra:

*   **Incursões End-Game Solo ([[missoes/exterminio.md|Extermínios]], [[missoes/sobrevivencia.md|Sobrevivência]]):** Considerável força e sobrevivência inata devida à invisibilidade e capacidade de escalonar "Damage real", ultrapassando defesas ativas no [[sistemas/caminho_de_aco.md|Caminho de Aço]].
*   **Caças Furtivas ([[missoes/espionagem.md|Espionagem]], [[missoes/assassinato.md|Assassinato]]):** Performa de maneira autoconclusiva para operações que exigem restrição de alarmes sistêmicos no território.

#### 🤝 Sinergia em Time:

*   **[[warframes/mag.md|Mag]] / [[warframes/nidus.md|Nidus]]:** Expande margens de lucro tático quando apoiado diretamente por atrações espaciais magnéticas estáticas que confinam os alvos para abate facilitado do Blade Storm.
*   **[[warframes/banshee.md|Banshee]]:** A injeção de Silence escala drasticamente a paralisação tática.

#### ⚔️ Conexões Canônicas com O Arsenal Furtivo:

O design militarizado purista do Ash Prime ratifica e invoca a progressão letal no combate focado em lâminas ancestrais cortantes, especialmente o trançado passivo de golpes de **[[armas/nikana.md|Nikanas]]** ou a aplicação cirúrgica de uso de **[[armas/adagas.md|Adagas]]** operando combinadas com o Mod Assassino nato de "[[mods/covert_lethality.md|Covert Lethality]]". No folclore do Lançamento do Cofre Prime, Ash Prime foi visualmente apresentado de forma canônica atrelado ao rifle sniper **[[armas/vectis_prime.md|Vectis Prime]]** e em suporte tático robótico com o sentinela utilitária **[[companheiros/carrier_prime.md|Carrier Prime]]**, cristalizando assim o estilo militar estrito e autônomo (não necessitando de drops de munição no terreno e atirando oculto na fumaça).
## 🎨 Apresentação e Estilização (Fashion Frame)

O rigor base do chassi Ash Prime compele a arquétipos letais sombrios em fardamentos militarizados restritos, favorecendo intensamente a utilização elementar de paletas monocromáticas.

#### Skins e Geometrias de Destaque
*   **[[cosmeticos/skins/koga_skin.md|Ash Koga]] (Deluxe):** Aborda silhuetas exclusivas com reminiscência limpa a estéticas asiáticas marciais ancestrais.
*   **Skins [[cosmeticos/skins/tennogen.md|TennoGen]]:** Opções originadas pela comunidade que garantem maior customização orgânica ou reforço tático visual sobre as camadas da versão Prime.

#### Padrões de Cores e Paletas Recomendadas
Aconselha-se tonalidades absolutas pretas perante cinzas chumbo estáticos operacionais (Paleta **[[cosmeticos/paletas/smoke_colors.md|Smoke Colors]]**) contrastados por canais de energia puramente alaranjados densos (Paleta **[[cosmeticos/paletas/halloween.md|Halloween]]**), simulando processos ininterruptos de queimas de brasas de carvão vegetal.

----------------------------------------


## Seção: armas
### 📄 arquivo: _Armas _Indice.md

# Armas — Índice

> [!quote]
> *"Uma arma é apenas metal. O Tenno que a empunha é o que a torna letal."*

---

## Visão Geral

Armas em Warframe são o principal meio de combate do Tenno. Dividem-se em quatro categorias de slot: **Primária**, **Secundária**, **Branca (Melee)** e **Archwing**. Cada slot é independente — o jogador equipa uma de cada tipo simultaneamente (exceto Archwing, usado apenas em zonas específicas).

O poder real de uma arma vem dos **Mods equipados**, não do nível base. Stats nativos (dano, critical chance, status chance, fire rate) definem o potencial; os mods amplificam ou redirecionam esse potencial.

---

## Aquisição e Forja

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

---

## Stats e Mecânicas

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

---

## Mastery

Cada arma contribui com **Affinity de Mastery** quando levada ao Rank 30 pela primeira vez:
- **Armas comuns:** 3.000 pontos
- **Armas Prime:** 6.000 pontos (contam separado da versão base)

---

## Sub-Índices

Cada sub-índice cobre mecânicas exclusivas da sua categoria além da lista de armas:

| Sub-Índice | Mecânicas Exclusivas Cobertas |
|---|---|
| [[_Armas _Primarias _Indice\|Primárias]] | Modos de disparo, tipos de munição, punch-through, beam weapons, Incarnon |
| [[_Armas _Secundarias _Indice\|Secundárias]] | Sistema Kitgun modular, armas de arremesso, prefixo Ak- (dual-wield), Incarnon |
| [[_Armas _Brancas _Indice\|Brancas]] | Stances por tipo de arma, combo counter, heavy attacks, finishers, slam attacks |
| [[_Armas _Archwing _Indice\|Archwing]] | Modos espacial/atmosfera/terrestre, Archgun Deployer, Zenith Crown, pool de mods exclusivo |

---

## Lista Completa

### Primárias (129)

| Arma | Tipo | Fonte |
|---|---|---|
| [[acceltra\|Acceltra]] | Rifle de Assalto | Drop (Demolyst Manic, Steel Path) |
| [[acceltra_prime\|Acceltra Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[ambassador\|Ambassador]] | Rifle de Assalto | Drop (Amalgam, Jupiter) |
| [[amprex\|Amprex]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[arca_plasmor\|Arca Plasmor]] | Espingarda | Pesquisa de Clã (Corpus) |
| [[astilla\|Astilla]] | Espingarda | Pesquisa de Clã (Corpus) |
| [[astilla_prime\|Astilla Prime]] | Espingarda | Relíquias (Prime) |
| [[attica\|Attica]] | Arco | Mercado (blueprint) |
| [[battacor\|Battacor]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[baza\|Baza]] | Rifle de Assalto | Mercado (blueprint) |
| [[baza_prime\|Baza Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[boltor\|Boltor]] | Rifle de Assalto | Mercado (blueprint) |
| [[boltor_prime\|Boltor Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[braton\|Braton]] | Rifle de Assalto | Mercado (blueprint) |
| [[braton_prime\|Braton Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[braton_vandal\|Braton Vandal]] | Rifle de Assalto | Evento / Drop (Acolytes) |
| [[buzlok\|Buzlok]] | Rifle de Assalto | Mercado (blueprint) |
| [[cedo\|Cedo]] | Espingarda | Pesquisa de Clã (Entrati) |
| [[cernos\|Cernos]] | Arco | Mercado (blueprint) |
| [[cernos_prime\|Cernos Prime]] | Arco | Relíquias (Prime) |
| [[convectrix\|Convectrix]] | Espingarda | Pesquisa de Clã (Corpus) |
| [[corinth\|Corinth]] | Espingarda | Mercado (blueprint) |
| [[corinth_prime\|Corinth Prime]] | Espingarda | Relíquias (Prime) |
| [[daikyu\|Daikyu]] | Arco | Mercado (blueprint) |
| [[dera\|Dera]] | Rifle de Assalto | Mercado (blueprint) |
| [[dera_vandal\|Dera Vandal]] | Rifle de Assalto | Nightwave / Evento |
| [[dex_sybaris\|Dex Sybaris]] | Rifle Semi-Auto | Evento (Aniversário DE) |
| [[drakgoon\|Drakgoon]] | Espingarda | Mercado (blueprint) |
| [[exergis\|Exergis]] | Espingarda | Pesquisa de Clã (Corpus) |
| [[felarx\|Felarx]] | Incarnon | Incarnon (Duviri) |
| [[ferrox\|Ferrox]] | Rifle Especial | Mercado (blueprint) |
| [[flux_rifle\|Flux Rifle]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[fulmin\|Fulmin]] | Rifle Especial | Drop (Amalgam, Jupiter) |
| [[fulmin_prime\|Fulmin Prime]] | Rifle Especial | Relíquias (Prime) |
| [[glaxion\|Glaxion]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[glaxion_vandal\|Glaxion Vandal]] | Rifle de Assalto | Nightwave / Evento |
| [[gorgon\|Gorgon]] | Rifle de Assalto | Mercado (blueprint) |
| [[gorgon_wraith\|Gorgon Wraith]] | Rifle de Assalto | Nightwave / Evento |
| [[grakata\|Grakata]] | Rifle de Assalto | Mercado (blueprint) |
| [[harpak\|Harpak]] | Rifle Especial | Mercado (blueprint) |
| [[hek\|Hek]] | Espingarda | Mercado (blueprint) |
| [[hind\|Hind]] | Rifle de Assalto | Mercado (blueprint) |
| [[ignis\|Ignis]] | Lança-Chamas | Pesquisa de Clã (Grineer) |
| [[ignis_wraith\|Ignis Wraith]] | Lança-Chamas | Pesquisa de Clã (blueprint tradável) / Evento |
| [[javlok\|Javlok]] | Lançador | Mercado (blueprint) |
| [[karak\|Karak]] | Rifle de Assalto | Mercado (blueprint) |
| [[karak_wraith\|Karak Wraith]] | Rifle de Assalto | Evento / Drop (Acolytes) |
| [[kohm\|Kohm]] | Espingarda | Mercado (blueprint) |
| [[komorex\|Komorex]] | Sniper | Pesquisa de Clã (Corpus) |
| [[kuva_bramma\|Kuva Bramma]] | Lançador | Kuva Lich |
| [[kuva_chakkhurr\|Kuva Chakkhurr]] | Sniper | Kuva Lich |
| [[kuva_hek\|Kuva Hek]] | Espingarda | Kuva Lich |
| [[kuva_ogris\|Kuva Ogris]] | Lançador | Kuva Lich |
| [[kuva_quartakk\|Kuva Quartakk]] | Rifle de Assalto | Kuva Lich |
| [[kuva_tonkor\|Kuva Tonkor]] | Lançador | Kuva Lich |
| [[kuva_zarr\|Kuva Zarr]] | Lançador | Kuva Lich |
| [[lanka\|Lanka]] | Sniper | Mercado (blueprint) |
| [[latron\|Latron]] | Rifle Semi-Auto | Mercado (blueprint) |
| [[latron_prime\|Latron Prime]] | Rifle Semi-Auto | Relíquias (Prime) |
| [[latron_wraith\|Latron Wraith]] | Rifle Semi-Auto | Nightwave / Evento |
| [[lenz\|Lenz]] | Arco | Mercado (blueprint) |
| [[miter\|Miter]] | Lançador | Mercado (blueprint) |
| [[mk1_braton\|MK1-Braton]] | Rifle de Assalto | Starter / Mercado |
| [[mutalist_quanta\|Mutalist Quanta]] | Lançador | Drop (Invasões Infested, Eris) |
| [[nataruk\|Nataruk]] | Arco | Nakak, Cetus (pós The New War) |
| [[ogris\|Ogris]] | Lançador | Mercado (blueprint) |
| [[opticor\|Opticor]] | Sniper | Pesquisa de Clã (Corpus) |
| [[opticor_vandal\|Opticor Vandal]] | Sniper | Nightwave / Evento |
| [[panthera\|Panthera]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[panthera_prime\|Panthera Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[paracyst\|Paracyst]] | Rifle Especial | Mercado (blueprint) |
| [[paris\|Paris]] | Arco | Mercado (blueprint) |
| [[paris_prime\|Paris Prime]] | Arco | Relíquias (Prime) |
| [[penta\|Penta]] | Lançador | Mercado (blueprint) |
| [[phantasma\|Phantasma]] | Espingarda | Pesquisa de Clã (Entrati) |
| [[phantasma_prime\|Phantasma Prime]] | Espingarda | Relíquias (Prime) |
| [[phenmor\|Phenmor]] | Incarnon | Incarnon (Duviri) |
| [[prisma_grakata\|Prisma Grakata]] | Rifle de Assalto | Baro Ki'Teer / Nightwave |
| [[proboscis_cernos\|Proboscis Cernos]] | Arco | Pesquisa de Clã (Entrati) |
| [[quanta\|Quanta]] | Lançador | Pesquisa de Clã (Corpus) |
| [[quanta_vandal\|Quanta Vandal]] | Lançador | Nightwave / Evento |
| [[rakta_cernos\|Rakta Cernos]] | Arco | Sindicato (Red Veil) |
| [[rubico\|Rubico]] | Sniper | Mercado (blueprint) |
| [[rubico_prime\|Rubico Prime]] | Sniper | Relíquias (Prime) |
| [[sancti_tigris\|Sancti Tigris]] | Espingarda | Sindicato (New Loka) |
| [[scourge\|Scourge]] | Lançador | Pesquisa de Clã (Entrati) |
| [[scourge_prime\|Scourge Prime]] | Lançador | Relíquias (Prime) |
| [[secura_penta\|Secura Penta]] | Lançador | Sindicato (Perrin Sequence) |
| [[shedu\|Shedu]] | Rifle Especial | Drop (Sentients, Murex — Empyrean) |
| [[simulor\|Simulor]] | Lançador | Pesquisa de Clã (Corpus) |
| [[snipetron\|Snipetron]] | Sniper | Baro Ki'Teer |
| [[snipetron_vandal\|Snipetron Vandal]] | Sniper | Evento |
| [[sobek\|Sobek]] | Espingarda | Mercado (blueprint) |
| [[soma\|Soma]] | Rifle de Assalto | Mercado (blueprint) |
| [[soma_prime\|Soma Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[sporothrix\|Sporothrix]] | Arco | Pesquisa de Clã (Entrati) |
| [[stahlta\|Stahlta]] | Rifle de Assalto | Pesquisa de Clã (Entrati) |
| [[stradavar\|Stradavar]] | Rifle de Assalto | Mercado (blueprint) |
| [[stradavar_prime\|Stradavar Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[strun\|Strun]] | Espingarda | Mercado (blueprint) |
| [[strun_wraith\|Strun Wraith]] | Espingarda | Nightwave / Evento |
| [[supra\|Supra]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[supra_vandal\|Supra Vandal]] | Rifle de Assalto | Nightwave / Evento |
| [[sybaris\|Sybaris]] | Rifle Semi-Auto | Mercado (blueprint) |
| [[sybaris_prime\|Sybaris Prime]] | Rifle Semi-Auto | Relíquias (Prime) |
| [[synoid_simulor\|Synoid Simulor]] | Lançador | Sindicato (Cephalon Suda) |
| [[telos_boltor\|Telos Boltor]] | Rifle de Assalto | Sindicato (Arbiters of Hexis) |
| [[tenet_arca_plasmor\|Tenet Arca Plasmor]] | Espingarda | Irmãs de Parvos |
| [[tenet_envoy\|Tenet Envoy]] | Lançador | Irmãs de Parvos |
| [[tenet_ferrox\|Tenet Ferrox]] | Rifle Especial | Irmãs de Parvos |
| [[tenet_flux_rifle\|Tenet Flux Rifle]] | Rifle de Assalto | Irmãs de Parvos |
| [[tenora\|Tenora]] | Rifle de Assalto | Mercado (blueprint) |
| [[tenora_prime\|Tenora Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[tiberon\|Tiberon]] | Rifle de Assalto | Mercado (blueprint) |
| [[tiberon_prime\|Tiberon Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[tigris\|Tigris]] | Espingarda | Mercado (blueprint) |
| [[tigris_prime\|Tigris Prime]] | Espingarda | Relíquias (Prime) |
| [[tonkor\|Tonkor]] | Lançador | Mercado (blueprint) |
| [[trumna\|Trumna]] | Lançador | Pesquisa de Clã (Entrati) |
| [[vaykor_hek\|Vaykor Hek]] | Espingarda | Sindicato (Steel Meridian) |
| [[vectis\|Vectis]] | Sniper | Mercado (blueprint) |
| [[vectis_prime\|Vectis Prime]] | Sniper | Relíquias (Prime) |
| [[veldt\|Veldt]] | Rifle de Assalto | Mercado (blueprint) |
| [[vermisplicer\|Vermisplicer]] | Espingarda | Pesquisa de Clã (Entrati) |
| [[vulkar\|Vulkar]] | Sniper | Mercado (blueprint) |
| [[vulkar_wraith\|Vulkar Wraith]] | Sniper | Nightwave / Evento |
| [[zarr\|Zarr]] | Lançador | Mercado (blueprint) |
| [[zhuge\|Zhuge]] | Arco | Mercado (blueprint) |
| [[zhuge_prime\|Zhuge Prime]] | Arco | Relíquias (Prime) |

---

### Secundárias (93)

| Arma | Tipo | Fonte |
|---|---|---|
| [[acrid\|Acrid]] | Especial | Drop (Invasões Infested) |
| [[akarius\|Akarius]] | Pistolas Duplas | Pesquisa de Clã (Entrati) |
| [[akbolto\|Akbolto]] | Pistolas Duplas | Mercado (2× Bolto) |
| [[akbolto_prime\|Akbolto Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[akjagara\|Akjagara]] | Pistolas Duplas | Mercado (blueprint) |
| [[akjagara_prime\|Akjagara Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[aklex\|Aklex]] | Pistolas Duplas | Mercado (2× Lex) |
| [[aklex_prime\|Aklex Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[aksomati\|Aksomati]] | Pistolas Duplas | Pesquisa de Clã (Corpus) |
| [[aksomati_prime\|Aksomati Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[akstiletto\|Akstiletto]] | Pistolas Duplas | Mercado (blueprint) |
| [[akstiletto_prime\|Akstiletto Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[akvasto\|Akvasto]] | Pistolas Duplas | Mercado (2× Vasto) |
| [[akvasto_prime\|Akvasto Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[akzani\|Akzani]] | Pistolas Duplas | Pesquisa de Clã (Cetus) |
| [[arca_scisco\|Arca Scisco]] | Pistola | Pesquisa de Clã (Corpus) |
| [[athodai\|Athodai]] | Pistola | Fortuna (Old Mate, rank 5) |
| [[atomos\|Atomos]] | Especial | Pesquisa de Clã (Corpus) |
| [[azima\|Azima]] | Especial | Nightwave / Evento |
| [[ballistica\|Ballistica]] | Arco Secundário | Mercado (blueprint) |
| [[ballistica_prime\|Ballistica Prime]] | Arco Secundário | Relíquias (Prime) |
| [[bolto\|Bolto]] | Pistola | Mercado (blueprint) |
| [[brakk\|Brakk]] | Pistola | Drop (Grustrag Three) / Invasões |
| [[bronco\|Bronco]] | Pistola | Mercado (blueprint) |
| [[bronco_prime\|Bronco Prime]] | Pistola | Relíquias (Prime) |
| [[bubonico\|Bubonico]] | Canhão de Braço | Pesquisa de Clã (Entrati) |
| [[castanas\|Castanas]] | Arremesso | Mercado (blueprint) |
| [[catchmoon\|Catchmoon]] | Kitgun | Kitgun (Fortuna) |
| [[cyanex\|Cyanex]] | Especial | Pesquisa de Clã (Entrati) |
| [[despair\|Despair]] | Arremesso | Drop (Stalker) |
| [[detron\|Detron]] | Pistola | Drop (Corrupted, Void) |
| [[dex_furis\|Dex Furis]] | Pistola | Evento (Aniversário DE) |
| [[embolist\|Embolist]] | Especial | Pesquisa de Clã (Grineer) |
| [[epitaph\|Epitaph]] | Pistola | Pesquisa de Clã (Entrati) |
| [[euphona_prime\|Euphona Prime]] | Pistola | Relíquias (Prime) |
| [[furis\|Furis]] | Pistola | Mercado (blueprint) |
| [[fusilai\|Fusilai]] | Arremesso | Nakak, Cetus (caça) |
| [[gammacor\|Gammacor]] | Especial | Pesquisa de Clã (Corpus) |
| [[gaze\|Gaze]] | Kitgun | Kitgun (Fortuna) |
| [[hikou\|Hikou]] | Arremesso | Mercado (blueprint) |
| [[hikou_prime\|Hikou Prime]] | Arremesso | Relíquias (Prime) |
| [[knell\|Knell]] | Pistola | Pesquisa de Clã (Quills, Cetus) |
| [[knell_prime\|Knell Prime]] | Pistola | Relíquias (Prime) |
| [[kohmak\|Kohmak]] | Especial | Pesquisa de Clã (Corpus) |
| [[kompressa\|Kompressa]] | Especial | Pesquisa de Clã (Entrati) |
| [[kulstar\|Kulstar]] | Especial | Pesquisa de Clã (Grineer) |
| [[kuva_brakk\|Kuva Brakk]] | Pistola | Kuva Lich |
| [[kuva_nukor\|Kuva Nukor]] | Pistola | Kuva Lich |
| [[kuva_seer\|Kuva Seer]] | Pistola | Kuva Lich |
| [[kuva_twin_stubbas\|Kuva Twin Stubbas]] | Pistolas Duplas | Kuva Lich |
| [[laetum\|Laetum]] | Incarnon | Incarnon (Duviri) |
| [[lato\|Lato]] | Pistola | Starter / Mercado |
| [[lato_prime\|Lato Prime]] | Pistola | Indisponível (Founder's Pack, 2013) |
| [[lato_vandal\|Lato Vandal]] | Pistola | Nightwave / Evento |
| [[lex\|Lex]] | Pistola | Mercado (blueprint) |
| [[lex_prime\|Lex Prime]] | Pistola | Relíquias (Prime) |
| [[magnus\|Magnus]] | Pistola | Mercado (blueprint) |
| [[magnus_prime\|Magnus Prime]] | Pistola | Relíquias (Prime) |
| [[mara_detron\|Mara Detron]] | Pistola | Baro Ki'Teer |
| [[nukor\|Nukor]] | Pistola | Pesquisa de Clã (Corpus) |
| [[ocucor\|Ocucor]] | Especial | Pesquisa de Clã (Entrati) |
| [[pandero\|Pandero]] | Pistola | Mercado (blueprint) |
| [[pandero_prime\|Pandero Prime]] | Pistola | Relíquias (Prime) |
| [[rattleguts\|Rattleguts]] | Kitgun | Kitgun (Fortuna) |
| [[sancti_castanas\|Sancti Castanas]] | Arremesso | Sindicato (New Loka) |
| [[seer\|Seer]] | Pistola | Drop (Vor, Mercury — Tolstoj) |
| [[sicarus\|Sicarus]] | Pistola | Mercado (blueprint) |
| [[sicarus_prime\|Sicarus Prime]] | Pistola | Relíquias (Prime) |
| [[sonicor\|Sonicor]] | Especial | Pesquisa de Clã (Corpus) |
| [[spira\|Spira]] | Arremesso | Mercado (blueprint) |
| [[spira_prime\|Spira Prime]] | Arremesso | Relíquias (Prime) |
| [[staticor\|Staticor]] | Especial | Pesquisa de Clã (Corpus) |
| [[stubba\|Stubba]] | Especial | Pesquisa de Clã (Grineer) |
| [[stug\|Stug]] | Especial | Pesquisa de Clã (Corpus) |
| [[synoid_gammacor\|Synoid Gammacor]] | Especial | Sindicato (Cephalon Suda) |
| [[tenet_agendus\|Tenet Agendus]] | Especial | Irmãs de Parvos |
| [[tenet_cycron\|Tenet Cycron]] | Especial | Irmãs de Parvos |
| [[tenet_detron\|Tenet Detron]] | Pistola | Irmãs de Parvos |
| [[tenet_diplos\|Tenet Diplos]] | Pistolas Duplas | Irmãs de Parvos |
| [[tenet_plinx\|Tenet Plinx]] | Pistola | Irmãs de Parvos |
| [[tenet_spirex\|Tenet Spirex]] | Especial | Irmãs de Parvos |
| [[tombfinger\|Tombfinger]] | Kitgun | Kitgun (Fortuna) |
| [[twin_grakata\|Twin Grakata]] | Pistolas Duplas | Mercado (blueprint) |
| [[twin_vipers\|Twin Vipers]] | Pistolas Duplas | Mercado (blueprint) |
| [[twin_vipers_wraith\|Twin Vipers Wraith]] | Pistolas Duplas | Nightwave / Evento |
| [[vasto\|Vasto]] | Pistola | Mercado (blueprint) |
| [[vasto_prime\|Vasto Prime]] | Pistola | Relíquias (Prime) |
| [[velox\|Velox]] | Pistola | Drop (Corpus, Orb Vallis) |
| [[viper\|Viper]] | Pistola | Mercado (blueprint) |
| [[viper_wraith\|Viper Wraith]] | Pistola | Nightwave / Evento |
| [[zakti\|Zakti]] | Arremesso | Mercado (blueprint) |
| [[zakti_prime\|Zakti Prime]] | Arremesso | Relíquias (Prime) |
| [[zylok\|Zylok]] | Pistola | Nightwave / Evento |

---

### Brancas — Melee (135)

| Arma | Tipo | Fonte |
|---|---|---|
| [[ack_and_brunt\|Ack e Brunt]] | Espada e Escudo | Pesquisa de Clã (Grineer) |
| [[anku\|Anku]] | Foice | Pesquisa de Clã (Grineer) |
| [[arca_titron\|Arca Titron]] | Martelo | Pesquisa de Clã (Corpus) |
| [[arum_spinosa\|Arum Spinosa]] | Lâmina e Chicote | Pesquisa de Clã (Entrati) |
| [[atterax\|Atterax]] | Chicote | Mercado (blueprint) |
| [[bo\|Bo]] | Cajado | Mercado (blueprint) |
| [[bo_prime\|Bo Prime]] | Cajado | Relíquias (Prime) |
| [[boltace\|Boltace]] | Espadas Duplas | Pesquisa de Clã (Corpus) |
| [[broken_sword\|Broken Sword]] | Espada | Drop (Stalker) |
| [[broken_war\|Broken War]] | Espada | Drop (Stalker — partes de War) |
| [[ceramic_dagger\|Ceramic Dagger]] | Adaga | Mercado (blueprint) |
| [[cobra_and_crane\|Cobra e Crane]] | Espada e Escudo | Pesquisa de Clã (Grineer) |
| [[cronus\|Cronus]] | Espada | Drop (Ambulas, Pluto) |
| [[dakra_prime\|Dakra Prime]] | Espada | Relíquias (Prime) |
| [[dark_dagger\|Dark Dagger]] | Adaga | Mercado (blueprint) |
| [[dark_split_sword\|Dark Split-Sword]] | Espada Pesada / Dupla | Mercado (blueprint) |
| [[dark_sword\|Dark Sword]] | Espada | Mercado (blueprint) |
| [[destreza\|Destreza]] | Espadim | Mercado (blueprint) |
| [[destreza_prime\|Destreza Prime]] | Espadim | Relíquias (Prime) |
| [[dragon_nikana\|Dragon Nikana]] | Espada | Mercado (blueprint + componentes Clã) |
| [[dual_cleavers\|Dual Cleavers]] | Espadas Duplas | Mercado (blueprint) |
| [[dual_ether\|Dual Ether]] | Espadas Duplas | Mercado (blueprint) |
| [[dual_heat_swords\|Dual Heat Swords]] | Espadas Duplas | Mercado (blueprint) |
| [[dual_ichor\|Dual Ichor]] | Espadas Duplas | Mercado (blueprint) |
| [[dual_kamas\|Dual Kamas]] | Espadas Duplas | Mercado (blueprint) |
| [[dual_kamas_prime\|Dual Kamas Prime]] | Espadas Duplas | Relíquias (Prime) |
| [[dual_skana\|Dual Skana]] | Espadas Duplas | Mercado (blueprint) |
| [[dual_zoren\|Dual Zoren]] | Espadas Duplas | Mercado (blueprint) |
| [[ether_daggers\|Ether Daggers]] | Adagas Duplas | Mercado (blueprint) |
| [[ether_reaper\|Ether Reaper]] | Foice | Mercado (blueprint) |
| [[ether_sword\|Ether Sword]] | Espada | Mercado (blueprint) |
| [[fang\|Fang]] | Espadas Duplas | Mercado (blueprint) |
| [[fang_prime\|Fang Prime]] | Espadas Duplas | Relíquias (Prime) |
| [[fragor\|Fragor]] | Martelo | Mercado (blueprint) |
| [[fragor_prime\|Fragor Prime]] | Martelo | Relíquias (Prime) |
| [[furax\|Furax]] | Garras | Mercado (blueprint) |
| [[furax_wraith\|Furax Wraith]] | Garras | Nightwave / Evento |
| [[galatine\|Galatine]] | Espada Pesada | Mercado (blueprint) |
| [[galatine_prime\|Galatine Prime]] | Espada Pesada | Relíquias (Prime) |
| [[galvacord\|Galvacord]] | Chicote | Pesquisa de Clã (Grineer) |
| [[glaive\|Glaive]] | Glaive | Mercado (blueprint) |
| [[glaive_prime\|Glaive Prime]] | Glaive | Relíquias (Prime) |
| [[gram\|Gram]] | Espada Pesada | Mercado (blueprint) |
| [[gram_prime\|Gram Prime]] | Espada Pesada | Relíquias (Prime) |
| [[guandao\|Guandao]] | Lança | Mercado (blueprint) |
| [[guandao_prime\|Guandao Prime]] | Lança | Relíquias (Prime) |
| [[halikar\|Halikar]] | Glaive | Mercado (blueprint) |
| [[halikar_wraith\|Halikar Wraith]] | Glaive | Nightwave / Evento |
| [[hate\|Hate]] | Foice | Drop (Stalker) |
| [[heat_sword\|Heat Sword]] | Espada | Mercado (blueprint) |
| [[hirudo\|Hirudo]] | Garras | Pesquisa de Clã (Grineer) |
| [[innodem\|Innodem]] | Espada | Pesquisa de Clã (Entrati) |
| [[jat_kittag\|Jat Kittag]] | Martelo | Mercado (blueprint) |
| [[jat_kusar\|Jat Kusar]] | Cajado | Pesquisa de Clã (Corpus) |
| [[jaw_sword\|Jaw Sword]] | Espada | Mercado (blueprint) |
| [[karyst\|Karyst]] | Adaga | Mercado (blueprint) |
| [[karyst_prime\|Karyst Prime]] | Adaga | Relíquias (Prime) |
| [[kesheg\|Kesheg]] | Lança | Pesquisa de Clã (Grineer) |
| [[kestrel\|Kestrel]] | Glaive | Mercado (blueprint) |
| [[krohkur\|Krohkur]] | Espada | Mercado (blueprint) |
| [[kronen\|Kronen]] | Tonfa | Pesquisa de Clã (Corpus) |
| [[kronen_prime\|Kronen Prime]] | Tonfa | Relíquias (Prime) |
| [[kuva_shildeg\|Kuva Shildeg]] | Martelo | Kuva Lich |
| [[lacera\|Lacera]] | Lâmina e Chicote | Pesquisa de Clã (Corpus) |
| [[lecta\|Lecta]] | Chicote | Mercado (blueprint) |
| [[lesion\|Lesion]] | Lança | Pesquisa de Clã (Entrati) |
| [[machete\|Machete]] | Facão | Mercado (blueprint) |
| [[machete_wraith\|Machete Wraith]] | Facão | Nightwave / Evento |
| [[magistar\|Magistar]] | Martelo | Pesquisa de Clã (Grineer) |
| [[magistar_wraith\|Magistar Wraith]] | Martelo | Nightwave / Evento |
| [[mios\|Mios]] | Lâmina e Chicote | Pesquisa de Clã (Entrati) |
| [[mire\|Mire]] | Espada | Drop (Ambulas, Pluto) |
| [[nami_duo\|Nami Duo]] | Espadas Duplas | Pesquisa de Clã (Corpus) |
| [[nami_solo\|Nami Solo]] | Espada | Pesquisa de Clã (Corpus) |
| [[nikana\|Nikana]] | Espada | Mercado (blueprint) |
| [[nikana_prime\|Nikana Prime]] | Espada | Relíquias (Prime) |
| [[ninkondi\|Ninkondi]] | Nunchaku | Pesquisa de Clã (Corpus) |
| [[ninkondi_prime\|Ninkondi Prime]] | Nunchaku | Relíquias (Prime) |
| [[ohma\|Ohma]] | Tonfa | Pesquisa de Clã (Corpus) |
| [[okina\|Okina]] | Espadas Duplas | Pesquisa de Clã (Corpus) |
| [[okina_prime\|Okina Prime]] | Espadas Duplas | Relíquias (Prime) |
| [[orthos\|Orthos]] | Lança | Mercado (blueprint) |
| [[orthos_prime\|Orthos Prime]] | Lança | Relíquias (Prime) |
| [[orvius\|Orvius]] | Glaive | Quest (Chains of Harrow) |
| [[pangolin_prime\|Pangolin Prime]] | Espada | Relíquias (Prime) |
| [[pangolin_sword\|Pangolin Sword]] | Espada | Mercado (blueprint) |
| [[paracesis\|Paracesis]] | Espada Pesada | Quest (The Sacrifice) |
| [[pennant\|Pennant]] | Espada Pesada | Pesquisa de Clã (Entrati) |
| [[plasma_sword\|Plasma Sword]] | Espada | Mercado (blueprint) |
| [[praedos\|Praedos]] | Tonfa | Pesquisa de Clã (Entrati) |
| [[prisma_dual_cleavers\|Prisma Dual Cleavers]] | Espadas Duplas | Baro Ki'Teer |
| [[prisma_skana\|Prisma Skana]] | Espada | Baro Ki'Teer |
| [[prova\|Prova]] | Lança | Pesquisa de Clã (Corpus) |
| [[prova_vandal\|Prova Vandal]] | Lança | Nightwave / Evento |
| [[pulmonars\|Pulmonars]] | Leques | Pesquisa de Clã (Entrati) |
| [[rakta_dark_dagger\|Rakta Dark Dagger]] | Adaga | Sindicato (Red Veil) |
| [[reaper_prime\|Reaper Prime]] | Foice | Relíquias (Prime) |
| [[redeemer\|Redeemer]] | Espingarda Melee | Pesquisa de Clã (Tenno) |
| [[redeemer_prime\|Redeemer Prime]] | Espingarda Melee | Relíquias (Prime) |
| [[ripkas\|Ripkas]] | Garras | Pesquisa de Clã (Grineer) |
| [[sarpa\|Sarpa]] | Espingarda Melee | Pesquisa de Clã (Tenno) |
| [[scoliac\|Scoliac]] | Chicote | Pesquisa de Clã (Grineer) |
| [[secura_lecta\|Secura Lecta]] | Chicote | Sindicato (Perrin Sequence) |
| [[shaku\|Shaku]] | Cajado | Pesquisa de Clã (Corpus) |
| [[sheev\|Sheev]] | Adaga | Pesquisa de Clã (Grineer) |
| [[sigma_and_octantis\|Sigma e Octantis]] | Espada e Escudo | Evento (Aniversário DE) |
| [[silva_and_aegis\|Silva e Aegis]] | Espada e Escudo | Mercado (blueprint) |
| [[silva_and_aegis_prime\|Silva e Aegis Prime]] | Espada e Escudo | Relíquias (Prime) |
| [[skana\|Skana]] | Espada | Starter / Mercado |
| [[skana_prime\|Skana Prime]] | Espada | Relíquias (Prime) |
| [[skiajati\|Skiajati]] | Espada | Quest (The Sacrifice) |
| [[stiletto_prime\|Stiletto Prime]] | Adaga | Relíquias (Prime) |
| [[stropha\|Stropha]] | Espingarda Melee | Pesquisa de Clã (Tenno) |
| [[sydon\|Sydon]] | Lança | Pesquisa de Clã (Grineer) |
| [[tatsu\|Tatsu]] | Espada Pesada | Pesquisa de Clã (Entrati) |
| [[tatsu_prime\|Tatsu Prime]] | Espada Pesada | Relíquias (Prime) |
| [[tekko\|Tekko]] | Garras | Mercado (blueprint) |
| [[tekko_prime\|Tekko Prime]] | Garras | Relíquias (Prime) |
| [[telos_boltace\|Telos Boltace]] | Espadas Duplas | Sindicato (Arbiters of Hexis) |
| [[tenet_exec\|Tenet Exec]] | Espada Pesada | Irmãs de Parvos |
| [[tenet_grigori\|Tenet Grigori]] | Foice | Irmãs de Parvos |
| [[tenet_livia\|Tenet Livia]] | Espadim | Irmãs de Parvos |
| [[tipedo\|Tipedo]] | Lança | Mercado (blueprint) |
| [[tipedo_prime\|Tipedo Prime]] | Lança | Relíquias (Prime) |
| [[tonbo\|Tonbo]] | Lança | Pesquisa de Clã (Grineer) |
| [[twin_basolk\|Twin Basolk]] | Adagas Duplas | Pesquisa de Clã (Grineer) |
| [[vastilok\|Vastilok]] | Espingarda Melee | Pesquisa de Clã (Tenno) |
| [[vaykor_sydon\|Vaykor Sydon]] | Lança | Sindicato (Steel Meridian) |
| [[venka\|Venka]] | Garras | Pesquisa de Clã (Grineer) |
| [[venka_prime\|Venka Prime]] | Garras | Relíquias (Prime) |
| [[vitrica\|Vitrica]] | Espada Pesada | Pesquisa de Clã (Entrati) |
| [[volnus\|Volnus]] | Martelo | Pesquisa de Clã (Corpus) |
| [[volnus_prime\|Volnus Prime]] | Martelo | Relíquias (Prime) |
| [[war\|War]] | Espada Pesada | Drop (Stalker) |
| [[xoris\|Xoris]] | Glaive | Quest (The Deadlock Protocol) |

---

### Archwing (23)

| Arma | Tipo | Fonte |
|---|---|---|
| [[centaur\|Centaur]] | Arch-Melee | Pesquisa de Clã (Tenno) |
| [[cortege\|Cortege]] | Arch-Gun | Pesquisa de Clã (Entrati) |
| [[corvas\|Corvas]] | Arch-Gun | Pesquisa de Clã (Grineer) |
| [[corvas_prime\|Corvas Prime]] | Arch-Gun | Relíquias (Prime) |
| [[cyngas\|Cyngas]] | Arch-Gun | Pesquisa de Clã (Corpus) |
| [[dual_decurion\|Dual Decurion]] | Arch-Gun | Pesquisa de Clã (Corpus) |
| [[fluctus\|Fluctus]] | Arch-Gun | Pesquisa de Clã (Corpus) |
| [[grattler\|Grattler]] | Arch-Gun | Pesquisa de Clã (Grineer) |
| [[imperator\|Imperator]] | Arch-Gun | Mercado (blueprint) / Starter |
| [[imperator_vandal\|Imperator Vandal]] | Arch-Gun | Drop (Archwing missions) / Baro Ki'Teer |
| [[kaszas\|Kaszas]] | Arch-Melee | Pesquisa de Clã (Grineer) |
| [[knux\|Knux]] | Arch-Melee | Pesquisa de Clã (Corpus) |
| [[kuva_ayanga\|Kuva Ayanga]] | Arch-Gun | Kuva Lich |
| [[kuva_grattler\|Kuva Grattler]] | Arch-Gun | Kuva Lich |
| [[larkspur\|Larkspur]] | Arch-Gun | Pesquisa de Clã (Entrati) |
| [[larkspur_prime\|Larkspur Prime]] | Arch-Gun | Relíquias (Prime) |
| [[mausolon\|Mausolon]] | Arch-Gun | Pesquisa de Clã (Entrati) |
| [[morgha\|Morgha]] | Arch-Gun | Pesquisa de Clã (Entrati) |
| [[onorix\|Onorix]] | Arch-Melee | Pesquisa de Clã (Grineer) |
| [[phaedra\|Phaedra]] | Arch-Gun | Pesquisa de Clã (Corpus) |
| [[prisma_veritux\|Prisma Veritux]] | Arch-Melee | Baro Ki'Teer |
| [[velocitus\|Velocitus]] | Arch-Gun | Pesquisa de Clã (Corpus) |
| [[veritux\|Veritux]] | Arch-Melee | Pesquisa de Clã (Tenno) |

---

## Por Tipo

### Primárias
**Rifles de Assalto:** [[braton|Braton]] · [[soma|Soma]] · [[boltor|Boltor]] · [[tiberon|Tiberon]] · [[grakata|Grakata]] · [[tenora|Tenora]] · [[acceltra|Acceltra]] · [[stradavar|Stradavar]] · [[baza|Baza]] · [[karak|Karak]] · [[hind|Hind]] · [[supra|Supra]] · [[gorgon|Gorgon]] · [[amprex|Amprex]] · [[battacor|Battacor]] · [[panthera|Panthera]] · [[veldt|Veldt]] · [[stahlta|Stahlta]] · [[dera|Dera]] · [[glaxion|Glaxion]] · [[flux_rifle|Flux Rifle]] · [[buzlok|Buzlok]]

**Espingardas:** [[hek|Hek]] · [[sobek|Sobek]] · [[corinth|Corinth]] · [[tigris|Tigris]] · [[arca_plasmor|Arca Plasmor]] · [[cedo|Cedo]] · [[kohm|Kohm]] · [[astilla|Astilla]] · [[phantasma|Phantasma]] · [[drakgoon|Drakgoon]] · [[exergis|Exergis]] · [[convectrix|Convectrix]] · [[strun|Strun]] · [[vermisplicer|Vermisplicer]]

**Snipers:** [[rubico|Rubico]] · [[lanka|Lanka]] · [[vectis|Vectis]] · [[opticor|Opticor]] · [[komorex|Komorex]] · [[vulkar|Vulkar]] · [[snipetron|Snipetron]] · [[kuva_chakkhurr|Kuva Chakkhurr]]

**Arcos:** [[paris|Paris]] · [[cernos|Cernos]] · [[daikyu|Daikyu]] · [[nataruk|Nataruk]] · [[lenz|Lenz]] · [[zhuge|Zhuge]] · [[attica|Attica]] · [[sporothrix|Sporothrix]] · [[rakta_cernos|Rakta Cernos]] · [[proboscis_cernos|Proboscis Cernos]] · [[kuva_bramma|Kuva Bramma]]

**Lançadores:** [[ogris|Ogris]] · [[tonkor|Tonkor]] · [[zarr|Zarr]] · [[penta|Penta]] · [[simulor|Simulor]] · [[quanta|Quanta]] · [[tenet_envoy|Tenet Envoy]] · [[trumna|Trumna]] · [[scourge|Scourge]] · [[javlok|Javlok]] · [[mutalist_quanta|Mutalist Quanta]] · [[miter|Miter]]

**Especiais/Incarnon:** [[ignis|Ignis]] · [[ferrox|Ferrox]] · [[fulmin|Fulmin]] · [[shedu|Shedu]] · [[phenmor|Phenmor]] · [[felarx|Felarx]] · [[ambassador|Ambassador]] · [[paracyst|Paracyst]] · [[harpak|Harpak]]

### Secundárias
**Pistolas:** [[lex|Lex]] · [[magnus|Magnus]] · [[vasto|Vasto]] · [[sicarus|Sicarus]] · [[bronco|Bronco]] · [[detron|Detron]] · [[seer|Seer]] · [[nukor|Nukor]] · [[pandero|Pandero]] · [[knell|Knell]] · [[epitaph|Epitaph]] · [[laetum|Laetum]] · [[athodai|Athodai]] · [[brakk|Brakk]] · [[lato|Lato]]

**Pistolas Duplas:** [[aklex|Aklex]] · [[akbolto|Akbolto]] · [[akstiletto|Akstiletto]] · [[aksomati|Aksomati]] · [[akjagara|Akjagara]] · [[akvasto|Akvasto]] · [[twin_vipers|Twin Vipers]] · [[twin_grakata|Twin Grakata]] · [[akzani|Akzani]] · [[akarius|Akarius]] · [[tenet_diplos|Tenet Diplos]] · [[kuva_twin_stubbas|Kuva Twin Stubbas]]

**Arremesso:** [[despair|Despair]] · [[hikou|Hikou]] · [[spira|Spira]] · [[fusilai|Fusilai]] · [[castanas|Castanas]] · [[zakti|Zakti]]

**Kitguns:** [[rattleguts|Rattleguts]] · [[catchmoon|Catchmoon]] · [[tombfinger|Tombfinger]] · [[gaze|Gaze]]

**Especiais/Incarnon:** [[gammacor|Gammacor]] · [[staticor|Staticor]] · [[sonicor|Sonicor]] · [[cyanex|Cyanex]] · [[kompressa|Kompressa]] · [[tenet_cycron|Tenet Cycron]] · [[ocucor|Ocucor]] · [[atomos|Atomos]] · [[bubonico|Bubonico]] · [[kulstar|Kulstar]] · [[acrid|Acrid]] · [[embolist|Embolist]]

### Brancas
**Espadas:** [[skana|Skana]] · [[nikana|Nikana]] · [[destreza|Destreza]] · [[pangolin_sword|Pangolin]] · [[mire|Mire]] · [[innodem|Innodem]] · [[krohkur|Krohkur]] · [[dakra_prime|Dakra Prime]]

**Espadas Pesadas:** [[galatine|Galatine]] · [[gram|Gram]] · [[paracesis|Paracesis]] · [[skiajati|Skiajati]] · [[pennant|Pennant]] · [[vitrica|Vitrica]] · [[tatsu|Tatsu]] · [[war|War]] · [[tenet_exec|Tenet Exec]]

**Espadas Duplas:** [[dual_kamas|Dual Kamas]] · [[dual_ichor|Dual Ichor]] · [[boltace|Boltace]] · [[okina|Okina]] · [[fang|Fang]] · [[dual_ether|Dual Ether]]

**Lanças:** [[guandao|Guandao]] · [[orthos|Orthos]] · [[lesion|Lesion]] · [[tipedo|Tipedo]] · [[sydon|Sydon]] · [[tonbo|Tonbo]] · [[kesheg|Kesheg]] · [[prova|Prova]]

**Cajados / Nunchaku:** [[bo|Bo]] · [[jat_kusar|Jat Kusar]] · [[shaku|Shaku]] · [[ninkondi|Ninkondi]]

**Martelos:** [[fragor|Fragor]] · [[jat_kittag|Jat Kittag]] · [[magistar|Magistar]] · [[volnus|Volnus]] · [[arca_titron|Arca Titron]] · [[kuva_shildeg|Kuva Shildeg]]

**Foices / Glaives:** [[hate|Hate]] · [[reaper_prime|Reaper Prime]] · [[anku|Anku]] · [[glaive|Glaive]] · [[orvius|Orvius]] · [[xoris|Xoris]] · [[halikar|Halikar]] · [[tenet_grigori|Tenet Grigori]]

**Garras / Socos:** [[venka|Venka]] · [[tekko|Tekko]] · [[furax|Furax]] · [[hirudo|Hirudo]] · [[ripkas|Ripkas]]

**Tonfas:** [[kronen|Kronen]] · [[ohma|Ohma]] · [[praedos|Praedos]]

**Chicotes / Lâmina e Chicote:** [[atterax|Atterax]] · [[scoliac|Scoliac]] · [[lecta|Lecta]] · [[galvacord|Galvacord]] · [[lacera|Lacera]] · [[mios|Mios]] · [[arum_spinosa|Arum Spinosa]]

**Espingardas Melee:** [[redeemer|Redeemer]] · [[stropha|Stropha]] · [[sarpa|Sarpa]] · [[vastilok|Vastilok]]

**Espada e Escudo:** [[silva_and_aegis|Silva e Aegis]] · [[sigma_and_octantis|Sigma e Octantis]] · [[ack_and_brunt|Ack e Brunt]]

### Archwing
**Arch-Guns:** [[mausolon|Mausolon]] · [[larkspur|Larkspur]] · [[imperator|Imperator]] · [[velocitus|Velocitus]] · [[phaedra|Phaedra]] · [[fluctus|Fluctus]] · [[grattler|Grattler]] · [[cyngas|Cyngas]] · [[corvas|Corvas]] · [[cortege|Cortege]] · [[morgha|Morgha]] · [[dual_decurion|Dual Decurion]] · [[kuva_ayanga|Kuva Ayanga]] · [[kuva_grattler|Kuva Grattler]]

**Arch-Melee:** [[onorix|Onorix]] · [[veritux|Veritux]] · [[kaszas|Kaszas]] · [[knux|Knux]] · [[centaur|Centaur]] · [[prisma_veritux|Prisma Veritux]]

---

## Curiosidades

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

---

## Referências Cruzadas

| Índice | Relação |
|---|---|
| [[_Armas _Primarias _Indice\|Primárias]] | Modos de disparo, munição, mecânicas exclusivas de primárias |
| [[_Armas _Secundarias _Indice\|Secundárias]] | Kitguns, dual-wield, mecânicas exclusivas de secundárias |
| [[_Armas _Brancas _Indice\|Brancas]] | Stances por tipo, combo counter, heavy attacks |
| [[_Armas _Archwing _Indice\|Archwing]] | Modos espacial/terrestre, deployer, pool de mods |
| [[_Mods _Indice\|Mods]] | Mods que modificam stats de armas |
| [[_Recursos _Indice\|Recursos]] | Materiais usados no craft de armas |
| [[_Locais _Indice\|Locais]] | Planetas onde drops e fontes ocorrem |
| [[_Warframes _Indice\|Warframes]] | Frames que amplificam armas por habilidades |

----------------------------------------


## Seção: armas\primarias
### 📄 arquivo: _Armas _Primarias _Indice.md

# Armas Primárias — Índice

> [!quote]
> *"A escolha da primária define o alcance do Tenno antes do inimigo chegar ao corpo-a-corpo."*

---

## Visão Geral

Armas primárias ocupam o slot principal do Tenno e são a primeira linha de combate à distância. São as armas com maior variedade de mecânicas do jogo — de rifles automáticos a arcos de carga, lança-chamas, snipers e lançadores de projéteis explosivos.

**Slot:** Primário · **Mods:** 8 slots + Exilus (com adaptador) + Arcane (com adaptador)

---

## Modos de Disparo

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

---

## Tipos de Munição

| Tipo | Armas que Usam | Observações |
|---|---|---|
| **Rifle** | Rifles de assalto, semi-auto, lança-chamas, beam | Mais abundante — dropa de maioria dos inimigos |
| **Espingarda** | Todas as espingardas (shotguns) | Pool separado do rifle |
| **Sniper** | Snipers (Rubico, Lanka, Vectis, Vulkar) | Pool pequeno — poucos drops por missão |
| **Arco** | Arcos (Paris, Cernos, Daikyu, Nataruk) | Projéteis físicos, alguns recuperáveis |
| **Especial** | Varia por arma (Lançadores, Rifles Especiais) | Depende da arma específica |

---

## Mecânicas Especiais

**Punch-Through:** Projétil atravessa inimigos e/ou objetos. Inato em algumas armas (Boltor, Ferrox). Adicionável via mods: Shred, Metal Auger, Terminal Velocity.

**Espingardas e Status por Projétil:** Espingardas disparam múltiplos pellets por tiro. Cada pellet tem sua própria chance de status — na prática, armas com alta status chance e múltiplos pellets aplicam vários procs por disparo.

**Críticos em Arcos:** Arcos têm Headshot Multiplier inato — tiros na cabeça multiplicam o dano crítico. Ideal para builds de crit com Lanka, Rubico Prime.

**Incarnon Genesis:** Felarx e Phenmor possuem modo Incarnon. Ao cumprir um objetivo de evolução em combate (ex: 50 headshots), a arma se transforma temporariamente em uma forma alternativa mais poderosa com mecânicas distintas. Obtidas via Duviri Paradox.

**Rifles com Múltiplos Modos:** Algumas armas alternam modo de disparo — Tiberon alterna Auto/Burst/Semi, Stradavar alterna Auto/Semi, Fulmin alterna automático elétrico/disparo único.

---

## Lista Completa (129)

| Arma | Tipo | Fonte |
|---|---|---|
| [[acceltra\|Acceltra]] | Rifle de Assalto | Drop (Demolyst Manic, Steel Path) |
| [[acceltra_prime\|Acceltra Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[ambassador\|Ambassador]] | Rifle de Assalto | Drop (Amalgam, Jupiter) |
| [[amprex\|Amprex]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[arca_plasmor\|Arca Plasmor]] | Espingarda | Pesquisa de Clã (Corpus) |
| [[astilla\|Astilla]] | Espingarda | Pesquisa de Clã (Corpus) |
| [[astilla_prime\|Astilla Prime]] | Espingarda | Relíquias (Prime) |
| [[attica\|Attica]] | Arco | Mercado (blueprint) |
| [[battacor\|Battacor]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[baza\|Baza]] | Rifle de Assalto | Mercado (blueprint) |
| [[baza_prime\|Baza Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[boltor\|Boltor]] | Rifle de Assalto | Mercado (blueprint) |
| [[boltor_prime\|Boltor Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[braton\|Braton]] | Rifle de Assalto | Mercado (blueprint) |
| [[braton_prime\|Braton Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[braton_vandal\|Braton Vandal]] | Rifle de Assalto | Evento / Drop (Acolytes) |
| [[buzlok\|Buzlok]] | Rifle de Assalto | Mercado (blueprint) |
| [[cedo\|Cedo]] | Espingarda | Pesquisa de Clã (Entrati) |
| [[cernos\|Cernos]] | Arco | Mercado (blueprint) |
| [[cernos_prime\|Cernos Prime]] | Arco | Relíquias (Prime) |
| [[convectrix\|Convectrix]] | Espingarda | Pesquisa de Clã (Corpus) |
| [[corinth\|Corinth]] | Espingarda | Mercado (blueprint) |
| [[corinth_prime\|Corinth Prime]] | Espingarda | Relíquias (Prime) |
| [[daikyu\|Daikyu]] | Arco | Mercado (blueprint) |
| [[dera\|Dera]] | Rifle de Assalto | Mercado (blueprint) |
| [[dera_vandal\|Dera Vandal]] | Rifle de Assalto | Nightwave / Evento |
| [[dex_sybaris\|Dex Sybaris]] | Rifle Semi-Auto | Evento (Aniversário DE) |
| [[drakgoon\|Drakgoon]] | Espingarda | Mercado (blueprint) |
| [[exergis\|Exergis]] | Espingarda | Pesquisa de Clã (Corpus) |
| [[felarx\|Felarx]] | Incarnon | Incarnon (Duviri) |
| [[ferrox\|Ferrox]] | Rifle Especial | Mercado (blueprint) |
| [[flux_rifle\|Flux Rifle]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[fulmin\|Fulmin]] | Rifle Especial | Drop (Amalgam, Jupiter) |
| [[fulmin_prime\|Fulmin Prime]] | Rifle Especial | Relíquias (Prime) |
| [[glaxion\|Glaxion]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[glaxion_vandal\|Glaxion Vandal]] | Rifle de Assalto | Nightwave / Evento |
| [[gorgon\|Gorgon]] | Rifle de Assalto | Mercado (blueprint) |
| [[gorgon_wraith\|Gorgon Wraith]] | Rifle de Assalto | Nightwave / Evento |
| [[grakata\|Grakata]] | Rifle de Assalto | Mercado (blueprint) |
| [[harpak\|Harpak]] | Rifle Especial | Mercado (blueprint) |
| [[hek\|Hek]] | Espingarda | Mercado (blueprint) |
| [[hind\|Hind]] | Rifle de Assalto | Mercado (blueprint) |
| [[ignis\|Ignis]] | Lança-Chamas | Pesquisa de Clã (Grineer) |
| [[ignis_wraith\|Ignis Wraith]] | Lança-Chamas | Pesquisa de Clã (blueprint tradável) / Evento |
| [[javlok\|Javlok]] | Lançador | Mercado (blueprint) |
| [[karak\|Karak]] | Rifle de Assalto | Mercado (blueprint) |
| [[karak_wraith\|Karak Wraith]] | Rifle de Assalto | Evento / Drop (Acolytes) |
| [[kohm\|Kohm]] | Espingarda | Mercado (blueprint) |
| [[komorex\|Komorex]] | Sniper | Pesquisa de Clã (Corpus) |
| [[kuva_bramma\|Kuva Bramma]] | Lançador | Kuva Lich |
| [[kuva_chakkhurr\|Kuva Chakkhurr]] | Sniper | Kuva Lich |
| [[kuva_hek\|Kuva Hek]] | Espingarda | Kuva Lich |
| [[kuva_ogris\|Kuva Ogris]] | Lançador | Kuva Lich |
| [[kuva_quartakk\|Kuva Quartakk]] | Rifle de Assalto | Kuva Lich |
| [[kuva_tonkor\|Kuva Tonkor]] | Lançador | Kuva Lich |
| [[kuva_zarr\|Kuva Zarr]] | Lançador | Kuva Lich |
| [[lanka\|Lanka]] | Sniper | Mercado (blueprint) |
| [[latron\|Latron]] | Rifle Semi-Auto | Mercado (blueprint) |
| [[latron_prime\|Latron Prime]] | Rifle Semi-Auto | Relíquias (Prime) |
| [[latron_wraith\|Latron Wraith]] | Rifle Semi-Auto | Nightwave / Evento |
| [[lenz\|Lenz]] | Arco | Mercado (blueprint) |
| [[miter\|Miter]] | Lançador | Mercado (blueprint) |
| [[mk1_braton\|MK1-Braton]] | Rifle de Assalto | Starter / Mercado |
| [[mutalist_quanta\|Mutalist Quanta]] | Lançador | Drop (Invasões Infested, Eris) |
| [[nataruk\|Nataruk]] | Arco | Nakak, Cetus (pós The New War) |
| [[ogris\|Ogris]] | Lançador | Mercado (blueprint) |
| [[opticor\|Opticor]] | Sniper | Pesquisa de Clã (Corpus) |
| [[opticor_vandal\|Opticor Vandal]] | Sniper | Nightwave / Evento |
| [[panthera\|Panthera]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[panthera_prime\|Panthera Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[paracyst\|Paracyst]] | Rifle Especial | Mercado (blueprint) |
| [[paris\|Paris]] | Arco | Mercado (blueprint) |
| [[paris_prime\|Paris Prime]] | Arco | Relíquias (Prime) |
| [[penta\|Penta]] | Lançador | Mercado (blueprint) |
| [[phantasma\|Phantasma]] | Espingarda | Pesquisa de Clã (Entrati) |
| [[phantasma_prime\|Phantasma Prime]] | Espingarda | Relíquias (Prime) |
| [[phenmor\|Phenmor]] | Incarnon | Incarnon (Duviri) |
| [[prisma_grakata\|Prisma Grakata]] | Rifle de Assalto | Baro Ki'Teer / Nightwave |
| [[proboscis_cernos\|Proboscis Cernos]] | Arco | Pesquisa de Clã (Entrati) |
| [[quanta\|Quanta]] | Lançador | Pesquisa de Clã (Corpus) |
| [[quanta_vandal\|Quanta Vandal]] | Lançador | Nightwave / Evento |
| [[rakta_cernos\|Rakta Cernos]] | Arco | Sindicato (Red Veil) |
| [[rubico\|Rubico]] | Sniper | Mercado (blueprint) |
| [[rubico_prime\|Rubico Prime]] | Sniper | Relíquias (Prime) |
| [[sancti_tigris\|Sancti Tigris]] | Espingarda | Sindicato (New Loka) |
| [[scourge\|Scourge]] | Lançador | Pesquisa de Clã (Entrati) |
| [[scourge_prime\|Scourge Prime]] | Lançador | Relíquias (Prime) |
| [[secura_penta\|Secura Penta]] | Lançador | Sindicato (Perrin Sequence) |
| [[shedu\|Shedu]] | Rifle Especial | Drop (Sentients, Murex — Empyrean) |
| [[simulor\|Simulor]] | Lançador | Pesquisa de Clã (Corpus) |
| [[snipetron\|Snipetron]] | Sniper | Baro Ki'Teer |
| [[snipetron_vandal\|Snipetron Vandal]] | Sniper | Evento |
| [[sobek\|Sobek]] | Espingarda | Mercado (blueprint) |
| [[soma\|Soma]] | Rifle de Assalto | Mercado (blueprint) |
| [[soma_prime\|Soma Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[sporothrix\|Sporothrix]] | Arco | Pesquisa de Clã (Entrati) |
| [[stahlta\|Stahlta]] | Rifle de Assalto | Pesquisa de Clã (Entrati) |
| [[stradavar\|Stradavar]] | Rifle de Assalto | Mercado (blueprint) |
| [[stradavar_prime\|Stradavar Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[strun\|Strun]] | Espingarda | Mercado (blueprint) |
| [[strun_wraith\|Strun Wraith]] | Espingarda | Nightwave / Evento |
| [[supra\|Supra]] | Rifle de Assalto | Pesquisa de Clã (Corpus) |
| [[supra_vandal\|Supra Vandal]] | Rifle de Assalto | Nightwave / Evento |
| [[sybaris\|Sybaris]] | Rifle Semi-Auto | Mercado (blueprint) |
| [[sybaris_prime\|Sybaris Prime]] | Rifle Semi-Auto | Relíquias (Prime) |
| [[synoid_simulor\|Synoid Simulor]] | Lançador | Sindicato (Cephalon Suda) |
| [[telos_boltor\|Telos Boltor]] | Rifle de Assalto | Sindicato (Arbiters of Hexis) |
| [[tenet_arca_plasmor\|Tenet Arca Plasmor]] | Espingarda | Irmãs de Parvos |
| [[tenet_envoy\|Tenet Envoy]] | Lançador | Irmãs de Parvos |
| [[tenet_ferrox\|Tenet Ferrox]] | Rifle Especial | Irmãs de Parvos |
| [[tenet_flux_rifle\|Tenet Flux Rifle]] | Rifle de Assalto | Irmãs de Parvos |
| [[tenora\|Tenora]] | Rifle de Assalto | Mercado (blueprint) |
| [[tenora_prime\|Tenora Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[tiberon\|Tiberon]] | Rifle de Assalto | Mercado (blueprint) |
| [[tiberon_prime\|Tiberon Prime]] | Rifle de Assalto | Relíquias (Prime) |
| [[tigris\|Tigris]] | Espingarda | Mercado (blueprint) |
| [[tigris_prime\|Tigris Prime]] | Espingarda | Relíquias (Prime) |
| [[tonkor\|Tonkor]] | Lançador | Mercado (blueprint) |
| [[trumna\|Trumna]] | Lançador | Pesquisa de Clã (Entrati) |
| [[vaykor_hek\|Vaykor Hek]] | Espingarda | Sindicato (Steel Meridian) |
| [[vectis\|Vectis]] | Sniper | Mercado (blueprint) |
| [[vectis_prime\|Vectis Prime]] | Sniper | Relíquias (Prime) |
| [[veldt\|Veldt]] | Rifle de Assalto | Mercado (blueprint) |
| [[vermisplicer\|Vermisplicer]] | Espingarda | Pesquisa de Clã (Entrati) |
| [[vulkar\|Vulkar]] | Sniper | Mercado (blueprint) |
| [[vulkar_wraith\|Vulkar Wraith]] | Sniper | Nightwave / Evento |
| [[zarr\|Zarr]] | Lançador | Mercado (blueprint) |
| [[zhuge\|Zhuge]] | Arco | Mercado (blueprint) |
| [[zhuge_prime\|Zhuge Prime]] | Arco | Relíquias (Prime) |

---

## Referências Cruzadas

| Índice | Relação |
|---|---|
| [[_Armas _Indice\|Armas]] | Índice geral — todas as categorias de arma |
| [[_Mods Armas _Indice\|Mods de Armas]] | Mods de rifle, espingarda, sniper e arco |
| [[_Recursos _Indice\|Recursos]] | Materiais para crafting de primárias |
| [[_Locais _Indice\|Locais]] | Planetas onde drops de primárias ocorrem |

----------------------------------------


## Seção: armas\secundarias
### 📄 arquivo: _Armas _Secundarias _Indice.md

# Armas Secundárias — Índice

> [!quote]
> *"Quando a primária cai, a secundária define quem sobrevive."*

---

## Visão Geral

Armas secundárias ocupam o slot de pistola do Tenno. São mais compactas que as primárias mas cobrem funções diversas — pistolas de precisão, armas de arremesso, espingardas secundárias, kits modulares e canhões de braço.

**Slot:** Secundário · **Mods:** 8 slots + Exilus (com adaptador) + Arcane (com adaptador)

---

## Sistema Kitgun

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

---

## Armas de Arremesso (Thrown)

Armas como Hikou, Spira, Despair, Fusilai, Zakti e Castanas são arremessadas em vez de disparadas. Mecânicas únicas:

| Mecânica | Detalhe |
|---|---|
| **Status por projétil** | Cada projétil arremessado tem chance independente de status |
| **Multishot** | Adiciona projéteis arremessados simultâneos por lançamento |
| **Recuperação** | A maioria não recupera projéteis — consome ammo normalmente |
| **Explosivas** | Castanas e Sancti Castanas explodem por timer ou contato |

---

## Prefixo Ak- (Dual-Wield)

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

---

## Incarnon Genesis

**Laetum** é a única secundária Incarnon do Duviri Paradox. Evolui durante a missão ao cumprir um objetivo de evolução — transforma-se em uma forma alternativa mais poderosa com mecânica de disparo distinta. Obtida via missões do Duviri Circuit.

---

## Lista Completa (93)

| Arma | Tipo | Fonte |
|---|---|---|
| [[acrid\|Acrid]] | Especial | Drop (Invasões Infested) |
| [[akarius\|Akarius]] | Pistolas Duplas | Pesquisa de Clã (Entrati) |
| [[akbolto\|Akbolto]] | Pistolas Duplas | Mercado (2× Bolto) |
| [[akbolto_prime\|Akbolto Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[akjagara\|Akjagara]] | Pistolas Duplas | Mercado (blueprint) |
| [[akjagara_prime\|Akjagara Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[aklex\|Aklex]] | Pistolas Duplas | Mercado (2× Lex) |
| [[aklex_prime\|Aklex Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[aksomati\|Aksomati]] | Pistolas Duplas | Pesquisa de Clã (Corpus) |
| [[aksomati_prime\|Aksomati Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[akstiletto\|Akstiletto]] | Pistolas Duplas | Mercado (blueprint) |
| [[akstiletto_prime\|Akstiletto Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[akvasto\|Akvasto]] | Pistolas Duplas | Mercado (2× Vasto) |
| [[akvasto_prime\|Akvasto Prime]] | Pistolas Duplas | Relíquias (Prime) |
| [[akzani\|Akzani]] | Pistolas Duplas | Pesquisa de Clã (Cetus) |
| [[arca_scisco\|Arca Scisco]] | Pistola | Pesquisa de Clã (Corpus) |
| [[athodai\|Athodai]] | Pistola | Fortuna (Old Mate, rank 5) |
| [[atomos\|Atomos]] | Especial | Pesquisa de Clã (Corpus) |
| [[azima\|Azima]] | Especial | Nightwave / Evento |
| [[ballistica\|Ballistica]] | Arco Secundário | Mercado (blueprint) |
| [[ballistica_prime\|Ballistica Prime]] | Arco Secundário | Relíquias (Prime) |
| [[bolto\|Bolto]] | Pistola | Mercado (blueprint) |
| [[brakk\|Brakk]] | Pistola | Drop (Grustrag Three) / Invasões |
| [[bronco\|Bronco]] | Pistola | Mercado (blueprint) |
| [[bronco_prime\|Bronco Prime]] | Pistola | Relíquias (Prime) |
| [[bubonico\|Bubonico]] | Canhão de Braço | Pesquisa de Clã (Entrati) |
| [[castanas\|Castanas]] | Arremesso | Mercado (blueprint) |
| [[catchmoon\|Catchmoon]] | Kitgun | Kitgun (Fortuna) |
| [[cyanex\|Cyanex]] | Especial | Pesquisa de Clã (Entrati) |
| [[despair\|Despair]] | Arremesso | Drop (Stalker) |
| [[detron\|Detron]] | Pistola | Drop (Corrupted, Void) |
| [[dex_furis\|Dex Furis]] | Pistola | Evento (Aniversário DE) |
| [[embolist\|Embolist]] | Especial | Pesquisa de Clã (Grineer) |
| [[epitaph\|Epitaph]] | Pistola | Pesquisa de Clã (Entrati) |
| [[euphona_prime\|Euphona Prime]] | Pistola | Relíquias (Prime) |
| [[furis\|Furis]] | Pistola | Mercado (blueprint) |
| [[fusilai\|Fusilai]] | Arremesso | Nakak, Cetus (caça) |
| [[gammacor\|Gammacor]] | Especial | Pesquisa de Clã (Corpus) |
| [[gaze\|Gaze]] | Kitgun | Kitgun (Fortuna) |
| [[hikou\|Hikou]] | Arremesso | Mercado (blueprint) |
| [[hikou_prime\|Hikou Prime]] | Arremesso | Relíquias (Prime) |
| [[knell\|Knell]] | Pistola | Pesquisa de Clã (Quills, Cetus) |
| [[knell_prime\|Knell Prime]] | Pistola | Relíquias (Prime) |
| [[kohmak\|Kohmak]] | Especial | Pesquisa de Clã (Corpus) |
| [[kompressa\|Kompressa]] | Especial | Pesquisa de Clã (Entrati) |
| [[kulstar\|Kulstar]] | Especial | Pesquisa de Clã (Grineer) |
| [[kuva_brakk\|Kuva Brakk]] | Pistola | Kuva Lich |
| [[kuva_nukor\|Kuva Nukor]] | Pistola | Kuva Lich |
| [[kuva_seer\|Kuva Seer]] | Pistola | Kuva Lich |
| [[kuva_twin_stubbas\|Kuva Twin Stubbas]] | Pistolas Duplas | Kuva Lich |
| [[laetum\|Laetum]] | Incarnon | Incarnon (Duviri) |
| [[lato\|Lato]] | Pistola | Starter / Mercado |
| [[lato_prime\|Lato Prime]] | Pistola | Indisponível (Founder's Pack, 2013) |
| [[lato_vandal\|Lato Vandal]] | Pistola | Nightwave / Evento |
| [[lex\|Lex]] | Pistola | Mercado (blueprint) |
| [[lex_prime\|Lex Prime]] | Pistola | Relíquias (Prime) |
| [[magnus\|Magnus]] | Pistola | Mercado (blueprint) |
| [[magnus_prime\|Magnus Prime]] | Pistola | Relíquias (Prime) |
| [[mara_detron\|Mara Detron]] | Pistola | Baro Ki'Teer |
| [[nukor\|Nukor]] | Pistola | Pesquisa de Clã (Corpus) |
| [[ocucor\|Ocucor]] | Especial | Pesquisa de Clã (Entrati) |
| [[pandero\|Pandero]] | Pistola | Mercado (blueprint) |
| [[pandero_prime\|Pandero Prime]] | Pistola | Relíquias (Prime) |
| [[rattleguts\|Rattleguts]] | Kitgun | Kitgun (Fortuna) |
| [[sancti_castanas\|Sancti Castanas]] | Arremesso | Sindicato (New Loka) |
| [[seer\|Seer]] | Pistola | Drop (Vor, Mercury — Tolstoj) |
| [[sicarus\|Sicarus]] | Pistola | Mercado (blueprint) |
| [[sicarus_prime\|Sicarus Prime]] | Pistola | Relíquias (Prime) |
| [[sonicor\|Sonicor]] | Especial | Pesquisa de Clã (Corpus) |
| [[spira\|Spira]] | Arremesso | Mercado (blueprint) |
| [[spira_prime\|Spira Prime]] | Arremesso | Relíquias (Prime) |
| [[staticor\|Staticor]] | Especial | Pesquisa de Clã (Corpus) |
| [[stubba\|Stubba]] | Especial | Pesquisa de Clã (Grineer) |
| [[stug\|Stug]] | Especial | Pesquisa de Clã (Corpus) |
| [[synoid_gammacor\|Synoid Gammacor]] | Especial | Sindicato (Cephalon Suda) |
| [[tenet_agendus\|Tenet Agendus]] | Especial | Irmãs de Parvos |
| [[tenet_cycron\|Tenet Cycron]] | Especial | Irmãs de Parvos |
| [[tenet_detron\|Tenet Detron]] | Pistola | Irmãs de Parvos |
| [[tenet_diplos\|Tenet Diplos]] | Pistolas Duplas | Irmãs de Parvos |
| [[tenet_plinx\|Tenet Plinx]] | Pistola | Irmãs de Parvos |
| [[tenet_spirex\|Tenet Spirex]] | Especial | Irmãs de Parvos |
| [[tombfinger\|Tombfinger]] | Kitgun | Kitgun (Fortuna) |
| [[twin_grakata\|Twin Grakata]] | Pistolas Duplas | Mercado (blueprint) |
| [[twin_vipers\|Twin Vipers]] | Pistolas Duplas | Mercado (blueprint) |
| [[twin_vipers_wraith\|Twin Vipers Wraith]] | Pistolas Duplas | Nightwave / Evento |
| [[vasto\|Vasto]] | Pistola | Mercado (blueprint) |
| [[vasto_prime\|Vasto Prime]] | Pistola | Relíquias (Prime) |
| [[velox\|Velox]] | Pistola | Drop (Corpus, Orb Vallis) |
| [[viper\|Viper]] | Pistola | Mercado (blueprint) |
| [[viper_wraith\|Viper Wraith]] | Pistola | Nightwave / Evento |
| [[zakti\|Zakti]] | Arremesso | Mercado (blueprint) |
| [[zakti_prime\|Zakti Prime]] | Arremesso | Relíquias (Prime) |
| [[zylok\|Zylok]] | Pistola | Nightwave / Evento |

---

## Referências Cruzadas

| Índice | Relação |
|---|---|
| [[_Armas _Indice\|Armas]] | Índice geral — todas as categorias de arma |
| [[_Mods Armas _Indice\|Mods de Armas]] | Mods de pistola e secundária |
| [[_Recursos _Indice\|Recursos]] | Materiais para crafting de secundárias |
| [[_Locais _Indice\|Locais]] | Planetas onde drops de secundárias ocorrem |

----------------------------------------


## Seção: armas\brancas
### 📄 arquivo: _Armas _Brancas _Indice.md

# Armas Brancas — Índice

> [!quote]
> *"O verdadeiro poder do Tenno não está na arma — está nas mãos que a empunham."*

---

## Visão Geral

Armas brancas (melee) são o slot de combate corpo-a-corpo do Tenno. São as armas com mecânicas mais profundas do jogo — **stances** que substituem completamente os ataques básicos, um **combo counter** que amplifica o dano progressivamente e **heavy attacks** devastadores que consomem o contador acumulado.

**Slot:** Melee · **Mods:** 8 slots + slot de Stance (exclusivo) + Exilus (com adaptador)

---

## Sistema de Stances

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

---

## Combo Counter

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

---

## Heavy Attacks

Heavy attacks (botão de ataque segurado) **consomem todo o combo counter** para desferir um golpe de alto dano multiplicado:

- **Dano:** Proporcional ao multiplicador do combo consumido
- **Spin Attack (Heavy aéreo):** Versão rotacional com AoE — executado no ar
- **Weeping Wounds:** Funciona com heavy attacks (combo escala status)

> [!warning] Perda total do Combo
> Heavy attacks **zeram o combo counter imediatamente**. Builds que usam Blood Rush geralmente evitam heavy attacks para manter o multiplicador alto.

---

## Ataques Especiais

| Tipo | Gatilho | Efeito |
|---|---|---|
| **Slam Attack** | Pular + heavy attack ao aterrissar | AoE radial proporcional ao combo |
| **Finisher (pé)** | Inimigo derrubado / vulnerável | Alto dano fixo + animação de execução |
| **Ground Finisher** | Inimigo no chão | Dano alto com animação específica |
| **Wall Attack** | Corrida em parede + ataque | Ataque durante parkour vertical |

---

## Zaws — Armas Brancas Modulares

Zaws são brancas modulares montadas em **Cetus** (Planície de Eidolon) pelo NPC **Hok**. Três componentes:

| Componente | Função |
|---|---|
| **Strike** | Define o tipo da arma e dano base |
| **Grip** | Afeta dano e velocidade de ataque |
| **Link** | Afeta crit/status e capacidade de mods |

> [!tip]
> Zaws também precisam ser gildados (rank 30 + Ostron Standing) para receber o nome permanente e contribuir com Mastery.

---

## Lista Completa (135)

| Arma | Tipo | Fonte |
|---|---|---|
| [[ack_and_brunt\|Ack e Brunt]] | Espada e Escudo | Pesquisa de Clã (Grineer) |
| [[anku\|Anku]] | Foice | Pesquisa de Clã (Grineer) |
| [[arca_titron\|Arca Titron]] | Martelo | Pesquisa de Clã (Corpus) |
| [[arum_spinosa\|Arum Spinosa]] | Lâmina e Chicote | Pesquisa de Clã (Entrati) |
| [[atterax\|Atterax]] | Chicote | Mercado (blueprint) |
| [[bo\|Bo]] | Cajado | Mercado (blueprint) |
| [[bo_prime\|Bo Prime]] | Cajado | Relíquias (Prime) |
| [[boltace\|Boltace]] | Espadas Duplas | Pesquisa de Clã (Corpus) |
| [[broken_sword\|Broken Sword]] | Espada | Drop (Stalker) |
| [[broken_war\|Broken War]] | Espada | Drop (Stalker — partes de War) |
| [[ceramic_dagger\|Ceramic Dagger]] | Adaga | Mercado (blueprint) |
| [[cobra_and_crane\|Cobra e Crane]] | Espada e Escudo | Pesquisa de Clã (Grineer) |
| [[cronus\|Cronus]] | Espada | Drop (Ambulas, Pluto) |
| [[dakra_prime\|Dakra Prime]] | Espada | Relíquias (Prime) |
| [[dark_dagger\|Dark Dagger]] | Adaga | Mercado (blueprint) |
| [[dark_split_sword\|Dark Split-Sword]] | Espada Pesada / Dupla | Mercado (blueprint) |
| [[dark_sword\|Dark Sword]] | Espada | Mercado (blueprint) |
| [[destreza\|Destreza]] | Espadim | Mercado (blueprint) |
| [[destreza_prime\|Destreza Prime]] | Espadim | Relíquias (Prime) |
| [[dragon_nikana\|Dragon Nikana]] | Nikana | Mercado (blueprint + componentes Clã) |
| [[dual_cleavers\|Dual Cleavers]] | Espadas Duplas | Mercado (blueprint) |
| [[dual_ether\|Dual Ether]] | Espadas Duplas | Mercado (blueprint) |
| [[dual_heat_swords\|Dual Heat Swords]] | Espadas Duplas | Mercado (blueprint) |
| [[dual_ichor\|Dual Ichor]] | Espadas Duplas | Mercado (blueprint) |
| [[dual_kamas\|Dual Kamas]] | Espadas Duplas | Mercado (blueprint) |
| [[dual_kamas_prime\|Dual Kamas Prime]] | Espadas Duplas | Relíquias (Prime) |
| [[dual_skana\|Dual Skana]] | Espadas Duplas | Mercado (blueprint) |
| [[dual_zoren\|Dual Zoren]] | Espadas Duplas | Mercado (blueprint) |
| [[ether_daggers\|Ether Daggers]] | Adagas Duplas | Mercado (blueprint) |
| [[ether_reaper\|Ether Reaper]] | Foice | Mercado (blueprint) |
| [[ether_sword\|Ether Sword]] | Espada | Mercado (blueprint) |
| [[fang\|Fang]] | Espadas Duplas | Mercado (blueprint) |
| [[fang_prime\|Fang Prime]] | Espadas Duplas | Relíquias (Prime) |
| [[fragor\|Fragor]] | Martelo | Mercado (blueprint) |
| [[fragor_prime\|Fragor Prime]] | Martelo | Relíquias (Prime) |
| [[furax\|Furax]] | Garras | Mercado (blueprint) |
| [[furax_wraith\|Furax Wraith]] | Garras | Nightwave / Evento |
| [[galatine\|Galatine]] | Espada Pesada | Mercado (blueprint) |
| [[galatine_prime\|Galatine Prime]] | Espada Pesada | Relíquias (Prime) |
| [[galvacord\|Galvacord]] | Chicote | Pesquisa de Clã (Grineer) |
| [[glaive\|Glaive]] | Glaive | Mercado (blueprint) |
| [[glaive_prime\|Glaive Prime]] | Glaive | Relíquias (Prime) |
| [[gram\|Gram]] | Espada Pesada | Mercado (blueprint) |
| [[gram_prime\|Gram Prime]] | Espada Pesada | Relíquias (Prime) |
| [[guandao\|Guandao]] | Lança | Mercado (blueprint) |
| [[guandao_prime\|Guandao Prime]] | Lança | Relíquias (Prime) |
| [[halikar\|Halikar]] | Glaive | Mercado (blueprint) |
| [[halikar_wraith\|Halikar Wraith]] | Glaive | Nightwave / Evento |
| [[hate\|Hate]] | Foice | Drop (Stalker) |
| [[heat_sword\|Heat Sword]] | Espada | Mercado (blueprint) |
| [[hirudo\|Hirudo]] | Garras | Pesquisa de Clã (Grineer) |
| [[innodem\|Innodem]] | Espada | Pesquisa de Clã (Entrati) |
| [[jat_kittag\|Jat Kittag]] | Martelo | Mercado (blueprint) |
| [[jat_kusar\|Jat Kusar]] | Cajado | Pesquisa de Clã (Corpus) |
| [[jaw_sword\|Jaw Sword]] | Espada | Mercado (blueprint) |
| [[karyst\|Karyst]] | Adaga | Mercado (blueprint) |
| [[karyst_prime\|Karyst Prime]] | Adaga | Relíquias (Prime) |
| [[kesheg\|Kesheg]] | Lança | Pesquisa de Clã (Grineer) |
| [[kestrel\|Kestrel]] | Glaive | Mercado (blueprint) |
| [[krohkur\|Krohkur]] | Espada | Mercado (blueprint) |
| [[kronen\|Kronen]] | Tonfa | Pesquisa de Clã (Corpus) |
| [[kronen_prime\|Kronen Prime]] | Tonfa | Relíquias (Prime) |
| [[kuva_shildeg\|Kuva Shildeg]] | Martelo | Kuva Lich |
| [[lacera\|Lacera]] | Lâmina e Chicote | Pesquisa de Clã (Corpus) |
| [[lecta\|Lecta]] | Chicote | Mercado (blueprint) |
| [[lesion\|Lesion]] | Lança | Pesquisa de Clã (Entrati) |
| [[machete\|Machete]] | Facão | Mercado (blueprint) |
| [[machete_wraith\|Machete Wraith]] | Facão | Nightwave / Evento |
| [[magistar\|Magistar]] | Martelo | Pesquisa de Clã (Grineer) |
| [[magistar_wraith\|Magistar Wraith]] | Martelo | Nightwave / Evento |
| [[mios\|Mios]] | Lâmina e Chicote | Pesquisa de Clã (Entrati) |
| [[mire\|Mire]] | Espada | Drop (Ambulas, Pluto) |
| [[nami_duo\|Nami Duo]] | Espadas Duplas | Pesquisa de Clã (Corpus) |
| [[nami_solo\|Nami Solo]] | Espada | Pesquisa de Clã (Corpus) |
| [[nikana\|Nikana]] | Nikana | Mercado (blueprint) |
| [[nikana_prime\|Nikana Prime]] | Nikana | Relíquias (Prime) |
| [[ninkondi\|Ninkondi]] | Nunchaku | Pesquisa de Clã (Corpus) |
| [[ninkondi_prime\|Ninkondi Prime]] | Nunchaku | Relíquias (Prime) |
| [[ohma\|Ohma]] | Tonfa | Pesquisa de Clã (Corpus) |
| [[okina\|Okina]] | Espadas Duplas | Pesquisa de Clã (Corpus) |
| [[okina_prime\|Okina Prime]] | Espadas Duplas | Relíquias (Prime) |
| [[orthos\|Orthos]] | Lança | Mercado (blueprint) |
| [[orthos_prime\|Orthos Prime]] | Lança | Relíquias (Prime) |
| [[orvius\|Orvius]] | Glaive | Quest (Chains of Harrow) |
| [[pangolin_prime\|Pangolin Prime]] | Espada | Relíquias (Prime) |
| [[pangolin_sword\|Pangolin Sword]] | Espada | Mercado (blueprint) |
| [[paracesis\|Paracesis]] | Espada Pesada | Quest (The Sacrifice) |
| [[pennant\|Pennant]] | Espada Pesada | Pesquisa de Clã (Entrati) |
| [[plasma_sword\|Plasma Sword]] | Espada | Mercado (blueprint) |
| [[praedos\|Praedos]] | Tonfa | Pesquisa de Clã (Entrati) |
| [[prisma_dual_cleavers\|Prisma Dual Cleavers]] | Espadas Duplas | Baro Ki'Teer |
| [[prisma_skana\|Prisma Skana]] | Espada | Baro Ki'Teer |
| [[prova\|Prova]] | Lança | Pesquisa de Clã (Corpus) |
| [[prova_vandal\|Prova Vandal]] | Lança | Nightwave / Evento |
| [[pulmonars\|Pulmonars]] | Leques | Pesquisa de Clã (Entrati) |
| [[rakta_dark_dagger\|Rakta Dark Dagger]] | Adaga | Sindicato (Red Veil) |
| [[reaper_prime\|Reaper Prime]] | Foice | Relíquias (Prime) |
| [[redeemer\|Redeemer]] | Espingarda Melee | Pesquisa de Clã (Tenno) |
| [[redeemer_prime\|Redeemer Prime]] | Espingarda Melee | Relíquias (Prime) |
| [[ripkas\|Ripkas]] | Garras | Pesquisa de Clã (Grineer) |
| [[sarpa\|Sarpa]] | Espingarda Melee | Pesquisa de Clã (Tenno) |
| [[scoliac\|Scoliac]] | Chicote | Pesquisa de Clã (Grineer) |
| [[secura_lecta\|Secura Lecta]] | Chicote | Sindicato (Perrin Sequence) |
| [[shaku\|Shaku]] | Cajado | Pesquisa de Clã (Corpus) |
| [[sheev\|Sheev]] | Adaga | Pesquisa de Clã (Grineer) |
| [[sigma_and_octantis\|Sigma e Octantis]] | Espada e Escudo | Evento (Aniversário DE) |
| [[silva_and_aegis\|Silva e Aegis]] | Espada e Escudo | Mercado (blueprint) |
| [[silva_and_aegis_prime\|Silva e Aegis Prime]] | Espada e Escudo | Relíquias (Prime) |
| [[skana\|Skana]] | Espada | Starter / Mercado |
| [[skana_prime\|Skana Prime]] | Espada | Relíquias (Prime) |
| [[skiajati\|Skiajati]] | Nikana | Quest (The Sacrifice) |
| [[stiletto_prime\|Stiletto Prime]] | Adaga | Relíquias (Prime) |
| [[stropha\|Stropha]] | Espingarda Melee | Pesquisa de Clã (Tenno) |
| [[sydon\|Sydon]] | Lança | Pesquisa de Clã (Grineer) |
| [[tatsu\|Tatsu]] | Espada Pesada | Pesquisa de Clã (Entrati) |
| [[tatsu_prime\|Tatsu Prime]] | Espada Pesada | Relíquias (Prime) |
| [[tekko\|Tekko]] | Garras | Mercado (blueprint) |
| [[tekko_prime\|Tekko Prime]] | Garras | Relíquias (Prime) |
| [[telos_boltace\|Telos Boltace]] | Espadas Duplas | Sindicato (Arbiters of Hexis) |
| [[tenet_exec\|Tenet Exec]] | Espada Pesada | Irmãs de Parvos |
| [[tenet_grigori\|Tenet Grigori]] | Foice | Irmãs de Parvos |
| [[tenet_livia\|Tenet Livia]] | Espadim | Irmãs de Parvos |
| [[tipedo\|Tipedo]] | Lança | Mercado (blueprint) |
| [[tipedo_prime\|Tipedo Prime]] | Lança | Relíquias (Prime) |
| [[tonbo\|Tonbo]] | Lança | Pesquisa de Clã (Grineer) |
| [[twin_basolk\|Twin Basolk]] | Adagas Duplas | Pesquisa de Clã (Grineer) |
| [[vastilok\|Vastilok]] | Espingarda Melee | Pesquisa de Clã (Tenno) |
| [[vaykor_sydon\|Vaykor Sydon]] | Lança | Sindicato (Steel Meridian) |
| [[venka\|Venka]] | Garras | Pesquisa de Clã (Grineer) |
| [[venka_prime\|Venka Prime]] | Garras | Relíquias (Prime) |
| [[vitrica\|Vitrica]] | Espada Pesada | Pesquisa de Clã (Entrati) |
| [[volnus\|Volnus]] | Martelo | Pesquisa de Clã (Corpus) |
| [[volnus_prime\|Volnus Prime]] | Martelo | Relíquias (Prime) |
| [[war\|War]] | Espada Pesada | Drop (Stalker) |
| [[xoris\|Xoris]] | Glaive | Quest (The Deadlock Protocol) |

---

## Referências Cruzadas

| Índice | Relação |
|---|---|
| [[_Armas _Indice\|Armas]] | Índice geral — todas as categorias de arma |
| [[_Mods _Indice\|Mods]] | Stances são mods — encontrados no índice de mods |
| [[_Mods Armas _Indice\|Mods de Armas]] | Mods de melee (Blood Rush, Weeping Wounds etc.) |
| [[_Locais _Indice\|Locais]] | Planetas onde inimigos dropam stances e brancas |

----------------------------------------


## Seção: armas\archwing
### 📄 arquivo: _Armas _Archwing _Indice.md

# Armas Archwing — Índice

> [!quote]
> *"No vácuo do espaço, nenhuma arma convencional importa."*

---

## Visão Geral

Armas Archwing são equipamentos exclusivos para combate espacial e atmosférico, equipados no exoesqueleto Archwing. Dividem-se em **Arch-Guns** (ranged) e **Arch-Melee** (corpo-a-corpo). Possuem pool de mods completamente separado das armas terrestres.

**Slot Arch-Gun:** Slot de arma principal do Archwing
**Slot Arch-Melee:** Slot melee exclusivo do Archwing
**Mods:** 8 slots exclusivos — mods de Arch-Gun ou Arch-Melee (não compartilhados com armas terrestres)

---

## Modos de Uso

| Modo | Contexto | Como Acessar |
|---|---|---|
| **Espaço (Space)** | Missões Archwing no vácuo — planetas com anel orbital | Ativar Archwing automaticamente ao iniciar missão espacial |
| **Atmosfera** | Combate externo do Railjack em missões de alto nível | Sair pela escotilha traseira do Railjack durante missão |
| **Terrestre (Ground)** | Missões terrestres normais via item especial | Archgun Deployer ou Zenith Crown (ver seção abaixo) |

---

## Uso Terrestre de Arch-Guns

Arch-Guns podem ser convocadas em missões terrestres com dois métodos:

| Método | Como Obter | Limitação |
|---|---|---|
| **Archgun Deployer** | Recompensa de bounty em Fortuna (Orb Vallis) | Cargas limitadas — recarrega com tempo real (fora de missão) |
| **Zenith Crown** | Oferta sazonal da Nightwave | Convocação ilimitada — exclusivo para Mausolon |

> [!important] Arch-Melee não é usável no solo
> **Arch-Melee** é exclusiva de combate espacial e atmosférico — não pode ser convocada em missões terrestres com nenhum método disponível.

---

## Pool de Mods Exclusivo

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

---

## Pesquisa de Clã para Archwing

A maioria das Arch-Guns está bloqueada atrás de pesquisa de clã em laboratórios específicos:

| Facção | Laboratório | Armas Disponíveis |
|---|---|---|
| **Tenno** | Tenno Lab | Centaur, Veritux |
| **Grineer** | Grineer Lab | Corvas, Grattler, Kaszas, Onorix |
| **Corpus** | Corpus Lab | Cyngas, Dual Decurion, Fluctus, Knux, Phaedra, Velocitus |
| **Entrati** | Entrati Lab | Cortege, Larkspur, Mausolon, Morgha |

---

## Lista Completa (23)

| Arma | Tipo | Uso Terrestre | Fonte |
|---|---|---|---|
| [[centaur\|Centaur]] | Arch-Melee | Não | Pesquisa de Clã (Tenno) |
| [[cortege\|Cortege]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Entrati) |
| [[corvas\|Corvas]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Grineer) |
| [[corvas_prime\|Corvas Prime]] | Arch-Gun | Sim (Deployer) | Relíquias (Prime) |
| [[cyngas\|Cyngas]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Corpus) |
| [[dual_decurion\|Dual Decurion]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Corpus) |
| [[fluctus\|Fluctus]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Corpus) |
| [[grattler\|Grattler]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Grineer) |
| [[imperator\|Imperator]] | Arch-Gun | Sim (Deployer) | Mercado (blueprint) / Starter |
| [[imperator_vandal\|Imperator Vandal]] | Arch-Gun | Sim (Deployer) | Drop (Archwing missions) / Baro Ki'Teer |
| [[kaszas\|Kaszas]] | Arch-Melee | Não | Pesquisa de Clã (Grineer) |
| [[knux\|Knux]] | Arch-Melee | Não | Pesquisa de Clã (Corpus) |
| [[kuva_ayanga\|Kuva Ayanga]] | Arch-Gun | Sim (Deployer) | Kuva Lich |
| [[kuva_grattler\|Kuva Grattler]] | Arch-Gun | Sim (Deployer) | Kuva Lich |
| [[larkspur\|Larkspur]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Entrati) |
| [[larkspur_prime\|Larkspur Prime]] | Arch-Gun | Sim (Deployer) | Relíquias (Prime) |
| [[mausolon\|Mausolon]] | Arch-Gun | Sim (Deployer / Zenith Crown) | Pesquisa de Clã (Entrati) |
| [[morgha\|Morgha]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Entrati) |
| [[onorix\|Onorix]] | Arch-Melee | Não | Pesquisa de Clã (Grineer) |
| [[phaedra\|Phaedra]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Corpus) |
| [[prisma_veritux\|Prisma Veritux]] | Arch-Melee | Não | Baro Ki'Teer |
| [[velocitus\|Velocitus]] | Arch-Gun | Sim (Deployer) | Pesquisa de Clã (Corpus) |
| [[veritux\|Veritux]] | Arch-Melee | Não | Pesquisa de Clã (Tenno) |

---

## Referências Cruzadas

| Índice | Relação |
|---|---|
| [[_Armas _Indice\|Armas]] | Índice geral — todas as categorias de arma |
| [[_Mods _Indice\|Mods]] | Mods de Arch-Gun e Arch-Melee |
| [[_Locais _Indice\|Locais]] | Planetas com missões Archwing (Uranus, Lua, Railjack) |
| [[_Warframes _Indice\|Warframes]] | Não confundir com Archwing (exoesqueleto) — são sistemas separados |

----------------------------------------


## Seção: companheiros
### 📄 arquivo: _Companheiros _Indice.md

> [!quote]
> *"Um Tenno nunca luta verdadeiramente sozinho."*

---

## O que são Companheiros?

Companheiros são criaturas e unidades que acompanham o Tenno em missões. Cada tipo tem comportamentos, habilidades e slots de mod distintos. Apenas um companheiro pode ser equipado por vez.

Todos os companheiros têm:
- **Slot de companheiro** independente do loadout de armas/warframe
- **Sistema de mods próprio** à Companion mods e mods de arma de companheiro
- **Afeto:** substituiu a morte permanente (antes da rework de 2023) à companheiros não morrem mais de forma permanente

---

## Tipos de Companheiro

| Tipo           | Origem                               | Características                                                                          |
| -------------- | ------------------------------------ | ----------------------------------------------------------------------------------------- |
| **Sentinel**   | Mercado / Relí­quias                 | Robô flutuantes; não entram em combate direto; habilidades passivas e ativas via precepts |
| **Kubrow**     | Incubação de ovos (Plains / Mercado) | Caninos; comportamento agressivo ou utilitário conforme a raça                            |
| **Kavat**      | Incubação de DNA felino              | Felinos; buffs e utilidade; Smeeta à o mais usado em farm                                 |
| **MOA**        | Modular dê Fortuna (Solaris United)  | Robôs modulares; customizáveis com diferentes modelos e precepts                          |
| **Hound**      | Irmãs de Parvos                      | Robôs de combate; obtidos apás derrotar uma Irmã de Parvos                               |
| **Vulpaphyla** | Deimos (Entrati)                     | Raposas infestadas; ressuscitam automaticamente se morrerem                               |
| **Predasite**  | Deimos (Entrati)                     | Felinos infestados; habilidades de debuff e controle                                      |

---

## Mastery

Companheiros contribuem com **Affinity de Mastery** ao atingir Rank 30:
- Sentinels, Kubrows, Kavats, MOAs, Hounds: **3.000 pontos** cada
- Versões Prime de Sentinels: **6.000 pontos** (contam separado da versão base)

---

## Lista Completa

> [!info] Status
> `nao-obtido` · `incubado` · `maximizado` · `vendido`

### Sentinels (16)

| Companheiro | Status |
|---|---|
| [[carrier\|Carrier]] | nao-obtido |
| [[carrier_prime\|Carrier Prime]] | nao-obtido |
| [[dethcube\|Dethcube]] | nao-obtido |
| [[dethcube_prime\|Dethcube Prime]] | nao-obtido |
| [[diriga\|Diriga]] | nao-obtido |
| [[djinn\|Djinn]] | nao-obtido |
| [[helios\|Helios]] | nao-obtido |
| [[helios_prime\|Helios Prime]] | nao-obtido |
| [[nautilus\|Nautilus]] | nao-obtido |
| [[nautilus_prime\|Nautilus Prime]] | nao-obtido |
| [[oxylus\|Oxylus]] | nao-obtido |
| [[shade\|Shade]] | nao-obtido |
| [[shade_prime\|Shade Prime]] | nao-obtido |
| [[taxon\|Taxon]] | nao-obtido |
| [[wyrm\|Wyrm]] | nao-obtido |
| [[wyrm_prime\|Wyrm Prime]] | nao-obtido |

---

### Kubrows (6)

| Companheiro | Status |
|---|---|
| [[chesa\|Chesa Kubrow]] | nao-obtido |
| [[helminth_charger\|Helminth Charger]] | nao-obtido |
| [[huras\|Huras Kubrow]] | nao-obtido |
| [[raksa\|Raksa Kubrow]] | nao-obtido |
| [[sahasa\|Sahasa Kubrow]] | nao-obtido |
| [[sunika\|Sunika Kubrow]] | nao-obtido |

---

### Kavats, Vulpaphylas e Predasites (10)

| Companheiro | Status |
|---|---|
| [[adarza\|Adarza Kavat]] | nao-obtido |
| [[crescent_vulpaphyla\|Crescent Vulpaphyla]] | nao-obtido |
| [[hyena_predasite\|Hyena Predasite]] | nao-obtido |
| [[medjay_predasite\|Medjay Predasite]] | nao-obtido |
| [[panzer_vulpaphyla\|Panzer Vulpaphyla]] | nao-obtido |
| [[pharaoh_vulpaphyla\|Pharaoh Vulpaphyla]] | nao-obtido |
| [[smeeta\|Smeeta Kavat]] | nao-obtido |
| [[vasca\|Vasca Kavat]] | nao-obtido |
| [[venari\|Venari]] | nao-obtido |
| [[vizier_predasite\|Vizier Predasite]] | nao-obtido |

---

### MOAs — Modulares (6)

> MOAs são construídos em Fortuna com modelos intercambiáveis. Cada entrada representa um modelo base.

| Companheiro | Status |
|---|---|
| [[balla\|Balla MOA]] | nao-obtido |
| [[drex\|Drex MOA]] | nao-obtido |
| [[lambeo\|Lambeo MOA]] | nao-obtido |
| [[oloro\|Oloro MOA]] | nao-obtido |
| [[para\|Para MOA]] | nao-obtido |
| [[stratus\|Stratus MOA]] | nao-obtido |

---

### Hounds — Irmãs de Parvos (7)

> Hounds são obtidos ao derrotar Irmãs de Parvos. Cada entrada representa um tipo de Hound.

| Companheiro | Status |
|---|---|
| [[bhaira\|Bhaira Hound]] | nao-obtido |
| [[dorma\|Dorma Hound]] | nao-obtido |
| [[hec\|Hec Hound]] | nao-obtido |
| [[lega\|Lega Hound]] | nao-obtido |
| [[orm\|Orm Hound]] | nao-obtido |
| [[tauga\|Tauga Hound]] | nao-obtido |
| [[voca\|Voca Hound]] | nao-obtido |

---

## Por Função

### Utilidade e Farm
[[smeeta|Smeeta Kavat]] · [[carrier|Carrier]] · [[carrier_prime|Carrier Prime]] · [[sahasa|Sahasa Kubrow]] · [[chesa|Chesa Kubrow]] · [[oxylus|Oxylus]] · [[taxon|Taxon]]

### Buffs e Dano
[[adarza|Adarza Kavat]] · [[panzer_vulpaphyla|Panzer Vulpaphyla]] · [[helios|Helios]] · [[helios_prime|Helios Prime]] · [[dethcube|Dethcube]] · [[dethcube_prime|Dethcube Prime]]

### Defesa e Sobrevivência
[[raksa|Raksa Kubrow]] · [[huras|Huras Kubrow]] · [[djinn|Djinn]] · [[nautilus|Nautilus]] · [[nautilus_prime|Nautilus Prime]] · [[vasca|Vasca Kavat]]

### Furtividade
[[huras|Huras Kubrow]] · [[shade|Shade]] · [[shade_prime|Shade Prime]]

### Combate Agressivo
[[sunika|Sunika Kubrow]] · [[venari|Venari]] · [[wyrm|Wyrm]] · [[wyrm_prime|Wyrm Prime]]

### Modulares (Fortuna / Parvos)
[[lambeo|Lambeo MOA]] · [[oloro|Oloro MOA]] · [[para|Para MOA]] · [[stratus|Stratus MOA]] · [[balla|Balla MOA]] · [[drex|Drex MOA]] · [[bhaira|Bhaira Hound]] · [[lega|Lega Hound]] · [[orm|Orm Hound]]

### Deimos (Infestados)
[[panzer_vulpaphyla|Panzer Vulpaphyla]] · [[crescent_vulpaphyla|Crescent Vulpaphyla]] · [[pharaoh_vulpaphyla|Pharaoh Vulpaphyla]] · [[medjay_predasite|Medjay Predasite]] · [[vizier_predasite|Vizier Predasite]] · [[hyena_predasite|Hyena Predasite]]

---

## Curiosidades

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


## Seção: cosmeticos
### 📄 arquivo: _Cosmeticos _Indice.md

> [!quote]
> *"A aparência do Tenno é sua assinatura no Sistema Solar."*

---

## O Sistema de Estilização

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

---

## Fontes de Cosméticos

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

---

## Arquivos de Referência

| Cosmético | Arquivo | Descrição |
|---|---|---|
| [[skins\|Skins]] | skins.md | Warframe skins, weapon skins — Tennogen, Deluxe, Prime |
| [[capacetes\|Capacetes]] | capacetes.md | Helmets alternativos por frame |
| [[syandanas\|Syandanas]] | syandanas.md | Capas e ornamentos dorsais |
| [[anexos\|Anexos]] | nexos.md | Armor pieces — ombro, peito, braço, perna |
| [[efemeras\|Efemeras]] | efemeras.md | Efeitos visuais passivos no frame |
| [[paletas\|Paletas de Cores]] | paletas.md | Conjuntos de cores para customização |
| [[animacoes\|Animações e Emotes]] | nimacoes.md | Idle animations e gestos sociais |
| [[brasoes_emblemas\|Brasões e Emblemas]] | rasoes_emblemas.md | Sigils e badges de identidade |
| [[sugatras\|Sugatras]] | sugatras.md | Ornamentos pendurados em armas brancas |
| [[decoracoes\|Decorações do Orbiter]] | decoracoes.md | Itens para o Orbiter e Dojo |

---

## Tennogen

Tennogen é o programa de criação comunitária da Digital Extremes. Jogadores enviam designs via Steam Workshop — os aprovados são vendidos na Steam com divisão de royalties entre o criador e a DE.

**Regras do Tennogen:**
- Disponível principalmente no **PC via Steam** — consoles têm acesso limitado e via Platinum
- Não pode ser comprado com Platinum no PC — exige compra separada em dinheiro real
- Qualidade altamente variável — os mais populares têm votação massiva da comunidade

---

## Prime Access e Prime Vault

Cada Prime Access inclui um pacote cosmético completo:
- Skin/visual Prime do frame (via acesso antecipado)
- Syandana Prime exclusiva
- Armor set Prime
- Estátua para o Orbiter
- Efemera (em alguns pacotes recentes)

Prime Vault retorna frames Prime antigos com seus pacotes cosméticos originais.

---

## Curiosidades

- Warframe foi pioneiro em Tennogen — um dos primeiros jogos a formalizar royalties para criadores de conteúdo cosmético.
- O sistema de cores tem mais de 30 paletas disponíveis — incluindo tons que não existem na paleta padrão.
- Efemeras de Lich são farmadas intencionalmente pela comunidade — alguns elementos como Toxin Vengeful são raros e valiosos no trading.
- O modo Captura (Fashion Frame) tem comunidade própria dentro do jogo — jogadores criam poses e tiram screenshots com iluminação customizada.
- A Digital Extremes lançou skins colaborativas com franquias externas (Neon Genesis Evangelion, entre outras) — mostrando o alcance do sistema.
- Alguns jogadores chamam o sistema de customização de ''Fashion Frame'' — considerado por parte da comunidade o verdadeiro end-game do jogo.
- Sigils de sindicato contribuem passivamente com standing apenas ao serem usados em missões — mechânica pouco conhecida por iniciantes.

----------------------------------------


## Seção: cosmeticos
### 📄 arquivo: efemeras.md

﻿---
title: Efemeras
tipo: cosmetico
tags:
  - cosmetico
  - efemera
atualizado: 2026-04-19
---

## O que são Efemeras?

Efemeras são efeitos visuais passivos aplicados ao Warframe — trilhas de luz, auras elementais, partículas e distorções que seguem o frame durante o movimento.

---

## Exemplos de Tipos

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

---

## Aquisição

| Fonte | Exemplos |
|---|---|
| **Kuva Liches** | Efemeras Vengeful (7 variantes elementais) |
| **Sisters of Parvos** | Tenet Efemera |
| **Eidolons** | Efemera de Teralyst, Hydrolyst, Gantulyst |
| **Orb Vallis Bosses** | Blazing Step, Shocking Step, Freezing Step |
| **Steel Path** | Galvanized Efemera |
| **Eventos / Login** | Exclusivas por tempo limitado |
| **Prime Access** | Algumas Prime Access incluem efemeras |

---

## Observações

- Efemeras de Lich/Sister são as mais farmadas — exigem criar e derrotar liches com o elemento correto
- Algumas efemeras são extremamente raras e valiosas no trading
- Apenas uma efemera pode ser equipada por vez
- Efeitos são visíveis por todos os jogadores na missão

----------------------------------------


## Seção: cosmeticos
### 📄 arquivo: skins.md

﻿---
title: Skins
tipo: cosmetico
tags:
  - cosmetico
  - skin
atualizado: 2026-04-19
---

## O que são Skins?

Skins substituem completamente a aparência visual de um Warframe ou arma, mantendo os stats e habilidades intactos. São puramente estéticos.

---

## Tipos de Skin

| Tipo | Descrição |
|---|---|
| **Tennogen** | Criadas pela comunidade via Steam Workshop; compradas com dinheiro real via Steam |
| **Prime Accessories** | Skin + Syandana incluídos em pacotes de Prime Access |
| **Deluxe Bundles** | Skins oficiais de alta qualidade vendidas por Platinum |
| **Graxx / Feyarch** | Skins temáticas de sindicatos ou eventos |
| **Umbra Tennogen** | Skins compatíveis com Excalibur Umbra (limitadas) |
| **Weapon Skins** | Substituem o visual de armas específicas ou categorias inteiras |

---

## Fontes de Aquisição

- **Mercado** (Platinum) — Deluxe Bundles, weapon skins oficiais
- **Steam** (dinheiro real) — Tennogen exclusivo de PC
- **Prime Access / Prime Vault** — incluídos em pacotes premium
- **Nightwave** — ocasionalmente oferecidas como recompensas de rank
- **Eventos** — skins exclusivas por tempo limitado

---

## Observações

- Tennogen **não está disponível** em consoles via Steam — consoles têm seleção reduzida via Platinum
- Skins de Warframe não substituem o capacete — precisam do capacete default ou de um capacete compatível
- Algumas skins de arma cobrem categorias inteiras (ex: skin para todas as espadas simples)

----------------------------------------


## Seção: cosmeticos
### 📄 arquivo: paletas.md

﻿---
title: Paletas de Cores
tipo: cosmetico
tags:
  - cosmetico
  - paleta
  - cor
atualizado: 2026-04-19
---

## O que são Paletas?

Paletas são conjuntos de cores usados para customizar Warframes, armas, companheiros, veículos e decorações do Orbiter. Cada paleta adiciona um conjunto de tons ao editor de cores.

---

## Paletas Notáveis

| Paleta | Como Obter |
|---|---|
| **Classic Saturated** | 75.000 Créditos — paleta base acessível |
| **Tenno** | Platinum — tons variados |
| **Dojo / Syndicate** | Algumas paletas exclusivas de pesquisa de clã |
| **Event Palettes** | Drops de eventos sazonais (Frostfall, Plague Star etc.) |
| **Nightwave** | Periodicamente como recompensa de rank |
| **Twitch Drops** | Paletas distribuídas via drops de streams oficiais |
| **Paleta Prime** | Incluída em alguns Prime Access |

---

## Canais de Cor

Cada item tem múltiplos canais de cor independentes:

| Canal | Área Colorida |
|---|---|
| **Primário** | Cor dominante do item |
| **Secundário** | Cor de contraste |
| **Terciário** | Detalhes menores |
| **Quaternário** | Acentos e brilhos |
| **Energia** | Cor dos efeitos de habilidade e energia |

---

## Observações

- A paleta **Classic Saturated** é considerada essencial — cobre a maioria dos tons básicos com intensidade
- Cor de Energia afeta partículas de habilidade, olhos do frame e alguns efeitos visuais
- Paletas de evento são as mais difíceis de reobter — muitas nunca voltam
- A **Iguais** (Equals) paleta é uma das mais populares por incluir tons neutros e pretos reais

----------------------------------------


## Seção: cosmeticos
### 📄 arquivo: syandanas.md

﻿---
title: Syandanas
tipo: cosmetico
tags:
  - cosmetico
  - syandana
atualizado: 2026-04-19
---

## O que são Syandanas?

Syandanas são capas, véus e ornamentos dorsais equipados no Warframe. Vão desde capas simples até estruturas elaboradas com físicas e efeitos de partícula.

---

## Categorias Visuais

| Estilo | Exemplos |
|---|---|
| **Capas longas** | Asa de anjo, tecidos fluídos |
| **Estruturais** | Asas mecânicas, estruturas rígidas |
| **Com efeitos** | Syandanas com partículas, luz, fogo, void |
| **Prime** | Incluídas em Prime Access — geralmente douradas com design elaborado |
| **Tennogen** | Criadas pela comunidade |
| **Sindicato** | Algumas syandanas são recompensas de standing de sindicatos |

---

## Aquisição

- **Mercado** (Platinum) — maioria das syandanas
- **Prime Access / Prime Vault** — sempre incluem uma syandana Prime exclusiva
- **Tennogen** (Steam) — syandanas criadas por jogadores
- **Nightwave** — rotação periódica como recompensa
- **Eventos e Login Rewards** — ocasionalmente

---

## Observações

- Syandanas têm física simulada — reagem ao movimento e parkour do frame
- Algumas são exclusivas de pacotes e nunca voltam ao mercado individualmente
- A syandana é o cosmético mais visível durante gameplay — grande peso na identidade visual do personagem

----------------------------------------


## Seção: cosmeticos
### 📄 arquivo: animacoes.md

## O que são Animações e Emotes?

Animações customizam a postura idle do Warframe (como ele fica parado) e emotes são gestos executados manualmente para interação social ou expressão.

---

## Tipos

| Tipo | Descrição |
|---|---|
| **Idle Animation** | Substitui a animação de espera padrão do frame |
| **Emote** | Gesto ativado manualmente (dança, saudação, etc.) |
| **Stance Emotes** | Posturas alternativas que o frame assume |
| **Captura Animations** | Usadas em modo Captura para poses fotográficas |

---

## Exemplos

| Animação / Emote | Origem |
|---|---|
| **Limbo Agony** | Icônica dança de Limbo — muito popular |
| **Tennogen Idles** | Packs de animação criados pela comunidade |
| **Harka Stance** | Postura guerreira — Nightwave |
| **Emotes de Saudação** | Pack inicial ou Mercado |
| **Dança do Cetus** | Evento / Nightwave |

---

## Aquisição

- **Mercado** (Platinum) — packs de emotes e idles individuais
- **Tennogen** (Steam) — animation packs criados pela comunidade
- **Nightwave** — emotes como recompensas de rank
- **Eventos** — emotes exclusivos de eventos sazonais
- **Login Rewards** — ocasionalmente

---

## Observações

- Idle animations são visíveis apenas quando o frame está parado — grande impacto em Captura (modo fotográfico)
- Emotes são acessados via roda de comandos rápidos
- Alguns emotes sincronizam com outros jogadores próximos

----------------------------------------


## Seção: cosmeticos
### 📄 arquivo: capacetes.md

﻿---
title: Capacetes
tipo: cosmetico
tags:
  - cosmetico
  - capacete
atualizado: 2026-04-19
---

## O que são Capacetes?

Capacetes são variantes visuais do elmo de cada Warframe. Cada frame tem ao menos um capacete alternativo além do padrão. São 100% estéticos — nenhum capacete altera stats desde a rework de 2013.

---

## Aquisição

| Fonte | Método |
|---|---|
| **Mercado** | Compra direta por Platinum |
| **Alerts / Invasions** (antigo) | Eram drops de alertas antes do Nightwave substituir o sistema |
| **Tennogen** | Alguns capacetes alternativos via Steam Workshop |
| **Prime Accessories** | Capacetes Prime incluídos em pacotes de Prime Access |
| **Crafting** | Blueprints de capacetes podiam ser adquiridos e construídos na Fundição (sistema descontinuado) |

---

## Observações

- Capacetes **Prime** têm design mais elaborado e são obtidos via Prime Accessories, não via Relíquias
- Capacetes Tennogen têm qualidade variável — alguns são altamente votados pela comunidade
- A escolha do capacete não afeta gameplay — apenas aparência e preferência visual

----------------------------------------


## Seção: cosmeticos
### 📄 arquivo: anexos.md

## O que são Anexos?

Anexos são peças de armadura decorativas fixadas em partes específicas do Warframe. Não alteram stats — apenas aparência.

---

## Slots de Anexo

| Slot | Localização |
|---|---|
| **Ombro esquerdo** | Pauldron esquerdo |
| **Ombro direito** | Pauldron direito |
| **Peito** | Placa peitoral |
| **Perna esquerda** | Greave esquerda |
| **Perna direita** | Greave direita |
| **Braço** | Gauntlet (punho/antebraço) |

---

## Tipos de Anexo

| Tipo | Característica |
|---|---|
| **Armor Sets** | Conjuntos temáticos que cobrem todos os slots com design unificado |
| **Prime Accessories** | Geralmente incluem arm/chest/leg armor junto com syandana |
| **Tennogen** | Peças individuais criadas pela comunidade |
| **Sindicato** | Itens de standing de alguns sindicatos |

---

## Aquisição

- **Mercado** (Platinum) — armor sets e peças individuais
- **Prime Access / Prime Vault** — Prime Accessories sempre incluem peças de armadura
- **Tennogen** (Steam) — peças individuais votadas pela comunidade
- **Nightwave** — periodicamente como recompensa de rank

---

## Observações

- Cada slot aceita apenas uma peça por vez
- É possível misturar peças de sets diferentes para criar looks únicos
- Algumas peças têm física simulada ou efeitos de partícula

----------------------------------------


## Seção: cosmeticos
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
---

## O que são Brasões e Emblemas?

**Sigils (Brasões)** são marcas decorativas aplicadas no peito ou nas costas do Warframe. **Emblemas** são pequenos badges menores aplicados no ombro.

---

## Tipos

| Tipo | Localização | Descrição |
|---|---|---|
| **Sigil** | Peito / Costas | Marca grande, personalizável em posição e tamanho |
| **Emblema** | Ombro esquerdo / direito | Badge menor, geralmente de clã ou evento |

---

## Sigils de Sindicato

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

---

## Aquisição

| Fonte | Tipo |
|---|---|
| **Sindicatos** | Sigils de afiliação (gratuitos com rank) |
| **Eventos** | Sigils exclusivos por participação |
| **Mercado** (Platinum) | Sigils decorativos sem vínculo de sindicato |
| **Clãs** | Emblemas personalizados com o logo do clã |
| **Nightwave** | Sigils como recompensas de rank |
| **Conquistas** | Alguns sigils desbloqueiam por milestones (MR máximo, etc.) |

---

## Observações

- Emblemas de clã são criados pelo Warlord ou líderes e aplicados a todos os membros
- Sigils podem ser redimensionados e reposicionados livremente na tela de customização
- Usar sigil de sindicato durante missões contribui passivamente para o standing daquele sindicato

----------------------------------------


## Seção: cosmeticos
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
---

## O que são Decorações?

Decorações são itens colocados no interior do Orbiter (nave base do Tenno) e no Dojo (sede do clã). Permitem personalizar os ambientes de forma livre.

---

## Tipos de Decoração

| Tipo | Local | Exemplos |
|---|---|---|
| **Estátuas de Frame** | Orbiter | Estátuas Prime obtidas em Prime Access |
| **Troféus / Plaques** | Orbiter | Registram conquistas (MR, Eidolons etc.) |
| **Objetos temáticos** | Orbiter / Dojo | Plantas, móveis, artefatos Orokin |
| **Captura de Bestas** | Orbiter | Troféus de conservação (Plains, Vallis, Deimos) |
| **Decorações Sazonais** | Orbiter | Eventos como Frostfall e Naberus |
| **Dojo Rooms** | Dojo | Salas inteiras decoráveis: arenas, jardins, galerias |

---

## Aquisição

| Fonte | Itens |
|---|---|
| **Mercado** (Platinum) | Packs de decoração, estátuas |
| **Prime Access** | Estátua Prime exclusiva do pacote |
| **Conservação** | Troféus de criaturas capturadas vivas |
| **Eventos** | Decorações sazonais por participação |
| **Nightwave** | Decorações como recompensa de rank |
| **Pesquisa de Clã** | Decorações específicas do Dojo |

---

## Sistema de Decoração do Orbiter

- Decorações são posicionadas livremente em modo de edição
- Itens têm limites de capacidade (decoration cap) no Orbiter
- O Dojo tem sistema próprio com capacidade muito maior e ferramentas avançadas de construção

---

## Observações

- Estátuas Prime são consideradas itens de prestígio — indicam participação em Prime Access no lançamento
- O sistema de Dojo permite construções elaboradas — alguns clãs criam réplicas de cenários e obras de arte
- Troféus de conservação encorajam o modo de jogo de caça passiva nos open worlds

----------------------------------------


## Seção: cosmeticos
### 📄 arquivo: sugatras.md

﻿---
title: Sugatras
tipo: cosmetico
tags:
  - cosmetico
  - sugatra
atualizado: 2026-04-19
---

## O que são Sugatras?

Sugatras são ornamentos decorativos pendurados no punho ou pommel de armas brancas (melee). São análogos aos amuletos de espada em culturas orientais — puramente estéticos.

---

## Características

- Equipadas no slot de **Sugatra** de qualquer arma branca
- Ficam penduradas no punho/cabo da arma durante gameplay e animações
- Têm física simulada — balançam durante o movimento
- Uma por arma, no slot dedicado

---

## Aquisição

| Fonte | Observação |
|---|---|
| **Mercado** (Platinum) | Maioria das sugatras disponíveis |
| **Prime Access** | Algumas inclusas em pacotes Prime |
| **Nightwave** | Periodicamente como recompensa |
| **Eventos** | Sugatras exclusivas por participação |
| **Sindicatos** | Algumas disponíveis via standing |
| **Missões especiais** | Raras — drops ou recompensas de quest |

---

## Observações

- São o cosmético de menor impacto visual geral — visíveis apenas em animações de melee e câmeras próximas
- Populares entre jogadores que investem em builds de melee puro
- Algumas sugatras Prime têm efeitos de partícula sutis

----------------------------------------


## Seção: locais
### 📄 arquivo: _Locais _Indice.md

> [!quote]
> *"O Sistema Origem é vasto. E cada canto dele ainda sangra."*

---

## O Sistema Origem

O Sistema Origem é o nome dado ao Sistema Solar no universo de Warframe — o palco de todas as guerras, descobertas e tragédias que compõem a narrativa do jogo. Cada planeta e região tem história própria: cicatrizes do Império Orokin, territórios disputados por Grineer e Corpus, anomalias do Void e ruínas que guardam segredos de civilizações extintas. Navegar o mapa estelar é tanto progressão mecânica quanto exploração de um universo com milhares de anos de história acumulada.

A estrutura do mapa estelar é linear na progressão inicial — planetas são desbloqueados sequencialmente via Junctions — mas se abre completamente ao longo do jogo. Cada planeta tem facção dominante, boss exclusivo, conjunto de recursos nativos e tipos de missão disponíveis. A dificuldade escala com a posição no mapa: Mercúrio começa com inimigos de nível 1–10, enquanto Sedna e Eris chegam a 40–60 no modo normal e centenas no Steel Path.

Os Open Worlds são regiões especiais que expandem um planeta com um mapa aberto e persistente — distinto do tile set procedural das missões normais. Cada Open World tem seu próprio ecossistema, sindicato, mecânicas exclusivas e narrativa interna. São o conteúdo mais rico em termos de profundidade de sistema dentro de um único local.

---

## Mapa Estelar

### Planetas Principais

| Planeta | Facção | Boss | Nível (Normal) | Recursos Nativos |
|---|---|---|---|---|
| [[locais/planetas/mercurio\|Mercúrio]] | Grineer | Captain Vor | 1–15 | Ferrite, Polymer Bundle |
| [[locais/planetas/venus\|Vênus]] | Corpus | Jackal | 3–15 | Alloy Plate, Circuits, Polymer Bundle |
| [[locais/planetas/terra\|Terra]] | Grineer | Vay Hek | 8–22 | Ferrite, Rubedo, Neurodes |
| [[locais/planetas/marte\|Marte]] | Grineer / Corpus | Lech Kril | 10–25 | Salvage, Gallium, Morphics |
| [[locais/planetas/phobos\|Phobos]] | Corpus | Lech Kril + Vor | 15–25 | Alloy Plate, Rubedo, Morphics |
| [[locais/planetas/ceres\|Ceres]] | Grineer | Sargas Ruk | 18–28 | Alloy Plate, Circuits, Orokin Cell |
| [[locais/planetas/jupiter\|Júpiter]] | Corpus | Alad V | 20–30 | Alloy Plate, Salvage, Hexenon |
| [[locais/planetas/europa\|Europa]] | Corpus | Raptors | 25–35 | Rubedo, Control Module, Morphics |
| [[locais/planetas/saturno\|Saturno]] | Grineer | General Sargas Ruk | 28–38 | Alloy Plate, Plastids, Orokin Cell |
| [[locais/planetas/urano\|Urano]] | Grineer | Tyl Regor | 30–40 | Polymer Bundle, Plastids, Tellurium |
| [[locais/planetas/neptuno\|Netuno]] | Corpus | Hyena Pack | 33–43 | Ferrite, Nano Spores, Neural Sensors |
| [[locais/planetas/plutao\|Plutão]] | Corpus | Ambulas | 35–45 | Alloy Plate, Nano Spores, Argon Crystal |
| [[locais/planetas/sedna\|Sedna]] | Grineer | Kela de Thaym | 37–47 | Alloy Plate, Nano Spores, Orokin Cell |
| [[locais/planetas/eris\|Eris]] | Infested | Infested Alad V / Phorid | 38–48 | Nano Spores, Neurodes, Mutagen Sample |

### Áreas Especiais

| Local | Facção | Nível (Normal) | Acesso | Destaque |
|---|---|---|---|---|
| [[locais/planetas/void\|Void]] | Orokin | 25–40 | Junction de Phobos | Void Relics, Corrupted Vor, tileset Orokin |
| [[locais/planetas/lua\|Lua]] | Orokin / Sentient | 25–35 | The Second Dream (quest) | Spy avançado, tileset único, lore denso |
| [[locais/planetas/deimos\|Deimos]] | Infested / Entrati | 25–40 | Heart of Deimos (quest) | Família Entrati, Iso Vaults, Cambion Drift |
| [[locais/planetas/zariman\|Zariman Ten Zero]] | Void / Grineer antigo | 40–60 | Angels of the Zariman (quest) | Void Angels, The Holdfasts, Voidplumes |
| [[locais/planetas/kuva_fortress\|Fortaleza Kuva]] | Grineer | 25–35 | The War Within (quest) | Kuva Siphon, Kuva Flood, Kuva farm |

---

## Open Worlds

Regiões de mapa aberto com ecossistemas, sindicatos e mecânicas exclusivas. Cada uma expande um planeta existente com camadas de conteúdo que vão muito além das missões convencionais.

| Open World | Planeta Base | Sindicato | Lançamento | Warframe Exclusivo |
|---|---|---|---|---|
| [[locais/open-worlds/cetus\|Planícies de Eidolon]] | Terra | Ostron (Cetus) | Out 2017 | Gara |
| [[locais/open-worlds/fortuna\|Orbe Vallis]] | Vênus | Solaris United (Fortuna) | Nov 2018 | Baruuk |
| [[locais/open-worlds/deimos\|Câmbion Drift]] | Deimos | Entrati (Necralisk) | Ago 2020 | Xaku, Lavos |
| [[locais/open-worlds/zariman\|Zariman Ten Zero]] | — (nave perdida) | The Holdfasts (Chrysalith) | Abr 2022 | Gyre |
| [[locais/open-worlds/duviri\|Duviri]] | — (dimensão do Void) | Kaithe (Drifter's Camp) | Abr 2023 | Kullervo |

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

---

## Curiosidades

- Mercúrio é tecnicamente o planeta mais próximo do Sol no Sistema Origem, mas não é o primeiro desbloqueado — o jogo começa na Terra e Mercúrio é uma divergência lateral, refletindo a ordem de desenvolvimento do jogo.
- A Lua ficou inacessível por anos de jogo até The Second Dream em 2015 — o tileset foi construído especificamente para a revelação narrativa da quest, e voltar à Lua após completá-la tem um peso completamente diferente.
- As Planícies de Eidolon foram o maior mapa do jogo por anos — maiores que qualquer mapa de missão convencional em ordens de magnitude. A chegada do Orbe Vallis em 2018 a superou em área.
- Deimos é o único planeta do mapa estelar completamente coberto por Infested — não há facções convencionais na superfície, apenas a biomassa e os inimigos da família Entrati.
- O Duviri foi o primeiro local do jogo a não ser baseado em nenhum corpo celeste real do Sistema Solar — é uma dimensão do Void com leis físicas próprias, o que permitiu à DE criar a estética visual mais distinta da história do jogo.
- A Fortaleza Kuva era considerada irrelevante por anos antes de The War Within — após a quest, tornou-se destino regular de farm por Kuva e o único lugar com Siphons e Floods.
- Zariman foi o nome da nave antes de ser um local jogável — mencionado no lore desde o início do jogo como o evento que criou os Tenno. Chegar fisicamente à nave em 2022 foi um momento de fechamento narrativo para veteranos.
- O Void é o único bioma que não tem facção dominante no sentido convencional — os Corrupted são Orokin reanimados controlados pelo próprio ambiente, não uma civilização organizada.

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: ceres.md

# Ceres

> [!info] Visão Geral
> Cinturão de asteroides com bases Grineer pesadas

## Facção Principal
- Grineer
- Inimigos: Lancers, Napalms, Bombards

## Missões Disponíveis
- Exterminate, Defense, Survival, Sabotage

## Chefe
- [[lech_kril|Lech Kril (Exta)]] — recompensa: [[frost|Frost]] partes

## Recursos Notáveis
- Alloy Plate
- Ferrite
- Orokin Cell

## Minha Progressão
- [ ] Planeta desbloqueado
- [ ] Chefe derrotado

## Conexões
- Chefe: [[lech_kril|Lech Kril]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: deimos.md

# Deimos / Cambion Drift

> [!info] O que é
> Terceiro Open World — lua infestada de Marte. Necralisk é o hub e Cambion Drift é o exterior infestado.

## Como Acessar
- Pré-requisito: Heart of Deimos (quest)
- Rota: Marte → nó Deimos

## O que fazer aqui
- Bounties com Son/Grandmother
- Caça a Necramechs
- Criação de Necramechs
- Conservação de animais

## Facção: Entrati
- Moeda: Entrati Standing
- Cap diário de standing: MR × 1.000

## Recursos Exclusivos
- Bile
- Spinal Core Section
- Thaumic Distillate

## Recompensas de Bounty
- Partes de Necramech
- mods Deimos
- Xaku blueprint

## Minha Progressão
- [ ] Desbloqueado
- [ ] Primeiro Bounty completado
- [ ] Standing máximo alcançado

## Conexões
- Boss: [[zealoid_prelate|Zealoid Prelate]]
- Sindicato: [[mecanicas/sindicatos/entrati|Entrati]]
- Open World: [[locais/open-worlds/deimos|Câmbion Drift]]
- Warframes: [[xaku|Xaku]], [[lavos|Lavos]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: eris.md

# Eris

> [!info] Visão Geral
> Planeta completamente infestado, origem do Technocyte

## Facção Principal
- Infested
- Inimigos: Chargers, Ancients, Crawlers, Infested Corpus

## Missões Disponíveis
- Exterminate, Survival, Defense, Infested Salvage

## Chefe
- [[jordas_golem|Jordas Golem]] / [[phorid|Phorid]] — recompensa: [[atlas|Atlas]] (quest), [[nyx|Nyx]] (Phorid)

## Recursos Notáveis
- Nano Spores
- Plastids
- Neurodes

## Minha Progressão
- [ ] Planeta desbloqueado
- [ ] Chefe derrotado

## Conexões
- Chefe: [[jordas_golem|Jordas Golem]] · [[phorid|Phorid]]
- Recursos: [[recursos/]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: europa.md

# Europa

> [!info] Visão Geral
> Lua gelada com bases subaquáticas

## Facção Principal
- Corpus
- Inimigos: Crewmen, MOAs, Ospreys

## Missões Disponíveis
- Defense, Survival, Mobile Defense, Exterminate

## Chefe
- [[raptors|Raptors (Naamah)]] — recompensa: Nova partes

## Recursos Notáveis
- Ferrite
- Salvage
- Control Module

## Minha Progressão
- [ ] Planeta desbloqueado
- [ ] Chefe derrotado

## Conexões
- Chefe: [[raptors|Raptors]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: jupiter.md

# Júpiter

> [!info] Visão Geral
> Gigante gasoso com instalações flutuantes Corpus

## Facção Principal
- Corpus
- Inimigos: Crewmen, MOAs, Amalgams

## Missões Disponíveis
- Exterminate, Spy, Capture, Junction

## Chefe
- [[alad_v|Alad V (Themisto)]] — recompensa: [[nyx|Nyx]] partes

## Recursos Notáveis
- Circuits
- Oxium
- Salvage

## Minha Progressão
- [ ] Planeta desbloqueado
- [ ] Chefe derrotado

## Conexões
- Chefe: [[alad_v|Alad V]]
- Boss especial: [[ropalolyst|Ropalolyst]] — recompensa: [[wisp|Wisp]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: kuva_fortress.md



----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: lua.md

# Lua

> [!info] Visão Geral
> Instalações Orokin na Lua, desbloqueada após The Second Dream

## Facção Principal
- Orokin/Sentient
- Inimigos: Corrupted, Sentients

## Missões Disponíveis
- Exterminate, Spy, Rescue, Survival, Crossfire

## Chefe
- [[corrupted_vor|Vor Corrompido (Tycho)]] — recompensa: Mods Lua raros

## Recursos Notáveis
- Oxium
- Neural Sensors
- mods Lua

## Minha Progressão
- [ ] Planeta desbloqueado
- [ ] Chefe derrotado

## Conexões
- Chefe: [[corrupted_vor|Vor Corrompido]]
- Recursos: [[recursos/]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: marte.md

# Marte

> [!info] Visão Geral
> Planeta árido com territórios disputados

## Facção Principal
- Grineer/Corpus
- Inimigos: Lancers, Crewmen, Hyenas

## Missões Disponíveis
- Exterminate, Defense, Spy, Mobile Defense

## Chefe
- [[lech_kril|Lech Kril & Vor (War)]] — recompensa: [[excalibur|Excalibur]] partes

## Recursos Notáveis
- Morphics
- Gallium
- Rubedo

## Minha Progressão
- [ ] Planeta desbloqueado
- [ ] Chefe derrotado

## Conexões
- Chefe: [[lech_kril|Lech Kril]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: mercurio.md

# Mercúrio

> [!info] Visão Geral
> Primeiro planeta, tutorial do sistema solar

## Facção Principal
- Grineer
- Inimigos: Lancers, Troopers, Commanders

## Missões Disponíveis
- Exterminate, Mobile Defense, Spy, Capture

## Chefe
- [[captain_vor|Captain Vor (Tolstoj)]] — recompensa: Morphics, créditos

## Recursos Notáveis
- Ferrite
- Polymer Bundle
- Morphics

## Minha Progressão
- [ ] Planeta desbloqueado
- [ ] Chefe derrotado

## Conexões
- Chefe: [[captain_vor|Captain Vor]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: neptuno.md

# Netuno

> [!info] Visão Geral
> Profundezas oceânicas com refinarias Corpus

## Facção Principal
- Corpus
- Inimigos: Crewmen, MOAs, Hyenas

## Missões Disponíveis
- Exterminate, Capture, Spy, Hijack

## Chefe
- [[hyena_pack|Hyena Pack (Psamathe)]] — recompensa: [[loki|Loki]] partes

## Recursos Notáveis
- Nano Spores
- Ferrite
- Control Module

## Minha Progressão
- [ ] Planeta desbloqueado
- [ ] Chefe derrotado

## Conexões
- Chefe: [[hyena_pack|Hyena Pack]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: phobos.md

# Phobos

> [!info] Visão Geral
> Lua de Marte com instalações Corpus em ruínas

## Facção Principal
- Corpus
- Inimigos: Crewmen, MOAs, Ospreys

## Missões Disponíveis
- Exterminate, Capture, Mobile Defense, Rescue

## Chefe
- [[lech_kril|Lech Kril & Vor (Iliad)]] — recompensa: [[frost|Frost]] partes

## Recursos Notáveis
- Morphics
- Salvage
- Circuits

## Minha Progressão
- [ ] Planeta desbloqueado
- [ ] Chefe derrotado

## Conexões
- Chefe: [[lech_kril|Lech Kril]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: plutao.md

# Plutão

> [!info] Visão Geral
> Mundo frio e distante com laboratórios Corpus

## Facção Principal
- Corpus
- Inimigos: Crewmen, MOAs, Ospreys

## Missões Disponíveis
- Exterminate, Defense, Survival, Interception

## Chefe
- [[ambulas|Ambulas (Hades)]] — recompensa: [[mesa|Mesa]] partes

## Recursos Notáveis
- Nano Spores
- Plastids
- Circuits

## Minha Progressão
- [ ] Planeta desbloqueado
- [ ] Chefe derrotado

## Conexões
- Chefe: [[ambulas|Ambulas]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: saturno.md

# Saturno

> [!info] Visão Geral
> Anel planetário com fortalezas Grineer massivas

## Facção Principal
- Grineer
- Inimigos: Lancers, Napalms, Bombards, Corrupted

## Missões Disponíveis
- Exterminate, Defense, Survival, Spy

## Chefe
- [[sargas_ruk|Sargas Ruk (Tethys)]] — recompensa: [[ember|Ember]] partes

## Recursos Notáveis
- Alloy Plate
- Nano Spores
- Orokin Cell

## Minha Progressão
- [ ] Planeta desbloqueado
- [ ] Chefe derrotado

## Conexões
- Chefe: [[sargas_ruk|Sargas Ruk]]
- Recursos: [[recursos/]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: sedna.md

# Sedna

> [!info] Visão Geral
> Planeta distante com arenas Grineer (Rathuum)

## Facção Principal
- Grineer
- Inimigos: Lancers, Bombards, Executioners (Rathuum)

## Missões Disponíveis
- Exterminate, Defense, Survival, Rathuum (Arena)

## Chefe
- [[kela_de_thaym|Kela de Thaym (Merrow)]] — recompensa: [[saryn|Saryn]] partes

## Recursos Notáveis
- Nano Spores
- Plastids
- Rubedo

## Minha Progressão
- [ ] Planeta desbloqueado
- [ ] Chefe derrotado

## Conexões
- Chefe: [[kela_de_thaym|Kela de Thaym]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: terra.md

# Terra

> [!info] Visão Geral
> Planeta natal dos humanos, agora dominado pelo Grineer

## Facção Principal
- Grineer
- Inimigos: Lancers, Scorpions, Ballistas

## Missões Disponíveis
- Exterminate, Rescue, Spy, Sabotage

## Chefe
- [[vay_hek|Vay Hek (Oro)]] — recompensa: [[hydroid|Hydroid]] partes

## Recursos Notáveis
- Neurodes
- Ferrite
- Rubedo

## Minha Progressão
- [ ] Planeta desbloqueado
- [ ] Chefe derrotado

## Conexões
- Chefe: [[vay_hek|Vay Hek]]
- Open World: [[locais/open-worlds/cetus|Planícies de Eidolon (Cetus)]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: urano.md

# Urano

> [!info] Visão Geral
> Planeta inclinado com shipyards subaquáticos

## Facção Principal
- Grineer
- Inimigos: Lancers, Scorch, Hellions

## Missões Disponíveis
- Exterminate, Sabotage, Spy, Survival

## Chefe
- [[tyl_regor|Tyl Regor (Titania)]] — recompensa: [[equinox|Equinox]] partes

## Recursos Notáveis
- Alloy Plate
- Plastids
- Tellurium

## Minha Progressão
- [ ] Planeta desbloqueado
- [ ] Chefe derrotado

## Conexões
- Chefe: [[tyl_regor|Tyl Regor]]
- Recursos: [[recursos/]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: venus.md

# Vênus

> [!info] Visão Geral
> Planeta Corpus com ambientes frios e interiores corporativos

## Facção Principal
- Corpus
- Inimigos: Crewmen, MOAs, Ospreys

## Missões Disponíveis
- Exterminate, Capture, Spy, Defense

## Chefe
- [[jackal|Jackal (Fossa)]] — recompensa: [[rhino|Rhino]] partes

## Recursos Notáveis
- Polymer Bundle
- Circuits
- Rubedo

## Minha Progressão
- [ ] Planeta desbloqueado
- [ ] Chefe derrotado

## Conexões
- Chefe: [[jackal|Jackal]]
- Open World: [[locais/open-worlds/fortuna|Orbe Vallis (Fortuna)]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: void.md

# Void

> [!info] Visão Geral
> Dimensão Orokin com Torres e missões Fissure

## Facção Principal
- Orokin
- Inimigos: Corrupted enemies (versões corrompidas de Grineer e Corpus)

## Missões Disponíveis
- Exterminate, Defense, Survival, Sabotage, Capture (Fissure missions)

## Chefe
- [[corrupted_vor|Corrupted Vor]] — recompensa: mods Orokin, Argon Crystal

## Recursos Notáveis
- Argon Crystal
- Forma
- mods raros

## Minha Progressão
- [ ] Planeta desbloqueado
- [ ] Chefe derrotado

## Conexões
- Chefe: [[corrupted_vor|Corrupted Vor]]

----------------------------------------


## Seção: locais\planetas
### 📄 arquivo: zariman.md

# Zariman Ten Zero

> [!info] O que é
> Nave Orokin fantasma presa no Void. Chrysalith é o hub e os andares da nave são as missões.

## Como Acessar
- Pré-requisito: Angels of the Zariman (quest)
- Rota: Via menu de missões após a quest

## O que fazer aqui
- Bounties com Cavalero
- Farming de Incarnon Adapters
- Missões Void especiais

## Facção: The Holdfasts
- Moeda: Voidplume / Holdfasts Standing
- Cap diário de standing: MR × 1.000

## Recursos Exclusivos
- Voidplume
- Calx
- Aggristone

## Recompensas de Bounty
- Incarnon Adapters
- mods Incarnon Genesis
- Styanax blueprint

## Minha Progressão
- [ ] Desbloqueado
- [ ] Primeiro Bounty completado
- [ ] Standing máximo alcançado

## Conexões
- Boss: [[void_angel|Void Angel]]
- Sindicato: [[mecanicas/sindicatos/the_holdfasts|The Holdfasts]]
- Warframes: [[voruna|Voruna]], [[gyre|Gyre]]

----------------------------------------


## Seção: locais\open-worlds
### 📄 arquivo: cetus.md

# Cetus / Plains of Eidolon

> [!info] O que é
> Primeiro Open World. Cetus é a cidade hub e Plains of Eidolon é o campo aberto na Terra.

## Como Acessar
- Pré-requisito: The Second Dream
- Rota: Terra → nó Cetus

## O que fazer aqui
- Bounties com Konzu
- Caça aos Eidolons (noite)
- Pescaria
- Mineração
- Crafting de Amps

## Facção: Ostron
- Moeda: Ostron Standing
- Cap diário de standing: MR × 1.000

## Recursos Exclusivos
- Cetus Wisps
- Iradite
- Grokdrul
- Nistlepod

## Recompensas de Bounty
- Partes de Amp
- mods Vigilante Set
- blueprints de [[warframes/gara|Gara]]

## Minha Progressão
- [ ] Desbloqueado
- [ ] Primeiro Bounty completado
- [ ] Standing máximo alcançado

## Conexões
- Sistema: [[sistemas/plains-e-bounties|Plains & Bounties]]

----------------------------------------


## Seção: locais\open-worlds
### 📄 arquivo: deimos.md



----------------------------------------


## Seção: locais\open-worlds
### 📄 arquivo: duviri.md

# Duviri

> [!info] O que é
> Mundo surreal dentro do Void governado por Thrax. Roguelite com Warframes aleatórios.

## Como Acessar
- Pré-requisito: The Duviri Paradox (quest)
- Rota: Via menu de missões após a quest

## O que fazer aqui
- The Circuit (roguelite)
- Duviri Proper (mundo aberto)
- coleta de Intrinsics

## Facção: — (Dominus Thrax)
- Moeda: Duviri Intrinsic
- Cap diário de standing: MR × 1.000

## Recursos Exclusivos
- Pathos Clamp
- Solaris United Toroids

## Recompensas de Bounty
- Incarnon Genesis mods
- Archon Shards
- Kullervo blueprint

## Minha Progressão
- [ ] Desbloqueado
- [ ] Primeiro Bounty completado
- [ ] Standing máximo alcançado

## Conexões
- Sistema: [[sistemas/plains-e-bounties|Plains & Bounties]]

----------------------------------------


## Seção: locais\open-worlds
### 📄 arquivo: fortuna.md

# Fortuna / Orb Vallis

> [!info] O que é
> Segundo Open World em Vênus. Fortuna é o hub subterrâneo e Orb Vallis é o ambiente frio exterior.

## Como Acessar
- Pré-requisito: Vênus desbloqueado
- Rota: Vênus → nó Fortuna

## O que fazer aqui
- Bounties com Eudico
- K-Drive races
- Crafting de Kitguns/Moas
- Caça às Orb Mothers

## Facção: Solaris United
- Moeda: Solaris United Standing
- Cap diário de standing: MR × 1.000

## Recursos Exclusivos
- Debt-Bonds
- Toroids
- Thermia

## Recompensas de Bounty
- Kitguns
- Moa companions
- mods especiais
- Garuda partes

## Minha Progressão
- [ ] Desbloqueado
- [ ] Primeiro Bounty completado
- [ ] Standing máximo alcançado

## Conexões
- Sistema: [[sistemas/plains-e-bounties|Plains & Bounties]]

----------------------------------------


## Seção: locais\open-worlds
### 📄 arquivo: zariman.md



----------------------------------------


## Seção: lore
### 📄 arquivo: _Lore _Indice.md

> [!quote]
> *"Você sabe o que está dentro desses Warframes, Tenno? Você sabe o que você é?"*
> — Lotus

> [!warning] Esta seção contém spoilers das quests principais. Preencha cada arquivo após completar a quest correspondente.

---

## O Universo de Warframe

O universo de Warframe se passa em um futuro distante dentro do Sistema Solar — chamado de Sistema Origem — milhares de anos após o colapso de uma civilização avançada conhecida como Orokin. O que os jogadores encontram ao chegar é um sistema fragmentado: guerras antigas ainda em curso, facções que disputam os destroços do passado, e uma verdade sobre a natureza do próprio personagem que só se revela lentamente através das quests.

A lore do jogo não é apresentada de forma direta. Ela está espalhada em fragmentos: diálogos durante missões, arquivos de codex, esculturas Ayatan, coleções de Cephalon e — principalmente — nas Jornadas. Cada quest principal desvela uma camada da história, e algumas revelações fundamentais só chegam após dezenas ou centenas de horas de jogo. O jogador que ignora a narrativa e foca apenas no gameplay perde uma das histórias de ficção científica mais elaboradas dos jogos modernos.

A narrativa central gira em torno de uma pergunta que o jogo demora anos para responder completamente: *quem é o Tenno?* A resposta, revelada progressivamente desde The Second Dream até 1999, redefine tudo — a relação com os Warframes, com a Lotus, com o próprio corpo do personagem. Entender a lore é entender por que cada sistema de jogo existe.

---

## Cronologia

A história do universo Warframe se divide em eras definidas por eventos catastróficos. A cronologia completa está documentada em [[lore/cronologia/cronologia\|Cronologia do Universo]].

| Era | Período | Evento Central |
|---|---|---|
| [[era_orokin\|Era Orokin]] | Passado distante | Apogeu da civilização Orokin — conquista do Sistema Origem e expansão ao Tau |
| [[antiga_guerra\|A Antiga Guerra]] | Passado distante | Rebelião dos Sentient contra os Orokin — o início do fim |
| [[o_colapso\|O Colapso]] | Passado distante | Traição dos Tenno — queda do Império Orokin e colapso da civilização |
| [[era_do_despertar\|Era do Despertar]] | Presente do jogo | Tenno acordam — guerras entre Grineer, Corpus e Infested pelo Sistema Origem |
| [[a_nova_guerra\|A Nova Guerra]] | Presente do jogo | Invasão Sentient liderada por Ballas — o conflito que define o fim do mundo conhecido |
| [[ecos_do_vazio\|Ecos do Void]] | Presente do jogo | Pós-guerra — Zariman, Duviri, Sanctum e as consequências da Nova Guerra |

---

## Facções

As facções são os grupos que habitam, combatem e sobrevivem no Sistema Origem. Cada uma tem origem, motivação e papel narrativo distintos — e todas têm conexão direta com o legado Orokin.

| Facção | Origem | Papel no Universo |
|---|---|---|
| [[lore/faccoes/orokin\|Orokin]] | Civilização ancestral | Criadores dos Warframes, Tenno, Sentient e praticamente toda a tecnologia avançada do universo |
| [[lore/faccoes/tenno\|Tenno]] | Sobreviventes da tragédia Zariman | Guerreiros ligados aos Warframes via Transference — protagonistas da história |
| [[lore/faccoes/sentient\|Sentient]] | IA criada pelos Orokin | Enviados ao sistema Tau, se rebelaram e retornaram para destruir seus criadores |
| [[lore/faccoes/grineer\|Grineer]] | Clones degradados de trabalhadores Orokin | Império militarista em expansão — domina metade do Sistema Origem |
| [[lore/faccoes/corpus\|Corpus]] | Corporação mercantil | Escavam e revendem tecnologia Orokin — movidos por lucro e doutrina do Dinheiro como divindade |
| [[lore/faccoes/infested\|Infested]] | Vítimas do vírus Technocyte | Biomassa parasitária que consome tudo — não têm hierarquia organizada, apenas fome |
| [[lore/faccoes/dax\|Dax]] | Soldados de elite Orokin | Guardiões dos Orokin condicionados pela Continuidade — alguns sobreviveram ao Colapso |
| [[lore/faccoes/murmur\|Murmur]] | Entidades do Void | Criações de Albrecht Entrati — emergem do Sanctum Anatomica como ameaça pós-New War |

---

## Personagens

### Figuras Centrais

Personagens com papel narrativo direto na história principal — presentes em múltiplas quests ou responsáveis por revelações fundamentais.

| Personagem | Facção | Papel |
|---|---|---|
| [[lore/personagens/lotus\|Lotus / Natah]] | Sentient / Tenno | Guia dos Tenno — sua verdadeira identidade é o núcleo da narrativa |
| [[lore/personagens/teshin\|Teshin]] | Dax | Guardião Dax que sobreviveu ao Colapso — mentor e antagonista em diferentes momentos |
| [[lore/personagens/ballas\|Ballas]] | Orokin | Executor Orokin traidor — criador dos Warframes modernos, villain central |
| [[lore/personagens/hunhow\|Hunhow]] | Sentient | Pai de Natah — general Sentient que ameaça destruir os Tenno de dentro |
| [[lore/personagens/erra\|Erra]] | Sentient | Irmão de Natah — general que lidera a invasão da Nova Guerra |
| [[lore/personagens/albrecht_entrati\|Albrecht Entrati]] | Orokin | Cientista que descobriu o Void — sua pesquisa é a origem de quase tudo |
| [[lore/personagens/margulis\|Margulis]] | Orokin (dissidente) | Cientista que salvou e educou os Tenno — executada pelos Orokin por isso |
| [[lore/personagens/the_drifter\|The Drifter]] | Tenno | Versão alternativa do Operador — protagonista do Duviri e do arco de 1999 |

### Aliados e NPCs

Personagens recorrentes que apoiam, guiam ou fornecem contexto narrativo ao longo do jogo.

| Personagem | Contexto | Papel |
|---|---|---|
| [[lore/personagens/ordis\|Ordis]] | Nave do jogador | Cephalon da nave — IA com memórias fragmentadas de um passado violento |
| [[lore/personagens/cephalon_simaris\|Cephalon Simaris]] | Relays | Cephalon obcecado por preservar conhecimento — gerencia o Sanctuary |
| [[lore/personagens/cephalon_cy\|Cephalon Cy]] | Railjack | Cephalon militar que comanda a nave Railjack — sarcástico e pragmático |
| [[lore/personagens/nora_night\|Nora Night]] | Nightwave | Apresentadora de rádio misteriosa — voz do Nightwave e comentarista do Sistema Origem |
| [[lore/personagens/baro_kiteer\|Baro Ki'Teer]] | Relays | Comerciante de itens Prime — sua obsessão por tecnologia Orokin tem raízes narrativas |
| [[lore/personagens/eudico\|Eudico]] | Fortuna | Líder de fato dos Solaris United — carrega implante de dívida Corpus |
| [[lore/personagens/little_duck\|Little Duck]] | Vox Solaris | Agente clandestina de Fortuna — conecta ao conteúdo de Orb Mothers |
| [[lore/personagens/loid\|Loid e Otak]] | Necralisk | Synovia Entrati dividido em duas personalidades — guia do Câmbion Drift |
| [[lore/personagens/onkko\|Onkko / The Quills]] | Planícies de Eidolon | Líder dos Quills — revelado como versão alternativa de Teshin em outra linha do tempo |
| [[lore/personagens/cavalero\|Cavalero]] | Duviri | Fabricante de armas no Duviri — figura central das recompensas do circuito |
| [[lore/personagens/dominus_thrax\|Dominus Thrax]] | Duviri | Rei do Duviri — sua psique fragmentada é o próprio reino |
| [[lore/personagens/arthur\|Arthur]] | 1999 | Protagonista do arco 1999 — conexão entre o passado pré-Orokin e o presente |

### Antagonistas

| Personagem | Facção | Papel |
|---|---|---|
| [[lore/personagens/vor\|Vor]] | Grineer | Primeiro antagonista do jogo — comandante que desperta o Tenno com a Janus Key |
| [[lore/personagens/grandmother_entrati\|Avó Entrati]] | Entrati | Matriarca da família — guarda segredos sobre Albrecht e o Void |
| [[lore/personagens/father_entrati\|Pai Entrati]] | Entrati | Filho de Albrecht — fragmentado pelo Void, manufatura Necramechs |
| [[lore/personagens/son_entrati\|Filho Entrati]] | Entrati | Responsável pelos companheiros Infestados — Son Tokens |
| [[lore/personagens/daughter_entrati\|Filha Entrati]] | Entrati | Especialista em pesca Infestada — Daughter Tokens |
| [[lore/personagens/mother_entrati\|Mãe Entrati]] | Entrati | Portal entre mundos — distribui bounties do Câmbion Drift |

---

## Chefes

### Bosses de Planeta

Cada planeta tem um boss fixo desbloqueado após completar a Junction correspondente. São a principal fonte de partes de Warframe.

| Boss | Planeta | Facção | Warframe que Dropa |
|---|---|---|---|
| [[lore/chefes/captain_vor\|Captain Vor]] | Mercúrio | Grineer | — (Vor's Prize) |
| [[lore/chefes/jackal\|Jackal]] | Vênus | Corpus | Rhino |
| [[lore/chefes/vay_hek\|Vay Hek]] | Terra | Grineer | Hydroid |
| [[lore/chefes/lech_kril\|Lech Kril]] | Marte / Ceres | Grineer | Excalibur / Frost |
| [[lore/chefes/sargas_ruk\|Sargas Ruk]] | Saturno | Grineer | Ember |
| [[lore/chefes/alad_v\|Alad V]] | Júpiter | Corpus | Nyx |
| [[lore/chefes/raptors\|Raptors]] | Europa | Corpus | Nova |
| [[lore/chefes/tyl_regor\|Tyl Regor]] | Urano | Grineer | Equinox |
| [[lore/chefes/ambulas\|Ambulas]] | Plutão | Corpus | Mesa |
| [[lore/chefes/kela_de_thaym\|Kela de Thaym]] | Sedna | Grineer | Saryn |
| [[lore/chefes/phorid\|Phorid]] | Eris (invasão) | Infested | Nyx (alternativo) |
| [[lore/chefes/hyena_pack\|Hyena Pack]] | Netuno | Corpus | Loki |
| [[lore/chefes/corrupted_vor\|Corrupted Vor]] | Void | Orokin corrompido | — (loot de Void) |
| [[lore/chefes/jordas_golem\|Jordas Golem]] | Eris | Infested | Atlas (quest) |
| [[lore/chefes/zealoid_prelate\|Zealoid Prelate]] | Deimos | Infested | Harrow Systems |

### Bosses Especiais e End-Game

| Boss | Contexto | Recompensa Principal |
|---|---|---|
| [[lore/chefes/stalker\|Stalker / Shadow Stalker]] | Assassino que persegue o Tenno | Mods Stalker exclusivos, Dread / Despair / Hate |
| [[lore/chefes/eidolon_teralyst\|Eidolon Teralyst]] | Planícies — noite | Eidolon Shard, Arcanes |
| [[lore/chefes/eidolon_gantulyst\|Eidolon Gantulyst]] | Planícies — noite (Tridolon) | Brilliant Eidolon Shard, Arcanes superiores |
| [[lore/chefes/eidolon_hydrolyst\|Eidolon Hydrolyst]] | Planícies — noite (Tridolon) | Radiant Eidolon Shard, melhores Arcanes |
| [[lore/chefes/profit_taker\|Profit-Taker Orb]] | Orbe Vallis — fase 4 | Toroids raros, Arcanes, Atmo Systems |
| [[lore/chefes/exploiter_orb\|Exploiter Orb]] | Orbe Vallis — missão especial | Diluted Thermia, mods exclusivos |
| [[lore/chefes/ropalolyst\|Ropalolyst]] | Júpiter — Junction | Wisp blueprints |
| [[lore/chefes/hemocyte\|Hemocyte]] | Evento Plague Star | Helminth Charger, mods exclusivos |
| [[lore/chefes/archon_boreal\|Archon Boreal]] | Archon Hunt semanal | Archon Shard Azure |
| [[lore/chefes/archon_amar\|Archon Amar]] | Archon Hunt semanal | Archon Shard Crimson |
| [[lore/chefes/archon_nira\|Archon Nira]] | Archon Hunt semanal | Archon Shard Teal |
| [[lore/chefes/kullervo\|Kullervo]] | Duviri — boss fixo | Kullervo blueprints |
| [[lore/chefes/void_angel\|Void Angel]] | Zariman — boss de área | Voidplume Intact, Arcanes Zariman |

---

## Curiosidades

- A revelação de The Second Dream em 2015 foi um momento cultural para a comunidade — jogadores relataram parar de jogar por minutos ao perceber a verdade sobre o Tenno, e o jogo ganhou milhares de novos jogadores apenas por boca a boca sobre a twist.
- Ballas foi introduzido como narrador misterioso dos Codex muito antes de aparecer fisicamente no jogo — veteranos que leram os fragmentos reconheceram sua voz em The Sacrifice imediatamente.
- O lore de Albrecht Entrati, revelado em Whispers in the Walls, recontextualiza eventos que aconteceram milhares de anos antes dos Grineer e Corpus existirem — tornando-o o personagem com o maior impacto retroativo na narrativa.
- Ordis foi originalmente um guerreiro chamado Ordan Karris — um dos assassinos mais temidos da era Orokin. Sua transformação em Cephalon foi uma punição, e fragmentos de sua personalidade original vazam em certas falas.
- O Stalker nunca foi explicado completamente em uma única quest — sua história é construída através de fragmentos, drops de mods e o lore de The Second Dream, The Sacrifice e a quest A Man of Few Words.
- A família Entrati é uma das adições narrativas mais aclamadas do jogo — cada membro representa uma fase do luto e da disfunção familiar, e o jogador precisa navegar essa dinâmica para progredir em Deimos.
- Nora Night é amplamente teorizada como sendo a própria Lotus em uma forma alternativa, ou uma entidade do Void — a DE nunca confirmou sua verdadeira identidade, mantendo o mistério como parte do personagem.
- O Duviri Paradox revelou que o Drifter e o Operador são a mesma pessoa em linhas do tempo diferentes — uma das estruturas narrativas mais ambiciosas já implementadas em um jogo live-service.

----------------------------------------


## Seção: lore\cronologia
### 📄 arquivo: antiga_guerra.md

# A Antiga Guerra

> [!info] A Rebelião das máquinas e a batalha sangrenta das criações que testou o Império Dourado.

## O Projeto Terraformador
[Inserir explicação sobre os Sentients, máquinas capazes de se adaptar aos danos físicos, enviados para preparar o sistema em Tau.]

## O Retorno de Tau
[A rebelião dos Sentients, o descarte de restrições robóticas e o retorno focado em aniquilar a praga que são seus criadores (os Orokin).]

## A Criação Tardia: Warframes
[Os experimentos sombrios do Executor Ballas manipulando a Muta-cepa Helminth em infantes e grandes guerreiros Dax decaídos.]

## A Simbiose Perfeita (Tenno e Frames)
[A intervenção de Margulis / Lotus e o uso da *Transferência* para controlar as armaduras incontroláveis de Infestação. A virada bélica contra as Frotas Sentients.]

----------------------------------------


## Seção: lore\cronologia
### 📄 arquivo: a_nova_guerra.md

# A Nova Guerra

> [!info] A Invasão irredutível contra o Sistema Origem e o governo absoluto das Sombras e "Falsificações" pelo império Narmer.

## A Invasão Sentient
[A investida monumental da Armada Sentient (conduzida pelo renascido Erra) que penetrou todos os planetas, escravizando e obliterando fileiras de Corpus, Grineer e Tenno igualmente.]

## A Queda (Ballas e A Máscara de Narmer)
[Sem a proteção da Lua ou Lotus, fomos obliterados. Ballas e Erra subjugam todo o Sistema Origem criando uma seita divina mental universal através dos véus: O governo indissolúvel de **Narmer**. Todos que usam o véu não veem o horror, apenas glória iluminada e um sol gentil.]

## O Despertar do Derivante (Drifter)
[A introdução das paradoxais leis do temporal e multiversal: A versão do passageiro que não aceitou a barganha no Vazio ressurge, empunhando apenas de táticas "mortais", resgatando os destroços de um sistema em agonia contra os Diáconos. Destacando suporte do Herói Grineer independente que formou O Acampamento, Kahl-175.]

## O Colapso do Falso Deus Divino
[A união final entre as partes somáticas (Drifter e Operador) resgatando Praghasa e derrotando os desígnios manipuladores de Ballas frente a Margulis e a Natah originais. O sistema livre – mas eternamente machucado pelas cicatrizes físicas e sociais que as cascas de Narmer deixaram nos habitantes.]

----------------------------------------


## Seção: lore\cronologia
### 📄 arquivo: cronologia.md

# Cronologia do Universo Warframe

> [!warning] Spoilers de todas as quests principais. Preencher progressivamente conforme completar as quests.

## Era Orokin (passado distante)

> Preencher após completar [[the-sacrifice|The Sacrifice]] e [[the-new-war|The New War]].

- Os [[lore/faccoes/orokin|Orokin]] dominam o Sistema Solar
- Projeto Zariman: crianças enviadas ao Void retornam como Tenno
- [[lore/personagens/margulis|Margulis]] protege as crianças Tenno do extermínio
- Criação dos primeiros Warframes como armas de guerra
- Envio dos Sentient ao Sistema Tau para terraformação
- Rebelião dos Sentient: retornam corrompidos pelo Void
- Rebelião dos Tenno: queda do Império Orokin

## Era Atual (eventos do jogo)

- Grineer e Corpus dividem o Sistema Solar após colapso Orokin
- [[lore/personagens/lotus|Lotus]] desperta os Tenno do criostasis
- Eventos das quests se desenrolam em ordem

## Linha do Tempo das Quests

| Evento | Quest |
|--------|-------|
| Despertar dos Tenno | [[vors-prize\|Vor's Prize]] |
| Revelação do Operator | [[the-second-dream\|The Second Dream]] ⭐ |
| Origem dos Warframes | [[the-sacrifice\|The Sacrifice]] ⭐ |
| Invasão Sentient | [[the-new-war\|The New War]] ⭐ |
| Zariman descoberta | [[angels-of-the-zariman\|Angels of the Zariman]] |
| Duviri revelado | [[the-duviri-paradox\|The Duviri Paradox]] |
| Laboratórios de Albrecht | [[whispers-in-the-walls\|Whispers in the Walls]] |

----------------------------------------


## Seção: lore\cronologia
### 📄 arquivo: ecos_do_vazio.md

# Ecos do Vazio (e Paradoxo Duviri)

> [!info] O Olhar para o abismo te devolve o Olhar – "Rap. Tap. Tap." As revelações dos últimos confins da história que brincam com o conceito de realidade, ficção e tempo de uma forma apocalíptica. 

## O Paradoxo de Duviri
[O refúgio mental construído a partir de histórias de ficção infantil ganha forma manifesta no Vazio, sustentando a estada paradoxal do Drifter (O Derivante) dentro das cinco oscilações emocionais espirais de um reino despótico governado por Dominus Thrax.]

## Os Arquivos Subterrâneos de Entrati
[Descobrimento do Sanctum Anatomica cravado nas profundezas de Necralisk. Os Laboratórios gigantes que outrora pertenceram a Albrecht Entrati focados rigorosamente nos experimentos temporais, somáticos e do coração primordial do Cavia para adentrar reinos intocados.]

## Sussurros das Paredes & O Murmúrio
[A manifestação física da apatia multiversal. Aquela Barganha antiga cobra seu preço. "O Homem na Parede" expõe as criações de areia do Murmúrio que defendem uma realidade incompreensível vazando por fendas espaciotemporais. Entidade sem rosto tentando colapsar a existência em sua imagem indiferente.]

## Warframe: 1999
[A viagem de volta ao momento que originou da concepção embrionária de infecção que antecede os próprios Sentients, ou os Warframes: A exploração na cidade murada e sombria de Hollvania no ano-calendário de exatos 1999 no planeta Terra – um evento orquestrado pelo próprio desaparecido Albrecht que busca infectar humanos usando proto-fótons da Mutação Infestada em Arthur, Aoi e Letie...]

----------------------------------------


## Seção: lore\cronologia
### 📄 arquivo: era_do_despertar.md

# A Era do Despertar

> [!info] A história contemporânea: de onde o jogo efetivamente começa. O despertar dos Tenno nos dias modernos do Sistema Origem.

## O Chamado de Vor
[O despertar milenar por ordem reativada da Lotus e o embate imediato contra as frotas de Vor, salvando o próprio chassi no momento do Despertar.]

## Um Sistema Fragmentado
[Mapeamento dos confrontos diretos contra Vay Hek, Sargus Ruk (Grineer) e Alad V e Nef Anyo (Corpus), além dos constantes Surto Infestados recuperando o mapa estelar.]

## O Segundo Sonho
[A exposição da verdadeira natureza do Operador. A Lua que estava escondida no Vazio sendo trazida de volta pelo Stalker e Erra/Hunhow para o espaço real, quebrando o sonho somático de infância.]

## A Guerra Interior e O Sacrifício
[O aprendizado sob o manto das Montanhas, as intrigas do Executor Ballas ressurgindo da morte iminente de outrora, e o resgate da memória e origem do próprio Excalibur Umbra para a perseguição à antiga mãe, a Lotus.]

----------------------------------------


## Seção: lore\cronologia
### 📄 arquivo: era_orokin.md

# A Era Orokin

> [!info] O auge da humanidade no Sistema Origem e o domínio absoluto do Império Esplêndido.

## A Formação do Império
[Inserir texto sobre o ápice da raça humana governada sob a elite Orokin e suas leis de simetria e poder.]

## A Descoberta do Vazio
[Inserir detalhes sobre o gênio Albrecht Entrati e a exploração do multiverso e das barreiras dimensionais.]

## O Incidente Zariman Ten Zero
[Inserir a tragédia da expedição perdida à Tau, os pactos com "O Homem na Parede" e o surgimento das crianças irradiadas pelo Vazio (os Tenno).]

## As Ferramentas do Império
- **Grineers:** Desenvolvimento da mão de obra escrava clonada.
- **Corpus:** O cartel sectário mercantil que financiava os avanços.
- **Biologia Infestada:** Criação precursora de armas parasíticas como armamentos.

----------------------------------------


## Seção: lore\cronologia
### 📄 arquivo: o_colapso.md

# O Colapso

> [!info] A grande traição pós-guerra e a queda inevitável de todo um ecossistema estelar.

## O Sangue Dourado Derramado (Os Tambores de Vitória)
[Momentos após a vitória iminente contra os Sentients, onde os Tenno viraram as costas e as lâminas contra a arrogante e corrupta elite Orokin.]

## A Dispersão Bélica
- **Revolta Grineer:** Clones antes oprimidos que passaram a dominar territórios pelo Sistema Origem pela força massiva e violência estrutural.
- **A Ganância Corpus:** O ressurgimento do grupo focado no capital comercial para monopolizar a escassa tecnologia pós-Colapso.
- **O Surto Tecnossmótico:** A Infestação fugiu do controle biológico e tomou luas, naves e ecossistemas inteiros.

## O Longo Sono (Estase)
[A decisão protetiva da Lotus em esconder a Lua dentro do Vazio para afastar o corpo dos Tenno e mergulhá-los em milênios de Sono Criogênico ininterrupto.]

----------------------------------------


## Seção: lore\chefes
### 📄 arquivo: _Chefes _Indice.md

# Assassinatos (Os Chefes do Sistema)

> [!info] Missões singulares, nodos de planeta que culminam numa batalha elaborada e roteirizada que garantem na maioria recursos preciosos in-game ou espólios únicos de chefão.

## 🟩 Chefões da Tropa Grineer
- **[[lore/chefes/captain_vor|Capitão Vor]]** (Mercúrio, "Tolstoj")
- **[[lore/chefes/vay_hek|Conselheiro Vay Hek]]** (Terra, "Oro")
- **[[lore/chefes/lech_kril|Tenente Lech Kril]]** (Marte/Ceres)
- **[[lore/chefes/kela_de_thaym|Kela De Thaym]]** (Sedna, "Merrow")
- **[[lore/chefes/tyl_regor|Tyl Regor]]** (Urano, "Titania")

## 🟦 Consócios Corporativos Corpus
- **[[lore/chefes/jackal|O Chacal]]** (Vênus, "Fossa")
- **[[sargento|O Sargento]]** (Fobos, "Iliad")
- **[[lore/chefes/alad_v|Alad V Original e Zanuka]]** (Júpiter, "Themisto")
- **[[lore/chefes/raptors|Raptor]]** (Europa, "Naamah")
- **[[lore/chefes/hyena_pack|Matilha Hyena]]** (Netuno, "Psamathe")
- **[[lore/chefes/ambulas|Ambulas, sob Nef Anyo]]** (Plutão, "Hades")

## 🟥 Aglomerados Infestados
- **[[lore/chefes/phorid|O Phorid]]** (Dinossauro deformado espalhando Surto Infestado aleatoriamente)
- **[[lephantis|Lephantis]]** (Deimos, Magnicídio Derelict)
- **[[lore/chefes/jordas_golem|O Golem Jordas]]** (Eris, Chefe em modo Archwing)

----------------------------------------


## Seção: lore\chefes
### 📄 arquivo: jackal.md

# Jackal

> [!info] Visão Geral
> Quadrúpede robótico Corpus com ataques de laser e stomping. Primeiro chefe significativo.

## Localização
- Planeta: [[locais/planetas/venus|Vênus]]
- Nó: Fossa

## Mecânicas da Luta
1. Destrua as 4 pernas (painéis amarelos)
2. Com pernas destruídas, ataque o corpo exposto
3. Painéis amarelos nas pernas — foco de dano

## Recompensas
- Rhino Neuroptics, Chassis, Systems (rotação)

## Dicas
- Fique em movimento constante para evitar o laser de rastreamento
- [[rhino|Rhino]] é obtido aqui

## Conexões
- Local: [[locais/planetas/venus|Vênus]]
- Recompensa: [[rhino|Rhino]]

----------------------------------------


## Seção: lore\chefes
### 📄 arquivo: lech_kril.md

# Lech Kril

> [!info] Visão Geral
> Comandante Grineer congelante com martelo e sistema de resfriamento nas costas.

## Localização
- Planeta: [[locais/planetas/ceres|Ceres]]
- Nó: Exta (também em Marte - War com Vor)

## Mecânicas da Luta
1. Ataque o tubo de resfriamento nas costas para deixá-lo vulnerável
2. Com tubo destruído, ataque o corpo aquecido
3. Tubo de resfriamento nas costas — use Heat para superar o congelamento

## Recompensas
- Ember/Frost partes em Ceres; Excalibur partes com Vor em Marte

## Dicas
- Fique atrás dele para atacar o tubo
- Dano de Heat é mais eficaz quando vulnerável

## Conexões
- Local: [[locais/planetas/ceres|Ceres]]
- Recompensa: [[ember|Ember]] · [[frost|Frost]] · [[excalibur|Excalibur]]

----------------------------------------


## Seção: lore\chefes
### 📄 arquivo: profit_taker.md

# Profit-Taker Orb

> [!info] Visão Geral
> Aranha Corpus colossal em Orb Vallis. Uma das fontes principais de Arcanes endgame.

## Localização
- Planeta: [[fortuna|Fortuna / Orb Vallis]]
- Nó: Phase 4 da Heist de Fortuna

## Mecânicas da Luta
1. Destrua os escudos com tipos de dano que aparecem nas pernas
2. Ataque o núcleo exposto com dano Archgun
3. Os tipos de dano para os escudos rotacionam aleatoriamente — precisa de variedade de elementos

## Recompensas
- Arcane Energize, Guardian, Avenger e outros arcanes raros

## Dicas
- Leve múltiplos tipos de dano elemental ou use Operator para Void damage
- Principal fonte de Arcanes endgame — vale repetir

## Conexões
- Local: [[fortuna|Fortuna]]
- Recompensa: [[sistemas/arcanes|Arcanes]]

----------------------------------------


## Seção: lore\chefes
### 📄 arquivo: ropalolyst.md

# Ropalolyst

> [!info] Visão Geral
> Chefe Sentient que paira no ar e usa ataques de energia. Requer The Sacrifice para acessar.

## Localização
- Planeta: [[jupiter|Júpiter]]
- Nó: Wisp boss node (desbloqueado após The Sacrifice)

## Mecânicas da Luta
1. Conduza o Ropalolyst por cabos elétricos para danificá-lo
2. Escale para cima e ataque diretamente o ponto fraco
3. Deve ser conduzido por relâmpagos específicos no mapa

## Recompensas
- Wisp Blueprint (único — não são partes, é o blueprint completo)

## Dicas
- Aprenda o layout da arena antes de lutar
- [[wisp|Wisp]] blueprint completo — raro, pois não são partes separadas

## Conexões
- Local: [[jupiter|Júpiter]]
- Recompensa: [[wisp|Wisp]]

----------------------------------------


## Seção: lore\chefes
### 📄 arquivo: alad_v.md

# Alad V

> [!info] Visão Geral
> CEO Corpus obsessivo que usa um Warframe Zanuka como guarda-costas.

## Localização
- Planeta: [[jupiter|Júpiter]]
- Nó: Themisto

## Mecânicas da Luta
1. Destrua o Zanuka guardião primeiro
2. Ataque Alad V diretamente
3. Alad V tem escudo baixo — dano Magnetic ou Toxin eficaz

## Recompensas
- Mesa Neuroptics, Chassis, Systems

## Dicas
- Destrua o Zanuka rapidamente para focar em Alad V
- [[mesa|Mesa]] é obtida aqui

## Conexões
- Local: [[jupiter|Júpiter]]
- Recompensa: [[mesa|Mesa]]

----------------------------------------


## Seção: lore\chefes
### 📄 arquivo: ambulas.md

# Ambulas

> [!info] Visão Geral
> Corpus Moa gigante aprimorado com habilidades de cura e dano de área massivo.

## Localização
- Planeta: [[plutao|Plutão]]
- Nó: Hades

## Mecânicas da Luta
1. Damage Ambulas até ele chamar Condors (naves de resgate)
2. Destrua as naves de resgate para impedir a cura
3. Condors de resgate devem ser destruídas para evitar que cure Ambulas

## Recompensas
- Ash Neuroptics, Chassis, Systems

## Dicas
- Foque nas Condors assim que aparecerem
- [[ash|Ash]] é obtido aqui

## Conexões
- Local: [[plutao|Plutão]]
- Recompensa: [[ash|Ash]]

----------------------------------------


## Seção: lore\chefes
### 📄 arquivo: kela_de_thaym.md

# Kela de Thaym

> [!info] Visão Geral
> Gladiadora Grineer que luta em arena com plateias e mecânicas de espetáculo.

## Localização
- Planeta: [[sedna|Sedna]]
- Nó: Merrow

## Mecânicas da Luta
1. Destrua os drones de transmissão na arena
2. Ataque Kela quando os escudos caírem
3. Precisa desativar transmissores antes de causar dano a ela

## Recompensas
- Saryn Neuroptics, Chassis, Systems

## Dicas
- Priorize os transmissores antes de focar nela
- [[saryn|Saryn]] é obtida aqui

## Conexões
- Local: [[sedna|Sedna]]
- Recompensa: [[saryn|Saryn]]

----------------------------------------


## Seção: lore\chefes
### 📄 arquivo: raptors.md

# Raptors

> [!info] Visão Geral
> Três drones voadores Corpus que atacam em ondas sucessivas.

## Localização
- Planeta: [[europa|Europa]]
- Nó: Naamah

## Mecânicas da Luta
1. Destrua o primeiro Raptor
2. Dois Raptors aparecem simultaneamente
3. Escudos Corpus — Magnetic ou Toxin eficaz

## Recompensas
- Nova Neuroptics, Chassis, Systems

## Dicas
- Use armas de alto DPS para eliminar cada um rapidamente
- [[nova|Nova]] é obtida aqui

## Conexões
- Local: [[europa|Europa]]
- Recompensa: [[nova|Nova]]

----------------------------------------


## Seção: mecanicas
### 📄 arquivo: _Mecanicas _Indice.md

> [!quote]
> *"Warframe não é um jogo que você aprende em horas. É um jogo que você aprende em anos."*

---

## O que são Mecânicas?

Mecânicas são os sistemas transversais do Warframe — camadas de jogo que se aplicam a todo o conteúdo independentemente de planeta, missão ou Warframe escolhido. Enquanto recursos pertencem a planetas e mods pertencem a equipamentos, as mecânicas definem as regras fundamentais de como o jogo funciona: como o dano é calculado, como a progressão vertical se aprofunda, como a economia gira e como os sistemas sociais operam.

Compreender as mecânicas é o que separa um jogador intermediário de um veterano. Um Warframe com o mod certo no slot errado, uma build que ignora o sistema de combinações elementais, ou uma gestão ineficiente de standing e trading podem transformar centenas de horas de farm em progresso desperdiçado. Cada mecânica documentada aqui é independente — pode ser consultada isoladamente — mas todas interagem entre si em construções de alto nível.

Mecânicas específicas de Open Worlds, Railjack, Archwing ou conteúdo end-game localizado estão documentadas dentro dos arquivos de seus respectivos contextos, evitando duplicação. Este índice cobre apenas os sistemas verdadeiramente transversais.

---

## Combate

Sistemas que definem como o dano é calculado, aplicado e amplificado em qualquer situação de combate.

| Mecânica | Descrição |
|---|---|
| [[mecanicas/dano_e_status\|Dano e Status]] | Tipos de dano físico e elemental, combinações, procs e interações com facções |
| [[mecanicas/critico\|Crítico]] | Yellow crit, Orange crit, Red crit — como chance e multiplicador se relacionam |
| [[mecanicas/combo_counter\|Combo Counter]] | Acumulação de combo em armas brancas e como escala mods como Blood Rush |
| [[mecanicas/parkour\|Parkour]] | Bullet jump, wall latch, aim glide, double jump — o sistema de mobilidade |
| [[mecanicas/stealth_e_finishers\|Stealth e Finishers]] | Multiplicadores de dano furtivo, finishers e interações com frames de invisibilidade |
| [[mecanicas/augments\|Augments]] | Mods de habilidade exclusivos por Warframe — alteram ou expandem habilidades específicas |

---

## Forja e Crafting

| Mecânica | Descrição |
|---|---|
| [[mecanicas/forja\|Forja]] | Sistema de crafting — blueprints, timers, slots, rush com Platinum e gestão de produção |

---

## Progressão

Sistemas que controlam o avanço vertical do jogador — poder, flexibilidade e desbloqueios permanentes.

| Mecânica | Descrição |
|---|---|
| [[mecanicas/mastery_rank\|Mastery Rank]] | Como o MR funciona, testes por rank, benefícios e itens bloqueados por nível |
| [[mecanicas/forma_e_polaridades\|Forma e Polaridades]] | Polarização de slots, reset de rank, como planejar builds a longo prazo |
| [[mecanicas/operator_e_focus\|Operator e Focus]] | As cinco escolas de Focus, Void Mode, Amps e progressão do Operator |
| [[mecanicas/helminth\|Helminth]] | Subsumar habilidades entre Warframes — custo, restrições e sinergias |
| [[mecanicas/incarnon\|Incarnon]] | Adapters Incarnon — como ativar, evoluir e quais armas suportam |
| [[mecanicas/steel_path\|Steel Path]] | Modo de dificuldade +100 nível — desbloqueios, recompensas e Steel Essence |
| [[mecanicas/arbitrations\|Arbitrations]] | Missões sem revive com drones de escudo — recompensas e como funciona a rotação |
| [[mecanicas/nightwave\|Nightwave]] | Passe de temporada — desafios semanais, créditos e recompensas exclusivas |

---

## Economia e Social

Sistemas que governam a circulação de recursos, moedas e interações entre jogadores.

| Mecânica | Descrição |
|---|---|
| [[mecanicas/platinum\|Platinum]] | A moeda premium — como obter sem pagar, conversão e o que vale comprar |
| [[mecanicas/trading\|Trading]] | Sistema de trocas — limites por MR, Trade Tax, itens negociáveis e Trade Chat |
| [[mecanicas/baro_ki_teer\|Baro Ki'Teer]] | O Void Trader — rotação quinzenal, histórico, Ducats e como se preparar |
| [[mecanicas/cla_e_dojo\|Clã e Dojo]] | Criação e gestão de clã, pesquisa de Dojo, salas e decoração |
| [[_Sindicatos _Indice\|Sindicatos]] | Os seis sindicatos principais + Open Worlds — reputação, recompensas e alianças |

---

## Eventos

Conteúdo de tempo limitado que retorna periodicamente com mecânicas próprias e recompensas exclusivas.

| Evento | Tipo | Recompensa Principal |
|---|---|---|
| [[mecanicas/eventos/plague_star\|Plague Star]] | Operação sazonal — Eidolon | Helminth Charger, mods exclusivos |
| [[mecanicas/eventos/thermia_fractures\|Thermia Fractures]] | Operação sazonal — Orbe Vallis | Diluted Thermia, Opticor Vandal |
| [[mecanicas/eventos/razorback_armada\|Razorback Armada]] | Alerta de invasão Corpus | Brakk receiver, créditos |
| [[mecanicas/eventos/balor_fomorian\|Balor Fomorian]] | Alerta de invasão Grineer | Imperator Vandal, créditos |
| [[mecanicas/eventos/nights_of_naberus\|Nights of Naberus]] | Evento de Halloween | Cosméticos exclusivos da temporada |
| [[mecanicas/eventos/anniversary\|Anniversary]] | Aniversário do jogo — março | Itens comemorativas, Dex weapons |
| [[mecanicas/eventos/tennobaum\|Tennobaum]] | Evento de fim de ano | Cosméticos, bênçãos de comunidade |

---

## Curiosidades

- O sistema de dano do Warframe passou por uma reformulação completa em 2013 (Damage 2.0) que introduziu os tipos elementais combinados — antes existiam apenas danos físicos básicos.
- O Focus System foi adicionado em 2015 com The Second Dream e ficou praticamente sem atualização por anos antes de ser reformulado em 2021 com o sistema de Operator mais profundo.
- Helminth foi controverso no lançamento em 2020 — a comunidade ficou dividida sobre subsumar habilidades de Warframes que outros jogadores precisariam farmar para obter, e a DE restringiu quais habilidades podiam ser transferidas.
- O MR30 era considerado o teto absoluto do jogo por anos — a DE adicionou MR 31 a 40 em 2023 com os testes de Exemplar, dando aos veteranos uma meta de progressão de longo prazo inédita.
- Baro Ki'Teer visita o jogo desde 2014 — veteranos rastreiam o histórico completo de suas visitas em planilhas da comunidade para prever quais mods Primed voltarão.
- O sistema de Trading existe desde 2014 mas o Trade Chat é infame pelo volume de spam — ferramentas externas como warframe.market foram criadas pela comunidade para tornar o processo suportável.
- Nightwave substituiu o sistema de Alerts em 2019 — a mudança foi controversa porque Alerts permitiam farm direto de itens raros em momentos específicos, enquanto Nightwave distribui as recompensas ao longo de semanas.
- Steel Path foi adicionado em 2020 após anos de pedidos da comunidade por conteúdo mais difícil — a ironia é que a maioria dos veteranos o considera fácil com builds otimizadas, mas permanece útil como fonte de Steel Essence.

----------------------------------------


## Seção: mecanicas\sindicatos
### 📄 arquivo: _Sindicatos _Indice.md

> [!quote]
> *"Todo sindicato quer algo de você. A questão é se o que oferecem vale o preço."*

---

## O que são Sindicatos?

Sindicatos são facções aliadas com as quais o Tenno pode construir reputação ao longo do jogo. Cada sindicato tem uma filosofia, um conjunto de recompensas exclusivas e um limite diário de standing que pode ser ganho. A reputação é acumulada completando missões com o emblema do sindicato equipado no ombro — cada missão contribui com standing proporcional à quantidade de Afinidade gerada durante a run.

Os sindicatos principais são seis facções ideológicas que disputam influência no Sistema Origem. Eles formam duas coalizões opostas: aliados no mesmo grupo concedem acesso aos mods uns dos outros a custo maior, enquanto sindicatos rivais perdem reputação quando você ganha com o oposto. Escolher bem com quais se alinhar no início do jogo evita retrabalho de reputação mais tarde.

Além dos seis principais, existem sindicatos de Open World vinculados a cada região do mapa — Ostron nas Planícies, Solaris United na Vallis, Entrati em Deimos, The Holdfasts no Zariman, Kaithe no Duviri e Cavia no Sanctum Anatomica. Esses sindicatos funcionam de forma independente — a reputação é ganha por atividades dentro da própria área — e desbloqueiam acesso a Warframes, armas e equipamentos exclusivos de cada mundo.

---

## Como Funciona a Reputação

| Aspecto | Detalhe |
|---|---|
| **Limite diário** | Calculado como 1.000 × MR do jogador — aumenta a cada rank ganho |
| **Como ganhar** | Missões com emblema do sindicato equipado no slot de ombro |
| **Fonte** | Afinidade gerada na missão é convertida em standing proporcional |
| **Ranks** | Cada sindicato tem 5 ranks (Iniciado → Campeão) com recompensas por promoção |
| **Custo de promoção** | Cada rank exige entregar itens específicos (recursos, componentes) além do standing |
| **Rivais** | Ganhar standing com um sindicato rival reduz o standing de sindicatos opostos |
| **Sindicatos OW** | Têm seu próprio limite diário e sistema de ranks — independente dos seis principais |

---

## Alianças e Rivalidades

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

---

## Sindicatos Principais

| Sindicato | Filosofia | Mods Exclusivos Destaque | Warframe Associado |
|---|---|---|---|
| [[mecanicas/sindicatos/steel_meridian\|Steel Meridian]] | Proteção dos colonos Grineer dissidentes | Hunter Munitions, Hunter Adrenaline, Empowered Blades | — |
| [[mecanicas/sindicatos/arbiters_of_hexis\|Arbiters of Hexis]] | Transcendência e maestria do Tenno | Master's Edge, Winds of Purity, Justice Blades | — |
| [[mecanicas/sindicatos/cephalon_suda\|Cephalon Suda]] | Preservação do conhecimento e evolução | Growing Power, Entropy Burst, Lethal Torrent | — |
| [[mecanicas/sindicatos/new_loka\|New Loka]] | Pureza da humanidade original | Growing Power, Frostbite, Smite Infusion | — |
| [[mecanicas/sindicatos/red_veil\|Red Veil]] | Purificação através da destruição | Thermite Rounds, Scorch, Firewalk | — |
| [[mecanicas/sindicatos/perrin_sequence\|Perrin Sequence]] | Controle econômico e prosperidade Corpus | High Voltage, mods de pistola | — |

---

## Sindicatos de Open World

| Sindicato | Região | Como Ganhar Standing | Warframe Exclusivo |
|---|---|---|---|
| [[mecanicas/sindicatos/ostron\|Ostron]] | Planícies de Eidolon (Cetus) | Bounties, vender partes de peixe e minerais | Gara |
| [[mecanicas/sindicatos/solaris_united\|Solaris United]] | Orbe Vallis (Fortuna) | Bounties, vender peixes e minerais da Vallis | Baruuk |
| [[mecanicas/sindicatos/entrati\|Entrati]] | Câmbion Drift (Necralisk) | Bounties, oferendas de recursos Infestados | Xaku, Lavos |
| [[mecanicas/sindicatos/the_holdfasts\|The Holdfasts]] | Zariman Ten Zero | Missões Zariman, vender Voidplumes | Gyre |
| [[mecanicas/sindicatos/kaithe\|Kaithe]] | Duviri (Drifter's Camp) | Testemunhos, exploração e bosses do Duviri | Kullervo |
| [[mecanicas/sindicatos/cavia\|Cavia]] | Sanctum Anatomica (Deimos) | Missões Sanctum, oferendas de Tagfer e Vome | Qorvex, Dante |

---

## Outros Sindicatos

| Sindicato | Contexto | Como Acessar |
|---|---|---|
| **[[mecanicas/nightwave\|Nightwave (Nora Night)]]** | Passe de temporada rotativo | Automático — desafios semanais e diários | 
| **[[mecanicas/sindicatos/the_quills\|The Quills]]** | Progressão do Operator — Amp e Focus | Planícies de Eidolon, pós-The Second Dream |
| **[[mecanicas/sindicatos/vox_solaris\|Vox Solaris]]** | Progressão de Amp avançada e Orb Mothers | Fortuna, pós-rank com Solaris United |
| **[[mecanicas/sindicatos/necraloid\|Necraloid]]** | Pesquisa e progressão de Necramech | Necralisk (Deimos) |
| **[[mecanicas/sindicatos/operational_supply\|Operational Supply (Tenshin)]]** | Missões Kahl — pós-Veilbreaker | Albrecht's Laboratories |
| **[[mecanicas/sindicatos/cephalon_simaris\|Cephalon Simaris]]** | Sanctuary Onslaught e scanner | Relay — disponível desde o início |
| **[[mecanicas/sindicatos/conclave\|Conclave (Teshin)]]** | PvP entre Tennos | Relay — acesso livre |

---

## Curiosidades

- O sistema de sindicatos foi adicionado em 2014 e inicialmente causou divisão — jogadores temiam que se alinhar com um sindicato bloqueasse conteúdo permanentemente. A DE depois tornou mais fácil mudar de aliança.
- Red Veil e Steel Meridian são aliados apesar de filosofias opostas — ambos focam em ação direta, o que os une pragmaticamente contra inimigos comuns.
- New Loka é frequentemente citada como o sindicato com a narrativa mais sombria — a "pureza da humanidade" que pregam carrega conotações que a comunidade debateu extensamente.
- Cephalon Suda é tecnicamente uma inteligência artificial, o que torna sua presença como líder de sindicato humanizado uma curiosidade narrativa do universo.
- O limite diário de standing vinculado ao MR foi uma decisão deliberada da DE para incentivar a progressão de Mastery — jogadores de MR baixo que farmariam sindicatos compulsivamente eram redirecionados para diversificar o equipamento primeiro.
- Vox Solaris é o sindicato mais difícil de rankear dos Open Worlds — requer standing máximo com Solaris United como pré-requisito antes mesmo de começar.
- The Quills permaneceu misterioso por muito tempo na narrativa — seu líder Onkko é revelado como o operador de Teshin em uma linha do tempo alternativa, detalhe que poucos jogadores percebem sem ler o lore.

----------------------------------------


## Seção: missoes
### 📄 arquivo: _Missoes _Indice.md

> [!quote]
> *"Cada missão é um contrato. Cada contrato, uma oportunidade de crescer."*

---

## O que são Missões?

Missões são a unidade fundamental de jogo no Warframe. Cada nó do mapa estelar representa uma missão com tipo, facção e nível de inimigos definidos. O jogador entra sozinho ou em squad de até 4 Tennos, completa o objetivo e extrai — colhendo recursos, experiência de Afinidade e recompensas de rotação. A progressão no jogo é estruturada em torno de desbloquear novos nós, derrotar bosses de planeta e completar Junctions para avançar ao próximo sistema.

O tipo da missão determina o estilo de jogo: algumas pedem rapidez e furtividade, outras resistência prolongada. A escolha do tipo influencia diretamente o que pode ser farmado — recursos, mods, partes Prime e XP acumulam de formas distintas dependendo do objetivo em campo. Missões de sobrevivência e defesa são as mais populares para farm por volume, enquanto missões de espionagem e captura são preferidas quando o objetivo é velocidade e eficiência de rotação.

Além das missões do mapa estelar, o jogo oferece camadas adicionais de conteúdo: Jornadas (quests) que avançam a narrativa, Junctions que conectam planetas, e Bounties nos Open Worlds que funcionam como missões em cadeia dentro de um mapa aberto. Cada camada tem ritmo, recompensas e contexto narrativo próprios.

---

## Tipos de Missão

O jogo conta com mais de 20 tipos distintos de missão, organizados entre missões convencionais do mapa estelar, modos especiais de alto risco e missões exclusivas de sistemas avançados como Railjack e Archwing.

### Missões Convencionais

| Tipo | Objetivo | Recomendado Para | Disponível Em |
|---|---|---|---|
| [[missoes/tipos/exterminate\|Exterminate]] | Matar todos os inimigos ou atingir a cota de eliminações | Farm rápido de recursos, XP inicial | Todos os planetas |
| [[missoes/tipos/capture\|Capture]] | Capturar o alvo vivo e extrair | Rotação veloz, loot de captura | Todos os planetas |
| [[missoes/tipos/rescue\|Rescue]] | Resgatar prisioneiro e extrair sem matá-lo | Farm de mods, rotação rápida | Todos os planetas |
| [[missoes/tipos/sabotage\|Sabotage]] | Destruir reator ou objetivo central do mapa | Farm de recursos específicos do planeta | Todos os planetas |
| [[missoes/tipos/mobile_defense\|Mobile Defense]] | Defender três terminais sequencialmente | Farm de mods e recursos | Todos os planetas |
| [[missoes/tipos/defense\|Defense]] | Sobreviver 5/10/20+ ondas protegendo um ponto | Farm de mods, partes Prime, XP em squad | Todos os planetas |
| [[missoes/tipos/survival\|Survival]] | Sobreviver mantendo suprimento de Oxigênio ativo | Farm de volume — recursos, mods, XP | Todos os planetas |
| [[missoes/tipos/excavation\|Excavation]] | Ativar e proteger escavadoras para coletar Cryotic | Farm de Cryotic e recompensas de rotação | Todos os planetas |
| [[missoes/tipos/spy\|Spy]] | Hackear 3 cofres de dados sem acionar alarmes | Farm de Vaultrun — Warframe blueprints, mods raros | Todos os planetas |
| [[missoes/tipos/assassination\|Assassination]] | Derrotar o boss do planeta | Farm de partes de Warframe e mods de boss | Um nó por planeta |
| [[missoes/tipos/interception\|Interception]] | Capturar e manter 4 torres de sinal | Farm de recompensas de rotação, XP | Todos os planetas |
| [[missoes/tipos/hijack\|Hijack]] | Conduzir veículo blindado até a zona de extração | Desafio tático — dano ao veículo drena HP | Planetas específicos |
| [[missoes/tipos/defection\|Defection]] | Escolta de colonos Grineer em fuga por checkpoints | Farm de mod Harrow Neuroptics | Eris |
| [[missoes/tipos/infested_salvage\|Infested Salvage]] | Manter suprimentos de antídoto contra névoa infestada | Farm de blueprint do Nidus | Eris |
| [[missoes/tipos/disruption\|Disruption]] | Inserir chaves em consoles e protegê-los de Demolysts | Farm de partes de Warframe, mods Acolyte | Júpiter e outros |
| [[missoes/tipos/assault\|Assault]] | Missão longa de múltiplos objetivos em sequência | Recompensas únicas — sem opção de farm em loop | Missões especiais |
| [[missoes/tipos/rush\|Rush]] | Chegar ao ponto de extração no menor tempo possível | Não usado para farm — missão de habilidade | Competitivo |
| [[missoes/tipos/pursuit\|Pursuit]] | Destruir nave Grineer Balor Fomorian em campo Archwing | Eventos sazonais, recompensas únicas | Archwing |

### Missões de Alto Risco e Conteúdo Especial

| Tipo | Descrição | Requisito | Recompensa Principal |
|---|---|---|---|
| [[missoes/tipos/sortie\|Sortie]] | 3 missões encadeadas com modificadores de dificuldade | Conclusão de The War Within | Riven Mod, Anasa Sculpture, mods raros |
| [[missoes/tipos/archon_hunt\|Archon Hunt]] | 3 missões com boss Archon semanal — dificuldade extrema | Conclusão de The New War | Archon Shards, mods Archon |
| [[missoes/tipos/arbitration\|Arbitration]] | Survival/Defense sem revive — inimigos com escudos de drone | MR10+ e todos os nós do mapa estelar desbloqueados | Mods de Arbitration, Ayatan, Endo |
| [[missoes/tipos/nightmare\|Nightmare]] | Missão com dois modificadores negativos simultâneos | Desbloquear o nó normal equivalente | Mods Nightmare exclusivos |
| [[missoes/tipos/void_fissure\|Void Fissure]] | Missão com Void Fissures — abre Relic para obter partes Prime | Ter uma Void Relic | Partes Prime e refinamento de Relics |
| [[missoes/tipos/steel_path\|Steel Path]] | Versão com inimigos nível +100 de todo o mapa estelar | Completar 100% do mapa estelar no modo normal | Arcanes, mods Steel Path, Steel Essence |
| [[missoes/tipos/sanctuary_onslaught\|Sanctuary Onslaught]] | Ondas infinitas em zonas do Cephalon Simaris — XP extremo | Acesso ao Simulacrum (MR8) | Mods de Onslaught, Khora chassis |
| [[missoes/tipos/elite_sanctuary_onslaught\|Elite Sanctuary Onslaught]] | Versão elite do Onslaught — inimigos muito mais fortes | Completar Sanctuary Onslaught | Khora sistema/neuroptics, mods Elite |
| [[missoes/tipos/void_cascade\|Void Cascade]] | Missão Zariman — purificar Exolizers antes de explodirem | Conclusão de Angels of the Zariman | Standing Holdfasts, mods Zariman |
| [[missoes/tipos/void_flood\|Void Flood]] | Missão Zariman — coletar Vitoplast antes do timer esgotar | Conclusão de Angels of the Zariman | Standing Holdfasts, mods Zariman |
| [[missoes/tipos/void_armageddon\|Void Armageddon]] | Defense no Zariman com mecânicas de Void | Conclusão de Angels of the Zariman | Standing Holdfasts |

### Missões Railjack (Proximas)

| Tipo | Objetivo | Proxima Disponível |
|---|---|---|
| [[missoes/tipos/skirmish\|Skirmish]] | Destruir esquadrões e cruzadores inimigos no espaço | Earth, Venus, Saturn, Neptune, Veil |
| [[missoes/tipos/volatile\|Volatile]] | Invadir cruzador, destruir motor e extrair antes da explosão | Saturn, Neptune, Veil |
| [[missoes/tipos/survival_railjack\|Survival (RJ)]] | Manter suporte de vida no espaço contra ondas inimigas | Saturn, Neptune |
| [[missoes/tipos/defense_railjack\|Defense (RJ)]] | Defender ponto estratégico contra vagas no espaço | Neptune, Veil |
| [[missoes/tipos/sabotage_railjack\|Sabotage (RJ)]] | Destruir estrutura estratégica inimiga no campo de asteroides | Earth, Venus |
| [[missoes/tipos/assassination_railjack\|Assassination (RJ)]] | Derrotar boss de Proxima — Lich, Sister, Corpus flagship | Todas as Proximas |

---

## Jornadas (Quests)

Jornadas são as quests narrativas do Warframe — missões lineares com cutscenes, diálogos e revelações de lore que expandem a história do universo. Algumas desbloqueiam sistemas de jogo inteiros (como o Operator após The Second Dream), outras entregam Warframes, companheiros ou armas exclusivas. As jornadas de Warframe são quests curtas que fazem parte do loop de obtenção de um frame específico e podem ser iniciadas a qualquer momento sem dependência narrativa forte. A ordem de conclusão das quests principais importa: várias têm pré-requisitos rígidos e o jogo bloqueia o acesso sem eles.

### Jornadas Principais

| Jornada | Lançamento | Período Narrativo | Duração Est. | Pré-Requisito | Recompensa Principal |
|---|---|---|---|---|---|
| [[missoes/jornadas/principais/vors_prize\|Vor's Prize]] | Mar 2013 | Despertar do Tenno | ~20 min | — | Tutorial completo, Excalibur/Mag/Volt |
| [[missoes/jornadas/principais/once_awake\|Once Awake]] | 2013 | Pós-despertar | ~15 min | Vor's Prize | Acesso ao mercado |
| [[missoes/jornadas/principais/the_archwing\|The Archwing]] | Out 2014 | Expansão ao espaço | ~30 min | MR2, Vor's Prize | Blueprint do Archwing + Elytron |
| [[missoes/jornadas/principais/natah\|Natah]] | Jul 2015 | Revelação sobre a Lotus | ~1h | Acesso à Lua (Junction) | Acesso ao próximo capítulo |
| [[missoes/jornadas/principais/the_second_dream\|The Second Dream]] | Dez 2015 | Verdade sobre o Tenno | ~2h | Natah completa | Operator desbloqueado |
| [[missoes/jornadas/principais/the_war_within\|The War Within]] | Nov 2016 | Aprofundamento do Operator | ~3h | The Second Dream, MR5 | Poderes do Operator, Focus escolar |
| [[missoes/jornadas/principais/apostasy_prologue\|Apostasy Prologue]] | Out 2017 | Ponte narrativa — Lotus | ~10 min | The War Within | Lore, acesso ao próximo capítulo |
| [[missoes/jornadas/principais/chains_of_harrow\|Chains of Harrow]] | Jun 2017 | Horror e redenção | ~1h30 | The War Within, Sedna Junction | Blueprint do Harrow |
| [[missoes/jornadas/principais/octavias_anthem\|Octavia's Anthem]] | Mar 2017 | Música e Cephalon | ~1h | The War Within | Blueprint da Octavia |
| [[missoes/jornadas/principais/the_sacrifice\|The Sacrifice]] | Jun 2018 | Origem dos Warframes | ~2h | The War Within | Blueprint do Excalibur Umbra, Parazon |
| [[missoes/jornadas/principais/chimera_prologue\|Chimera Prologue]] | Out 2018 | Pós-Sacrifice | ~15 min | The Sacrifice | Lore Sentient |
| [[missoes/jornadas/principais/erra\|Erra]] | Dez 2019 | Invasão Sentient | ~20 min | Chimera Prologue | Lore, preparação para New War |
| [[missoes/jornadas/principais/rising_tide\|Rising Tide]] | Dez 2019 | Construção da nave | ~1h | MR8 | Dry Dock desbloqueado, acesso ao Railjack |
| [[missoes/jornadas/principais/the_deadlock_protocol\|The Deadlock Protocol]] | Jun 2020 | Herança Corpus | ~1h | MR8 | Blueprint do Protea |
| [[missoes/jornadas/principais/heart_of_deimos\|Heart of Deimos]] | Ago 2020 | Entrati e Infested | ~1h | The War Within | Acesso ao Câmbion Drift |
| [[missoes/jornadas/principais/the_waverider\|The Waverider]] | Dez 2020 | Corpus jovem e K-Drive | ~45 min | Heart of Deimos | Blueprint do Yareli |
| [[missoes/jornadas/principais/prelude_to_war\|Prelude to War]] | 2021 | Ponte pré-New War | ~15 min | Erra | Lore, acesso à New War |
| [[missoes/jornadas/principais/the_new_war\|The New War]] | Dez 2021 | Guerra total contra Sentient | ~4-5h | Erra, Heart of Deimos, MR5 | Caliban, poderes Operator expandidos |
| [[missoes/jornadas/principais/angels_of_the_zariman\|Angels of the Zariman]] | Abr 2022 | Tragédia da nave Zariman | ~1h30 | The New War | Acesso ao Zariman, Gyre |
| [[missoes/jornadas/principais/veilbreaker\|Veilbreaker]] | Set 2022 | Kahl-175 e libertação Grineer | ~1h | The New War | Styanax, acesso às missões Kahl |
| [[missoes/jornadas/principais/the_duviri_paradox\|The Duviri Paradox]] | Abr 2023 | Drifter e o reino caótico | ~2h | The New War | Acesso ao Duviri, Drifter jogável |
| [[missoes/jornadas/principais/whispers_in_the_walls\|Whispers in the Walls]] | Dez 2023 | Segredos Entrati e Albrecht | ~2h | The New War, Heart of Deimos | Acesso ao Sanctum Anatomica, Citrine |
| [[missoes/jornadas/principais/1999\|1999]] | Dez 2024 | Arthur e o passado pré-Orokin | ~3h | Whispers in the Walls | Acesso à Cidade 1999, Cyte-09 |

### Jornadas de Warframe e Companheiro

| Jornada | Lançamento | Duração Est. | Pré-Requisito | Recompensa Principal |
|---|---|---|---|---|
| [[missoes/jornadas/secundarios/howl_of_the_kubrow\|Howl of the Kubrow]] | Jun 2014 | ~30 min | Vor's Prize | Sistema de Kubrow desbloqueado, ovo de Kubrow |
| [[missoes/jornadas/secundarios/stolen_dreams\|Stolen Dreams]] | Dez 2014 | ~40 min | MR3 | Blueprint do Ash |
| [[missoes/jornadas/secundarios/hidden_messages\|Hidden Messages]] | Dez 2014 | ~30 min | MR4 | Blueprint da Mirage |
| [[missoes/jornadas/secundarios/patient_zero\|Patient Zero]] | Out 2014 | ~30 min | Vor's Prize | Blueprint da Mesa |
| [[missoes/jornadas/secundarios/the_new_strange\|The New Strange]] | Mar 2015 | ~45 min | Vor's Prize | Blueprint do Chroma |
| [[missoes/jornadas/secundarios/the_jordas_precept\|The Jordas Precept]] | Jun 2015 | ~1h | The New Strange | Blueprint do Atlas |
| [[missoes/jornadas/secundarios/the_limbo_theorem\|The Limbo Theorem]] | Jan 2015 | ~45 min | MR2 | Blueprint do Limbo |
| [[missoes/jornadas/secundarios/a_man_of_few_words\|A Man of Few Words]] | 2016 | ~20 min | The Second Dream | Lore do Stalker |
| [[missoes/jornadas/principais/sands_of_inaros\|Sands of Inaros]] | Mar 2016 | ~1h | MR5, The Second Dream | Blueprint do Inaros |
| [[missoes/jornadas/secundarios/the_silver_grove\|The Silver Grove]] | Ago 2016 | ~45 min | The Second Dream | Blueprint da Titania, sistema Apothics |
| [[missoes/jornadas/secundarios/the_index_preview\|The Index Preview]] | Out 2016 | ~20 min | MR5 | Acesso ao The Index |
| [[missoes/jornadas/secundarios/the_glast_gambit\|The Glast Gambit]] | Dez 2016 | ~1h | The War Within, MR5 | Blueprint do Nidus |
| [[missoes/jornadas/secundarios/mask_of_the_revenant\|Mask of the Revenant]] | Ago 2018 | ~45 min | The War Within | Blueprint do Revenant |

---

## Junctions

Junctions são nós especiais do mapa estelar que conectam planetas. Para desbloquear o acesso a um novo planeta, o jogador deve completar uma série de desafios no planeta atual — missões, derrotas de boss e marcos de progressão. Ao concluir, recebe um Specter do planeta destino como recompensa de combate e o acesso é liberado permanentemente. As Junctions formam o esqueleto da progressão no mapa estelar e garantem que o jogador tenha um mínimo de desenvolvimento antes de avançar.

| Junction | De → Para | Desafios Principais | Recompensa |
|---|---|---|---|
| [[missoes/juncoes/venus_junction\|Venus Junction]] | Terra → Vênus | Completar 3 missões na Terra; derrotar Captain Vor em Mercúrio; ter Mastery Rank 1 | Specter de Vênus |
| [[missoes/juncoes/mercury_junction\|Mercury Junction]] | Terra → Mercúrio | Completar 3 missões na Terra; craftar 1 Warframe; craftar 1 arma primária | Specter de Mercúrio |
| [[missoes/juncoes/mars_junction\|Mars Junction]] | Terra → Marte | Completar Exterminate na Terra; completar missão Spy; 150 kills com rifle | Specter de Marte |
| [[missoes/juncoes/phobos_junction\|Phobos Junction]] | Marte → Phobos | Completar todas as missões em Marte; derrotar o boss de Marte (Ruk) | Specter de Phobos |
| [[missoes/juncoes/ceres_junction\|Ceres Junction]] | Marte → Ceres | Completar 3 missões em Marte; 100 kills com Warframe abilities | Specter de Ceres |
| [[missoes/juncoes/jupiter_junction\|Jupiter Junction]] | Ceres → Júpiter | Completar todas as missões em Ceres; derrotar boss de Ceres (Lech Kril); MR2 | Specter de Júpiter |
| [[missoes/juncoes/europa_junction\|Europa Junction]] | Júpiter → Europa | Completar missão Spy em Júpiter; 200 kills com pistola; craftar 3 mods | Specter de Europa |
| [[missoes/juncoes/saturn_junction\|Saturn Junction]] | Europa → Saturno | Completar Survival em Europa; craftar arma usando blueprint de recompensa | Specter de Saturno |
| [[missoes/juncoes/uranus_junction\|Uranus Junction]] | Saturno → Urano | Completar missão Rescue em Saturno; 1000 kills com Warframe; MR4 | Specter de Urano |
| [[missoes/juncoes/neptune_junction\|Neptune Junction]] | Urano → Netuno | Completar Interception em Urano; completar Archwing mission | Specter de Netuno |
| [[missoes/juncoes/pluto_junction\|Pluto Junction]] | Netuno → Plutão | Completar Defense em Netuno; derrotar Raptor em Europa; MR5 | Specter de Plutão |
| [[missoes/juncoes/sedna_junction\|Sedna Junction]] | Plutão → Sedna | Completar Spy em Plutão; completar missão Hijack; craftar Forma | Specter de Sedna |
| [[missoes/juncoes/eris_junction\|Eris Junction]] | Sedna → Eris | Completar Assassination em Sedna; 500 kills com branca; MR6 | Specter de Eris |
| [[missoes/juncoes/lua_junction\|Lua Junction]] | Eris → Lua | Completar The Second Dream (quest obrigatória); todas as missões em Eris | Specter da Lua |
| [[missoes/juncoes/kuva_fortress_junction\|Kuva Fortress Junction]] | Sedna → Fortaleza Kuva | Completar The War Within; MR5 | Acesso à Fortaleza Kuva |
| [[missoes/juncoes/void_junction\|Void Junction]] | Phobos → Void | Completar 3 missões em Phobos; usar Void Relic uma vez | Acesso ao Void |
| [[missoes/juncoes/deimos_junction\|Deimos Junction]] | Marte → Deimos | Completar Heart of Deimos (quest); todas as missões em Marte | Acesso ao Câmbion Drift |
| [[missoes/juncoes/zariman_junction\|Zariman Junction]] | — | Completar Angels of the Zariman (quest) | Acesso ao Zariman Ten Zero |

---

## Bounties (Open Worlds)

Bounties são missões encadeadas oferecidas pelos sindicatos dos Open Worlds. Cada bounty é composto por 3 a 5 etapas sequenciais com objetivos variados — Defense, Capture, Sabotage, Assassination — que ocorrem dentro do mapa aberto sem tela de loading entre elas. Completar o bounty inteiro entrega as recompensas de todas as etapas mais um bônus final. As recompensas incluem standing com o sindicato local, itens exclusivos da área e partes de Warframes específicos de cada mundo. O nível de dificuldade é escolhido antes de iniciar, com tiers progressivos que determinam o nível dos inimigos e a qualidade das recompensas.

### [[missoes/bounties/eidolon\|Planícies de Eidolon]]
*Sindicato: Ostron (Cetus) · Nível Base: Dia — inimigos comuns; Noite — Vomvalysts e Eidolons*

| Tier | Nível dos Inimigos | Recompensas Destaque | Melhor Para |
|---|---|---|---|
| **Tier 1** | 10–30 | Standing Ostron, Iradite, blueprints básicos | Início de jogo, farm de recursos comuns |
| **Tier 2** | 20–40 | Standing, Gara Neuroptics, Cetus Wisp | Farm de Gara e recursos incomuns |
| **Tier 3** | 30–50 | Standing, Gara Chassis, Cores Sentient | Farm de Gara e Sentient Cores |
| **Tier 4** | 40–60 | Standing, Gara Systems, Breath of the Eidolon | Farm de Gara Systems e materiais raros |
| **Tier 5** | 50–70+ | Standing máximo, recompensas raras, mods Ostron | Farm de standing e recompensas end-tier |
| **Caça Eidolon (Noite)** | 30–60 | Eidolon Shards, Brilliant/Radiant Shards, Arcanes | Farm de Arcanes e progressão do Operator |

### [[missoes/bounties/orbe_vallis\|Orbe Vallis]]
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

### [[missoes/bounties/cambion_drift\|Câmbion Drift]]
*Sindicato: Entrati (Necralisk) · Ciclo dia (Fass) / noite (Vome) afeta recursos e spawns Infestados*

| Tier | Nível dos Inimigos | Recompensas Destaque | Melhor Para |
|---|---|---|---|
| **Tier 1** | 15–35 | Standing Entrati, Bile, Ganglion | Início no Deimos |
| **Tier 2** | 25–45 | Standing, Xaku Neuroptics, materiais Infestados | Farm de Xaku |
| **Tier 3** | 35–55 | Standing, Xaku Chassis, Namalon | Farm de Xaku e Necramech components |
| **Tier 4** | 45–65 | Standing, Xaku Systems, Pustulant Cerebrum | Farm de Xaku Systems |
| **Tier 5** | 55–75+ | Standing máximo, Necramech mods, recompensas raras | Farm de mods Necramech e standing |
| **Iso Vault** | 40–80 | Blueprints Necramech, Namalon, Voidrig/Bonewidow parts | Farm de Necramech completo |

### [[missoes/bounties/duviri\|Duviri]]
*Sindicato: Kaithe (Drifter's Camp) · Mecânica roguelike — cada run tem armas e frames aleatórios do Decret*

| Tier | Nível dos Inimigos | Recompensas Destaque | Melhor Para |
|---|---|---|---|
| **Testemunho (Normal)** | 30–60 | Pathos Clamp, blueprints Duviri, mods | Introdução ao Duviri, farm de Pathos Clamp |
| **Testemunho (Hard)** | 60–100 | Cavalero's Burden, mods raros, Incarnon Genesis | Farm de Incarnon Adapters |
| **O Circuito** | Variável | Incarnon Genesis adapters por semana | Meta de farm — Incarnon para armas clássicas |
| **Kullervo** | 80–100 | Kullervo parts, Kullervo's Bane | Farm do Warframe Kullervo |

### [[missoes/bounties/zariman\|Zariman Ten Zero]]
*Sindicato: The Holdfasts (Chrysalith) · Ambiente Void — inimigos Void Angels e Zariman enemies*

| Tier | Nível dos Inimigos | Recompensas Destaque | Melhor Para |
|---|---|---|---|
| **Tier 1** | 40–60 | Standing Holdfasts, Voidplume Pinion/Quill | Início no Zariman |
| **Tier 2** | 50–70 | Standing, Gyre Neuroptics, Voidplume Crest | Farm de Gyre |
| **Tier 3** | 60–80 | Standing, Gyre Chassis, Voidplume Drift | Farm de Gyre e recursos raros |
| **Tier 4** | 70–90 | Standing, Gyre Systems, Voidplume Down | Farm de Gyre Systems |
| **Tier 5** | 80–100+ | Standing máximo, Arcanes Zariman, Voidplume Intact | Farm de Arcanes e mods Zariman |
| **Void Angel** | 80–100 | Voidplume Intact, Arcanes raros | Recurso mais raro do Zariman |

---

## Curiosidades

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


## Seção: mods
### 📄 arquivo: _Mods _Indice.md

# Mods — Índice

> [!quote]
> *"Mods não são apenas upgrades. São a linguagem com que você reescreve um Warframe."*

---

## Visão Geral

Mods são o **sistema central de progressão e customização** do Warframe. Cada mod é um cartão equipável que modifica atributos de Warframes, armas ou companheiros — aumentando dano, defesa, velocidade de habilidades, alcance e dezenas de outros parâmetros. Sem mods, um Warframe é apenas uma casca; com o conjunto certo, o mesmo frame pode ter desempenhos radicalmente diferentes dependendo do conteúdo.

Mods são obtidos de diversas fontes: drops de inimigos, recompensas de missão, sindicatos, Nightwave e vendedores especiais. Cada mod tem um **custo de capacidade** que consome o pool de mod capacity do equipamento — e pode ser rankiado com **Endo** e **Créditos** para aumentar seus efeitos (e custo) simultaneamente.

---

## Como Adquirir

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

---

## Raridades

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

---

## Sistema de Capacidade

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

---

## Sub-Índices

| Sub-Índice | Conteúdo Exclusivo |
|---|---|
| [[_Mods Warframe _Indice\|Mods de Warframe]] | Defesa, habilidades (4 pilares), aura, exilus, augments, set Umbral |
| [[_Mods Armas _Indice\|Mods de Armas]] | Primárias, secundárias, brancas, stances, archwing; combinações elementais |
| [[_Mods Companheiros _Indice\|Mods de Companheiros]] | Sentinels, kavats, kubrows, MOAs, hounds; precept mods |
| [[_Mods Especiais _Indice\|Mods Especiais]] | Primed, Umbral, Corrupted (Orokin Vault), Syndicate, Rivens, Amalgam |

---

## Curiosidades

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

---

## Referências Cruzadas

| Índice | Relação |
|---|---|
| [[_Warframes _Indice\|Warframes]] | Frames que equipam os mods de warframe |
| [[_Armas _Indice\|Armas]] | Armas que equipam os mods de arma |
| [[_Companheiros _Indice\|Companheiros]] | Companheiros que equipam mods de companheiro |
| [[_Mecanicas _Indice\|Mecânicas]] | Sistemas de combate que os mods influenciam |
| [[_Sindicatos _Indice\|Sindicatos]] | Fonte de mods Syndicate |

----------------------------------------


## Seção: mods\armas
### 📄 arquivo: _Mods Armas _Indice.md

# Mods de Armas — Índice

> [!quote]
> *"A arma é o veículo. Os mods são o motor."*

---

## Visão Geral

Mods de armas modificam **dano, velocidade, crítico, status e elementos** de armas primárias, secundárias, brancas e archwing. Cada categoria de arma tem mods específicos — um mod de rifle não se aplica a pistolas, e stances são exclusivos de brancas.

**Slots:** 8 normais + 1 Exilus (requer Exilus Weapon Adapter) + 1 Arcane (armas com slot arcane)
**Capacidade base:** 30 (rank 30) → 60 com Orokin Catalyst

---

## Combinações de Dano Elemental

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

---

## Primárias — Dano e Crítico

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[serration\|Serration]] | Comum | +Dano base de rifle | Drop geral |
| [[primed_serration\|Primed Serration]] | Primed | +Dano base muito elevado | Baro Ki'Teer |
| [[split_chamber\|Split Chamber]] | Incomum | +Multishot — projéteis extras por disparo | Drop geral |
| [[vigilante_armaments\|Vigilante Armaments]] | Incomum | +Multishot + chance de upgrade de crítico | Drop geral (set Vigilante) |
| [[point_strike\|Point Strike]] | Incomum | +Chance de crítico | Drop geral |
| [[vital_sense\|Vital Sense]] | Incomum | +Multiplicador de crítico | Drop geral |
| [[argon_scope\|Argon Scope]] | Lendário | +Chance de crítico temporário ao dar headshot | Arbitrations |
| [[hunter_munitions\|Hunter Munitions]] | Raro | Críticos aplicam Slash — rifle | Syndicato (Steel Meridian) |
| [[heavy_caliber\|Heavy Caliber]] | Corrupted | +Dano muito alto / -Accuracy | Orokin Vault |
| [[critical_delay\|Critical Delay]] | Corrupted | +Chance de crítico alto / -Fire Rate | Orokin Vault |
| [[vile_acceleration\|Vile Acceleration]] | Corrupted | +Fire Rate muito alto / -Dano base | Orokin Vault |
| [[speed_trigger\|Speed Trigger]] | Incomum | +Fire Rate | Drop geral |
| [[shred\|Shred]] | Incomum | +Fire Rate + Punch Through | Drop geral |
| [[tainted_mag\|Tainted Mag]] | Corrupted | +Magazine Size / -Reload Speed | Orokin Vault |
| [[depleted_reload\|Depleted Reload]] | Corrupted | -Reload Time / -Magazine Size | Orokin Vault |

---

## Primárias — Elementais

| Mod | Raridade | Elemento | Nota |
|---|---|---|---|
| [[hellfire\|Hellfire]] | Incomum | +Calor | Drop geral |
| [[cryo_rounds\|Cryo Rounds]] | Incomum | +Frio | Drop geral |
| [[stormbringer\|Stormbringer]] | Incomum | +Elétrico | Drop geral |
| [[infected_clip\|Infected Clip]] | Incomum | +Tóxico | Drop geral |
| [[primed_cryo_rounds\|Primed Cryo Rounds]] | Primed | +Frio muito elevado | Baro Ki'Teer |
| [[high_voltage\|High Voltage]] | Raro | +Elétrico + proc Elétrico | Syndicato (Perrin Sequence) |
| [[thermite_rounds\|Thermite Rounds]] | Raro | +Calor + proc Calor | Syndicato (Red Veil) |
| [[rime_rounds\|Rime Rounds]] | Incomum | +Frio — espingardas | Drop geral |
| [[seeking_force\|Seeking Force]] | Incomum | +Punch Through — espingardas | Drop geral |
| [[tainted_shell\|Tainted Shell]] | Corrupted | +Pellet Count / -Fire Rate — espingardas | Orokin Vault |

---

## Secundárias

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[hornet_strike\|Hornet Strike]] | Comum | +Dano base de pistola | Drop geral |
| [[barrel_diffusion\|Barrel Diffusion]] | Incomum | +Multishot de pistola | Drop geral |
| [[lethal_torrent\|Lethal Torrent]] | Raro | +Multishot + Fire Rate | Syndicato (Cephalon Suda) |
| [[pistol_gambit\|Pistol Gambit]] | Incomum | +Chance de crítico de pistola | Drop geral |
| [[target_cracker\|Target Cracker]] | Incomum | +Multiplicador de crítico de pistola | Drop geral |
| [[primed_pistol_gambit\|Primed Pistol Gambit]] | Primed | +Chance de crítico muito elevado | Baro Ki'Teer |
| [[primed_target_cracker\|Primed Target Cracker]] | Primed | +Multiplicador de crítico muito elevado | Baro Ki'Teer |
| [[anemic_agility\|Anemic Agility]] | Corrupted | +Fire Rate / -Dano base | Orokin Vault |
| [[convulsion\|Convulsion]] | Incomum | +Elétrico em pistola | Drop geral |
| [[deep_freeze\|Deep Freeze]] | Incomum | +Frio em pistola | Drop geral |
| [[heated_charge\|Heated Charge]] | Incomum | +Calor em pistola | Drop geral |
| [[pathogen_rounds\|Pathogen Rounds]] | Incomum | +Tóxico em pistola | Drop geral |
| [[frostbite\|Frostbite]] | Raro | +Frio + proc Frio em pistola | Syndicato (New Loka) |
| [[scorch\|Scorch]] | Raro | +Calor + proc Calor em pistola | Syndicato (Red Veil) |
| [[hemorrhage\|Hemorrhage]] | Raro | Procs de Impact → Slash em pistola | Syndicato (Steel Meridian) |
| [[augur_pact\|Augur Pact]] | Incomum | Gasto de Energia aumenta dano de pistola | Syndicatos (set Augur) |

---

## Brancas — Dano e Crítico

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[pressure_point\|Pressure Point]] | Comum | +Dano base branca | Drop geral |
| [[primed_pressure_point\|Primed Pressure Point]] | Primed | +Dano base muito elevado | Baro Ki'Teer |
| [[true_steel\|True Steel]] | Incomum | +Chance de crítico | Drop geral |
| [[organ_shatter\|Organ Shatter]] | Incomum | +Multiplicador de crítico | Drop geral |
| [[blood_rush\|Blood Rush]] | Raro | +Crítico escala com Combo Counter | Arbitrations |
| [[weeping_wounds\|Weeping Wounds]] | Raro | +Status escala com Combo Counter | Arbitrations |
| [[condition_overload\|Condition Overload]] | Raro | +Dano por status ativo no alvo | Drop geral |
| [[spoiled_strike\|Spoiled Strike]] | Corrupted | +Dano muito alto / -Attack Speed | Orokin Vault |
| [[berserker_fury\|Berserker Fury]] | Raro | +Attack Speed ao realizar crítico | Drop geral |
| [[quickening\|Quickening]] | Incomum | +Attack Speed + Combo Duration | Drop geral |
| [[body_count\|Body Count]] | Incomum | +Duração do Combo Counter | Drop geral |
| [[drifting_contact\|Drifting Contact]] | Corrupted | +Combo Duration / chance de Status | Orokin Vault |
| [[corrupt_charge\|Corrupt Charge]] | Corrupted | +Combo inicial alto / -Duração do Counter | Orokin Vault |
| [[life_strike\|Life Strike]] | Raro | Consume Combo → regenera HP | Drop geral |
| [[healing_return\|Healing Return]] | Raro | Regenera HP por hit em alvo com status ativo | Drop geral |
| [[primed_fever_strike\|Primed Fever Strike]] | Primed | +Tóxico muito elevado em brancas | Baro Ki'Teer |

---

## Brancas — Stances

Stances são mods de slot exclusivo que substituem completamente os ataques normais da arma por combos específicos. Ver [[_Armas _Brancas _Indice|Brancas — Stances por Tipo]] para a tabela completa de compatibilidade.

| Mod | Raridade | Tipo de Arma | Fonte |
|---|---|---|---|
| [[crimson_dervish\|Crimson Dervish]] | Raro | Espada | Drop geral |
| [[swooping_falcon\|Swooping Falcon]] | Raro | Espada | Drop geral |
| [[iron_phoenix\|Iron Phoenix]] | Incomum | Espada | Drop geral |
| [[vengeful_revenant\|Vengeful Revenant]] | Raro | Espada | Drop geral |
| [[blind_justice\|Blind Justice]] | Raro | Nikana / Espada | Drop geral |
| [[tranquil_cleave\|Tranquil Cleave]] | Incomum | Nikana | Drop geral |
| [[decisive_judgement\|Decisive Judgement]] | Raro | Nikana | Drop geral |
| [[eleventh_storm\|Eleventh Storm]] | Raro | Espadim (Rapier) | Drop geral |
| [[pointed_wind\|Pointed Wind]] | Incomum | Espadim / Adaga | Drop geral |
| [[tempo_royale\|Tempo Royale]] | Raro | Espada Pesada | Drop geral |
| [[rending_crane\|Rending Crane]] | Incomum | Espada Pesada | Drop geral |
| [[cleaving_whirlwind\|Cleaving Whirlwind]] | Raro | Espada Pesada | Drop geral |
| [[swirling_tiger\|Swirling Tiger]] | Raro | Espadas Duplas | Drop geral |
| [[crossing_snakes\|Crossing Snakes]] | Incomum | Espadas Duplas | Drop geral |
| [[dividing_blades\|Dividing Blades]] | Raro | Espadas Duplas | Drop geral |
| [[homing_fang\|Homing Fang]] | Raro | Adaga / Adagas Duplas | Drop geral |
| [[gnashing_payara\|Gnashing Payara]] | Raro | Adagas Duplas | Drop geral |
| [[spinning_needle\|Spinning Needle]] | Raro | Adagas Duplas | Drop geral |
| [[shimmering_blight\|Shimmering Blight]] | Incomum | Lança (Polearm) | Drop geral |
| [[bleeding_willow\|Bleeding Willow]] | Raro | Lança (Polearm) | Drop geral |
| [[typhoon_s_edge\|Typhoon's Edge]] | Raro | Lança (Polearm) | Drop geral |
| [[clashing_forest\|Clashing Forest]] | Incomum | Cajado (Staff) | Drop geral |
| [[flailing_branch\|Flailing Branch]] | Incomum | Cajado (Staff) | Drop geral |
| [[atlantas_struggle\|Atlantas Struggle]] | Raro | Nunchaku | Drop geral |
| [[gemini_cross\|Gemini Cross]] | Raro | Tonfa | Drop geral |
| [[sovereign_outcast\|Sovereign Outcast]] | Raro | Tonfa | Drop geral |
| [[crushing_ruin\|Crushing Ruin]] | Raro | Martelo | Drop geral |
| [[shattering_storm\|Shattering Storm]] | Incomum | Martelo | Drop geral |
| [[vermillion_storm\|Vermillion Storm]] | Raro | Garras | Drop geral |
| [[seismic_palm\|Seismic Palm]] | Incomum | Garras | Drop geral |
| [[brutal_tide\|Brutal Tide]] | Raro | Garras | Drop geral |
| [[reaping_spiral\|Reaping Spiral]] | Raro | Foice (Scythe) | Drop geral |
| [[stalking_fan\|Stalking Fan]] | Raro | Foice (Scythe) | Drop geral |
| [[astral_twilight\|Astral Twilight]] | Raro | Glaive | Drop geral |
| [[defiled_snapdragon\|Defiled Snapdragon]] | Raro | Chicote | Drop geral |
| [[burning_wasp\|Burning Wasp]] | Incomum | Chicote | Drop geral |
| [[wise_razor\|Wise Razor]] | Raro | Lâmina e Chicote | Drop geral |
| [[final_harbinger\|Final Harbinger]] | Raro | Espada e Escudo | Drop geral |
| [[bullet_dance\|Bullet Dance]] | Raro | Espingarda Melee | Drop geral |
| [[high_noon\|High Noon]] | Raro | Espingarda Melee | Drop geral |
| [[slicing_feathers\|Slicing Feathers]] | Raro | Leques (Warfan) | Drop geral |

---

## Archwing

Mods de Archwing têm pool **completamente separado** — não se aplicam a armas terrestres e vice-versa.

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[dual_rounds\|Dual Rounds]] | Incomum | +Multishot — Arch-Gun | Drop Archwing |
| [[automatic_trigger\|Automatic Trigger]] | Incomum | +Fire Rate — Arch-Gun | Drop Archwing |
| [[charged_bullets\|Charged Bullets]] | Incomum | +Dano base — Arch-Gun | Drop Archwing |
| [[explosive_payload\|Explosive Payload]] | Incomum | +Status Chance — Arch-Gun | Drop Archwing |
| [[hollowed_bullets\|Hollowed Bullets]] | Raro | +Crit Chance — Arch-Gun | Drop Archwing |
| [[polar_coil\|Polar Coil]] | Incomum | +Frio — Arch-Gun | Drop Archwing |
| [[orokin_reach\|Orokin Reach]] | Incomum | +Alcance — Arch-Melee | Drop Archwing |
| [[elec_drain\|Elec Drain]] | Incomum | +Elétrico — Arch-Melee | Drop Archwing |
| [[astral_slash\|Astral Slash]] | Incomum | +Slash — Arch-Melee | Drop Archwing |

---

## Referências Cruzadas

| Índice | Relação |
|---|---|
| [[_Mods _Indice\|Mods]] | Índice geral — sistema de mods |
| [[_Mods Especiais _Indice\|Mods Especiais]] | Primed, Corrupted e Syndicate de armas |
| [[_Armas _Indice\|Armas]] | Armas que equipam estes mods |
| [[_Armas _Brancas _Indice\|Brancas]] | Stances por tipo de arma branca |
| [[_Armas _Archwing _Indice\|Archwing]] | Armas archwing e seu pool de mods |

----------------------------------------


## Seção: mods\warframe
### 📄 arquivo: _Mods Warframe _Indice.md

# Mods de Warframe — Índice

> [!quote]
> *"Quatro pilares sustentam qualquer build: Força, Duração, Alcance e Eficiência."*

---

## Visão Geral

Mods de Warframe modificam as **habilidades e atributos base** do frame. Cada frame tem 8 slots normais + 1 slot de Aura + 1 slot Exilus. A Aura adiciona capacidade à capacidade total do frame.

**Slots:** 8 normais + 1 Aura + 1 Exilus (requer Warframe Exilus Adapter)
**Capacidade base:** 30 (rank 30) → 60 com Orokin Reactor

---

## Os 4 Pilares de Build

As habilidades de todo Warframe são afetadas por quatro stats, cada um controlado por uma família de mods:

| Pilar | Stat | O que afeta | Mods base → Corrupted |
|---|---|---|---|
| **Strength** | Poder das habilidades | Dano, escudo, cura e qualquer valor numérico das skills | Intensify → Blind Rage, Transient Fortitude |
| **Duration** | Duração das habilidades | Quanto tempo habilidades persistem | Continuity → Narrow Minded |
| **Range** | Alcance das habilidades | Raio e distância de efeito | Stretch → Overextended |
| **Efficiency** | Custo de energia | Quanto menos energia as habilidades consomem | Streamline → Fleeting Expertise |

> [!note] Mods Corrupted e trade-offs
> Mods Corrupted (Orokin Vault) empurram um pilar ao limite com penalidade em outro. Ex: Blind Rage dá +Strength enorme mas drena -Efficiency. A arte do build é balancear esses trade-offs.

---

## Defesa e Sobrevivência

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[vitality\|Vitality]] | Comum | +HP | Drop geral |
| [[redirection\|Redirection]] | Comum | +Shield | Drop geral |
| [[steel_fiber\|Steel Fiber]] | Incomum | +Armor | Drop geral |
| [[primed_vigor\|Primed Vigor]] | Primed | +HP e +Shield combinados | Baro Ki'Teer |
| [[umbral_vitality\|Umbral Vitality]] | Umbral | +HP muito elevado — set Umbral | Quest (The Sacrifice) |
| [[adaptation\|Adaptation]] | Raro | Resistência ao tipo de dano recebido (acumula até 90%) | Arbitrations |
| [[quick_thinking\|Quick Thinking]] | Raro | Usa Energia como buffer quando HP chega a zero | Drop geral |
| [[rolling_guard\|Rolling Guard]] | Raro | Invencibilidade breve + remove status no dodge | Arbitrations |
| [[grace\|Grace]] | Raro | Regenera HP ao sair de estado crítico | Drop geral |
| [[augur_accord\|Augur Accord]] | Incomum | Gasto de Energia restaura Shields | Syndicatos |

---

## Habilidades

### Strength

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[intensify\|Intensify]] | Incomum | +Strength | Drop geral |
| [[umbral_intensify\|Umbral Intensify]] | Umbral | +Strength muito elevado — set Umbral | Quest (The Sacrifice) |
| [[transient_fortitude\|Transient Fortitude]] | Corrupted | +Strength alto / -Duration | Orokin Vault |
| [[blind_rage\|Blind Rage]] | Corrupted | +Strength muito alto / -Efficiency | Orokin Vault |
| [[energy_conversion\|Energy Conversion]] | Raro | +Strength temporário ao pegar orb de energia | Drop geral |
| [[augur_secrets\|Augur Secrets]] | Incomum | Gasto de Energia +Strength temporário | Syndicatos |
| [[power_drift\|Power Drift]] | Incomum | +Strength menor + knockdown resist | Junction |

### Duration

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[continuity\|Continuity]] | Comum | +Duration | Drop geral |
| [[constitution\|Constitution]] | Incomum | +Duration + -Knockdown Recovery | Drop geral |
| [[primed_continuity\|Primed Continuity]] | Primed | +Duration muito elevado | Baro Ki'Teer |
| [[narrow_minded\|Narrow Minded]] | Corrupted | +Duration muito alto / -Range | Orokin Vault |
| [[augur_message\|Augur Message]] | Incomum | Gasto de Energia +Duration temporário | Syndicatos |

### Range

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[stretch\|Stretch]] | Comum | +Range | Drop geral |
| [[overextended\|Overextended]] | Corrupted | +Range muito alto / -Strength | Orokin Vault |
| [[cunning_drift\|Cunning Drift]] | Incomum | +Range menor — slot Exilus | Drop geral |

### Efficiency

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[streamline\|Streamline]] | Incomum | -Custo de Energia | Drop geral |
| [[fleeting_expertise\|Fleeting Expertise]] | Corrupted | +Efficiency muito alto / -Duration | Orokin Vault |

### Energia

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[flow\|Flow]] | Incomum | +Max Energia | Drop geral |
| [[primed_flow\|Primed Flow]] | Primed | +Max Energia muito elevado | Baro Ki'Teer |
| [[rage\|Rage]] | Raro | Dano em HP → Energia | Drop de Boss |
| [[hunter_adrenaline\|Hunter Adrenaline]] | Raro | Dano em HP → Energia (mais eficiente) | Syndicato (Steel Meridian) |

### Velocidade e Utilidade

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[natural_talent\|Natural Talent]] | Raro | -Cast Time de habilidades | Drop geral |

---

## Mods Umbral

O **Set Umbral** consiste em três mods que se combinam para bônus extras quando dois ou mais estão equipados:

| Mod | Efeito Base | Bônus de Set |
|---|---|---|
| [[umbral_vitality\|Umbral Vitality]] | +HP | +HP e +Umbral Damage (2 mods) |
| [[umbral_intensify\|Umbral Intensify]] | +Strength | +Strength e +Umbral Damage (2 mods) |
| [[umbral_fiber\|Umbral Fiber]] | +Armor | +Armor e +Umbral Damage (2 mods) |

> [!note] Custo de Capacidade
> Mods Umbral têm custo de capacidade muito alto. Equipar o set completo exige frame com Orokin Reactor e várias Formas instaladas — na prática, reservados para frames com polaridade Umbra (ω) pré-instalada, como Excalibur Umbra.

---

## Augments de Frame

Augments são mods **exclusivos por habilidade de frame específico** que modificam o comportamento de uma habilidade (ex: Seeking Shuriken modifica Ash, Roar de Rhino modifica outros frames via Helminth). Obtidos em:

- Sindicatos (maioria)
- Nightwave (rotação)
- Cephalon Simaris (alguns)

> [!important]
> Augments não aparecem neste índice individualmente — cada frame tem até 4 augments (um por habilidade). Consulte o arquivo individual do frame para os augments específicos.

---

## Aura

Mods de Aura têm **polaridade Penjaga (=)** e ficam em slot exclusivo. O valor do mod é somado à capacidade total do frame — uma Aura de +18 aumenta a capacidade total de 30 para 48 (sem Reactor).

| Mod | Raridade | Efeito | Sinergias |
|---|---|---|---|
| [[corrosive_projection\|Corrosive Projection]] | Incomum | -Armor dos inimigos | Meta contra Grineer (stack de 4 na squad) |
| [[steel_charge\|Steel Charge]] | Comum | +Dano de arma branca | Builds de melee |
| [[energy_siphon\|Energy Siphon]] | Incomum | Regeneração passiva de Energia (squad) | Frames com altas demandas de energia |
| [[growing_power\|Growing Power]] | Incomum | +Strength ao aplicar Status | Syndicate (Cephalon Suda / New Loka) |
| [[dead_eye\|Dead Eye]] | Incomum | +Dano de armas sniper | Builds sniper |
| [[rifle_amp\|Rifle Amp]] | Comum | +Dano de rifles | Builds DPS |
| [[pistol_amp\|Pistol Amp]] | Comum | +Dano de pistolas | Builds pistola |
| [[rejuvenation\|Rejuvenation]] | Comum | Regeneração passiva de HP (squad) | Frames tanky |
| [[enemy_radar\|Enemy Radar]] | Comum | Mostra inimigos no minimapa | QoL / stealth |
| [[loot_detector\|Loot Detector]] | Incomum | Mostra recursos e drops no minimapa | Farm |
| [[brief_respite\|Brief Respite]] | Incomum | Gasto de Energia restaura Shields | Shield-gating builds |
| [[combat_discipline\|Combat Discipline]] | Raro | Kills de aliados +HP; mortes -HP | Builds específicas (suporte) |
| [[empowered_blades\|Empowered Blades]] | Incomum | Status em branca aumentam dano | Syndicate (Steel Meridian) |
| [[physique\|Physique]] | Comum | +HP da squad | Suporte |

---

## Exilus (Warframe)

Slot Exilus de Warframe só aceita mods de **mobilidade e utilidade**. Requer **Warframe Exilus Adapter** para desbloquear.

| Mod | Raridade | Efeito |
|---|---|---|
| [[rush\|Rush]] | Comum | +Velocidade de corrida |
| [[sprint_boost\|Sprint Boost]] | Comum | +Velocidade de sprint |
| [[handspring\|Handspring]] | Comum | -Tempo de recuperação de knockdown |
| [[mobilize\|Mobilize]] | Incomum | +Velocidade de parkour |
| [[aviator\|Aviator]] | Incomum | -Dano recebido enquanto em ar |
| [[cunning_drift\|Cunning Drift]] | Incomum | +Range de habilidades (menor que Stretch) |
| [[power_drift\|Power Drift]] | Incomum | +Strength menor + knockdown resist |
| [[coaction_drift\|Coaction Drift]] | Incomum | Amplifica efeito de Auras na squad |
| [[vigilante_pursuit\|Vigilante Pursuit]] | Incomum | Radar de inimigos |

---

## Referências Cruzadas

| Índice | Relação |
|---|---|
| [[_Mods _Indice\|Mods]] | Índice geral — sistema de mods |
| [[_Mods Especiais _Indice\|Mods Especiais]] | Mods Corrupted, Primed, Umbral e Syndicate de warframe |
| [[_Warframes _Indice\|Warframes]] | Frames que equipam estes mods |
| [[_Sindicatos _Indice\|Sindicatos]] | Fonte de mods Syndicate e alguns Augments |

----------------------------------------


## Seção: mods\companheiros
### 📄 arquivo: _Mods Companheiros _Indice.md

# Mods de Companheiros — Índice

> [!quote]
> *"Um companheiro bem modado vale mais que um segundo warframe."*

---

## Visão Geral

Mods de companheiros modificam os **atributos e comportamentos** de Sentinels, Kavats, Kubrows, MOAs e Hounds. Cada tipo de companheiro tem um conjunto de mods exclusivos chamados **Precept Mods** que controlam suas ações autônomas em combate.

**Slots:** 8 slots normais (companheiro) + 10 slots de arma do companheiro
**Capacidade base:** 30 → 60 com Orokin Reactor (companheiro) ou Orokin Catalyst (arma do companheiro)

---

## Precept Mods

Precept mods são **instruções comportamentais** — definem o que o companheiro faz autonomamente. Estão ligados a um tipo específico de companheiro e ocupam slots normais.

| Tipo de Precept | Exemplos | Efeito |
|---|---|---|
| **Comportamento ativo** | Assault Mode, Striker | Companheiro ataca inimigos próximos |
| **Comportamento defensivo** | Guardian, Regen | Companheiro protege ou ressuscita o operador |
| **Comportamento de suporte** | Medi-Ray, Pack Leader | Companheiro cura o operador ou a si mesmo |
| **Comportamento de loot** | Vacuum, Fetch | Companheiro atrai itens automaticamente |

> [!tip] Vacuum / Fetch são obrigatórios
> **Vacuum** (Sentinels) e **Fetch** (outros companheiros) atraem itens próximos automaticamente. São os mods de maior impacto de QoL no jogo — considerados quase obrigatórios em qualquer build.

---

## Mods Universais (qualquer companheiro)

| Mod | Raridade | Efeito | Fonte |
|---|---|---|---|
| [[link_health\|Link Health]] | Incomum | HP do companheiro escala com HP do operador | Drop geral |
| [[link_shields\|Link Shields]] | Incomum | Shield do companheiro escala com Shield do operador | Drop geral |
| [[link_armor\|Link Armor]] | Incomum | Armor do companheiro escala com Armor do operador | Drop geral |
| [[animal_instinct\|Animal Instinct]] | Incomum | Radar de inimigos e loot no minimapa | Drop geral |
| [[primed_animal_instinct\|Primed Animal Instinct]] | Primed | Radar — raio muito maior | Baro Ki'Teer |

---

## Sentinels

| Mod | Raridade | Tipo | Efeito | Fonte |
|---|---|---|---|---|
| [[vacuum\|Vacuum]] | Incomum | Precept | Atrai itens próximos automaticamente | Drop geral / mercado |
| [[primed_regen\|Primed Regen]] | Primed | Precept | Múltiplas ressurreições por missão | Baro Ki'Teer |
| [[regen\|Regen]] | Raro | Precept | Ressurreição do Sentinel uma vez por missão | Drop geral |
| [[guardian\|Guardian]] | Raro | Precept | Regenera Shields do operador quando ativado | Drop geral |
| [[medi_ray\|Medi-Ray]] | Incomum | Precept | Cura o operador periodicamente | Drop geral |
| [[striker\|Striker]] | Incomum | Precept | Sentinel ataca inimigos próximos | Drop geral |
| [[assault_mode\|Assault Mode]] | Incomum | Precept | Persegue e ataca alvos ativamente | Drop geral |
| [[sweeper\|Sweeper]] | Incomum | Arma | Shotgun equipada no Sentinel | Drop geral |
| [[calculated_shot\|Calculated Shot]] | Raro | Arma | +Crítico da arma do Sentinel | Drop geral |
| [[spare_parts\|Spare Parts]] | Raro | Loot | Drop de recurso raro ao Sentinel morrer | Drop geral |
| [[synth_deconstruct\|Synth Deconstruct]] | Incomum | Loot | Drop de orb de saúde ao matar — set Synth | Drop geral |
| [[synth_fiber\|Synth Fiber]] | Incomum | Defesa | Overshields ao pegar orb de saúde — set Synth | Drop geral |
| [[enemy_sense\|Enemy Sense]] | Incomum | Utilidade | Radar de inimigos | Drop geral |

> [!note] Sentinels populares
> **Carrier** com Vacuum + Primed Regen é o setup mais comum. **Helios** escaneia inimigos para o Codex automaticamente. **Wyrm** usa Crowd Dispersion para knockback.

---

## Kavats

| Mod | Raridade | Tipo | Efeito | Fonte |
|---|---|---|---|---|
| [[fetch\|Fetch]] | Incomum | Precept | Atrai itens — equivalente ao Vacuum | Drop geral |
| [[charm\|Charm]] | Raro | Precept | **Smeeta Kavat** — buff aleatório incluindo duplicação de recursos | Drop geral |
| [[mischief\|Mischief]] | Incomum | Precept | Smeeta — distrai inimigos | Drop geral |
| [[tek_enhance\|Tek Enhance]] | Incomum | Precept | Smeeta — aumenta duração dos buffs de Charm | Drop geral |
| [[sharpened_claws\|Sharpened Claws]] | Raro | Precept | **Adarza Kavat** — remove armor ao atacar inimigos | Drop geral |
| [[reflect\|Reflect]] | Raro | Precept | Adarza — reflete dano recebido | Drop geral |
| [[cat_s_eye\|Cat's Eye]] | Raro | Precept | Adarza — +Crit Chance para o operador por buffs | Drop geral |
| [[bite\|Bite]] | Raro | Combate | +Crítico do Kavat | Drop geral |
| [[pack_leader\|Pack Leader]] | Incomum | Cura | Finishers do operador curam o companheiro | Drop geral |

> [!tip] Smeeta para Farm
> O buff **Charm** da Smeeta Kavat pode duplicar drops de recursos, orbs de energia e até relíquias abertas. É o companheiro mais usado em sessões de farm intensivo.

---

## Kubrows

| Mod | Raridade | Tipo | Efeito | Fonte |
|---|---|---|---|---|
| [[fetch\|Fetch]] | Incomum | Precept | Atrai itens — equivalente ao Vacuum | Drop geral |
| [[maul\|Maul]] | Incomum | Precept | **Raksa Kubrow** — +Dano do Kubrow | Drop geral |
| [[protect\|Protect]] | Raro | Precept | Raksa — regenera Shields ao sofrer dano | Drop geral |
| [[howl\|Howl]] | Incomum | Precept | Raksa — amedronta inimigos próximos | Drop geral |
| [[dig\|Dig]] | Raro | Precept | **Sahasa Kubrow** — escava itens e recursos | Drop geral |
| [[loyal_companion\|Loyal Companion]] | Raro | Precept | Kubrow revive o operador uma vez por missão | Drop geral |
| [[hunt\|Hunt]] | Incomum | Precept | **Sunika Kubrow** — persegue inimigos em fuga | Drop geral |
| [[bite\|Bite]] | Raro | Combate | +Crítico do Kubrow | Drop geral |
| [[pack_leader\|Pack Leader]] | Incomum | Cura | Finishers do operador curam o companheiro | Drop geral |

---

## MOAs

| Mod | Raridade | Tipo | Efeito | Fonte |
|---|---|---|---|---|
| [[fetch\|Fetch]] | Incomum | Precept | Atrai itens — equivalente ao Vacuum | Drop geral |
| [[security_override\|Security Override]] | Incomum | Precept | Hackeia consoles e câmeras automaticamente | Drop Fortuna |
| [[thumper\|Thumper]] | Incomum | Precept | Derruba inimigos no chão | Drop Fortuna |
| [[targeting_receptor\|Targeting Receptor]] | Incomum | Precept | +Dano em alvos marcados | Drop Fortuna |
| [[anti_grav_array\|Anti-Grav Array]] | Incomum | Precept | Suspende inimigos no ar | Drop Fortuna |
| [[shockwave_actuator\|Shockwave Actuator]] | Incomum | Precept | Onda de choque radial ao aterrissar | Drop Fortuna |

> [!note] MOAs modulares
> MOAs são montados em Fortuna com componentes (Brace, Gyro, Loader, Weapon) — o conjunto de precepts disponíveis depende do Gyro selecionado.

---

## Hounds

| Mod | Raridade | Tipo | Efeito | Fonte |
|---|---|---|---|---|
| [[fetch\|Fetch]] | Incomum | Precept | Atrai itens — equivalente ao Vacuum | Drop geral |
| [[hound_bite\|Hound Bite]] | Incomum | Precept | Aplica status ao morder | Drop Parvos |
| [[coda_defiance\|Coda Defiance]] | Incomum | Precept | Resistência a efeitos de status | Drop Parvos |
| [[tenacious_bond\|Tenacious Bond]] | Raro | Precept | +Crit Chance das armas ao companheiro estar cheio de HP | Drop Parvos |

> [!note] Hounds modulares
> Hounds são obtidos como subproduto do sistema de Irmãs de Parvos — cada Hound tem precepts determinados pela Irmã que o acompanhava.

---

## Referências Cruzadas

| Índice | Relação |
|---|---|
| [[_Mods _Indice\|Mods]] | Índice geral — sistema de mods |
| [[_Companheiros _Indice\|Companheiros]] | Tipos de companheiros que equipam estes mods |
| [[_Locais _Indice\|Locais]] | Fortuna (MOAs, Hounds), Cetus (Kavats, Kubrows) |

----------------------------------------


## Seção: mods\especiais
### 📄 arquivo: _Mods Especiais _Indice.md

# Mods Especiais — Índice

> [!quote]
> *"Primed para os veteranos. Corrupted para os ousados. Rivens para os obcecados."*

---

## Visão Geral

Mods Especiais são categorias de mods com **origens e mecânicas distintas** das variantes comuns. Representam o topo da progressão de build — mais poderosos, mais raros e mais custosos em capacidade.

| Categoria | Origem | Característica |
|---|---|---|
| **Primed** | Baro Ki'Teer / Nightwave | Versões superiores de mods comuns — mesmo efeito, mais pontos |
| **Umbral** | Quest (The Sacrifice) | Set exclusivo com bônus sinérgico — custo de capacidade muito alto |
| **Corrupted** | Orokin Vault (Derelict) | Dois efeitos opostos — poder alto com penalidade |
| **Syndicate** | Seis Sindicatos | Efeito especial adicional — proc único ao matar |
| **Amalgam** | Drop de inimigos Amalgam | Set mods com bônus exclusivo de mecânica de jogo |
| **Riven** | Sorties / Nightwave | Atributos aleatórios por arma específica |

---

## Mods Primed

Versões amplificadas de mods comuns obtidas **exclusivamente de Baro Ki'Teer** (por Ducats + Créditos) em rotação quinzenal, ou de temporadas da **Nightwave**.

> [!important] Rastreie visitas do Baro
> Cada visita de Baro traz um inventário diferente. Mods Primed não voltam necessariamente na próxima visita. Veteranos monitoram o histórico de visitas para saber quando determinado Primed vai reaparecer.

### Primed de Warframe

| Mod | Equivalente Comum | Melhoria | Fonte |
|---|---|---|---|
| [[primed_vigor\|Primed Vigor]] | Vigor | +HP e +Shield muito elevados | Baro Ki'Teer |
| [[primed_continuity\|Primed Continuity]] | Continuity | +Duration muito elevado | Baro Ki'Teer |
| [[primed_flow\|Primed Flow]] | Flow | +Max Energia muito elevado | Baro Ki'Teer |

### Primed de Armas (Primárias)

| Mod | Equivalente Comum | Melhoria | Fonte |
|---|---|---|---|
| [[primed_serration\|Primed Serration]] | Serration | +Dano base muito elevado — rifle | Baro Ki'Teer |
| [[primed_cryo_rounds\|Primed Cryo Rounds]] | Cryo Rounds | +Frio muito elevado — rifle | Baro Ki'Teer |

### Primed de Armas (Secundárias)

| Mod | Equivalente Comum | Melhoria | Fonte |
|---|---|---|---|
| [[primed_pistol_gambit\|Primed Pistol Gambit]] | Pistol Gambit | +Crit Chance muito elevado — pistola | Baro Ki'Teer |
| [[primed_target_cracker\|Primed Target Cracker]] | Target Cracker | +Crit Multiplier muito elevado — pistola | Baro Ki'Teer |

### Primed de Armas (Brancas)

| Mod | Equivalente Comum | Melhoria | Fonte |
|---|---|---|---|
| [[primed_pressure_point\|Primed Pressure Point]] | Pressure Point | +Dano base muito elevado — branca | Baro Ki'Teer |
| [[primed_fever_strike\|Primed Fever Strike]] | Fever Strike | +Tóxico muito elevado — branca | Baro Ki'Teer |

### Primed de Companheiros

| Mod | Equivalente Comum | Melhoria | Fonte |
|---|---|---|---|
| [[primed_animal_instinct\|Primed Animal Instinct]] | Animal Instinct | Radar de raio muito maior | Baro Ki'Teer |
| [[primed_regen\|Primed Regen]] | Regen | Múltiplas ressurreições por missão | Baro Ki'Teer |

---

## Mods Umbral

Set de três mods obtidos em **The Sacrifice** (quest) e em raids. Têm custo de capacidade muito alto mas se potencializam mutuamente quando dois ou mais estão equipados.

| Mod | Efeito | Bônus de Set (2+ mods) |
|---|---|---|
| [[umbral_vitality\|Umbral Vitality]] | +HP elevado | +HP e +Umbral Damage |
| [[umbral_intensify\|Umbral Intensify]] | +Strength elevado | +Strength e +Umbral Damage |
| [[umbral_fiber\|Umbral Fiber]] | +Armor elevado | +Armor e +Umbral Damage |

> [!note] Slot Umbra (Ω)
> Frames com polaridade Umbra pré-instalada (ex: Excalibur Umbra) reduzem o custo dos mods Umbral pela metade. Outros frames precisam de muitas Formas para viabilizar o set completo.

---

## Mods Corrupted

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
| [[blind_rage\|Blind Rage]] | +Strength muito alto | -Efficiency | Strength |
| [[transient_fortitude\|Transient Fortitude]] | +Strength alto | -Duration | Strength |
| [[fleeting_expertise\|Fleeting Expertise]] | +Efficiency muito alto | -Duration | Efficiency |
| [[narrow_minded\|Narrow Minded]] | +Duration muito alto | -Range | Duration |
| [[overextended\|Overextended]] | +Range muito alto | -Strength | Range |

### Corrupted de Armas

| Mod | Efeito Positivo | Penalidade | Tipo |
|---|---|---|---|
| [[heavy_caliber\|Heavy Caliber]] | +Dano muito alto | -Accuracy | Rifle |
| [[vile_acceleration\|Vile Acceleration]] | +Fire Rate muito alto | -Dano base | Rifle |
| [[vile_precision\|Vile Precision]] | -Recoil muito alto | -Fire Rate | Rifle |
| [[critical_delay\|Critical Delay]] | +Crit Chance alto | -Fire Rate | Rifle |
| [[hollow_point\|Hollow Point]] | +Crit Multiplier | -Dano base | Rifle |
| [[tainted_mag\|Tainted Mag]] | +Magazine Size | -Reload Speed | Rifle |
| [[depleted_reload\|Depleted Reload]] | -Reload Time | -Magazine Size | Rifle |
| [[tainted_shell\|Tainted Shell]] | +Pellet Count | -Fire Rate | Espingarda |
| [[anemic_agility\|Anemic Agility]] | +Fire Rate | -Dano base | Pistola |
| [[spoiled_strike\|Spoiled Strike]] | +Dano muito alto | -Attack Speed | Branca |
| [[corrupt_charge\|Corrupt Charge]] | +Combo inicial alto | -Duração do Counter | Branca |
| [[drifting_contact\|Drifting Contact]] | +Combo Duration | chance de Status | Branca |

---

## Mods Syndicate

Exclusivos dos **seis sindicatos principais**. Adicionam um **proc especial** (explosão, buff, efeito) às ações do equipamento além do bônus normal do mod.

> [!note] Aliados e Inimigos
> Cada sindicato tem aliados e inimigos. Mods de sindicatos aliados também ficam disponíveis para compra, mas a custo maior de reputação.

### Aura de Sindicato

| Mod | Sindicato | Efeito |
|---|---|---|
| [[growing_power\|Growing Power]] | Cephalon Suda / New Loka | +Strength ao aplicar Status — Aura |
| [[empowered_blades\|Empowered Blades]] | Steel Meridian | Status em branca aumentam dano — Aura |
| [[masters_edge\|Master's Edge]] | Arbiters of Hexis | +Efficiency de habilidades — Aura |

### Mods de Armas de Sindicato

| Mod | Sindicato | Tipo | Efeito |
|---|---|---|---|
| [[hunter_munitions\|Hunter Munitions]] | Steel Meridian | Rifle | Críticos aplicam Slash |
| [[hunter_adrenaline\|Hunter Adrenaline]] | Steel Meridian | Warframe | Dano em HP → Energia |
| [[lethal_torrent\|Lethal Torrent]] | Cephalon Suda | Pistola | +Multishot + Fire Rate |
| [[high_voltage\|High Voltage]] | Perrin Sequence | Rifle | +Elétrico + proc Elétrico |
| [[thermite_rounds\|Thermite Rounds]] | Red Veil | Rifle | +Calor + proc Calor |
| [[frostbite\|Frostbite]] | New Loka | Pistola | +Frio + proc Frio |
| [[scorch\|Scorch]] | Red Veil | Pistola | +Calor + proc Calor |
| [[hemorrhage\|Hemorrhage]] | Steel Meridian | Pistola | Procs de Impact → Slash |
| [[smite_infusion\|Smite Infusion]] | New Loka | Branca | +Radiação + explosão ao matar |
| [[firewalk\|Firewalk]] | Red Veil | Branca | Kills criam rastro de fogo |
| [[winds_of_purity\|Winds of Purity]] | Arbiters of Hexis | Branca | Kills de finisher → Energia e HP |
| [[entropy_burst\|Entropy Burst]] | Cephalon Suda | Branca | Kills disparam explosão de Radiação |
| [[justice_blades\|Justice Blades]] | Arbiters of Hexis | Branca | Kills têm chance de explosão |

---

## Mods Amalgam

Obtidos de **inimigos Amalgam** (Jupiter — Ropalolyst, Disruption) e de missões especiais. São **Set Mods** — bônus extras ao equipar dois ou mais da mesma série.

| Mod | Efeito | Bônus de Set |
|---|---|---|
| [[amalgam_serration\|Amalgam Serration]] | +Dano base de rifle (menor que Serration normal) | +Velocidade de Sprint | Junction Marte — não negociável |
| [[amalgam_barrel_diffusion\|Amalgam Barrel Diffusion]] | +Multishot de pistola | +Dodge Speed | Drop Amalgam |
| [[amalgam_organ_shatter\|Amalgam Organ Shatter]] | +Crit Multiplier branca | -Charge Attack Time | Drop Amalgam |
| [[amalgam_daikyu_target_acquired\|Amalgam Daikyu Target Acquired]] | Exclusivo Daikyu | Sliding aumenta dano | Drop Amalgam |

---

## Rivens

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

---

## Referências Cruzadas

| Índice | Relação |
|---|---|
| [[_Mods _Indice\|Mods]] | Índice geral — sistema de mods |
| [[_Mods Warframe _Indice\|Mods de Warframe]] | Primed e Corrupted de warframe em contexto de build |
| [[_Mods Armas _Indice\|Mods de Armas]] | Primed e Corrupted de armas em contexto de build |
| [[_Sindicatos _Indice\|Sindicatos]] | Como ganhar reputação para comprar mods Syndicate |
| [[_Mecanicas _Indice\|Mecânicas]] | Sorties — fonte de Rivens |

----------------------------------------


## Seção: recursos
### 📄 arquivo: _Recursos _Indice.md

# Recursos — Índice

> [!quote]
> *"O Sistema Origem é rico em materiais. Saber onde procurar é metade da batalha."*

---

## Visão Geral

Recursos são materiais coletados em missões e usados na **Fundição** para craftar Warframes, armas, componentes e itens de progressão. Cada recurso tem origem específica — planeta, facção ou modo de jogo — e uma raridade que determina com que frequência dropa.

O loop de progressão depende diretamente dos recursos: toda peça craftável exige uma combinação específica, e receitas avançadas frequentemente pedem materiais de várias regiões diferentes. Recursos são coletados automaticamente ao passar sobre eles no mapa. Cada planeta tem um conjunto de recursos nativos com drop mais frequente, mais um pool de raros compartilhados. Alguns recursos especiais só existem em sistemas específicos — Open Worlds, Nightwave, Sorties — e não aparecem em missões convencionais.

---

## Como Farmar

Recursos dropam de inimigos, containers e lockers nos mapas de missão. Missões de **Survival** e **Defense** são as mais eficientes por volume — quanto mais tempo dentro, mais inimigos spawnam e mais material acumula.

| Método | Efeito |
|---|---|
| **[[nekros\|Nekros]] (Desecrate)** | Rola drops adicionais em cadáveres — duplica efetivamente a taxa de drop |
| **[[hydroid\|Hydroid]] (Pilfering Swarm)** | Chance de drop extra em inimigos afetados pelo Tentacle Swarm |
| **[[khora\|Khora]] (Pilfering Strangledome)** | Chance de drop extra em inimigos presos no Strangledome |
| **Resource Booster** | Dobra todos os recursos coletados por 3 ou 7 dias |
| **Resource Drop Chance Booster** | Aumenta a chance de inimigos droparem recursos |
| **Smeeta Kavat (Charm)** | Buff aleatório que pode dobrar recursos coletados temporariamente |

O setup padrão de farm eficiente combina Nekros + Resource Booster + Smeeta Kavat — podendo quadruplicar o volume coletado por corrida.

---

## Categorias de Raridade

| Raridade | Descrição |
|---|---|
| **Comum** | Drop abundante em quase qualquer missão do planeta de origem. Pode exigir grandes quantidades em crafts avançados. |
| **Incomum** | Drop moderado — presente no planeta certo, mas em volume menor. Gargalo em fases intermediárias. |
| **Raro** | Drop escasso. Requer farm dedicado no planeta ou missão certa, frequentemente com Warframe de loot. |
| **Especial** | Não dropa em missões convencionais. Obtido via Nightwave, Sorties, Void Relics ou eventos sazonais. |

---

## Recursos Comuns

| Recurso | Planeta / Origem | Método | Notas |
|---|---|---|---|
| [[raridades/comum/alloy_plate\|Alloy Plate]] | Vênus, Júpiter, Sedna, Ceres, Phobos | Drop geral | Um dos recursos mais abundantes do jogo |
| [[raridades/comum/circuits\|Circuits]] | Vênus, Ceres | Containers e inimigos | — |
| [[raridades/comum/detonite_ampule\|Detonite Ampule]] | Qualquer planeta Grineer | Drop de inimigos | Acumulado para craftar Detonite Injector (pesquisa de Clã) |
| [[raridades/comum/ferrite\|Ferrite]] | Mercúrio, Terra, Netuno, Void | Drop geral | Essencial para builds iniciais |
| [[raridades/comum/fieldron_sample\|Fieldron Sample]] | Qualquer planeta Corpus | Drop de inimigos | Acumulado para craftar Fieldron (pesquisa de Clã) |
| [[raridades/comum/mutagen_sample\|Mutagen Sample]] | Eris, Deimos, Orokin Derelict | Drop Infestado | Acumulado para craftar Mutagen Mass (pesquisa de Clã) |
| [[raridades/comum/nano_spores\|Nano Spores]] | Saturno, Netuno, Eris, Deimos | Drop geral | Acumula rápido em Survival |
| [[raridades/comum/polymer_bundle\|Polymer Bundle]] | Mercúrio, Vênus, Urano | Containers e inimigos | — |
| [[raridades/comum/rubedo\|Rubedo]] | Phobos, Terra, Sedna, Europa, Void | Containers e lockers | — |
| [[raridades/comum/salvage\|Salvage]] | Marte, Júpiter, Sedna | Drop geral | Necessário em grande volume para Vauban e pesquisas de Clã |

---

## Recursos Incomuns

| Recurso | Planeta / Origem | Método | Notas |
|---|---|---|---|
| [[raridades/incomum/hexenon\|Hexenon]] | Júpiter | Inimigos Amalgam e Gas City | Usado para craftar Wisp e componentes de Clã |
| [[raridades/incomum/oxium\|Oxium]] | Júpiter | Drop de Oxium Osprey | Inimigo se autodestrói se não morto rápido — farm exige atenção |
| [[raridades/incomum/plastids\|Plastids]] | Saturno, Urano, Phobos, Plutão, Eris | Drop geral | Essencial para Nidus e frames de temática Infestada |

---

## Recursos Raros

| Recurso | Planeta / Origem | Método | Notas |
|---|---|---|---|
| [[raridades/raro/argon_crystal\|Argon Crystal]] | Void | Drop geral | **Decai em 24h** após encerrar sessão — farmear próximo do uso |
| [[raridades/raro/control_module\|Control Module]] | Europa, Netuno | Bosses e containers | — |
| [[raridades/raro/cryotic\|Cryotic]] | Qualquer planeta | Missões Excavation | Exclusivo de Excavation — 100 por escavador completado |
| [[raridades/raro/gallium\|Gallium]] | Marte, Urano | Bosses e containers | — |
| [[raridades/raro/kuva\|Kuva]] | Fortaleza Kuva | Siphon / Flood | Usada para rolar e melhorar Riven Mods |
| [[raridades/raro/morphics\|Morphics]] | Mercúrio, Marte, Phobos, Europa | Drop de bosses | — |
| [[raridades/raro/neural_sensors\|Neural Sensors]] | Júpiter, Fortaleza Kuva | Drop do boss Alad V | — |
| [[raridades/raro/neurodes\|Neurodes]] | Terra, Eris, Lua, Deimos | Drop de bosses | — |
| [[raridades/raro/nitain_extract\|Nitain Extract]] | Nightwave, Ghoul Purge | Recompensa de temporada | Não dropa em missões normais |
| [[raridades/raro/orokin_cell\|Orokin Cell]] | Saturno, Ceres, Deimos | Drop de bosses | Frequente gargalo em crafts de Warframes Prime |
| [[raridades/raro/tellurium\|Tellurium]] | Urano, missões Archwing | Drop de inimigos | Melhor farmado em Archwing Interception em Urano |

---

## Recursos Especiais

Itens obtidos via sistemas específicos — não dropam em farm convencional. Representam progressão vertical: aumentam poder ou flexibilidade do equipamento sem serem consumidos em receitas de crafting comuns.

| Recurso | Origem | Função |
|---|---|---|
| [[raridades/especial/forma\|Forma]] | Relíquias do Void, Sorties, Nightwave | Reseta rank e adiciona polaridade ao equipamento |
| [[raridades/especial/aura_forma\|Aura Forma]] | Nightwave, Sorties | Permite qualquer polaridade no slot de Aura |
| [[raridades/especial/umbral_forma\|Umbral Forma]] | Nightwave, end-game | Slot Umbral — compatível com mods da série Umbra |
| [[raridades/especial/orokin_catalyst\|Orokin Catalyst]] | Sorties, Alerts, Login Reward | Dobra capacidade de mod de armas ("potato azul") |
| [[raridades/especial/orokin_reactor\|Orokin Reactor]] | Sorties, Alerts, Login Reward | Dobra capacidade de mod de Warframes ("potato dourado") |
| [[raridades/especial/exilus_adapter\|Exilus Adapter]] | Sindicatos, Nightwave, Sorties | Desbloqueia slot Exilus em armas |
| [[raridades/especial/warframe_exilus_adapter\|Warframe Exilus Adapter]] | Sindicatos, Nightwave | Desbloqueia slot Exilus em Warframes |
| [[raridades/especial/endo\|Endo]] | Arbitrations, Ayatan Sculptures, Missões | Moeda para rankear mods |
| [[raridades/especial/ayatan_sculpture\|Ayatan Sculpture]] | Missões aleatórias, Maroo's Bazaar | Convertida em Endo ou usada como decoração |
| [[raridades/especial/ayatan_amber_star\|Ayatan Amber Star]] | Drop aleatório em missões | Inserida em Sculptures para aumentar valor em Endo |
| [[raridades/especial/ayatan_cyan_star\|Ayatan Cyan Star]] | Drop aleatório em missões | Inserida em Sculptures para aumentar valor em Endo |
| [[raridades/especial/void_traces\|Void Traces]] | Missões de Void Fissure | Refina Relíquias do Void — aumenta raridade das recompensas |
| [[raridades/especial/archon_shard_teal\|Archon Shard (Teal)]] | Archon Hunts semanais | Empowerment permanente — atributo de habilidade |
| [[raridades/especial/archon_shard_crimson\|Archon Shard (Crimson)]] | Archon Hunts semanais | Empowerment permanente — atributo de força/vida |
| [[raridades/especial/archon_shard_azure\|Archon Shard (Azure)]] | Archon Hunts semanais | Empowerment permanente — atributo de energia/escudo |
| [[raridades/especial/archon_shard_amber\|Archon Shard (Amber)]] | Archon Hunts semanais | Empowerment permanente — atributo de eficiência/duração |
| [[raridades/especial/archon_shard_topaz\|Archon Shard (Topaz)]] | Archon Hunts semanais | Empowerment permanente — atributo de alcance |
| [[raridades/especial/archon_shard_violet\|Archon Shard (Violet)]] | Archon Hunts semanais | Empowerment permanente — atributo combinado |
| [[raridades/especial/riven_mod\|Riven Mod]] | Sorties, Nightwave | Mod com atributos aleatórios vinculado a uma arma específica |
| [[raridades/especial/orokin_ducats\|Orokin Ducats]] | Troca de peças Prime (quiosque de Baro) | Moeda exclusiva de Baro Ki'Teer — sem outra fonte |
| [[raridades/especial/aya\|Aya]] | Drop aleatório em missões regulares | Usada no sistema Prime Resurgence |
| [[raridades/especial/regal_aya\|Regal Aya]] | Compra com Platinum | Acesso imediato a qualquer item Prime Resurgence |
| [[raridades/especial/cephalon_fragment\|Cephalon Fragment]] | Exploração de planetas | Revela lore ao completar conjuntos por planeta |

---

## Recursos de Open Worlds

Cada Open World tem ecossistema próprio — coletados por coleta manual, mineração, pesca ou drops de inimigos exclusivos. Usados para reputação com sindicatos locais e crafting de equipamentos exclusivos de cada mundo.

---

### Planícies de Eidolon (Terra)
*Sindicato: Ostron (Cetus) · Ferramentas: Nosam Cutter (mineração), Fishing Spear (pesca)*

| Recurso | Raridade | Método | Notas |
|---|---|---|---|
| [[open_worlds/eidolon/iradite\|Iradite]] | Comum | Coleta em campo | Alta concentração à noite |
| [[open_worlds/eidolon/grokdrul\|Grokdrul]] | Comum | Containers Grineer | Espalhados pelo mapa |
| [[open_worlds/eidolon/nistlepod\|Nistlepod]] | Comum | Plantas | Comum em toda a planície |
| [[open_worlds/eidolon/maprico\|Maprico]] | Comum | Plantas | Afloramentos rochosos |
| [[open_worlds/eidolon/coprite\|Coprite]] | Comum | Mineração | Minério básico |
| [[open_worlds/eidolon/fersteel\|Fersteel]] | Comum | Mineração | Minério básico |
| [[open_worlds/eidolon/intact_sentient_core\|Intact Sentient Core]] | Comum | Vomvalysts | Drop básico de Sentient pequeno |
| [[open_worlds/eidolon/murkray_liver\|Murkray Liver]] | Comum | Pesca — Murkray | — |
| [[open_worlds/eidolon/murkray_bladder\|Murkray Bladder]] | Comum | Pesca — Murkray | — |
| [[open_worlds/eidolon/sharrac_tegmen\|Sharrac Tegmen]] | Comum | Pesca — Sharrac | — |
| [[open_worlds/eidolon/yogwun_stomach\|Yogwun Stomach]] | Comum | Pesca — Yogwun | — |
| [[open_worlds/eidolon/karkina_antenna\|Karkina Antenna]] | Comum | Pesca — Karkina | — |
| [[open_worlds/eidolon/tralok_eyes\|Tralok Eyes]] | Comum | Pesca — Tralok | — |
| [[open_worlds/eidolon/ruks_claw\|Ruk's Claw]] | Incomum | Plantas | Encostas e terreno elevado |
| [[open_worlds/eidolon/lunar_pitcher\|Lunar Pitcher]] | Incomum | Plantas | Perto de ruínas |
| [[open_worlds/eidolon/azurite\|Azurite]] | Incomum | Mineração | — |
| [[open_worlds/eidolon/ferros\|Ferros]] | Incomum | Mineração | — |
| [[open_worlds/eidolon/pyrol\|Pyrol]] | Incomum | Mineração | — |
| [[open_worlds/eidolon/exceptional_sentient_core\|Exceptional Sentient Core]] | Incomum | Vomvalysts | Versão superior do Core |
| [[open_worlds/eidolon/cuthol_tendon\|Cuthol Tendon]] | Incomum | Pesca — Cuthol | — |
| [[open_worlds/eidolon/norg_brain\|Norg Brain]] | Incomum | Pesca — Norg | — |
| [[open_worlds/eidolon/cetus_wisp\|Cetus Wisp]] | Raro | Coleta em campo | Flutua perto da água — exclusivamente à noite |
| [[open_worlds/eidolon/auron\|Auron]] | Raro | Mineração | — |
| [[open_worlds/eidolon/devar\|Devar]] | Raro | Mineração | — |
| [[open_worlds/eidolon/flawless_sentient_core\|Flawless Sentient Core]] | Raro | Vomvalysts | — |
| [[open_worlds/eidolon/radiant_sentient_core\|Radiant Sentient Core]] | Raro | Vomvalysts | Versão mais rara |
| [[open_worlds/eidolon/eidolon_shard\|Eidolon Shard]] | Raro | Teralyst | Progressão do Operator |
| [[open_worlds/eidolon/brilliant_eidolon_shard\|Brilliant Eidolon Shard]] | Raro | Gantulyst | Versão superior |
| [[open_worlds/eidolon/radiant_eidolon_shard\|Radiant Eidolon Shard]] | Raro | Hydrolyst | Versão mais poderosa |
| [[open_worlds/eidolon/breath_of_the_eidolon\|Breath of the Eidolon]] | Raro | Todos os Eidolons | Crafting avançado |
| [[open_worlds/eidolon/mawfish_bones\|Mawfish Bones]] | Raro | Pesca — Mawfish | Peixe raro |
| [[open_worlds/eidolon/glappid_scale\|Glappid Scale]] | Raro | Pesca — Glappid | Peixe de isca especial |

---

### Orbe Vallis (Vênus)
*Sindicato: Solaris United (Fortuna) · Ferramentas: Mining Laser (mineração), Fishing Spear (pesca)*

| Recurso | Raridade | Método | Notas |
|---|---|---|---|
| [[open_worlds/orbe_vallis/venerdo\|Venerdo]] | Comum | Coleta em campo | Espalhado pela Vallis |
| [[open_worlds/orbe_vallis/gorgaricus_spore\|Gorgaricus Spore]] | Comum | Coleta em campo | Fungos específicos |
| [[open_worlds/orbe_vallis/aucrumite\|Aucrumite]] | Comum | Mineração | Minério básico |
| [[open_worlds/orbe_vallis/coprun\|Coprun]] | Comum | Mineração | Minério básico |
| [[open_worlds/orbe_vallis/training_debt_bond\|Training Debt-Bond]] | Comum | Bounties (Fortuna) | Nível mais baixo de Debt-Bond |
| [[open_worlds/orbe_vallis/tromyzon_fragment\|Tromyzon Fragment]] | Comum | Pesca — Tromyzon | Servofish comum |
| [[open_worlds/orbe_vallis/charamote_shard\|Charamote Shard]] | Comum | Pesca — Charamote | Servofish comum |
| [[open_worlds/orbe_vallis/thermal_sludge\|Thermal Sludge]] | Incomum | Containers Corpus | — |
| [[open_worlds/orbe_vallis/hespazym_alloy\|Hespazym Alloy]] | Incomum | Mineração | — |
| [[open_worlds/orbe_vallis/nyth\|Nyth]] | Incomum | Mineração | — |
| [[open_worlds/orbe_vallis/sentirum\|Sentirum]] | Incomum | Mineração | — |
| [[open_worlds/orbe_vallis/gyromag_systems\|Gyromag Systems]] | Incomum | Coolant Raknoids | Drop de Raknoid menor |
| [[open_worlds/orbe_vallis/shelter_debt_bond\|Shelter Debt-Bond]] | Incomum | Bounties (Fortuna) | — |
| [[open_worlds/orbe_vallis/medical_debt_bond\|Medical Debt-Bond]] | Incomum | Bounties (Fortuna) | — |
| [[open_worlds/orbe_vallis/synathid_casing\|Synathid Casing]] | Incomum | Pesca — Synathid | — |
| [[open_worlds/orbe_vallis/scrubber_exa_brain\|Scrubber Exa Brain]] | Incomum | Pesca — Scrubber Exa | — |
| [[open_worlds/orbe_vallis/echowinder_shell\|Echowinder Shell]] | Incomum | Pesca — Echowinder | — |
| [[open_worlds/orbe_vallis/amarast\|Amarast]] | Raro | Mineração | — |
| [[open_worlds/orbe_vallis/marquise_thyst\|Marquise Thyst]] | Raro | Mineração | — |
| [[open_worlds/orbe_vallis/calda_toroid\|Calda Toroid]] | Raro | Inimigos — Enrichment Labs | Alta demanda para builds de Mech |
| [[open_worlds/orbe_vallis/crisma_toroid\|Crisma Toroid]] | Raro | Inimigos — Temple of Profit | Alta demanda para builds de Mech |
| [[open_worlds/orbe_vallis/sola_toroid\|Sola Toroid]] | Raro | Inimigos — Spaceport | Alta demanda para builds de Mech |
| [[open_worlds/orbe_vallis/vega_toroid\|Vega Toroid]] | Raro | Thermia Fractures | Alta demanda para builds de Mech |
| [[open_worlds/orbe_vallis/atmo_systems\|Atmo Systems]] | Raro | Exploiter Orb | — |
| [[open_worlds/orbe_vallis/repeller_systems\|Repeller Systems]] | Raro | Exploiter Orb | Recompensa principal do Exploiter |
| [[open_worlds/orbe_vallis/advances_debt_bond\|Advances Debt-Bond]] | Raro | Bounties (Fortuna) | — |
| [[open_worlds/orbe_vallis/familial_debt_bond\|Familial Debt-Bond]] | Raro | Bounties (Fortuna) | Nível mais raro de Debt-Bond |
| [[open_worlds/orbe_vallis/recaster_mucus\|Recaster Mucus]] | Raro | Pesca — Recaster | — |
| [[open_worlds/orbe_vallis/sapcaddy_bladder\|Sapcaddy Bladder]] | Raro | Pesca — Sapcaddy | — |

---

### Câmbion Drift (Deimos)
*Sindicato: Entrati (Necralisk) · Ferramentas: Sunpoint Plasma Drill (mineração), Fishing Spear Infested (pesca)*

| Recurso | Raridade | Método | Notas |
|---|---|---|---|
| [[open_worlds/cambion_drift/mytocardin\|Mytocardin]] | Comum | Coleta em campo | Plantas Infestadas |
| [[open_worlds/cambion_drift/embolos_spore\|Embolos Spore]] | Comum | Coleta em campo | Formações Infestadas |
| [[open_worlds/cambion_drift/sporulate_sac\|Sporulate Sac]] | Comum | Inimigos Infestados | Drop geral |
| [[open_worlds/cambion_drift/thaumica\|Thaumica]] | Comum | Mineração | Minério básico |
| [[open_worlds/cambion_drift/ganglion\|Ganglion]] | Comum | Carnis / Carnis Rex | — |
| [[open_worlds/cambion_drift/bile\|Bile]] | Comum | Jugulus e Infestados | — |
| [[open_worlds/cambion_drift/vitreospina_fillet\|Vitreospina Fillet]] | Comum | Pesca — Vitreospina | — |
| [[open_worlds/cambion_drift/glutinox_fillet\|Glutinox Fillet]] | Comum | Pesca — Glutinox | — |
| [[open_worlds/cambion_drift/longwinder_fillet\|Longwinder Fillet]] | Comum | Pesca — Longwinder | — |
| [[open_worlds/cambion_drift/infested_nacelle\|Infested Nacelle]] | Incomum | Containers / Inimigos | — |
| [[open_worlds/cambion_drift/pustulite\|Pustulite]] | Incomum | Containers / Inimigos | — |
| [[open_worlds/cambion_drift/lucent_terrogel\|Lucent Terrogel]] | Incomum | Mineração | — |
| [[open_worlds/cambion_drift/pheromones\|Pheromones]] | Incomum | Resíduos de Fass / Vome | Poças no campo — ciclo dia/noite |
| [[open_worlds/cambion_drift/cabochon_embolos\|Cabochon Embolos]] | Incomum | Jugulus | — |
| [[open_worlds/cambion_drift/bracoid\|Bracoid]] | Incomum | Carnis | — |
| [[open_worlds/cambion_drift/duroid_fillet\|Duroid Fillet]] | Incomum | Pesca — Duroid | — |
| [[open_worlds/cambion_drift/flagellocanth_fillet\|Flagellocanth Fillet]] | Incomum | Pesca — Flagellocanth | — |
| [[open_worlds/cambion_drift/trabeculum\|Trabeculum]] | Raro | Mineração | — |
| [[open_worlds/cambion_drift/pustulant_cerebrum\|Pustulant Cerebrum]] | Raro | Jugulus Rex | — |
| [[open_worlds/cambion_drift/namalon\|Namalon]] | Raro | Necramechs / Iso Vault | Essencial para crafting de Necramech |
| [[open_worlds/cambion_drift/lobotriscid_fillet\|Lobotriscid Fillet]] | Raro | Pesca — Lobotriscid | — |
| [[open_worlds/cambion_drift/chondricord_fillet\|Chondricord Fillet]] | Raro | Pesca — Chondricord | — |
| [[open_worlds/cambion_drift/cryptosuctus_fillet\|Cryptosuctus Fillet]] | Raro | Pesca — Cryptosuctus | Peixe raro |

---

### Duviri
*Sindicato: Kaithe (Drifter's Camp)*

| Recurso | Raridade | Método | Notas |
|---|---|---|---|
| [[open_worlds/duviri/pathos_clamp\|Pathos Clamp]] | Comum | Missões, exploração, bosses | Principal recurso do Duviri — crafta frames e armas exclusivos |
| [[open_worlds/duviri/cavaleros_burden\|Cavalero's Burden]] | Raro | Drop de bosses do circuito | Usado em trocas com Cavalero |
| [[open_worlds/duviri/kullervo_bane\|Kullervo's Bane]] | Raro | Boss Kullervo | Drop específico do encontro |

---

### Zariman Ten Zero
*Sindicato: The Holdfasts (Chrysalith) · Ferramentas: Fishing Spear Void (pesca)*

| Recurso | Raridade | Método | Notas |
|---|---|---|---|
| [[open_worlds/zariman/voidplume_pinion\|Voidplume Pinion]] | Comum | Coleta em campo | — |
| [[open_worlds/zariman/voidplume_quill\|Voidplume Quill]] | Comum | Coleta em campo | — |
| [[open_worlds/zariman/chondricord_fillet\|Chondricord Fillet]] | Comum | Pesca — Chondricord | — |
| [[open_worlds/zariman/glutinox_fillet\|Glutinox Fillet]] | Comum | Pesca — Glutinox | — |
| [[open_worlds/zariman/voidplume_crest\|Voidplume Crest]] | Incomum | Coleta em campo / missões | — |
| [[open_worlds/zariman/voidplume_drift\|Voidplume Drift]] | Incomum | Coleta em campo / missões | — |
| [[open_worlds/zariman/mawfish_bones\|Mawfish Bones]] | Incomum | Pesca — Mawfish | — |
| [[open_worlds/zariman/vitreospina_fillet\|Vitreospina Fillet]] | Incomum | Pesca — Vitreospina | — |
| [[open_worlds/zariman/voidplume_down\|Voidplume Down]] | Raro | Missões / Void Angels | — |
| [[open_worlds/zariman/voidplume_wisp\|Voidplume Wisp]] | Raro | Missões / Void Angels | — |
| [[open_worlds/zariman/voidplume_intact\|Voidplume Intact]] | Raro | Drop de Void Angels | Muito raro — requer derrotar Void Angel |

---

### Railjack (Proximas)
*Recursos minerados de asteroides — usados para craftar e atualizar componentes da nave.*

| Recurso | Raridade | Proxima | Notas |
|---|---|---|---|
| [[railjack/asterite\|Asterite]] | Comum | Todas | Recurso universal — base de quase todo crafting Railjack |
| [[railjack/pustrels\|Pustrels]] | Comum | Earth Proxima | — |
| [[railjack/coprun\|Coprun]] | Comum | Earth Proxima | — |
| [[railjack/lucum\|Lucum]] | Comum | Earth Proxima | — |
| [[railjack/aucrumite\|Aucrumite]] | Comum | Earth / Venus Proxima | — |
| [[railjack/fresnite\|Fresnite]] | Comum | Venus Proxima | — |
| [[railjack/heciphron\|Heciphron]] | Incomum | Earth / Mercury Proxima | — |
| [[railjack/isos\|Isos]] | Incomum | Deimos Proxima | — |
| [[railjack/radian_sentirum\|Radian Sentirum]] | Incomum | Venus Proxima | — |
| [[railjack/carbides\|Carbides]] | Incomum | Jupiter Proxima | — |
| [[railjack/noctrul\|Noctrul]] | Incomum | Saturn Proxima | — |
| [[railjack/goblite_tears\|Goblite Tears]] | Incomum | Neptune Proxima | — |
| [[railjack/adramal_alloy\|Adramal Alloy]] | Raro | Saturn Proxima | — |
| [[railjack/gallos_rod\|Gallos Rod]] | Raro | Veil Proxima | — |
| [[railjack/magnum_khra\|Magnum Khra]] | Raro | Veil Proxima | Recurso mais raro do Railjack |

---

## Referências Cruzadas

| Sistema | Índice |
|---|---|
| Warframes de farm (Nekros, Hydroid, Khora) | [[_Warframes _Indice\|Warframes]] |
| Locais de coleta por planeta | [[_Locais _Indice\|Locais]] |
| Missões eficientes por tipo (Survival, Excavation) | [[_Missoes _Indice\|Missões]] |
| Sindicatos dos Open Worlds | [[_Sindicatos _Indice\|Sindicatos]] |
| Mecânicas de Boosters e Nightwave | [[_Mecanicas _Indice\|Mecânicas]] |

---

## Curiosidades

- Argon Crystal é o único recurso perecível do jogo — sua mecânica de decaimento foi adicionada para forçar o uso logo após o farm.
- Nitain Extract foi por muito tempo o recurso mais odiado da comunidade — obtido apenas via Nightwave ou eventos de tempo limitado.
- Forma foi inicialmente não-craftável — era apenas recompensa de missão. A receita craftável foi adicionada após pressão da comunidade.
- Orokin Cell é frequentemente o gargalo de builds de Warframes Prime — necessária em grande quantidade e com drop concentrado em apenas alguns planetas.
- Tellurium tem uma das piores taxas de drop do jogo convencional — missões Archwing em Urano são virtualmente a única fonte eficiente.
- Kuva foi introduzida com o sistema de Riven Mods — tornou a Fortaleza Kuva, antes irrelevante no end-game, em destino regular de farm.
- Toroids na Orbe Vallis eram notoriamente difíceis no lançamento — a comunidade desenvolveu estratégias específicas de farm em cavernas com alert level máximo.
- Oxium Osprey foi inimigo infame por anos — o Osprey se autodestrói se não morto rápido, forçando a comunidade a desenvolver técnicas dedicadas para matar o grupo inteiro antes da explosão.

----------------------------------------
