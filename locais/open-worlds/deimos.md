---
title: Cambion Drift (Deimos)
tipo: local
subtipo: open-world
faccao: infested
tags: [local, open-world, infested, deimos]
atualizado: 2026-10-06
verificado: false
agente: opus
---

# Cambion Drift (Deimos)

> [!info] Resumo
> Landscape [[lore/faccoes/infested.md|Infested]] de Deimos, com hub no **Necralisk** (casa da [[mecanicas/sindicatos/entrati.md|House Entrati]]). Mapa **estático** na superfície, com cavernas **procedurais** que descem até ruínas Entrati. Ciclo **Fass / Vome** em vez de dia e noite. Exige **[[missoes/jornadas/principais/heart_of_deimos.md|Heart of Deimos]]**.

---

## 📊 Ficha

| Item | Valor |
|---|---|
| Facção dominante | **[[lore/faccoes/infested.md\|Infested]]**; **Necramechs** como inimigos próprios; **[[lore/faccoes/murmur.md\|The Murmur]]** nos nós de Albrecht's Laboratories |
| Faixa de nível | **20–35** no Drift (Free Roam); **100+** nas Bounties de [[mecanicas/steel_path.md\|Steel Path]] |
| Como desbloquear | **[[missoes/jornadas/principais/heart_of_deimos.md\|Heart of Deimos]]** concluída |
| Junção de entrada | **Nenhuma.** Deimos conecta-se ao Star Chart pela **[[missoes/juncoes/jupiter_junction.md\|Junção de Júpiter]]** a partir dos nós de Orokin Derelict, não por Junção própria do Drift |
| Boss | **[[lore/chefes/zealoid_prelate.md\|Zealoid Prelate]]** (Exequias, nível 30–35) e **Lephantis** (Magnacidium, nível 20–25), nos nós de Orokin Derelict; **The Fragmented** (Effervo, nível 55–60) em Albrecht's Laboratories |
| Nós totais de Deimos | **18**, incluindo **2 hubs** (Necralisk e Sanctum Anatomica) e a Junção de Júpiter |
| Recursos de região | **[[recursos/raridades/comum/nano_spores.md\|Nano Spores]]**, **[[recursos/raridades/comum/mutagen_sample.md\|Mutagen Sample]]**, **[[recursos/raridades/raro/orokin_cell.md\|Orokin Cell]]**, **[[recursos/raridades/raro/neurodes.md\|Neurodes]]** |
| Tileset | **Cambion Drift** (estático na superfície, procedural nas cavernas) |

### Como o Drift funciona por dentro

- **Não é gerado por tiles** como os nós normais: a superfície é um **mapa estático** com features únicas. É **menor** que as Plains of Eidolon e o Orb Vallis, mas tem **sistemas de cavernas ricos** que descem até as ruínas Entrati — e **parte dessas cavernas é procedural**.
- **Dois nós do Star Chart levam ao Drift.** O primeiro nasce o jogador no **extremo oeste**, na caverna atrás do **Albrecht's Prospect**; e, depois de Heart of Deimos, **fora do Necralisk**. O segundo é o próprio **Necralisk**, onde você aparece numa praça de frente para a **Grandmother** e o **Otak**.
- **Cada instância do Necralisk cabe até 50 jogadores**, mas a saída para o Drift é em **squad de 2 a 4 ou solo**. **Cada mapa é uma instância separada** e não é compartilhado entre squads.
- **Entrar no Drift — do Necralisk ou direto do Star Chart — cria uma instância nova**, com geração procedural aplicada a **locais de spawn de recurso, veios minerais e rotas de caverna**.
- **O progresso é salvo** ao: voltar ao Necralisk pelo airlock (encerra a missão e salva tudo); voltar à Orbiter pelo menu; **completar Bounties** (salva automaticamente); e pescar, minerar ou usar consumível (salva aquele conteúdo específico).

---

## 🗺️ Conteúdo Especial

