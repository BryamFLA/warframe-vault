---
title: Parkour (Maneuvers)
tipo: mecanica
tags: [mecanica, parkour, movimento, bullet-jump, mobilidade]
atualizado: 2026-10-04
verificado: true
agente: opus
---

# Parkour (Maneuvers)

> [!info] Em uma linha
> Sistema de movimentação do Warframe — Bullet Jump, Aim Glide, Wall Dash, Roll e combinações — que é mais rápido que correr e é a principal defesa do jogo, já que inimigo não acerta quem está em movimento.

---

## 🧩 Como Funciona

Correr (Sprint) é o jeito **mais lento** de atravessar um mapa em Warframe. O movimento real é uma cadeia: **Bullet Jump → Aim Glide / Double Jump → Roll → Bullet Jump de novo**. O Bullet Jump sai a **14,5 m/s** de velocidade inicial, contra ~1,0 de Sprint Speed base da maioria dos frames, e pode ser repetido indefinidamente desde que você toque o chão, uma parede ou faça Wall Latch entre um e outro.

A regra que organiza todo o sistema é o **reset de manobra**: Roll no ar, Double Jump e Bullet Jump só podem ser feitos uma vez cada por "voo". Tocar o chão reseta — mas **Wall Dash e Wall Latch também resetam**, e são mais rápidos que descer até o chão. É isso que permite cadeias infinitas sem pousar.

Parkour também é defesa. **Roll reduz todo o dano recebido em 75%** (ou dá invulnerabilidade com Rolling Guard) e dá imunidade a knockdown durante a animação; Aim Glide reduz a precisão do inimigo; Bullet Jump deixa você fora de linha de tiro. Em conteúdo de alto nível isso vale mais que armadura.

---

## 🔢 Fórmulas e Números

```
Bullet Jump: velocidade inicial = 14,5 m/s
Bullet Jump: 100 de dano Blast com proc garantido, raio de 3 m, dano decai com a distância

Jump Kick: dano Impact = 20 + 100% do dano base da melee equipada (incluindo mods de dano base)
Jump Kick com Gale Kick = 20 + 200% do dano base da melee

Aim Glide: 3 s   (compartilha o timer com Wall Latch)
Aim Glide com Archgun deployado: duração reduzida em ~70% → 0,9 s
Wall Latch: 6 s  (compartilha o timer com Aim Glide)

Roll: -75% de todo o dano recebido durante a animação + imunidade a knockdown

Hard Landing: dispara ao cair a 20 m/s ou mais. Não causa dano, só travamento breve

Velocidade base andando: 6 m/s
Velocidade base em zipline: 7,5 m/s

Slam Jump (tech de comunidade): ~50 m/s
```

| Variável | Significado | Fonte do valor |
|---|---|---|
| 14,5 m/s | Velocidade inicial do Bullet Jump | Wiki, Maneuvers § Bullet Jump |
| 100 Blast / 3 m | Dano e raio do Bullet Jump, proc garantido | Wiki, Maneuvers § Bullet Jump |
| 3 s / 6 s | Aim Glide e Wall Latch, **mesmo timer** | Wiki, Maneuvers § Aim Glide e Wall Latch |
| 75% | Redução de dano do Roll | Wiki, Maneuvers § Rolling |
| 20 m/s | Velocidade de queda que dispara Hard Landing | Wiki, Maneuvers § Hard Landing |
| 70 ms | Janela para Knockdown Recovery (apertar jump ou roll) | Wiki, Maneuvers § Knockdown Recovery |
| 70° | Ângulo máximo de aproximação para Wall Dash **horizontal** | Wiki, Maneuvers § Wall Dash |

**Tetos e limites conhecidos:**

