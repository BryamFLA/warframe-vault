---
title: Helminth
aliases: [Helminth, infundir habilidade, subsumir, subsume, sala do helminth, trocar habilidade de warframe]
tipo: mecanica
resumo: "Criatura Infestada na Helminth Infirmary da Orbiter que come recursos, converte em Secretions e permite trocar uma habilidade de qualquer Warframe por outra, aplicar Archon Shards e injetar buffs semanais (Invigoration)."
status: completo
rag: true
tags: [mecanica, helminth, subsume, archon-shard, invigoration, orbiter]
fontes: ["https://wiki.warframe.com/w/Helminth", "https://wiki.warframe.com/w/Archon_Shard"]
atualizado: 2026-10-07
verificado: true
agente: opus
---

# Helminth

> [!info] Em uma linha
> Criatura Infestada na Helminth Infirmary da Orbiter que come recursos, converte em Secretions e permite trocar uma habilidade de qualquer Warframe por outra, aplicar Archon Shards e injetar buffs semanais (Invigoration).


## ⚙️ Como Funciona — Helminth


O Helminth é um ser Infestado que mora na **Helminth Infirmary** da Orbiter, responsável pelas "funções biológicas" da nave — o reparo dos Warframes nos bastidores. Primeira aparição no Update 19.5 (2016-12-22), mas só virou sistema jogável no Update 29.0 (2020-08-25). Você interage sentando o Warframe equipado na cadeira no centro da sala.

O ciclo é sempre o mesmo: **alimente o Helminth com recursos → ele converte em Secretions → você gasta Secretions em funções**. Existem 7 tipos de Secretion (Bile, Biotics, Calx, Oxides, Pheromones, Synthetics e Sentient Appetite), cada um alimentado por um conjunto fixo de recursos. Cada Secretion vai de 0% a 100%, e tudo que excede 100% é **desperdiçado**.

As quatro funções são: **Subsume** (devorar um Warframe para aprender uma de suas habilidades), **Infusion** (substituir uma habilidade de outro frame pela habilidade aprendida), **Invigoration** (buffs temporários semanais) e **Archon Shards** (bônus permanentes de stat). Cada uma exige um Segment próprio instalado.


## 🔢 Fórmulas e Números — Helminth


### Desbloqueio dos Segments

| Segment | Onde pegar o blueprint | Requisito | Custo do BP | Função |
|---|---|---|---|---|
| **Helminth Segment** | Son, no Necralisk (Deimos) | Mastery Rank 8 + Rank 3 "Associate" com [[mecanicas/sindicatos/entrati.md\|Entrati]] | 15.000 Standing | Subsume + Infusion |
| **Helminth Invigoration Segment** | Son, no Necralisk | Mastery Rank 8 + Rank 5 "Family" com Entrati | 30.000 Standing | Invigoration |
| **Helminth Archon Shard Segment** | Recompensa da quest **Veilbreaker** | Concluir Veilbreaker | — | Archon Shards |
| **Helminth Coalescent Segment** | Bird 3, no Sanctum Anatomica | Rank 2 "Researcher" com [[mecanicas/sindicatos/cavia.md\|Cavia]] | 30.000 Standing | Fusão de Shards |

Todos custam **50.000 Credits + 24 h de forja**, rush por 50 Platinum. Os três primeiros também vêm prontos no Market dentro do **Helminth Segments Bundle por 300 Platinum**.

> Antes de ter o Helminth Segment, a Infirmary só abre equipando [[warframes/regular/nidus.md|Nidus]] / [[warframes/primes/nidus_prime.md|Nidus Prime]] ou carregando um **Helminth Cyst** pego de outro jogador. O cisto é puramente cosmético, cresce em 24 h e matura em 7 dias; drenar um cisto maduro durante a incubação de um Kubrow gera o companheiro **Helminth Charger**. Novo cisto nasce 24 h após drenar.

### Conversão de recurso em Secretion

```
Secretion ganho = valor base do recurso x taxa de apetite atual

Apetite "gosta"   (seta verde)    → até  30%   (máximo)
Apetite neutro    (sem seta)      →       15%   (mediana)
Apetite "não gosta" (seta vermelha) →      7%
Apetite "odeia"                    → até   3%   (mínimo)

Recuperação de apetite: 24 h do vermelho total até neutro
                      + 24 h do neutro até verde total
```

