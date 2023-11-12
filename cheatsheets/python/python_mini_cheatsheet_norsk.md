---
marp: true
theme: gaia
class: invert
---



# Python Cheat Sheet

## Variabler og Datatyper

### Variabler
```python
navn = "Ola"
alder = 30
```

---


### Datatyper
```python
tekst = "Dette er en tekst"
heltall = 42
desimaltall = 3.14
sannhet = True
```

---

## Kontrollstrukturer

### Betingelser
```python
if alder > 18:
    print("Du er myndig")
else:
    print("Du er ikke myndig")
```

---

## Løkker (for-løkker)

Løkker brukes til å gjenta noe

### For å gjøre noe x antall ganger...
kan vi bruke for-løkker med `range()`
```python
for i in range(5): # skriver ut tallene fra 0 til 4
    print(i)
for i in range(1,6): # skriver ut tallene fra 1 til 5
    print(i)
```

---

Når man looper over elementer i en liste har ikke variabelnavnet noe å si for operasjonen av programmet
```py
frukter = ["eple", "banan", "appelsin"]
for frukt in frukter:
    print(frukt) # Skriver ut en frukt per linje
```
er det samme som 
```py
frukter = ["eple", "banan", "appelsin"]
for f in frukter:
    print(f) # Skriver ut en frukt per linje
```
>Den eneste forskjellen er variabelnavnet for hvert enkelt element som i eksempel #1 er `frukt` og i eksempel #2 er `f`

---

## While-løkker