- Com **Archgun deployado**: Wall Latch fica **impossível** e Aim Glide cai para ~0,9 s.
- **Um Roll aéreo por voo.** Depois dele é preciso tocar chão, Wall Dash ou Wall Latch para rolar de novo no ar.
- **Bullet Jump não encadeia depois de Double Jump**, mas Double Jump encadeia depois de Bullet Jump.
- Mantling **não acontece durante cast de habilidade**, e pode ser cancelado com crouch/slide.
- Na zipline **não é possível castar habilidade nem usar melee** — só andar, correr, deslizar e atirar.
- **Nenhum dano de queda existe no jogo.** Hard Landing só trava o movimento por um instante.

---

## 📋 Tabelas de Referência

### As manobras e seus comandos

| Manobra | Comando (PC / controle) | O que faz |
|---|---|---|
| **Sprint** | Shift / L3 | Corre. Atirar cancela; algumas melee podem ser usadas correndo. Pode virar toggle em Acessibilidade ("Hold to Sprint") |
| **Roll (Dodge)** | Tocar Sprint | −75% de dano, imunidade a knockdown, tira Latcher/Maggot/Leech, dispela esporos de Swarm Mutalist MOA e Banish indesejado, nega onda de fogo de Arson Eximus, evita Hard Landing |
| **Sidespring** | Aim + lateral + tocar Sprint | Rolamento lateral curto; serve pela redução de dano |
| **Backspring** | Aim + trás + tocar Sprint | Handspring para trás mantendo a orientação. No ar não precisa de Aim |
| **Crouch** | Ctrl / L1 | Reduz hitbox, ajuda stealth. Toggle no V |
| **Slide** | Em movimento + Crouch | Crouch andando. Para gradualmente por atrito, exceto em rampas. Melee durante slide = Slide Attack |
| **Jump Kick** | No ar em movimento + Crouch | Mantém momento, derruba a maioria dos inimigos, dano Impact puro. Pousa em slide |
| **Jump** | Espaço | Pulo básico |
| **Double Jump** | No ar + Jump | Carrega o momento atual. Tocar qualquer superfície recarrega |
| **Bullet Jump** | Crouch + Jump | 14,5 m/s na direção da mira, 100 Blast em 3 m. Funciona a partir do slide |
| **Aim Glide** | No ar + Aim | Planeio controlado de 3 s. Funciona bloqueando com melee ou castando habilidade. Reduz a precisão inimiga |
| **Mantling** | Aproximar da borda + Jump | Agarra e sobe a borda. Double Jump durante o mantle acelera a subida |
| **Wall Dash vertical** | Correr perpendicular à parede + Jump | Sobe a parede. Segurar Jump continua indefinidamente. Quanto maior o Sprint Speed, mais rápido sobe |
| **Wall Dash horizontal** | Correr a menos de 70° da parede + Jump | Atravessa a parede lateralmente, com a mesma regra de continuidade |
| **Wall Latch** | Durante Wall Dash + Aim | Para grudado na parede por 6 s. Permite castar habilidades que normalmente não funcionam no ar. Evita Hard Landing |
| **Zipline** | X perto da linha | Monta de qualquer ponto, inclusive no ar. Velocidade sobe de 6 para 7,5 m/s; Aim não aplica o debuff de velocidade |
| **Knockdown Recovery** | Jump ou Roll na janela de 70 ms | Levanta rápido. O brilho que sinaliza a janela está bugado e não aparece, mas a janela existe |

### Técnicas avançadas (vocabulário de comunidade, não oficial)

| Técnica | Comando | Detalhe |
|---|---|---|
| **Bullet Roll** | Crouch + tocar Shift e Espaço juntos | Conta como Bullet Jump **e** Roll ao mesmo tempo: pega bônus dos dois e dispara Rolling Guard e Motus Setup. Direção fica entre a mira e o eixo horizontal, permitindo ângulos que o Roll sozinho não alcança. Dá 2 stacks de Arcane Double Back. Passiva do Chroma permite 2 Bullet Rolls seguidos. Difícil ou impossível no controle |
| **Slam Jump** | No ar + E + flick da câmera para baixo | Explora o momento do Melee Slam para disparar na direção da FOV inicial a ~50 m/s. Melee rápido demais = ataque aéreo normal; melee tarde = slam normal. Funciona pilotando Necramech e com o Kahl de jetpack. **Não funciona com Glaive** |
| **Slam Cancel** | No ar + Melee Slam + tocar Shift | Roll cronometrado para sair da animação de slam antes dos frames finais, que zeram o momento. A janela encurta conforme a velocidade de ataque aumenta |
| **Roll Slide** | Tocar Sprint + Crouch em qualquer direção | Slide durante o Roll, para ajuste fino de direção |
| **Roll Pickup** | Tocar Sprint + X sobre o item | Pega item sem travar na animação. Vale para datamass de Mobile Defense e célula de Excavation |

