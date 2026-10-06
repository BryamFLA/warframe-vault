---
title: Stealth e Finishers
aliases: [Stealth e Finishers]
tipo: mecanica
resumo: "Stealth e Finishers — Inimigo que não te viu morre por um multiplicador que chega a 128x o dano da arma, e dá até +500% de Affinity; Finisher converte todo o dano em Finisher Damage, que ignora armadura e escudo."
status: completo
rag: true
tags: [mecanica, stealth, finisher, mercy, parazon, dano-finisher]
fontes: ["https://wiki.warframe.com/w/Finisher", "https://wiki.warframe.com/w/Stealth"]
atualizado: 2026-10-07
verificado: true
agente: opus
---

# Stealth e Finishers

> [!info] Em uma linha
> Inimigo que não te viu morre por um multiplicador que chega a **128x** o dano da arma, e dá até **+500% de Affinity**; Finisher converte **todo** o dano em Finisher Damage, que ignora armadura e escudo.


## ⚙️ Como Funciona — Stealth e Finishers


Inimigos só veem num **cone frontal curto**, limitado pelo cenário, e são ruins em notar ameaça a distância ou **acima da cabeça**. **Agachar** esconde bem a silhueta. **Invisibilidade** permite passar pela visão deles sem suspeita — mas **ruído alto ainda os alerta de todas as direções**, inclusive contra um Tenno invisível.

O alerta tem três estados, visíveis pela cor do minimapa: **branco** (não alertado), **âmbar** (alerta menor) e **vermelho** (combate total). Alerta menor já **bloqueia Stealth Attack** — e o alerta decai com o tempo.

Finishers são ataques de melee com animação própria e dano altíssimo. **Todo o dano é convertido em Finisher Damage**, e o jogador fica **invulnerável durante a animação**. Existem quatro famílias: **Stealth Attack** (inimigo desprevenido, pelas costas), **Ground Finisher** (inimigo no chão), **Front/Back/Universal Finisher** (inimigo vulnerabilizado por habilidade ou ataque), e **Mercy** (pelo Parazon, em inimigo marcado).


## 🔢 Fórmulas e Números — Stealth e Finishers


```
Stealth Damage Bonus = 1 + 0,20 x rank da arma
  Armas com rank máximo 40 (Paracesis, Kuva, Tenet, Coda):
Stealth Damage Bonus = 1 + 0,15 x rank da arma

  Nos dois casos, arma totalmente rankeada dá bônus de +7x (rank 30) ou 8x (rank 40)

Dano de Stealth Finisher =
  Dano da arma  x  Multiplicador do tipo de melee  x  (1 + Stealth Damage Bonus)

Se der crítico:
  Dano da arma  x  Multiplicador do tipo  x  (1 + Stealth Damage Bonus + Multiplicador Crítico)

Mods elementais e físicos aplicam apenas METADE do bônus antes da conversão

Dano de Mercy = vida residual do inimigo + 1

Bônus de Affinity de stealth kill:
  +100% cumulativo por abate furtivo, até +500% (5 abates)
  Janela do combo: 30 s, renovada a cada abate furtivo

Velocidade da animação de finisher:
  Teto de 33% mais rápido, atingido com +50% de velocidade de ataque
  A velocidade de ataque BASE da arma não afeta a animação
```

| Variável | Significado | Fonte do valor |
|---|---|---|
| 1 + 0,20 × rank | Stealth Damage Bonus de arma de rank máximo 30 | Wiki, Finisher § Stealth Attack |
| 1 + 0,15 × rank | Mesmo bônus, para arma de rank máximo 40 | Wiki, Finisher § Stealth Attack |
| +7x / 8x | Bônus final de arma maxada (rank 30 / rank 40) | Wiki, Finisher § Stealth Attack |
| metade | Fração do bônus de mod elemental e físico aplicada antes da conversão | Wiki, Finisher § Stealth Attack |
| +500% | Teto do bônus de Affinity, após 5 abates furtivos | Wiki, Stealth § Affinity Bonus |
| 30 s | Janela do combo de stealth kill | Wiki, Stealth § Affinity Bonus |
| 50 m | Raio em que arma ou habilidade ruidosa alerta inimigos | Wiki, Stealth § Fighting Silently |
| ~1,5 s | Tempo que o inimigo leva para acionar o alarme no console | Wiki, Stealth § Control Panels |
| 10 s | Duração da marca do Parazon na oportunidade de Mercy | Wiki, Finisher § Mercies |
| 33% | Teto de aceleração da animação de finisher | Wiki, Finisher |

