---
title: Modelo — Inventário do Jogador
tipo: protocolo
rag: false
tags: [protocolo, ia, inventario]
atualizado: 2026-10-13
agente: opus
---

# Modelo — Inventário do Jogador

> [!info] Para que serve
> Formato do documento que descreve **o que um jogador já tem e já fez**. O agente de IA cruza este documento com o vault (notas + `_MODELOS/dados/itens.json`) para recomendar a próxima ação. Toda referência a item usa o campo **`id`** do frontmatter do vault (ex.: `warframe:rhino`, `arma:braton_prime`, `mod:serration`, `arcane:arcane_energize`), que é estável e único.

## Esquema (YAML ou JSON — mesmos campos)

```yaml
jogador:
  nome: "Tenno123"
  plataforma: pc            # pc | ps | xbox | switch | mobile
  mastery_rank: 12
  plataina: 150             # opcional
  creditos: 2500000
  endo: 40000
  data_snapshot: 2026-10-13

progresso:
  quests_concluidas: [vors_prize, once_awake, the_archwing, natah, the_second_dream]   # nome do arquivo em missoes/jornadas/**
  juncoes_concluidas: [venus_junction, mercury_junction, mars_junction]               # nome do arquivo em missoes/juncoes/
  planetas_desbloqueados: [terra, venus, mercurio, marte]                              # nome do arquivo em locais/planetas/
  steel_path: false
  intrinsecos_railjack: {tactical: 0, piloting: 0, gunnery: 0, engineering: 0, command: 0}
  intrinsecos_drifter: {combat: 0, riding: 0, opportunity: 0, endurance: 0}
  focus_escolas: {}         # ex.: {zenurik: 30} pontos/nós
  sindicatos:               # nome do arquivo em mecanicas/sindicatos/
    ostron: {rank: 3, standing: 12000}
    steel_meridian: {rank: 1, standing: 4000}
  helminth: false

itens:                      # o que o jogador POSSUI (construído)
  - {id: warframe:excalibur, rank: 30, forma: 2, potato: true}
  - {id: arma:braton_prime, rank: 30, forma: 1, potato: true}
  - {id: companheiro:taxon, rank: 30}

pecas_e_blueprints:         # o que tem mas ainda não construiu
  - {id: warframe:rhino, partes: [blueprint, neuroptics, chassis]}   # falta systems
  - {id: arma:alternox, partes: [blueprint]}

mods:
  - {id: mod:serration, rank: 10}
  - {id: mod:vitality, rank: 6}
arcanes:
  - {id: arcane:arcane_energize, rank: 2, copias: 3}

recursos:                   # id: quantidade
  recurso:orokin_cell: 12
  recurso:neural_sensors: 3
  recurso:argon_crystal: 0

reliquias:
  - {nome: "Lith A1", refino: intact, quantidade: 4}

objetivos_do_jogador:       # texto livre — o que ele quer
  - "Quero farmar Saryn"
  - "Quero começar o Steel Path"
preferencias:
  estilo: [melee, solo]     # solo | squad | stealth | tank | nuke | suporte | melee
  tempo_por_sessao_min: 60
```

## Regras do documento

- `id` sempre igual ao do vault. Para descobrir: procurar `title`/`aliases` em `_MODELOS/dados/itens.json`.
- Item possuído = construído. Peças soltas ficam em `pecas_e_blueprints`.
- Campos ausentes = desconhecido (não "zero"). A IA deve perguntar ao jogador quando o dado for decisivo.
- `forma` e `potato` (Orokin Reactor/Catalyst) importam para recomendar builds.
