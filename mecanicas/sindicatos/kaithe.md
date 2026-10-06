---
title: Kaithe
aliases: [Kaithe]
tipo: mecanica
resumo: "Kaithe — Montaria de Duviri do Drifter: criatura equina com asas etéreas que voa, corre a 7 m/s (14 m/s em dash) e tem quatro habilidades próprias destravadas pelos Riding Intrinsics."
status: completo
rag: true
tags: [mecanica, kaithe, duviri, drifter, montaria, intrinsics]
fontes: ["https://wiki.warframe.com/w/Kaithe"]
atualizado: 2026-10-07
verificado: true
agente: opus
---

# Kaithe

> [!info] Em uma linha
> Montaria de Duviri do Drifter: criatura equina com asas etéreas que voa, corre a 7 m/s (14 m/s em dash) e tem quatro habilidades próprias destravadas pelos **Riding Intrinsics**.

> [!warning] Nota de estrutura do vault
> Este arquivo está dentro de `mecanicas/sindicatos/`, mas o **Kaithe não é um sindicato** — é a montaria de Duviri. O arquivo foi preenchido com o conteúdo correto do que ele nomeia. Os sindicatos que ainda **não têm arquivo** no vault são **Ventkids**, **Kahl's Garrison**, **The Hex** e **Nightcap**. Ver `_MODELOS/_STATUS_opus.md`.


## ⚙️ Como Funciona — Kaithe


> *"O Kaithe de Duviri. Uma memória vestida num sonho de aço. Mais rápido que flechas, mais leal que o coração de um soldado firme. Corra reto, nobre Kaithe!"* — Bombastine

Os **Kaithes** são criaturas equinas que habitam **[[locais/open-worlds/duviri.md\|Duviri]]**. Apesar de serem criaturas terrestres, possuem um **par de asas etéreas** que lhes permite **voar** pelos céus de Duviri. Introduzidos no Update 33.0 (2023-04-26).

O Kaithe é obtido na quest **[[missoes/jornadas/principais/the_duviri_paradox.md\|The Duviri Paradox]]**. Como **[[lore/personagens/the_drifter.md\|Drifter]]**, ele é invocado com a primeira habilidade, **Summon Kaithe**.

Montado, o Drifter usa **controles de movimento equinos**, empunha o **Sirocco** e acessa **quatro habilidades especiais**. Todos os stats do Kaithe — vida, escudo, armadura, energia — são **herdados do montador**, e o Kaithe **não é modável** nem tem variantes customizáveis de stat (só cosméticas).


## 🔢 Fórmulas e Números — Kaithe


```
Velocidade        =  7 m/s
Velocidade de dash = 14 m/s

Vida, escudo, armadura e energia = HERDADOS do montador
Modável = NÃO

Cooldown de desmontar = 1,25 s
  (reduzido a 1 s com Combat Intrinsic Rank 5 — Swifter Abilities)

Hoof Stomp (habilidade 3)      = 150 de dano + Stagger em área
Steadfast Dismount (habilidade 4) = 150 de Overguard, cooldown de 150 s
Tempered Benison / Neural Pulse: Guiding Hand expõe weakpoint por 10 s,
  e acertar o weakpoint faz 3x de dano (Combat Intrinsic Rank 6)
Overpowering Abilities: +150% de dano do Drifter por 3 s ao montar
  ou desmontar (Combat Intrinsic Rank 10)
```

| Variável | Significado | Fonte do valor |
|---|---|---|
| 7 / 14 m/s | Velocidade normal e de dash | Wiki, Kaithe (infobox) |
| 1,25 s → 1 s | Cooldown de desmontar, reduzido pelo Combat Rank 5 | Wiki, Summon Kaithe |
| 150 de dano | Hoof Stomp | Wiki, Hoof Stomp |
| 150 Overguard / 150 s | Steadfast Dismount e seu cooldown | Wiki, Steadfast Dismount |
| 3x | Multiplicador no weakpoint exposto por Guiding Hand (Combat Rank 6) | Wiki, Guiding Hand |
| +150% por 3 s | Dano do Drifter ao montar/desmontar (Combat Rank 10) | Wiki, Summon Kaithe |