**Tetos e limites conhecidos:**

- **Alerta menor já bloqueia Stealth Attack.** Só volta a funcionar quando o alerta cai abaixo disso.
- **Infested e Corrupted não usam alarme manual**, mas são hive-mind: um único inimigo em combate total põe **todos** num raio enorme em alerta menor. Por isso **não dá para recuperar stealth** contra essas facções — só contra Grineer e Corpus, resetando o alarme num console.
- **Pop-up de dano de stealth é sempre amarelo**, igual a crítico, mesmo quando não houve crítico.
- Stealth Damage Bonus **não funciona no Simulacrum** sem Enemy AI ativado.
- **Finisher só pode ser executado uma vez por inimigo** até ele ser vulnerabilizado de novo. Exceções: **Desiccation** do Inaros permite atacar várias vezes na duração, e Stealth Finisher em **Nox** também.
- **Mercy não dispara enquanto o inimigo tiver escudo**, mesmo abaixo do limiar de vida. Se o escudo começar a regenerar, a oportunidade é **perdida**.
- Mercy pode disparar **até duas vezes** no mesmo alvo, mas a segunda tem duração muito mais curta.
- **Não dá Finisher** em Roller (Grineer), Osprey, Camera e Turret (Corpus). Entre os bosses, **só o The Sergeant** ainda aceita stealth attack.
- **Garuda** sobrescreve Front/Back finisher com animação de garra, o que **impede** Rumblejack e Rapier de aplicarem os procs forçados deles.
- O bônus de Affinity **reseta** se você matar um inimigo alertado ou for atacado por um. **Companion, Sentinel e Operator não resetam.**
- Turret, Security Camera, Sensor Bar, container e Sensor Regulator são **objetos**: não resetam o combo, mas também **não contam** como stealth kill.


## 📋 Tabelas de Referência — Stealth e Finishers


### Multiplicadores de Stealth Attack por tipo de melee

"Final" = multiplicador × 8 (arma maxada).

| Tipo de melee | Stealth | Final |
|---|---|---|
| **Sword** | **16x** | **128x** |
| **Exalted Blade** | **16x (8x + 8x)** | **128x** |
| Bayonet | 12x | 96x |
| Hammer | 12x (4x + 8x) | 96x |
| Heavy Blade | 12x (4x + 8x) | 96x |
| Heavy Scythe | 12x (4x + 8x) | 96x |
| Scythe | 12x (4x + 8x) | 96x |
| Rumblejack | 10,4x (0,4x + 10x) | 83,2x — proc forçado de **Electricity** no 1º hit |
| Blade and Whip · Claws · Dual Swords · Fist · Glaive · Gunblade · Machete · Nikana · Rapier · Sparring · Sword and Shield · Tonfa · Two-Handed Nikana · Warfan · Whip | 8x | 64x — Rapier tem proc forçado de **Slash** em cada hit |
| Dagger · Dual Daggers · Nunchaku · Polearm · Staff | 6x | 48x |
| Valkyr Talons | 4x | 32x |

### Multiplicadores de Ground Finisher (inimigo caído)

| Tipo de melee | Ground Finisher |
|---|---|
| **Valkyr Talons** | **54x (10x × 5 + 4x)** |
| **Fist** · **Sparring** | **30x (5x × 6 hits)** |
| Bayonet | 24x (12x × 2) |
| Tonfa | 20x (10x × 2) |
| Dual Daggers · Dual Swords | 16x (8x × 2) |
| Claws | 13,5x (2,5x × 5 + 1x) |
| Exalted Blade · Hammer · Heavy Blade · Heavy Scythe · Polearm · Scythe · Two-Handed Nikana | 12x |
| Dagger | 10x (5x × 2) |
| Glaive · Gunblade · Machete · Nikana · Nunchaku · Rapier · Staff · Sword · Warfan · Whip · Blade and Whip | 10x |
| Assault Saw | 9x |
| Sword and Shield | 8x |

