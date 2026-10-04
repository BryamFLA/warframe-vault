---
title: The Perrin Sequence
tipo: mecanica
tags: [mecanica, sindicato, perrin-sequence, corpus, mercadores]
atualizado: 2026-10-04
verificado: true
agente: opus
---

# The Perrin Sequence

> [!info] Em uma linha
> Coletivo de mercadores brilhantes e poderosos, dissidentes do Corpus, que querem restaurar a ordem trazendo prosperidade e direção ao mundo violento que estudam.

---

## 🧩 Como Funciona

A Perrin Sequence é um **coletivo de mercadores brilhantes e poderosos**, cindido do Corpus. O objetivo deles é **restaurar a ordem trazendo prosperidade e direção** ao mundo violento que eles observam e estudam.

É o sindicato da solução econômica: comércio em vez de guerra. Aliada natural da New Loka (as duas querem restauração, não purga), oposta aos Arbiters of Hexis (que desconfiam de qualquer coisa movida por lucro) e **inimiga mortal do Steel Meridian** — porque o Meridian defende colônias contra o mesmo aparato comercial de que a Perrin veio.

Mecanicamente, The Perrin Sequence é um **sindicato de facção**: o console de sindicatos da Orbiter abre no **Mastery Rank 3**, você faz um **Pledge** no terminal e **15% de toda a Affinity ganha** vira Standing. Subir aqui **sobe** o Standing do aliado e **derruba** o do oposto e do inimigo — é a escolha que define quais augments você terá acesso.

| Relação | Sindicato | Efeito no Standing |
|---|---|---|
| 🤝 **Aliado** | New Loka | **+50% Rep** |
| ⚠️ **Oposto** | Arbiters of Hexis | **−50% Rep** |
| ⛔ **Inimigo** | Steel Meridian | **−100% Rep** |

## 🔢 Fórmulas e Números

```
Conversão de Affinity em Standing (com Pledge ativo no terminal da Orbiter) = 15%

Teto diário de Standing (sindicato de facção) = 16.000 + (500 x Mastery Rank)
  Reset: 00:00 UTC
  Syndicate Alerts e Syndicate Medallions NÃO contam nesse teto

Standing por rank:
  Rank 5 → teto 132.000   |  Rank 2 → teto  44.000
  Rank 4 → teto  99.000   |  Rank 1 → teto  22.000
  Rank 3 → teto  70.000   |  Rank 0 →  -5.000 a 5.000
  Rank -1 → -22.000 a 0   |  Rank -2 → -44.000 a 0  (piso absoluto)

Subir de rank consome TODO o Standing acumulado + um sacrifício (Credits e recursos)
A cada promoção você escolhe 1 presente do rank novo
  (armas exclusivas do sindicato NÃO podem ser escolhidas como presente)

Warframe Augment Mod = 25.000 Standing (só no Rank 5)
Syndicate Relic Pack  = 20.000 Standing (Rank 2) — 2 Relics Lith/Meso + 1 garantida Neo/Axi

Syndicate Alert: 3 por dia, expiram em 24 h (reset junto com as Sorties)
Syndicate Medallions por missão de alerta = 8
  Exceção: Defense e Interception dão 0 a 2 (depende do tileset)
  Exceção da exceção: Grineer Sealab e Grineer Galleon dão 8 em qualquer tipo
```

| Variável | Significado | Fonte do valor |
|---|---|---|
| 15% | Fração da Affinity convertida em Standing via Pledge | Wiki, Syndicate § Faction |
| 16.000 + 500/MR | Teto diário de Standing de facção | Wiki, Syndicate § Gaining Reputation and Ranking |
| 132.000 | Teto de Standing do Rank 5 | Wiki, Syndicate § Gaining Reputation and Ranking |
| −44.000 | Piso absoluto de Standing negativo (Rank −2) | Wiki, Syndicate § Faction |
| 25.000 | Custo de cada Warframe Augment Mod | Wiki, Warframe Augment Mods § Acquisition |
| 20.000 | Custo do Syndicate Relic Pack | Wiki, Syndicate § Rank 2 |
| 8 medalhões | Por missão de Syndicate Alert | Wiki, Syndicate § Syndicate Medallions |
| 886 | Máximo de medalhões (de 500 Standing) para ir de −44.000 a 132.000 | Wiki, Syndicate § Faction |

**Tetos e limites conhecidos:**

- Para **encontrar** os medalhões é preciso ter **Standing favorável** com o sindicato que ofereceu o alerta.
- Desde o Update 16, cair de um tier alto para um baixo exige **um único** sacrifício para voltar, não vários.
- Reobter um rank depois de rebaixamento **não** permite escolher outro presente.
- Assassinos (Stalker e companhia) **não** spawnam em missão de sindicato.
- Missão de sindicato **ignora** a lista normal de spawn do tileset — dá para encontrar Hellion em Grineer Asteroid e Anti MOA fora da Gas City.

