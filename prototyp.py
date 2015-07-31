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
        return "{:<8}{:<4}{:<10}{:<1}".format(self.namn, self.alder, self.art, self.kon)

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
            self.djurobjekter[namn] = Djur(attributer[0], int(attributer[1]), attributer[2][1:], attributer[3][1:])

# Skriver ut programmets valmenyn.
    def meny(self):
        print('''Vänligen välja om du vill:
              1. Se en lista på alla djur i parken
              2. Lägga till ett djur
              3. Ta bort ett djur''')

    # Läser in och returnerar användarens val.
    def valja(self):
       val = input("")
       if val == "1":
            print('''Vill du sortera efter:
            1. Namn
            2. Art
            3. Ålder
            4. Kön''')
            sortval = input("")
            if sortval == "1":
                sortval = "namn"
            elif sortval == "2":
                sortval = "art"
            elif sortval == "3":
                sortval = "alder"
            elif sortval == "4":
                sortval = "kon"
            print("Vill du sortera stigande eller fallande? (standard: fallande)")
            sortsatt = input("")
            if not sortsatt or sortsatt.lower()[0] == "f":
                sortsatt = False
            else:
                sortsatt = True
            self.sortera(sortval,sortsatt)
       elif val == "2":
           self.addera()
       elif val == "3":
           self.salja()
       return val

    # Lägger till ett djur
    def addera(self):
        nyttnamn = input("Djurets namn?")
        nyalder = int(input("Djurets ålder?"))
        nyart = input("Djurets art?")
        nyttkon = input("Djurets kön?")
        self.djurobjekter[nyttnamn] = Djur(nyttnamn, int(nyalder), nyart, nyttkon)
        print("Följande djuret har tilläggats:")
        print(self.djurobjekter[nyttnamn])

    # Tar bort ett djur
    def salja(self):
        print("Vilket djur vill du ta bort?")
        rensa = input("")
        print("Följande djuret har sålts:\n" + str(self.djurobjekter.pop(rensa)))

    # Sorterar alla djur i parken efter namn, ålder, art eller kön.
    def sortera(self, attribut, fallande=False):
        print("Sorterad efter " + attribut)
        sorterad = sorted(list(self.djurobjekter.values()), key=operator.attrgetter(attribut), reverse=fallande)
        for i in sorterad:
            print(i)

    # Sparar listan på alla djur i parken
    def spara(self):
        print("Vill du spara filen?")
        spara = input("")
        if spara.lower()[0] == "j":
            djurlistan = list(self.djurobjekter.values())
            print(djurlistan)
            #with open(self.filnamn, mode="w", encoding="utf-8") as fil:
            #    fil.write("\n".join(listlist))

# Huvudprogram

def huvudprogram():
    djurpark = Djurpark("djurpark.txt")
    djurpark.sortera("namn")
    print("Välkommen till djurparken!")
    val = "0"
    while val:
        djurpark.meny()
        val = djurpark.valja()
    djurpark.spara()

huvudprogram()
