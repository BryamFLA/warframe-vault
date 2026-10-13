---
title: Dano e Status
aliases: [Dano e Status]
tipo: mecanica
resumo: Sistema que decide quanto dano cada tipo causa contra cada facção e que efeito de status cada tipo aplica.
status: completo
rag: true
tags: [mecanica, dano, status, elementos, armadura, vocabulario]
fontes: ["https://wiki.warframe.com/w/Damage", "https://wiki.warframe.com/w/Damage_Type_Modifier", "https://wiki.warframe.com/w/Damage/Calculation", "https://wiki.warframe.com/w/Damage/Grineer", "https://wiki.warframe.com/w/Damage/Corpus", "https://wiki.warframe.com/w/Damage/Infested", "https://wiki.warframe.com/w/Damage/Techrot", "https://wiki.warframe.com/w/Status_Effect"]
atualizado: 2026-10-07
verificado: false
agente: opus
---

# Dano e Status

> [!info] Em uma linha
> Sistema que decide quanto dano cada tipo causa contra cada facção e que efeito de status cada tipo aplica. É a camada de vocabulário de toda arma, mod e habilidade do jogo.

> [!danger] Damage 3.0 — a tabela antiga por tipo de saúde/armadura está OBSOLETA
> Desde a **Update 36.0 (18/06/2024)** o jogo usa **Damage 3.0**: os modificadores deixaram de ser "por tipo de saúde/armadura" (Ferrite, Alloy, Cloned Flesh, Proto Shield...) e passaram a ser **por facção**, com apenas dois valores possíveis — **Vulnerável `+` = ×1,5** e **Resistente `-` = ×0,5**.
> Guias, vídeos e planilhas de antes de junho de 2024 (e boa parte da internet) ainda citam a tabela Damage 2.0 com valores como "Corrosivo +75% contra Ferrite". **Isso não vale mais.** A tabela antiga está preservada mais abaixo apenas como referência histórica.


## ⚙️ Como Funciona — Dano e Status


Todo dano no jogo é um **pacote de tipos**, não um número único. Uma Braton com Serration e Stormbringer não dispara "500 de dano": dispara uma parcela de Impact, uma de Puncture, uma de Slash e uma de Electricity, e **cada parcela é calculada separadamente** contra o alvo. Por isso um mod que só adiciona elemento pode valer mais que um que adiciona dano bruto, e por isso o mesmo build tem desempenho diferente contra Grineer e contra Corpus.

Cada parcela passa por três filtros independentes: o **modificador de facção** (×1,5, ×1,0 ou ×0,5), a **redução por armadura** (se o alvo tem armadura e o tipo não a ignora) e os **buffs/debuffs ativos no alvo** (Viral, Corrosivo, Heat, Magnetic). Os resultados são somados no fim. Um tipo pode estar em ×1,5 enquanto outro no mesmo tiro está em ×0,5.

Separado do dano, cada tipo tem um **efeito de status** (proc) com chance própria de disparar. O status é frequentemente mais importante que o dano: Viral e Corrosivo multiplicam o dano de *tudo* que vem depois, e Slash e Toxin causam dano que ignora armadura e escudo respectivamente. Buildar status é buildar dano.


## 🔢 Fórmulas e Números — Dano e Status


### Cadeia de cálculo (Damage 3.0)

```
1) Dano base moddado (por tipo, no Arsenal):
   Dano Total = Dano Base
              × [1 + Bônus Elementais + Distribuição Física × Bônus Físicos]
              × (1 + Bônus de Dano)
              × [Multishot Base × (1 + Bônus de Multishot)]

2) Quantização (o jogo arredonda em passos de 1/32 do dano base):
   Scale        = Dano Base Moddado / 32
   Quantizado(x) = sign(x) × floor(|x| × 32 + 0,5) / 32

3) Crítico (média esperada):
   Tiro Médio = Dano Total × (1 + Chance Crítica × (Multiplicador Crítico − 1))

4) Ponto fraco / headshot:
   Tiro Médio no Ponto Fraco = Tiro Médio × (Mult. Ponto Fraco + Bônus de Dano em Ponto Fraco)

5) Modificador de facção, por tipo de dano:
   Vulnerável (+) = ×1,5     Neutro = ×1,0     Resistente (−) = ×0,5

6) Redução por armadura (só para tipos que não ignoram armadura):
   DM = 1 − 0,9 × raiz(AR / 2700)          [AR = armadura líquida do inimigo]

7) Soma final:
   Dano Infligido = SD1×DM1 + SD2×DM2 + ... + SDn×DMn
   [SD = valor moddado daquele tipo de dano; DM = multiplicador daquele tipo]
```

