---
title: Thermia Fractures
aliases: [Thermia Fractures]
tipo: mecanica
resumo: "Thermia Fractures — Evento de world state recorrente no Orb Vallis: selar fraturas térmicas com Coolant Canisters para acumular pontos (que nunca zeram entre edições) e Diluted Thermia, o item que invoca o Exploiter Orb."
status: completo
rag: true
tags: [mecanica, evento, thermia-fractures, orb-vallis, exploiter-orb, amalgam]
fontes: ["https://wiki.warframe.com/w/Thermia_Fractures"]
atualizado: 2026-10-07
verificado: true
agente: opus
---

# Thermia Fractures

> [!info] Em uma linha
> Evento de world state recorrente no Orb Vallis: selar fraturas térmicas com Coolant Canisters para acumular pontos (que **nunca zeram entre edições**) e **Diluted Thermia**, o item que invoca o Exploiter Orb.


## ⚙️ Como Funciona — Thermia Fractures


As Thermia Fractures acontecem quando **refrigerante Orokin é bombeado no solo rápido demais**, causando um surto térmico que faz a **Thermia** — um líquido parecido com magma — irromper na superfície. A causa é o **Nef Anyo**, que quer lucro rápido fazendo o **[[lore/chefes/exploiter_orb.md\|Exploiter Orb]]** colher a Thermia da superfície. Mas as fraturas ameaçam torrar **Fortuna** inteira.

> *"Aula rápida de geologia: fraturas térmicas é o que você ganha quando bombeia refrigerante demais no solo rápido demais. (…) Nef pode consertar isso, mas não vai. Em vez disso, ele tem aquele maldito Exploiter Orb colhendo a thermia da superfície por lucro rápido. Vá lá, localize uma fratura e eu te ajudo a selar."* — [[lore/personagens/eudico.md\|Eudico]]

É um **world state event recorrente**, que volta **a cada poucas semanas** no [[locais/open-worlds/fortuna.md\|Orb Vallis]].

O ciclo é: **matar um Coolant Raknoid** para pegar um **Coolant Canister** → achar uma fratura (identificável de longe pela fissura jorrando líquido laranja) → **interagir com o canister** para iniciar uma defesa estilo Mobile Defense → defender até selar.


## 🔢 Fórmulas e Números — Thermia Fractures


```
Selar 1 fratura com 1 canister = 3 minutos
  A UI mostra um contador até 100, não o tempo

Cada canister colocado enche o canister de Diluted Thermia em 25%
  Canister cheio (4 canisters) = 1 unidade de Diluted Thermia

Alimentar até 3 canisters ADICIONAIS nos primeiros 30 segundos:
  cada canister extra = +50 segundos (+25 unidades no contador)
  Com 4 canisters: 175 unidades = 5,5 minutos

PONTOS DO EVENTO:
  1 ponto por canister contribuído numa fratura selada com sucesso
  3 pontos ao completar um canister de Diluted Thermia
  → 1 canister cheio = 7 pontos (4 contribuídos + 3 de conclusão)

"Burp" da fratura: a cada 5 a 15 segundos
```

| Variável | Significado | Fonte do valor |
|---|---|---|
| 3 min / 100 | Tempo e contador de selagem com 1 canister | Wiki, Thermia Fractures § Sealing |
| 25% | Enchimento do canister de Diluted Thermia por canister colocado | Wiki, Thermia Fractures § Sealing |
| +50 s / +25 unidades | Ganho por canister extra, até 3, nos primeiros **30 s** | Wiki, Thermia Fractures § Sealing |
| 175 unidades / 5,5 min | Máximo com 4 canisters | Wiki, Thermia Fractures § Sealing |
| **7 pontos** | Valor de 1 canister cheio de Diluted Thermia | Wiki, Thermia Fractures § Rewards |
| 5 a 15 s | Intervalo entre Burps | Wiki, Thermia Fractures § Sealing |

**Tetos e limites conhecidos:**

- **Os pontos acumulam entre edições do evento.** O que você juntou numa rodada é carregado para as próximas — e **cada recompensa só pode ser obtida uma vez**.
- O número de fraturas seladas no resumo pós-missão é o **total do evento**, não o da sessão.
- **Resource Booster aumenta a Diluted Thermia recebida, mas NÃO aumenta os pontos.**
- O **Exploiter Orb pode ser invocado esteja o evento ativo ou não** — o único limite é quanta Diluted Thermia você tem. A invocação é no **Thermic Condenser**, no fundo do **Deck 12**.
- **Canisters parcialmente cheios podem ser misturados:** 2 canisters numa fratura geram um canister meio cheio, que somado a um vazio em outra fratura completa 1 unidade.


