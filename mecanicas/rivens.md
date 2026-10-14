---
title: Riven Mods
aliases: [Riven, Rivens, Riven Mod, riven mod, mod riven, disposition, disposição de riven, reroll, rolar riven, cycle riven, Veiled Riven, riven velado, Riven Transmuter, Riven Sliver, Riven Splicer, trait lock]
tipo: mecanica
resumo: "Riven Mods são mods aleatórios presos a uma arma: chegam velados (desafio para revelar), têm 2–3 bônus e talvez 1 penalidade, força ditada pela Disposition da arma (0,5–1,55) e atributos rerroláveis com Kuva (900 a 3.500 por ciclo)."
status: completo
rag: true
tags: [mecanica, mods, riven, kuva, disposition, endgame, trading]
fontes: ["https://wiki.warframe.com/w/Riven_Mods", "https://wiki.warframe.com/w/Endo"]
atualizado: 2026-10-14
verificado: true
agente: opus
---

# Riven Mods

> [!info] Em uma linha
> Riven é um mod aleatório preso a **uma** arma (e suas variantes). Chega velado, você cumpre um desafio para revelar, e depois pode rerrolar os atributos com [[recursos/raridades/raro/kuva.md|Kuva]]. A força dos números depende da **Disposition** da arma.

## ⚙️ Como Funciona — Riven Mods

| Propriedade | Regra |
|---|---|
| Atributos | 2 ou 3 bônus, podendo ter 1 negativo (o negativo aumenta os bônus) |
| Polaridade | Madurai, Naramon ou Vazarin, aleatória e fixa |
| Mastery Rank para usar | Próprio do mod, entre **8 e 16** |
| Arma | 1 arma e suas variantes, fixa |
| Limite | 1 Riven por arma |
| Rank máximo e fusão | Rank máx **8** (o exemplo da página de Endo usa Riven no rank máximo = 2^8); custo de fusão e taxa de trade iguais aos de mod Rare: 10 × 3 × (2^8 − 1) = **7.650 Endo** do rank 0 ao 8 |
| Slots de inventário | 15 iniciais; +1 por 20 platinum ou +3 por 60, até 180; MR 30 dá +30 (total 210) |
| Venda | Não pode ser vendido por Credits; pode ser dissolvido em Endo |

### Estados

| Estado | O que acontece |
|---|---|
| **???** (não aberto) | Não ocupa slot de Riven |
| **Veiled** (equipado) | Mostra o desafio; ocupa slot; não dá bônus; não pode ser ranqueado. Só entra em arma da mesma classe (Rifle → primária não-shotgun; Shotgun → shotgun; Pistol → secundária; Melee/Zaw → melee; Kitgun → primária ou secundária) |
| **Unveiled** | Revela arma, stats, polaridade e MR; pode ser ranqueado |

O desafio pode ser cumprido com **qualquer** arma ou habilidade, desde que o Riven velado esteja equipado no loadout. Dá para revelar vários ao mesmo tempo (um em cada arma). A arma usada no desafio não influencia o resultado.

## 🔢 Fórmulas e Números — Riven Mods

### Disposition

| Pontos | Faixa | Significado |
|---|---|---|
| ●●●●● | 1,31–1,55 | Armas pouco usadas → atributos mais altos |
| ●●●●○ | 1,11–1,30 | Acima da média |
| ●●●○○ | 0,90–1,10 | Neutra |
| ●●○○○ | 0,70–0,89 | Abaixo da média |
| ●○○○○ | 0,50–0,69 | Armas muito usadas; **toda arma nova começa aqui** |

- A Disposition muda **a cada ~3 meses, junto com cada Prime Access**, e os Rivens já revelados são reajustados automaticamente.
- Variantes podem ter Disposition diferente (ex.: Telos Boltor e Boltor Prime 1,20; Boltor 1,30). Em Zaw vale o Strike; em Kitgun vale o Chamber.
- O valor atual aparece no Arsenal, aba Upgrade. Cada arquivo de arma do vault tem o campo `disposicao_riven` (instantâneo; confira no jogo).

### Custo de ciclo (reroll) em Kuva

