---
title: Ash
aliases: [Ash]
tipo: warframe
archetype: [furtivo, dps, assassino]
resumo: "Ash — Warframe furtivo de assassinato que escala por Bleed e Finisher: a passiva dá +25% de dano e +50% de duração aos efeitos de Bleed, e Blade Storm marca alvos a 50 m por 12 de energia cada."
status: completo
rag: true
tags: [warframe, stealth, slash, bleed]
mastery_rank: 0
progenitor: Radiation
sindicato_augment: ["[[mecanicas/sindicatos/arbiters_of_hexis.md|Arbiters of Hexis]]", "[[mecanicas/sindicatos/red_veil.md|Red Veil]]"]
fontes: ["https://wiki.warframe.com/w/Ash", "https://wiki.warframe.com/w/Module:Warframes/data", "https://wiki.warframe.com/w/Module:Ability/data", "https://wiki.warframe.com/w/Blade_Storm", "https://wiki.warframe.com/w/Module:DropTables/data"]
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

# Ash

> [!info] Resumo
> Warframe **furtivo de assassinato**. A mecânica central é **Bleed**: a passiva dá **+25% de dano** e **+50% de duração** a todo efeito de Bleed que ele aplica, e as quatro habilidades alimentam isso.
> **Blade Storm** não tem custo de ativação — ele **marca** inimigos a até **50 m** por **12 de energia cada** e envia clones para executá-los. É o Warframe de limpar sala sem ser visto, forte em **[[missoes/tipos/exterminate.md|Exterminate]]** e **[[missoes/tipos/spy.md|Spy]]**, e fraco onde há objetivo a defender.


## 📊 Estatísticas Base — Ash


| Atributo | Rank 0 | Rank 30 |
|---|---|---|
| Vida | **455** | **455** — não escala com rank |
| Escudo | **270** | **270** — não escala com rank |
| Armadura | **105** | **105** |
| Energia | **100** | **100** |
| Energia inicial | **50** | **50** |
| Vel. Sprint | **1,15** | **1,15** |