| Item | Detalhe |
|---|---|
| **Sindicato local** | **[[mecanicas/sindicatos/entrati.md\|House Entrati]]** — reputação paga em **Tokens**, não em standing direto. Também **[[mecanicas/sindicatos/necraloid.md\|Necraloid]]** (Loid, nos Isolation Vaults) e **[[mecanicas/sindicatos/cavia.md\|Cavia]]** (Albrecht's Laboratories) |
| **Ciclo** | **Fass / Vome** — ver tabela abaixo. **Não é dia e noite**: são dois wyrms Infested em guerra permanente |
| **Pesca** | Sim, com as espécies divididas por ciclo (ver tabela) |
| **Mineração** | Sim. **Veios minerais aparecem em laranja (ores)** — não em vermelho como nas outras landscapes — **e azul (gems)**. Podem nascer em **qualquer superfície infestada, inclusive hastes e tentáculos**, mas **não em rochas de verdade**. Minérios e gemas são trocados com o **Otak** por **Otak Tokens** |
| **Conservação** | Sim |
| **Bounties** | **Mother**, no Necralisk e em vários pontos do Drift. Ver **[[missoes/bounties/cambion_drift.md\|Bounties do Necralisk]]** |
| **Montaria / veículo** | **Velocipods** selvagens podem ser montados e **funcionam como K-Drive** |
| **Fast travel** | **Blinkpads** em locais fixos, usados por interação direta ou abrindo o mapa e selecionando |
| **Conteúdo de cofre** | **Isolation Vaults** (com Necramechs guardiões) e, depois deles, as **Arcana Bounties** |
| **Corrida** | **K-Drive Races** |

### O ciclo Fass e Vome

O Drift alterna entre dois **wyrms Infested** no fundo do céu: o laranja **Fass** e o azul **Vome**, em guerra constante. Cada um emerge, dispara um feixe que destrói o outro e espalha os restos pelo Drift, até regenerar e se vingar — em ciclo. **Todos os jogadores veem o mesmo wyrm ao mesmo tempo.**

O wyrm ativo determina **a quantidade de inimigos**, **os peixes e a fauna disponíveis** e, por consequência, **a dificuldade do mapa**. O Drift usa **exatamente as mesmas durações de ciclo das Plains of Eidolon** (o ciclo total é, na prática, **1.126 ms mais curto que 150 min**).

| | **Fass** | **Vome** |
|---|---|---|
| Duração | **100 minutos** (junto com o **dia** nas Plains) | **50 minutos** (junto com a **noite** nas Plains) |
| Inimigos | **Aumenta** a quantidade de Infested | **Diminui** a quantidade de Infested |
| Resíduo espalhado | **Vome Residue** — áreas em **azul** que dão **leve bônus de velocidade e regeneração de vida** a Warframes, Companions e Necramechs pilotados | **Fass Residue** — áreas em **vermelho** que **reduzem levemente a movimentação** de Warframes, Companions e Necramechs pilotados |
| Necramechs | Encontrados **desativados**, e **pilotáveis com Transference** | **Autônomos e ativos, aliados ao Tenno** — vagam e engajam os Infested |
| Peixes exclusivos | **Cryptosuctus** (comum), **Ostimyr** (incomum) | **Lobotriscid** (comum), **Glutinox** (incomum), **Aquapulmo** (raro), **Myxostomata** (muito raro) |

**Peixes de qualquer ciclo:** Kymaeros (comum), Barbisteo (comum), Amniophysi (comum), **Vitreospina** (incomum), **Duroid** (incomum), **Chondricord** (incomum), **Flagellocanth** (raro).

> [!tip] O resíduo é invertido em relação ao wyrm ativo
> Reparo fácil de errar: durante **Fass**, o que está espalhado pelo chão é **Vome Residue** (azul, bom para você) — porque é o Vome que acabou de ser destruído. Durante **Vome**, o chão tem **Fass Residue** (vermelho, ruim). O wyrm ativo no céu é o que **matou** o outro.

### Requiem Obelisks — o farm de recurso mais eficiente do Drift

Obeliscos espalhados pela superfície, cada um com um símbolo **Requiem**. A wiki é explícita: **são um método mais eficiente de farmar recursos de mineração e pesca que as próprias atividades** — **exceto** para os recursos mais raros — além de produzirem outros recursos úteis.

| Item | Detalhe |
|---|---|
| Como ativar | Atirar no **Reactive Crystal** com **dano de Void do Operator** |
| Duração | **90 segundos** ativo, com **cooldown de 12 segundos** |
| Efeito | Varia conforme o símbolo Requiem do obelisco (ex.: **Fass (Chaos)** aplica Confusion, fazendo os inimigos se atacarem; **Jahu (Form)** cria uma esfera de 10 m que empurra inimigos) |
| Condições para gerar recurso | O obelisco **ainda ativado**; os Infested **afetados** (ou recém-afetados) pelo efeito dele; e mortos **pelo Operator, por um Necramech ou pelo Excalibur Umbra em forma de specter** (enquanto você usa o Operator) |
| Spawn de inimigo | Na superfície, invoca Infested **4 vezes, em grupos de 3**. Dentro de um **Isolation Vault**, os inimigos nascem **infinitamente** entre a etapa "Defeat Enemy Necramechs" e a ativação do Reactive Crystal do cofre. **Cooldown de 10 minutos** para spawn direto de obelisco |
| Desgaste | **O obelisco tem uma barra de vida pequena**, consumida por cada ativação, até **quebrar e ficar inerte**. **Use ataques de dano baixo** para ativá-lo mais vezes — crítico dentro de um Isolation Vault, onde o spawn é infinito |

> [!important] Habilidade que agrupa inimigo multiplica o obelisco
> Como a condição é o inimigo estar **afetado pelo efeito** e morrer pelo Operator/Necramech, qualquer Warframe que **junte inimigos** acelera muito o processo. Vale trazer um frame de agrupamento mesmo que você vá matar de Operator.

---

## 💎 Recursos Nativos

| Recurso | Raridade | Melhor nó |
|---|---|---|
| **[[recursos/raridades/comum/nano_spores.md\|Nano Spores]]** | Comum | **Terrorem** (Survival, 25–35) — endless no Orokin Derelict |
| **[[recursos/raridades/comum/mutagen_sample.md\|Mutagen Sample]]** | Comum | **Terrorem** (Survival) |
| **[[recursos/raridades/raro/orokin_cell.md\|Orokin Cell]]** | Raro | **Terrorem** (Survival) — Deimos é uma das melhores regiões do jogo para Orokin Cell |
| **[[recursos/raridades/raro/neurodes.md\|Neurodes]]** | Raro | **Terrorem** (Survival) |
| Recursos de mineração e pesca do Drift (Pustulite, Thaumica, Trabeculum, Namalon, Bile, Ganglion, Pheromones, e os fillets de peixe) | Variado | **Requiem Obelisks** na superfície, mais eficientes que minerar ou pescar — exceto para os mais raros |
| **Mother / Father / Daughter / Son / Otak / Grandmother Tokens** | Moeda de sindicato | **Bounties** e troca de recurso com os Entrati |

---

## 🎯 Nós Notáveis

| Nó | Tipo de missão | Facção | Nível | Por que importa |
|---|---|---|---|---|
| **Necralisk** | Hub | Tenno | — | Cidade dos Entrati. **Mother** (bounties), **Otak** (mineração), **Grandmother**, Father, Daughter, Son |
| **Cambion Drift** | Free Roam | Infested | **20–35** | O landscape em si |
| **Terrorem** | [[missoes/tipos/survival.md\|Survival]] | Infested | 25–35 | **Melhor farm de recurso de Deimos** — Nano Spores, Orokin Cell, Neurodes |
| **Magnacidium** | [[missoes/tipos/assassination.md\|Assassination]] | Infested | 20–25 | Boss **Lephantis** |
| **Exequias** | [[missoes/tipos/assassination.md\|Assassination]] | Infested | 30–35 | Boss **[[lore/chefes/zealoid_prelate.md\|Zealoid Prelate]]** |
| **Sanctum Anatomica** | Hub | Tenno | — | Hub de **Albrecht's Laboratories**, aberto por **[[missoes/jornadas/principais/whispers_in_the_walls.md\|Whispers in the Walls]]** |
| **Effervo** | [[missoes/tipos/assassination.md\|Assassination]] | [[lore/faccoes/murmur.md\|The Murmur]] | 55–60 | Boss **The Fragmented**. Exige Whispers in the Walls |
| **Cambire** | Alchemy | The Murmur | 55–60 | Um dos nós com **Omnia [[missoes/tipos/void_fissure.md\|Void Fissure]]** |
| **Persto** | [[missoes/tipos/survival.md\|Survival]] | The Murmur | 55–60 | O outro nó com **Omnia Void Fissure** de Albrecht's |
| **Armatus** | [[missoes/tipos/disruption.md\|Disruption]] | The Murmur | 55–60 | Exige **[[missoes/jornadas/principais/the_deadlock_protocol.md\|The Deadlock Protocol]]** *e* Whispers in the Walls |
| **Testudo** | Netracells | The Murmur | **220–240** | **O nó de nível mais alto de Deimos** — conteúdo de endgame |
| **Munio** | Mirror Defense | The Murmur | 55–60 | Exige Whispers in the Walls |

---

## 📖 Lore

O **Necralisk** é a casa da **House Entrati**, uma família de [[lore/faccoes/orokin.md|Orokin]] **parcialmente Infestados**, ao norte do nó **Dirus** em Deimos. É a ruína de uma **residência Orokin opulenta** — muito menor que uma Orokin Tower — escondida dentro de um grande crescimento Infested no **nordeste do Cambion Drift**.

A família sobreviveu à queda Orokin por ter se infestado deliberadamente, e cada membro guarda uma parte do legado de **[[lore/personagens/albrecht_entrati.md|Albrecht Entrati]]**, o patriarca que abriu as primeiras portas para o Void. Os **Isolation Vaults** nas cavernas guardam o que ele deixou lá embaixo, e **Albrecht's Laboratories** — aberta por **[[missoes/jornadas/principais/whispers_in_the_walls.md|Whispers in the Walls]]** — é a continuação direta dessa linha, agora com **[[lore/faccoes/murmur.md|The Murmur]]** como oposição.

---

## 📚 Fontes
- https://wiki.warframe.com/w/Cambion_Drift — natureza estática da superfície com cavernas procedurais, os dois nós de acesso, limite de 50 jogadores no Necralisk, condições de salvamento de progresso, ciclo Fass/Vome com durações, resíduos, comportamento dos Necramechs e lista de peixes por ciclo, mineração em laranja/azul e troca com Otak, Requiem Obelisks (ativação por Void, 90 s, cooldown de 12 s, condições de drop, spawns, desgaste), Velocipods como K-Drive, Blinkpads (consultado em 2026-10-06)
- https://wiki.warframe.com/w/Module:Missions/data — os 18 nós de Deimos com tipo, facção, nível, tileset, bosses e pré-requisitos; recursos de região de Deimos (consultado em 2026-10-06)
