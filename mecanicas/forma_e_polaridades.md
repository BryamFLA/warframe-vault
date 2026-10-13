---
title: Forma e Polaridades
aliases: [Forma e Polaridades]
tipo: mecanica
resumo: "Forma e Polaridades — Polaridade é o símbolo em cada slot de mod; casar a polaridade do mod com a do slot corta a drenagem pela metade, e a Forma é o item que troca a polaridade de um slot — ao custo de zerar o rank do equipamento."
status: completo
rag: true
tags: [mecanica, forma, polaridade, mods, capacidade, vocabulario]
fontes: ["https://wiki.warframe.com/w/Polarity", "https://wiki.warframe.com/w/Forma", "https://wiki.warframe.com/w/The_Steel_Path"]
atualizado: 2026-10-07
verificado: false
agente: opus
---

# Forma e Polaridades

> [!info] Em uma linha
> Polaridade é o símbolo em cada slot de mod; casar a polaridade do mod com a do slot corta a drenagem pela metade, e a **Forma** é o item que troca a polaridade de um slot — ao custo de zerar o rank do equipamento.


## ⚙️ Como Funciona — Forma e Polaridades


Todo equipamento tem uma **capacidade de mod** limitada e cada mod tem uma **drenagem** (custo). Sem polaridade, você raramente consegue equipar oito mods bons. Cada slot exibe um **símbolo de polaridade** (V, D, barra, Y, U...), e cada mod também tem um. Quando os dois batem, **a drenagem do mod cai 50%**, arredondando para cima. Quando não batem, **sobe 25%**. Slot sem polaridade cobra o valor cheio, sem penalidade.

Os slots de **Aura** (Warframe) e **Stance** (arma branca) funcionam ao contrário: eles *dão* capacidade em vez de gastar. Nesses slots, polaridade **casada dobra o bônus** (+100%), e polaridade **errada reduz o bônus em 20%**. É por isso que trocar a polaridade da aura de um frame pode render mais capacidade útil que polarizar dois slots normais.

A **Forma** é o consumível que muda a polaridade de um slot para a que você escolher. Ela só pode ser aplicada em equipamento no **rank máximo** e, ao ser usada, **reseta a afinidade do item para não-ranqueado** — você precisa subir os 30 ranks de novo. Isso é intencional: é o eixo de progressão de longo prazo do jogo, e cada re-ranqueamento também rende [[mecanicas/mastery_rank.md|mastery]] apenas na primeira vez.


## 🔢 Fórmulas e Números — Forma e Polaridades


```
Slot NORMAL:

   Polaridade casada:      Drenagem = teto(Drenagem Base × 0,5)
   Polaridade diferente:   Drenagem = Drenagem Base × 1,25
   Slot sem polaridade:    Drenagem = Drenagem Base

   "teto()" = arredonda para cima até o próximo inteiro.
   Ex.: mod de drenagem 9 em slot casado -> teto(4,5) = 5, não 4.

Slot de AURA ou STANCE (dá capacidade, não gasta):

   Polaridade casada:      Bônus = Bônus Base × 2      (+100%)
   Polaridade diferente:   Bônus = Bônus Base × 0,8    (−20%)
   Slot sem polaridade:    Bônus = Bônus Base
```

| Variável | Significado | Fonte do valor |
|---|---|---|
| `Drenagem Base` | Custo do mod no rank em que está equipado | Página do mod na wiki |
| `Bônus Base` | Capacidade que a aura/stance concede no rank atual | Página do mod |
| Capacidade do equipamento | Cresce com o rank do item; dobra com Orokin Reactor/Catalyst | ⚠️ tabela por rank NÃO VERIFICADA |

**Tetos e limites conhecidos:**

