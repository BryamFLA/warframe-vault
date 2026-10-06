---
title: Arbitrations
aliases: [Arbitrations]
tipo: mecanica
resumo: "Arbitrations — Variante \"elite\" de Alert hospedada pelos Arbiters of Hexis: só missões endless a partir do nível 60–80, sem bleedout e sem auto-revive, com Shield Drones que tornam inimigos invulneráveis, pagando em Vitus Essence."
status: completo
rag: true
tags: [mecanica, arbitration, endgame, vitus-essence, arbiters-of-hexis]
fontes: ["https://wiki.warframe.com/w/Arbitrations"]
atualizado: 2026-10-07
verificado: true
agente: opus
---

# Arbitrations

> [!info] Em uma linha
> Variante "elite" de Alert hospedada pelos Arbiters of Hexis: só missões endless a partir do nível 60–80, **sem bleedout e sem auto-revive**, com Shield Drones que tornam inimigos invulneráveis, pagando em Vitus Essence.


## ⚙️ Como Funciona — Arbitrations


Arbitrations (Update 23.10, 2018-10-12) destravam quando você **tem acesso a Plutão** e completa a tarefa da **Eris Junction "Equip a Focus Lens"**. Depois disso aparecem na janela de Operation. Existe **uma única Arbitration ativa por vez** no Star Chart, trocando de nó **a cada hora**.

A seleção só pega nós de missão **endless**: Alchemy, Defection, Defense, Disruption, Excavation, Infested Salvage, Interception, Mirror Defense, Survival / Conjunction Survival, Void Cascade, Void Flood e Void Armageddon. O nível inimigo começa em **60–80**.

A regra que define o modo é a morte: **não existe bleedout**. Zerar a vida mata na hora, e **você não pode se reviver**. Para voltar, um aliado precisa levar **5 Resurgence Tokens** até a Revive Tower que nasce no local da sua morte — e carregar token aplica o debuff **Resurgence Burden**, que reduz vida e escudo máximos e drena energia continuamente.


## 🔢 Fórmulas e Números — Arbitrations


```
Nível inicial do inimigo = 60-80
Troca de nó = a cada 1 hora
Rotação de recompensa = A A B B C C C C ...  (endless no C após as 4 primeiras)

Tokens para reviver 1 jogador morto = 5
  Não precisam estar no mesmo Warframe: a soma de 5 tem de chegar
  à Revive Tower ao mesmo tempo
  Morrer carregando tokens = perde TODOS os tokens carregados
  Tokens NÃO são afetados por Vacuum nem Fetch

Bônus de alerta (sorteados por jogador, por alerta):
  1 Warframe aleatório  → +300% Força de Habilidade e +500 de Vida
  3 Armas aleatórias    → +300% de Dano

Vitus Essence = 1 por rotação concluída
  + 6% de chance de drop por Arbitration Shield Drone (despawna em 5 min)
Credits de conclusão = 50.000
```

| Variável | Significado | Fonte do valor |
|---|---|---|
| 60–80 | Faixa de nível inicial | Wiki, Arbitrations § Mechanics |
| 1 hora | Intervalo de troca de nó | Wiki, Arbitrations § Mechanics |
| AABBCCCC… | Rotação de recompensa (diferente do AABC normal) | Wiki, Arbitrations § Rewards |
| 5 tokens | Custo de 1 revive | Wiki, Arbitrations § Rules |
| +300% / +500 / +300% | Bônus de Força, Vida e Dano dos itens sorteados | Wiki, Arbitrations § Bonuses |
| 6% | Chance de Vitus Essence por Drone | Wiki, Arbitrations § Rewards |
| 50.000 Credits | Recompensa fixa de conclusão | Wiki, Arbitrations § Rewards |
| 3.000 Blast | Dano da explosão do Drone ao morrer (escala com o nível) | Wiki, Arbitration Shield Drones |

**Tetos e limites conhecidos:**

- **Requisito de entrada:** Warframe no rank 30, **ou** jogador MR 30 com o Warframe polarizado pelo menos uma vez (mesma regra de [[missoes/tipos/sortie.md\|Sortie]]).
- **Máximo de Drones em campo por tamanho de squad:** 1 / 2 / 2 / 3 para 1 / 2 / 3 / 4 jogadores.
- **Vida dos Drones escala com o squad:** +50% / +100% / +200% com 2 / 3 / 4 jogadores.
- **Sair da missão não dá recompensa nenhuma. Falhar a missão mantém** o que já foi ganho no fim de cada rotação — mas não os recursos e Credits dropados por inimigos.
- O bônus de alerta vale até para **Warframe e arma que você não possui**, e se estende a **todas as variantes** (Prime, Syndicate etc.).


## 📋 Tabelas de Referência — Arbitrations


