---
title: Operator e Focus
tipo: mecanica
tags: [mecanica, operator, focus, tenno, void, escolas, waybound]
atualizado: 2026-10-04
verificado: true
agente: opus
---

# Operator e Focus

> [!info] Em uma linha
> Focus 3.0 é a árvore de poderes do Tenno dentro do Warframe: cinco escolas (Madurai, Vazarin, Naramon, Unairu, Zenurik), cada uma com 10 Ways, duas delas desvinculáveis (Way-Bound) para valer em qualquer escola.

> [!warning] Spoiler — The Second Dream, The War Within, The Old Peace
> Tudo abaixo depende de saber o que o Operator é. Não leia sem ter feito **The Second Dream**.

---

## 🧩 Como Funciona

Focus destranca em três degraus. **The Second Dream** libera a **Transcendence**: uma projeção invulnerável do Operator com um Void Beam, dura **10 s**, e o medidor recarrega sozinho em **3 minutos** — e com ela as **duas Passive Ways** de cada escola. **The War Within** substitui a Transcendence pela **Transference**, que coloca o Operator fisicamente em campo com habilidades, Amp e Arcanes próprios, e faz as passivas de Focus valerem **desde o início da missão**, mesmo sem nunca usar Transference. Para revelar o resto das Ways é preciso ter feito **The War Within + Saya's Vigil** e falar com [[mecanicas/sindicatos/the_quills.md\|The Quills]] em Cetus. Depois de **The Old Peace** abre-se a camada do **Tauron Strike**.

No fim de The Second Dream você escolhe **uma** escola de graça. Cada escola restante custa **50.000 Focus Points** para destrancar (200.000 pelas quatro). Cada escola tem **10 Ways** com **4 ranks** cada, e o custo depende da distância do nó central na árvore.

As Ways se dividem em três tipos. **Active Ways** (ícone circular) alteram os poderes de Void — Void Sling e Void Mode — e dão duas habilidades castáveis; são **6 por escola**, em três pares, e só funcionam na escola selecionada. **Passive Ways** (ícone hexagonal) dão bônus de stat ao Warframe e/ou ao Operator desde o começo da missão; são **2 por escola**. **Way-Bounds** são as duas restantes e são especiais: elas podem ser **desvinculadas** da escola e passam a valer em **qualquer** escola selecionada.

> [!danger] Focus gasto não volta
> Destrancar uma Way é gasto único e confirmado. Depois de confirmar, **o Focus não é reembolsado nem recuperado**. Antes de confirmar ainda é possível reverter para o último estado salvo.

---

## 🔢 Fórmulas e Números

```
Teto diário de Focus = 250.000 + (5.000 x Mastery Rank)
Reset: 00:00 UTC

Convergence Orb: multiplica a conversão de Affinity em Focus por 10x
  Duração: 45 s, OU até morrer, OU até bater o teto diário — o que vier primeiro
  Bônus imediato: +5.000 Focus na escola ativa
  Despawna em 1 minuto se não for pego

Desvincular um Way-Bound = levar ao último rank + 750.000 Focus + 1 Brilliant Eidolon Shard
```

| Variável | Significado | Fonte do valor |
|---|---|---|
| 250.000 | Teto diário base de Focus por Lens, no MR 0 | Wiki, Focus § Daily Cap |
| +5.000 por MR | Escala do teto diário | Wiki, Focus § Daily Cap |
| 10x / 45 s / +5.000 | Multiplicador, duração e bônus do Convergence Orb | Wiki, Focus § Convergence Orbs |
| 50.000 | Custo para destrancar cada escola não escolhida | Wiki, Focus § Costs |
| 750.000 + 1 Brilliant Shard | Custo de desvincular **um** Way-Bound | Wiki, Focus § Way-Bounds |
| 10 s / 3 min | Duração e recarga da Transcendence (antes de The War Within) | Wiki, Focus § Activation |

### Custo por posição da Way na árvore

| Posição | Ranks (unlock → rank 4) | Total | Quantidade por escola |
|---|---|---|---|
| Way central | 25.000 → +50.000 → +105.000 → +200.000 | **380.000** | 1 |
| Adjacente ao centro | 60.000 → +105.000 → +215.000 → +400.000 | **780.000** | 5 (total 3.900.000) |
| Mais distante do centro | 95.000 → +160.000 → +325.000 → +600.000 | **1.180.000** | 4 (total 4.720.000) |
| Way-Bound (desvincular) | +750.000 + 1 Brilliant Eidolon Shard | — | 2 (total 1.500.000 + 2 shards) |