| Variável | Significado | Fonte do valor |
|---|---|---|
| 30% / 15% / 7% / 3% | Taxa de conversão por nível de apetite | Wiki, seção Secretions |
| 100% | Teto absoluto de qualquer Secretion; excesso é perdido | Wiki, seção Secretions |
| 2x | **Lucent Teroglobe** (→ Calx), **Pustulite** e **Ganglion** (→ Biotics) sempre dão o dobro, podendo chegar a 60% com apetite verde | Wiki, seção Secretions |
| 50% da barra | Quanto um recurso de **Sentient Appetite** restaura do apetite do recurso mais odiado (desbloqueado no rank 8 de Metamorphosis) | Wiki, seções Secretions e Metamorphosis |

**Tetos e limites conhecidos:**

- Um Warframe só pode ter **uma habilidade substituída por configuração de mod** (config A, B, C podem ter habilidades diferentes).
- Uma habilidade infundida **ocupa sempre o mesmo slot** em todas as configs em que foi infundida. Para mudar o slot, é preciso remover e reinfundir, **pagando o Secretion de novo** (nunca é devolvido).
- O mesmo Warframe **não pode ser subsumido duas vezes**.
- Só **um Warframe por vez** pode estar em processo de Subsume. Demora **23 horas**; rush por 50 Platinum.
- Só **Warframes não-Prime e não-Umbra** podem ser subsumidos. Passivas nunca são subsumíveis.
- Só **uma habilidade do próprio Helminth** por config, e ela conta como a substituição — não dá para ter uma habilidade Helminth e uma habilidade subsumida de frame na mesma config.
- **5 slots de Archon Shard** por Warframe.

### Metamorphosis — ranks e desbloqueios

| Rank | XP do rank anterior | XP acumulado | Desbloqueia |
|---|---|---|---|
| 0 | 0 | 0 | Habilidades **Empower**, **Infested Mobility**, **Master's Summons** |
| 1 | 2.250 | 2.250 | **Subsume de Warframes** + 3 slots de subsume |
| 2 | 3.375 | 5.625 | Habilidade **Rebuild Shields** |
| 3 | 4.500 | 10.125 | Habilidade **Perspicacity** |
| 4 | 5.625 | 15.750 | 10 slots de subsume |
| 5 | 6.750 | 22.500 | Habilidade **Energized Munitions** |
| 6 | 7.875 | 30.375 | Habilidade **Marked For Death** |
| 7 | 9.000 | 39.375 | 20 slots de subsume |
| 8 | 10.125 | 49.500 | **Sentient Appetite** (restaurar apetite) |
| 9 | 11.250 | 60.750 | Habilidade **Expedite Suffering** |
| 10 | 12.375 | 73.125 | **Unbound Subsume** — slots ilimitados |
| 11 | 13.500 | 86.625 | Habilidade **Parasitic Armor** |
| 12 | 14.625 | 101.250 | Habilidade **Hideous Resistance** |
| 13 | 15.750 | 117.000 | Habilidade **Voracious Metastasis** |
| 14 | 16.875 | 133.875 | Habilidade **Sickening Pulse** |
| 15 | 18.000 | 151.875 | Habilidade **Golden Instinct** |

### Como ganhar XP de Metamorphosis

| Atividade | XP |
|---|---|
| Subsumir um Warframe | 1.600 |
| Infundir uma habilidade | 8 XP por 1% de material usado |
| Alimentar o Helminth | ~6,66 XP por 1% de material ganho — 200 XP se gosta (30%), 100 XP neutro (15%), 46 XP se não gosta (7%), 20 XP se odeia (3%) |
| Injetar uma Invigoration | 4.800 |


## 📋 Tabelas de Referência — Helminth


### Recursos por tipo de Secretion