---

## 📋 Tabelas de Referência

### Identidade de equipamento

| Item | Valor |
|---|---|
| **Prefixo das armas** | **Secura** |
| **Efeito de sindicato** | **Sequence** |
| Tipo de dano do efeito | **Radiation** |
| Restauração do efeito | 25% de Escudo |
| Buff temporário do efeito | **+50% de Escudo base** |
| Eximus Specter (Rank 1) | MOA — Blitz Eximus Specter |
| Team Bonus Consumable (Rank 3) | **Squad Energy Restore (Large)** |
| Syandana (Rank 5) | **Secura Syandana** — brilha conforme os **Credits coletados** |

### Weapon Augment Mods (Rank 4)

| Mod | Arma |
|---|---|
| **Deadly Sequence** | Grinlok (e Prisma Grinlok) |
| **Sequence Burn** | Spectra (e Spectra Vandal) |
| **Toxic Sequence** | [[armas/secundarias/acrid.md|Acrid]] |
| **Voltage Sequence** | [[armas/primarias/lanka.md|Lanka]] |

### Armas exclusivas (Rank 5)

[[armas/primarias/secura_penta.md|Secura Penta]] (primária) · **Secura Dual Cestra** (secundária) · [[armas/brancas/secura_lecta.md|Secura Lecta]] (melee)

> Armas de sindicato são versões modificadas de armas existentes, com stats alterados e — exceto as melee — o **efeito de sindicato embutido**, idêntico ao que um Weapon Augment Mod dá. **São tradeáveis**, mas só se estiverem **sem uso, sem rank e sem Forma ou Orokin Catalyst**. Todas têm requisito de Mastery Rank.

### Partes de Archweapon vendidas aqui (Rank 5)

Corvas (Receiver) · Cyngas (Receiver) · Dual Decurion (Barrel) · Fluctus (Stock) · Phaedra (Receiver) · Velocitus (Receiver) · Agkuza (Handle) · Centaur (Handle) · Kaszas (Handle) · Onorix (Handle) · Rathbone (Handle)

### Warframes cujos augments este sindicato vende (Rank 5)

Banshee · Caliban · Chroma · Dagath · Gauss · Gyre · Hildryn · Inaros · Ivara · Mag · Nekros · Nidus · Nokko · Protea · Revenant · Rhino · Sevagoth · Trinity · Uriel · Valkyr · Vauban

> Cada Warframe é favorecido por **dois** sindicatos. A lista completa de augment por frame está em [[mecanicas/augments.md|Augments]].

### Ofertas por rank (estrutura comum a todos os 6 sindicatos de facção)

| Rank | O que abre |
|---|---|
| **1** | **Eximus Specter** próprio do sindicato · Syndicate Alerts |
| **2** | **Syndicate Relic Pack** — 3 Void Relics por 20.000 Standing (2 Lith/Meso + 1 garantida Neo/Axi) |
| **3** | **Large Team Bonus Consumable** próprio do sindicato (blueprint reutilizável de 10 unidades) |
| **4** | **Weapon Augment Mods** — mods exclusivos de arma, que também ativam o **efeito de sindicato** da arma |
| **5** | **Warframe Augment Mods** (25.000 cada) · **armas exclusivas** do sindicato · **Syandana** própria · partes de Archweapon · entrada do sindicato no Relay redesenhada com destaques em bronze |

> **Como funciona o efeito de sindicato na arma:** equipar um **Weapon Augment Mod** faz a arma acumular Syndicate Points a partir da Affinity que ela ganha, mostrados numa barra ao lado do contador de munição. Cheia, a barra zera e a arma dispara o efeito: **dano elemental radial + buff temporário de stat + restauração de stat**, tudo de uma vez.

### Death Squad

Standing negativo faz o sindicato caçar você com **Death Squads** de Eximus. Eles chegam com luzes piscando e uma transmissão do líder do sindicato, e vêm **envoltos em luz vermelha** (é como se diferencia de um Assassin normal).

| Rank de desfavor | O que vem |
|---|---|
| **−1** | **Eximus Squad** — 3 a 5 unidades Eximus |
| **−2** | **Eximus Platoon** — 5 a 8 unidades Eximus |

Como todo Eximus, eles têm **Overguard**, que os torna imunes a crowd control (Chaos, Stasis, Gloom) até ser removido. Cada unidade abatida tem chance de dropar o **blueprint de Specter** do tipo dela.

O Death Squad deste sindicato é sempre do mesmo tipo: **MOA — Arctic Eximus**.

**Matar o Death Squad não muda o Standing** nem desencoraja o sindicato. Outros Tenno podem ajudar sem sofrer penalidade. E, diferente de Assassins, **não existe Death Mark nem aviso no inbox** — o único indicador é o próprio Standing negativo.

