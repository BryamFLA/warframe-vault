---
title: Razorback Armada
aliases: [Razorback Armada]
tipo: mecanica
resumo: Evento recorrente em que o Corpus ataca um Relay com o Razorback — um Jackal gigante do Nef Anyo.
status: completo
rag: true
tags: [mecanica, evento, razorback, corpus, relay, nef-anyo]
fontes: ["https://wiki.warframe.com/w/Razorback"]
atualizado: 2026-10-07
verificado: true
agente: opus
---

# Razorback Armada

> [!info] Em uma linha
> Evento recorrente em que o Corpus ataca um Relay com o **Razorback** — um Jackal gigante do Nef Anyo. Entrar exige um **Razorback Cipher**, e matá-lo exige **hackear Bursas** e virá-los contra ele.


## ⚙️ Como Funciona — Razorback Armada


O **Razorback** é um chefe Corpus introduzido no Tactical Alert "Divine Will", na Hotfix 18.4.10 (2016-02-11). É uma criação do **Nef Anyo** — essencialmente um **[[lore/chefes/jackal.md\|Jackal]] muito maior** que o Nef se vangloria de ser "impermeável ao mal". A ironia é que ele é **vulnerável às criações anteriores do próprio Nef: os Bursas**.

> *"Povo do Sistema de Origem, com a bênção dos seus credits e o poder da energia sagrada do Void, construí uma criatura mais forte que qualquer outra. (…) Convoco todos os Tenno, Corpus hereges e Grineer a vir ao meu laboratório e tentar derrotar meu Razorback. E quando falharem, o Sistema inteiro verá que o Void age através de mim."* — Nef Anyo

O evento aparece como um **nó ao lado de um Relay ativo**, depois que o **status de construção no menu de Invasion é concluído apoiando o Corpus**. Concluir a missão **3 vezes por edição do evento** dá **200.000 Credits** e um **[[recursos/raridades/especial/orokin_catalyst.md\|Orokin Catalyst]] pronto**.


## 🔢 Fórmulas e Números — Razorback Armada


```
Entrada: exige 1 Razorback Cipher POR JOGADOR
  Apenas 1 pessoa interage com o terminal, mas TODOS consomem um Cipher

Razorback Cipher Blueprint (REUTILIZÁVEL):
  1.250 Credits + 1.500 + 3 + 4 de recursos  (um deles é Cryptographic ALU)
  Tempo: 1 minuto  ·  Rush: 1 Platinum

Stats do Razorback:
  Escudo 2.000  ·  Vida 6.000  ·  Armadura 100  (redução de dano 17,32%)
  Nível de spawn: 43   ·   Codex Scans: 3
  Ataques: Missile Shot 15 (x2 multishot) · Missile AoE 35 ·
           Grenade Cluster 100 (x4) — todos ELÉTRICOS, 0% de status

Luta: 4 ciclos. Cada Bursa hackeado derruba o Razorback e libera
  dano em até 25% da vida dele antes de ele voltar e ficar invulnerável

Bursa hackeado MORRE em 10 segundos

Recompensa por 3 conclusões no evento: 200.000 Credits + 1 Orokin Catalyst pronto
```

| Variável | Significado | Fonte do valor |
|---|---|---|
| 1 Cipher por jogador | Todos consomem, mesmo quem não interage | Wiki, Razorback § Razorback Cipher |
| 1 min / 1 pl | Forja e rush do Cipher (blueprint **reutilizável**) | Wiki, Razorback § Razorback Cipher |
| 2.000 / 6.000 / 100 | Escudo, vida e armadura do Razorback | Wiki, Razorback (infobox) |
| 17,32% | Redução de dano pela armadura 100 | Wiki, Razorback (infobox) |
| 43 | Nível de spawn | Wiki, Razorback (infobox) |
| **25%** | Vida liberada por cada Bursa hackeado | Wiki, Razorback § Strategy |
| **10 s** | Tempo que um Bursa hackeado sobrevive | Wiki, Razorback § Strategy |
| 200.000 Credits | Recompensa por 3 conclusões na edição | Wiki, Razorback (intro) |

**Tetos e limites conhecidos:**