**Totais:**

| Escopo | Focus Points |
|---|---|
| Maxar todas as Ways de **uma** escola | 9.000.000 |
| + desvincular os 2 Way-Bounds dessa escola | +1.500.000 e 2 Brilliant Eidolon Shards → **10.500.000** |
| Maxar as 5 Ways de Tauron Strike de uma escola | 5.005.000 + recursos de Tau |
| Maxar **todas as 5 escolas** (Ways + Way-Bounds + Tauron Strike) | **77.525.000** |

**Tetos e limites conhecidos:**

- O teto diário vale **só para Focus vindo de Focus Lens**. **Eidolon Shards ignoram o teto diário.**
- Focus de inimigo do Void (Thrax, Void Angel) **conta** para o teto diário.
- Convergence Orbs **param de aparecer** depois de bater o teto diário — exceto se você tiver Tauron Strike destrancado, caso em que ficam azuis e só aumentam a carga do Tauron Strike (+10%).
- Convergence Orbs só aparecem se você levar **algum equipamento com Focus Lens** instalada.
- Para desvincular, a Way-Bound precisa estar **no último rank** antes de pagar os 750.000.
- Bônus de dano de Operator do **Vengeance** tem teto de **+1000%**.

---

## 📋 Tabelas de Referência

### Taxa de conversão de Affinity em Focus

Primeiro, como a Affinity se distribui:

| Fonte do abate | Distribuição |
|---|---|
| Habilidade de Warframe | **100% para o Warframe** (abates por proc de Syndicate Weapon Augment contam como abate de Warframe) |
| Arma | 50% Warframe / 50% arma que matou |
| Aliado | 25% Warframe / 75% dividido igualmente entre as armas equipadas |
| Em modo Operator | 37,5% vai para o **Amp** |

Depois, quanto disso vira Focus, por tipo de Lens:

| Lens no Warframe | Lens na arma | Abate por habilidade | Abate por arma | Abate de aliado |
|---|---|---|---|---|
| — | Focus Lens | 0% | 0,625% | 0,9375% |
| — | Greater Focus Lens | 0% | 0,875% | 1,3125% |
| — | Eidolon Lens | 0% | 1,125% | 1,6875% |
| — | Lua Lens | 0% | 1,625% | 2,4375% |
| Focus Lens | — | 1,25% | 0,625% | 0,3125% |
| Focus Lens | Focus Lens | 1,25% | 1,25% | 1,25% |
| Focus Lens | Greater Focus Lens | 1,25% | 1,5% | 1,625% |
| Focus Lens | Eidolon Lens | 1,25% | 1,75% | 2% |
| Focus Lens | Lua Lens | 1,25% | 2,25% | 2,75% |

> A escola de Focus ganha é definida pela **escola da Lens instalada**, não pela escola ativa: Naramon Lens no Warframe gera Focus de Naramon.
>
> **Warframe sem Lens é desperdício puro:** abate por arma manda 50% da Affinity para o frame, e sem Lens esses 50% não convertem nada.

### Fontes de Focus que não são Lens

| Fonte | Focus | Conta no teto diário? |
|---|---|---|
| [[recursos/open_worlds/eidolon/eidolon_shard.md\|Eidolon Shard]] | 2.500 | ❌ Não |
| Synthetic Eidolon Shard | 5.000 | ❌ Não |
| [[recursos/open_worlds/eidolon/brilliant_eidolon_shard.md\|Brilliant Eidolon Shard]] | 25.000 | ❌ Não |
| [[recursos/open_worlds/eidolon/radiant_eidolon_shard.md\|Radiant Eidolon Shard]] | 40.000 | ❌ Não |
| Thrax Centurion / Thrax Legatus abatido | 2.500 para **todo o squad** | ✅ Sim |
| Ravenous Void Angel (Void Armageddon) | 7.500 | ✅ Sim |
| Void Angel dormente (qualquer missão do Zariman) | 15.000 | ✅ Sim |
| Convergence Orb (bônus imediato) | +5.000 | ✅ Sim |

> Thrax Centurion e Thrax Legatus também aparecem em Conjunction Survival, Duviri e The Circuit — não só no Zariman.

---

## 🌳 As cinco escolas, Way por Way