| Variável | Significado | Fonte do valor |
|---|---|---|
| `Dano Base` | Dano do arsenal sem mods, dividido entre os tipos da arma | Página da arma na wiki |
| `Bônus Elementais` | Soma dos mods elementais (ex.: Stormbringer +90% Elétrico) | Página do mod |
| `Distribuição Física` | Fração do dano base que é Impact/Puncture/Slash | Página da arma |
| `Multishot` | Projéteis por disparo (Split Chamber +90% = 1,9 média) | Página do mod |
| `AR` | Armadura líquida do inimigo, **depois** de Corrosivo/Heat/Shattering Impact | Calculada em jogo |
| `DM` | Multiplicador restante após armadura (1 = sem redução) | Fórmula acima |
| `SD` | Valor moddado de um tipo de dano específico | Cálculo |

### Armadura — as duas fórmulas

```
Redução de dano de INIMIGO (armadura líquida ≤ 2.700):
   Redução = 0,9 × raiz(Armadura Líquida / 2700)
   → o teto natural dessa fórmula é 90% de redução, alcançado em 2.700 de armadura

Redução de dano do TENNO (Warframe, Necramech, companheiro)
e de inimigo com armadura acima de 2.700:
   Redução = Armadura / (Armadura + 300)

Vida efetiva (fórmula Tenno):
   Vida Efetiva = Vida Nominal × (Armadura + 300) / 300
```

**Tetos e limites conhecidos:**

| Limite | Valor | Observação |
|---|---|---|
| Modificador de facção — vulnerável | ×1,5 (+50%) | Valor único; não existe "+75%" no Damage 3.0 |
| Modificador de facção — resistente | ×0,5 (−50%) | Valor único |
| Piso de modificador com buffs externos | −100% (×0) | Buffs/debuffs de mods podem empurrar o modificador até 0, nunca abaixo |
| Redução por armadura de inimigo | 90% na fórmula da raiz | Alcançado em 2.700 de armadura líquida |
| Armadura de inimigo por escala de nível | limitada entre 200 e 2.700 | ⚠️ multiplicador exato por nível NÃO VERIFICADO |
| Redução por armadura do Tenno | assintótica, nunca chega a 100% | 300 armadura = 50%; 900 = 75% |
| Elementos primários por arma via mods | 2 | Um terceiro mod primário força uma combinação |
| Elementos combinados simultâneos | 2 | Ex.: Corrosivo + Heat, ou Viral + Heat |
| Stacks de status (maioria) | 10 | Impact e Puncture são 5; Slash/Heat/Electricity/Toxin são ilimitados |

> [!warning] Empilhamento de resistências é multiplicativo
> Modificadores não se somam. Quatro resistências de 25% resultam em `0,75 × 0,75 × 0,75 × 0,75 = 31,5%` do dano passando (68,5% de redução), não 100% de redução. Desde a U36.0 o cálculo opera sobre o "dano restante", um modificador por vez.


## 📋 Tabelas de Referência — Dano e Status


### Modificadores por FACÇÃO — Damage 3.0 (tabela ATUAL)

`+` = ×1,5 (leva 50% mais dano) · `-` = ×0,5 (leva metade do dano) · em branco = neutro (×1,0)