- **Cryptographic ALU só existe durante o Razorback Armada.** Dropa de inimigos de Archwing sobre **Júpiter e Netuno**, e em missões de **Empyrean** nas zonas **Venus Proxima, Neptune Proxima e Veil Proxima**.
- **Perspicacity** (habilidade do [[mecanicas/helminth.md\|Helminth]]) e **Auto Breach** funcionam no terminal da porta, **mas ainda consomem o Cipher**. Nos terminais de spawn de Bursa, o efeito deles é **reduzido**.
- Um Bursa hackeado **não pode** ser usado para duas fases de vulnerabilidade: ele morre em 10 s, e há **alguns segundos de atraso** entre as fases em que nenhum Bursa consegue atordoar o Razorback. Manter vários Bursas vivos é inútil.
- Drop de **Orokin Cell** dos Hyenas começa em **100%** e **diminui progressivamente** quanto mais Hyenas você spawna — correção da Hotfix 25.8.1 (2019-10-09) contra o exploit de farm infinito.


## 📋 Tabelas de Referência — Razorback Armada


### A luta, passo a passo

| Passo | O que fazer |
|---|---|
| 1 | Chegar à arena. A sala do Razorback é trancada por um **terminal cujos painéis se movem continuamente** — impossível de resolver sem o **Cipher** |
| 2 | Ativar o terminal dentro da arena: a plataforma central sobe e revela o Razorback |
| 3 | O Razorback é **imune a todo dano** (como o Jackal) |
| 4 | **Hackear um dos dois terminais** das sacadas superiores laterais → spawna um **Bursa** logo abaixo |
| 5 | **Danificar o Bursa** até derrubá-lo e **hackeá-lo** para virá-lo contra o Razorback |
| 6 | Quando o Bursa ataca, o Razorback **colapsa** e permite dano em **até 25% da vida** |
| 7 | **Repetir 3 vezes mais** (4 ciclos no total) |

### Ataques do Razorback

| Ataque | Efeito |
|---|---|
| **Turret** | Duas torres montadas nas "bochechas" disparam rajadas de metralhadora |
| **Rippling Shockwave** | Pisa o chão com as pernas massivas, gerando onda de choque que **derruba** os Tenno |
| **Plasma Grenade Cluster** | Deposita granadas de plasma que grudam no chão e explodem logo depois (100 de dano Elétrico, 4x multishot) |
| **Homing Missiles** | Dispara um grande cacho de mísseis teleguiados (15 de dano por tiro, 35 em área, Elétrico) |

As **quatro sacadas superiores**, protegidas por **Laser Barrier**, spawnam soldados Corpus que descem para apoiar o Razorback.

### Recompensas da missão (para todo o squad)

| Recompensa | Chance |
|---|---|
| Gorgon Wraith **Barrel** | 18,97% |
| Gorgon Wraith **Blueprint** | 18,97% |
| Gorgon Wraith **Receiver** | 18,97% |
| Gorgon Wraith **Stock** | 18,97% |
| **Auger Strike** | 5,53% |
| **Bore** | 5,53% |
| **Breach Loader** | 5,53% |
| **Piercing Caliber** | 5,53% |
| **Magma Chamber** | 1,01% |
| **Searing Steel** | 1,01% |

**Recompensa de evento (fora da tabela de drop):** concluir a missão **3 vezes** na edição dá **200.000 Credits** e um **Orokin Catalyst pronto**.

### Histórico de aparições (pós-Update 32.0, World State sincronizado)

Desde o Update 32.0 (2022-09-07) todas as plataformas compartilham World State e status de Relay. Edições recentes:

| Data | Relay |
|---|---|
| 2024-03-01 | Kronia (Saturno) |
| 2024-05-28 | Orcus (Plutão) |
| 2024-09-04 | Strata (Terra) |
| 2024-11-26 | Kronia (Saturno) |
| 2025-01-15 | Strata (Terra) |
| 2025-03-17 | Kronia (Saturno) |
| 2025-06-04 | Strata (Terra) |
| 2025-09-04 | Kronia (Saturno) |
| 2025-11-21 | Orcus (Plutão) |
| 2026-05-07 | Orcus (Plutão) |
| 2026-07-30 | Strata (Terra) |
| 2026-09-21 | Orcus (Plutão) |
| 2026-09-28 | Kronia (Saturno) |


## 🛠️ Como Usar na Prática — Razorback Armada