| Ciclo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10+ |
|---|---|---|---|---|---|---|---|---|---|---|
| Normal | 900 | 1.000 | 1.200 | 1.400 | 1.700 | 2.000 | 2.350 | 2.750 | 3.150 | 3.500 |
| Com trait travado | 1.800 | 2.000 | 2.400 | 2.800 | 3.400 | 4.000 | 4.700 | 5.500 | 6.300 | 7.000 |

- 9 primeiros ciclos: **16.450 Kuva** no total. Ciclar não muda arma, rank, polaridade nem MR.
- **Trait Locking**: trava um atributo e dobra o custo; também congela o layout (ex.: 2 positivos + 1 negativo).
- **Splicing** (com Riven Splicer, só da The Icebind): combina dois atributos num atributo novo fora do pool normal (ex.: um elemento combinado). O atributo emendado fica travado mas **não** dobra o custo de Kuva; só 1 por Riven.

### Endo ao dissolver

```
Endo = (100 × (MR do Riven − 8) + 22,5 × 2^rank + 200 × ciclos) − 7     (arredondado para baixo)
Exemplo da wiki: MR 13, rank 8, 5 ciclos → 7.253 Endo
```

## 🎯 Como Conseguir — Riven Mods

| Fonte | Detalhe |
|---|---|
| Quest [[missoes/jornadas/principais/the_war_within.md\|The War Within]] | 1 Riven garantido |
| Palladino (Iron Wake, Terra) | 10 [[recursos/raridades/especial/riven_sliver.md\|Riven Sliver]] → 1 Riven velado, 2× por semana (exige Chains of Harrow) |
| [[missoes/tipos/sortie.md\|Sortie]] | Melee 8,14% · Pistol 7,61% · Rifle 6,79% · Kitgun 2% · Zaw 2% · Shotgun 1,36% |
| Steel Path Honors ([[lore/personagens/teshin.md\|Teshin]]) | Oferta rotativa; não inclui Pistol nem Melee |
| Acrithis (Duviri) | 15 [[recursos/open_worlds/duviri/pathos_clamp.md\|Pathos Clamps]]; Riven de arma de companion por 20 |
| [[missoes/tipos/archon_hunt.md\|Archon Hunt]], Steel Path Circuit, Steel Path Descendia, baús da The Icebind | Possíveis recompensas |
| [[mecanicas/nightwave.md\|Nightwave]], Calendário 1999, Daily Tribute (marcos Evergreen dão 3 Rivens + 3 slots) | Esporádico |
| Arbitration Honors | Riven de Archgun por 35 [[recursos/raridades/especial/vitus_essence.md\|Vitus Essence]] |
| [[mecanicas/sindicatos/cephalon_simaris.md\|Cephalon Simaris]] | Riven de arma de companion por 100.000 Standing |

**Riven Transmuter** ([[recursos/raridades/especial/riven_transmuter.md|arquivo]]): sacrifica 4 Rivens → 1 Riven velado de um dos tipos sacrificados (4 do mesmo tipo garantem o tipo). Vem 2× da captura do [[lore/chefes/eidolon_hydrolyst.md|Eidolon Hydrolyst]], de [[lore/personagens/loid.md|Loid]] por 180 Vessel Capillaries ou de Palladino por 10 Riven Slivers.

## 💡 Dicas Práticas — Riven Mods

- Para negociar, quem recebe precisa de **MR 8** ([[mecanicas/trading.md|Trading]]). Preço é mercado livre e muda muito — não existe valor de referência confiável.
- Rivens velados são negociados "às cegas"; vale mais rolar o desafio quando a classe é popular (Melee, Rifle).
- Ciclar o mesmo Riven além do 9º custa 3.500 por ciclo; começar outro Riven sem ciclos sai mais barato.

## 🔗 Relacionados — Riven Mods

- [[mecanicas/modding.md|Modding]] — capacidade, polaridade e fusão.
- [[mecanicas/endo_e_creditos.md|Endo e Credits]], [[recursos/raridades/raro/kuva.md|Kuva]], [[recursos/raridades/especial/riven_sliver.md|Riven Sliver]].

## 📚 Fontes — Riven Mods

- https://wiki.warframe.com/w/Riven_Mods — propriedades, estados, aquisição, Disposition, ciclo, Trait Locking, Splicing, Transmutation (consultado em 2026-10-14)
- https://wiki.warframe.com/w/Endo — fórmula de Endo ao dissolver Riven (consultado em 2026-10-14)