Formato do custo: `rank 1 / 2 / 3 / 4` em Focus Points.

### ⚡ Zenurik — School of the Arcane ("Dominate the Enemy")

Energia e controle. A escolha padrão da maioria dos jogadores, pela regeneração de energia.

| Way | Tipo | Efeito (rank 1 → 4) | Custo |
|---|---|---|---|
| **Energy Pulse** | Passiva (Warframe + Operator) | Pickup de energia dá +20/30/40/50% de energia extra ao longo de 11/9/7/5 s | 25.000 / 50.000 / 105.000 / 200.000 |
| **Inner Might** | Passiva (Warframe) | Permite castar habilidade **sem gastar energia nem escudo**, com recarga de 90/80/70/60 s | 60.000 / 105.000 / 215.000 / 400.000 |
| **Void Siphon** | **Way-Bound** (Operator) | +22/45/67/90% de regen de energia do Operator (**não** do Amp) | 60.000 / 105.000 / 215.000 / 400.000 / 750.000 + Brilliant Shard |
| **Void Flow** | **Way-Bound** (Operator) | +22/45/67/90% de energia máxima do Operator (**não** do Amp) | 95.000 / 160.000 / 325.000 / 600.000 / 750.000 + Brilliant Shard |
| **Wellspring** | Ativa 1 (Warframe + Operator) | Cria um poço de energia por 5/5/6/8 s; aliados que passam ganham 3/4/4/5 energia/s por 20/22/25/30 s | 60.000 / 105.000 / 215.000 / 400.000 |
| **Hardened Wellspring** | Ativa (Warframe + Operator) | Castar a 1ª habilidade dentro do Wellspring aumenta o tamanho, soma 14/16/18/20 s de duração e dá +12/15/18/20% de Força de Habilidade a quem estiver dentro | 95.000 / 160.000 / 325.000 / 600.000 |
| **Temporal Drag** | Ativa 2 (Operator) | Rajada radial que lentifica inimigo em 50/60/70/80% por 4/6/8/10 s | 60.000 / 105.000 / 215.000 / 400.000 |
| **Temporal Shot** | Ativa (Warframe + Operator) | +40/60/80/100% de dano de headshot em inimigo sob Temporal Drag | 95.000 / 160.000 / 325.000 / 600.000 |
| **Disarming Sling** | Ativa (Operator) | Void Sling atravessando inimigo tem 20/30/40/50% de chance de **desarmá-lo** | 60.000 / 105.000 / 215.000 / 400.000 |
| **No Quarter** | Ativa (Operator) | Matar inimigo desarmado dá +2/5/7/10% de regen de energia do Operator por 2,5/5/7,5/10 s, até 4 stacks | 95.000 / 160.000 / 325.000 / 600.000 |

**Tauron Strike — Lorak** (após The Old Peace): feixe de energia; inimigo perfurado tem 25/50/75/100% de chance de dropar Energy Orb se morrer em 10 s. Nós extras: **Prismatic Beam** (inimigo atingido dispara feixes menores em 5/10/15/20 m), **Spectral Pages** (1/2/3/4 páginas espectrais, cada uma +10% de velocidade de cast, Força, Duração e +100 de energia), **Boundless Energy** (+25/30/35/40% nos bônus das páginas), **Brilliant Insight** (páginas também cegam inimigos em 4/8/12/16 m).

### 🔥 Madurai — School of the Fighters ("Engage the Enemy")

Dano puro. Escola obrigatória para caça de Eidolon.

