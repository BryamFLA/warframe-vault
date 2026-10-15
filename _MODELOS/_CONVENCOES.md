---
title: Convenções Obrigatórias do Vault
tipo: protocolo
tags: [protocolo, agente, convencoes]
atualizado: 2026-09-09
---

# ⚖️ Convenções Obrigatórias — Leia antes de escrever qualquer coisa

> [!danger] Este documento é um contrato
> Qualquer agente (humano ou IA) que edite este vault segue estas regras **sem exceção**. Elas existem porque a primeira leva de arquivos foi escrita sem elas e resultou em **96% dos wikilinks quebrados** e dados de jogo não verificáveis.

---

## 1. Regra de ouro: dado errado é pior que dado ausente

Um vault vazio é honesto. Um vault preenchido com números inventados parece confiável e envenena toda consulta futura.

- **Todo dado numérico** (stats, custo de energia, quantidade de recurso, tempo de forja, valor de mod por rank, drop chance) **exige fonte verificada.**
- Fonte canônica: **https://wiki.warframe.com** (Warframe Wiki oficial). Fonte secundária aceita: warframe.com e patch notes oficiais da Digital Extremes.
- Não encontrou ou não conseguiu verificar? Escreva o campo assim:

```
| Vida | ⚠️ NÃO VERIFICADO |
```

- **Proibido** preencher número "de memória" sem marcar `⚠️`. Modelos de linguagem erram stats de Warframe com frequência alta — o jogo muda a cada update.

---

## 2. Nunca crie arquivos novos

O vault já tem **1181 arquivos** `.md` criados e estruturados. Sua tarefa é **preencher**, não expandir.

- Não crie arquivos.
- Não crie pastas.
- Não renomeie arquivos.
- Encontrou uma entidade que merece arquivo próprio e não existe? Anote na sua lista de pendências no fim da sessão — não crie.

---

## 3. Links: só para alvos que existem

Esta é a regra que mais foi violada. Antes de escrever qualquer `[[link]]`, confirme o caminho no campo `caminho` de `_MODELOS/dados/itens.json` (regenerar com `python3 _MODELOS/exportar_itens.py`) e, ao terminar, rode `python3 _MODELOS/gerador/links.py` (0 links quebrados).

**Formato obrigatório** — caminho completo a partir da raiz do vault, com extensão, com alias legível:

```
[[mecanicas/critico.md|Crítico]]
[[lore/faccoes/grineer.md|Grineer]]
[[warframes/primes/ash_prime.md|Ash Prime]]
```

**Se o alvo não existe no índice de caminhos, escreva em texto puro.** Sem colchetes. Nunca "chute" um caminho.

### Armadilhas reais já cometidas neste vault

| ❌ Errado | ✅ Certo |
|---|---|
| `[[sistemas/helminte.md]]` | `[[mecanicas/helminth.md\|Helminth]]` |
| `[[sistemas/caminho_de_aco.md]]` | `[[mecanicas/steel_path.md\|Steel Path]]` |
| `[[lore/faccoes/sindicatos/arbitros_de_hexis.md]]` | `[[mecanicas/sindicatos/arbiters_of_hexis.md\|Árbitros de Hexis]]` |
| `[[armas/nikana.md]]` | `[[armas/brancas/nikana.md\|Nikana]]` |
| `[[mods/fatal_teleport.md]]` | `[[mods/warframe/fatal_teleport.md\|Fatal Teleport]]` |
| `[[NPCs/cephalon_simaris.md]]` | `[[lore/personagens/cephalon_simaris.md\|Cephalon Simaris]]` |
| `[[cosmeticos/skins/koga_skin.md]]` | `[[cosmeticos/skins.md\|Skins]]` (não há um arquivo por skin) |
| `[[chefes]]` | `[[lore/_Lore _Indice.md\|Lore]]` |

### Idioma dos nomes de arquivo é misto — respeite o que existe

O vault não é consistente e **não cabe a você consertar isso**:

