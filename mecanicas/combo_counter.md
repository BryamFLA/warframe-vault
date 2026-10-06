---
title: Combo Counter
aliases: [Combo Counter]
tipo: mecanica
resumo: "Combo Counter — Contador de acertos consecutivos de arma branca que multiplica o dano de melee de 2× até 12× — e, com Blood Rush e Weeping Wounds, escala também chance crítica e chance de status."
status: completo
rag: true
tags: [mecanica, melee, combo, dano, vocabulario]
fontes: ["https://wiki.warframe.com/w/Melee_Combo_Counter", "https://wiki.warframe.com/w/Critical_Hit"]
atualizado: 2026-10-07
verificado: false
agente: opus
---

# Combo Counter

> [!info] Em uma linha
> Contador de acertos consecutivos de arma branca que multiplica o dano de melee de 2× até 12× — e, com Blood Rush e Weeping Wounds, escala também chance crítica e chance de status. É o que faz melee escalar para nível alto.


## ⚙️ Como Funciona — Combo Counter


Cada acerto de arma branca (e cada bloqueio) adiciona 1 ao **contador de combo**. Ao cruzar limiares de contagem, o contador sobe de **camada**, e cada camada multiplica o dano de melee: 20 acertos = 2×, 40 = 3×, e assim até 220 acertos = 12×. O contador tem um **temporizador de 5 segundos** que reinicia a cada novo acerto ou bloqueio; se você parar de bater, ele expira e o combo zera.

O multiplicador de dano é só metade do valor. A outra metade é que **três famílias de mods leem o multiplicador de combo como variável de entrada**: [[mods/armas/blood_rush.md|Blood Rush]] escala chance crítica com ele, [[mods/armas/weeping_wounds.md|Weeping Wounds]] escala chance de status, e o conjunto Gladiator dá bônus que crescem com a camada. É por isso que uma arma branca de 20% de chance crítica base chega a camada vermelha de crítico em combate real — o combo faz o trabalho.

O combo também é **moeda**: o **Heavy Attack** consome o contador para converter em um golpe pesado, entregando entre 2× e 12× de dano de uma vez. Mods de eficiência de heavy attack reduzem esse consumo (com teto de 90%, então sempre restam 10% consumidos), permitindo golpes pesados repetidos sem perder o combo acumulado.


## 🔢 Fórmulas e Números — Combo Counter


```
Dano de melee com combo:
   Dano = Dano Base Moddado × Multiplicador de Combo

Chance crítica com Blood Rush:
   CC Total = CC Base × (1 + Bônus Relativos + Blood Rush × (Combo − 1)) + Absolutos

Chance de status com Weeping Wounds:
   Status Total = Status Base × (1 + Bônus Relativos + Weeping Wounds × (Combo − 1))
   [NAO VERIFICADO - forma da fórmula inferida por simetria com Blood Rush;
    confira em https://wiki.warframe.com/w/Weeping_Wounds]

Heavy Attack:
   Consumo padrão = 100% do contador de combo
   Dano entregue  = entre 2× e 12×, conforme a camada gasta
   Com mods de eficiência (teto 90%): consumo mínimo = 10% do contador
```

| Variável | Significado | Fonte do valor |
|---|---|---|
| `Multiplicador de Combo` | 2,0 a 12,0 conforme a camada atingida | Tabela abaixo |
| `Combo` | O mesmo multiplicador, usado como número na fórmula (ex.: 12,0) | Tabela abaixo |
| `Blood Rush` | Valor do mod Blood Rush no rank máximo | Página do mod |
| `Weeping Wounds` | Valor do mod Weeping Wounds no rank máximo | Página do mod |
| `CC Base` | Chance crítica da arma branca sem mods | Página da arma |

**Tetos e limites conhecidos:**

| Limite | Valor | Observação |
|---|---|---|
| Multiplicador máximo de combo | **12×** (220 acertos) | Padrão para praticamente todas as armas brancas |
| Exceção conhecida | **Venka Prime: 13×** (240 acertos) | Única arma com camada extra |
| Temporizador base do combo | **5 segundos** | Renovado a cada acerto ou bloqueio |
| Teto de eficiência de Heavy Attack | **90%** | Sempre resta 10% do contador consumido |
| Dano de Heavy Attack | 2× a 12× | Conforme a camada gasta |
| Decaimento com Naramon (Power Spike) | 20 / 15 / 10 / 5 pontos por ciclo | O combo **decai** em vez de zerar |

