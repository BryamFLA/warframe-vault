---
title: Atlas
aliases: [Atlas]
tipo: warframe
archetype: [brawler, dps, tank]
resumo: "Atlas — Brawler de 475 de armadura que soca com Landslide e se cura com Rubble de inimigos petrificados; a passiva o deixa imune a Knockdown enquanto está no chão."
status: completo
rag: true
tags: [warframe, brawler, terra, armadura, rubble]
mastery_rank: 0
progenitor: Toxin
sindicato_augment: ["[[mecanicas/sindicatos/red_veil.md|Red Veil]]", "[[mecanicas/sindicatos/steel_meridian.md|Steel Meridian]]"]
fontes: ["https://wiki.warframe.com/w/Atlas", "https://wiki.warframe.com/w/Module:Warframes/data", "https://wiki.warframe.com/w/Module:Ability/data", "https://wiki.warframe.com/w/Jordas_Golem", "https://wiki.warframe.com/w/Module:DropTables/data", "https://wiki.warframe.com/w/The_Jordas_Precept"]
estado:
  forjado: false
  rank_max: false
  polarizacoes: 0
  reator_instalado: false
  subsuncao_helminte_cedida: false
atualizado: 2026-10-08
verificado: true
agente: opus
---

# Atlas

> [!info] Resumo
> **Brawler de punho.** O frame de maior armadura entre os iniciais: **475** — mais que o quádruplo do **[[warframes/regular/ash.md|Ash]]**. A passiva o deixa **imune a Knockdown enquanto estiver no chão**, o que é raro no jogo e muda como ele joga: ele não é derrubado por Bombard nem por explosão.
> O ciclo dele é fechado: **Petrify** fossiliza inimigos e aumenta o dano que eles tomam, **Landslide** ou melee os estilhaça, e os estilhaços viram **Rubble** — que **cura o Atlas e lhe dá armadura extra**. Ele se sustenta matando.


## 📊 Estatísticas Base — Atlas


| Atributo | Rank 0 | Rank 30 |
|---|---|---|
| Vida | **270** | **270** — não escala com rank |
| Escudo | **270** | **270** — não escala com rank |
| Armadura | **475** | **475** — a mais alta entre os frames iniciais |
| Energia | **175** | **175** |
| Energia inicial | **50** | **50** |
| Vel. Sprint | **0,9** | **0,9** — lento de propósito |