| Secretion | Recursos aceitos (quantidade por alimentação) |
|---|---|
| **Bile** | 350 Aggristone · 250 Ariette Scale · 900 Antiserum Injector Fragment · 3 Argon Crystal · 3.000 Cryotic · 5 Diluted Thermia · 800 Efervon Sample · 7 Enigma Gyrum · 450 Ignia · 200 Isos · 7 Javlok Capacitor · 120 Maphica · 40 Morphics · 65 Nav Coordinate · 30 Omega Isotope · 5 Orokin Cipher · 75 Rune Marrow · 10 Somatic Fibers · 50 Thermal Sludge · 5.000 Ticor Plate · 40 Vainthorn · 55 Vessel Capillaries · 10 Voidgel Orb |
| **Biotics** | 35 Connla Sprout · 75 Dracroot · 8 Dusklight Sarracenia · 35 Eevani · 8 Frostleaf · 50 Ganglion (2x) · 25 Gorgaricus Spore · 700 Höllvanian Pitchweave Fragment · 150 Kovnik · 8 Lunar Pitcher · 50 Maprico · 8 Moonlight Dragonlily · 8 Moonlight Jadeleaf · 8 Moonlight Threshcone · 8 Mytocardia Spore · 25 Nistlepod · 25 Pustulite (2x) · 8 Ruk's Claw · 40 Scuttler Husk · 35 Silphsela · 8 Sunlight Dragonlily · 8 Sunlight Jadeleaf · 8 Sunlight Threshcone · 35 Tasoma Extract · 50 Tepa Nodule · 35 Ueymag · 8 Vestan Moss · 35 Yao Shrub |
| **Calx** | 300 Asterite · 250 Belric Crystal Fragment · 7.000 Cubic Diodes · 45 Fate Pearl · 40 Fergolyte · 175 Gallos Rods · 30 Grokdrul · 300 Hexenon · 50 Iradite · 50 Lucent Teroglobe (2x) · 80 Nacreous Pebble · 50 Nullstones · 250 Rania Crystal Fragment · 6.000 Rubedo · 180 Stela · 145 Temporal Dust |
| **Oxides** | 1.000 Agnovidisc · 15.000 Alloy Plate · 2.500 Carbides · 45.000 Entrati Obols · 20.000 Ferrite · 25 Gallium · 775 Laudavi · 10 Maw Fang · 750 Oxium · 20.000 Salvage · 110 Servoris · 10 Tellurium · 10.000 Titanium |
| **Pheromones** | 35 Beating Heartstrings · 3 Chitinous Husk · 3 Infected Palpators · 150 Lamentus · 125 Mutagen Sample · 20.000 Nano Spores · 15 Neurodes · 4.000 Plastids · 3 Pulsating Tubercles · 3 Severed Bile Sac · 300 Techrot Chitin · 25 Techrot Motherboard · 50 Thrax Plasm · 20 Lua Thrax Plasm |
| **Synthetics** | 6 Atmo Systems · 10 Aucrux Capacitors · 7.000 Circuits · 75 Control Module · 30 Cryptographic ALU · 125 Detonite Ampule · 5 Entrati Lanthorn · 65 Experimental Arc-Relay · 125 Fieldron Sample · 12 Gyromag Systems · 15 Komms · 800 Necracoil · 25 Neural Sensors · 15 Orokin Cell · 12.500 Polymer Bundle · 3 Repeller Systems · 200 Saggen Pearl |
| **Sentient Appetite** | 2 Anomaly Shard · 5 Cetus Wisp · 75 Intact Sentient Core · 10 Exceptional Sentient Core · 5 Flawless Sentient Core · 10 Eidolon Shard |

### Habilidades subsumíveis — qual frame dá qual habilidade