**Tetos e limites conhecidos:**

- **Summon Kaithe é exclusivo do Drifter em Duviri** — até o **Riding Rank 9 (Equestrian Bond)**, que libera o **Kaithe Summon** nos open worlds do Sistema de Origem.
- **Não pode ser invocado na Teshin's Cave** antes de entrar em Duviri.
- Você é **desmontado ao tomar dano** de inimigos (o Riding Rank 2, **Cavalier Strength**, reduz essa chance) ou ao **atacar com melee**.
- Invocar ou desmontar **parado** é animação de corpo inteiro que trava tudo; **em movimento**, o movimento continua.
- **Todas as peças do Kaithe são puramente cosméticas** e compradas com **Platinum**.


## 📋 Tabelas de Referência — Kaithe


### As quatro habilidades

| Tecla | Habilidade | Efeito | Destravada por |
|---|---|---|---|
| **1** | **Summon Kaithe** | Invoca o Kaithe. Castar de novo desmonta. Invocado no ar, ele abre as asas e planeia na hora. Cooldown de 1,25 s ao desmontar | Riding Rank 1 |
| **2** | **Guiding Hand** | Solta uma luz-guia até o próximo objetivo principal ou secundário. **Prioriza alvos de Conservação** quando um encontro de conservação começa | Base |
| **3** | **Hoof Stomp** | O Kaithe pisoteia o chão (até em pleno voo), criando onda de choque que dá **Stagger**, **150 de dano** e **reduz a armadura** dos inimigos na área | Riding Rank 3 |
| **4** | **Steadfast Dismount** | Desmonta concedendo **150 de Overguard**. Cooldown de **150 segundos** | Riding Rank 6 |

**Upgrade do Guiding Hand:** comprar **Enigma Sense** da **Acrithis** melhora o Guiding Hand permanentemente, marcando os **Duviri Enigma** próximos com ícone no mapa e waypoint.

### Riding Intrinsics (os 10 ranks)

| Rank | Nome | Efeito |
|---|---|---|
| **1** | Summon Kaithe | Tocar `1` invoca o Kaithe (destravado durante The Duviri Paradox) |
| **2** | **Cavalier Strength** | Mais resistência a ser desmontado por inimigo |
| **3** | **Hoof Stomp** | Destrava a habilidade 3 |
| **4** | **Fast Travel** | Viagem rápida pelo mapa para locais centrais de Duviri e para **Materliths** |
| **5** | **Smooth Path** | Plantas e pedras ficam marcadas no mapa enquanto você cavalga (efeito de **Loot Detector**) |
| **6** | **Steadfast Dismount** | Destrava a habilidade 4 |
| **7** | **Endurance Racer** | Reduz o cooldown entre dashes |
| **8** | **Unique Identity** | Permite **dar nome** ao seu Kaithe |
| **9** | **Equestrian Bond** | Libera o **Kaithe Summon nos open worlds do Sistema de Origem** |
| **10** | **Herd Travel** | Viagem rápida pelo mapa até **outros Drifters** |

### Combat Intrinsics que afetam o Kaithe

| Rank | Nome | Efeito |
|---|---|---|
| **5** | **Swifter Abilities** | Reduz o cooldown de habilidade para **1 segundo** |
| **6** | **Neural Pulse** | Em Duviri, **Guiding Hand expõe um weakpoint** nos inimigos por **10 s**; acertar o weakpoint faz **3x de dano** |
| **10** | **Overpowering Abilities** | **+150% de dano do Drifter por 3 s** após montar ou desmontar |

### Componentes cosméticos

Todas as peças são **puramente cosméticas** e compradas com **Platinum**. A customização é feita na **Teshin's Cave** em Duviri ou no **Dagath's Hollow** do [[mecanicas/cla_e_dojo.md\|Clan Dojo]]. Por padrão você começa com o **Histornam Kaithe Pedigree** e o **Histornam Tail**.