### Sprint Speed por Warframe

| Sprint Speed | Warframes |
|---|---|
| 0,90 | Atlas, Qorvex |
| 0,95 | Follie, Frost (e Prime), Grendel (e Prime), Rhino, Saryn, Sevagoth (e Prime), Voruna |
| 1,00 | Atlas Prime, Chroma (e Prime), Citrine (e Prime), Excalibur (Prime, Umbra), Garuda (e Prime), Gyre, Harrow (e Prime), Hildryn, Inaros, Jade, Koumei, Mag (e Prime), Nidus (e Prime), Oberon (e Prime), Oraxia, Revenant, Rhino Prime, Saryn Prime, Styanax (e Prime), Temple, Titania (e Prime), Trinity, Vauban (e Prime), Volt (e Prime), Wukong, Yareli |
| 1,02 | Xaku |
| 1,05 | Gyre Prime, Hildryn Prime, Hydroid (e Prime), Inaros Prime, Khora (e Prime), Octavia (e Prime), Wukong Prime |
| 1,07 | Xaku Prime |
| 1,10 | Banshee, Caliban (e Prime), Cyte-09, Dagath, Ember (e Prime), Kullervo, Mesa (e Prime), Narin, Nekros (e Prime), Nyx, Revenant Prime, Trinity Prime, Uriel, Valkyr (e Prime), Yareli Prime, Zephyr |
| 1,125 | Nyx Prime |
| 1,15 | Ash, Banshee Prime, Dante, Equinox (e Prime), Gara (e Prime), Ivara, Lavos (e Prime), Limbo (e Prime), Nezha, Sirius & Orion, Zephyr Prime |
| 1,20 | Ash Prime, Baruuk (e Prime), Ivara Prime, Mirage (e Prime), Nezha Prime, Nova (e Prime), Protea (e Prime), Voruna Prime, Wisp |
| 1,25 | Loki (e Prime), Nokko, Wisp Prime |
| **1,40** | **Gauss** |
| **1,50** | **Gauss Prime** |

### Os quatro stats de mobilidade (não se confundem)

| Stat | O que afeta |
|---|---|
| **Sprint Speed** | Só a velocidade de corrida. Mods: [[mods/warframe/rush.md\|Rush]], Armored Agility, Speed Drift |
| **Parkour Velocity** | Distância e velocidade de Bullet Jump, Roll e slide. Mods: [[mods/warframe/mobilize.md\|Mobilize]], Hit And Run, Lightning Dash, Piercing Step. Também o **Amber Archon Shard** (+15% / +22,5%) |
| **Aim Glide / Wall Latch Duration** | Só a duração dessas duas manobras. Mods: Aerodynamic, Patagium, Stealth Drift, Piercing Step, Rending Turn, Toxic Flight, Ice Spring, Firewalker, Lightning Dash, Mobilize, Battering Maneuver, Nira's Anguish, Boreal's Anguish |
| **Dodge Speed** | Só a velocidade de Roll, Sidespring e Backspring. Única fonte de mod: **Amalgam Barrel Diffusion**. Também a passiva do Mirage |
| **Movement Speed** | Velocidade de animação de manobras que **não** são sprint. Mods: Agile Aim, Dispatch Overdrive, Snap Shot, Spry Sights. Habilidades: Jet Stream, Escape Velocity, Razorwing Blitz, Infiltrate (agachado ou em zipline) |
| **Mobility** | Stat **exclusivo do Conclave** (PvP): multiplicador de velocidade de Bullet Jump, slide e atrito de slide |

