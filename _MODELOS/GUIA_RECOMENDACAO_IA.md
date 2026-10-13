---
title: Guia — Como a IA Recomenda Ações
tipo: protocolo
rag: false
tags: [protocolo, ia, recomendacao]
atualizado: 2026-10-13
agente: opus
---

# Guia — Como a IA Recomenda Ações

> [!info] Arquitetura em duas camadas
> **Busca (RAG)** encontra as notas certas do vault; **geração (LLM)** cruza essas notas com o **inventário do jogador** (`_MODELOS/MODELO_inventario_jogador.md`) e responde. Este guia diz como cada camada deve trabalhar.

## 1. Fontes que a IA tem

| Fonte | Uso |
|---|---|
| Notas `*.md` com `rag: true` | Conteúdo para responder (cortar por `## `; prefixar cada chunk com `title` + `aliases`). |
| `_MODELOS/dados/itens.json` | Tabela de todas as entidades (`id`, `tipo`, `mastery_rank`, `negociavel`, `vaultado`, `fonte_principal`, `uso_2025_rank`…). Use para filtros exatos sem RAG. Regenerar com `python3 _MODELOS/exportar_itens.py`. |
| `mecanicas/guia_de_progressao.md` | Fases do jogo e regras SE/ENTÃO de recomendação. |
| `mecanicas/rotinas_diarias_e_semanais.md` | O que fazer hoje/esta semana. |
| `mecanicas/popularidade_uso.md` + `uso_2025_rank` | Popularidade oficial (dados de uso da DE). |
| Inventário do jogador | Estado atual (o que tem, o que falta, MR, quests). |

## 2. Fluxo de resposta

1. **Classificar a pergunta:** onde conseguir · como construir · build · lore/história · o que fazer em <local> · o que fazer agora · comparação · mecânica.
2. **Resolver entidades:** casar nomes com `title`/`aliases` do `itens.json` (aceitar PT, EN e apelidos). Ex.: "criótico" → `recurso:cryotic`.
3. **Buscar:** para entidade conhecida, ler direto a nota (`caminho`) e as seções relevantes (`## 🌍 Onde Conseguir — X`, `## 🔨 …`, `## 🛠️ Build …`, `## 📖 História …`, `## ⭐ Avaliação Popular — X`). Para pergunta aberta, BM25/vetorial nos chunks.
4. **Cruzar com o inventário:** remover o que o jogador já tem; marcar requisitos que ele não cumpre (MR, quest, junction, rank de sindicato).
5. **Gerar:** resposta curta, passos numerados, citar a nota (caminho) de cada fato.

## 3. Regras de recomendação

- **Bloqueios primeiro:** se a ação exige quest/junction/MR/rank que o jogador não tem, recomende antes o desbloqueio (ver `mecanicas/guia_de_progressao.md`).
- **Aproveitar o que já tem:** peças em `pecas_e_blueprints` → recomendar terminar (falta peça X, farm em Y). Recursos suficientes → recomendar construir.
- **Gargalos:** compare `componentes` da receita (seção de forja da nota) com `recursos` do inventário; aponte o recurso que falta e onde farmar (seção Onde Conseguir do recurso).
- **Itens vaultados** (`vaultado: true`): sugerir Prime Resurgence/Varzia ou trade em vez de relíquias.
- **Negociáveis** (`negociavel`): se o farm é longo e o item é negociável, mencione a opção de comprar com Platinum.
- **Popularidade:** use `uso_2025_rank` como desempate ("muito usado pela comunidade"), nunca como única razão.
- **Builds:** use a seção de Build da nota; adapte aos mods que o jogador possui (`mods`). Se faltar um mod-chave, diga onde conseguir (`mods/**`).
- **Diário/semanal:** quando o jogador pergunta "o que faço hoje", combine rotinas (`rotinas_diarias_e_semanais.md`) com os objetivos dele.
- **Honestidade:** se a nota está `status: parcial` ou não cobre o ponto, diga que não tem certeza e indique a fonte da wiki (`fontes`).

## 4. Exemplos

**"Onde consigo o Excalibur?"** → entidade `warframe:excalibur` → seção Onde Conseguir. Se o inventário já tem Excalibur: "você já tem; quer o Excalibur Prime/Umbra?".

**"O que faço agora?" (MR 4, sem The Second Dream)** → guia de progressão: completar junctions até Netuno/Plutão, Natah → The Second Dream; recursos-gargalo dele; rotinas diárias.

**"Quero o Alternox"** → nota `armas/primarias/alternox.md` (passo a passo de forja + pesquisa no Dojo) + recursos do inventário → lista do que falta.

## 5. Manutenção

- Notas geradas dos módulos da wiki trazem `gerado_de: modulos-da-wiki`; os geradores estão em `_MODELOS/gerador/`.
- Avaliação de busca: `python3 _MODELOS/rag_eval.py 5` (8 perguntas-alvo) e `--geral` (amostra de entidades).