| Warframe | Habilidade subsumida | Augment aplicável | Papel |
|---|---|---|---|
| Ash | Shuriken | Seeking Shuriken | Armor Strip, Slash |
| Atlas | Petrify | Ore Gaze | Crowd Control, farm (inimigos petrificados não dropam Rubble) |
| Banshee | Silence | Savage Silence | Debuff de dano, desativa habilidade inimiga, stealth |
| Baruuk | Lull | Endless Lullaby | Crowd Control, stealth (Sleep) |
| Caliban | Sentient Wrath | — | CC, debuff. **ALTERADO:** só cone frontal, sem status Tau |
| Chroma | Elemental Ward | Everlasting Ward | Vida/escudo/armadura/reload. Elemento definido pela cor de emissão primária |
| Citrine | Fractured Blast | — | CC, cura, energia. **ALTERADO:** dano 125/150/200/250, orb de vida 25%, orb de energia 10% |
| Cyte-09 | Evade | — | Cura, invisibilidade. **ALTERADO:** duração base 15 s, teto 25 s |
| Dagath | Wyrd Scythes | — | CC, dano Viral. **ALTERADO:** slow reduzido a 15/18/22/26% |
| Dante | Dark Verse | — | Dano Slash + Stagger |
| Ember | Fire Blast | Healing Flame, Purifying Flames | Armor strip (teto de 75% por cast), cura. **ALTERADO:** Healing Flame cura 37 e não dá Overguard |
| Equinox | Rest & Rage | Calm & Frenzy | CC, debuff, stealth. Versão definida pela cor de emissão primária |
| Excalibur | Radial Blind | Radiant Finish | Crowd Control (Blind) |
| Follie | Self Portrait | — | Redução de dano. **ALTERADO:** teto de 75%, sem Inkblot nos inimigos |
| Frost | Ice Wave | Ice Wave Impedance | Crowd Control (Cold) |
| Gara | Spectrorage | Spectrosiphon | Crowd Control, energia |
| Garuda | Blood Altar | — | Cura, CC |
| Gauss | Thermal Sunder | — | Dano Heat/Cold, CC |
| Grendel | Nourish | — | Buff de dano Viral, energia, cura |
| Gyre | Coil Horizon | — | CC, dano Elétrico |
| Harrow | Condemn | — | CC, escudo. **Trava Acolytes por completo** |
| Hildryn | Pillage | — | Strip de armadura **e** escudo, escudo para si |
| Hydroid | Tempest Barrage | — | CC, dano |
| Inaros | Desiccation | — | Blind, cura |
| Ivara | Quiver | Empowered Quiver | Invisibilidade (Cloak Arrow), CC |
| Jade | Ophanim Eyes | — | Buff de squad |
| Khora | Ensnare | — | CC. **Trava Acolytes por completo** |
| Koumei | Omamori | — | Mitigação |
| Kullervo | Wrathful Advance | — | Mobilidade, buff de crítico |
| Lavos | Vial Rush | — | Mobilidade, status |
| Limbo | Banish | — | CC, Rift |
| Loki | Decoy | — | CC, aggro |
| Mag | Pull | — | CC, pickup à distância |
| Mesa | Shooting Gallery | — | Buff de dano de arma, CC |
| Mirage | Eclipse | Total Eclipse | Buff de dano / redução de dano. **Restrito** (ver abaixo) |
| Nekros | Terrify | — | Armor strip, CC |
| Nezha | Fire Walker | — | Velocidade, Heat, limpa status |
| Nidus | Larva | Larva Burst | CC por agrupamento |
| Nokko | Brightbonnet | — | Suporte |
| Nova | Null Star | — | Redução de dano, CC |
| Nyx | Mind Control | Mind Freak | CC. Psychic Bolts **não** é a habilidade subsumível de Nyx |
| Oberon | Smite | Smite Infusion | Dano, buff elemental |
| Octavia | Resonator | — | CC |
| Oraxia | Webbed Embrace | — | CC |
| Protea | Dispensary | — | Energia, vida, munição |
| Qorvex | Chyrinka Pillar | — | Dano Radiation, CC |
| Revenant | Reave | — | Cura, drenagem |
| Rhino | Roar | — | Buff de dano. **Restrito** (ver abaixo) |
| Saryn | Molt | — | Velocidade, aggro |
| Sevagoth | Gloom | — | Slow, cura |
| Sirius & Orion | Jade Stars / Astral Shell | — | Suporte |
| Styanax | Tharros Strike | Tharros Lethality | **Strip de armadura e escudo** + cura |
| Temple | Pyrotechnics | — | Dano |
| Titania | Spellbind | Spellbound Harvest | CC, imunidade a status |
| Trinity | Well of Life | — | Cura |
| Uriel | Remedium | — | Cura |
| Valkyr | Warcry | — | Velocidade de ataque, armadura, slow |
| Vauban | Tesla Nervos | — | CC, dano Elétrico |
| Volt | Shock | Shock Trooper | Dano Elétrico, buff elemental |
| Voruna | Lycath's Hunt | — | Farm de loot |
| Wisp | Breach Surge | — | Blind, dano por eco |
| Wukong | Defy | — | Invulnerabilidade, armadura |
| Xaku | Xata's Whisper | — | Buff de dano Void. **Restrito** (ver abaixo) |
| Yareli | Aquablades | — | Dano Slash |
| Zephyr | Airburst | — | CC |