### Multiplicadores de Front / Back / Universal Finisher

| Tipo de melee | Back | Front | Universal |
|---|---|---|---|
| **Hammer** | **24x (12x × 2)** | 12x | 12x |
| **Rapier** | **24x (8x × 3)** | 8x | 16x (8x × 2) | 
| Dual Daggers | 6x | 6x | **18x (1,8x + 4,2x + 6x + 6x)** |
| Scythe | 16x (8x × 2) | 8x | 8x |
| Valkyr Talons | 16x | 16x | 2,4x |
| Nikana | 8x | **16x (8x × 2)** | 8x |
| Assault Saw | 10x | 10x | 1x |
| Rumblejack | 10,4x | 10,4x | — |
| Heavy Blade | 8x (2x + 6x) | **2x** | **2x** |
| Heavy Scythe | 6x (2x + 4x) | **2x** | **2x** |
| Bayonet | 12x | **2x** | **2x** |
| Blade and Whip · Gunblade · Machete · Sword and Shield · Tonfa · Two-Handed Nikana · Whip | 8x | 8x | 16x (8x × 2) |
| Nunchaku | 8x | 8x | 12x (6x × 2) |
| Dual Swords | 8x | 8x (4x × 2) | 8x (4x × 2) |
| Exalted Blade · Sword | 8x | 8x (6x + 2x) | 8x |
| Claws | 8x | 8x | 2,4x |
| Fist · Sparring | 8x | 8x | 2,4x |
| Glaive | 8x | 8x | 8x |
| Dagger · Polearm · Staff · Warfan | 6x / 8x | 6x / 8x | igual |

> **Lição de build:** **Heavy Blade, Heavy Scythe e Bayonet caem para 2x** no Front e Universal Finisher. **Hammer** e **Rapier** são os reis do Back Finisher (24x). **Sword** e **Exalted Blade** são os reis do Stealth Attack (128x final).

### Estados de alerta

| Estado | Minimapa | O que o inimigo faz | Stealth Attack funciona? |
|---|---|---|---|
| **Não alertado** | Branco | Patrulha normal | ✅ Sim |
| **Alerta menor** | Âmbar | Fica atrás de cobertura ou patrulha com arma erguida, olha atrás de quinas, visão expandida, conversa com os outros. Disparado por tiro distante, corpo de aliado visto, ou arma silenciosa batendo no cenário | ❌ **Não** |
| **Combate total** | Vermelho | Persegue, chama reforço, aciona alarme no console (~1,5 s). Visão expandida de longe, inclusive para companions | ❌ Não |

> Matar o inimigo **antes** de ele terminar de usar o console (~1,5 s) impede o alarme. Se ele tomar dano suficiente, ele **aborta** o alarme e vira para atacar. Um alarme já soado pode ser **resetado** hackeando outro terminal.
>
> **Câmeras e Turrets** são um caso separado: ativar câmera ou atirar em turret **não** gera alerta nenhum para os outros inimigos, e o tiro do turret é **silencioso**. É por isso que o desafio de "10 stealth kills" pode ser feito até em missão com alarme tocando, destruindo câmeras.

### Inimigos que não aceitam Finisher

| Facção | Unidades |
|---|---|
| Grineer | Roller |
| Corpus | Ospreys, Cameras, Turrets |
| Bosses | Todos, **exceto The Sergeant**. Bosses não-humanoides (Phorid, Jackal) nunca aceitaram |

**MOA** antes não aceitava; hoje tem animação de stealth attack para **toda** classe de melee. **Warden** (missões de Rescue) toma **dano bônus** de stealth attack — essencial, porque eles têm vida altíssima e disparam a sequência de execução ao te verem.

### Armas silenciosas de fábrica

**Toda melee é silenciosa**, inclusive arma arremessada, o Deconstructor e o tiro de shotgun do [[armas/brancas/redeemer.md\|Redeemer]] (desde que o inimigo esteja a mais de 5 m).

