---
title: Trading
tipo: mecanica
tags: [mecanica, trading, economia, platinum, dojo]
atualizado: 2026-10-04
verificado: true
agente: opus
---

# Trading

> [!info] Em uma linha
> Sistema de troca entre jogadores feito no Trading Post do Dojo ou no Maroo's Bazaar: exige Mastery Rank 2 e 2FA, cobra taxa em Credits de quem **recebe** o item, e é a única rota de Platinum dentro do jogo.

---

## 🧩 Como Funciona

Trading libera no **Mastery Rank 2** e exige **autenticação de dois fatores (2FA)** ativada no site oficial desde o Update 25.0 (2019-05-22). Acontece em dois lugares: no **Trading Post** de um [[mecanicas/cla_e_dojo.md\|Clan Dojo]] (você pode convidar não-membros do clã para o seu Dojo) ou no **Maroo's Bazaar**, o relay dedicado em Marte. Railjack não permite trade.

Cada parceiro oferece **até 6 itens** por transação — máximo de 12 itens no total. Cópias do mesmo item contam como itens separados. **Platinum é a exceção:** qualquer quantidade ocupa só **1** dos 6 slots. Só pode existir **uma oferta de Platinum na mesa por vez**: se o outro lado precisa oferecer Platinum em vez de você, basta você remover a sua oferta e ele colocar a dele, sem cancelar o trade.

**Quem paga a taxa é quem recebe o item**, e a taxa é sempre em **Credits**, nunca em Platinum. Sobre a taxa base do jogo incide ainda uma taxa de hub: **fixa de +10% no Maroo's Bazaar**, ou **variável de 0% a 100% no Dojo**, definida por qualquer membro do clã com privilégio de Treasurer em qualquer Trading Post.

---

## 🔢 Fórmulas e Números

```
Taxa total = taxa base do item x (1 + taxa de hub)

Taxa de hub:
  Maroo's Bazaar = +10% fixo
  Clan Dojo      = +0% a +100%, definida pelo Treasurer do clã

Trades por dia = Mastery Rank do jogador
  Founders: +2 trades por dia
  Reset: 00:00 GMT
  Subir de rank concede +1 trade imediatamente, mesmo com o limite já esgotado
```

| Variável | Significado | Fonte do valor |
|---|---|---|
| MR 2 | Requisito mínimo para tradear | Wiki, Trading § Prerequisites |
| 6 itens | Máximo por parceiro, por trade (12 no total) | Wiki, Trading § Limitations |
| +10% | Taxa de hub fixa do Maroo's Bazaar | Wiki, Trading § Tradables |
| 0–100% | Faixa de taxa de hub do Dojo | Wiki, Trading § Tradables |
| 500 Credits | Taxa por **unidade** de Platinum recebida | Wiki, Trading § Trade Tax |
| 00:00 GMT | Reset do limite diário de trades | Wiki, Trading § Limitations |

**Tetos e limites conhecidos:**

- O limite diário **não depende** de quantos itens foram trocados — 1 trade de 6 itens gasta o mesmo que 1 trade de 1 item. **Encha os 6 slots sempre.**
- **Riven Mod:** ambos os jogadores precisam ser **MR 8 ou mais**.
- **Arcane Legendary:** quem recebe precisa ser **MR 11 ou mais**. A lista: Arcane Barrier, Arcane Grace, Arcane Energize, Exodia Contagion, Exodia Epidemic, Arcane Reaper, Longbow Sharpshot, Secondary Shiver, Melee Crescendo, Melee Duplicate, Arcane Universal Fallout, Arcane Hot Shot, Arcane Escapist.
- **Blueprints e armas tradeáveis não podem ir para quem não atende o MR do item.**
- Arma ou Riven só é tradeável se o comprador **tiver slot livre** para receber.
- **Switch não troca Platinum** com outras plataformas, nem com Cross Save (política da Nintendo).
- Com exceção de adversários convertidos (Lich / Sister / Coda), **não há limite** de quantas vezes um item pode ser tradeado.

---

## 📋 Tabelas de Referência

### Taxa base por raridade — Mods e Void Relics

| Raridade / Tier | Taxa base |
|---|---|
| Common · Lith, Meso | 2.000 Credits |
| Uncommon · Neo, Axi | 4.000 Credits |
| Rare, Requiem, Riven | 8.000 Credits |
| Legendary, Archon · Eidolon Capture | 1.000.000 Credits |

### Taxa base — Arcane Enhancements (por rank)

