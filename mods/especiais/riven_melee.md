---
title: Melee Riven Mod
aliases: [Melee Riven Mod, riven melee]
tipo: mod
categoria: especial
raridade: riven
polaridade: "Madurai, Naramon ou Vazarin (sorteada)"
resumo: "Mod único por instância: cada Riven de Melee tem atributos sorteados, é designado a uma única arma (e suas variantes) e não tem tabela de efeito por rank fixa."
status: completo
rag: true
tags: [mod, especial, riven]
fontes: ["https://wiki.warframe.com/w/Riven_Mods"]
atualizado: 2026-10-07
verificado: true
agente: opus
---

# Melee Riven Mod (Riven de Melee)

> [!info] O que é
> Mod **único por instância**: cada Riven de Melee tem atributos sorteados, é **designado a uma única arma** (e suas variantes) e **não tem tabela de efeito por rank fixa**. Equipável em **armas brancas (melee)**.

> [!danger] Este arquivo não pode ter tabela de ranks
> Ao contrário de todo outro mod do vault, **um Riven não tem valores fixos**. Duas cópias do mesmo Riven de Melee para a mesma arma têm números diferentes. Por isso **não existe** tabela `Rank / Efeito / Drenagem` aqui — e inventar uma violaria as seções 1 e 8 das convenções. O que está documentado abaixo são as **regras do sistema**, que são fixas e verificáveis.


## 📊 Ficha — Melee Riven Mod


| Item | Valor |
|---|---|
| Equipável em | **armas brancas (melee)** |
| Polaridade | **Madurai, Naramon ou Vazarin** — sorteada, **independente dos atributos** |
| Raridade | **Riven** |
| Rank máximo | **8** |
| Custo de upgrade e taxa de Créditos na troca | **Iguais aos de um mod Rare** |
| Mastery Rank para equipar | **Próprio do Riven, independente da arma — de 8 a 16** |
| Quantos bônus carrega | **2 ou 3** |
| Pode ter atributo negativo | **Sim.** O efeito negativo pode ser aleijante, mas **aumenta muito a potência dos bônus positivos** |
| Conflita com | **Qualquer outro Riven** — não é possível equipar dois Rivens na mesma arma |
| Comercializável | **Sim** |
| Slots de Riven | **15** iniciais; compráveis de **3 em 3 por 60 Platinum** no Mercado, até **180**; custo total dos 165 adicionais: **3.300 Platinum**. **MR 30 dá 30 slots extras**, totalizando **210** |


## 🔒 Estados: ???, Velado e Desvelado — Melee Riven Mod


| Estado | O que acontece |
|---|---|
| **???** | Como o Riven chega ao inventário. **Neste estado não ocupa slot de Riven.** |
| **Velado (Veiled)** | Ao equipar um Riven `???`, ele fica velado: **revela um desafio** que precisa ser cumprido para desvelar. **A arma com o Riven equipado tem que estar no loadout** para participar do desafio. Neste estado: **ocupa slot de Riven**, **não ocupa capacidade de mod**, **não dá nenhum bônus nem maldição** e **não pode ser upado**. |
| **Desvelado (Unveiled)** | Os **atributos, a polaridade e o espaço de mod** são revelados e ele **passa a poder ser upado**. Só então ele **passa a exigir um Mastery Rank** para equipar. |

> [!note] Restrição de classe no estado velado
> Rivens de Melee e de Zaw velados só podem ser equipados em armas brancas.


## 🎲 Disposition — o que define a força dos atributos — Melee Riven Mod


**Disposition** é um multiplicador de atributos dado pelo sistema, que agrega a **popularidade de uso da arma** entre jogadores de Mastery Rank alto e rankings internos da "força" da arma. Ele controla **a faixa de valores possíveis** dos atributos.

O valor real vai de **0,5 a 1,55**, simplificado no jogo em 5 categorias:

| Disposition | Faixa | Significado |
|---|---|---|
| ●●●●● | **1,31–1,55** | **Strong.** Armas **menos usadas**. Rivens dão os **maiores** atributos |
| ●●●●○ | **1,11–1,30** | Armas menos populares. Atributos **acima da média** |
| ●●●○○ | **0,90–1,10** | **Neutral.** Uso médio. Atributos **médios** |
| ●●○○○ | **0,70–0,89** | Armas um pouco mais populares. Atributos **abaixo da média** |
| ●○○○○ | **0,50–0,69** | **Faint.** Armas **mais usadas**. Atributos **mais contidos**. **Toda arma nova começa aqui** |

Regras que importam na prática:

- **Disposition não é necessariamente compartilhada entre as variantes de uma arma.** O **Telos Boltor** compartilha a disposition da variante **Prime** em **1,20**, mas o **Boltor** base tem **1,30**.
- Em **armas modulares**, a disposition é do **componente principal**: o **Strike** no Zaw e o **Chamber** no Kitgun. No Kitgun, o **mesmo Chamber pode ter dispositions diferentes** nas versões primária e secundária.
- **A disposition muda a cada 3 meses**, alinhada com cada novo **Prime Access**. Quando muda, **os atributos dos Rivens já desvelados daquela arma são ajustados automaticamente**.
- A disposition da arma aparece no **Arsenal, na aba Upgrade**.