| Categoria | Armas |
|---|---|
| **Silenciosas (primária)** | [[armas/primarias/attica.md\|Attica]] · [[armas/primarias/cernos.md\|Cernos]] · [[armas/primarias/daikyu.md\|Daikyu]] · Dread · Evensong · Paris / Mk1-Paris / [[armas/primarias/paris_prime.md\|Paris Prime]] · [[armas/primarias/rakta_cernos.md\|Rakta Cernos]] (exceto explosões de Blight) · Mutalist Cernos (mas a nuvem tóxica alerta na hora) · [[armas/primarias/zhuge.md\|Zhuge]] / [[armas/primarias/zhuge_prime.md\|Zhuge Prime]] · [[armas/primarias/baza.md\|Baza]] / [[armas/primarias/baza_prime.md\|Baza Prime]] · Nagantaka (exceto o Alt-Fire) |
| **Silenciosas (secundária)** | Ballistica (quando carregada), Ballistica Prime e Rakta Ballistica · Cantare · Fusilai · [[armas/secundarias/hikou.md\|Hikou]] / [[armas/secundarias/hikou_prime.md\|Hikou Prime]] · Kunai / Mk1-Kunai · Pox · [[armas/secundarias/spira.md\|Spira]] / [[armas/secundarias/spira_prime.md\|Spira Prime]] · Stinger · [[armas/secundarias/despair.md\|Despair]] |
| **Ruído reduzido** | Amprex, Flux Rifle, Glaxion, Ignis, Quanta, Synapse (25 m) · Fulmin (20 m, **silencioso em Semi-Auto**) · Opticor, Gammacor, Synoid Gammacor (10 m) |

> **Atenção:** Dread, Paris (e Prime) e Despair deixam de ser silenciosas **na forma Incarnon Genesis** — as explosões alertam. Ver [[mecanicas/incarnon.md\|Incarnon]].

**Mods de silenciamento:** **Suppress**, **Hush** e **Silent Battery** no rank máximo deixam qualquer pistola, rifle ou shotgun **completamente** silenciosa.

### Mercy (Parazon)

| Item | Detalhe |
|---|---|
| Como dispara | Inimigo enfraquecido ganha um **símbolo vermelho de Parazon** por **10 s** |
| Dano | **Vida residual do inimigo + 1** — ou seja, mata sempre |
| Independente de melee | O trigger e a animação não dependem da melee equipada; **não é preciso ter melee equipada** |
| Buff | Os mods equipados no **Parazon** definem o buff que você ganha ao executar o Mercy |
| Repetição | Até **2 vezes** no mesmo alvo; a segunda tem duração muito menor |
| Bloqueio | **Não dispara com escudo ativo**, mesmo abaixo do limiar. Escudo voltando a regenerar **cancela** a oportunidade |

### O que aumenta dano de Finisher

| Fonte | Detalhe |
|---|---|
| **Finishing Touch** | Mod de bônus direto de dano de Finisher |
| **Covert Lethality** | **Só em Daggers** |
| **Hunter's Bonesaw** | **Só em Ground Finishers** |
| **Radiant Finish** | Augment do Radial Blind do Excalibur |
| **Savage Silence** | Augment do Silence da Banshee — aplica **vulnerabilidade a Finisher Damage**, que é **multiplicativa** com os bônus aditivos |
| **Obex Incarnon Genesis** | Na forma Incarnon, cada hit de finisher dispara um ataque radial grande |
| Velocidade de ataque | (Primed) Fury, Gladiator Vice, Quickening, Berserker Fury, Arcane Strike aceleram a **animação** até o teto de 33% |

> Finishing Touch e Covert Lethality somam **aditivamente** entre si. Vulnerabilidade a Finisher Damage (Savage Silence) é **multiplicativa** por cima.


## 🛠️ Como Usar na Prática — Stealth e Finishers