| Peça | O que é |
|---|---|
| **Pedigree** | O **corpo principal** do Kaithe. Comprar um Pedigree **inclui o Tail correspondente** |
| **Chamfron** | Os adornos e a armadura **de cabeça** |
| **Tail** | A **cauda** |
| **Saddle** | A **sela** |
| **Coronet** | Adorno de casco |

**Pedigrees:**

| Pedigree | Descrição | Custo |
|---|---|---|
| **Histornam** | O [[lore/personagens/dominus_thrax.md\|Dominus Thrax]] prefere os Histornam acima de todas as raças — foi num deles que aprendeu a cavalgar | **Padrão** |
| **Aetigo** | Espécie nativa da ilha mais ao sul de Duviri. Os olhos de esmeralda refletiam as planícies verdes; quando a ilha virou cinzas, desbotaram até o nada | 220 pl |
| **Psyacus** | Inspira medo nos de coração fraco. Diz-se que quem monta um Psyacus é corajoso ou sem coração | 230 pl |
| **Gynfas** | Os Contos de Duviri falam do Gynfas visitando casas em noite sem lua. Negar-lhe entrada é convidar o infortúnio. Montaria adequada para **[[warframes/regular/dagath.md\|Dagath]]** Yfari | 220 pl |

**Chamfrons:** Dyrncaul (75 pl) · Irdeni (75 pl) · Aethon (75 pl) · Kheyur (65 pl) · Sviari (65 pl) · Aumen (60 pl).

**Tails:** Histornam (padrão) · Aebolg (45 pl) · Caersid (45 pl) · Heoro (45 pl) · Velific (55 pl) · Aetigo e Psyacus (inclusos com o Pedigree correspondente).

**Bundles:**

| Bundle | Conteúdo | Custo |
|---|---|---|
| Grassland Steed Pack | Aetigo Kaithe, Caersid Tail, Sviari Chamfron, Sohseki Saddle | 330 pl |
| Outland Steed Pack | Psyacus Kaithe, Aebolg Tail, Irdeni Chamfron, Dovin Saddle | 340 pl |
| Steed's Regalia Pack | Heoro e Velific Tails, Dyrncaul e Kheyur Chamfrons, Vaidurian Saddle | 245 pl |
| **Royal Steed Pack** | Os três pacotes acima | 800 pl |
| Aethon Kaithe Collection | Aethon Tail, Chamfron e Saddle | 160 pl |
| Aumen Kaithe Collection | Aumen Tail, Chamfron e Saddle | 155 pl |


## 🛠️ Como Usar na Prática — Kaithe


| Objetivo | O que fazer |
|---|---|
| Atravessar Duviri rápido | Cavalgar a 7 m/s, **dash a 14 m/s**, e **voar** sobre o terreno. Riding Rank 7 (**Endurance Racer**) reduz o cooldown entre dashes |
| Não ser derrubado | **Riding Rank 2 (Cavalier Strength)** reduz a chance de desmonte forçado por dano |
| Achar objetivo e Conservação | **Guiding Hand** (tecla 2) aponta o próximo objetivo e **prioriza alvo de Conservação** durante um encontro |
| Achar recurso enquanto cavalga | **Riding Rank 5 (Smooth Path)**: plantas e pedras marcadas no mapa, efeito de Loot Detector |
| Dano real com o Kaithe | **Combat Rank 6 (Neural Pulse)**: Guiding Hand expõe weakpoint por 10 s, e acertar faz **3x de dano** |
| Burst de dano do Drifter | **Combat Rank 10 (Overpowering Abilities)**: **+150% de dano por 3 s** ao montar **ou** desmontar — dá para abusar montando e desmontando em sequência |
| Sobreviver a um cerco | **Steadfast Dismount** (tecla 4): desmonta com **150 de Overguard**. Cooldown longo de 150 s |
| Remover armadura em área | **Hoof Stomp** (tecla 3) dá Stagger, 150 de dano **e reduz armadura** — funciona até em pleno voo |
| Usar o Kaithe fora de Duviri | **Riding Rank 9 (Equestrian Bond)** libera o **Kaithe Summon** nos open worlds do Sistema de Origem |
| Viajar rápido | Riding Rank 4 (**Fast Travel**, locais centrais e Materliths) e Rank 10 (**Herd Travel**, até outros Drifters) |
| Marcar os Enigma de Duviri | Comprar **Enigma Sense** da **Acrithis** — upgrade permanente do Guiding Hand |
| Dar nome ao Kaithe | **Riding Rank 8 (Unique Identity)** |