## 📋 Tabelas de Referência — Thermia Fractures


### Os Burps e o que cada um faz

| Burp | Efeito | Condição |
|---|---|---|
| **Eximus Burp** | Spawna unidades Eximus extras | Qualquer quantidade de canisters |
| **Nullifier Burp** | Cria brevemente uma **bolha de Nullifier** de **30 m** em volta da fratura | Qualquer quantidade |
| **Level Burp** | Aumenta o **Enemy Alert Level** atual | **Mínimo 2 canisters** |
| **Raknoid Burp** | Spawna **Thermic Raknoids** — parecidos com Mite Raknoids, mas com dano **Heat** | **Mínimo 2 canisters** |
| **Radiation Burp** | Rajada súbita e breve de **Radiation** em **30 m**, com **proc garantido de 4 segundos** | **Mínimo 3 canisters** |
| **Rage Burp** | **+25% de dano** nos inimigos próximos | **Mínimo 3 canisters** |

> Mais canisters = mais Diluted Thermia e mais pontos por fratura, **mas também Alert level inicial maior, Burps mais frequentes e Burps especiais**. É a troca central do evento.

### Recompensas por pontos acumulados

**Cada uma só pode ser obtida uma vez na vida da conta.**

| Pontos | Recompensa |
|---|---|
| **5** | Operation Buried Debts Emblem |
| **25** | **Amalgam Shotgun Barrage** e **Amalgam [[mods/armas/serration.md\|Serration]]** |
| **50** | **[[mods/armas/barrel_diffusion.md\|Amalgam Barrel Diffusion]]** e **Amalgam [[mods/armas/organ_shatter.md\|Organ Shatter]]** |
| **75** | Operation Buried Debts Sigil |
| **100** | **[[armas/primarias/opticor_vandal.md\|Opticor Vandal]]** — já com **slot de arma** e **Orokin Catalyst pré-instalado** |

> **Amalgam Barrel Diffusion** é especialmente relevante: é a **única fonte de mod de Dodge Speed do jogo**. Ver [[mecanicas/parkour.md\|Parkour]].

### Bônus de world state para todos os jogadores

| Status de controle | Bônus |
|---|---|
| **Out of Control** (menos de 35%) | Nenhum |
| **Intermittent Control** (35% ou mais) | **Credits dobrados** em todas as missões do Orb Vallis |

O bônus de Credits dobrados **dobra todos os Credits no fim da missão**, inclusive os dropados pelo **[[lore/chefes/profit_taker.md\|Profit-Taker Orb]]**. O status **Intermittent Control termina** quando o timer acaba **ou** quando os jogadores levam o controle a **Full Control**.

**O cálculo de Credits do Profit-Taker com o bônus ativo:**

