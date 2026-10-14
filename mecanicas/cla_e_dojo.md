---
title: Clã e Dojo
aliases: [Clã e Dojo, Cla e Dojo, clã, dojo, pesquisa do clã, laboratório do dojo]
tipo: mecanica
resumo: "O clã é a estrutura social do jogo e o Dojo é a base dele: salas de Research que replicam equipamento por Credits, Trading Post com taxa configurável, Dry Dock para Railjack — tudo pago em recursos multiplicados pelo Clan Tier."
status: completo
rag: true
tags: [mecanica, cla, dojo, pesquisa, clan-vault, tier]
fontes: ["https://wiki.warframe.com/w/Clan_Dojo", "https://wiki.warframe.com/w/Clan"]
atualizado: 2026-10-07
verificado: true
agente: opus
---

# Clã e Dojo

> [!info] Em uma linha
> O clã é a estrutura social do jogo e o Dojo é a base dele: salas de Research que replicam equipamento por Credits, Trading Post com taxa configurável, Dry Dock para Railjack — tudo pago em recursos multiplicados pelo **Clan Tier**.


## ⚙️ Como Funciona — Clã e Dojo


Para entrar no Dojo é preciso construir uma **Clan Key** — o blueprint vem automaticamente ao entrar num clã. Depois disso, o Dojo aparece no Star Chart como se fosse um planeta, com um nó com o nome do clã e a opção de visitar clãs em destaque.

O Dojo é construído por membros com o privilégio **Architect**, e limitado por **três recursos independentes**: **Capacity** (quantas salas), **Energy** (quantas salas, de outra forma) e **Decoration Capacity** (quantas decorações, por sala). O teto absoluto é de **128 salas**.

Toda construção passa por duas fases: **Funding** (qualquer membro doa recursos do inventário pessoal; quem tem **Treasurer** doa do **Clan Vault**) e **Construction** (contagem em tempo real, acelerável por Platinum — mínimo de 1 pl, e cada pl reduz um pouco o cronômetro).

> [!danger] O multiplicador de tier é a decisão mais importante do clã
> O **Clan Tier** define o cap de membros **e multiplica todo custo** de pesquisa, sala e decoração: **x1, x3, x10, x30, x100**. Um clã **Moon** paga **100x** o que um **Ghost** paga pela mesma pesquisa. Clã grande sem gente ativa é a armadilha clássica.


## 🔢 Fórmulas e Números — Clã e Dojo


```
Clan Key: 1.500 Credits + 1 Morphics(?) + 500 + 500 de recursos
  Tempo: 12 h  ·  Rush: 10 Platinum

Custo final = custo base (Ghost) x Clan Tier Multiplier

Capacity:
  1ª Clan Hall           = +100
  Inspiration Hall       = +100
  Demais Clan Halls      = +200 cada
  Toda sala que não é Hall CONSOME capacity

Energy:
  Cada Reactor construído = +25 Energy
  Toda sala, exceto Reactor, consome Energy
  Decoração NÃO consome Energy (só Decoration Capacity)

Teto de salas = 128
  Ao atingir, toda porta não usada mostra "Dead End"

Toda sala exige 1 Forma (ou mais, nos tiers altos)
  Mountain: 8 Forma  ·  Moon: 15 Forma, em vários casos

Bônus de recurso para o Clan Vault, jogando com gente do clã:
  2 jogadores do mesmo clã = +10% por jogador
  3 jogadores             = +15% por jogador
  Squad cheio (4)         = +20% por jogador
```

| Variável | Significado | Fonte do valor |
|---|---|---|
| 12 h / 10 pl | Forja e rush da Clan Key | Wiki, Clan Dojo § Access Acquisition |
| +100 / +200 | Capacity da 1ª Hall e da Inspiration Hall / das demais Halls | Wiki, Clan Dojo § Capacity |
| +25 | Energy por Reactor | Wiki, Clan Dojo § Energy |
| 128 | Teto absoluto de salas | Wiki, Clan Dojo § Dojo Room Limitations |
| x1 / x3 / x10 / x30 / x100 | Clan Tier Multiplier de Ghost a Moon | Wiki, Clan § Clan Tier |
| +10% / +15% / +20% | Bônus de recurso para o Vault por jogador, com 2 / 3 / 4 do mesmo clã | Wiki, Clan Dojo § Clan Vault |
| 60 dias | Moratória de ascensão após fazer downsize do clã | Wiki, Clan § Clan Tier |
| ~1 Forma por sala | Mínimo; Mountain chega a 8 e Moon a 15 | Wiki, Clan § Clan Tier Multiplier |

