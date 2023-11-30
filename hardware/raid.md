---
marp: true
theme: gaia
class: invert
---



# RAID: Redundant Array of Independent Disks

## Innledning
RAID er en teknologi som brukes for å forbedre påliteligheten og ytelsen til datalagringssystemer ved å kombinere flere fysiske harddisker til en logisk enhet. Her er noen vanlige typer RAID:

---

## RAID 0 - Striping
- **Beskrivelse:** Distribuerer data jevnt over flere disker uten redundans.
- **Fordeler:** Økt ytelse, da data kan leses/skrives samtidig på flere disker.
- **Ulemper:** Ingen feiltoleranse; tap av en disk fører til tap av alle data.

---

## RAID 1 - Mirroring
- **Beskrivelse:** Dupliserer data på to eller flere disker.
- **Fordeler:** Høy pålitelighet, da data er tilgjengelig selv om en disk feiler.
- **Ulemper:** Lav utnyttelse av lagringskapasitet, da hver disk er en kopi av den andre.

---


## RAID 5 - Striping with Parity
- **Beskrivelse:** Distribuerer data over flere disker med en ekstra disk for paritetsinformasjon.
- **Fordeler:** God ytelse og en viss grad av feiltoleranse.
- **Ulemper:** Sårbar for feil hvis to disker svikter samtidig.

---


## RAID 6 - Striping with Dual Parity
- **Beskrivelse:** Ligner RAID 5, men bruker to paritetsdisker for bedre feiltoleranse.
- **Fordeler:** Høy feiltoleranse; kan håndtere to samtidige diskesvikt.
- **Ulemper:** Lavere skriveytelse på grunn av dobbel paritet.

---


## RAID 10 - Mirrored Stripes
- **Beskrivelse:** Kombinerer RAID 1 og RAID 0 ved å speile og stripe data.
- **Fordeler:** Kombinerer fordelene ved høy ytelse og feiltoleranse.
- **Ulemper:** Krever minst fire disker, og halvparten av kapasiteten er tilgjengelig.

---


## Konklusjon
Valget av RAID-nivå avhenger av behovene for ytelse, pålitelighet og tilgjengelig lagringskapasitet. Hver RAID-konfigurasjon har sine egne styrker og svakheter, og det er viktig å velge den som passer best for spesifikke bruksområder.