| Configuração | Credits por run |
|---|---|
| Base | 250.000 |
| Com o bônus + Effigy do [[warframes/regular/chroma.md\|Chroma]] | **500.000** |
| + Credit Booster + Credit Blessing (True Master's Font) | **1.400.000** |
| + Loyal Retriever / Prosperous Retriever (o drop se divide em 5) | até **2.800.000** |


## 🛠️ Como Usar na Prática — Thermia Fractures


| Objetivo | O que fazer |
|---|---|
| **Pontos mais rápido** | **Sempre use 4 canisters** por fratura: 7 pontos por canister cheio contra 1 por fratura com canister único. Mas só funciona se os 3 extras entrarem nos **primeiros 30 segundos** |
| Aguentar 4 canisters | **Amesha** + **Benevolent Decoy**: pouse a Archwing colada no canister, empilhe o Decoy **3 vezes** e suba até os inimigos não conseguirem mirar nela. Desça e recaste quando acabar |
| Alternativa sem Archwing | **[[warframes/regular/vauban.md\|Vauban]]**: **Bastille** segurado lança um vórtice que arrasta tudo para o centro; combine com **Photon Strike** (ou qualquer dano em área) |
| Não desperdiçar canister parcial | **Pode misturar:** 2 canisters numa fratura dão um meio cheio, que com 1 vazio em outra fratura completa uma unidade |
| Invocar o Exploiter Orb | **Thermic Condenser**, no fundo do **Deck 12**. Funciona **mesmo fora do evento** — só precisa de Diluted Thermia na mão |
| Farmar Credits em massa | Enquanto o status estiver em **Intermittent Control (35%+)**, rode **Profit-Taker** com Chroma, Credit Booster e Blessing: até **2,8 milhões por run** |
| Booster certo | **Resource Booster** aumenta a **Diluted Thermia**, **não** os pontos. Para pontos, só contribuir canister |
| Prioridade de recompensa | **50 pontos** (Amalgam Barrel Diffusion, única fonte de Dodge Speed) e **100 pontos** ([[armas/primarias/opticor_vandal.md\|Opticor Vandal]] com slot e Catalyst inclusos) |
| Pegar o canister | **Coolant Raknoid**, que acompanha o Exploiter Orb patrulhando o **Temple of Profit** |
| Não perder progresso | Os pontos **nunca zeram** entre edições do evento — dá para fechar as 100 ao longo de várias rodadas |


## ⚠️ Erros Comuns — Thermia Fractures


- **"Perdi os pontos quando o evento acabou."** **Não.** Pontos **acumulam entre edições** e cada recompensa só é obtida uma vez.
- **"Resource Booster dá mais pontos."** Dá mais **Diluted Thermia**, **não** pontos.
- **"Mais canisters é sempre melhor."** Mais pontos, sim — mas também **Alert level maior, Burps mais frequentes** e os Burps especiais (Radiation e Rage só aparecem com 3+).
- **"Só posso invocar o Exploiter Orb durante o evento."** Dá para invocar **sempre**, no Thermic Condenser do Deck 12, desde que você tenha Diluted Thermia.
- **"Posso jogar canister extra a qualquer momento."** Só nos **primeiros 30 segundos** da selagem.
- **"Canister pela metade é desperdício."** Pode ser **misturado** com outro em outra fratura.
- **"O resumo mostra o que selei nessa sessão."** Mostra o **total do evento**.
- **"Full Control é o melhor estado."** Para **bônus de Credits**, não: o dobro de Credits vale no **Intermittent Control (35%+)**, e chegar a **Full Control encerra** o bônus.


## 🔗 Relacionados — Thermia Fractures


- [[mecanicas/eventos/_Eventos _Indice.md|Eventos]] — a visão geral dos eventos recorrentes.
- [[mecanicas/sindicatos/solaris_united.md|Solaris United]] e [[mecanicas/sindicatos/vox_solaris.md|Vox Solaris]] — os dois sindicatos do Orb Vallis; a Eudico é quem conduz o evento.
- [[mecanicas/parkour.md|Parkour]] — **Amalgam Barrel Diffusion** (50 pontos) é a **única fonte de mod de Dodge Speed** do jogo.
- [[mecanicas/dano_e_status.md|Dano e Status]] — Radiation Burp aplica proc garantido de 4 s; Thermic Raknoid faz dano Heat.
- [[mecanicas/forma_e_polaridades.md|Forma e Polaridades]] — o [[armas/primarias/opticor_vandal.md|Opticor Vandal]] de 100 pontos vem com **Orokin Catalyst pré-instalado**.
- [[mecanicas/mastery_rank.md|Mastery Rank]] — o Opticor Vandal conta Mastery como variante própria.
- [[mecanicas/steel_path.md|The Steel Path]] — o SP dá +100% de drop de recurso, o que ajuda na Diluted Thermia (não nos pontos).
- [[locais/open-worlds/fortuna.md|Fortuna / Orb Vallis]] — onde o evento acontece, incluindo o Temple of Profit e o Deck 12.
- [[lore/chefes/exploiter_orb.md|Exploiter Orb]] — invocado com Diluted Thermia no Thermic Condenser.
- [[lore/chefes/profit_taker.md|Profit-Taker Orb]] — o alvo do farm de Credits durante o bônus de Intermittent Control.
- [[lore/personagens/eudico.md|Eudico]] — quem narra e conduz o evento.
- [[warframes/regular/vauban.md|Vauban]] e [[warframes/regular/chroma.md|Chroma]] — os dois frames citados pela wiki como os mais úteis aqui.
- [[mods/armas/barrel_diffusion.md|Barrel Diffusion]] — a versão normal do mod cuja variante Amalgam é a recompensa de 50 pontos.

---