---

## 🛠️ Como Explorar na Prática

| Objetivo | O que fazer |
|---|---|
| Atravessar mapa no menor tempo | Bullet Jump → Aim Glide → Roll → tocar parede (Wall Dash reseta tudo) → Bullet Jump. Nunca correr em linha reta |
| Sobreviver a nuke de Eximus | Roll no momento do hit: **−75% de dano** e imunidade a knockdown. Com [[mods/warframe/rolling_guard.md\|Rolling Guard]] vira invulnerabilidade com reset de status |
| Evitar Hard Landing | Double Jump, Jump Kick, Roll **ou** Aim Glide pouco antes de tocar o chão. **Kavat's Grace** mitiga de forma passiva |
| Subir parede alta | Wall Dash vertical segurando Jump. Frame com Sprint Speed alto sobe mais rápido — Gauss Prime (1,5) é o mais rápido do jogo |
| Castar habilidade "de solo" no ar | **Wall Latch**: algumas habilidades que não podem ser castadas no ar funcionam grudado na parede |
| Pegar datamass sem travar | Roll por cima dela segurando o botão de interagir — **Roll Pickup** ignora a animação de pickup |
| Quebrar grade / ventilador | **Bullet Jump** quebra no **início** do voo (100 Blast em 3 m); **Jump Kick** quebra no **fim** do voo (20 + 100% do dano base da melee, ou + 200% com Gale Kick) |
| Build de velocidade pura | [[mods/warframe/rush.md\|Rush]] (Sprint Speed) + [[mods/warframe/mobilize.md\|Mobilize]] (Parkour Velocity) + [[mods/armas/barrel_diffusion.md\|Amalgam Barrel Diffusion]] (Dodge Speed) são os três stats diferentes — um não substitui o outro |
| Encadear 2 Bullet Rolls | Só com a passiva do Chroma |
| Zipline mais rápido | Correr e deslizar na linha; Aim **não** aplica debuff de velocidade em zipline |

**Mods que interagem:** [[mods/warframe/rush.md|Rush]] e Armored Agility (Sprint Speed); [[mods/warframe/mobilize.md|Mobilize]], Hit And Run, Lightning Dash e Piercing Step (Parkour Velocity); Aerodynamic, Patagium e Stealth Drift (duração de Aim Glide/Wall Latch); [[mods/armas/barrel_diffusion.md|Amalgam Barrel Diffusion]] (única fonte de Dodge Speed); [[mods/warframe/rolling_guard.md|Rolling Guard]] (invulnerabilidade + limpa status ao rolar); Kavat's Grace (mitiga Hard Landing); Gale Kick (dobra o dano do Jump Kick); [[mods/warframe/aviator.md|Aviator]] (redução de dano no ar); Motus Setup, Motus Impact e Motus Signal (bônus ao fazer manobras); Melee Careen (10 stacks de Cold ao rolar); [[mods/warframe/handspring.md|Handspring]] — **cuidado**: acelera a animação de knockdown e por isso **encurta** a janela de recuperação, dificultando o recovery manual.

> [!warning] Handspring é contraintuitivo
> [[mods/warframe/handspring.md|Handspring]] **acelera** a animação de knockdown, o que **reduz** a janela de 70 ms do Knockdown Recovery. Para quem usa o recovery manual, equipar Handspring piora.