---

## 🛠️ Como Explorar na Prática

| Objetivo | O que fazer |
|---|---|
| Subir Standing rápido | Pledge no terminal da Orbiter (15% da Affinity) + as **3 Syndicate Alerts diárias** + os **8 medalhões** de cada alerta. Alerta e medalhão **não contam** no teto diário |
| Não desperdiçar Standing | Promover de rank **consome tudo**. Compre o que quiser **antes** de subir |
| Pegar os augments sem brigar | Augments são **tradeáveis**. Em vez de inverter 176.000 de Standing, compre do mercado |
| Farmar este sindicato em paralelo | Perrin + **New Loka** + **Red Veil** é um dos 3 grupos totalmente não-hostis, com **Steel Meridian** como reboque via Red Veil |
| Evitar Death Squad | Não acumule Standing negativo. Se acumular, espere Eximus Squad (3–5) ou Platoon (5–8) com Overguard |
| Escolher o presente de promoção | Arma exclusiva **não pode** ser o presente grátis — escolha mod ou cosmético e compre a arma com Standing |
| Efeito de sindicato na arma | Equipe um **Weapon Augment** desta lista. A arma passa a acumular Syndicate Points pela Affinity dela e dispara Sequence (Radiation radial + +50% de Escudo base + 25% de Escudo) quando a barra enche |

---

## ⚠️ Erros Comuns

- **"Posso subir todos os sindicatos."** Não ao mesmo tempo. Subir The Perrin Sequence **derruba** Arbiters of Hexis (−50%) e Steel Meridian (−100%).
- **"Standing sobra depois da promoção."** **Todo** o Standing é consumido ao subir de rank, mais um sacrifício em Credits e recursos.
- **"Alerta de sindicato conta no teto diário."** **Não.** Nem os medalhões. São a única forma de passar dos 16.000 + 500/MR.
- **"Acho medalhão em qualquer alerta."** Só com **Standing favorável** com o sindicato que ofereceu a missão.
- **"Arma de sindicato que usei é tradeável."** Só se estiver **sem uso, sem rank, sem Forma e sem Catalyst**.
- **"Melee de sindicato tem o efeito embutido."** **Não.** As melee exclusivas são a exceção: não trazem o efeito de sindicato.
- **"Matar o Death Squad melhora meu Standing."** Não muda nada, nem para cima nem para baixo.
- **"Caí 3 ranks, preciso de 3 sacrifícios."** Desde o Update 16, é **um sacrifício por tier** ao se mover entre eles.
- **"Posso escolher outro presente ao reconquistar o rank."** Não. Reobter rank após rebaixamento **não** libera outra escolha.

---

## 🔗 Mecânicas Relacionadas

- [[mecanicas/sindicatos/_Sindicatos _Indice.md|Sindicatos]] — a visão geral das 18 facções e suas relações.
- [[mecanicas/augments.md|Augments]] — a tabela completa de Warframe → augment → sindicato, e os grupos que não brigam entre si.
- [[mecanicas/mastery_rank.md|Mastery Rank]] — MR 3 abre os sindicatos de facção, MR 8 libera as melee de sindicato, MR 12 as primárias; o teto diário sobe 500 por rank.
- [[mecanicas/trading.md|Trading]] — augments, armas de sindicato não usadas e armadura de sindicato são tradeáveis.
- [[mecanicas/dano_e_status.md|Dano e Status]] — o efeito Sequence entrega **Radiation**, o que define contra quem ele vale.
- [[mecanicas/forma_e_polaridades.md|Forma e Polaridades]] — pôr Forma numa arma de sindicato a torna **intradeável** para sempre.
- [[mecanicas/nightwave.md|Nightwave]] — vende alguns dos mesmos augments por 20 Cred, sem exigir Standing.
- [[mecanicas/sindicatos/new_loka.md|New Loka]] — aliado: +50% de Rep junto.
- [[mecanicas/sindicatos/arbiters_of_hexis.md|Arbiters of Hexis]] — oposto: −50% de Rep.
- [[mecanicas/sindicatos/steel_meridian.md|Steel Meridian]] — inimigo: −100% de Rep.

---

## 📚 Fontes
- https://wiki.warframe.com/w/Syndicate — descrição e relações do sindicato, tabela de ranks e Standing, conversão de 15% da Affinity, teto diário, ofertas por rank (Specter, Relic Pack, Team Bonus Consumable, Weapon Augments, Warframe Augments), tabela de efeito de sindicato por facção (dano, restauração e buff), armas exclusivas, Syandanas, partes de Archweapon, Death Squads, Syndicate Alerts e Medallions (consultado em 2026-10-04)
- https://wiki.warframe.com/w/Warframe_Augment_Mods — lista de Warframes favorecidos e regras de aquisição (consultado em 2026-10-04)
