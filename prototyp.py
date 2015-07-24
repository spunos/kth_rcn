# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Titel: Djurparken
# Författare:
# Datum:

# Det här är ett program för att hålla koll på djur i en djurpark.
# Med programmet kan man söka efter djur, sortera djuren på olika sätt, och lägga till och ta bort djur.
# Alla ändringar sparas i en fil med namnet "djurpark.txt".

import operator

# Klass som beskriver ett djur:
class Djur():
    def __init__(self, namn, alder, art, kon):
        self.namn = namn        # djurets namn
        self.alder = alder      # djurets ålder
        self.art = art          # djurets art
        self.kon = kon          # djurets kön

    # Returnerar en sträng som beskriver djuret
    def __str__(self):
        return

# Klass som beskriver djurparken:
class Djurpark():
    # Läser in listan på alla djur i parken. Skapar listan om det inte redan finns.
    def __init__(self, filnamn):
        self.filnamn= filnamn

    # Skriver ut programmets valmenyn.
    def meny(self):
        # sortera
        # addera
        # ta bort
        return

    # Läser in och returnerar användarens val.
    def valja(self):
        print('''Vänligen välja om du vill:
              1. Se en lista på alla djur i parken
              2. Lägga till ett djur
              3. Ta bort ett djur''')
        val = input("")
        if val.lower() == "s":
            sortval = input('''Vill du sortera efter:
            1. Namn
            2. Art
            3. Ålder
            4. Kön''')
            stigande = input("På vilket sätt vill du sortera? (standard: fallande)")

        return val

    # Lägger till ett djur
    def addera(self):
        return

    # Tar bort ett djur
    def salja(self):
        return

    # Sorterar alla djur i parken efter namn, ålder, art eller kön.
    def sortera_namn(self, attribut, fallande):
        print("Sorterad efter " + attribut)
        print(sorted(djurlistan, operator.attrgetter(attribute), reverse=desc))

    # Sparar listan på alla djur i parken
    def spara(self, filename):
        return

# Huvudprogram

djurlistan = []
try:
    with open("djurpark.txt", 'r', encoding="utf-8") as file:
        for line in FILNAMN:
            djurlistan.append(line)
except:
    skapafil = input("Filen \"djurpark.txt\" finns inte än. Vill du skapa den?")
    if skapafil.lower()[0] == "j":
        with open("djurpark.txt", "w", encoding="utf-8") as file:
            file.write('Katt\n')
            file.write('Hund\n')
# val = "";
# while val:
#   djurpark.meny()
#   val = djurpark.valja()
#   # utför detta val

# djurpark.spara(FILNAMN)