> [!important] Os stats do Ash não sobem com o rank
> O [`Module:Warframes/data`](https://wiki.warframe.com/w/Module:Warframes/data) publica campos separados de rank 30 (`HealthRank30`, `ShieldRank30`, `ArmorRank30`, `EnergyRank30`) **apenas para os 35 frames cujos stats escalam**. O Ash **não é um deles**: os valores acima são fixos do rank 0 ao 30.
>
> Subir o rank do Ash só serve para **liberar os slots de mod e a capacidade**, não para ganhar vida ou escudo.

| Item | Valor |
|---|---|
| Polaridades inatas | **2× Madurai** (V) |
| Polaridade de Aura | **Madurai** (V) |
| Mastery Rank exigido | **0** — disponível desde o início |
| Progenitor (para Kuva/Tenet) | **Radiation** |
| Preço no Mercado | **375 platina** (frame pronto) ou **35.000 créditos** (blueprint principal) |
| Preço de venda | **10.000 créditos** |
| Introduzido em | **Vanilla** — é um dos frames originais do jogo |
| Versão Prime | **[[warframes/primes/ash_prime.md\|Ash Prime]]** — mais escudo (365), mais armadura (185), sprint 1,2 e 3 polaridades. **Vaulted desde 30/05/2017** |
| Tema | Assassino, Ninja |


## 🔮 Habilidades — Ash


| # | Nome | Custo | Efeito |
|---|---|---|---|
| Passiva | **Bleed aprimorado** | — | Efeitos de **Bleed** causados por Ash fazem **+25% de dano** e duram **+50% mais tempo**. Vale para qualquer fonte de Bleed dele — arma de Slash inclusive |
| 1 | **Shuriken** | **25** | Lança uma lâmina giratória de alto dano que **crava o inimigo na parede**. É a habilidade **cedida ao [[mecanicas/helminth.md\|Helminth]]** |
| 2 | **Smoke Screen** | **35** | Solta uma bomba de fumaça que **atordoa** os inimigos em volta e **deixa Ash invisível** por um tempo |
| 3 | **Teleport** | **25** | Teleporta até um alvo e executa um **Finisher**. Se o Finisher mata, Ash **recupera parte da energia gasta** |
| 4 | **Blade Storm** | **0 para ativar** · **12 por inimigo marcado** | Entra em modo de marcação: inimigos a até **50 m** vistos perto da mira ganham uma marca de morte (**12 de energia cada**) e são executados por **clones de sombra**. Ash pode entrar na briga com **Teleport**. **Os clones são afetados pelos mods dele** |

### Detalhamento das habilidades — Ash

- **Passiva — Bleed aprimorado:** é o eixo de toda build de dano do Ash. Os **+25% de dano** e **+50% de duração** valem para **qualquer** proc de Bleed que ele cause, inclusive o da arma. Isso faz dele o melhor frame do jogo para armas de **Slash** alto e para o mod **[[mods/especiais/hemorrhage.md|Hemorrhage]]**.

- **1. Shuriken (25):** dano direto e **crava o alvo na parede**, o que o remove da luta. É a habilidade que Ash **doa ao [[mecanicas/helminth.md|Helminth]]** — ou seja, se você subsumir o Ash, é o Shuriken que fica disponível para colocar em outros frames. Escala com **Força de Habilidade**.

- **2. Smoke Screen (35):** **invisibilidade + atordoamento em área**. O atordoamento é o que importa tanto quanto a invisibilidade: inimigo atordoado é alvo de **Finisher**, e Finisher ignora armadura. Escala com **Duração** (tempo invisível) e **Alcance** (raio do atordoamento).

- **3. Teleport (25):** teleporta e executa **Finisher** no alvo. O detalhe que muda a build: **se o Finisher mata, parte da energia volta**. Com Eficiência decente, o Teleport fica quase gratuito, o que o torna a ferramenta de mobilidade **e** de execução ao mesmo tempo.

- **4. Blade Storm (0 + 12 por marca):** a habilidade mais mal-entendida do Ash. **Ativar não custa nada.** O custo é **por inimigo marcado — 12 de energia cada**, dentro de **50 m** da mira. Com 100 de energia cheia você marca cerca de **8 alvos**; com **[[mods/warframe/blind_rage.md|Blind Rage]]** e pouca Eficiência, bem menos.
  - Os **clones de sombra herdam os mods do Ash**, então Força de Habilidade aumenta o dano deles.
  - **Marcar não interrompe o que você está fazendo:** dá para marcar e continuar atirando.
  - **Eficiência é o stat mais valioso** numa build de Blade Storm, porque ela multiplica quantos alvos você marca por barra de energia.

### Augments — Ash

| Augment | Habilidade | Efeito | Sindicato |
|---|---|---|---|
| **Seeking Shuriken** | Shuriken | Reduz a armadura dos alvos atingidos | [[mecanicas/sindicatos/red_veil.md\|Red Veil]] / [[mecanicas/sindicatos/arbiters_of_hexis.md\|Arbiters of Hexis]] |
| **Smoke Shadow** | Smoke Screen | Estende a invisibilidade aos aliados próximos | [[mecanicas/sindicatos/red_veil.md\|Red Veil]] / [[mecanicas/sindicatos/arbiters_of_hexis.md\|Arbiters of Hexis]] |
| **Teleport Rush** | Teleport | Dá bônus de velocidade após o teleporte | [[mecanicas/sindicatos/red_veil.md\|Red Veil]] / [[mecanicas/sindicatos/arbiters_of_hexis.md\|Arbiters of Hexis]] |
| **Rising Storm** | Blade Storm | Aumenta o contador de combo de melee e o número de execuções | [[mecanicas/sindicatos/red_veil.md\|Red Veil]] / [[mecanicas/sindicatos/arbiters_of_hexis.md\|Arbiters of Hexis]] |

> [!note] Os 4 Augments do Ash não têm arquivo próprio no vault
> Os nomes estão em **texto puro** de propósito, conforme a seção 3 do `_CONVENCOES.md`: `mods/warframe/` não tem arquivo para nenhum deles. O **[[mecanicas/augments.md|sistema de Augments]]** está documentado, mas não os mods individuais.
>
> Os quatro são comprados com reputação de **[[mecanicas/sindicatos/red_veil.md|Red Veil]]** ou **[[mecanicas/sindicatos/arbiters_of_hexis.md|Arbiters of Hexis]]** — os dois sindicatos que vendem Augment de Ash, segundo o `Module:Warframes/data`.


## 🏗️ Como Construir — Ash


> [!danger] A fonte de drop mudou — guia antigo está errado
> **Os componentes do Ash NÃO caem mais de Manics.** Isso mudou no **Update 29.10 (19/03/2021)**. Antes do **Update 17.0 (31/07/2015)**, caíam do **[[lore/chefes/tyl_regor.md|Tyl Regor]]**, em Titania, **[[locais/planetas/urano.md|Urano]]**.
>
> **Hoje os três componentes vêm de missões de Railjack (Proxima)**, e cada um de um Proxima diferente. Qualquer guia que mande farmar Manic está desatualizado em mais de quatro anos.

**Blueprint principal:** comprado no **Mercado** por **35.000 créditos**. O frame pronto custa **375 platina**.

**Componentes:** missões de **Survival**, **Defense**, **Exterminate** e **Volatile** de Railjack, no Proxima certo para cada peça. Exige a jornada **[[missoes/jornadas/principais/rising_tide.md|Rising Tide]]** para ter um Railjack.

| Componente | Onde dropa | Custo de fabricação | Tempo |
|---|---|---|---|
| **Blueprint principal** | **Mercado** — 35.000 créditos | 25.000 cr · 1 Neurovisor · 1 Chassi · 1 Sistemas · 1 [[recursos/raridades/raro/orokin_cell.md\|Orokin Cell]] | **3 dias** |
| **Neurovisor** | **Neptune Proxima** — Defense/A e Survival/A a **12,50%**; Exterminate e Volatile a **4,71%** | 15.000 cr · 150 [[recursos/raridades/comum/alloy_plate.md\|Alloy Plate]] · 1 [[recursos/raridades/raro/neural_sensors.md\|Neural Sensors]] · 150 [[recursos/raridades/comum/polymer_bundle.md\|Polymer Bundle]] · 500 [[recursos/raridades/comum/rubedo.md\|Rubedo]] | **12 h** |
| **Chassi** | **Pluto Proxima** — Defense/A e Survival/A a **13,33%**; Exterminate e Volatile a **4,82%** | 15.000 cr · 1 [[recursos/raridades/raro/morphics.md\|Morphics]] · 1.000 [[recursos/raridades/comum/ferrite.md\|Ferrite]] · 300 [[recursos/raridades/comum/rubedo.md\|Rubedo]] | **12 h** |
| **Sistemas** | **Venus Proxima** — Defense/A e Survival/A a **13,33%**; Exterminate e Volatile a **4,88%** | 15.000 cr · 1 [[recursos/raridades/raro/control_module.md\|Control Module]] · 1 [[recursos/raridades/raro/morphics.md\|Morphics]] · 500 [[recursos/raridades/comum/salvage.md\|Salvage]] · 500 [[recursos/raridades/incomum/plastids.md\|Plastids]] | **12 h** |

**Via alternativa — The Circuit (Duviri):** depois de **[[missoes/jornadas/principais/the_duviri_paradox.md|The Duviri Paradox]]**, na semana em que o Ash estiver na rotação, **todos os blueprints dele** (principal e componentes) saem do **The Circuit** ao alcançar as recompensas de **Tier 10**. É o caminho mais previsível, porque não depende de drop.

> [!tip] Qual caminho escolher
> **Defense/A e Survival/A são quase três vezes melhores** que Exterminate e Volatile (≈13% contra ≈4,8%). Em números da própria wiki: no Pluto Proxima, o Chassi sai em **~7 rotações A** de Defense/Survival contra **~20** de Exterminate.
>
> Se você já passou por **[[missoes/jornadas/principais/the_duviri_paradox.md|The Duviri Paradox]]** e o Ash está na rotação da semana, **o Circuit é melhor que os três Proximas** — garantido em vez de sorteado.

**Custo total de recurso (os 4 blueprints):** 70.000 créditos, 150 Alloy Plate, 1 Neural Sensors, 150 Polymer Bundle, 800 Rubedo, 2 Morphics, 1.000 Ferrite, 1 Control Module, 500 Salvage, 500 Plastids, 1 Orokin Cell — e **3 dias e 12 horas** de forja somados (os componentes podem ser forjados em paralelo).


## 🛠️ Build — Ash


### Build geral — Blade Storm na estrela do mapa

| Slot | Mod | Função |
|---|---|---|
| Aura | [[mods/warframe/corrosive_projection.md\|Corrosive Projection]] | −18% de armadura inimiga por membro do squad. Polaridade Madurai bate com a Aura do Ash |
| Exilus | [[mods/warframe/natural_talent.md\|Natural Talent]] | +Velocidade de conjuração. Deixa a marcação do Blade Storm e o Smoke Screen quase instantâneos |
| 1 | [[mods/warframe/primed_continuity.md\|Primed Continuity]] | +55% Duração — mantém o Smoke Screen de pé |
| 2 | [[mods/warframe/intensify.md\|Intensify]] | +30% Força — dano dos clones e do Shuriken |
| 3 | [[mods/warframe/streamline.md\|Streamline]] | +30% Eficiência — **o stat mais importante**: mais marcas por barra de energia |
| 4 | [[mods/warframe/fleeting_expertise.md\|Fleeting Expertise]] | +60% Eficiência, −60% Duração. Com Primed Continuity a Duração fica positiva |
| 5 | [[mods/warframe/stretch.md\|Stretch]] | +45% Alcance — raio do atordoamento do Smoke Screen |
| 6 | [[mods/warframe/vitality.md\|Vitality]] | +440% Vida. Com 455 de base, o Ash é frágil sem isso |
| 7 | [[mods/warframe/primed_flow.md\|Primed Flow]] | +150% Energia máxima — mais marcas antes de recarregar |
| 8 | [[mods/warframe/rolling_guard.md\|Rolling Guard]] | Imunidade a status e dano ao rolar. Rede de segurança para frame de pouca vida |

**Resultado:** Eficiência no teto (175%), Duração ainda positiva, Força moderada. Com Eficiência máxima o custo por marca cai de **12 para 3** de energia — ou seja, **~33 alvos** com a barra cheia de Primed Flow, em vez de 8.

**Prioridade de Forma:** 1 Madurai (Intensify) → 1 Naramon (Stretch) → 1 Madurai (Fleeting Expertise). As **2 polaridades Madurai inatas** já cobrem dois slots, então **3 Forma** bastam para esta build.

### Build Steel Path — Bleed com arma de Slash

| Slot | Mod | Função |
|---|---|---|
| Aura | [[mods/warframe/corrosive_projection.md\|Corrosive Projection]] | Remoção de armadura é o gargalo do [[mecanicas/steel_path.md\|Steel Path]] — inimigo lá tem +250% de armadura |
| Exilus | [[mods/warframe/natural_talent.md\|Natural Talent]] | Conjuração rápida, para não morrer no meio da animação |
| 1 | [[mods/warframe/umbral_vitality.md\|Umbral Vitality]] | +440% Vida e sinergia Umbral |
| 2 | [[mods/warframe/adaptation.md\|Adaptation]] | Até +90% de resistência ao tipo de dano recebido. **Indispensável** num frame de 455 de vida |
| 3 | [[mods/warframe/rolling_guard.md\|Rolling Guard]] | Imunidade por 3 s ao rolar — a saída de emergência |
| 4 | [[mods/warframe/primed_continuity.md\|Primed Continuity]] | +55% Duração — Smoke Screen longo é a defesa real do Ash |
| 5 | [[mods/warframe/streamline.md\|Streamline]] | +30% Eficiência |
| 6 | [[mods/warframe/fleeting_expertise.md\|Fleeting Expertise]] | +60% Eficiência |
| 7 | [[mods/warframe/primed_flow.md\|Primed Flow]] | +150% Energia máxima |
| 8 | [[mods/warframe/umbral_intensify.md\|Umbral Intensify]] | +77% Força com o set Umbral completo |

**A ideia desta build é diferente:** no **[[mecanicas/steel_path.md|Steel Path]]** o dano dos clones de Blade Storm não acompanha a armadura inimiga. O que escala é a **passiva de Bleed**.

Então a build é de **sobrevivência + Eficiência**, e o dano vem da **arma**: uma arma de **Slash** alto com **[[mods/especiais/hunter_munitions.md|Hunter Munitions]]** ou **[[mods/especiais/hemorrhage.md|Hemorrhage]]** aplica Bleed, e o Ash o multiplica em **+25% de dano e +50% de duração**. Bleed é dano **que ignora armadura** — é por isso que funciona lá.

**Arcanos recomendados:** Arcane Energize (energia nos orbes) e Arcane Guardian (armadura). ⚠️ Nenhum dos dois tem arquivo próprio no vault.

**Prioridade de Forma:** as 3 do set Umbral consomem muita capacidade — conte **4 a 5 Forma** mais um **Orokin Reactor**, e use os **Umbral Forma** se tiver.


## 🧬 Helminth — Ash


| Item | Valor |
|---|---|
| Habilidade cedida ao Helminth | **Shuriken** — confirmada como `Subsumed` no `Module:Warframes/data` |
| Habilidade tática (Helminth) | **Smoke Screen** |
| Slot recomendado para substituição | **1 (Shuriken)** — é a habilidade mais dispensável dele numa build de Blade Storm |
| Subsumidas comuns neste frame | **Nourish** (Grendel) para dano e energia; **Eclipse** (Mirage) para dano; **Gloom** (Sevagoth) para controle. ⚠️ Nenhuma tem arquivo próprio no vault |

> [!note] Subsumir o Ash entrega o Shuriken
> Alimentar um Ash ao **[[mecanicas/helminth.md|Helminth]]** libera **Shuriken** para instalar em qualquer outro frame. Como o Ash é de **MR 0** e tem blueprint de 35.000 créditos no Mercado, ele é um dos frames mais baratos de farmar só para subsumir.


## 🔗 Sinergias e Uso — Ash


**Funciona bem em:**

- **[[missoes/tipos/exterminate.md|Exterminate]]** — Blade Storm limpa grupos a 50 m sem você se expor. É o uso natural do frame.
- **[[missoes/tipos/spy.md|Spy]]** — Smoke Screen dá invisibilidade sob demanda para passar por sensores, e Teleport atravessa vãos.
- **[[missoes/tipos/assassination.md|Assassination]]** — Teleport + Finisher ignora armadura, o que é exatamente o que um boss blindado não quer.
- **[[missoes/tipos/capture.md|Capture]]** e **[[missoes/tipos/rescue.md|Rescue]]** — missões curtas em que mobilidade e stealth valem mais que dano sustentado.
- **Farm de [[mecanicas/operator_e_focus.md|Focus]]** — a invisibilidade do Smoke Screen mantém o multiplicador de **[[mecanicas/stealth_e_finishers.md|stealth]]** (até 500% de afinidade), o que o torna uma opção boa em **Adaro**, em **[[locais/planetas/sedna.md|Sedna]]**.

**Evitar em:**

- **[[missoes/tipos/defense.md|Defense]]** e **[[missoes/tipos/mobile_defense.md|Mobile Defense]]** — Ash não protege nada. Ele não tem escudo de área, cura nem controle de multidão duradouro, e a invisibilidade não ajuda o pod.
- **[[missoes/tipos/interception.md|Interception]]** — Blade Storm mata um grupo por vez, não defende quatro pontos.
- **[[mecanicas/steel_path.md|Steel Path]] com build de Blade Storm** — o dano dos clones não acompanha a armadura de lá. Use a build de Bleed com arma, não a de habilidade.

**Sinergia de esquadrão:**

- **Qualquer frame que remova armadura** (Nezha com Augment, Hildryn, ou um aliado com **[[mods/warframe/corrosive_projection.md|Corrosive Projection]]**) multiplica o dano dos clones, que é dano físico direto.
- **Frames de energia** (Trinity com Energy Vampire, Harrow) resolvem o único limite real do Ash: energia. Mais energia = mais marcas.
- **Evite empilhar com outro frame de dano em área** — o Blade Storm perde o alvo se o aliado matar antes da execução, e a energia das marcas é gasta à toa.

**Armas que combinam:** o Ash quer **Slash** alto, porque a passiva dele multiplica Bleed. **[[armas/brancas/glaive_prime.md|Glaive Prime]]**, **[[armas/brancas/kronen_prime.md|Kronen Prime]]** e qualquer rifle com **[[mods/especiais/hunter_munitions.md|Hunter Munitions]]** aproveitam direto. Armas de puro **Impact** ou de dano elemental sem Slash **não** usam a passiva dele.


## 📖 História — Ash


> *"Behold the patron saint of the Orokin school of political assassination. Ash specializes in stealth. The edge of his blade is sooner felt than seen."* — Códice

Ash é o **assassino político** dos **[[lore/faccoes/orokin.md|Orokin]]**. A descrição do Códice é direta sobre isso: ele não foi feito para guerra aberta, foi feito para resolver problemas internos do império sem que ninguém visse. É um dos **frames originais** do jogo, disponível desde o lançamento.

O tema é declaradamente **ninja** — fumaça, shuriken, teleporte, execução. O que a ficção não esconde é o desconforto: diferente de um **[[warframes/regular/excalibur.md|Excalibur]]** ou de um **[[warframes/regular/rhino.md|Rhino]]**, que são soldados, o Ash é a ferramenta que os Orokin usavam **uns contra os outros**.


## 💡 Curiosidades — Ash


- **O `InternalName` do Ash é `/Lotus/Powersuits/Ninja/Ninja`.** O nome de desenvolvimento dele era literalmente "Ninja" — o tema veio antes do nome.
- **Blade Storm custa 0 de energia para ativar.** Toda a energia é gasta **por marca (12 cada)**. É por isso que Eficiência rende mais que Força numa build de Blade Storm, e por isso que o número de alvos, não o dano, é o limite da habilidade.
- **A fonte de drop dos componentes já mudou duas vezes:** Tyl Regor (até o Update 17.0, em 2015) → Manics (até o Update 29.10, em 2021) → missões de Railjack Proxima (hoje). É um dos frames com histórico de aquisição mais instável do jogo.

---