![bg right](https://ih1.redbubble.net/image.3901584493.2224/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg)

Vi kan bruke while-løkker til å gjøre det samme
```py
i = 0
while i < 5: # skriver ut tallene fra 0 til 4
    print(i) 
    i += 1 # inkrementerer i (gjør større)
```

```py
i = 1
while i < 6: # skriver ut tallene fra 1 til 5
    print(i) 
    i += 1 # inkrementerer i (gjør større)
```

```py
frukter = ["eple", "banan", "appelsin"]
i = 0
while i < len(frukter): # skriver ut en frukt per linje
    print(frukter[i])
    i += 1
```


---
## Timer: Eggkoker

![bg right](https://ih1.redbubble.net/image.3901584493.2224/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg)

1. Kalkuler antall sekunder
1. For hvert antall sekunder
   - Print gjenværende tid
   - Reduser antall sek. med 1
   - Vent (sleep) 1 sekund

```py
from time import sleep

sekunder = 60 * 7 # 7 minutter * 60 sek = 420 sek

while sekunder > 0:
    sekunder -= 1 # reduserer sekunder med 1
    print(f"{sekunder} sekunder igjen... ")
    sleep(1)
print("Egget ditt er ferdig!")    
```


---

## Funksjoner

### Funksjon uten input parametre

```python
def si_hei():
    print("Hei")
si_hei()
```



### Funksjon med en input parameter

```python
def hilsen(navn):
    print("Hei, " + navn + "!")
hilsen("Kari")
```

---

### Funksjon uten input parametre med returverdi

```python
def si_hei():
    return "Hei"

svar = si_hei()
print(svar)
```

### Funksjon med en input parameter og returverdi

```python
def hilsen(navn):
    return "Hei, " + navn + "!"

svar = hilsen("Kari")
print(svar)
```

---



![bg fit](https://scaler.com/topics/images/dictionaries-vs-lists-in-python.webp)

---


## Samlinger (collections) av data

### Lister vs Dictionaries

* Både lister og dictionaries er samlinger av data, men har hver sitt bruksområde basert på hvordan du ønsker å organisere dataene. 
* En liste i Python er en ordnet samling av elementer.
* En dictionary er en uordnet samling av nøkkel-verdi-par, der hvert element har en unik nøkkel for å muliggjøre rask tilgang til data.

---

## Liste vs Dictionary eksempel

### Dictionary
```python
person = {"navn": "Per", "alder": 25}
print(person["navn"])  # Utskrift: Per
print(person["alder"])  # Utskrift: 25
```

### Liste

```python
frukter = ["eple", "banan", "appelsin"]
print(frukter[0])  # Utskrift: eple
print(frukter[1])  # Utskrift: banan
print(frukter[2])  # Utskrift: appelsin
```

---


### Ofte brukte metoder på liste-objektet

* `append(obj)` legger til et nytt objekt i listen

```python
frukter = ["eple", "banan", "appelsin"]
frukter.append("mango") # Legger mango til listen
print(frukter) # Utskrift: ['eple', 'banan', 'appelsin', 'mango']
```


* `extend(iterable)` legger til elementene fra et annet iterable (f.eks. liste eller tuple) til slutten av listen

```python
frukter = ["eple", "banan", "appelsin"]
nye_frukter = ["kiwi", "jordbær"]
frukter.extend(nye_frukter)
print(frukter) # Utskrift: ['eple', 'banan', 'appelsin', 'kiwi', 'jordbær']
```

---

* `insert(index, obj)` setter inn et objekt på en spesifikk indeks i listen

```python
frukter = ["eple", "banan", "appelsin"]
frukter.insert(1, "mango")
print(frukter) # Utskrift: ['eple', 'mango', 'banan', 'appelsin']
```

---

* `remove(obj)` fjerner det første forekomsten av et objekt i listen

```python
frukter = ["eple", "banan", "appelsin"]
frukter.remove("banan")
print(frukter) # Utskrift: ['eple', 'appelsin']
```

---

* `pop(index)` fjerner og returnerer elementet på den angitte indeksen. Hvis indeksen ikke er spesifisert, fjernes og returneres det siste elementet.

```python
frukter = ["eple", "banan", "appelsin"]
siste_frukt = frukter.pop()
print(siste_frukt) # Utskrift: appelsin
print(frukter) # Utskrift: ['eple', 'banan']
```

---

* `index(obj)` returnerer indeksen til det første forekomsten av et objekt i listen

```python
frukter = ["eple", "banan", "appelsin"]
index_banan = frukter.index("banan")
print(index_banan) # Utskrift: 1
```

---

* `count(obj)` returnerer antall ganger et objekt forekommer i listen

```python
tall = [1, 2, 3, 2, 4, 2, 5]
antall_toere = tall.count(2)
print(antall_toere) # Utskrift: 3
```

---

* `sort()` sorterer elementene i listen i stigende rekkefølge

```python
tall = [5, 2, 8, 1, 3]
tall.sort()
print(tall) # Utskrift: [1, 2, 3, 5, 8]
```

---

* `reverse()` reverserer rekkefølgen på elementene i listen

```python
frukter = ["eple", "banan", "appelsin"]
frukter.reverse()
print(frukter) # Utskrift: ['appelsin', 'banan', 'eple']
```

---

Dette gir en oversikt over noen av de mest brukte metodene på liste-objektet i Python. Du kan tilpasse eller legge til flere eksempler etter behov.



* `append(obj)` legger til et nytt objekt i listen

```python
frukter = ["eple", "banan", "appelsin"]
frukter.append("mango") # Legger mango til listen
print(frukter) # Utskrift: ['eple', 'banan', 'appelsin', 'mango']
```

---

### Dictionary
```python
person = {"navn": "Per", "alder": 25}
print(person["navn"])  # Utskrift: Per
```

---

## Filbehandling

### Lesing fra fil
```python
with open("fil.txt", "r") as fil:
    innhold = fil.read()
    print(innhold)
```

### Skriving til fil
```python
with open("ny_fil.txt", "w") as fil:
    fil.write("Dette er en ny fil.")
```

---

## Moduler og Biblioteker

```python
import math

radius = 5
omkrets = 2 * math.pi * radius
print("Omkrets:", omkrets)
```

---

## Forskjellige typer import

Eksempel: Vi ønsker å lage et program som simulerer et terningkast

<style scoped>
pre{
    font-size:90%;
}
</style>

```python
import random # Vi importerer hele biblioteket 
terningkast = random.randint(1,6) 
print(terningkast)
```

```python
from random import randint # Vi importerer bare funksjonen vi trenger
terningkast = randint(1,6)
print(terningkast)
```

```python
from random import * # Vi importerer alt direkte til vårt namespace
terningkast = randint(1,6)
print(terningkast)
```

---

## Feilhåndtering

```python
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Kan ikke dele på null.")
```