## ⚠️ Erros Comuns — Kaithe


- **"O Kaithe é um sindicato."** Não é. É a **montaria de Duviri**. (O arquivo está na pasta de sindicatos por decisão de estrutura do vault, não por ser um.)
- **"Dá para modar o Kaithe."** **Não é modável.** Vida, escudo, armadura e energia são **herdados do montador**, e todas as peças são **cosméticas**.
- **"O Kaithe tem vida própria."** Herda do Drifter. Tomar dano **desmonta** você em vez de matar o Kaithe.
- **"Posso invocar em qualquer lugar."** Só em **Duviri** — até o **Riding Rank 9**, que libera nos open worlds do Sistema de Origem. E **nunca** na Teshin's Cave antes de entrar em Duviri.
- **"Melee não desmonta."** **Atacar com melee desmonta.** É inclusive a forma rápida de sair da montaria.
- **"Hoof Stomp só funciona no chão."** Funciona **em pleno voo** também.
- **"Comprar o Pedigree não dá a cauda."** **Dá.** Todo Pedigree vem com o Tail correspondente.
- **"Steadfast Dismount pode ser spammado."** Cooldown de **150 segundos**.


## 🔗 Relacionados — Kaithe


- [[mecanicas/parkour.md|Parkour]] — o Kaithe substitui o parkour como locomoção em Duviri; 7 m/s contra ~1,0 de Sprint Speed de Warframe.
- [[mecanicas/operator_e_focus.md|Operator e Focus]] — o Drifter é a contraparte do Operator, e usa o Sirocco montado.
- [[mecanicas/mastery_rank.md|Mastery Rank]] — cada rank de **Drifter Intrinsic** vale **1.500 pontos de Mastery**; os 10 ranks de Riding somam 15.000.
- [[mecanicas/incarnon.md|Incarnon]] — o Circuit de Duviri é a fonte dos Incarnon Genesis, e Drifter Intrinsics Opportunity Rank 9 muda as recompensas das tiers 5 e 10.
- [[mecanicas/steel_path.md|The Steel Path]] — em Duviri o SP dá **+20 de nível** sem bônus de vida nem escudo, e as missões de Duviri no SP pagam 5 Steel Essence e 15 Pathos Clamp.
- [[mecanicas/platinum.md|Platinum]] — todas as peças e bundles do Kaithe são compradas com Platinum.
- [[mecanicas/cla_e_dojo.md|Clã e Dojo]] — o **Dagath's Hollow** do Dojo é um dos dois lugares onde o Kaithe pode ser customizado.
- [[locais/open-worlds/duviri.md|Duviri]] — a região.
- [[lore/personagens/the_drifter.md|The Drifter]] — o único que monta o Kaithe.
- [[lore/personagens/dominus_thrax.md|Dominus Thrax]] — ligado ao Pedigree Histornam.
- [[warframes/regular/dagath.md|Dagath]] — o Pedigree Gynfas é descrito como a montaria dela.
- [[missoes/jornadas/principais/the_duviri_paradox.md|The Duviri Paradox]] — a quest que entrega o Kaithe.
- [[missoes/bounties/duviri.md|Bounties de Duviri]] — onde o Kaithe é usado no dia a dia.
- [[recursos/open_worlds/duviri/pathos_clamp.md|Pathos Clamp]] e [[recursos/open_worlds/duviri/cavaleros_burden.md|Cavalero's Burden]] — recursos da região.

---