| Limite | Valor | Observação |
|---|---|---|
| Requisito para aplicar Forma | equipamento no **rank máximo** | Rank 30 (ou 40 em Kuva/Tenet/Coda/Paracesis) |
| Efeito colateral da Forma | **reseta o rank para não-ranqueado** | Afinidade zerada; mastery só conta na primeira vez |
| Limite de polarizações por item | ⚠️ **NÃO VERIFICADO** | Não confirmado nesta consulta |
| Redução por polaridade casada | 50%, arredondando **para cima** | Nunca dá para zero |
| Penalidade por polaridade errada | +25% de drenagem | Slot vazio de polaridade é melhor que slot errado |
| Bônus de aura/stance casada | ×2 (+100%) | O maior ganho de capacidade disponível |
| Custo em Nakak (Cetus) | **3.000 de standing + 5.000 créditos** | Forma pronta, não blueprint |
| Custo no Mercado | **20 platina** | Forma pronta |
| Umbra Forma semanal (Teshin) | **150 Steel Essence** | Ver [[mecanicas/steel_path.md\|Steel Path]] |

> [!warning] ⚠️ Custo e tempo de forja NÃO VERIFICADOS
> O custo de construção do blueprint de Forma (créditos e recursos) e o tempo de forja **não foram confirmados** nesta consulta. Os valores que a comunidade cita são:
> ```
> NAO VERIFICADO
> Blueprint de Forma:
>   Créditos: ?
>   Recursos: 1x Célula Orokin + Rubedo + Salvage + Ferrite (quantidades não confirmadas)
>   Tempo de forja: 23 horas
>   Rush: 25 platina
> ```
> Confira em https://wiki.warframe.com/w/Forma antes de usar.


## 📋 Tabelas de Referência — Forma e Polaridades


### As polaridades

| Símbolo | Nome | Para que tipo de mod | Onde dropa / como obter |
|---|---|---|---|
| **V** | **Madurai** | Mods de dano e de potência | Comumente dropada por Grineer |
| **D** | **Vazarin** | Mods defensivos (vida, armadura, escudo) | Dropada por todas as facções |
| **—** (barra / dash) | **Naramon** | Mods de utilidade e diversos | Comumente dropada por Corpus |
| **⌒** (risco) | **Zenurik** | **Augments de Warframe** e algumas stances de melee | Introduzida na Update 13.0 |
| **R** | **Unairu** | Stances de melee específicas | Introduzida na Update 13.0 |
| **Y** | **Penjaga** | Mods de habilidade de companheiro | Dropada por todas as facções |
| **U** | **Umbra** | Mods anti-Sentient (conjunto Umbral) | Após concluir [[missoes/jornadas/principais/the_sacrifice.md\|The Sacrifice]] |
| **O** | **Any / Omni** | Universal — aceita qualquer polaridade **exceto Umbra** | Stance Forma / Omni Forma |

> [!note] Os nomes são os mesmos das escolas de Focus
> Madurai, Vazarin, Naramon, Zenurik e Unairu são também as cinco escolas de [[mecanicas/operator_e_focus.md|Focus]] do Operator. Os símbolos são compartilhados de propósito, mas os sistemas são independentes: polaridade de slot não afeta escola de Focus.

### Variantes de Forma e adaptadores

| Item | O que faz | Observação |
|---|---|---|
| [[recursos/raridades/especial/forma.md\|Forma]] | Muda a polaridade de um slot normal para a escolhida | Reseta o rank do item |
| [[recursos/raridades/especial/aura_forma.md\|Aura Forma]] | Aplica polaridade **Omni** no slot de aura — aceita qualquer aura sem penalidade | ⚠️ detalhes de aplicação não verificados |
| [[recursos/raridades/especial/umbral_forma.md\|Umbral Forma]] | Aplica a polaridade **Umbra (U)**, necessária para os mods Umbral sem drenagem proibitiva | Fonte principal: 150 Steel Essence com Teshin, oferta semanal |
| Stance Forma / Omni Forma | Aplica polaridade **Omni (O)** — aceita qualquer polaridade exceto Umbra | Nome varia por contexto |
| [[recursos/raridades/especial/exilus_adapter.md\|Exilus Adapter]] | **Desbloqueia** o slot Exilus de uma arma | Não é polaridade; abre um slot |
| [[recursos/raridades/especial/warframe_exilus_adapter.md\|Warframe Exilus Adapter]] | Desbloqueia o slot Exilus de um Warframe | Idem |
| [[recursos/raridades/especial/orokin_reactor.md\|Orokin Reactor]] | **Dobra a capacidade de mod** de Warframe / Archwing / Necramech | "Orokin-ar" um frame |
| [[recursos/raridades/especial/orokin_catalyst.md\|Orokin Catalyst]] | **Dobra a capacidade de mod** de uma arma | "Orokin-ar" uma arma |