### O que funciona e o que não funciona (sem bleedout)

| ❌ Não funciona em Arbitration | ✅ Funciona normalmente |
|---|---|
| Sacrifice (Arcane) | Nidus — passiva Adaptive Mutation |
| Inaros — passiva Undying | Wukong — passiva Five Levels of Immortality |
| Sevagoth — passiva Tombstone | Inaros — **Negation Armor** |
| Nokko — passiva Vital Decay | Loki — **Savior Decoy** |
| Unairu — **Last Gasp** | Oberon — **Phoenix Renewal** |
| | Khora — **Venari Bodyguard** |
| | Sirius — Light's Sanctuary |
| | Protea — **Temporal Anchor** |
| | Dagath — Grave Spirit |
| | Trinity — Well of Life |
| | Arcane Escapist · Emergence Savior |

> A regra geral: **só funciona o que impede a entrada no bleedout**, nunca o que atua durante o bleedout. Incapacitação e auto-revive de **Companion** funcionam normalmente.

### Modificadores por tipo de missão

| Missão | O que muda |
|---|---|
| **Excavation** | Tempo de escavação sobe de **100 s para 180 s**, e são necessárias **2 escavações** para 1 rodada de recompensa |
| **Survival** | Life Support Capsule vale **75%** do normal |
| **Interception** | Torres inimigas enchem **2x mais rápido** |
| **Defense** | O objetivo é um **Hexis Operative** NPC armado com Telos Akbolto, que **segue um jogador escolhido** (não vagueia) e não pode receber arma. Downtime entre ondas cai para **2 s**. O Operative **não entra em bleedout** — a morte dele é **falha imediata**. Ele **não tem Shield Gate**, então só se beneficia de recarga de escudo (delay e velocidade), nunca de shield gating. Exceção: no tileset Grineer Sealab ele fica preso à área de um dos 4 cryopods, trocando a cada onda |
| **Defection** | Alvos de resgate **não podem ser revividos** |
| **Infested Salvage** | Consoles têm **15x** a vida normal, mas **não regeneram** com Vaporizer Bubble |
| **Disruption** | Alcance do bipe do Demolyst/Demolisher é **metade**, e eles só são marcados a **15 m** (em vez de 30 m) |

### Arbitration Shield Drone

| Item | Detalhe |
|---|---|
| Função | Amarra-se a inimigos num raio de **10 m**, dando **invulnerabilidade total** e dispelando habilidades |
| Marca visual | Inimigo amarrado ganha **aura magenta** |
| Imunidades | Imune à maioria das habilidades, Exalted Weapons e Status Effects |
| Shield Gate | **Não tem** |
| Máximo em campo | 1 / 2 / 2 / 3 (squad de 1 / 2 / 3 / 4) |
| Vida por squad | +50% / +100% / +200% (squad de 2 / 3 / 4) |
| Morte | Explode causando **3.000 de Blast** em inimigos próximos, inclusive em outros Drones. O dano escala com o nível |
| Overguard | **Não** recebe de Ancient Protector, mas **recebe armadura** de Swarm Mutalist MOA |
| Bug conhecido | Trava com frequência em escadas e beiradas |

### Recompensas por rotação

Rotação **AABBCCCC…** — após as 4 primeiras rotações, continua em **C indefinidamente**.

| Rotação | Recompensa | Chance |
|---|---|---|
| **A** | Endo x900 | 44% |
| A | Ayatan Ayr Sculpture | 9% |
| A | Ayatan Sah Sculpture | 9% |
| A | Ayatan Valana Sculpture | 9% |
| A | Vitus Essence x3 | 7% |
| A | Arcane Blade Charger | 5% |
| A | Arcane Bodyguard | 5% |
| A | Arcane Primary Charger | 5% |
| A | Arcane Pistoleer | 5% |
| **B** | Endo x1.200 | 44,5% |
| B | Ayatan Piv Sculpture | 12% |
| B | Ayatan Vaya Sculpture | 12% |
| B | Vitus Essence x3 | 7% |
| B | Arcane Blade Charger | 5% |
| B | Arcane Bodyguard | 5% |
| B | Arcane Pistoleer | 5% |
| **C** | Endo x1.500 | 35% |
| C | Ayatan Orta Sculpture | 20% |
| C | Vitus Essence x3 | 10% |
| C | Arcane Blade Charger | 5% |
| C | Arcane Primary Charger | 5% |
| C | Arcane Tanker | 5% |

> Em **Excavation** a recompensa sai a cada **2 escavações**. Em **Disruption** a tier segue o sistema padrão de Disruption (rodada + conduits defendidos), sem alteração.

### Arbitration Honors — loja de Vitus Essence