**Tetos e limites conhecidos:**

- **Doação ao Clan Vault é irreversível.** Recurso ou decoração doado **não volta**.
- **Sala usada como pré-requisito não pode ser destruída** enquanto a sala dependente existir.
- Cancelar uma sala **antes** de ela ficar totalmente financiada devolve tudo: o que veio de inventário pessoal volta ao membro, o que veio do Vault volta **ao Vault**, não aos membros.
- **Decoration Capacity de uma sala não pode ser aumentada.** É fixa por tipo de sala.
- Salas únicas (Clan Halls, Barracks, Dry Dock) **desaparecem da lista** depois de construídas.
- Tier só sobe **um degrau por vez**, em ordem, e **não dá para fazer downsize durante um evento**.
- Um **Treasurer** é **forçado** a doar do Vault primeiro: não há opção na UI para priorizar o inventário pessoal (só se o Vault ficar sem o recurso).
- **Articulas, Displays e itens únicos não podem ir para o Vault**: Ambulas Noggle, Stalker Noggle, Shadow Debt Noggles, Kuria Statuette, Sacred Vessel, Oro Ornament, Rell's Donda, Prominence Wisp Totem, Thousand-Year Fish Statuette.


## 📋 Tabelas de Referência — Clã e Dojo


### Clan Tier

| Tier | Cap de membros | Membros para ascender | Barracks exigida | **Multiplicador de custo** |
|---|---|---|---|---|
| **Ghost** | 10 | 1 | — | **x1** |
| **Shadow** | 30 | 5 | Shadow Barracks | **x3** |
| **Storm** | 100 | 15 | Storm Barracks | **x10** |
| **Mountain** | 300 | 30 | Mountain Barracks | **x30** |
| **Moon** | 1.000 | 50 | Moon Barracks | **x100** |

Exemplos do multiplicador na prática: projeto de base 10.000 Credits custa **30.000** em Shadow · base 600 Ferrite custa **6.000** em Storm · base 650 Salvage custa **19.500** em Mountain · base 500 Circuits custa **50.000** em Moon.

> **Nota técnica:** os custos base são de fato calculados a partir do tier **Moon** e divididos para baixo, arredondando. É por isso que Forma de sala pode ser 1 nos três primeiros tiers e salta para 8 (Mountain) e 15 (Moon).

### Hierarquia e privilégios

8 posições, cada uma um **conjunto de privilégios**, não um nível de autoridade. O criador começa como **Founding Warlord** com tudo.

| Privilégio | O que permite |
|---|---|
| **Ruler** | Adicionar e remover permissões dos outros |
| **Recruiter** | Convidar jogadores para o clã |
| **Regulator** | Expulsar jogadores de rank inferior |
| **Promotion** | Promover membros até o próprio nível |
| **Architect** | Construir e destruir **salas e decorações** |
| **Dojo Decorator** | Construir e destruir **só decorações** |
| **Treasurer** | Financiar do **Clan Vault** em vez do inventário pessoal, e **ajustar a taxa de trade do clã** |
| **Tech** | Enfileirar projetos de Research para os membros financiarem |
| **Tactician** | Enfileirar Solar Rails no Orokin Lab e implantá-los |
| **Chat Moderator** | Expulsar ou suspender do chat do clã |
| **Herald** | Alterar e publicar a Message of the Day |
| **Fabricator** | Replicar tecnologia do clã |

**Atribuição padrão de novo clã:**

| Posição | Ruler | Recruiter | Regulator | Promotion | Architect | Treasurer | Tech | Tactician |
|---|---|---|---|---|---|---|---|---|
| Warlord | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| General | — | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Officer | — | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | — |
| Leader | — | ✔ | — | — | ✔ | — | ✔ | — |
| Sage | — | ✔ | — | — | ✔ | ✔ | ✔ | — |
| Soldier | — | ✔ | — | — | — | — | ✔ | — |
| Initiate | — | — | — | — | — | — | — | — |
| Utility | — | — | — | — | ✔ | — | — | — |

### Salas que importam

