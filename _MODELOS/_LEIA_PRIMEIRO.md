---
title: Leia Primeiro — como este vault funciona
tipo: protocolo
rag: false
tags: [protocolo, agente, indice]
atualizado: 2026-10-14
---

# 🎛️ Leia Primeiro

Este vault é a **base de conhecimento (second brain) do Warframe** em PT-BR, usada pelo agente de IA local do repositório [`warframe-agent`](https://github.com/BryamFLA/warframe-agent) (busca RAG + `gemma4:12b` no Ollama). Qualquer IA ou pessoa que for **atualizar o vault** deve ler este arquivo e [[_MODELOS/_CONVENCOES.md|_CONVENCOES]] antes de escrever.

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `warframes/`, `armas/`, `companheiros/`, `mods/` (inclui `mods/arcanes/`), `recursos/`, `cosmeticos/` | Uma nota por item do jogo |
| `missoes/` | Tipos de missão, quests (`jornadas/`), junções, bounties |
| `locais/` | Planetas e mundos abertos (com listas completas "📦 Itens de …") |
| `mecanicas/` | Sistemas do jogo, sindicatos, eventos, guia de progressão, rotinas, glossário |
| `lore/` | Facções, personagens, chefes, cronologia |
| `_MODELOS/` | Infraestrutura (não é conteúdo do jogo; o agente não indexa esta pasta) |

Cada pasta tem um índice `_<Pasta> _Indice.md` gerado automaticamente.

## `_MODELOS/`

| Item | Para quê |
|---|---|
| `_CONVENCOES.md` + `MODELO_*.md` | Padrão obrigatório de escrita (frontmatter, headings com o nome da entidade, wikilinks com caminho completo) |
| `dados/itens.json` | Todas as entidades com `id`, `title`, `aliases`, `caminho`… **O agente usa este arquivo** para reconhecer nomes. Regenere sempre que criar/renomear notas |
| `exportar_itens.py` | Regenera `dados/itens.json` |
| `gerador/` | Scripts: `indices.py` (índices), `links.py` (valida/corrige links), `itens_local.py all --write` (listas de itens dos hubs), `gen_*`/`enrich_*` (notas a partir dos módulos de dados da wiki; baixe os dados com `fetch_all.py`) |
| `rag_core.py`, `rag_eval.py`, `rag_eval2.py` | Testes de busca. Rode depois de mudanças grandes: `python3 _MODELOS/rag_eval.py 5`, `python3 _MODELOS/rag_eval.py 5 --geral`, `python3 _MODELOS/rag_eval2.py` |
| `MODELO_inventario_jogador.md`, `GUIA_RECOMENDACAO_IA.md` | Formato do inventário do jogador e regras para a IA recomendar ações |
| `_PENDENCIAS.md`, `_STATUS_opus.md` | O que falta e histórico do trabalho |

## Rotina de atualização (ex.: novo update do jogo)

1. Escreva/atualize as notas seguindo `_CONVENCOES.md` e o `MODELO_*.md` da pasta; fonte: wiki.warframe.com.
2. `python3 _MODELOS/exportar_itens.py` → `python3 _MODELOS/gerador/indices.py` → `python3 _MODELOS/gerador/itens_local.py all --write`.
3. `python3 _MODELOS/gerador/links.py` (0 quebrados) e os testes de busca acima.
4. Commit e push. No Mac, reinicie a API do agente para ele reler o vault.