| Rank | Common | Uncommon | Rare | Legendary |
|---|---|---|---|---|
| Unranked | 2.000 | 4.000 | 8.000 | 100.000 |
| 1 | 6.000 | 12.000 | 24.000 | 300.000 |
| 2 | 12.000 | 24.000 | 48.000 | 600.000 |
| 3 | 20.000 | 40.000 | 80.000 | 1.000.000 |
| 4 | 30.000 | 60.000 | 120.000 | 1.500.000 |
| 5 | 42.000 | 84.000 | 168.000 | 2.100.000 |

> A wiki registra um **bug conhecido**: Arcanes Common, Uncommon e Rare estão cobrando a taxa de **rank 0** independente do rank real.

### Taxa base — outros itens

| Tier | Taxa | Itens |
|---|---|---|
| **Rare** | 8.000 | Ayatan Stars · adversários tradeados na branch Crimson |
| **Uncommon** | 4.000 | Alguns blueprints de parte de Warframe Prime · Ayatan Sculptures **vazias** |
| **Uncommon (especial)** | 12.000 | Ayatan Sculpture **com estrelas encaixadas** |
| **Common** | 2.000 | Antitoxins · Arcane Helmets · Vay Hek Beacons · emotes de sindicato · peixes · Focus Lenses · Imprints · Keys tradeáveis · Mutalist Alad V Nav Coordinates · componentes de Necramech (danificados e reparados) · blueprints não-Prime · blueprints Prime (inclusive a maioria das partes de Warframe Prime) · partes Prime **não construídas** · Proof Fragments · Refined Gems · Scenes · armas tradeáveis e suas partes · partes de arma de Archwing de sindicato · armadura de sindicato · partes de Archwing do Tenno Lab |
| **Platinum** | 500 por unidade | — |

### O que pode e o que não pode ser tradeado