> [!warning] Restrição de buff de dano
> **Eclipse**, **Roar** e **Xata's Whisper** só podem substituir uma habilidade específica, e só nos frames que já têm uma habilidade de buff de dano: Vex Armor (Chroma), Resupply (Cyte-09), Eclipse (Mirage), Amp (Octavia), Silken Stride (Oraxia), Roar (Rhino), Ripper's Wail (Temple), Demonium (Uriel), Xata's Whisper (Xaku). Nenhuma outra habilidade nem nenhum outro frame tem restrição — Shooting Gallery ou Smite Infusion, por exemplo, podem ir em qualquer slot de qualquer frame, inclusive junto do Vex Armor do Chroma.

**Custo de Secretions:** varia por habilidade. Exemplos verificados — Ash: subsumir custa Calx 50% + Pheromones 77% + Bile 80%, injetar custa Oxides 51% + Biotics 38% + Synthetics 17% (848 XP). Atlas: subsumir Oxides 75% + Synthetics 57% + Bile 80%, injetar Calx 19% + Biotics 19% + Pheromones 60% (784 XP). A faixa típica é **~48–85% em três Secretions para subsumir** e **~10–77% em três Secretions para injetar**. Os valores exatos de cada habilidade estão na tabela "Subsumable Ability Checklist" da wiki.

### Habilidades próprias do Helminth

| Habilidade | Energia | Efeito (rank 0 → 3) | Rank de Metamorphosis |
|---|---|---|---|
| **Empower** | 25 | +20/30/40/50% de Força de Habilidade **aditiva** no próximo cast. Dura indefinidamente até ser consumida. Não pode ser recastada ativa, não afeta a si mesma | 0 |
| **Infested Mobility** | 50 | +35/45/50/60% de velocidade de sprint e +15/20/25/30% de parkour velocity, por 5/6/7/8 s. Não afeta velocidade de caminhada | 0 |
| **Master's Summons** | 50 | Restaura 25/50/75/100% da vida e escudo do Companion e o teleporta para seu lado de qualquer distância. Revive companion incapacitado. **Não afeta Venari** | 0 |
| **Rebuild Shields** | 50 | Restaura 25/50/75/100% do escudo máximo. Cooldown de **12 s**. Não restaura escudo do companion. Funciona na Hildryn | 2 |
| **Perspicacity** | 25 | 100% de chance de auto-breach no próximo hack. Funciona em Nightmare, Sortie e Archon Hunt. **Só funciona como Warframe, não como Operator** | 3 |
| **Energized Munitions** | 50 | +75% de eficiência de munição por 3/3,5/4/5 s — consome 1 munição a cada 4 tiros. Multiplicativo com outras fontes de eficiência de munição | 5 |
| **Marked For Death** | 50 | Stuna 1 alvo em 15/20/25/30 m e marca; 35/45/60/75% do próximo dano (incluindo crítico e status) é replicado em todos os inimigos em linha de visão até 7/8/9/10 m. Teto de dano replicado: **150%** | 6 |
| **Expedite Suffering** | ⚠️ NÃO VERIFICADO | Condensa todos os status de Slash e Toxin do alvo em uma única instância | 9 |
| **Parasitic Armor** | ⚠️ NÃO VERIFICADO | Sacrifica escudo para converter em armadura por um tempo | 11 |
| **Hideous Resistance** | ⚠️ NÃO VERIFICADO | Imunidade a status | 12 |
| **Voracious Metastasis** | ⚠️ NÃO VERIFICADO | Consome energia para se curar e dar energia equivalente a cada aliado | 13 |
| **Sickening Pulse** | ⚠️ NÃO VERIFICADO | Pulso que adiciona stacks a status já existentes; soma o dano de Slash, Heat e Toxin numa nova instância com timer renovado | 14 |
| **Golden Instinct** | ⚠️ NÃO VERIFICADO | Void Spark que aponta para o Medallion, Ayatan Sculpture, caixa rara, Kuria ou Fragment mais próximo | 15 |

Mods de Duração, Eficiência e Força funcionam normalmente em todas elas.

### Invigoration