| Pasta | Idioma do nome de arquivo | Exemplo real |
|---|---|---|
| `mods/` | inglês | `blind_rage.md` |
| `mecanicas/` | inglês/misto | `steel_path.md`, `dano_e_status.md` |
| `mecanicas/sindicatos/` | inglês | `arbiters_of_hexis.md` |
| `missoes/tipos/` | inglês | `defense.md`, `capture.md` |
| `companheiros/` | inglês | `carrier_prime.md` |
| `lore/cronologia/` | português | `antiga_guerra.md` |
| `locais/planetas/` | português | `marte.md`, `plutao.md`, `neptuno.md` |
| `armas/`, `warframes/` | nome próprio | `acceltra.md`, `ash_prime.md` |

---

## 4. Estrutura: dados antes de prosa

O consumidor principal deste vault é um modelo de IA respondendo perguntas. Ele precisa de **tabela**, não de parágrafo.

- Toda informação que cabe em tabela **vai em tabela**.
- Prosa só onde ela é o conteúdo: lore, história, avaliação de uso.
- **Limite de prosa:** 3 parágrafos por seção narrativa. Se passou disso, você está enchendo linguiça.
- **Proibido:** frases decorativas sem conteúdo verificável. Exemplo real do que **não** fazer, extraído do vault: *"dando mais espaço estático confortável para posicionamentos do extermínio orgânico limpo no fluxo biológico da partida regular"* — isso não responde pergunta nenhuma.

---

## 5. YAML frontmatter

Preserve os campos que já existem no arquivo. Atualize `atualizado`. Adicione os campos de controle:

```yaml
---
title: Nome Exato Da Entidade
tipo: warframe            # warframe | arma | mod | recurso | missao | mecanica | local | lore | companheiro | cosmetico
tags: [tag1, tag2]
atualizado: 2026-09-09
verificado: true          # true = todo dado numérico conferido na wiki. false = há ⚠️ no corpo
agente: gemini            # gemini | gpt | opus — quem escreveu
---
```

---

## 6. Seção de fontes (obrigatória)

Todo arquivo preenchido termina com:

```markdown
## 📚 Fontes
- https://wiki.warframe.com/w/Ash — stats, habilidades, custos (consultado em 2026-09-09)
- https://wiki.warframe.com/w/Manic — drop de componentes (consultado em 2026-09-09)
```

Sem fonte, o arquivo não é considerado concluído.

---

## 7. Idioma e tom

- Português do Brasil.
- **Termos de jogo ficam em inglês** quando é assim que o jogador os usa: *Steel Path*, *Bleed*, *Finisher*, *Slash*, *Blade Storm*, *Riven*, *Forma*, *Helminth*. Não traduza nome de habilidade, mod, arma ou missão.
- Tom: direto e técnico. Nada de épico floreado.

---

## 8. Não invente estas coisas em hipótese alguma

| Item | Por quê |
|---|---|
| Drop chance / porcentagem de drop | Muda a cada update e é o dado mais alucinado |
| Localização exata de drop de componente | Mudou várias vezes (o `ash.md` atual está provavelmente errado por isso) |
| Valores de mod por rank | Precisam da tabela da wiki |
| Riven disposition | Muda a cada poucos meses |
| Preço em platina | Mercado flutuante — só cite faixa e diga que é estimativa |
| Data de release de item | Confira na wiki |

---

## 9. Fluxo de trabalho por arquivo

1. Abra o arquivo alvo e leia o que já existe (preserve o que estiver correto).
2. Abra o modelo da pasta correspondente em `_MODELOS/`.
3. Consulte a wiki para os dados. Uma aba por entidade.
4. Preencha seguindo o modelo, seção por seção.
5. Valide os links com `python3 _MODELOS/gerador/links.py`.
6. Preencha `## 📚 Fontes`.
7. Ajuste o YAML (`atualizado`, `verificado`, `agente`).

---

## 10. Escopo e conflito entre agentes