Fica na sala dos [[mecanicas/sindicatos/arbiters_of_hexis.md\|Arbiters of Hexis]] em qualquer Relay. **A disponibilidade não depende da sua reputação com o sindicato.**

| Custo em Vitus Essence | Itens |
|---|---|
| **5** | Vitus Emblem |
| **10** | Ayatan Amber Star Blueprint · Arcane Pistoleer · Arcane Tanker · Arcane Bodyguard · Arcane Blade Charger · Arcane Primary Charger |
| **15** | Vitus Illumina · Arbitration Statue · Vitus Essence Decoration · Amprex Telos Skin · Atomos Telos Skin · Atterax Telos Skin |
| **20** | Scars of Arbitration Sigil · **Sharpshooter** · **Cautious Shot** · **Power Donation** · **Vigorous Swap** · **Rolling Guard** · **Adaptation** · **Combat Discipline** · **Melee Guidance** · **Swift Momentum** · todas as 12 **Galvanized** (Acceleration, Aptitude, Chamber, Crosshairs, Diffusion, Hell, Savvy, Scope, Shot, Steel, Reflex, Elementalist) |
| **25** | 10.000 Kuva · Grendel Chassis Locator · Grendel Neuroptics Locator · Grendel Systems Locator |
| **30** | **Preparation** · **Aerial Ace** · **Mending Shot** · **Energizing Shot** · **Aerodynamic** · **Shepherd** · Bleeding Body Ephemera · Blazing Step Ephemera · Seeding Step Ephemera · Judicial Coils · Judicial Oculus |
| **35** | Archgun Riven Mod |
| **50** | Ayatan Zambuka Sculpture |
| **75** | Illumina Judicium |


## 🛠️ Como Usar na Prática — Arbitrations


| Objetivo | O que fazer |
|---|---|
| Farmar Endo em volume | É a melhor fonte do jogo: 900 / 1.200 / **1.500 Endo** por rotação, com 35–44% de chance, mais as Ayatan Sculptures. Depois da 4ª rotação você fica em C para sempre |
| Pegar as Galvanized | Todas as 12 custam **20 Vitus Essence** cada na loja dos Arbiters. São os mods que substituem Serration e companhia em build de alto nível |
| Pegar o Grendel | Os 3 Locators (Chassis, Neuroptics, Systems) custam **25 Vitus Essence** cada — a rota sem RNG |
| Sobreviver sem bleedout | O que vale é **não entrar** no bleedout: [[mods/warframe/adaptation.md\|Adaptation]], [[mods/warframe/rolling_guard.md\|Rolling Guard]], shield gating, Negation Armor (Inaros), Phoenix Renewal (Oberon), Venari Bodyguard (Khora), Temporal Anchor (Protea) |
| Lidar com os Drones | Mate o **Drone**, não o inimigo amarrado — o inimigo é invulnerável até o Drone cair. Drones são imunes à maioria das habilidades: use **arma**. E saia de perto: a explosão faz 3.000 de Blast |
| Jogar solo é mais fácil | **Sim, nesse aspecto:** só **1 Drone** em campo e sem bônus de vida nele. Com 4 jogadores são 3 Drones com **+200% de vida** |
| Aproveitar o bônus do alerta | +300% de Força de Habilidade e +500 de Vida no frame sorteado, e +300% de Dano nas 3 armas sorteadas. Vale até para itens que você **não tem** — e para qualquer variante deles |
| Reviver um aliado | Precisa de **5 Resurgence Tokens** entregues ao mesmo tempo na Revive Tower. **Vacuum e Fetch não pegam** — tem de passar por cima. E se quem carrega morrer, os tokens somem |
| Falhar sem perder tudo | **Nunca saia** da missão (perde tudo). **Falhar** mantém as recompensas de rotação já ganhas |
| Defense em Arbitration | O Hexis Operative morre de verdade e é falha imediata. Ele **não tem Shield Gate** — build de recarga de escudo e cura em área (Oberon, Trinity) vale mais que shield gating |

**Mods que interagem:** [[mods/warframe/adaptation.md|Adaptation]] e [[mods/warframe/rolling_guard.md|Rolling Guard]] são os dois mods centrais do modo (os dois comprados aqui mesmo por 20 Vitus Essence). [[mods/warframe/combat_discipline.md|Combat Discipline]] também vem desta loja. [[mods/companheiros/vacuum.md|Vacuum]] e [[mods/companheiros/fetch.md|Fetch]] **não** pegam Resurgence Token.