| Item | Detalhe |
|---|---|
| Quando | **3 Warframes aleatórios por semana**, começando segunda-feira às 0:00 UTC |
| Duração do buff | **7 dias** |
| O que cada um recebe | 1 buff de ofensiva + 1 buff de utilidade, ambos sorteados |
| Custo | Dois tipos de Secretion, entre **20% e 90%** cada, sorteados a cada vez |
| Override | Após **10 Invigorations aplicadas**, aparece o botão "Override Warframe", que troca um dos 3 sorteados pelo frame equipado. Permite até **4 frames invigorados** na semana. Usar o override zera o contador |
| Limite | Um frame não recebe uma segunda Invigoration enquanto a primeira está ativa |

| Buffs de ofensiva | Buffs de utilidade |
|---|---|
| Duração de Habilidade +100%\* | Armadura +1000^ |
| Alcance de Habilidade +100%\* | Energia Máxima +200%‡\* |
| Força de Habilidade +200%\* | Regeneração de Energia +2‡^ |
| Crítico de Primária +200%† | Vida +1000^ |
| Dano de Primária +250%†\* | Regeneração de Vida +25/s^ |
| Crítico de Secundária +200%†\* | Jump Resets 5 (4 pulos no ar) |
| Dano de Secundária +250%†\* | Velocidade de Sprint +75%\* |
| Crítico de Melee +200%†\* | Parkour Velocity +75%\* |
| Dano de Melee +250%†\* | Eficiência de Habilidade +75%\* |
| | Velocidade de Reload +75%\* |
| | Imunidade a Status (inclui resistir knockdown de inimigo e de arma explosiva) |

† Afeta Exalted Weapons da classe correspondente (buff de primária afeta Artemis Bow; de secundária afeta Balefire Charger).
‡ Não vale para Hildryn nem Lavos (não usam Energia).
\* Soma aditivamente com bônus do mesmo tipo.
^ Valor fixo aplicado depois de todos os outros bônus.

### Archon Shards

5 slots por Warframe. Cada Shard dá **uma** escolha entre 5 stats — e o mesmo bônus pode ser escolhido de novo com outro Shard da mesma cor. **Tauforged** dá **1,5x** o valor normal.

**Desocupar um Shard** devolve o Shard e custa Secretion: **15%** (ou **30%** se Tauforged), no tipo ligado à cor — Crimson→Oxides, Amber→Bile, Azure→Synthetics, Emerald→Biotics, Topaz→Pheromones, Violet→Calx.

| Cor | Bônus disponíveis (normal / Tauforged) |
|---|---|
| **Crimson** | +25% / +37,5% Dano Crítico de Melee · +25% / +37,5% Chance de Status de Primária · +25% / +37,5% Crítico de Secundária · +10% / +15% Força de Habilidade · +10% / +15% Duração de Habilidade |
| **Amber** | +30% / +45% da Energia máxima preenchida ao spawnar · +100% / +150% de eficácia de Health Orbs · +50% / +75% de eficácia de Energy Orbs · +25% / +37,5% Velocidade de Cast · +15% / +22,5% Parkour Velocity |
| **Azure** | +150 / +225 Vida máxima · +150 / +225 Escudo · +50 / +75 Energia máxima (não vale Hildryn/Lavos) · +150 / +225 Armadura · +5 / +7,5 Vida/s |
| **Emerald** | Status de Toxin faz +30% / +45% mais dano · Recupera +2 / +3 de Vida por inimigo afetado por Toxin · +10% / +15% de Ability Damage em inimigo com Corrosion · +2 / +3 no teto de stacks de Corrosion |
| **Topaz** | +1 / +2 de Vida máxima por abate com Blast (teto 300 / 450) · +5 / +7,5 de Escudo por abate com Blast · +1% / +1,5% de Crítico de Secundária por abate em inimigo com Heat (teto 50% / 75%) · +10% / +15% de Ability Damage em inimigo com Radiation |
| **Violet** | +10% / +15% de Ability Damage em inimigo com Electricity · +30% / +45% de Electricity na Primária, +10% / +15% adicional por Shard Crimson, Azure ou Violet equipado · +25% / +37,5% de Dano Crítico de Melee, **dobrado** se a Energia máxima passar de 500 (501+) · Health pickup dá +20% / +30% de Energia e Energy pickup dá +20% / +30% de Vida |