| Way | Tipo | Efeito | Custo |
|---|---|---|---|
| **Phoenix Talons** | Passiva (Warframe + Operator) | +5/10/20/30% de **dano físico** e de dano de Operator | 25.000 / 50.000 / 105.000 / 200.000 |
| **Power Transfer** | Passiva (Warframe + Operator) | +45/60/75/100% de Dano Crítico do Amp por 5/10/15/20 s ao trocar para Operator; +20/30/40/50% de velocidade de cast ao voltar para o Warframe | 60.000 / 105.000 / 215.000 / 400.000 |
| **Inner Gaze** | **Way-Bound** (Operator) | +10/20/30/40% de energia de Amp e Void Beam | 60.000 / 105.000 / 215.000 / 400.000 / 750.000 + Brilliant Shard |
| **Eternal Gaze** | **Way-Bound** (Operator) | +15/30/45/60% de regen de energia de Amp e Void Beam | 95.000 / 160.000 / 325.000 / 600.000 / 750.000 + Brilliant Shard |
| **Void Strike** | Ativa 1 (Warframe + Operator) | Consome **toda** a energia para aumentar dano por 5/6/7/8 s: +4/6/8/10% de dano por cada ponto percentual de energia consumido. Cooldown 70/60/50/40 s | 60.000 / 105.000 / 215.000 / 400.000 |
| **Void Fuel** | Ativa (Warframe + Operator) | +10/20/30/40% de eficiência de arma para Operator e Warframe enquanto Void Strike está ativo | 95.000 / 105.000 / 215.000 / 400.000 |
| **Contamination Wave** | Ativa 2 (Operator) | Onda de Void por 0,5/1/1,5/2 s que deixa inimigos 20/30/40/50% mais vulneráveis a dano de Operator por 5/10/15/20 s | 60.000 / 105.000 / 215.000 / 400.000 |
| **Distilled Contamination** | Ativa (Operator) | Matar inimigo contaminado deixa todos os afetados +20/30/40/50% mais vulneráveis e estende o efeito em 4/6/8/10 s. Máx. 2 stacks | 95.000 / 160.000 / 325.000 / 600.000 |
| **Chained Sling** | Ativa (Operator) | +20/30/40/50% de eficiência de energia em Void Slings consecutivos | 60.000 / 105.000 / 215.000 / 400.000 |
| **Sling Strength** | Ativa (Warframe) | Voltar ao Warframe depois de um Chained Sling dá +10/20/30/40% de Força de Habilidade por 5/10/15/20 s | 95.000 / 160.000 / 325.000 / 600.000 |

**Tauron Strike — Thara**: chuva de flechas explosivas por 4/5/6/7 s. Nós extras: **Rain of Arrows**, **Surging Storm** (raio 3,5→5 m), **Downpour** (1/2/3/4 alvos extras em 10 m), **Overwhelming Power** (+2/3/4/5% de Força por inimigo atingido, teto +20/30/40/50%).

### 🪨 Unairu — School of the Indomitable ("Outlast the Enemy")

Remoção de defesa e sobrevivência. A resposta direta ao escudo de 250% do [[mecanicas/steel_path.md\|Steel Path]].

| Way | Tipo | Efeito | Custo |
|---|---|---|---|
| **Poise** | Ativa (Warframe + Operator) | Imunidade a slow, stagger e knockdown por 10/20/30/40 s após cada Transference | 25.000 / 50.000 / 105.000 / 200.000 |
| **Stone Skin** | Passiva (Warframe + Operator) | +50/100/150/200 de **Armadura** para Warframe **e** Operator | 60.000 / 105.000 / 215.000 / 400.000 |
| **Last Gasp** | **Way-Bound** (Operator) | Revive o Warframe: use Transference durante o Bleedout e mate 3 inimigos antes de 9/11/13/15 s. Eximus, Thrax Centurion e Thrax Legatus enchem o medidor instantaneamente. 5 s de invulnerabilidade ao ativar. DoT ativo (Spores, Seeking Talons) também enche. **Não funciona** em frames com auto-revive (Inaros, Nokko, Sevagoth) | 60.000 / 105.000 / 215.000 / 400.000 / 750.000 + Brilliant Shard |
| **Vengeance** | **Way-Bound** (Operator) | Durante Last Gasp, dano de Operator +25/50/75/100% **mais** 10/15/20/25% por segundo. Aditivo com Unairu Wisp, Void Strike, Phoenix Talons, Amp Spike, Lethal Levitation, Eternal Eradicate e Virtuos Fury. **Teto: +1000%** | 95.000 / 160.000 / 325.000 / 600.000 / 750.000 + Brilliant Shard |
| **Magnetic Flare** | Ativa 1 (Operator) | Campo de 5/6/7/8 m por 12/18/24/30 s que **desativa o escudo** de qualquer inimigo que entrar | 60.000 / 105.000 / 215.000 / 400.000 |
| **Magnetic Boost** | Ativa (Operator) | Void Sling saindo de um Magnetic Flare renova a duração e aumenta o raio em 25/50/75/100% | 95.000 / 160.000 / 325.000 / 600.000 |
| **Caustic Strike** | Ativa 2 (Operator) | Bomba de energia com raio 5/6/7/8 m que remove **40/60/80/100% da armadura** inimiga. Tocar `2` de novo detona em voo | 60.000 / 105.000 / 215.000 / 400.000 |
| **Unairu Wisp** | Ativa (Operator) | 25/50/75/100% de chance de gerar um Wisp por inimigo atingido por Caustic Strike; o Wisp busca o aliado mais próximo no Affinity Range e dá +20/40/60/100% de dano de Operator por 5/10/15/20 s | 95.000 / 160.000 / 325.000 / 600.000 |
| **Reinforced Return** | Ativa (Warframe) | Warframe fica invulnerável por 1/2/3/4 s depois do Operator cair. Tocar `X` enquanto o Operator cai traz o Warframe até ele | 60.000 / 105.000 / 215.000 / 400.000 |
| **Static Purge** | Ativa (Warframe) | 25/50/75/100% de chance de limpar Transference Static ao matar, enquanto Reinforced Return está ativo | 95.000 / 160.000 / 325.000 / 600.000 |

