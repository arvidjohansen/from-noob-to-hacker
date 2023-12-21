from time import sleep



# Konverter til int
def validate_number(msg):
    num = 0
    while True:
        num = input(msg)
        try:
            return int(num)
        except ValueError:
            print(f'Feil! Kunne ikke konvertere verdien "{num}" til et tall!')

min = validate_number("Vennligst oppgi antall minutter: ")
sek = validate_number("Vennligst oppgi antall sekunder: ")
    
tot_sek = min * 60 + sek
print("Cooking ur egg for: " + str(tot_sek))





print("starting cooking egg....")