**Observações importantes sobre Shards:**
- O bônus de **Ability Damage** é um modificador único, só existe em Archon Shard. É **multiplicativo** com a Força de Habilidade e **não** se aplica a Exalted Weapons. Só vale se o inimigo **já tinha** o status antes de ser atingido pela habilidade.
- Bônus de Ability Damage de Shards diferentes somam entre si, independente da cor: 2 Violet + 1 Topaz, contra inimigo com Electricity **e** Radiation, dá 30% (20% + 10%).
- O bônus de **+150/+225 de Escudo** não serve para Inaros, Kullervo e Nidus (não têm escudo).
- O bônus de **Corrosion acima de 10 stacks** só vale para Corrosion aplicada pelas suas próprias habilidades e armas — não cria debuff que permita outros excederem 10.
- O teto de Crítico de Secundária do Topaz **soma por Shard**: 1 Tauforged + 1 normal = +2,5% por abate, teto de 125%.

**Fusão (Helminth Coalescent Segment):**

| Tipo | Custo | Resultado |
|---|---|---|
| Coalescent Fusion | 50 Stela | Crimson + Azure = **Violet** · Crimson + Amber = **Topaz** · Amber + Azure = **Emerald** |
| Ascent Fusion | 100 Stela | 3 Shards da mesma cor = **1 Tauforged** da mesma cor |

Normal só funde com normal; Tauforged só com Tauforged (gerando Tauforged). As duas fusões são **permanentes e irreversíveis** — o jogo pede para digitar CONFIRM.


## 🛠️ Como Usar na Prática — Helminth


| Objetivo | O que fazer |
|---|---|
| Resolver escudo de 250% no [[mecanicas/steel_path.md\|Steel Path]] | Subsumir **Styanax** (Tharros Strike) ou **Hildryn** (Pillage) — as duas removem armadura **e** escudo. Tharros Strike também cura |
| Travar Acolyte | Subsumir **Harrow** (Condemn) ou **Khora** (Ensnare): imobilizam Acolyte por completo |
| Resolver falta de energia em qualquer frame | Subsumir **Protea** (Dispensary) — gera orbe de energia, vida e munição no chão |
| Buff de dano universal | **Roar** (Rhino) ou **Eclipse** (Mirage) — mas ambos são **restritos** à lista acima. Para frames fora da lista, use **Nourish** (Grendel, buff Viral + energia) ou **Shooting Gallery** (Mesa) |
| Sobreviver com frame de papel | 5 Azure Shards: +750 de Vida e +750 de Armadura (ou +1125 cada com Tauforged) |
| Build de crítico de melee | Crimson (+25% Dano Crítico cada) ou Violet (+25%, dobrando para +50% com Energia máxima acima de 500 — combine com Primed Flow) |
| Não desperdiçar Secretion | Nunca alimente passando de 100%. Alimente **variando os recursos**: dar um recurso que o Helminth gosta e depois um neutro/odiado aumenta levemente a conversão do primeiro |
| Recuperar apetite rápido | Sentient Appetite (rank 8 de Metamorphosis): 1 recurso Sentient restaura 50% da barra do recurso mais odiado |
| Subir Metamorphosis rápido | Invigoration é o maior ganho único: **4.800 XP** por injeção, contra 1.600 por subsume |
| Gerar Helminth Charger | Pegar o cisto com Nidus, esperar 7 dias de maturação, drenar durante a incubação de um Kubrow |
| Testar habilidade sem perder o frame | Não existe teste. Infusion é reversível, mas o Secretion gasto **não volta** — pesquise antes |

**Mods que interagem:** [[mods/warframe/energy_conversion.md|Energy Conversion]] funciona de modo parecido com Empower (bônus aditivo de Força no próximo cast). Augments de habilidade funcionam nas habilidades infundidas, mas alguns dependem de outras habilidades do frame original e podem não funcionar.

**Frames que interagem:** [[warframes/regular/nidus.md|Nidus]] (único jeito de abrir a Infirmary antes do Segment), [[warframes/regular/hildryn.md|Hildryn]] e [[warframes/regular/styanax.md|Styanax]] (strip de armadura+escudo), [[warframes/regular/harrow.md|Harrow]] e [[warframes/regular/khora.md|Khora]] (travar Acolyte), [[warframes/regular/protea.md|Protea]] (Dispensary), [[warframes/regular/grendel.md|Grendel]] (Nourish), [[warframes/regular/rhino.md|Rhino]] e [[warframes/regular/mirage.md|Mirage]] (buffs restritos), [[warframes/regular/inaros.md|Inaros]] e [[warframes/regular/kullervo.md|Kullervo]] (não aproveitam Shard de escudo).