> [!warning] ⚠️ Valores por rank de mod não verificados
> Os valores exatos de Blood Rush, Weeping Wounds, Body Count, Drifting Contact, Corrupt Charge e do conjunto Gladiator por rank **não foram verificados** nesta consulta. Não cite números de rank de mod a partir deste arquivo — abra a página do mod.


## 📋 Tabelas de Referência — Combo Counter


### Tabela de camadas de combo

| Camada | Multiplicador | Acertos necessários |
|---|---|---|
| 1 | 1,0× | 0 |
| 2 | **2,0×** | 20 |
| 3 | 3,0× | 40 |
| 4 | 4,0× | 60 |
| 5 | 5,0× | 80 |
| 6 | 6,0× | 100 |
| 7 | 7,0× | 120 |
| 8 | 8,0× | 140 |
| 9 | 9,0× | 160 |
| 10 | 10,0× | 180 |
| 11 | 11,0× | 200 |
| 12 | **12,0×** | 220 |
| 13 (só Venka Prime) | 13,0× | 240 |

Padrão: **20 acertos por camada**, multiplicador igual ao número da camada.

### O que renova e o que perde o combo

| Ação | Efeito no combo |
|---|---|
| Acerto de arma branca | +1 e renova o temporizador de 5s |
| Bloqueio | +1 e renova o temporizador |
| Heavy Attack (sem mods de eficiência) | **consome 100%** do contador |
| Heavy Attack (com 90% de eficiência) | consome 10% do contador |
| Temporizador expirar | zera o contador — **exceto** com Naramon Power Spike, que faz decair |
| Trocar de arma / usar arma de fogo | o temporizador continua correndo; nada renova |

### Interações principais

| Mod / fonte | O que faz com o combo |
|---|---|
| [[mods/armas/blood_rush.md\|Blood Rush]] | Escala **chance crítica** com o multiplicador de combo — o mod mais importante de melee crítico |
| [[mods/armas/weeping_wounds.md\|Weeping Wounds]] | Escala **chance de status** com o multiplicador de combo |
| [[mods/armas/body_count.md\|Body Count]] | Aumenta a duração do temporizador de combo |
| [[mods/armas/drifting_contact.md\|Drifting Contact]] | Aumenta a duração do temporizador **e** a chance de status |
| [[mods/armas/corrupt_charge.md\|Corrupt Charge]] | Inicia o combo com contagem, ao custo de eficiência de heavy attack |
| [[mods/armas/quickening.md\|Quickening]] | Velocidade de ataque — mais acertos por segundo, combo mais rápido |
| [[mods/armas/condition_overload.md\|Condition Overload]] | Não lê combo, mas é o par natural: dano por tipo distinto de status ativo no alvo |
| [[mods/armas/life_strike.md\|Life Strike]] | Cura em heavy attack, convertendo combo em sustentação |
| Conjunto Gladiator | Bônus de conjunto que escalam com a camada de combo |
| Naramon — Power Spike ([[mecanicas/operator_e_focus.md\|Focus]]) | Faz o combo **decair** 20/15/10/5 pontos por ciclo em vez de zerar |

**Frames que interagem:**
[[warframes/regular/kullervo.md|Kullervo]] — construído em torno de melee crítico e combo · [[warframes/regular/valkyr.md|Valkyr]] — Hysteria mantém melee contínuo · [[warframes/regular/excalibur.md|Excalibur]] — Exalted Blade usa mods de melee · [[warframes/regular/gauss.md|Gauss]] — velocidade de ataque acelera o acúmulo · [[warframes/regular/wisp.md|Wisp]] — mote de velocidade de ataque


## 🛠️ Como Usar na Prática — Combo Counter


