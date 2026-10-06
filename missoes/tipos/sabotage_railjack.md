---
title: Sabotage (Railjack)
tipo: missao
subtipo: tipo
tags: [missao, tipo, railjack, empyrean]
atualizado: 2026-10-06
verificado: true
agente: opus
---

# Sabotage (Railjack)

> [!danger] Este tipo de missão não existe no jogo
> **Não há nenhum nó Empyrean do tipo Sabotage.** A verificação foi feita de duas formas na wiki oficial:
>
> 1. A página **Empyrean** lista explicitamente os modos Corpus do Railjack: *Exterminate, Defense, Volatile, Orphix, Spy, Survival* e *Assassination*. **Sabotage não está na lista.** As Proximas Grineer (Earth, Saturn, Veil) só têm **Skirmish**.
> 2. A consulta ao `Module:Missions/data`, que contém todos os nós do jogo, retorna **21 nós de tipo Sabotage** e **nenhum** deles tem a flag `IsRailjack = true`.
>
> Este arquivo existe no vault por um erro de estrutura da leva inicial. Pela **seção 2 das convenções** (nunca criar, renomear ou apagar arquivos) ele fica como está, documentando a ausência em vez de inventar conteúdo.

---

## 🎯 O que provavelmente se quis nomear

Duas coisas do Railjack cumprem o papel de "sabotagem" e **têm arquivo ou conteúdo próprio**:

| Candidato | O que é | Onde está documentado |
|---|---|---|
| **[[missoes/tipos/volatile.md\|Volatile]]** | O modo Railjack Corpus em que o squad **recalibra o reator da nave capital** mantendo o medidor de calor na faixa e depois **destrói os Reactor Weakpoints** no casco com a Forward Artillery. É o modo que mais se parece com uma sabotagem de reator | `missoes/tipos/volatile.md` |
| **Points of Interest** (dentro de **[[missoes/tipos/skirmish.md\|Skirmish]]**) | Objetivos de infiltração em postos orbitais Grineer — Asteroid Hangar, Asteroid Base, Missile Platform, Pulse Turbine, Shipkiller Platform. O Away Team entra e desabilita a estrutura | `missoes/tipos/skirmish.md` |

E o **Sabotage normal**, de solo, que existe em 21 nós do Star Chart e **nada tem de Railjack**, está em **[[missoes/tipos/sabotage.md|Sabotage]]**.

---

## 🗺️ Onde Encontrar

**Em nenhum lugar.** Não existe nó Empyrean de tipo Sabotage em Earth Proxima, Venus Proxima, Saturn Proxima, Neptune Proxima, Uranus Proxima, Pluto Proxima nem Veil Proxima.

Os tipos de nó que **de fato** existem no Empyrean, por região:

| Região | Facção | Tipos de nó |
|---|---|---|
| Earth Proxima | [[lore/faccoes/grineer.md\|Grineer]] | Skirmish, Free Flight, Assassination (oculto: Technocyte Coda) |
| Saturn Proxima | Grineer | Skirmish, Assassination (oculto: Kuva Lich) |
| Veil Proxima | Grineer e [[lore/faccoes/corpus.md\|Corpus]] | Skirmish, Exterminate, Defense, Survival, Spy, Volatile, Orphix |
| Venus Proxima | Corpus | Exterminate, Spy, Volatile, Orphix, Survival, Defense |
| Neptune Proxima | Corpus | Exterminate, Spy, Volatile, Orphix, Survival, Defense, Assassination (oculto: Sister of Parvos) |
| Pluto Proxima | Corpus | Exterminate, Spy, Volatile, Orphix, Survival, Defense |
| Uranus Proxima | Corpus | Skirmish, Exterminate, **Skirmish + Assassinate** (Scoria's Angel, The Kuva Wytch) |

---

## 💡 Pendência para o humano

- **Decisão sua:** este arquivo pode ser **apagado** ou **renomeado** (por exemplo para `orphix.md`, que é um tipo Railjack real e **não tem arquivo no vault** — existem 4 nós: Vesper Strait, Mammon's Prospect, Khufu Envoy e Erato). Eu não faço nenhuma das duas coisas pela seção 2 das convenções.
- Também **falta arquivo** para os tipos Railjack reais **Free Flight** e **Skirmish + Assassinate**.

---

## 📚 Fontes
- https://wiki.warframe.com/w/Empyrean — lista oficial dos modos Railjack por facção; Sabotage ausente da lista (consultado em 2026-10-06)
- https://wiki.warframe.com/w/Module:Missions/data — 21 nós Sabotage, nenhum com `IsRailjack = true`; tipos reais por Proxima (consultado em 2026-10-06)