| Objetivo | O que fazer |
|---|---|
| **Entrar na missão** | Forje o **Razorback Cipher** (blueprint reutilizável, 1 minuto). **Cada membro do squad precisa de um**, mesmo que só uma pessoa use o terminal |
| Conseguir Cryptographic ALU | Só existe **durante o evento**: inimigos de Archwing sobre **Júpiter e Netuno**, ou Empyrean nas **Venus / Neptune / Veil Proxima** |
| Matar o Razorback rápido | 4 ciclos de **hackear terminal → derrubar Bursa → hackear Bursa → 25% de dano**. Divida o squad entre as duas sacadas |
| Não desperdiçar Bursa | Bursa hackeado morre em **10 s**, e há atraso entre as fases de vulnerabilidade — **não** vale manter vários vivos |
| Resolver o travamento | Se o Razorback ficar pisoteando em cima de um Bursa hackeado e travar o progresso, **spawne outro Bursa no lado oposto** da arena |
| Garantir a recompensa de evento | **3 conclusões** por edição: **200.000 Credits + 1 Orokin Catalyst pronto** |
| Farmar Affinity | A missão tem **muitos Bursas, Hyenas e Eximus** — é uma das melhores fontes de Affinity do jogo durante o evento |
| Farmar Orokin Cell | Hyenas começam com **100% de drop** de Orokin Cell, mas a chance **cai progressivamente** quanto mais você spawna |
| Elemento certo | Os ataques do Razorback são todos **Elétricos**. Ele é Corpus com armadura 100 (17,32% de redução) e **2.000 de escudo**: Magnetic para o escudo, Toxin ignorando o escudo. Ver [[mecanicas/dano_e_status.md\|Dano e Status]] |


## ⚠️ Erros Comuns — Razorback Armada


- **"Só quem usa o terminal gasta o Cipher."** **Todos** no squad consomem um Cipher quando ele é usado.
- **"Perspicacity economiza o Cipher."** Funciona no terminal da porta, mas **ainda consome o Cipher**. E nos terminais de Bursa o efeito é **reduzido**.
- **"O Cipher é de uso único."** O **blueprint é reutilizável**; o item, não.
- **"Posso matar o Razorback direto."** Ele é **imune a todo dano** fora das janelas abertas por Bursa hackeado.
- **"Vou juntar 4 Bursas hackeados e matar de uma vez."** Cada um morre em **10 s**, e o atraso entre as fases impede que mais de um conte. Hackeie um por ciclo.
- **"Hyena dá Orokin Cell infinito."** Era um exploit, corrigido na Hotfix 25.8.1: a chance **diminui** quanto mais Hyenas aparecem.
- **"O evento aparece sozinho."** Só depois de o **status de construção no menu de Invasion** ser concluído **apoiando o Corpus**.
- **"Cryptographic ALU é farmável sempre."** Só **durante** o Razorback Armada.


## 🔗 Relacionados — Razorback Armada


- [[mecanicas/eventos/_Eventos _Indice.md|Eventos]] — a visão geral; o Razorback Armada é o espelho Corpus do [[mecanicas/eventos/balor_fomorian.md\|Balor Fomorian]] Grineer.
- [[mecanicas/eventos/balor_fomorian.md|Balor Fomorian]] — o evento equivalente do lado Grineer, também ligado ao menu de Invasion.
- [[mecanicas/forja.md|Forja]] — o Razorback Cipher é um blueprint **reutilizável** de 1 minuto.
- [[mecanicas/forma_e_polaridades.md|Forma e Polaridades]] — a recompensa de 3 conclusões é um **Orokin Catalyst pronto**.
- [[mecanicas/helminth.md|Helminth]] — **Perspicacity** auto-hackeia, mas não economiza o Cipher.
- [[mecanicas/dano_e_status.md|Dano e Status]] — o Razorback é Corpus com 2.000 de escudo e armadura 100; os ataques dele são todos Elétricos.
- [[mecanicas/mastery_rank.md|Mastery Rank]] — o Gorgon Wraith conta Mastery como variante própria.
- [[lore/chefes/jackal.md|Jackal]] — o chefe de que o Razorback é a versão gigante, com a mesma mecânica de invulnerabilidade.
- [[lore/faccoes/corpus.md|Corpus]] — a facção, e o Nef Anyo como criador.
- [[locais/planetas/jupiter.md|Júpiter]] e [[locais/planetas/neptuno.md|Netuno]] — onde o Cryptographic ALU dropa em Archwing.
- [[recursos/_Recursos _Indice.md|Recursos]] — Cryptographic ALU também cai em Empyrean (Venus, Neptune e Veil Proxima).
- [[recursos/raridades/especial/orokin_catalyst.md|Orokin Catalyst]] — a recompensa principal do evento.
- [[recursos/raridades/raro/orokin_cell.md|Orokin Cell]] — o drop dos Hyenas, com chance decrescente.

---