| Sala | Para quê |
|---|---|
| **Oracle** | **Pré-requisito de todos os Research Labs.** É a primeira coisa a construir depois das Halls |
| **Energy Lab** | Replicar armas de energia (Amprex, Synapse, Flux Rifle…) |
| **Chem Lab** | Replicar armas químicas (Acrid, Torid, Ignis Wraith…) |
| **Tenno Lab** | Partes de Banshee, Nezha, Volt e Zephyr · **Landing Craft Segment** · Prova, Dex |
| **Bio Lab** | Armas Infestadas (Hema, Mutalist Cernos, Pathocyst…) |
| **Orokin Lab** | Armas Orokin e Solar Rails |
| **Dry Dock** | **Railjack** — construção e gerenciamento. Sala única |
| **Ventkids' Bash Lab** | Peças de K-Drive |
| **Dagath's Hollow** | Pesquisa ligada à Dagath |
| **Observatory** | Libera **Navigation** e **Arsenal** dentro do Dojo (sem ela, não dá para trocar loadout nem lançar missão de lá) |
| **Reactor** | **+25 Energy** cada. Pode ser construída em qualquer lugar |
| **Barracks** | Define o **Clan Tier** (Shadow / Storm / Mountain / Moon) |
| **Crimson Branches** | Tradear **Adversaries** (Lich, Sister, Coda) |
| **Clan Hall** | Capacity (+100 na 1ª, +200 nas demais) e ponto de spawn para visitantes |
| **Duel Room** | Área de duelo entre Tenno |
| **Obstacle Course** | Padrão ou customizada; guarda recorde de tempo |
| **Temple of Honor** | Área social |

### Decorações funcionais

| Decoração | Função |
|---|---|
| **Treasury** | Onde membros doam recursos e decorações pessoais ao **Clan Vault** |
| **Trading Post** | Permite ao Treasurer definir a taxa de trade do Dojo (**0% a 100%**) e facilita o trade |
| **Transporter** | Teleporte customizado dentro do Dojo, com nome próprio |
| **Ascension Altar** | Onde o clã inicia a **Ascension Ceremony** para subir de Rank, e onde os membros recebem **Endo** |
| **Ludoplex** | Comprado do **Cephalon Simaris** e doado ao Vault. Minijogos |
| **Clan Vault (decoração)** | Qualquer membro pode doar **Credits** direto interagindo com ela |

### Clan Rank (Affinity do clã)

Clan Affinity vem de: construir pela **primeira vez** Oracle, Bio Lab, Chem Lab, Energy Lab, Tenno Lab, Orokin Lab, Duelling Room, Obstacle Course, Trading Post, Treasury e Temple of Honor; e de **concluir Research**.

| Rank | Próximo rank exige | XP total |
|---|---|---|
| 0 | 11.000 | 0 |
| 1 | 23.000 | 11.000 |
| 2 | 35.000 | 34.000 |
| 3 | 45.000 | 69.000 |
| 4 | 54.000 | 114.000 |
| 5 | 63.000 | 168.000 |
| 6 | 71.000 | 231.000 |
| 7 | 79.000 | 302.000 |
| 8 | 87.000 | 381.000 |
| 9 | 95.000 | 468.000 |
| 10 | 102.000 | 563.000 |
| 11 | 109.000 | 665.000 |
| 12 | 117.000 | 774.000 |
| 13 | 123.000 | 891.000 |

**Total de Clan Affinity disponível (Update 39.0, 2025-06-25):** 729.000 em 211 itens — ou **712.000 em 210** descontando exclusivos. Distribuição: Weapons 288.000 (90 itens) · Rooms 160.000 (14) · Gear 74.000 (25) · Warframes 52.000 (6) · Pigments 40.000 (40) · Archwings 22.500 (3) · Orbiter Segments 18.000 (3) · Solar Rail Construction 17.000 (1, **impossível desde o Update 16.0**) · Archguns 14.000 (4) · Resources 9.000 (4) · Visitors 8.000 (8) · Backdrops 6.000 (6) · Companions 6.000 (2) · Archmelees 5.000 (1) · Superchargers 5.000 (1) · K-Drive Scrawls 4.500 (3).


## 🛠️ Como Usar na Prática — Clã e Dojo