Cada agente trabalha **apenas** nas pastas atribuídas a ele. Não edite pasta de outro agente, nem os arquivos da raiz, nem `_MODELOS/`.

Commits: mensagem no formato `preenche(<pasta>): <n> arquivos — <agente>`. Commite a cada lote de 10–20 arquivos, nunca uma vez só no fim.

---

## 11. Lote e ritmo

- Trabalhe em **lotes de 10 a 20 arquivos**.
- Ao fim de cada lote, escreva no seu arquivo de status (`_MODELOS/_STATUS_<agente>.md`): o que preencheu, o que ficou `⚠️`, o que não achou fonte.
- Não tente preencher 100 arquivos numa tacada. A qualidade despenca e o custo de revisão vira maior que o de escrever.

---

## 12. Princípio da autossuficiência — duplicar é permitido e desejado

> [!important] Esta regra tem prioridade sobre economia de texto
> **Cada arquivo precisa responder sozinho as dúvidas sobre o seu elemento.** Se o leitor (humano ou IA) tem que abrir outro arquivo para entender uma frase, o dado está no lugar errado — ele também tem que estar aqui.

O vault antigo seguia "sem duplicação". **Essa regra foi revogada.** O motivo é prático: quando uma IA responde uma pergunta, ela costuma carregar um ou dois arquivos, não a árvore inteira. Um arquivo que só linka é um arquivo que não responde.

### Como aplicar

| Situação | ❌ Insuficiente | ✅ Correto |
|---|---|---|
| Build de warframe cita um mod | `Use [[mods/warframe/blind_rage.md\|Blind Rage]]` | `[[mods/warframe/blind_rage.md\|Blind Rage]] — +99% Força de Habilidade, −55% Eficiência (rank 10, drenagem 16, polaridade Madurai)` |
| Aquisição cita um recurso | `Custa 1 [[recursos/.../orokin_cell.md\|Célula Orokin]]` | `Custa 1 [[recursos/.../orokin_cell.md\|Célula Orokin]] — recurso raro, farmável em Saturno (Helene) e Ceres` |
| Arma cita combinação elemental | `Use Corrosivo contra Grineer` | `Use Corrosivo (Elétrico + Tóxico) contra Grineer — a armadura Ferrite deles toma +75% de Corrosivo` |
| Frame cita um tipo de missão | `Bom em [[missoes/tipos/survival.md\|Survival]]` | `Bom em [[missoes/tipos/survival.md\|Survival]] — a habilidade 4 mantém o mapa limpo entre as cápsulas de oxigênio, que caem a cada ~90s` |
| Lore cita um personagem | `Aliado de [[lore/personagens/ballas.md\|Ballas]]` | `Aliado de [[lore/personagens/ballas.md\|Ballas]], o Executor Orokin que traiu a Origem e criou os Warframes com a tecnologia Infestada` |

### O limite da duplicação

Duplique **o dado que a frase precisa**, não o arquivo inteiro.

- ✅ Repetir o efeito de um mod dentro de uma build.
- ✅ Repetir a fórmula do multiplicador crítico dentro do arquivo de uma arma.
- ✅ Repetir o resumo de uma facção dentro do arquivo de um chefe dela.
- ❌ Colar a tabela de ranks completa do mod dentro do arquivo do warframe.
- ❌ Copiar a lore inteira de uma facção dentro de cada arquivo de inimigo.

Regra prática: **uma a três linhas de contexto por referência.** Se passou disso, linke e resuma.

### Teste final de todo arquivo

Antes de considerar um arquivo pronto, faça esta pergunta:

> *"Se eu entregar só este arquivo para uma IA, ela consegue responder as dúvidas de um jogador sobre este elemento?"*

Se a resposta for "só se ela abrir mais três arquivos", o arquivo não está pronto.

Cada modelo em `_MODELOS/` termina com um bloco **❓ CHECKLIST** listando as perguntas concretas que aquele tipo de arquivo tem que responder. Use como critério de aceite.
