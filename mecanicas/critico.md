---
title: Crítico
aliases: [Crítico, Critico, chance crítica, dano crítico, crit]
tipo: mecanica
resumo: "Crítico — Um dos dois eixos de escala de dano do jogo (o outro é status): chance crítica decide com que frequência o acerto é crítico, multiplicador crítico decide quanto ele multiplica — e acima de 100% de chance o Warframe entra em camadas de críti."
status: completo
rag: true
tags: [mecanica, critico, dano, vocabulario]
fontes: ["https://wiki.warframe.com/w/Critical_Hit", "https://wiki.warframe.com/w/Damage/Calculation", "https://wiki.warframe.com/w/Damage_Type_Modifier", "https://wiki.warframe.com/w/Armor"]
atualizado: 2026-10-07
verificado: false
agente: opus
---

# Crítico

> [!info] Em uma linha
> Um dos dois eixos de escala de dano do jogo (o outro é status): chance crítica decide *com que frequência* o acerto é crítico, multiplicador crítico decide *quanto* ele multiplica — e acima de 100% de chance o Warframe entra em camadas de crítico que multiplicam ainda mais.


## ⚙️ Como Funciona — Crítico


Toda arma tem duas estatísticas de crítico: **Chance Crítica (CC)** e **Multiplicador Crítico (CM, "Critical Damage" no arsenal)**. A cada projétil disparado o jogo sorteia contra a CC; se acertar, o dano daquele projétil é multiplicado pelo CM. O sorteio é **por projétil**, não por disparo — uma escopeta com multishot 10 sorteia dez vezes.

O que torna o sistema interessante é que **a chance crítica não é limitada a 100%**. Ao passar de 100%, o excedente vira chance de subir de *camada* (tier): números amarelos são críticos normais, **laranjas ("Big Critical Hits") aparecem acima de 100%** de chance, e **vermelhos ("Super Critical Hits") acima de 200%**. Cada camada aplica o multiplicador crítico mais uma vez, o que faz o dano crescer em degraus, não linearmente.

Por isso builds de crítico têm um formato característico: primeiro você empurra a chance para além de 100% (mods de CC, [[mecanicas/combo_counter.md|combo counter]] via Blood Rush, buffs de aliados, arcanas), e só então investe em multiplicador — porque o multiplicador é aplicado uma vez por camada alcançada.


## 🔢 Fórmulas e Números — Crítico


### Chance crítica

```
Bônus RELATIVOS (mods percentuais, somam entre si antes de multiplicar):
   CC Total = CC Base × (1 + Soma dos Bônus Relativos)

Com bônus ABSOLUTOS (somados no fim, não escalam com a CC base):
   CC Total = CC Base × (1 + Bônus Relativos) + Bônus Absolutos

Com Blood Rush (escala com o multiplicador de combo de melee):
   CC Total = CC Base × (1 + Bônus Relativos + Blood Rush × (Combo − 1)) + Absolutos
```

| Variável | Significado | Fonte do valor |
|---|---|---|
| `CC Base` | Chance crítica da arma sem mods | Página da arma na wiki |
| `Bônus Relativos` | Mods de % de chance crítica (ex.: Point Strike +150%) | Página do mod |
| `Bônus Absolutos` | Bônus em pontos percentuais fixos, aplicados após a multiplicação | Página da fonte (arcana, habilidade) |
| `Blood Rush` | Multiplicador do mod Blood Rush | Página do mod |
| `Combo` | Multiplicador de combo de melee atual (2× a 12×) | [[mecanicas/combo_counter.md\|Combo Counter]] |

**Exemplo concreto:** arma com 25% de CC base + [[mods/armas/point_strike.md|Point Strike]] (+150%) → `0,25 × (1 + 1,50) = 0,625` = **62,5% de chance crítica**. Note que o mod multiplica a base — a mesma Point Strike numa arma de 5% de CC entrega só 12,5%. **Mods de crítico valem em armas que já têm crítico.**

### Dano médio esperado

```
Tiro Médio = Dano Total × (1 + CC × (CM − 1))
```

Com CC = 0,625 e CM = 2,0: `1 + 0,625 × 1,0 = 1,625` → **+62,5% de dano médio**.

### Camadas de crítico (tiers)

