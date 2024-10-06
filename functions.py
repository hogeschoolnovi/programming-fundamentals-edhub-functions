# ==========================================
# Voorbeeld Opdracht
# Schrijf een functie die de tekst “Hello, World!” print. Roep vervolgens de functie aan.
# ==========================================

def print_hello_world():
    print('Hello, World!')

print_hello_world()  # Uitkomst: Hello, World!


# ==========================================
# Opdracht 1:
# Print de tafel van 5 met behulp van een for-loop en een functie (genaamd 'print_tafel_regel').
# De factor en for-loop zijn al gegeven. Schrijf de functie om de regel van de tafel te printen.
#
# Verwachte uitkomst:
# 1  x  5  =  5
# 2  x  5  =  10
# 3  x  5  =  15 enz.
# ==========================================

factor = 5


def print_tafel_regel(i, factor):
    print(i, ' x ', factor, ' = ', i * factor)


for i in range(1, 11):
    print_tafel_regel(i, factor)





# ==========================================
# Opdracht 2:
# Maak een dobbelsteen met de volgende deelopdrachten.
#
# Opdracht 2a:
# Maak met behulp van de bibliotheek 'random' (library) een functie die een willekeurig getal tussen 1 en 6 genereert.
# Zorg dat de functie twee argumenten ontvangt, namelijk 'min' en 'max'. Voor het minimum (1) en maximum (6).
# Voer de functie 10 keer uit (met een for-loop). Als het willekeurige getal is gegenereert print je het getal.
#
# Opdracht 2b;
# Maak een variabele aan 'aantal_keer_zes' en zet deze op 0. Schrijf een functie die aan het eind print hoe vaak er een 6 is gegooid.
# De variabele 'aantal_keer_zes' moet in de print statement worden gebruikt.
#
# Verwachte uitkomst (voorbeeld):
# 3 7 2 6 1 4 5 6 2 1
# Er is 2 keer een 6 gegooid
# ==========================================

import random  # importeert de library 'random'. Voor de duidelijkheid van de opdracht staat deze import hier. Maar die hoort bovenaan het bestand te staan.

aantal_keer_zes = 0


def genereer_willekeurig_getal(min, max):
    return random.randrange(min, max)


def controleer_op_zes(willekeurig_getal):
    if willekeurig_getal == 6:
        return True
    else:
        return False


for worp in range(10):
    willekeurig_getal = genereer_willekeurig_getal(1, 7)
    print(willekeurig_getal, end=' ')
    if controleer_op_zes(willekeurig_getal):
        aantal_keer_zes += 1

print('\nEr is', aantal_keer_zes, 'keer een 6 gegooid')  # Uitkomst (voorbeeld): Er is 2 keer een 6 gegooid


# ==========================================
# Opdracht 3:
# Omrekenen van Fahrenheit naar Celsius.
#
# Schrijf een functie die de temperatuur in Fahrenheit ontvangt als argument en deze omrekent naar Celsius.
# De formule voor de conversie is als volgt: celsius = (fahrenheit - 32) * 5/9
# Schrijf ook een functie die de temperatuur afrond in hele getallen.
# print de temperatuur in Celsius afgerond op hele getallen.
#
# Verwachte uitkomst:
# 18
# 24
# 40
# ==========================================

temp_in_fahr_stockholm = 65
temp_in_fahr_sydney = 75
temp_in_fahr_cairo = 104


def fahrenheit_naar_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def rond_af_op_hele_getallen(celsius):
    return round(celsius)


print(rond_af_op_hele_getallen(fahrenheit_naar_celsius(temp_in_fahr_stockholm)))  # Uitkomst: 18
print(rond_af_op_hele_getallen(fahrenheit_naar_celsius(temp_in_fahr_sydney)))  # Uitkomst: 24
print(rond_af_op_hele_getallen(fahrenheit_naar_celsius(temp_in_fahr_cairo)))  # Uitkomst: 40
