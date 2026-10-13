# Gerador de arquivos a partir dos módulos da wiki

Usado em 2026-10-12 para preencher 483 stubs de `warframes/` e `armas/` e 37 de `companheiros/`.

1. Baixar para `$HOME`: `Module:{Blueprints,Warframes,Ability,Void,Research,Missions,DropTables,Resources,Companions}/data` e `Module:Weapons/data/{primary,secondary,melee,archwing,modular,misc,companion}` (salvos como `blueprints.lua`, `w_primary.lua` etc.) com `curl "https://wiki.warframe.com/index.php?title=Module:X/data&action=raw"`.
2. `python3 fetch_all.py` — baixa as páginas (cache em `~/gen/cache`), em lotes de até 170 s.
3. `python3 extract_acq.py` → `acq_en.json`; `tr_rules.py` traduz os padrões repetidos; o resto foi traduzido à mão em `acq_pt_manual.json`. Junção final: `acq_pt.json`.
4. `python3 run_gen.py` → grava em `~/gen/out/`; validar links e copiar para o vault.

Os arquivos gerados têm `status: parcial` e `gerado_de: modulos-da-wiki`. Não sobrescrever arquivos `completo` com o gerador.