| Facção | Vulnerável `+` | Resistente `-` |
|---|---|---|
| Tenno | — | — |
| Grineer | Impact, Corrosivo | — |
| Kuva Grineer | Corrosivo | Heat |
| Corpus | Puncture, Magnetic | — |
| Corpus Amalgam | Electricity, Magnetic | Blast |
| Infested | Slash, Heat | — |
| Infested Deimos | Gas | Viral |
| Orokin (Corrupted) | Puncture | Radiation |
| Sentient | Cold, Radiation | Corrosivo |
| Narmer | Toxin | Magnetic |
| The Murmur | Electricity | Radiation |
| Zariman | Void | — |
| Scaldra | Corrosivo | Gas |
| Techrot | Magnetic, Gas | Cold |
| Anarchs | Cold, Magnetic | Radiation |

> [!warning] ⚠️ Divergência não resolvida na própria wiki
> A página `Damage_Type_Modifier` lista **Gas** como terceira vulnerabilidade dos Infested; a página `Damage/Infested` lista apenas **Slash e Heat**. Trate Gas contra Infested comum como **⚠️ NÃO VERIFICADO**. Contra **Infested Deimos** o Gas é confirmado.

**Leitura prática por facção:**

| Contra | Use | Porque |
|---|---|---|
| Grineer ([[lore/faccoes/grineer.md\|Grineer]]) | Corrosivo (Elétrico + Tóxico) | +50% de dano *e* o status remove até 80% da armadura, que é o que segura o Grineer |
| Kuva Grineer / Kuva Lich | Corrosivo | +50%; **evite Heat**, eles resistem (×0,5) |
| Corpus ([[lore/faccoes/corpus.md\|Corpus]]) | Magnetic (Frio + Elétrico) ou Puncture | +50%; Magnetic também amplifica dano em escudo e bloqueia recarga |
| Infested ([[lore/faccoes/infested.md\|Infested]]) | Heat ou Slash | +50%; Heat ainda causa pânico e remove armadura |
| Infested de Deimos | Gas | +50%; **evite Viral**, resistem |
| Corrupted / Orokin ([[lore/faccoes/orokin.md\|Orokin]]) | Puncture | +50%; **evite Radiation** |
| Sentient ([[lore/faccoes/sentient.md\|Sentient]]) | Radiation ou Cold | +50%; **evite Corrosivo** |
| Narmer | Toxin | +50%; **evite Magnetic** |
| The Murmur ([[lore/faccoes/murmur.md\|The Murmur]]) | Electricity | +50%; **evite Radiation** |
| Zariman (Void) | Void | Dano de Void do Operator/Amp |
| Techrot (1999) | Magnetic ou Gas | +50%; **evite Cold** |

### Tipos físicos e seus status

| Tipo | Onde vem | Efeito de status | Duração | Stacks |
|---|---|---|---|---|
| **Impact** | Dano base de armas de concussão | Faz o alvo cambalear/tropeçar por 1s; aumenta o limiar de finisher do Parazon | 1s | 5 |
| **Puncture** | Dano base de armas perfurantes | Reduz o dano que o inimigo causa em 40% por stack | 10s | 5 (−80%) |
| **Slash** | Dano base de armas cortantes | **Bleed:** 35% do dano base por segundo, começa após 1s de atraso; **ignora armadura** | 6s | ilimitado |

> [!warning] ⚠️ Números divergentes entre páginas da wiki
> Para Impact, a página `Status_Effect` indica **+40% no limiar de finisher do Parazon** com 5 stacks, enquanto a página `Damage` indica **até +80%**. Trate como **⚠️ NÃO VERIFICADO**.
> Para Puncture, a página `Damage` acrescenta **+5% de chance crítica recebida por stack (até +25%)** — não confirmado na página `Status_Effect`. Trate como **⚠️ NÃO VERIFICADO**.

### Elementos primários

| Elemento | Efeito de status | Duração | Stacks | No máximo |
|---|---|---|---|---|
| **Heat** | 50% do dano base por segundo; causa pânico; **remove armadura** | 6s | ilimitado (dano) | até **50% de armadura removida** |
| **Cold** | Reduz velocidade e cadência de tiro (50% no 1º stack) | 6s | 10 | **90% de lentidão** no 9º stack; 10º congela |
| **Electricity** | 50% do dano base por segundo; encadeia para inimigos em **3 m**; atordoa | 6s | ilimitado (dano) | corrente contínua entre alvos próximos |
| **Toxin** | 50% do dano base por segundo; **ignora escudo**, bate direto na vida | 6s | ilimitado | — |