> [!warning] Por isso a convenção proíbe registrar disposition no vault
> A seção 8 das convenções lista **Riven disposition** entre os dados que não podem ser inventados, exatamente porque ela **muda a cada poucos meses**. Consulte o Arsenal no jogo ou https://wiki.warframe.com/w/Riven_Mods#Weapon_Disposition_List para o valor vigente.


## 🔄 Cycling (rerolar) — Melee Riven Mod


Rerolar é a função **Cycle**, no segmento de Mods da Orbiter, e custa **[[recursos/raridades/raro/kuva.md|Kuva]]** — obtido em objetivos de **Kuva Siphon** nos planetas próximos à **[[locais/planetas/kuva_fortress.md|Kuva Fortress]]** (que se move pelo Star Chart num ciclo de 50 horas) ou como recompensa incomum de **Bounties**.

**O que o cycle muda:** a **quantidade de atributos** e os **valores finais**.
**O que o cycle NÃO muda:** a **arma designada**, o **rank do mod**, a **polaridade** e o **Mastery Rank exigido**. E como a disposition pertence à arma e não ao mod, **um Riven rerolado nunca sai da faixa de valores daquela arma**.

Depois de rerolar, **as duas versões são mostradas** — a antiga e a nova — e **você escolhe qual manter**.

| Cycle | Custo em Kuva | Custo acumulado |
|---|---|---|
| 1 | **900** | 900 |
| 2 | **1.000** | 1.900 |
| 3 | **1.200** | 3.100 |
| 4 | **1.400** | 4.500 |
| 5 | **1.700** | 6.200 |
| 6 | **2.000** | 8.200 |
| 7 | **2.350** | 10.550 |
| 8 | **2.750** | 13.300 |
| 9 | **3.150** | 16.450 |
| 10 | **3.500** | 19.950 |

> O custo **começa em 900 Kuva** e sobe a cada cycle do mesmo mod, **travando em 3.500 Kuva**. O número de cycles já feitos aparece como uma **seta anti-horária no canto inferior direito** do mod.


## 🌍 Onde Conseguir — Melee Riven Mod


| Fonte | Detalhe |
|---|---|
| **[[missoes/jornadas/principais/the_war_within.md\|The War Within]]** | **1 Riven garantido** ao concluir a jornada |
| **Palladino** (Iron Wake) | Transmuta **10 Riven Sliver** em um Riven velado, **2× por semana**. Iron Wake exige a jornada **Chains of Harrow** concluída |
| **[[missoes/tipos/sortie.md\|Sortie]]** | Chance de drop de **8,14%** para este tipo específico |
| **[[mecanicas/steel_path.md\|Steel Path]]** — ofertas rotativas do Teshin | **Não inclui** Rivens de Pistol nem de Melee |
| **Acrithis** | Comprado por **15 [[recursos/open_worlds/duviri/pathos_clamp.md\|Pathos Clamps]]** |
| **[[missoes/tipos/archon_hunt.md\|Archon Hunt]]** | Recompensa possível |
| **Steel Path Circuit** | Recompensa possível (ver modos de Duviri) |
| **Steel Path Descendia** | Recompensa possível |
| **[[mecanicas/nightwave.md\|Nightwave]]** | Recompensa de rank possível, **dependendo da série** |
| **Calendário de 1999** | Recompensa possível |

### Chances de drop em Sortie, por tipo de Riven

| Tipo de arma | Chance de drop |
|---|---|
| **Melee** | 8,14% |
| **Pistol** | 7,61% |
| **Rifle** | 6,79% |
| **Kitgun** | 2% |
| **Zaw** | 2% |
| **Shotgun** | 1,36% |

**Comercializável:** sim

**Faixa de preço em platina:** ⚠️ **não registrada.** Riven é o item de preço mais volátil do jogo — depende da arma, da disposition vigente e da rolagem específica. Pela seção 8 das convenções, não há estimativa aqui. Consulte **riven.market** ou warframe.market no momento da negociação.


## 🛠️ Como Usar — Melee Riven Mod


**Vale a pena?** **Só com rolagem boa.** Um Riven de Melee ocupa um slot normal de mod e **só supera o mod comum daquele slot se a rolagem bater com a build**. Três coisas decidem:

1. **A disposition da arma.** Numa arma ●○○○○ (0,5–0,69) o Riven costuma perder para um mod comum. Numa ●●●●● (1,31–1,55) ele é o maior ganho único disponível.
2. **Os atributos sorteados.** 2 ou 3 bônus que precisam ser os que a build usa — um Riven de Dano + Multishot + Chance de Crítico é build-defining; um de Precisão + Zoom é lixo na mesma arma.
3. **O negativo.** Um atributo negativo **aumenta a potência dos positivos**. Um negativo irrelevante para a build (−Zoom numa arma de tiro curto, −Dano a Grineer numa build anti-Corpus) é o que faz um Riven ser excelente.

**O custo real é o Kuva.** Rerolar até a rolagem certa custa **3.500 Kuva por cycle** depois do décimo, e a tabela acima mostra que chegar lá já consumiu **19.950 Kuva** — muitas runs de Kuva Siphon. É o investimento mais caro por slot de mod do jogo.

**Mod concorrente pelo mesmo slot:** qualquer mod comum daquele slot. O Riven **não é mutuamente exclusivo** com nenhum mod específico — mas **nenhum outro Riven** pode ser equipado junto.

Ver também **[[recursos/raridades/especial/riven_mod.md|Riven Mod (recurso)]]**.

---
