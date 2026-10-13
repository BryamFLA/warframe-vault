import re
LAB={'Tenno Lab':'Tenno Lab','Chem Lab':'Chem Lab','Bio Lab':'Bio Lab','Energy Lab':'Energy Lab','Orokin Lab':'Orokin Lab','Dagath':'Dagath'}
R=[
 (r"^(?:The )?([^.]+?)(?:'s|’s)? blueprint can be purchased from the Market\.$", r"O blueprint de \1 é vendido no **Mercado** (por créditos)."),
 (r"^(?:The )?([^.]+?)(?:'s|’s)? blueprint can be purchased from the Market\. Alternatively, it can be acquired from completing the ([^.]+?) Junction\.$", r"O blueprint de \1 é vendido no **Mercado**; também é recompensa da **Junção \2**."),
 (r"^(?:The )?([^.]+?)(?:'s|’s)? blueprint can be researched from the (\w+ Lab) in the [Dd]ojo\.$", r"O blueprint de \1 é pesquisado no **\2** do **Dojo do clã** (depois é replicado e forjado)."),
 (r"^(?:The )?([^.]+?)(?:'s|’s)? blueprints? can be researched from the (\w+ Lab) in the [Dd]ojo\.$", r"Os blueprints de \1 são pesquisados no **\2** do **Dojo do clã**."),
 (r"^A fully built ([^.]+?) can be purchased from the Market for ([\d,]+) Credits\.$", r"\1 é vendida **pronta** no **Mercado** por **\2 créditos**."),
 (r"^([^.]+?) is obtained by vanquishing a Kuva Lich who generated with one equipped\..*$", r"\1 é uma **arma Kuva**: só se obtém **derrotando (vanquish) um Kuva Lich** que tenha sido gerado com ela. Depois, ela aparece pronta na Foundry. A arma não é negociável, mas um Lich convertido com ela pode ser trocado no Crimson Branch do Dojo."),
 (r"^([^.]+?) is obtained by vanquishing a Sister who generated with one equipped\..*$", r"\1 é uma **arma Tenet**: só se obtém **derrotando (vanquish) uma Sister of Parvos** gerada com ela. Depois, ela aparece pronta na Foundry. Não é negociável, mas uma Sister convertida com ela pode ser trocada no Crimson Branch do Dojo."),
 (r"^The blueprint for the chamber can be bought from Rude Zuud for ([\d,]+) Standing at Rank 0 with Solaris United\.$", r"É um **Kitgun**: o blueprint do *chamber* (cano) é comprado do **Rude Zuud** em Fortuna por \1 de Standing (Rank 0 no Solaris United); grip e loader são comprados à parte."),
 (r"^The ([^.]+?) can be acquired by reaching the Rank of (\w+) with\s+([^.]+?), and spending ([\d,]+) Standing to purchase\..*$", r"\1 é uma **arma de Sindicato**: compre do **\3** com **\4 de Standing** ao chegar no rank **\2** do sindicato. Cópias sem rank, sem Forma e sem Catalyst são negociáveis."),
 (r"^Blueprints and components are a potential Invasion reward\..*Mastery Rank of at least (\d+).*$", r"Blueprint e peças são **recompensa de Invasão** (Invasions). As peças são negociáveis; é preciso **MR \1** para adquirir o blueprint."),
 (r"^The ([^.]+?) can (?:be potentially|potentially be|be) (?:sold|purchased) (?:by|from) Baro Ki'Teer.*? for ([\d,]+) Credits and ([\d,]+)\s+[\d,]*\.?.*$", r"\1 é vendida pelo **Baro Ki'Teer** (mercador do Void que visita os Relays a cada 2 semanas) por **\2 créditos e \3 Ducats**. O estoque dele muda a cada visita. Cópias sem rank são negociáveis."),
]
def tr(s):
    for pat,rep in R:
        m=re.match(pat,s,re.S)
        if m: return m.expand(rep)
    return None
R2=[
 (r"^A built ([^.]+?) (?:can be|is) (?:purchased|bought) from the Market for ([\d,]+) Credits\.$", r"\1 é vendida **pronta** no **Mercado** por **\2 créditos**."),
 (r"^Mk1-Braton be purchased from the Market for ([\d,]+) Credits\.$", r"MK1-Braton é vendida pronta no **Mercado** por **\1 créditos**."),
 (r"^The ([^.]+?)(?:'s)? blueprint can be purchased from the Market for ([\d,]+) Credits\.$", r"O blueprint de \1 é vendido no **Mercado** por **\2 créditos**."),
 (r"^Unlike most Prime gear, ([^.]+?) is permanently unvaulted.*$", r"Diferente da maioria dos itens Prime, \1 **nunca é vaultado (permanently unvaulted)**: as Relíquias saem dos **Abandoned Derelict Caches** em missões de Railjack Corpus."),
 (r"^([^.]+?) is purchased from Ergo Glast of\s+The Perrin Sequence in any Relay for (\d+)\s+Corrupted Holokey.*$", r"\1 é uma **arma Tenet** comprada do **Ergo Glast** (The Perrin Sequence) em qualquer Relay por **\2 Corrupted Holokeys**, obtidas em missões **Void Storm** de Railjack (não exige Standing). O bônus de dano progenitor da oferta muda a cada 4 dias."),
 (r"^The ([^.]+?)(?:'|'s)? blueprint can be bought from Nightwave Offerings for\s+(\d+)x Cred\.?$", r"O blueprint de \1 é comprado nas **Nightwave Offerings** por **\2 Nightwave Creds**."),
 (r"^The ([^.]+?)(?:'s)? blueprint can be (purchased from the Market|researched from the Tenno Lab in the dojo)\. Its parts can be purchased from various Syndicates\. All parts, except for the blueprint, are tradeable\.$", r"\1 é uma arma de **Archwing**: o blueprint vem do \2, e as peças são compradas de vários **Sindicatos**. As peças (não o blueprint) são negociáveis."),
 (r"^The ([^.]+?) is (?:potentially|periodically) sold by Baro Ki'Teer.*? for ([\d,]+) Credits and ([\d,]+)\s.*$", r"\1 é vendida pelo **Baro Ki'Teer** (mercador do Void que visita os Relays a cada 2 semanas) por **\2 créditos e \3 Ducats**. O estoque muda a cada visita. Cópias sem rank, sem Forma e sem Catalyst são negociáveis."),
 (r"^The weapon is periodically sold by Baro Ki'Teer.*? for ([\d,]+) Credits and ([\d,]+)\s.*$", r"Vendida periodicamente pelo **Baro Ki'Teer** por **\1 créditos e \2 Ducats**. O estoque muda a cada visita."),
 (r"^[^.]+? Relic Drops$", r""),
]
_old=tr
def tr(s):
    r=_old(s)
    if r is not None: return r
    for pat,rep in R2:
        m=re.match(pat,s,re.S)
        if m: return m.expand(rep).replace("researched from the Tenno Lab in the dojo","Tenno Lab do Dojo").replace("purchased from the Market","Mercado")
    return None