### Elementos combinados

| Elemento | Receita | Efeito de status | Duração | Stacks | No máximo |
|---|---|---|---|---|---|
| **Blast** | Heat + Cold | Explosão em área após ~1,5s; 30% do dano base | variável | 10 | detonação de **300%** do dano em raio de 5 m |
| **Corrosivo** | Electricity + Toxin | **Remove 26% da armadura** por stack | 8s | 10 | **80% de armadura removida** |
| **Gas** | Heat + Toxin | Nuvem de dano em área; 50% do dano base por segundo | 6s | 10 | raio de **6 m** (+0,3 m por stack) |
| **Magnetic** | Cold + Electricity | Amplifica dano em **escudo e overguard**; bloqueia recarga de escudo | 6s | 10 | **+325%** de dano em escudo |
| **Radiation** | Heat + Electricity | Fogo amigo: o inimigo ataca os próprios aliados | 12s | 10 | **+550%** de dano entre inimigos (9º stack) |
| **Viral** | Cold + Toxin | Amplifica **dano na vida** (+100% no 1º stack) | 6s | 10 | **+325%** de dano na vida |

### Ordem de combinação dos elementos (regra de posicionamento de mod)

```
A ordem de leitura é a ordem dos SLOTS: do canto superior esquerdo (primeiro)
para o inferior direito (último).

Slots 1,2 = Frio + Elétrico  -> Magnetic
Slots 3,4 = Heat + Tóxico    -> Gas
Resultado: arma com Magnetic + Gas

Mesmos 4 mods, ordem diferente:
Slots 1,2 = Frio + Tóxico    -> Viral
Slots 3,4 = Heat + Elétrico  -> Radiation
Resultado: arma com Viral + Radiation
```

- Hierarquia interna quando há empate de leitura: **Heat > Cold > Electricity > Toxin**.
- **Elemento innato da arma** (ex.: Toxin nativo da Torid) é considerado **por último** — ele não entra na combinação e sai como elemento separado, **a menos que** você equipe um mod do mesmo elemento, que o "puxa" para a posição daquele mod na hierarquia. É assim que se converte innato em combinado.
- Só é possível ter **2 elementos primários por arma via mods**. Um terceiro mod primário força duas a se combinarem.

### Chance de status e procs

```
Chance de status é POR PROJÉTIL, não por disparo.

Procs médios por disparo = Multishot × Chance de Status por projétil
   Ex.: escopeta com 10 pellets e 12% de status = 1,2 procs por tiro em média

Qual tipo procou = Dano daquele tipo / Dano total do tiro
   Ex.: arma com 60% do dano em Corrosivo tem 60% de chance de o proc ser Corrosivo
```

- Chance de status **acima de 100%** garante 1 proc e dá chance de procs adicionais no mesmo acerto.
- Isso torna **multishot um multiplicador de status**, não só de dano — [[mods/armas/split_chamber.md|Split Chamber]] (+90% de multishot em rifles) aumenta procs na mesma proporção.

### ⛔ Tabela Damage 2.0 (OBSOLETA — apenas referência histórica)

> [!danger] NÃO USE PARA BUILDS
> Estes valores valiam **até a Update 36.0 (18/06/2024)**. Estão aqui porque a maior parte dos guias antigos os cita, e porque o vault precisa poder identificar quando uma fonte está desatualizada.

