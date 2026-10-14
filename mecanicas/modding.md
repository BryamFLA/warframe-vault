---
title: Modding (Mods, Capacidade e Polaridade)
aliases: [Modding, Mods, mod, modar, como modar, Mod Capacity, capacidade de mod, drenagem, drain, Fusion, fusão de mod, Transmutation, transmutar mod, Primed Mods, Flawed Mods, Exilus, Aura, Stance]
tipo: mecanica
resumo: "Mods são cartas instaladas no Arsenal que alteram stats; cada item tem 8 slots gerais (+Exilus/Aura/Stance), capacidade igual ao rank (até 30, dobrada por Orokin Reactor/Catalyst), polaridade igual corta a drenagem pela metade e a fusão com Endo segue 10 × raridade × (2^rank − 1)."
status: completo
rag: true
tags: [mecanica, mods, modding, capacidade, polaridade, fusao, endo, build]
fontes: ["https://wiki.warframe.com/w/Mod", "https://wiki.warframe.com/w/Endo"]
atualizado: 2026-10-14
verificado: true
agente: opus
---

# Modding (Mods, Capacidade e Polaridade)

> [!info] Em uma linha
> Mods são cartas instaladas no Arsenal que alteram stats do equipamento. A capacidade do item limita quantos cabem; polaridade e Forma reduzem a drenagem; a fusão com [[recursos/raridades/especial/endo.md|Endo]] e Credits sobe o rank do mod.

## ⚙️ Como Funciona — Modding

Mods são instalados no **Arsenal** do Orbiter (botão UPGRADE). Instalar e remover é **instantâneo e grátis**. Não é permitido instalar o mesmo mod duas vezes no mesmo item, nem duas variantes do mesmo mod (ex.: Flow + Primed Flow + Archon Flow são mutuamente exclusivos).

| Equipamento | Slots |
|---|---|
| Warframe | 8 gerais + 1 Exilus + 1 Aura (Jade tem 2 Aura) |
| Primária / Secundária | 8 gerais + 1 Exilus |
| Melee | 8 gerais + 1 Exilus + 1 Stance |
| Archgun, Archmelee, arma de Sentinel | 8 gerais |
| Companion | 10 gerais |
| Beast Claws | 8 gerais + 1 Posture |
| [[mecanicas/archwing.md\|Archwing]] e [[mecanicas/k_drive.md\|K-Drive]] | 8 gerais |
| [[mecanicas/necramech.md\|Necramech]] | 12 gerais |
| Tektolyst Artifact | 5 gerais |
| Parazon | 3 gerais + 3 especiais |
| Railjack (Plexus) | 8 gerais + Aura (Integrated) e 3 + 3 (Battle e Tactical) |

## 🔢 Fórmulas e Números — Modding

```
Capacidade do item = rank do item (normalmente 30; alguns itens vão a 40)
Com Orokin Reactor (Warframe/Companion/Archwing/K-Drive/Necramech) ou Orokin Catalyst (armas) = capacidade x 2
Capacidade mínima (item de rank baixo) = 15 + 1 a cada 2 Mastery Ranks   (MR 6 → 18; após MR 30, +1 por Legendary Rank)

Polaridade igual    → drenagem / 2, arredondada para cima   (Serration 14 → 7 em slot Madurai)
Polaridade diferente → drenagem + 25%, arredondada            (0–1: +0 · 2–5: +1 · 6–9: +2 · 10–13: +3 · 14–16: +4)
Aura / Stance / Posture → SOMAM capacidade: polaridade igual dobra o bônus; diferente tira 25%

Endo para fundir do rank 0 ao rank N = 10 × raridade × (2^N − 1)
   raridade: Common = 1 · Uncommon = 2 · Rare = 3 · Legendary = 4
Endo do rank N−1 para N = 10 × raridade × 2^(N−1)
```

| Endo total (do rank 0) | Rank 3 | Rank 5 | Rank 10 |
|---|---|---|---|
| Common | 70 | 310 | 10.230 |
| Uncommon / Peculiar | 140 | 620 | 20.460 |
| Rare / Riven / Amalgam / Galvanized | 210 | 930 | 30.690 |
| Legendary / Primed / Umbra / Archon | 280 | 1.240 | 40.920 |

- Mods Antique usam 160 × raridade × (2^N − 1).
- A fusão também custa Credits (cresce junto com o Endo). Um [[mods/especiais/legendary_core.md|Legendary Core]] maximiza qualquer mod sem custo de Endo/Credits.
- **Vender** um mod devolve 75% dos Credits investidos; **dissolver** devolve 75% do Endo investido. Rivens não podem ser vendidos.

As polaridades (Madurai, Vazarin, Naramon, Zenurik, Unairu, Penjaga, Umbra, Aura) e o uso de [[recursos/raridades/especial/forma.md|Forma]] estão em [[mecanicas/forma_e_polaridades.md|Forma e Polaridades]].

## 📋 Raridades e Variantes — Modding