### Onde conseguir Forma

| Fonte | Detalhe |
|---|---|
| Relíquias Void | Blueprint de Forma: 1× nas recompensas Comuns, 2× nas Incomuns |
| Recompensas de missão | Orokin Derelict Defense entre as fontes de maior chance; várias missões com chance menor. ⚠️ **porcentagens não citadas aqui de propósito** — drop chance muda a cada update |
| Contêineres raros / reforçados | Em locais específicos |
| Daily Tribute | Recompensa de login |
| [[mecanicas/nightwave.md\|Nightwave]] | Recompensa de rank |
| Nakak (Cetus) | Forma **pronta** por 3.000 de standing + 5.000 créditos |
| Mercado | Forma **pronta** por 20 platina |

### Ordem prática de investimento em um item

| Passo | O que fazer | Por quê |
|---|---|---|
| 1 | Subir ao rank 30 | Rende [[mecanicas/mastery_rank.md\|mastery]] e é requisito para Forma e para Reactor/Catalyst |
| 2 | Aplicar Orokin Reactor (frame) ou Catalyst (arma) | **Dobra a capacidade** — o maior ganho único, e não reseta o rank |
| 3 | Fechar o build sem Forma e ver o que sobra de capacidade | Muitos builds fecham só com Reactor/Catalyst |
| 4 | Polarizar a **aura/stance** primeiro | Casar aura dobra o bônus de capacidade — rende mais que um slot normal |
| 5 | Polarizar os slots dos mods de maior drenagem | 50% de 16 economiza mais que 50% de 4 |
| 6 | Aplicar Umbral Forma só se for usar mods Umbral | Umbral Forma é caro (150 Steel Essence) |


## 🛠️ Como Usar na Prática — Forma e Polaridades


| Objetivo | O que fazer |
|---|---|
| Ganhar capacidade sem gastar Forma | Orokin Reactor / Catalyst dobram a capacidade e **não** resetam o rank |
| Maior ganho por Forma gasta | Polarize o slot de **aura** ou **stance** casando a polaridade — o bônus dobra em vez de a drenagem cair 50% |
| Encaixar build de dano em arma | Polarize em **Madurai (V)**: [[mods/armas/serration.md\|Serration]], [[mods/armas/split_chamber.md\|Split Chamber]] e os elementais são quase todos V |
| Encaixar build defensivo em frame | Polarize em **Vazarin (D)**: [[mods/warframe/vitality.md\|Vitality]], [[mods/warframe/redirection.md\|Redirection]], [[mods/warframe/steel_fiber.md\|Steel Fiber]] |
| Encaixar augment de Warframe | Augments usam **Zenurik**. Polarize o slot correspondente |
| Encaixar conjunto Umbral | Precisa de **Umbral Forma (U)**. Sem ela, [[mods/warframe/umbral_intensify.md\|Umbral Intensify]] e [[mods/warframe/umbral_vitality.md\|Umbral Vitality]] drenam demais |
| Não desperdiçar Forma | **Feche o build no simulador antes.** Cada Forma custa 30 ranks de re-leveling; polarizar o slot errado custa uma segunda Forma |
| Evitar penalidade sem gastar Forma | Slot **sem** polaridade cobra valor cheio; slot com polaridade **errada** cobra +25%. Se não vai casar, é melhor não polarizar |

**Mods que interagem (drenagem alta, os que mais se beneficiam de polarização):**
Primed Serration · [[mods/armas/serration.md|Serration]] · [[mods/armas/split_chamber.md|Split Chamber]] · [[mods/armas/heavy_caliber.md|Heavy Caliber]] · [[mods/armas/primed_pressure_point.md|Primed Pressure Point]] · [[mods/armas/blood_rush.md|Blood Rush]] · [[mods/warframe/umbral_intensify.md|Umbral Intensify]] · [[mods/warframe/umbral_vitality.md|Umbral Vitality]] · [[mods/warframe/primed_flow.md|Primed Flow]] · [[mods/warframe/primed_continuity.md|Primed Continuity]] · [[mods/warframe/narrow_minded.md|Narrow Minded]] · [[mods/warframe/blind_rage.md|Blind Rage]]