**Tauron Strike — Cogron** (martelo): onda de choque que ondula 1/2/3/4 vezes. Nós extras: **Sundered Bounty** (2/3/4/5 Universal Orbs ou Ammo por onda), **Seismic Impact** (próximos 1/2/3/4 slams aéreos ganham a onda), **Tempered Benison** (2/3/4/5 Armor Motes de **+450 de armadura temporária**, máx. 5), **Great Quake** (+10/20/30/40% de raio).

### 🌊 Vazarin — School of the Protectors ("Counter the Enemy")

Suporte, cura e revive. A escola de Defense e de Eidolon Hunt em squad.

| Way | Tipo | Efeito | Custo |
|---|---|---|---|
| **Mending Unity** | Passiva (Warframe + Operator) | +10/15/20/25 m de **Affinity Radius** | 25.000 / 50.000 / 105.000 / 200.000 |
| **Mending Soul** | Passiva (Warframe + Operator) | Os primeiros 1/2/3/4 revives são **instantâneos**; os demais são 25/50/75/100% mais rápidos | 60.000 / 105.000 / 215.000 / 400.000 |
| **Enduring Tides** | **Way-Bound** (Operator) | +50/100/150/200% de Vida **e** Armadura do Operator. Aditivo com Magus Vigor e Magus Husk | 60.000 / 105.000 / 215.000 / 400.000 / 750.000 + Brilliant Shard |
| **Rejuvenating Tides** | **Way-Bound** (Operator) | +1,5/3/4,5/6 de Vida/s no Operator, **dobrado** enquanto você controla o Warframe | 95.000 / 160.000 / 325.000 / 600.000 / 750.000 + Brilliant Shard |
| **Guardian Shell** | Ativa 1 (Warframe + Operator) | Barreira no Operator e aliados no Affinity Range. Invulnerável nos primeiros 4 s, e **o dano levado durante a invulnerabilidade é somado** à vida base de 200/300/400/500 | 60.000 / 105.000 / 215.000 / 400.000 |
| **Guardian Break** | Ativa (Warframe) | Quando a Guardian Shell quebra: +90/110/130/150% de regen de escudo do Warframe e −20/40/60/80% de delay de regen, por 6/8/10/12 s | 95.000 / 160.000 / 325.000 / 600.000 |
| **Void Snare** | Ativa 2 (Warframe + Operator) | Projétil que cria vórtice de 5/6/7/8 s; Void Sling através dos inimigos presos dá 40/60/80/100 de vida a aliados no Affinity Range | 60.000 / 105.000 / 215.000 / 400.000 |
| **Protective Sling** | Ativa (Warframe + Operator) | Aliado tocado pelo Void Sling fica imune a dano por 2/3/4/5 s e é curado 30/40/50/60% ao longo de 5 s. Custa 10 de energia | 95.000 / 160.000 / 325.000 / 600.000 |
| **Void Regen** | Ativa (Operator) | Void Mode começa curando +4/6/8/10 de vida/s, subindo 4/6/8/10 por segundo até o máximo de 20/30/40/50 | 60.000 / 105.000 / 215.000 / 400.000 |
| **Squad Regen** | Ativa (Operator) | Quando Void Regen atinge o máximo, aplica a cura ao squad no Affinity Range por 30/40/50/60 s | 95.000 / 160.000 / 325.000 / 600.000 |

