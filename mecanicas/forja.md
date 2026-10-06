---
title: Forja (Foundry)
aliases: [Forja (Foundry), forja]
tipo: mecanica
resumo: "Forja (Foundry) — Seção da Orbiter onde todo equipamento do jogo é construído: blueprint + componentes + Credits + tempo real de espera, com opção de rush por Platinum."
status: completo
rag: true
tags: [mecanica, forja, foundry, crafting, blueprint]
fontes: ["https://wiki.warframe.com/w/Foundry", "https://wiki.warframe.com/w/Platinum"]
atualizado: 2026-10-07
verificado: true
agente: opus
---

# Forja (Foundry)

> [!info] Em uma linha
> Seção da Orbiter onde todo equipamento do jogo é construído: blueprint + componentes + Credits + tempo real de espera, com opção de rush por Platinum.


## ⚙️ Como Funciona — Forja (Foundry)


A Forja constrói Warframes, Archwings, Sentinels, armas e praticamente todo o resto. Destranca ao concluir a missão tutorial "Locate the Foundry Segment" da quest [[missoes/jornadas/principais/vors_prize.md\|Vor's Prize]] e instalar o **Foundry Segment** recebido nela — depois disso fica permanente.

O ciclo é: **conseguir o blueprint → juntar os componentes → iniciar a construção → esperar em tempo real → reivindicar (claim)**. A contagem roda **com o jogo fechado**, então um Warframe de 72 h fica pronto em 3 dias corridos independente de quanto você jogou. A Forja aceita **número ilimitado de construções simultâneas**; a única restrição é não ter **duas cópias do mesmo item** construindo ao mesmo tempo.

A Forja também é acessível pelo **Warframe Companion app** no celular, o que serve para iniciar e reivindicar construções fora do jogo.


## 🔢 Fórmulas e Números — Forja (Foundry)


```
Custo de rush = custo inicial de rush x (1 - ((progresso - 50) / 100))

O custo de rush é FIXO até o item chegar a 50% de progresso.
De 50% a 100%, ele cai linearmente até 50% do valor inicial.

Exemplo: rush inicial de 30 pl, item a 70% de progresso
  30 x (1 - ((70 - 50) / 100)) = 30 x 0,80 = 24 pl
```

| Variável | Significado | Fonte do valor |
|---|---|---|
| 50% | Ponto a partir do qual o custo de rush começa a cair | Wiki, Foundry § Rushing Construction |
| 50% do custo inicial | Piso do custo de rush, atingido em 100% de progresso | Wiki, Foundry § Rushing Construction |

### Custos típicos de rush

| Item | Platinum |
|---|---|
| Warframe completo | 50 |
| Parte de Warframe (Neuroptics, Chassis, Systems) | 25 |
| Armas em geral | 25 a 50 |
| Landing Craft novo | 50 |
| Parte de Landing Craft | 25 |
| Keys, consumíveis etc. | 1 a 15 |

### Slots para reivindicar

Um item pronto **fica preso na Forja** até existir slot livre do tipo correspondente.

| Slot | Platinum |
|---|---|
| 1 slot de Warframe | 20 |
| 2 slots de arma (par) | 12 |

**Tetos e limites conhecidos:**

- **Cancelar uma construção devolve tudo** — recursos e blueprint — **exceto Argon Crystal**, que é perdido. A única exceção que não pode ser cancelada é a **Clan Key**.
- **Argon Crystal decai** mesmo guardado no inventário: é o único recurso perecível do jogo, e a única coisa que o cancelamento não devolve.
- Blueprints de uso único mostram a quantidade restante; blueprints **reutilizáveis** têm fundo dourado e a inscrição "REUSABLE BLUEPRINT" no rodapé.
- Enquanto vários itens constroem ao mesmo tempo, a Forja exibe visualmente **o primeiro que começou**.


## 📋 Tabelas de Referência — Forja (Foundry)


### De onde vêm os blueprints

| Origem | Exemplos |
|---|---|
| **Market** (compra com Credits) | Blueprint principal da maioria dos Warframes e armas não-Prime |
| **Pesquisa de clã** (salas de Research no Dojo) | Partes de Banshee, Nezha, Volt e Zephyr; armas de Chem/Bio/Energy/Tenno Lab |
| **Chefes** | Partes (Neuroptics, Chassis, Systems) da maioria dos Warframes |
| **Quest** | Partes de Mirage, Limbo, Inaros e Chroma |
| **Nightwave Offerings** | Partes de Vauban; blueprints diversos |
| **Void Relics / Orokin Derelict** | Partes Prime |

### Estrutura típica de um Warframe

| Peça | Tempo de forja padrão |
|---|---|
| Neuroptics | 12 h |
| Chassis | 12 h |
| Systems | 12 h |
| Montagem final do Warframe | 72 h (vários frames usam **24 h** — confira na ficha do frame) |

> Os tempos de montagem variam por frame e foram confirmados caso a caso nas fichas de `warframes/`. Exemplos já auditados neste vault: Excalibur, Volt, Mag e Rhino em **24 h**; Nezha em **72 h**.

### Upgrade da Forja

| Upgrade | O que adiciona | Onde pegar | Custo |
|---|---|---|---|
| **Landing Craft Segment** | Permite construir Landing Crafts e **Air Support Charges** | Blueprint no Tenno Research Lab do Dojo | 15.000 Credits (ou 175 Platinum pronto no Market) |


## 🛠️ Como Usar na Prática — Forja (Foundry)


| Objetivo | O que fazer |
|---|---|
| Economizar Platinum de rush | Nunca rushe antes de 50% — o custo é **fixo** até lá. Esperar até ~90% já corta quase 40% do custo |
| Nunca deixar a Forja parada | Não há limite de construções simultâneas. Comece tudo que tiver material; a única regra é não duplicar o mesmo item |
| Recuperar blueprint Prime para tradear | Se começou a construir uma peça Prime por engano, **cancele**: o blueprint e os recursos voltam (menos Argon Crystal) e o blueprint volta a ser tradeável |
| Não perder Argon Crystal | [[recursos/raridades/raro/argon_crystal.md\|Argon Crystal]] decai com o tempo **e** é perdido em cancelamento. Só farme quando já tiver todo o resto pronto para iniciar a construção |
| Gerenciar slots | Item pronto sem slot fica retido na Forja — não é perdido. Venda uma arma antiga por Credits para liberar par de slots, ou compre por 12 pl (2 armas) / 20 pl (1 Warframe) |
| Forjar fora do jogo | O Warframe Companion app inicia e reivindica construções pelo celular |
| Air Support Charge | Exige o Landing Craft Segment, blueprint do Tenno Lab por 15.000 Credits |

**Mods que interagem:** nenhum. A Forja consome recursos e Credits, não mods — mas é onde se constrói [[recursos/raridades/especial/forma.md|Forma]], [[recursos/raridades/especial/umbral_forma.md|Umbral Forma]], [[recursos/raridades/especial/aura_forma.md|Aura Forma]], [[recursos/raridades/especial/orokin_catalyst.md|Orokin Catalyst]] e [[recursos/raridades/especial/orokin_reactor.md|Orokin Reactor]], que são o que de fato aumenta a capacidade de mod.


## ⚠️ Erros Comuns — Forja (Foundry)


- **"Preciso ficar jogando para a forja andar."** Não. O cronômetro é tempo real e corre com o jogo fechado.
- **"Cancelar perde tudo."** Devolve recursos **e** blueprint. A única perda é o **Argon Crystal**. A única construção que não pode ser cancelada é a Clan Key.
- **"Rush fica mais barato se eu esperar um pouco."** Só depois dos **50%**. Antes disso o preço é fixo — esperar de 10% para 40% não economiza nada.
- **"Item pronto sem slot é perdido."** Fica retido na Forja indefinidamente até você abrir um slot.
- **"Posso construir 2 Formas ao mesmo tempo."** Não. Duas construções do **mesmo item** simultâneas são bloqueadas — mas Forma e Forma Umbral, sendo itens diferentes, podem.
- **"Peça Prime já construída pode ser tradeada."** Não. Só o **blueprint** Prime é tradeável; peça construída e Warframe montado não são.


## 🔗 Relacionados — Forja (Foundry)


- [[mecanicas/platinum.md|Platinum]] — rush de construção, slots e compra de itens prontos.
- [[mecanicas/cla_e_dojo.md|Clã e Dojo]] — as salas de Research são a origem de boa parte dos blueprints, e o Landing Craft Segment sai do Tenno Lab.
- [[mecanicas/forma_e_polaridades.md|Forma e Polaridades]] — Forma, Umbral Forma, Aura Forma, Catalyst e Reactor são todos construídos na Forja.
- [[mecanicas/trading.md|Trading]] — cancelar uma construção é o que devolve um blueprint Prime ao estado tradeável.
- [[mecanicas/helminth.md|Helminth]] — os 4 Segments do Helminth são itens de Forja (50.000 Credits e 24 h cada).
- [[mecanicas/nightwave.md|Nightwave]] — fonte de blueprints exclusivos nas Offerings.
- [[recursos/_Recursos _Indice.md|Recursos]] — tudo que a Forja consome.
- [[missoes/jornadas/principais/vors_prize.md|Vor's Prize]] — a quest que entrega o Foundry Segment.

---