> [!important] 475 de armadura muda a matemática de vida
> Vida 270 parece pouco, mas armadura no Warframe **não é subtração, é redução percentual**: a fórmula é `redução = armadura / (armadura + 300)`. Com **475**, isso dá **≈61% de redução de dano**, o que faz os 270 de vida valerem como ~**700** de vida efetiva.
>
> É por isso que **[[mods/warframe/steel_fiber.md|Steel Fiber]]** (+110% de armadura) rende muito mais no Atlas que em quase qualquer outro frame: ele multiplica uma base já grande. Com Steel Fiber a armadura vai a ~998, e a redução a **≈77%**.
>
> Como nos outros frames aqui, o [`Module:Warframes/data`](https://wiki.warframe.com/w/Module:Warframes/data) **não publica campos `*Rank30`** para o Atlas — os valores são fixos do rank 0 ao 30.

| Item | Valor |
|---|---|
| Polaridades inatas | **Naramon** (—) + **Vazarin** (D) + **Madurai** (V) |
| Polaridade de Aura | **Madurai** (V) |
| Mastery Rank exigido | **0** |
| Progenitor (para Kuva/Tenet) | **Toxin** |
| Preço no Mercado | **275 platina** (frame pronto). O blueprint principal **não é vendido** por créditos |
| Preço de venda | **10.000 créditos** |
| Introduzido em | **Update 17.5** |
| Versão Prime | **[[warframes/primes/atlas_prime.md\|Atlas Prime]]** (Update 25.8) — 550 de vida, 500 de armadura, 215 de energia, 75 de energia inicial e **4 polaridades** |
| Tema | Brawler, Elemental de Terra |


## 🔮 Habilidades — Atlas


| # | Nome | Custo | Efeito |
|---|---|---|---|
| Passiva | **Imune a Knockdown** | — | **Imune a efeitos de Knockdown enquanto estiver no chão.** Não vale no ar nem durante parkour — é preciso estar com os pés no solo |
| 1 | **Landslide** | **25** (e **cai a cada golpe do combo**) | Soco deslizante explosivo, repetível **até três vezes** em combo. **Cada golpe aumenta o raio** e **reduz o custo de energia** do seguinte. **Aceita mods nos Landslide Fists**, que alteram os stats dele |
| 2 | **Tectonics** | **50** | Invoca um **Bulwark** (muro de pedra); ativar de novo manda as pedras rolando contra o inimigo. Bulwark atacado libera **Slash em área proporcional à vida que perdeu** |
| 3 | **Petrify** | **75** | Olhar que **fossiliza** inimigos, **aumenta o dano que eles tomam**, **cura os Rumblers** e cria **Bulwarks petrificados**. Inimigo petrificado estilhaçado dropa **Rubble**, que cura o Atlas. É a habilidade **cedida ao [[mecanicas/helminth.md\|Helminth]]** |
| 4 | **Rumblers** | **100** | Invoca **dois brutamontes de pedra** elementais. A invocação **petrifica** inimigos próximos ao Atlas. Ao fim, os Rumblers **desmoronam num monte de Rubble curativo** |

### Detalhamento das habilidades — Atlas

- **Passiva — imune a Knockdown no chão:** parece pequena e não é. No meio do jogo para a frente, o que mata Warframe de corpo a corpo é **ser derrubado** por **Bombard** Grineer, explosão de **Volatile Runner** ou onda de choque — você perde um segundo no chão e toma o resto. O Atlas simplesmente não cai. O preço é ter de ficar no solo: **durante parkour ou no ar a imunidade não vale**, o que é exatamente o oposto de como a maioria dos frames joga.

- **1. Landslide (25, decrescente):** o motor de dano dele. É um **combo de três golpes**, e cada golpe do combo **custa menos energia e tem raio maior** que o anterior. O detalhe mais importante da build: **os Landslide Fists aceitam mods** — ou seja, o dano do soco é influenciado pelos mods instalados neles, não só por Força de Habilidade. Encadear os três golpes é mais barato e mais forte que spammar o primeiro.

- **2. Tectonics (50):** a habilidade mais fraca do kit, e a candidata natural à substituição pelo **[[mecanicas/helminth.md|Helminth]]**. O **Bulwark** serve como cobertura móvel e, quando apanha, devolve **Slash em área proporcional ao dano que absorveu** — útil na teoria, lento na prática. Escala com **Força** (vida do muro) e **Alcance**.

- **3. Petrify (75):** **a habilidade central do Atlas**, e não pela petrificação em si. Ela faz quatro coisas ao mesmo tempo: **congela** o inimigo, **aumenta o dano que ele toma**, **cura os Rumblers** e transforma cada inimigo estilhaçado em **Rubble**. O Rubble é o que sustenta o frame — **cura e dá armadura temporária**. É também a habilidade que o Atlas **doa ao Helminth**. Escala com **Força** (bônus de dano recebido) e **Alcance** (cone do olhar).

- **4. Rumblers (100):** dois invocados de pedra que lutam por você, **mais** uma petrificação em área no momento da invocação, **mais** um monte de Rubble quando eles morrem. Três efeitos por um custo. Escala com **Força** (dano e vida dos Rumblers) e **Duração**.

> [!tip] O ciclo que faz o Atlas funcionar
> **Petrify** → estilhaça com **Landslide** ou melee → junta **Rubble** → Rubble dá **cura e armadura** → sobrevive para petrificar de novo.
>
> Isso tem uma consequência direta de build: **o Atlas quer Força e Alcance, e tolera pouca Duração** (só Rumblers e Tectonics usam Duração). E ele **precisa de inimigo** para se curar — num mapa vazio, o Atlas não se sustenta.

### Augments — Atlas

| Augment | Habilidade | Efeito | Sindicato |
|---|---|---|---|
| **Path of Statues** | Landslide | Deixa um rastro que petrifica inimigos que passam por ele | [[mecanicas/sindicatos/red_veil.md\|Red Veil]] / [[mecanicas/sindicatos/steel_meridian.md\|Steel Meridian]] |
| **Tectonic Fracture** | Tectonics | Permite mais de um Bulwark ao mesmo tempo, com menos vida cada | [[mecanicas/sindicatos/red_veil.md\|Red Veil]] / [[mecanicas/sindicatos/steel_meridian.md\|Steel Meridian]] |
| **Ore Gaze** | Petrify | Inimigos petrificados têm chance de dropar recurso extra ao estilhaçar | [[mecanicas/sindicatos/red_veil.md\|Red Veil]] / [[mecanicas/sindicatos/steel_meridian.md\|Steel Meridian]] |
| **Rumbled** | Rumblers | Atlas assume os atributos de um Rumbler, com Landslide reforçado | [[mecanicas/sindicatos/red_veil.md\|Red Veil]] / [[mecanicas/sindicatos/steel_meridian.md\|Steel Meridian]] |
| **Titanic Rumbler** | Rumblers | Troca os dois Rumblers por um só, maior e mais resistente | [[mecanicas/sindicatos/red_veil.md\|Red Veil]] / [[mecanicas/sindicatos/steel_meridian.md\|Steel Meridian]] |

> [!note] Atlas é um dos frames com mais Augments: cinco
> **Rumblers tem dois Augments** (Rumbled e Titanic Rumbler), que são **mutuamente exclusivos** na prática — ocupam o mesmo slot e mudam a habilidade de formas opostas.
>
> Os cinco são vendidos por **[[mecanicas/sindicatos/red_veil.md|Red Veil]]** e **[[mecanicas/sindicatos/steel_meridian.md|Steel Meridian]]**, conforme o `Module:Warframes/data`. ⚠️ **Nenhum tem arquivo próprio no vault** — os nomes ficam em texto puro (seção 3 do `_CONVENCOES.md`).

> [!warning] Correção do arquivo anterior
> A versão anterior deste arquivo listava os sindicatos de Augment do Atlas como **"Cephalon Suda e Véu Vermelho"**. Está **errado**: são **Red Veil e Steel Meridian**.


## 🏗️ Como Construir — Atlas


**Blueprint principal:** é **recompensa da jornada [[missoes/jornadas/secundarios/the_jordas_precept.md|The Jordas Precept]]** — não é vendido por créditos no Mercado. Cópias adicionais podem ser compradas do **[[mecanicas/sindicatos/cephalon_simaris.md|Cephalon Simaris]]** por **50.000 de reputação**. O frame pronto custa **275 platina**.

**Componentes:** os três caem do **[[lore/chefes/jordas_golem.md|Jordas Golem]]**, no nó **Jordas Golem Assassinate**, em **[[locais/planetas/eris.md|Eris]]** — que só abre **depois** da mesma jornada.

> [!important] É uma luta de Archwing
> O **[[lore/chefes/jordas_golem.md|Jordas Golem]]** é combatido **em Archwing**, dentro e fora de uma nave infestada gigante. Exige a jornada **[[missoes/jornadas/principais/the_archwing.md|The Archwing]]** e um Archwing com armas modadas — é a razão de muita gente travar no Atlas, não o drop.

| Componente | Onde dropa | Custo de fabricação | Tempo |
|---|---|---|---|
| **Blueprint principal** | **[[missoes/jornadas/secundarios/the_jordas_precept.md\|The Jordas Precept]]** (recompensa) ou **[[mecanicas/sindicatos/cephalon_simaris.md\|Cephalon Simaris]]** por 50.000 de reputação | 30.000 cr · 1 Neurovisor · 1 Chassi · 1 Sistemas · 1 [[recursos/raridades/raro/orokin_cell.md\|Orokin Cell]] | **3 dias** |
| **Neurovisor** | **[[lore/chefes/jordas_golem.md\|Jordas Golem]]** — **38,72%** (≈2 mortes esperadas) | 15.000 cr · 1.400 [[recursos/raridades/comum/polymer_bundle.md\|Polymer Bundle]] · 1.100 [[recursos/raridades/comum/alloy_plate.md\|Alloy Plate]] · 800 [[recursos/raridades/comum/circuits.md\|Circuits]] · 5 [[recursos/raridades/raro/neurodes.md\|Neurodes]] | **12 h** |
| **Chassi** | **[[lore/chefes/jordas_golem.md\|Jordas Golem]]** — **38,72%** (≈2 mortes esperadas) | 15.000 cr · 1.800 [[recursos/raridades/comum/nano_spores.md\|Nano Spores]] · 1.300 [[recursos/raridades/raro/cryotic.md\|Cryotic]] · 700 [[recursos/raridades/comum/rubedo.md\|Rubedo]] · 2 [[recursos/raridades/raro/argon_crystal.md\|Argon Crystal]] | **12 h** |
| **Sistemas** | **[[lore/chefes/jordas_golem.md\|Jordas Golem]]** — **22,56%** (≈4 mortes esperadas) | 15.000 cr · 4.600 [[recursos/raridades/comum/ferrite.md\|Ferrite]] · 1.700 [[recursos/raridades/comum/polymer_bundle.md\|Polymer Bundle]] · 5 [[recursos/raridades/raro/morphics.md\|Morphics]] · 1 [[recursos/raridades/raro/orokin_cell.md\|Orokin Cell]] | **12 h** |

**Via alternativa — The Circuit (Duviri):** depois de **[[missoes/jornadas/principais/the_duviri_paradox.md|The Duviri Paradox]]**, na semana em que o Atlas estiver na rotação, os blueprints saem do **The Circuit** nos tiers **2 (Neurovisor)**, **5 (Chassi)**, **8 (Sistemas)** e **10 (principal)**. Note que é diferente do **[[warframes/regular/ash.md|Ash]]**, cujos quatro blueprints saem todos no Tier 10.

> [!warning] Dois recursos exigem atenção
> - **[[recursos/raridades/raro/argon_crystal.md|Argon Crystal]] (2, para o Chassi)** — só cai no **[[locais/planetas/void.md|Void]]** e **decai 50% a cada 24 horas**. **Farme-o por último**, depois de já ter todo o resto, ou ele desaparece antes de você usar.
> - **[[recursos/raridades/raro/cryotic.md|Cryotic]] (1.300, para o Chassi)** — vem **só de missões de [[missoes/tipos/excavation.md|Excavation]]**. 1.300 é bastante: **Hieracon**, em **[[locais/planetas/plutao.md|Plutão]]**, é o melhor nó para isso.

**Custo total de recurso (os 4 blueprints):** 75.000 créditos, 3.100 Polymer Bundle, 1.100 Alloy Plate, 800 Circuits, 5 Neurodes, 1.800 Nano Spores, 1.300 Cryotic, 700 Rubedo, 2 Argon Crystal, 4.600 Ferrite, 5 Morphics, 2 Orokin Cell — e **3 dias e 12 horas** de forja. **É um frame caro em recurso comum**, bem mais que o Ash.


## 🛠️ Build — Atlas


### Build geral — Landslide e Rubble na estrela do mapa

| Slot | Mod | Função |
|---|---|---|
| Aura | [[mods/warframe/corrosive_projection.md\|Corrosive Projection]] | −18% de armadura inimiga por membro do squad. Landslide é dano direto: menos armadura = mais dano |
| Exilus | [[mods/warframe/rush.md\|Rush]] | +30% de velocidade de sprint. O Atlas tem sprint 0,9, o mais lento aqui — isso compensa |
| 1 | [[mods/warframe/umbral_intensify.md\|Umbral Intensify]] | +77% Força com o set — dano de Landslide, bônus do Petrify e vida dos Rumblers |
| 2 | [[mods/warframe/intensify.md\|Intensify]] | +30% Força, somando com o Umbral |
| 3 | [[mods/warframe/stretch.md\|Stretch]] | +45% Alcance — cone do Petrify e raio do Landslide |
| 4 | [[mods/warframe/streamline.md\|Streamline]] | +30% Eficiência — Petrify custa 75, que é caro |
| 5 | [[mods/warframe/steel_fiber.md\|Steel Fiber]] | +110% Armadura. **O melhor mod defensivo do Atlas**: leva 475 para ~998 e a redução de dano de 61% para ~77% |
| 6 | [[mods/warframe/umbral_vitality.md\|Umbral Vitality]] | +440% Vida e sinergia Umbral — com 270 de base, é necessário |
| 7 | [[mods/warframe/flow.md\|Flow]] | +150% Energia máxima — sustenta o ciclo Petrify/Rumblers |
| 8 | [[mods/warframe/natural_talent.md\|Natural Talent]] | +Velocidade de conjuração. O Petrify tem animação longa e o Atlas fica exposto nela |

**Resultado:** Força alta, Alcance bom, Armadura próxima de 1.000. O Atlas aguenta a estrela do mapa inteira sem recuar, e o **Rubble** do Petrify o cura entre grupos.

**Por que não há mod de Duração:** só **Rumblers** e **Tectonics** usam Duração, e nenhum dos dois é o eixo da build. Trocar Duração por Força e Armadura é o certo neste frame.

**Prioridade de Forma:** as **3 polaridades inatas** (Naramon, Vazarin, Madurai) já cobrem três slots. Conte **3 a 4 Forma** mais um **Orokin Reactor** — e os **Umbral Forma**, se tiver, para o set Umbral.

### Build Steel Path — tanque de armadura e Rubble

| Slot | Mod | Função |
|---|---|---|
| Aura | [[mods/warframe/corrosive_projection.md\|Corrosive Projection]] | No [[mecanicas/steel_path.md\|Steel Path]] o inimigo tem **+250% de armadura** — remoção de armadura deixa de ser opcional |
| Exilus | [[mods/warframe/rolling_guard.md\|Rolling Guard]] | Imunidade a dano e status por 3 s ao rolar — a saída quando o Rubble acaba |
| 1 | [[mods/warframe/umbral_vitality.md\|Umbral Vitality]] | +440% Vida com sinergia Umbral |
| 2 | [[mods/warframe/steel_fiber.md\|Steel Fiber]] | +110% Armadura — o eixo defensivo do frame |
| 3 | [[mods/warframe/adaptation.md\|Adaptation]] | Até +90% de resistência ao tipo recebido. **Multiplica** com a armadura, não soma |
| 4 | [[mods/warframe/umbral_intensify.md\|Umbral Intensify]] | +77% Força — o bônus de dano recebido do Petrify é o que mantém o Landslide relevante lá |
| 5 | [[mods/warframe/stretch.md\|Stretch]] | +45% Alcance — petrificar mais inimigos por olhar = mais Rubble |
| 6 | [[mods/warframe/streamline.md\|Streamline]] | +30% Eficiência |
| 7 | [[mods/warframe/flow.md\|Flow]] | +150% Energia máxima |
| 8 | [[mods/warframe/primed_vigor.md\|Primed Vigor]] | +110% Vida e +110% Escudo — reforça a base pequena de 270/270 |

**A lógica no [[mecanicas/steel_path.md|Steel Path]]:** o dano direto do **Landslide** não acompanha a armadura de lá, mas o **Petrify** sim — ele **aumenta o dano que o inimigo toma**, e isso é multiplicativo. Então o Atlas lá funciona como **tanque que amplifica**: petrifica, aumenta o dano recebido, e você mata com a arma ou com melee enquanto o **Rubble** o mantém de pé.

**Armadura e Adaptation se multiplicam.** Com ~998 de armadura (≈77% de redução) e Adaptation em 90%, a redução combinada passa de **97%** contra o tipo de dano que está entrando. É o que faz o Atlas viável no Steel Path apesar dos 270 de vida.

**Arcanos recomendados:** Arcane Guardian (armadura) e Arcane Energize (energia). ⚠️ Nenhum dos dois tem arquivo próprio no vault.

**Prioridade de Forma:** **4 a 5 Forma** mais **Orokin Reactor**. Com dois mods Umbral e Primed Vigor, a capacidade é o limite real.


## 🧬 Helminth — Atlas


| Item | Valor |
|---|---|
| Habilidade cedida ao Helminth | **Petrify** — confirmada como `Subsumed` no `Module:Warframes/data` |
| Habilidade tática (Helminth) | **Rumblers** |
| Slot recomendado para substituição | **2 (Tectonics)** — a habilidade mais fraca do kit, e a que menos participa do ciclo de Rubble |
| Subsumidas comuns neste frame | **Nourish** (Grendel) para dano e energia; **Gloom** (Sevagoth) para controle e cura; **Eclipse** (Mirage) para dano. ⚠️ Nenhuma tem arquivo próprio no vault |

> [!tip] Petrify é uma das subsumidas mais disputadas do jogo
> **Petrify** é valiosa fora do Atlas porque faz três coisas de uma vez: **para** o inimigo, **aumenta o dano que ele toma** e abre **Finisher**. Isso a torna útil em praticamente qualquer frame de dano.
>
> O Atlas é, por isso, um dos frames que mais vale **farmar duas vezes**: um para jogar, um para alimentar o **[[mecanicas/helminth.md|Helminth]]**. Mas note o custo: o segundo Atlas exige outra rodada de **[[lore/chefes/jordas_golem.md|Jordas Golem]]** em Archwing, mais **1.300 [[recursos/raridades/raro/cryotic.md|Cryotic]]** e **2 [[recursos/raridades/raro/argon_crystal.md|Argon Crystal]]** — ou uma semana dele na rotação do The Circuit.


## 🔗 Sinergias e Uso — Atlas


**Funciona bem em:**

- **[[missoes/tipos/defense.md|Defense]]** e **[[missoes/tipos/mobile_defense.md|Mobile Defense]]** — ao contrário do **[[warframes/regular/ash.md|Ash]]**, o Atlas **segura posição**: 475 de armadura, imunidade a Knockdown, Bulwark como cobertura e Rumblers puxando aggro. É o uso natural dele.
- **[[missoes/tipos/excavation.md|Excavation]]** — a escavadeira precisa ser defendida num ponto fixo, e o Atlas não sai de onde está. Combina com o fato de ele **precisar** de Cryotic de Excavation para se construir.
- **[[missoes/tipos/interception.md|Interception]]** — Rumblers defendem um ponto enquanto você cobre outro.
- **[[missoes/tipos/disruption.md|Disruption]]** — Petrify para o Demolisher e aumenta o dano que ele toma; a imunidade a Knockdown ignora o pulso de choque dele.
- **Mineração e farm de recurso** — o Augment **Ore Gaze** faz inimigo petrificado dropar recurso extra. É nicho, mas é o único frame com isso.

**Evitar em:**

- **[[missoes/tipos/spy.md|Spy]]** — sprint 0,9 (o mais lento do jogo entre os frames comuns), nenhuma invisibilidade e nenhuma mobilidade vertical. O Atlas é o pior frame possível para cofre cronometrado.
- **[[missoes/tipos/capture.md|Capture]]** e **[[missoes/tipos/rush.md|Rush]]** — missões que premiam velocidade pura. Landslide dá mobilidade horizontal, mas não compensa o sprint baixo.
- **Mapa vazio ou inimigo esparso** — o Atlas **se cura com Rubble de inimigo morto**. Sem inimigo para petrificar e estilhaçar, ele não tem sustento nenhum.

**Sinergia de esquadrão:**

- **Frames que agrupam inimigo** (Nidus com Larva, Vauban, Mag com Magnetize) multiplicam o Atlas diretamente: Petrify é em cone, e inimigo amontoado significa muito mais Rubble por conjuração.
- **Aliados com [[mods/warframe/corrosive_projection.md|Corrosive Projection]]** — Landslide é dano físico direto, então armadura inimiga é o limitador dele. Quatro Corrosive Projection no squad tiram 72% da armadura.
- **Frames de energia** (Trinity, Harrow) resolvem o custo de 75 do Petrify, que é o gargalo real da build de Alcance alto.

**Armas que combinam:** o Atlas quer **melee**, pela sinergia de estilhaçar inimigo petrificado de perto. **[[armas/brancas/tekko_prime.md|Tekko Prime]]** é a escolha temática e mecânica — são manoplas, como os punhos dele. **[[armas/brancas/kronen_prime.md|Kronen Prime]]** e **[[armas/brancas/glaive_prime.md|Glaive Prime]]** também funcionam. Para arma de tiro, qualquer coisa que aproveite o bônus de dano recebido do Petrify serve; **[[armas/secundarias/kuva_nukor.md|Kuva Nukor]]** é boa porque aplica status em vários alvos de uma vez.


## 📖 História — Atlas


> *"Enemies tremble before the brawler with fists as hard as stone. Atlas deals high damage. Command terrestrial elements that form the foundation of any battlefield."* — Códice

Atlas é o Warframe **elemental de terra** — pedra, não metal. O nome vem do titã da mitologia grega que sustenta o céu nos ombros, e o kit todo é literal sobre isso: ele invoca muros, levanta brutamontes de rocha e transforma inimigo em estátua.

Ele foi introduzido no **Update 17.5**, junto da jornada **[[missoes/jornadas/secundarios/the_jordas_precept.md|The Jordas Precept]]** — a história do **[[lore/chefes/jordas_golem.md|Jordas Golem]]**, um Cephalon enlouquecido fundido a uma nave infestada em **[[locais/planetas/eris.md|Eris]]**. Que o frame da terra firme só se consiga vencendo uma criatura no espaço, em Archwing, é uma das decisões de design mais estranhas do jogo.

A versão **[[warframes/primes/atlas_prime.md|Atlas Prime]]** chegou no **Update 25.8**, com 550 de vida, 500 de armadura, 215 de energia e **quatro polaridades**.


## 💡 Curiosidades — Atlas


- **O `InternalName` do Atlas é `/Lotus/Powersuits/Brawler/Brawler`.** Como o Ash (cujo nome interno é "Ninja"), o nome de desenvolvimento era o arquétipo puro.
- **Landslide é uma das poucas habilidades do jogo que aceitam mods de arma.** Os **Landslide Fists** são tratados como arma própria, com stats próprios — é por isso que o dano dele não depende só de Força de Habilidade.
- **Rumblers é uma das duas habilidades do jogo com dois Augments** (Rumbled e Titanic Rumbler), que mudam a habilidade em direções opostas: um transforma o Atlas num Rumbler, o outro troca os dois invocados por um só maior.

---