| Camada | Cor do número | Quando aparece |
|---|---|---|
| Não crítico | branco | sorteio falhou |
| Crítico | **amarelo** | CC abaixo de 100% |
| Big Critical Hit | **laranja** | chance crítica **acima de 100%** |
| Super Critical Hit | **vermelho** | chance crítica **acima de 200%** |

> [!warning] ⚠️ Fórmula de multiplicador por camada — NÃO VERIFICADA
> A wiki confirma a existência e os limiares das camadas (100% e 200%), mas a fórmula exata do multiplicador por camada **não foi confirmada nesta consulta**. A fórmula que se acredita correta, e que **deve ser tratada como não verificada**:
> ```
> NAO VERIFICADO
> Camada n = floor(CC Total)        // CC 2,3 -> camada 2 garantida, 30% de chance de camada 3
> Multiplicador de dano = 1 + n × (CM − 1)
>
> Ex.: CM = 2,0
>   camada 1 (amarelo)  -> ×2,0
>   camada 2 (laranja)  -> ×3,0
>   camada 3 (vermelho) -> ×4,0
> ```
> Confira em https://wiki.warframe.com/w/Critical_Hit antes de usar este número em qualquer cálculo.

**Tetos e limites conhecidos:**

| Limite | Valor | Observação |
|---|---|---|
| Teto de chance crítica | **não existe teto global** | Passar de 100% e 200% sobe de camada, não desperdiça |
| Teto de multiplicador crítico | não há teto conhecido | Escala com mods, arcanas e buffs |
| Camadas confirmadas | amarelo → laranja (>100%) → vermelho (>200%) | Camadas acima de vermelho existem mecanicamente, sem cor nova |
| Covenant (Harrow) | **+50% em corpo, +200% em headshot** | Teto do próprio buff |
| Crystallize (Citrine) | **300% de CC absoluta** | Sobrepõe todos os outros modificadores |
| Practiced Aim (Cyte-09) | **+300%** de bônus de CC | Teto do próprio buff |

> [!warning] ⚠️ Multiplicador de ponto fraco (headshot) — NÃO VERIFICADO
> O headshot entra na cadeia como `Tiro Médio no Ponto Fraco = Tiro Médio × (Mult. Ponto Fraco + Bônus de Dano em Ponto Fraco)`, mas o **valor base do multiplicador de ponto fraco por tipo de inimigo não foi verificado** aqui. Não invente "×2".


## 📋 Tabelas de Referência — Crítico


### Onde o crítico entra na cadeia de dano

| Ordem | Etapa | Observação |
|---|---|---|
| 1 | Dano base moddado por tipo | Físico + elemental |
| 2 | Quantização em passos de 1/32 | `Quantizado(x) = sign(x) × floor(\|x\|×32+0,5)/32` |
| 3 | **Crítico** | `× (1 + CC × (CM − 1))` na média, ou o multiplicador da camada no acerto individual |
| 4 | Ponto fraco / headshot | Multiplica o resultado do crítico |
| 5 | Modificador de facção | ×1,5 se vulnerável, ×0,5 se resistente, ×1,0 neutro ([[mecanicas/dano_e_status.md\|Dano e Status]]) |
| 6 | Redução por armadura | `1 − 0,9 × raiz(Armadura/2700)` para inimigo com até 2.700 de armadura |

O crítico é aplicado **antes** do modificador de facção e da armadura. Ou seja: crítico e escolha de elemento são multiplicativos entre si — não competem, se somam em valor.

### Mods de crítico por categoria de arma

| Categoria | Chance crítica | Multiplicador crítico |
|---|---|---|
| Rifle / primária | [[mods/armas/point_strike.md\|Point Strike]], [[mods/armas/critical_delay.md\|Critical Delay]] (+CC, −cadência), [[mods/armas/argon_scope.md\|Argon Scope]] (condicional em headshot) | [[mods/armas/vital_sense.md\|Vital Sense]] |
| Pistola / secundária | [[mods/armas/pistol_gambit.md\|Pistol Gambit]], [[mods/armas/primed_pistol_gambit.md\|Primed Pistol Gambit]] | [[mods/armas/target_cracker.md\|Target Cracker]], [[mods/armas/primed_target_cracker.md\|Primed Target Cracker]] |
| Melee | [[mods/armas/true_steel.md\|True Steel]], [[mods/armas/blood_rush.md\|Blood Rush]] (escala com combo) | [[mods/armas/organ_shatter.md\|Organ Shatter]] |