**Frames que interagem:** [[warframes/regular/inaros.md|Inaros]] (Negation Armor funciona, a passiva Undying **não**), [[warframes/regular/oberon.md|Oberon]] (Phoenix Renewal), [[warframes/regular/khora.md|Khora]] (Venari Bodyguard), [[warframes/regular/protea.md|Protea]] (Temporal Anchor), [[warframes/regular/nidus.md|Nidus]] (Adaptive Mutation), [[warframes/regular/wukong.md|Wukong]] (Five Levels of Immortality), [[warframes/regular/loki.md|Loki]] (Savior Decoy), [[warframes/regular/trinity.md|Trinity]] (Well of Life), [[warframes/regular/sevagoth.md|Sevagoth]] e [[warframes/regular/nokko.md|Nokko]] (passivas de auto-revive **desativadas**).


## ⚠️ Erros Comuns — Arbitrations


- **"É igual ao Steel Path."** São dois eixos diferentes. Arbitration exige o **Star Chart normal** (acesso a Plutão + Eris Junction), não o Steel Path, e o que a torna difícil é a **morte instantânea** e os Drones, não um multiplicador de vida.
- **"Meu Inaros é imortal aqui."** A passiva Undying **não funciona**. Negation Armor funciona. Mesma lógica em Sevagoth e Nokko.
- **"Last Gasp me salva."** Não funciona em Arbitration — é a Way-Bound da Unairu justamente desativada aqui.
- **"Vacuum pega os tokens."** Não pega. Nem Fetch. Resurgence Token tem de ser pego passando por cima.
- **"Vou matar o inimigo com aura magenta."** Ele é **invulnerável** enquanto o Drone estiver amarrado. Mate o Drone.
- **"Habilidade resolve o Drone."** Drones são imunes à maioria das habilidades, a Exalted Weapons e a status. Use arma comum.
- **"Squad grande é mais fácil."** Mais jogadores = **mais Drones** (até 3) com **+200% de vida**. A dificuldade escala contra você.
- **"Sair da missão guarda o que peguei."** Sair dá **zero**. Falhar guarda o que foi ganho no fim de cada rotação.
- **"A rotação é AABC."** Em Arbitration é **AABBCCCC…** — depois da 4ª rotação você fica em C para sempre, que é a melhor.
- **"Preciso de reputação com os Arbiters para comprar."** Não. A loja de Arbitration Honors ignora sua reputação com o sindicato.
- **"Excavation rende igual."** Cada escavação leva **180 s** em vez de 100, e são **2 escavações** por recompensa.


## 🔗 Relacionados — Arbitrations


- [[mecanicas/steel_path.md|The Steel Path]] — o outro pilar de dificuldade; exige o Star Chart completo, não Plutão + Eris Junction.
- [[mecanicas/sindicatos/arbiters_of_hexis.md|Arbiters of Hexis]] — quem hospeda o modo e onde fica a loja de Vitus Essence.
- [[mecanicas/mastery_rank.md|Mastery Rank]] — o requisito de frame rank 30 é furado no MR 30 com o frame polarizado uma vez.
- [[mecanicas/operator_e_focus.md|Operator e Focus]] — a tarefa da Eris Junction que destranca Arbitration é "Equip a Focus Lens", e Last Gasp (Unairu) não funciona aqui.
- [[mecanicas/dano_e_status.md|Dano e Status]] — Drones são imunes à maioria dos status, o que inverte a lógica de build do resto do jogo.
- [[mecanicas/forma_e_polaridades.md|Forma e Polaridades]] — as Galvanized compradas aqui costumam exigir repolarização da build.
- [[mecanicas/augments.md|Augments]] — a loja vende mods de utilidade (Power Donation, Vigorous Swap, Swift Momentum) que não existem em outro lugar.
- [[missoes/tipos/arbitration.md|Arbitration (tipo de missão)]] — a ficha do ponto de vista de missão.
- [[missoes/tipos/sortie.md|Sortie]] — mesmo requisito de frame rank 30, dificuldade e recompensa diferentes.
- [[missoes/tipos/defense.md|Defense]], [[missoes/tipos/excavation.md|Excavation]], [[missoes/tipos/survival.md|Survival]], [[missoes/tipos/interception.md|Interception]], [[missoes/tipos/disruption.md|Disruption]], [[missoes/tipos/defection.md|Defection]], [[missoes/tipos/infested_salvage.md|Infested Salvage]], [[missoes/tipos/void_cascade.md|Void Cascade]], [[missoes/tipos/void_flood.md|Void Flood]], [[missoes/tipos/void_armageddon.md|Void Armageddon]] — os tipos elegíveis, cada um com seu modificador.
- [[recursos/raridades/especial/endo.md|Endo]] e [[recursos/raridades/especial/ayatan_sculpture.md|Ayatan Sculpture]] — a razão econômica de jogar Arbitration.
- [[locais/planetas/eris.md|Eris]] e [[locais/planetas/plutao.md|Plutão]] — os dois requisitos de desbloqueio.

---