**Auras (slot que dobra o bônus quando casado):**
[[mods/warframe/energy_siphon.md|Energy Siphon]] · [[mods/warframe/corrosive_projection.md|Corrosive Projection]] · [[mods/warframe/steel_charge.md|Steel Charge]] · [[mods/warframe/rejuvenation.md|Rejuvenation]] · [[mods/warframe/physique.md|Physique]] · [[mods/warframe/dead_eye.md|Dead Eye]] · [[mods/warframe/growing_power.md|Growing Power]]


## ⚠️ Erros Comuns — Forma e Polaridades


1. **Polarizar antes de aplicar Orokin Reactor/Catalyst.** O Reactor/Catalyst **dobra a capacidade** e não reseta o rank. Muitos builds fecham só com ele — polarizar antes é gastar Forma à toa.

2. **Polarizar um slot normal antes da aura.** Casar a aura **dobra o bônus de capacidade**; casar um slot normal só corta 50% da drenagem de um mod. Aura primeiro, quase sempre.

3. **Achar que polaridade errada é neutra.** Slot com polaridade diferente cobra **+25%**. Slot sem polaridade cobra o valor cheio, sem penalidade. Polarizar errado é pior que não polarizar.

4. **Esquecer que a redução arredonda para cima.** Mod de drenagem 9 em slot casado custa **5**, não 4,5. Isso quebra builds calculados no papel por 1 ponto.

5. **Aplicar Forma sem estar no rank 30.** Não é possível — o item precisa estar no rank máximo.

6. **Não contar o re-leveling.** Cada Forma zera a afinidade. Um frame com 5 Forma foi ranqueado do 0 ao 30 seis vezes.

7. **Achar que re-ranquear rende mastery de novo.** Não rende. [[mecanicas/mastery_rank.md|Mastery]] de um item é contado **uma vez**; polarizar e re-subir não dá pontos novos (exceto nos ranks acima de 30 de Kuva/Tenet/Coda/Paracesis e Necramech, que exigem Forma para alcançar).

8. **Confundir polaridade de slot com escola de Focus.** Madurai, Vazarin, Naramon, Zenurik e Unairu nomeiam as duas coisas. São sistemas independentes.

9. **Comprar Forma pronta por platina achando que é a única via.** Blueprint de Forma cai de relíquias, Daily Tribute e Nightwave; Nakak vende a Forma pronta por standing.

10. **Citar o custo de forja a partir deste arquivo.** Está marcado ⚠️ NÃO VERIFICADO. Abra a página da wiki.


## 🔗 Relacionados — Forma e Polaridades


- [[mecanicas/mastery_rank.md|Mastery Rank]] — subir itens ao rank 30 é o que gera mastery; polarizar zera o rank mas não devolve pontos.
- [[mecanicas/forja.md|Forja]] — onde o blueprint de Forma é construído (tempo de forja e rush em platina).
- [[mecanicas/steel_path.md|Steel Path]] — Teshin vende **Umbral Forma por 150 Steel Essence** como oferta semanal.
- [[mecanicas/helminth.md|Helminth]] — habilidades injetadas ocupam o slot da habilidade substituída e continuam sujeitas à capacidade de mod do frame.
- [[mecanicas/augments.md|Augments]] — usam polaridade **Zenurik**; sem polarizar, o augment frequentemente não cabe.
- [[mecanicas/critico.md|Crítico]] e [[mecanicas/dano_e_status.md|Dano e Status]] — os builds que mais estouram capacidade são justamente crítico + status, que empilham mods de drenagem alta.
- [[mecanicas/trading.md|Trading]] — Forma pronta e blueprints circulam no mercado entre jogadores.
- [[mecanicas/nightwave.md|Nightwave]] — fonte recorrente de blueprint de Forma e de Umbral Forma em algumas temporadas.

---