| Raridade | Visual | Custo de fusão equivale a |
|---|---|---|
| Common | Bronze, 1 losango | Common |
| Uncommon | Prata, 2 losangos | Uncommon |
| Rare | Ouro, 3 losangos | Rare |
| Legendary | Platina, 4 losangos | Legendary |
| Riven, Amalgam, Galvanized, Requiem | Material próprio | Rare |
| Peculiar | Fumaça | Uncommon |
| Archon | Narmer, 5 losangos | Legendary |

| Variante | O que é | Como conseguir | Negociável? |
|---|---|---|---|
| Normal | Versão base | Drop de inimigo, missão, transmutação | ✅ |
| Flawed | Versão fraca, rank máx 3 | Caixa de mods perto de Cressa Tal em Iron Wake (desde o Update 34.0) | ❌ |
| Primed | Versão superior, rank máx 10, Legendary | [[mecanicas/baro_ki_teer.md\|Baro Ki'Teer]] (Ducats + Credits); 4 vêm do Daily Tribute | ✅ (exceto os do Tribute) |
| Primed do Daily Tribute | Primed Fury (200 dias), Primed Vigor (400), Primed Shred (600), Primed Sure Footed (900) | Login | ❌ |
| Umbra | Legendary + Set Umbral, polaridade Umbra (só com Umbra Forma) | Quest The Sacrifice e [[mecanicas/sindicatos/cephalon_simaris.md\|Cephalon Simaris]] | ❌ |
| Amalgam | Mods com efeito secundário em outro item | Evento Thermia Fractures e chefe Ropalolyst | ❌ (e não transmutáveis) |
| Galvanized | Stats base um pouco menores + bônus que acumula por kill, rank máx 10 | Arbitration Honors, 20 [[recursos/raridades/especial/vitus_essence.md\|Vitus Essence]] cada | ✅ |
| Archon | Mods de Warframe (ex.: Archon Stretch) com efeito extra ao usar habilidades, rank máx 10, custo de Legendary | Chipper, com Stock de Kahl's Garrison (rank 3 – Fort) | Não informado na fonte |

## 🎯 Como Conseguir — Modding

| Fonte | Detalhe |
|---|---|
| Drop de inimigo | Chance padrão de **3%** por inimigo (dobra com Mod Drop Booster e no [[mecanicas/steel_path.md\|Steel Path]]). Distribuição: 75,88% Common, 22,11% Uncommon, 2,01% Rare |
| Recompensa de missão | Missões não-endless e rotações de endless sorteiam mods, Endo ou Credits |
| Orokin Vault (Deimos) | Sempre dá um **Corrupted Mod** (ex.: Blind Rage, Overextended) |
| Nightmare Mode | Sempre dá um Nightmare Mod |
| [[mecanicas/sindicatos/_Sindicatos _Indice.md\|Sindicatos]] | Augment Mods de warframes e armas, comprados com Standing |
| [[mecanicas/nightwave.md\|Nightwave]] | Alguns Aura Mods na loja de Cred |
| Transmutation | 4 mods sem rank → 1 mod aleatório; 3 mods + 1 Transmutation Core → mod aleatório da polaridade escolhida |
| Requiem Relics | Requiem Mods (Oull cai de Kuva Lich / Sister) — ver [[mecanicas/reliquias_do_void.md\|Relíquias do Void]] |

## 💡 Dicas Práticas — Modding

- **Ordem de instalação importa** para mods elementais: elementos combinam da esquerda para a direita, de cima para baixo (ver [[mecanicas/dano_e_status.md|Dano e Status]]).
- **Quick Select** (a partir do MR 8) vende ou dissolve duplicatas em massa, sempre guardando 1 cópia e pulando mods ranqueados, Legendary e Riven.
- **Trading:** quem recebe Riven precisa de MR 8; mods Flawed, Umbra, Amalgam e Primed do Daily Tribute não são negociáveis ([[mecanicas/trading.md|Trading]]).
- Mods de Railjack ficam no Plexus, não no Arsenal ([[mecanicas/railjack.md|Railjack]]).

## 🔗 Relacionados — Modding

- [[mecanicas/endo_e_creditos.md|Endo e Credits]] — como farmar o que a fusão consome.
- [[mecanicas/rivens.md|Riven Mods]] — mods aleatórios por arma.
- [[mecanicas/arcanes.md|Arcanes]] — o "segundo sistema" de upgrade.
- [[mecanicas/forma_e_polaridades.md|Forma e Polaridades]], [[mecanicas/critico.md|Crítico]], [[mecanicas/dano_e_status.md|Dano e Status]], [[mods/_Mods _Indice.md|Índice de Mods]].

## 📚 Fontes — Modding

- https://wiki.warframe.com/w/Mod — slots, capacidade, polaridade, raridades, variantes, aquisição, ações (consultado em 2026-10-14)
- https://wiki.warframe.com/w/Endo — custos de fusão por raridade e fórmulas (consultado em 2026-10-14)
