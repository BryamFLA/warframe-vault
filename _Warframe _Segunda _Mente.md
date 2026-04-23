---
title: Warframe — Segunda Mente
tipo: home
tags:
  - home
  - index
  - warframe
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
atualizado: 2026-04-22
---

# Warframe — Segunda Mente

> [!quote]
> *"O Tenno não esquece. O Tenno organiza."*

---

## Sobre o Jogo

Warframe é um TPS cooperativo free-to-play ambientado no Sistema Origem — versão futurista do Sistema Solar. O jogador controla um Tenno, guerreiro antigo reanimado, operando dentro de exoesqueletos biomecânicos chamados Warframes. O jogo é construído em torno de farmear recursos, craftar equipamentos e dominar sistemas de build cada vez mais profundos.

**Ciclo central:** missões procedurais → recursos → crafting → novos frames e armas → Mastery Rank → conteúdo end-game.

**Modelo de conteúdo:** expansões gratuitas chamadas *Updates* adicionam novos Warframes, quests, open worlds e modos de jogo continuamente desde 2013.

---

## Arquitetura do Vault

Este vault organiza o conhecimento do jogo em pilares independentes com escopo definido e sem sobreposição entre seções.

| Pasta           | Conteúdo                                                                     |
| --------------- | ---------------------------------------------------------------------------- |
| `warframes/`    | Um arquivo por frame — base, Prime e Umbra. Habilidades, papel e como obter. |
| `armas/`        | Primárias, secundárias, brancas e archwing. Um arquivo por arma.             |
| `mods/`         | Mods de warframe, armas, companheiros e especiais. Um arquivo por mod.       |
| `recursos/`     | Materiais de crafting por raridade e sistema de origem.                      |
| `missoes/`      | Tipos de missão, jornadas, junctions e bounties.                             |
| `mecanicas/`    | Sistemas transversais: combate, progressão, economia, sindicatos e eventos.  |
| `locais/`       | Planetas do mapa estelar e open worlds.                                      |
| `lore/`         | Cronologia, facções, personagens e chefes.                                   |
| `companheiros/` | Sentinels, kubrows, kavats, MOAs, hounds e variantes de Deimos.              |
| `cosmeticos/`   | Skins, syandanas, capacetes, efemeras, paletas e anexos.                     |

**Regras do sistema:**
- Um arquivo por entidade — cada frame, arma, mod e recurso tem seu próprio `.md`
- Sem duplicação — inimigos ficam em `lore/faccoes/` via tag `inimigo`
- Mecânicas transversais ficam em `mecanicas/` sem hierarquia profunda
- Rivens têm pasta própria em `mods/especiais/` pelo volume potencial de entradas

---

## Índices do Sistema

| Índice                                  | Responde perguntas sobre                                                 | Sub-índices                                                                                                                                                             |     |
| --------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| [[_Warframes _Indice\|Warframes]]       | Frames, funções, bosses associados, onde obter, pré-requisitos de acesso | —                                                                                                                                                                       |     |
| [[_Armas _Indice\|Armas]]               | Slots, tipos, fontes, facções e sistemas de origem                       | [[_Armas _Primarias _Indice\|Primárias]] · [[_Armas _Secundarias _Indice\|Secundárias]] · [[_Armas _Brancas _Indice\|Brancas]] · [[_Armas _Archwing _Indice\|Archwing]] |     |
| [[_Mods _Indice\|Mods]]                 | Raridades, categorias, efeitos resumidos, fontes de obtenção             | [[_Mods Warframe _Indice\|Warframe]] · [[_Mods Armas _Indice\|Armas]] · [[_Mods Companheiros _Indice\|Companheiros]] · [[_Mods Especiais _Indice\|Especiais]]           |     |
| [[_Recursos _Indice\|Recursos]]         | Materiais, raridades, planetas de origem, métodos de coleta              | —                                                                                                                                                                       |     |
| [[_Companheiros _Indice\|Companheiros]] | Tipos, funções, fontes de obtenção, sistemas de origem                   | —                                                                                                                                                                       |     |
| [[_Missoes _Indice\|Missões]]           | Tipos de missão, objetivos, jornadas, junctions e bounties               | —                                                                                                                                                                       |     |
| [[_Mecanicas _Indice\|Mecânicas]]       | Sistemas de combate, progressão, economia e social                       | [[_Sindicatos _Indice\|Sindicatos]] · [[_Eventos _Indice\|Eventos]]                                                                                                     |     |
| [[_Locais _Indice\|Locais]]             | Planetas, facções dominantes, bosses, recursos nativos, como acessar     | —                                                                                                                                                                       |     |
| [[_Lore _Indice\|Lore]]                 | Facções, personagens, chefes, cronologia do universo                     | [[_Faccoes _Indice\|Facções]] · [[_Personagens _Indice\|Personagens]] · [[_Chefes _Indice\|Chefes]]                                                                     |     |
| [[_Cosmeticos _Indice\|Cosméticos]]     | Tipos de cosmético, fontes, exclusividade, sistema Tennogen              | —                                                                                                                                                                       |     |

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