| ✅ Pode | ❌ Não pode |
|---|---|
| Mods em geral, Ancient Fusion Core, Legendary Core | Flawed Mods |
| Peças Prime **não construídas** e blueprints Prime | Peças Prime **já construídas** e Warframe Prime montado |
| Void Relics, Intact ou refinados, vaultados ou não | Umbra Mods |
| Arcanes, rankeados ou não | Primed Mods vindos do Daily Tribute |
| Focus Lenses e seus blueprints | Última cópia de mod com polaridade Precept ("Unique copies of abilities cannot be traded") |
| Keys tradeáveis (Baro Void-Signal, Corpus Void Key, Nihil's Oubliette, Grendel Locators, Mutalist Alad V Assassinate Key, Vay Hek Frequency Triangulator) | Platinum inicial da conta e Platinum de sorteio |
| Ayatan Sculptures (vazias ou com estrelas) e Ayatan Stars | Qualquer coisa fora da janela de trade (viola os termos de uso) |
| Sentinels e armas de Sentinel **de Baro Ki'Teer** | Outros companions |
| Armas de Archwing **de Baro Ki'Teer** | Outras armas de Archwing |
| Arcane Helmets e partes de armadura de sindicato | — |
| Imprints, peixes, Scenes, Refined Gems, Proof Fragments | — |
| Componentes de Necramech, danificados ou reparados | — |

### Armas tradeáveis como item inteiro

Precisam estar **completamente sem rank, sem Affinity**, sem Forma, sem Lens e sem Orokin Catalyst. **Mudança cosmética é permitida:** recolorir, aplicar skin, pôr Cosmetic Attachment, equipar mods normais e usar no **Simulacrum** (onde não se ganha Affinity) mantêm a arma tradeável. É assim que se testa uma arma de sindicato ou Prisma caro antes de decidir revender.

Variantes cujas **partes e blueprints** são tradeáveis: Prime, Carmine, Vandal e Wraith. Fora dessas, as exceções que também têm partes tradeáveis: Arum Spinosa, Athodai, Broken War (só partes), Epitaph, Orvius (só partes), Pathocyst, Pennant, Quellor, Shedu (só partes), Sheev, Sporothrix, Stahlta (só partes), Stropha (só partes), Velox (só partes), Wolf Sledge.

### Gíria do Trade Chat (vocabulário de comunidade)

| Sigla | Significado |
|---|---|
| WTB | Want to buy — quero comprar |
| WTS | Want to sell — quero vender |
| WTT(F) | Want to trade (for) — quero trocar (por) |
| WTH | Want to hire — quero contratar |
| PC | Price check — quanto vale |
| PMO | Private Message Offer — mande oferta no privado |
| OBO | Or best offer — ou melhor oferta |
| `100p` | 100 Platinum |
| `100p+` | 100 Platinum ou mais |
| blitzer | Jogador que corre a missão solo só para pegar a recompensa tradeável e passar ao cliente |

---

## 🛠️ Como Explorar na Prática

| Objetivo | O que fazer |
|---|---|
| Não desperdiçar trade | O limite diário conta **transações**, não itens. Junte sempre 6 itens por trade |
| Ganhar Platinum sem gastar dinheiro | Vender partes Prime não construídas, mods raros, Rivens e Arcanes. É a rota padrão da comunidade |
| Pagar menos taxa | Dojo com Treasurer que zerou a taxa = **0% de hub tax**, melhor que os +10% fixos do Maroo's Bazaar |
| Recuperar blueprint Prime que já comecei a construir | Cancele a construção na [[mecanicas/forja.md\|Forja]]: blueprint e recursos voltam (exceto Argon Crystal) e o blueprint volta a ser tradeável |
| Testar arma caríssima antes de revender | Compre pronta, recolore, aplique skin, mode e teste **só no Simulacrum**. Zero Affinity = continua tradeável |
| Subir o limite no mesmo dia | Passar no teste de MR dá **+1 trade imediato**, mesmo com o limite do dia já esgotado |
| Achar comprador | Trade Chat no jogo (ative em Opções > Chat > Trade Chat, e use filtros por canal), Maroo's Bazaar em Marte, ou os sites de trading board da comunidade |
| Evitar ban | Só tradeie **o que aparece na janela de trade**. Trade por favor, promessa, serviço ou vaga de clã não é protegido e é violação do EULA |

---

## ⚠️ Erros Comuns

- **"Quem vende paga a taxa."** Quem **recebe** o item paga. E sempre em **Credits**, nunca em Platinum.
- **"O limite diário é de itens."** É de **transações**. Trocar 1 item gasta o mesmo trade que trocar 6.
- **"Posso tradear meu Rhino Prime montado."** Não. Só **blueprint** Prime e **parte Prime não construída**. Peça construída e frame montado são intradeáveis.
- **"Posso tradear os 50 pl que ganhei de graça."** Não. Personal Platinum (inicial e de sorteio) é travado.
- **"Taxa de Dojo é sempre melhor."** Depende do clã: o Treasurer pode ter deixado em **+100%**, o dobro da taxa base — pior que os +10% do Maroo's.
- **"Riven é MR 2 como o resto."** Riven exige **MR 8 nos dois lados**. Arcane Legendary exige **MR 11** de quem recebe.
- **"Usei a arma no Simulacrum, perdi o trade."** Não perdeu: o Simulacrum não dá Affinity. O que trava é Affinity real, Forma, Lens ou Catalyst.
- **"Sculpture vazia e com estrela têm a mesma taxa."** Vazia: 4.000. Com estrelas encaixadas: **12.000**.
- **"Switch troca Platinum normalmente."** Não troca com outras plataformas, nem com Cross Save ativo.
- **"Dá para tradear o último mod de Precept."** Não. A última cópia de um mod com polaridade Precept é bloqueada.

---

## 🔗 Mecânicas Relacionadas

- [[mecanicas/platinum.md|Platinum]] — o que o trade serve para conseguir, e onde gastar depois.
- [[mecanicas/mastery_rank.md|Mastery Rank]] — MR 2 libera, o MR é o limite diário, MR 8 para Riven, MR 11 para Arcane Legendary.
- [[mecanicas/cla_e_dojo.md|Clã e Dojo]] — o Trading Post e a taxa de hub definida pelo Treasurer.
- [[mecanicas/forja.md|Forja]] — cancelar construção é o que devolve blueprint Prime ao estado tradeável.
- [[mecanicas/baro_ki_teer.md|Baro Ki'Teer]] — origem dos Sentinels, armas de Sentinel e armas de Archwing que **são** tradeáveis, e o destino dos Ducats.
- [[mecanicas/augments.md|Augments]] — mods de sindicato são tradeáveis e uma das mercadorias mais líquidas.
- [[mecanicas/operator_e_focus.md|Operator e Focus]] — Focus Lenses e seus blueprints são tradeáveis como Common.
- [[locais/planetas/marte.md|Marte]] — onde fica o Maroo's Bazaar.
- [[recursos/raridades/especial/riven_mod.md|Riven Mod]], [[recursos/raridades/especial/ayatan_sculpture.md|Ayatan Sculpture]], [[recursos/raridades/especial/orokin_ducats.md|Orokin Ducats]] — as três mercadorias de maior valor por slot de trade.

---

## 📚 Fontes
- https://wiki.warframe.com/w/Trading — pré-requisitos (MR 2 e 2FA), locais, limite de 6 itens, tabela completa de taxas por raridade e por rank de Arcane, taxas de hub, lista do que é e do que não é tradeável, requisitos de MR por tipo de item, regras de arma tradeável, gíria do Trade Chat (consultado em 2026-10-04)
- https://wiki.warframe.com/w/Platinum — regra de Personal Platinum e restrição da Nintendo Switch (consultado em 2026-10-04)