**Tauron Strike — Nidri** (cajado): vórtice de água por 20 s. Nós extras: **Rift Waters** (remove 10/15/20/25% de **Overguard** por segundo), **Eroding Rapids** (25/50/75/100% de vulnerabilidade a status), **Deathless Currents** (cura 100/150/200/250 vida/s; jogador caído dentro é revivido na hora, jogador morto é reinvocado para o Nidri a qualquer distância), **Swelling Deluge** (duração 25/30/35/40 s).

### ⚔️ Naramon — School of the Tacticians ("Know the Enemy")

Melee. A escola de quem joga com arma branca e [[mecanicas/combo_counter.md\|Combo Counter]].

| Way | Tipo | Efeito | Custo |
|---|---|---|---|
| **Power Spike** | Passiva (Warframe) | Combo Counter **decai** 20/15/10/5 a cada poucos segundos fora de combate, em vez de zerar de uma vez | 25.000 / 50.000 / 105.000 / 200.000 |
| **Affinity Spike** | Passiva (Warframe) | Abate com melee dá +15/25/35/45% de Affinity de melee | 60.000 / 105.000 / 215.000 / 400.000 |
| **Mind Step** | **Way-Bound** (Operator) | +7/15/22/30% de velocidade de movimento do Operator | 60.000 / 105.000 / 215.000 / 400.000 / 750.000 + Brilliant Shard |
| **Far Sling** | **Way-Bound** (Operator) | +7/15/22/30% de distância máxima do Void Sling | 95.000 / 160.000 / 325.000 / 600.000 / 750.000 + Brilliant Shard |
| **Void Levitation** | Ativa 1 (Operator) | Onda de 3/4/5/6 m por 1/2/3/4 s que aplica **Lift** em todos os inimigos tocados | 60.000 / 105.000 / 215.000 / 400.000 |
| **Lethal Levitation** | Ativa (Warframe + Operator) | +20/30/40/50% de dano de arma por inimigo **Lifted** atacado pelo Operator, por 30/40/50/60 s, até 4 stacks | 95.000 / 160.000 / 325.000 / 600.000 |
| **Sling Stun** | Ativa 2 (Warframe) | Aumenta a largura do próximo Void Sling em 50/100/150/200%; inimigos atingidos ficam vulneráveis a **Finisher** e tomam +15/20/25/30% de dano de finisher | 60.000 / 105.000 / 215.000 / 400.000 |
| **Killer's Rush** | Ativa (Warframe) | Iniciar um finisher como Operator troca para o Warframe e dá +20/30/40/50% de **Chance Crítica de melee** por 10/20/30/40 s | 95.000 / 160.000 / 325.000 / 600.000 |
| **Opening Slam** | Ativa (Warframe) | Fazer um Slam como Operator troca para o Warframe e dá **ganho de Combo dobrado** por 5/10/15/20 s | 60.000 / 105.000 / 215.000 / 400.000 |
| **Amp Spike** | Ativa (Operator) | Trocar para Operator com multiplicador de Combo **8x** dá +40/60/80/100% de dano de Amp por 10/20/30/40 s | 95.000 / 160.000 / 325.000 / 600.000 |

**Tauron Strike — Vexoric** (espada colossal): onda de energia; **+2/4/6/8 de Combo por inimigo atingido**. Nós extras: **Spectral Blades** (1/2/3/4 espadas espectrais que copiam sua melee e atacam inimigos em 10 m por 30 s, somando Combo e carga de Tauron Strike; são dadas a **todo o squad** no Affinity Range), **Flowing Strikes** (alcance 14/18/22/26 m), **Hungering Blades** (25/50/75/100% de chance de atacar o mesmo inimigo duas vezes), **Astral Cut** (+20/40/60/80% no tamanho do corte).

### Tauron Strike — a camada de The Old Peace

Após **The Old Peace**, comprando o **Tektolyst Artifact** da escola com a Marie, destranca-se o **Tauron Strike**: a **terceira habilidade** do Operator, mais 5 nós de Focus próprios. Cada Tektolyst Artifact também é um slot de arma com **5 slots de Operator Mod** e **1 de Tektolyst Arcane Enhancement**.

| Custo | Valor |
|---|---|
| Destrancar o Tauron Strike de uma escola | 150 Lyroic Bridge + 150 Ren Hypercore + 150 Ascaris Prime (750 de cada para as 5) |
| Maxar os 5 nós de uma escola | 5.005.000 Focus + 2/3/5/6 dos recursos por tier (varia por escola) |
| Maxar os nós de Tauron Strike das 5 escolas | 114 Lyroic Bridge, 162 Ren Hypercore, 89 Ascaris Prime (os totais de destrancar + maxar somam 864 / 912 / 839) |

