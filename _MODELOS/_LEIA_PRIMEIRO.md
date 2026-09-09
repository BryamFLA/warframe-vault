---
title: Operação Multiagente — Leia Primeiro
tipo: protocolo
tags: [protocolo, agente, indice]
atualizado: 2026-09-09
---

# 🎛️ Operação Multiagente — Painel

Três agentes de IA preenchendo o vault em paralelo, cada um em pastas disjuntas.

## Divisão

| Agente | Pastas | Arquivos | Prompt |
|---|---|---|---|
| **Gemini 3.1 Pro** (Antigravity) | `recursos/`, `missoes/`, `companheiros/` | 302 | [[_MODELOS/PROMPT_gemini.md\|PROMPT_gemini]] |
| **GPT 6 Astra** (Desktop, Work) | `warframes/` | 116 | [[_MODELOS/PROMPT_gpt.md\|PROMPT_gpt]] |
| **Claude Opus 5** | `mecanicas/`, `lore/` | 120 | [[_MODELOS/PROMPT_opus.md\|PROMPT_opus]] |
| _Rodada 2 — a definir_ | `armas/` (385), `mods/` (221), `cosmeticos/` (11), `locais/` (25) | 642 | — |

**Por que `armas/` e `mods/` ficam para a rodada 2:** dependem de `mecanicas/dano_e_status.md` e `mecanicas/critico.md` existirem, senão cada agente inventa a própria terminologia de dano.

## Documentos do sistema

| Arquivo | Para quê |
|---|---|
| [[_MODELOS/_CONVENCOES.md\|_CONVENCOES]] | O contrato. Todo agente lê antes de escrever. |
| [[_MODELOS/_INDICE_DE_CAMINHOS.md\|_INDICE_DE_CAMINHOS]] | Os 1181 caminhos reais. Fonte da verdade para links. |
| `MODELO_*.md` | Estrutura obrigatória, uma por tipo de pasta. |
| `_STATUS_*.md` | Registro de lote por agente. |

## Modelos por pasta

| Pasta do vault | Modelo |
|---|---|
| `warframes/` | `MODELO_warframe.md` |
| `armas/` | `MODELO_arma.md` |
| `mods/` | `MODELO_mod.md` |
| `recursos/` | `MODELO_recurso.md` |
| `missoes/` | `MODELO_missao.md` |
| `mecanicas/` | `MODELO_mecanica.md` |
| `locais/` | `MODELO_local.md` |
| `lore/` | `MODELO_lore.md` |
| `companheiros/` | `MODELO_companheiro.md` |
| `cosmeticos/` | `MODELO_cosmetico.md` |

## Protocolo de arranque

1. Cada agente lê `_CONVENCOES.md` + `_INDICE_DE_CAMINHOS.md` + o modelo da sua pasta.
2. Cada agente faz o **lote de calibração** (5–10 arquivos) e **para**.
3. Revisão humana de um arquivo por agente.
4. Aprovado, segue em lotes de 10–20 com commit por lote.

## Estado auditado em 2026-09-09

| Pasta | Arquivos | Situação |
|---|---|---|
| `warframes/` | 116 | 109 templates vazios · 3 fichas básicas · 4 "gold" com dados suspeitos |
| `armas/` | 385 | 380 só com frontmatter |
| `mods/` | 221 | 216 vazios |
| `recursos/` | 161 | 160 vazios |
| `missoes/` | 95 | 94 vazios |
| `lore/` | 73 | 55 vazios |
| `mecanicas/` | 47 | 45 vazios |
| `companheiros/` | 46 | praticamente todos vazios |
| `locais/` | 25 | parcialmente preenchidos |
| `cosmeticos/` | 11 | parcialmente preenchidos |

**Auditoria de links nos 3 arquivos "gold":** 202 wikilinks, **6 válidos**, 196 quebrados. Causa: caminhos inventados (`sistemas/`, `NPCs/`, `empresas/`, `cosmeticos/skins/`). É o defeito que este conjunto de documentos existe para não deixar acontecer de novo.