**Frames que interagem:** [[warframes/regular/gauss.md|Gauss]] e [[warframes/primes/gauss_prime.md|Gauss Prime]] (1,4 e 1,5 de Sprint Speed, os mais rápidos), [[warframes/regular/volt.md|Volt]] (Speed é **multiplicativo** com outros buffs de velocidade), [[warframes/regular/titania.md|Titania]] (Razorwing e Razorwing Blitz), [[warframes/regular/wisp.md|Wisp]] (Breach Surge e mote de velocidade), [[warframes/regular/chroma.md|Chroma]] (passiva permite 2 Bullet Rolls seguidos), [[warframes/regular/mirage.md|Mirage]] (passiva aumenta Dodge Speed), [[warframes/regular/zephyr.md|Zephyr]] (controle aéreo), [[warframes/regular/nezha.md|Nezha]] (Fire Walker, subsumível), [[warframes/regular/yareli.md|Yareli]] (Merulina como veículo).

---

## ⚠️ Erros Comuns

- **"Sprint Speed e Parkour Velocity são a mesma coisa."** São stats separados. Rush não aumenta a distância do Bullet Jump; Mobilize não aumenta a velocidade de corrida.
- **"Existe dano de queda."** Não existe. Cair de qualquer altura só gera Hard Landing — um travamento breve, zero dano.
- **"Preciso tocar o chão para resetar o Bullet Jump."** Wall Dash e Wall Latch também resetam, e costumam ser mais rápidos.
- **"Aim Glide dura 3 s sempre."** Com Archgun deployado cai para ~0,9 s, e o timer é **compartilhado** com o Wall Latch — gastar um gasta o outro.
- **"Handspring ajuda a levantar."** Equipar Handspring **encurta** a janela de recuperação manual de 70 ms.
- **"Roll não protege de verdade."** Protege 75% do dano recebido e dá imunidade a knockdown — é a mitigação mais acessível do jogo, disponível em qualquer frame sem mod.
- **"Mobility é um stat normal."** É exclusivo do [[mecanicas/sindicatos/conclave.md|Conclave]] (PvP) e não existe no PvE.
- **"Bullet Jump pode ser feito depois de Double Jump."** Não. A ordem válida é Bullet Jump → Double Jump, nunca o contrário.
- **"Slam Jump é oficial."** É terminologia de comunidade; a wiki marca a seção como não-oficial. O comportamento existe, o nome não é da Digital Extremes.

---

## 🔗 Mecânicas Relacionadas

- [[mecanicas/stealth_e_finishers.md|Stealth e Finishers]] — Crouch reduz hitbox e ajuda stealth; Roll e Wall Latch posicionam para Finisher.
- [[mecanicas/combo_counter.md|Combo Counter]] — Slide Attack e ataques aéreos alimentam o contador; Slam Cancel preserva momento entre slams.
- [[mecanicas/dano_e_status.md|Dano e Status]] — Bullet Jump aplica proc garantido de Blast; Jump Kick aplica Impact puro.
- [[mecanicas/forma_e_polaridades.md|Forma e Polaridades]] — mods de mobilidade são quase todos **Exilus**, e o slot Exilus exige Exilus Warframe Adapter.
- [[mecanicas/helminth.md|Helminth]] — Infested Mobility (+60% de sprint e +30% de parkour velocity) e o Amber Archon Shard (+15% / +22,5% de Parkour Velocity).
- [[mecanicas/sindicatos/conclave.md|Conclave]] — onde o stat Mobility existe e onde o parkour define o combate.
- [[mecanicas/steel_path.md|The Steel Path]] — com inimigo a 250% de vida e escudo, não ser acertado vale mais que tanque; parkour é a defesa principal.
- [[mecanicas/mastery_rank.md|Mastery Rank]] — os testes de MR 8 (Wall Dash), 10 e 13 (Disappearing Platform), 11 (Time Trial) e 12 (Carousel) são testes de parkour.

---

## 📚 Fontes
- https://wiki.warframe.com/w/Maneuvers — lista completa de manobras e comandos, velocidade do Bullet Jump, dano e raio, durações de Aim Glide e Wall Latch, redução de dano do Roll, Hard Landing, zipline, Knockdown Recovery, técnicas avançadas, tabela de Sprint Speed por Warframe, os stats de mobilidade e suas fontes (consultado em 2026-10-04)