---

## 🛠️ Como Explorar na Prática

| Objetivo | O que fazer |
|---|---|
| Primeira escola a escolher | **Zenurik**. Wellspring resolve o problema de energia de qualquer frame no começo do jogo, e Inner Might dá cast grátis a cada 60 s |
| Resolver escudo e armadura do Steel Path | **Unairu**: Magnetic Flare desativa escudo em área, Caustic Strike remove 100% da armadura. Não gasta slot de habilidade do frame, diferente de subsumir Pillage no [[mecanicas/helminth.md\|Helminth]] |
| Caçar Eidolon | **Madurai** + Amp. Void Strike consome toda a energia para um pico de dano; Phoenix Talons e Power Transfer somam em cima |
| Build de melee | **Naramon**. Power Spike sozinho muda o jogo: o Combo **decai** em vez de zerar. Killer's Rush dá +50% de crítico de melee |
| Carregar squad em Defense / Eidolon | **Vazarin**. Mending Soul dá 4 revives instantâneos; Protective Sling dá imunidade a dano e cura em aliado tocado |
| Maximizar Focus por hora | Lua Lens no Warframe **e** na arma, usar habilidade para matar (100% da Affinity vai ao frame), e **sempre** pegar o Convergence Orb — 10x por 45 s |
| Furar o teto diário | Eidolon Shards **não contam** no teto. Guarde os shards da Eidolon Hunt para depois de bater os 250.000+ do dia |
| Escolher as Way-Bounds a desvincular primeiro | **Void Flow + Void Siphon** (Zenurik) e **Enduring Tides + Rejuvenating Tides** (Vazarin) são as quatro que mais mudam a sobrevivência e autonomia do Operator em qualquer escola |
| Sobreviver a um down | **Last Gasp** (Unairu, Way-Bound): com ele desvinculado, você se revive em qualquer escola matando 3 inimigos — e um Eximus enche o medidor sozinho |
| Não jogar Focus no lixo | Focus confirmado **nunca volta**. Antes de confirmar, dá para reverter. Pense a árvore inteira antes |

**Mods que interagem:** Arcanes de Operator — **Magus** (Magus Vigor, Magus Husk, Magus Elevate, Magus Repair) e **Virtuos** (Virtuos Fury, Virtuos Strike, Virtuos Shadow) — somam em cima dos bônus de Way. Enduring Tides é **aditivo** com Magus Vigor e Magus Husk. Vengeance é aditivo com Virtuos Fury. [[mods/warframe/rifle_amp.md|Rifle Amp]] e [[mods/warframe/pistol_amp.md|Pistol Amp]] são mods de aura de dano de arma, não de Amp de Operator — não confundir.

**Frames que interagem:** [[warframes/regular/inaros.md|Inaros]], [[warframes/regular/nokko.md|Nokko]] e [[warframes/regular/sevagoth.md|Sevagoth]] têm auto-revive e **não podem usar Last Gasp**. [[warframes/regular/hildryn.md|Hildryn]] e [[warframes/regular/lavos.md|Lavos]] não usam energia, então Wellspring e Energy Pulse não fazem nada neles. [[warframes/regular/saryn.md|Saryn]] (Spores) e [[warframes/regular/garuda.md|Garuda]] (Seeking Talons) enchem o medidor de Last Gasp com DoT.

---

## ⚠️ Erros Comuns