**Mods que interagem:**
[[mods/armas/blood_rush.md|Blood Rush]] — o pilar de melee crítico: escala CC com o multiplicador de combo, é o que leva armas brancas de 20% a camada vermelha · [[mods/armas/split_chamber.md|Split Chamber]] (+90% de multishot em rifles) — cada projétil sorteia crítico separadamente, então multishot multiplica críticos · [[mods/armas/hunter_munitions.md|Hunter Munitions]] — converte acertos **críticos** em procs de Slash que ignoram armadura, ligando build de crítico a dano de status · [[mods/armas/critical_delay.md|Critical Delay]] · [[mods/armas/argon_scope.md|Argon Scope]] · [[mods/armas/vigilante_armaments.md|Vigilante Armaments]] (conjunto Vigilante: chance de elevar a camada de crítico)

**Frames que interagem:**
[[warframes/regular/citrine.md|Citrine]] — Crystallize fixa 300% de CC absoluta na área · [[warframes/regular/kullervo.md|Kullervo]] — crítico alto nativo em melee · [[warframes/regular/wisp.md|Wisp]] — motes de buff de dano · [[warframes/regular/gauss.md|Gauss]] · [[warframes/regular/xaku.md|Xaku]] (remove armadura, o que amplifica o dano crítico que chega)


## ⚠️ Erros Comuns — Crítico


1. **Colocar mods de crítico em arma sem crítico.** Mods de CC são **relativos**: multiplicam a base. Point Strike numa arma de 5% de CC entrega 12,5%; na mesma arma um mod de status ou de dano bruto vale muito mais. Regra prática: crítico compensa a partir de ~20% de CC base.

2. **Achar que 100% de chance crítica é o teto.** É o oposto: 100% é onde o sistema **começa a ficar bom**. Acima disso o excedente vira chance de camada laranja, e acima de 200% de camada vermelha. Investir em CC além de 100% não é desperdício.

3. **Investir em multiplicador antes de chance.** O multiplicador é aplicado uma vez por camada. Subir a chance de 100% para 200% costuma valer mais que dobrar o multiplicador, porque adiciona uma camada inteira.

4. **Confundir "Critical Damage" com "dano crítico total".** O número no arsenal é o **multiplicador**, não o dano resultante. CM 2,0 significa "×2 no acerto crítico", não "+200%".

5. **Tratar crítico e status como escolhas excludentes.** [[mods/armas/hunter_munitions.md|Hunter Munitions]] e [[mods/armas/blood_rush.md|Blood Rush]] existem exatamente para juntá-los. Builds de melee de topo são crítico *e* status.

6. **Esquecer que o sorteio é por projétil.** Multishot multiplica críticos. [[mods/armas/split_chamber.md|Split Chamber]] é, indiretamente, um mod de crítico.

7. **Assumir a fórmula de multiplicador por camada.** Ela está marcada como ⚠️ NÃO VERIFICADO neste arquivo por um motivo. Não a cite como fato.

8. **Aplicar crítico depois da armadura no cálculo mental.** O crítico entra **antes** do modificador de facção e da redução por armadura. Contra alvo blindado, o número que aparece na tela já passou pela armadura — o crítico não "furou" nada.


## 🔗 Relacionados — Crítico


- [[mecanicas/dano_e_status.md|Dano e Status]] — o outro eixo de escala. Viral (+325% de dano na vida) e Corrosivo (−80% de armadura) multiplicam o dano crítico que chega ao alvo.
- [[mecanicas/combo_counter.md|Combo Counter]] — em melee, o multiplicador de combo (até 12×) é o que alimenta Blood Rush e leva a chance crítica a camada vermelha.
- [[mecanicas/incarnon.md|Incarnon]] — muitas formas Incarnon elevam drasticamente a chance ou o multiplicador crítico ao evoluir.
- [[mecanicas/steel_path.md|Steel Path]] — com inimigos a 2,5× de vida, camadas de crítico deixam de ser luxo.
- [[mecanicas/forma_e_polaridades.md|Forma e Polaridades]] — mods de crítico são caros em drenagem; polarizar é o que faz o build fechar.
- [[mecanicas/operator_e_focus.md|Operator e Focus]] — a escola Naramon dá bônus ligados a crítico de melee.
- [[mecanicas/augments.md|Augments]] — vários augments convertem crítico em efeito de status ou em dano de área.

---
