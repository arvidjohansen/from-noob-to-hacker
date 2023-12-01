
# eggtimer
# Lag en alarm som kan brukes til å ta tiden på å koke egg
# Brukeren skal kunne sette tiden selv
# Spør brukeren først etter antall minutter
# også antall sekunder
# regn så ut totalt antall sekunder
# og skriv ut til terminalen, hvert sekund, 
# hvor mange sekunder som har gått eller
# hvor mange sekunder som gjenstår
# til egget er ferdig kokt
# skriv ut en hyggelig melding til brukeren når tiden
# er ute
import time
def get_number(melding):
    # henter input fra bruker
    # prøver å konvertere til int
    # returnerer en int hvis mulig
    # looper uendelig hvis brukeren ikke 
    # skriver inn en gyldig int verdi
    while True:
        try:
            num = int(input(melding))
            return num
        except ValueError:
            print("vennligst oppgi et tall, du skrev ikke et tall.")


minutter = get_number("Hvor mange minutter vil du koke egg?")
sekunder = get_number("Hvor mange sekunder vil du koke egg?")

# Hvordan kan vi være sikker på at brukeren faktisk har skrevet
# inn tall, og ikke tekst?

# TODO: faktisk telle ned

tot_sek = minutter * 60 + sekunder

print(f"Egget vil nå koke i totalt antall sek: {tot_sek}")

while tot_sek > 0: 
    print(f"{tot_sek} remaining...")
    tot_sek -= 1
    time.sleep(1)

print("egget er ferdigt! ALARM (spill av alarm)")