- **"Focus gasto pode ser realocado."** Não existe respec. Focus confirmado numa Way **nunca** volta.
- **"Way-Bound funciona em qualquer escola desde o começo."** Não. Precisa estar no **último rank** e custar **750.000 Focus + 1 Brilliant Eidolon Shard** para ser desvinculada. Só então passa a valer em qualquer escola.
- **"Teto diário vale para tudo."** Vale só para Focus de **Focus Lens**. **Eidolon Shards ignoram o teto.**
- **"Lens só na arma basta."** Abate por habilidade de Warframe manda **100%** da Affinity ao frame — sem Lens no frame, você perde toda a conversão desses abates. A combinação ideal é Lens no frame **e** na arma.
- **"Convergence Orb dura até o fim da missão."** 45 segundos, ou até você morrer, ou até bater o teto — o que vier primeiro. Despawna em 1 minuto se não for pego.
- **"Void Flow aumenta a energia do Amp."** Não. Void Flow e Void Siphon mexem **só** na energia do Operator. Quem mexe no Amp é **Inner Gaze** e **Eternal Gaze** (Madurai).
- **"Last Gasp funciona em todo frame."** Não funciona em frames com auto-revive: Inaros, Nokko, Sevagoth.
- **"Caustic Strike remove escudo também."** Não. **Caustic Strike** remove **armadura**; **Magnetic Flare** desativa **escudo**. São dois nós diferentes da Unairu.
- **"Preciso só de The Second Dream."** The Second Dream dá só as duas passivas por escola. O resto exige **The War Within + Saya's Vigil** e falar com The Quills em Cetus.
- **"Zenurik ainda dá stun elétrico."** Não desde o Focus 3.0 (Update 31.5, 2022-04-27). Zenurik perdeu o efeito de Electricity, o Void Mode que puxava inimigos e o bônus de eficiência de Heavy Attack.
- **"Transcendence e Transference são a mesma coisa."** Transcendence (pós-The Second Dream) é uma projeção invulnerável de 10 s com recarga de 3 min. Transference (pós-The War Within) põe o Operator de verdade em campo, sem limite de tempo.

---

## 🔗 Mecânicas Relacionadas

- [[mecanicas/steel_path.md|The Steel Path]] — Unairu (Magnetic Flare + Caustic Strike) é a resposta sem custo de slot ao escudo de 250%.
- [[mecanicas/helminth.md|Helminth]] — a alternativa a Unairu é subsumir Pillage ou Tharros Strike, que custa um slot de habilidade do frame.
- [[mecanicas/mastery_rank.md|Mastery Rank]] — o teto diário de Focus é 250.000 + 5.000 por MR.
- [[mecanicas/combo_counter.md|Combo Counter]] — Power Spike (Naramon) muda a regra de decaimento do Combo; Opening Slam dobra o ganho; Amp Spike exige Combo 8x.
- [[mecanicas/critico.md|Crítico]] — Killer's Rush dá até +50% de chance crítica de melee; Power Transfer dá até +100% de dano crítico de Amp.
- [[mecanicas/stealth_e_finishers.md|Stealth e Finishers]] — Sling Stun abre inimigos a Finisher e Killer's Rush recompensa iniciá-los.
- [[mecanicas/parkour.md|Parkour]] — Void Sling é a locomoção do Operator; Far Sling e Mind Step (Naramon) a melhoram.
- [[mecanicas/sindicatos/the_quills.md|The Quills]] — o sindicato que libera o resto das Ways e vende peças de Amp.
- [[mecanicas/sindicatos/vox_solaris.md|Vox Solaris]] — Amps de tier superior e Arcanes de Operator.
- [[mecanicas/trading.md|Trading]] — Focus Lens e os blueprints de Eidolon Lens e Lua Lens são tradeáveis como Common (2.000 Credits).
- [[missoes/jornadas/principais/the_second_dream.md|The Second Dream]], [[missoes/jornadas/principais/the_war_within.md|The War Within]] — os dois degraus de desbloqueio.
- [[locais/open-worlds/zariman.md|Zariman Ten Zero]] — Thrax e Void Angels, as fontes de Focus que não precisam de Lens.
- [[missoes/tipos/void_armageddon.md|Void Armageddon]] — Ravenous Void Angel dá 7.500 de Focus.
- [[recursos/open_worlds/eidolon/brilliant_eidolon_shard.md|Brilliant Eidolon Shard]] — 25.000 de Focus cada, e o item exigido para desvincular cada Way-Bound.

---

## 📚 Fontes
- https://wiki.warframe.com/w/Focus — Transcendence e Transference, requisitos de desbloqueio, tipos de Way, regras de Way-Bound, teto diário, tabela de conversão por Lens e por fonte de abate, Convergence Orbs, Eidolon Shards, inimigos do Void, custos por posição na árvore e totais, camada de Tauron Strike (consultado em 2026-10-04)
- https://wiki.warframe.com/w/Focus/Zenurik · /Madurai · /Unairu · /Vazarin · /Naramon — efeito e custo exatos de cada Way por rank, incluindo os nós de Tauron Strike (consultado em 2026-10-04)