| Objetivo | O que fazer |
|---|---|
| Dano máximo por Stealth Attack | **Sword** ou **Exalted Blade** maxados: multiplicador **16x** × bônus 8x = **128x** o dano da arma, já convertido em Finisher Damage (ignora armadura e escudo) |
| Dano máximo por Back Finisher | **Hammer** (24x) ou **Rapier** (24x em 3 hits, com proc forçado de Slash em cada) |
| Dano máximo por Ground Finisher | **Valkyr Talons** (54x), ou **Fist / Sparring** (30x) para arma normal |
| Evitar o erro de build | **Heavy Blade, Heavy Scythe e Bayonet caem para 2x** no Front e no Universal Finisher. Em build de finisher, a classe da arma importa mais que o dano base |
| Farmar Affinity | 5 abates furtivos seguidos = **+500% de Affinity**, com janela de 30 s renovada a cada abate. É a rota mais rápida de rankear arma nova |
| Não perder o combo de Affinity | Não mate inimigo **alertado** nem deixe um te acertar. Companion, Sentinel e Operator **não** quebram o combo — só você |
| Manter stealth contra Grineer e Corpus | Mate quem corre para o console em menos de **~1,5 s**, ou hackeie outro terminal para **resetar** o alarme |
| Aceitar que Infested é diferente | Infested e Corrupted são hive-mind: um alertado põe todos num raio enorme em alerta menor, e **não existe console para resetar**. Stealth contra eles é uma janela, não um estado |
| Ficar silencioso com arma de fogo | **Suppress / Hush / Silent Battery** maxados silenciam qualquer pistola, rifle ou shotgun. Sem isso, o raio de alerta é **50 m** |
| Matar Warden em Rescue | Warden toma **dano bônus** de stealth attack. Mate de primeira, antes de ele disparar a execução do refém |
| Mercy garantido | Mercy mata sempre (vida residual + 1), mas **nunca** dispara com escudo. Contra Corpus, derrube o escudo primeiro |
| Abrir inimigo alertado a Finisher | **Toda dagger simples** abre inimigos a finisher depois de um **Heavy Attack**. Também: Sonic Boom (Banshee), Teleport (Ash), Desiccation (Inaros), Radial Blind (Excalibur), Sling Stun (Naramon) |
| Multiplicar dano de finisher | **Savage Silence** (Banshee) é vulnerabilidade **multiplicativa**; Finishing Touch e Covert Lethality são **aditivos**. Empilhar os três é o pico |

**Mods que interagem:** Finishing Touch · Covert Lethality (só Dagger) · Hunter's Bonesaw (só Ground Finisher) · Suppress, Hush e Silent Battery (silenciamento) · [[mods/warframe/rush.md|Rush]] (fugir de sala antes do alarme se espalhar) · (Primed) Fury, Gladiator Vice, Quickening, Berserker Fury (aceleram a animação até o teto de 33%) · [[mods/armas/reaping_spiral.md|Reaping Spiral]] e stances em geral definem o combo que causa stagger.

**Frames que interagem:** [[warframes/regular/loki.md|Loki]] e [[warframes/regular/ivara.md|Ivara]] (invisibilidade, a base do stealth), [[warframes/regular/ash.md|Ash]] (Teleport executa Finisher ou Mercy com +125% a +200% de dano, e devolve 50% da energia se matar), [[warframes/regular/excalibur.md|Excalibur]] (Radial Blind + augment Radiant Finish), [[warframes/regular/banshee.md|Banshee]] (Sonic Boom derruba e remove 70% da armadura; Silence + **Savage Silence** dá vulnerabilidade multiplicativa a Finisher), [[warframes/regular/inaros.md|Inaros]] (Desiccation permite múltiplos finishers no mesmo alvo), [[warframes/regular/garuda.md|Garuda]] (sobrescreve Front/Back com garras e **quebra** os procs forçados de Rumblejack e Rapier), [[warframes/regular/valkyr.md|Valkyr]] (Talons: 54x em Ground Finisher, mas só 4x em Stealth).


## ⚠️ Erros Comuns — Stealth e Finishers