| Tipo de dano | Ferrite | Alloy | Cloned Flesh | Flesh | Infested | Infested Flesh | Infested Sinew | Fossilized | Machinery | Robotic | Shield | Proto Shield |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Impact | — | — | −25% | −25% | — | — | — | — | +25% | — | +50% | +15% |
| Puncture | +50% | +15% | — | — | — | — | +25% | — | — | +25% | −20% | — |
| Slash | −15% | −50% | +25% | +25% | +25% | +50% | — | +15% | — | −25% | — | −50% |
| Cold | — | +25% | — | — | — | −50% | +25% | −25% | — | — | +50% | — |
| Electricity | — | −50% | — | — | — | — | — | — | +50% | +50% | — | — |
| Heat | — | — | +25% | — | +25% | +50% | — | — | — | — | — | −50% |
| Toxin | — | — | — | +50% | — | — | — | −50% | −25% | −25% | ignora | ignora |
| Blast | −25% | — | — | — | — | — | −50% | +50% | +75% | — | — | — |
| Corrosivo | **+75%** | — | — | — | — | — | — | +75% | — | — | — | −50% |
| Gas | — | — | −50% | −25% | +75% | +50% | — | — | — | — | — | — |
| Magnetic | — | −50% | — | — | — | — | — | — | — | — | +75% | +75% |
| Radiation | — | +75% | — | — | −50% | — | +50% | −75% | — | +25% | −25% | — |
| Viral | — | — | +75% | +50% | −50% | — | — | — | −25% | — | — | — |
| True / Void | — | — | — | — | — | — | — | — | — | — | — | — |


## 🛠️ Como Usar na Prática — Dano e Status


| Objetivo | O que fazer |
|---|---|
| Matar Grineer de nível alto | Corrosivo (Elétrico + Tóxico). Ganha +50% por facção e o status tira até 80% da armadura em 10 stacks |
| Matar Corpus rápido | Magnetic (Frio + Elétrico) para derrubar escudo com +325% de dano, e o dano na vida entra limpo depois |
| Multiplicar o dano de qualquer coisa | Viral (Frio + Tóxico) primeiro. 10 stacks = **+325% de dano na vida**. É o maior multiplicador acessível do jogo |
| Ignorar armadura sem remover armadura | Slash. O bleed do proc **passa por armadura**. Base de builds com [[mods/armas/hunter_munitions.md\|Hunter Munitions]], que converte acertos críticos em procs de Slash |
| Ignorar escudo | Toxin. O dano do proc bate direto na vida, mesmo com escudo cheio |
| Remover armadura sem Corrosivo | Heat — o status tira até 50% da armadura e ainda causa dano por segundo e pânico |
| Combinação de dano geral mais forte | **Viral + Heat**: Viral multiplica o dano na vida, Heat remove armadura e causa DoT. Cobre quase tudo |
| Converter elemento innato em combinado | Equipe um mod do **mesmo** elemento innato. Ele sobe na hierarquia e passa a combinar com o outro elemento |
| Escalar status em melee | [[mecanicas/combo_counter.md\|Combo Counter]] + [[mods/armas/weeping_wounds.md\|Weeping Wounds]], que escala chance de status com o multiplicador de combo |
| Escalar dano por variedade de status | [[mods/armas/condition_overload.md\|Condition Overload]] — dano de melee aumenta por **tipo distinto** de status ativo no alvo |

**Mods que interagem:**
[[mods/armas/serration.md|Serration]] · Primed Serration · [[mods/armas/split_chamber.md|Split Chamber]] · [[mods/armas/stormbringer.md|Stormbringer]] (Elétrico) · [[mods/armas/infected_clip.md|Infected Clip]] (Tóxico) · [[mods/armas/hellfire.md|Hellfire]] (Heat) · [[mods/armas/cryo_rounds.md|Cryo Rounds]] (Frio) · [[mods/armas/primed_cryo_rounds.md|Primed Cryo Rounds]] · [[mods/armas/high_voltage.md|High Voltage]] · [[mods/armas/thermite_rounds.md|Thermite Rounds]] · [[mods/armas/pathogen_rounds.md|Pathogen Rounds]] · [[mods/armas/frostbite.md|Frostbite]] · [[mods/armas/scorch.md|Scorch]] · [[mods/armas/convulsion.md|Convulsion]] · [[mods/armas/hunter_munitions.md|Hunter Munitions]] · [[mods/armas/hemorrhage.md|Hemorrhage]] · [[mods/armas/condition_overload.md|Condition Overload]] · [[mods/armas/weeping_wounds.md|Weeping Wounds]] · [[mods/warframe/corrosive_projection.md|Corrosive Projection]] (aura, remove armadura da esquadra)