## ⚠️ Erros Comuns — Helminth


- **"Vou subsumir meu Prime para liberar slot."** Impossível. Só **não-Prime e não-Umbra** podem ser subsumidos. E o frame é **destruído permanentemente** — a Mastery dele você mantém, mas o frame some do inventário.
- **"Nyx dá Psychic Bolts."** Não. Nyx dá **Mind Control**. Psychic Bolts, a habilidade que todo mundo quer para Steel Path, **não é subsumível**.
- **"Infusion é de graça se eu desistir."** Remover é reversível, mas o Secretion gasto **nunca volta**. Trocar o slot em que a habilidade mora também exige remover e reinfundir, pagando de novo.
- **"Posso ter Roar em qualquer frame."** Não. Eclipse, Roar e Xata's Whisper só entram em 9 frames específicos, e sempre substituindo a habilidade de buff de dano que o frame já tem.
- **"Mais Secretion é sempre melhor."** Qualquer Secretion acima de **100%** é jogado fora. Alimentar um recurso que o Helminth odeia rende 3% — vale mais esperar 48 h o apetite voltar ao verde do que torrar 20.000 Nano Spores por 3%.
- **"Tauforged é 2x."** É **1,5x**, não 2x.
- **"O cisto do Helminth é um debuff."** É puramente cosmético, e é o único caminho para o companion Helminth Charger.
- **"Ability Damage do Shard é igual a Força de Habilidade."** Não. É um modificador separado, **multiplicativo** com a Força, que só ativa se o inimigo **já tinha** o status antes do hit, e **não** afeta Exalted Weapons.
- **"Posso pôr duas habilidades infundidas no mesmo frame."** Uma por configuração de mod. Configs diferentes podem ter habilidades diferentes — é assim que se tem "duas", trocando de config.
- **"Invigoration eu escolho."** Não, é sorteio. Só depois de 10 Invigorations você ganha **um** Override para forçar o frame equipado.


## 🔗 Relacionados — Helminth


- [[mecanicas/steel_path.md|The Steel Path]] — Tharros Strike, Pillage e Condemn subsumidos são a resposta direta ao escudo de 250%; Archon Shards cobrem a sobrevivência.
- [[mecanicas/forma_e_polaridades.md|Forma e Polaridades]] — habilidade infundida não muda polaridade de slot, mas builds de Força/Duração para a habilidade nova geralmente exigem repolarizar.
- [[mecanicas/augments.md|Augments]] — quais augments funcionam em habilidade infundida e quais quebram fora do frame original.
- [[mecanicas/forja.md|Forja]] — os 4 Segments são itens de forja (50.000 Credits, 24 h cada).
- [[mecanicas/sindicatos/entrati.md|Entrati]] — Rank 3 para o Helminth Segment, Rank 5 para o Invigoration Segment, ambos com Son no Necralisk.
- [[mecanicas/sindicatos/cavia.md|Cavia]] — Rank 2 para o Coalescent Segment com Bird 3.
- [[mecanicas/dano_e_status.md|Dano e Status]] — os Shards Emerald, Topaz e Violet são condicionados a Toxin, Corrosion, Blast, Heat, Radiation e Electricity.
- [[mecanicas/critico.md|Crítico]] — Crimson, Topaz e Violet mexem diretamente em chance e dano crítico.
- [[mecanicas/platinum.md|Platinum]] — Helminth Segments Bundle (300 pl), rush de subsume e de forja (50 pl cada).
- [[missoes/tipos/archon_hunt.md|Archon Hunt]] — a fonte principal de Archon Shards.
- [[missoes/jornadas/principais/veilbreaker.md|Veilbreaker]] — a quest que libera o Archon Shard Segment.
- [[missoes/jornadas/principais/heart_of_deimos.md|Heart of Deimos]] — abre o Necralisk e o sindicato Entrati, pré-requisito prático para tudo isso.
- [[companheiros/_Companheiros _Indice.md|Companheiros]] — Helminth Charger, gerado pelo cisto.

---