- **"Invisível é invisível."** Ruído alto alerta inimigos **de todas as direções**, mesmo contra um Tenno invisível. Invisibilidade esconde da **visão**, não do som.
- **"Alerta vermelho é o que bloqueia stealth attack."** O **âmbar** (alerta menor) já bloqueia.
- **"Qualquer melee serve para build de finisher."** A classe muda o multiplicador de 2x a 128x. Heavy Blade é 12x no Ground mas **2x** no Front/Universal.
- **"Covert Lethality mata qualquer coisa."** Hoje é um **bônus de dano de Finisher** e **só funciona em Dagger** — não é mais o one-shot universal antigo.
- **"Mods elementais somam normal no finisher."** Aplicam apenas **metade** do bônus antes da conversão para Finisher Damage.
- **"Pop-up amarelo quer dizer crítico."** Stealth attack **sempre** mostra amarelo, mesmo sem crítico.
- **"Mercy funciona em qualquer inimigo fraco."** **Nunca** com escudo ativo. Se o escudo voltar a regenerar, a janela de 10 s é perdida.
- **"Dá para recuperar stealth contra Infested."** Não. Infested e Corrupted são hive-mind e não têm console de alarme.
- **"Atirei na câmera, perdi o stealth."** Câmera e turret **não** alertam os outros inimigos, e o tiro do turret é silencioso.
- **"Meu Sentinel matou e quebrou meu combo de Affinity."** Companion, Sentinel e Operator **não** resetam o combo. Só você matando alertado, ou tomando dano de alertado.
- **"Testei no Simulacrum e o dano estava errado."** Stealth Damage Bonus **não funciona** no Simulacrum sem **Enemy AI** ativado.
- **"Velocidade de ataque da arma acelera o finisher."** A velocidade **base** não afeta. Só mods e arcanes de velocidade, e o teto é **33%** com +50% de velocidade.
- **"Finisher não é invulnerável."** É. O jogador fica **invulnerável durante toda a animação** — por isso finisher é também uma ferramenta defensiva.


## 🔗 Relacionados — Stealth e Finishers


- [[mecanicas/dano_e_status.md|Dano e Status]] — Finisher Damage é um tipo próprio que ignora armadura e escudo; Rapier força Slash e Rumblejack força Electricity nos finishers.
- [[mecanicas/critico.md|Crítico]] — Stealth Finisher **pode** criticar, e o multiplicador crítico entra **somado** ao Stealth Damage Bonus na fórmula.
- [[mecanicas/combo_counter.md|Combo Counter]] — Heavy Attack de dagger abre inimigo a finisher; Opening Slam (Naramon) dobra o ganho de Combo.
- [[mecanicas/operator_e_focus.md|Operator e Focus]] — **Sling Stun** (Naramon) abre inimigos a Finisher com +30% de dano de finisher, e **Killer's Rush** dá até +50% de crítico de melee ao iniciar um.
- [[mecanicas/parkour.md|Parkour]] — agachar reduz a silhueta; Wall Latch dá vantagem de altura, que os inimigos são ruins em checar.
- [[mecanicas/incarnon.md|Incarnon]] — Dread, Paris e Despair **perdem** o silêncio na forma Incarnon; o Obex Incarnon dispara ataque radial por hit de finisher.
- [[mecanicas/augments.md|Augments]] — Radiant Finish (Excalibur) e Savage Silence (Banshee) são os dois augments que mais multiplicam dano de finisher.
- [[mecanicas/steel_path.md|The Steel Path]] — a maioria dos inimigos do SP continua indefesa contra stealth, e o Mercy via Impact é uma rota de abate que ignora os 250% de vida.
- [[mecanicas/mastery_rank.md|Mastery Rank]] — o teste de MR 9 é o Stealth Test e o de MR 19 é o Stealth Rescue Test.
- [[mecanicas/nightwave.md|Nightwave]] — o Act "Executioner" pede 10 abates com Finisher (Ground Finisher **não** conta).
- [[missoes/tipos/spy.md|Spy]] e [[missoes/tipos/rescue.md|Rescue]] — os dois tipos onde stealth é obrigatório, e onde o Warden toma dano bônus de stealth attack.
- [[missoes/tipos/sanctuary_onslaught.md|Sanctuary Onslaught]] — o bônus de +500% de Affinity é o que torna stealth competitivo para rankear equipamento.

---