**Frames que interagem:**
[[warframes/regular/saryn.md|Saryn]] (espalha Viral e Corrosivo por contágio) · [[warframes/regular/nidus.md|Nidus]] · [[warframes/regular/mag.md|Mag]] (foca escudo Corpus) · [[warframes/regular/oberon.md|Oberon]] (remove armadura) · [[warframes/regular/nezha.md|Nezha]] · [[warframes/regular/citrine.md|Citrine]] (status e crítico) · [[warframes/regular/qorvex.md|Qorvex]]


## ⚠️ Erros Comuns — Dano e Status


1. **Usar a tabela Damage 2.0.** O erro mais comum hoje. "Corrosivo dá +75% contra Ferrite" e "Radiation dá +75% contra Alloy" **eram** verdade até junho de 2024. Hoje o modificador é por facção e vale sempre ×1,5. Se uma fonte cita porcentagens variadas por tipo de armadura, ela é de antes da U36.0.

2. **Confundir "tipo de armadura" com "tipo de saúde".** No Damage 3.0 nenhum dos dois define mais o modificador. Armadura ainda existe e ainda reduz dano — mas via fórmula, não via tabela de fraqueza.

3. **Achar que resistências somam.** Não somam, multiplicam. Quatro reduções de 25% deixam passar 31,5% do dano, não 0%.

4. **Ignorar a ordem dos slots de mod.** Trocar dois mods de posição muda os elementos resultantes por completo. Viral+Heat e Magnetic+Gas podem sair dos mesmos quatro mods.

5. **Esquecer que o elemento innato entra por último.** Colocar Frio e Elétrico numa arma com Toxin innato não gera Corrosivo — gera Magnetic + Toxin solto. Para combinar o innato, equipe um mod do mesmo elemento dele.

6. **Buildar Corrosivo contra Sentient ou Heat contra Kuva Grineer.** Essas facções **resistem** justamente ao elemento que a intuição sugere. Sentient resiste a Corrosivo; Kuva Grineer resiste a Heat.

7. **Tratar chance de status como "por disparo".** É por projétil. Uma escopeta com 12% de status e 10 pellets aplica mais de um proc por tiro, em média.

8. **Achar que Viral e Corrosivo fazem a mesma coisa.** Corrosivo **remove armadura** (reduz a redução de dano). Viral **amplifica dano na vida** (multiplica o dano que chega). Empilhar os dois é multiplicativo, não redundante.

9. **Ignorar Slash contra alvos blindados.** O bleed do proc de Slash **ignora armadura por completo**. Contra inimigo com 2.700 de armadura (90% de redução), Slash é o caminho mais curto, sem precisar remover armadura antes.

10. **Assumir que o multiplicador de armadura de inimigo por nível é conhecido.** A armadura é limitada entre 200 e 2.700, mas o multiplicador exato por nível **não foi verificado** aqui — não invente esse número.


## 🔗 Relacionados — Dano e Status


- [[mecanicas/critico.md|Crítico]] — o crítico multiplica o dano **antes** do modificador de facção e da armadura; crítico e status são os dois eixos de escala de dano do jogo.
- [[mecanicas/combo_counter.md|Combo Counter]] — em melee, o multiplicador de combo (até 12×) escala dano, e via Blood Rush/Weeping Wounds escala crítico e status também.
- [[mecanicas/steel_path.md|Steel Path]] — inimigos com +100 de nível, 2,5× de vida e 2,5× de escudo; é onde a escolha correta de elemento deixa de ser opcional.
- [[mecanicas/forma_e_polaridades.md|Forma e Polaridades]] — capacidade de mod é o que limita quantos mods elementais cabem no build.
- [[mecanicas/helminth.md|Helminth]] — permite injetar habilidades de remoção de armadura ou de amplificação de dano em qualquer frame.
- [[mecanicas/incarnon.md|Incarnon]] — formas Incarnon frequentemente mudam os tipos de dano da arma ao evoluir.
- [[mecanicas/augments.md|Augments]] — vários augments alteram tipo de dano ou aplicação de status de habilidades.

---
