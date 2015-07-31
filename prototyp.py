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
class Djur(object):
    def __init__(self, namn, alder, art, kon):
        self.namn = namn        # djurets namn
        self.alder = alder      # djurets ålder
        self.art = art          # djurets art
        self.kon = kon          # djurets kön

    # Returnerar en sträng som beskriver djuret
    def __str__(self):
        return "{:<8}{:<4}{:<10}{:<4}".format(self.namn, self.alder, self.art, self.kon)

    def __repr__(self):
        return str(self)

# Klass som beskriver djurparken:
class Djurpark():
    # Läser in listan på alla djur i parken. Skapar listan om det inte redan finns.
    def __init__(self, filnamn):
        self.filnamn= filnamn
        try:
            with open(self.filnamn, mode='r', encoding="utf-8") as fil:
                djurlistan = fil.read().split("\n")
        except:
            djurlistan = ["Anna, 25, papegoja, f", "Bosse, 4, katt, m", "Cesar, 7, hund, m", "Dora, 11, får, f",
                          "Emma, 9, katt, f", "Fido, 2, hund, m"]
            skapafil = input("Filen \"djurpark.txt\" finns inte än. Vill du skapa den? (j/n)")
            if skapafil.lower()[0] == "j":
                with open(self.filnamn, mode="w", encoding="utf-8") as fil:
                    fil.write("\n".join(djurlistan))
        self.djurobjekter = {}       # dictionary
        for djur in djurlistan:
            attributer = djur.split(",")
            namn = attributer[0]
            self.djurobjekter[namn] = Djur(attributer[0], int(attributer[1]), attributer[2], attributer[3])
        #self.djurlistan = list(self.djurobjekter.values())
        #print(self.djurlistan)

# Skriver ut programmets valmenyn.
    def meny(self):
        print("Välkommen till djurparken!")
        print('''Vänligen välja om du vill:
              1. Se en lista på alla djur i parken
              2. Lägga till ett djur
              3. Ta bort ett djur''')

    # Läser in och returnerar användarens val.
    def valja(self):
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
        sorterad = sorted(list(self.djurobjekter.values()), key=operator.attrgetter(attribut), reverse=fallande)
        for i in sorterad:
            print(i)

    # Sparar listan på alla djur i parken
    def spara(self):
        return

# Huvudprogram

def huvudprogram():
    djurpark = Djurpark("djurpark.txt")
    djurpark.sortera_namn("alder", True)
#    val = "0"
#    while val:
#        djurpark.meny()
#        val = djurpark.valja()
#        break
#    djurpark.spara()

huvudprogram()