| Objetivo | O que fazer |
|---|---|
| Escolher o tier certo | **Fique em Ghost ou Shadow** se o clã é pequeno e ativo: x1 ou x3 de custo. Um clã Moon com 20 pessoas ativas **não consegue** financiar pesquisa (x100) |
| Reduzir o custo de um clã inchado | Desde o Update 18.0 é possível fazer **downsize** — mas há **60 dias de moratória** para voltar a subir, e não dá para fazer durante evento |
| Ordem de construção | Clan Hall → **Oracle** (pré-requisito dos labs) → **Tenno Lab** (Landing Craft Segment, partes de 4 Warframes) → **Dry Dock** (Railjack) → Reactors conforme falta Energy |
| Habilitar Arsenal no Dojo | Construir o **Observatory**. Sem ele não há Navigation nem Arsenal dentro do Dojo |
| Zerar a taxa de trade | Com privilégio **Treasurer**, defina a taxa do **Trading Post** em **0%** — bate os +10% fixos do Maroo's Bazaar. Ver [[mecanicas/trading.md\|Trading]] |
| Ganhar recursos jogando junto | Squad cheio do mesmo clã dá **+20% por jogador** direto para o Clan Vault, **sem** tirar nada do seu inventário pessoal |
| Estocar Forma antes de construir | **Toda** sala consome Forma, e Mountain/Moon chegam a 8 e 15. Farme [[recursos/raridades/especial/forma.md\|Forma]] blueprint em Void Relics antes de planejar |
| Economizar Capacity | Planeje onde as **Clan Halls** vão ficar **antes** de construir corredores. Sem Capacity para o corredor, só resta destruir salas (e perder as decorações delas) |
| Resolver falta de Energy | **Reactor**: +25 Energy cada, construível em qualquer lugar. Decoração não consome Energy |
| Pegar Endo de ascensão | Construa um **Ascension Altar**: os membros recebem Endo quando o clã sobe de tier |
| Tradear Lich / Sister / Coda | Exige a sala **Crimson Branches** |
| Não perder doação | Doação ao Vault é **permanente**. Confira antes |


## ⚠️ Erros Comuns — Clã e Dojo


- **"Clã maior é melhor."** É o contrário em termos de custo: **Moon paga 100x** o que Ghost paga pela mesma pesquisa. Tier grande só vale com muita gente **ativa** financiando.
- **"Capacity e Energy são a mesma coisa."** São dois pools independentes. Capacity vem das **Clan Halls**; Energy vem dos **Reactors**. Faltar um dos dois bloqueia a sala.
- **"Decoração gasta Energy."** Não. Decoração gasta **só** Decoration Capacity, que é fixa por sala e **não pode ser aumentada**.
- **"Posso construir 200 salas."** O teto é **128**. Depois disso toda porta livre mostra "Dead End".
- **"Dá para destruir qualquer sala."** Não se ela for **pré-requisito** de outra sala construída.
- **"Cancelei a sala, meu recurso voltou."** Volta — mas o que foi doado **pelo Vault** volta ao **Vault**, não aos membros.
- **"Doei uma decoração por engano, peço de volta."** Doação ao Clan Vault é **irreversível**.
- **"Como Treasurer eu escolho de onde doar."** Não. A UI **força** o Vault primeiro; só vai ao inventário pessoal se o Vault não tiver o recurso.
- **"Dá para pular um tier."** Não. A ascensão é **um degrau por vez**, em ordem.
- **"Posso construir o lab direto."** Todo Research Lab exige o **Oracle** antes.
- **"Dá para usar o Arsenal em qualquer Dojo."** Só com **Observatory** construído.
- **"Solar Rail ainda dá Clan Affinity."** A construção de Solar Rail **só foi possível até o Update 16.0 (2015-03-19)** — os 17.000 de Affinity dela são inalcançáveis hoje.


## 🔗 Relacionados — Clã e Dojo


- [[mecanicas/trading.md|Trading]] — o Trading Post e a taxa de hub de 0% a 100% definida pelo Treasurer; o Dojo é um dos dois locais de trade do jogo.
- [[mecanicas/forja.md|Forja]] — o Landing Craft Segment sai do Tenno Lab por 15.000 Credits; a Clan Key é um item de forja (12 h).
- [[mecanicas/forma_e_polaridades.md|Forma e Polaridades]] — toda sala do Dojo consome Forma, e nos tiers altos a conta explode.
- [[mecanicas/mastery_rank.md|Mastery Rank]] — armas de pesquisa de clã contam Mastery e destravam no MR 15.
- [[mecanicas/platinum.md|Platinum]] — rush de sala (mínimo 1 pl), renomear clã (200 pl) e trocar emblema (150 pl), ambos só pelo Warlord.
- [[mecanicas/sindicatos/cephalon_simaris.md|Cephalon Simaris]] — vende o Ludoplex, que é doado ao Vault.
- [[mecanicas/baro_ki_teer.md|Baro Ki'Teer]] — a alternativa a pesquisa de clã para armas exclusivas.
- [[mecanicas/nightwave.md|Nightwave]] — o Act "Just Visiting" pede visitar um **Featured Dojo**.
- [[recursos/raridades/especial/forma.md|Forma]] e [[recursos/raridades/especial/endo.md|Endo]] — o Forma que o Dojo consome e o Endo que a Ascension Ceremony devolve.
- [[recursos/_Recursos _Indice.md|Recursos]] — tudo que o Clan Vault armazena.

---