| Objetivo | O que fazer |
|---|---|
| Chegar a 12× rápido | Arma branca de ataque rápido e alcance grande contra grupos. 220 acertos com multishot de melee (Gemini Cross e similares) e alcance vêm em segundos |
| Manter 12× entre grupos | [[mods/armas/body_count.md\|Body Count]] ou [[mods/armas/drifting_contact.md\|Drifting Contact]] para estender o temporizador, e Naramon Power Spike para decair em vez de zerar |
| Transformar combo em crítico | [[mods/armas/blood_rush.md\|Blood Rush]]. Com 12× de combo, uma arma de chance crítica média passa de 100% e entra em camada laranja/vermelha ([[mecanicas/critico.md\|Crítico]]) |
| Transformar combo em status | [[mods/armas/weeping_wounds.md\|Weeping Wounds]], e depois [[mods/armas/condition_overload.md\|Condition Overload]] para converter a variedade de status em dano |
| Build de Heavy Attack | Mods de eficiência de heavy attack até o teto de 90%, para golpear pesado repetidamente gastando só 10% do contador por golpe |
| Build de dano contínuo | Ignore heavy attack, mantenha 12× permanente e deixe Blood Rush + Weeping Wounds fazerem o trabalho |
| Sustentar vida em melee | [[mods/armas/life_strike.md\|Life Strike]] em heavy attack, ou [[mods/armas/healing_return.md\|Healing Return]] curando por status ativo no alvo |


## ⚠️ Erros Comuns — Combo Counter


1. **Achar que combo só multiplica dano.** O multiplicador de dano (até 12×) é a parte menos importante em nível alto. O valor real está em Blood Rush e Weeping Wounds, que usam o combo como variável para crítico e status.

2. **Dar Heavy Attack sem mods de eficiência num build de combo contínuo.** Sem eficiência, um heavy attack **zera 100% do contador** — você troca todo o crítico e status escalados por um único golpe.

3. **Esquecer que bloquear conta.** Bloqueio adiciona ao contador e renova o temporizador. Serve para manter combo enquanto você reposiciona.

4. **Confundir duração de combo com decaimento.** Body Count e Drifting Contact **estendem o temporizador**; Naramon Power Spike faz o combo **decair em vez de zerar**. São efeitos diferentes e se somam.

5. **Assumir que toda arma vai a 13×.** O teto é **12×** (220 acertos). Venka Prime é a exceção conhecida com 13× (240 acertos).

6. **Contar camadas errado.** São **20 acertos por camada**, e o multiplicador é o número da camada — 220 acertos dão 12×, não 11× nem 220×.

7. **Citar valores de rank de Blood Rush ou Weeping Wounds a partir deste arquivo.** Estão marcados como ⚠️ não verificados de propósito. Abra a página do mod.

8. **Tratar o temporizador como pausado ao usar arma de fogo.** Ele continua correndo. Trocar para primária por mais de 5 segundos perde o combo (salvo Power Spike).


## 🔗 Relacionados — Combo Counter


- [[mecanicas/critico.md|Crítico]] — o destino principal do combo. Blood Rush converte 12× de combo em camada laranja/vermelha de crítico; camadas aparecem acima de 100% e 200% de chance crítica.
- [[mecanicas/dano_e_status.md|Dano e Status]] — Weeping Wounds converte combo em chance de status; status como Viral (+325% de dano na vida) e Corrosivo (−80% de armadura) é o que faz o dano de melee escalar.
- [[mecanicas/operator_e_focus.md|Operator e Focus]] — a escola **Naramon** dá Power Spike, que troca o zeramento do combo por decaimento gradual.
- [[mecanicas/stealth_e_finishers.md|Stealth e Finishers]] — finishers e ataques furtivos interagem com o contador e com multiplicadores de dano furtivo.
- [[mecanicas/incarnon.md|Incarnon]] — várias armas brancas Incarnon usam o contador de combo como gatilho ou recurso de evolução.
- [[mecanicas/steel_path.md|Steel Path]] — com inimigos a 2,5× de vida, melee sem combo escalado não sustenta.
- [[mecanicas/forma_e_polaridades.md|Forma e Polaridades]] — Blood Rush, Weeping Wounds e Condition Overload juntos são caros em drenagem; polarizar é obrigatório.

---
