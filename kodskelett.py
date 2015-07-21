# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Titel: Djurparken
# Författare:
# Datum:

# Det här är ett program för att hålla koll på djur i en djurpark.
# Med programmet kan man söka efter djur, sortera djuren och lägga till och ta bort djur.
# Alla ändringar sparas i en fil med namnet "djurpark.txt".

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
    def __init__(self, filnamn):
        self.filnamn= filnamn

    # Lägger till ett djur
    def addera(self):
        return

    # Tar bort ett djur
    def salja(self):
        return

    # Sorterar alla djur i parken efter namn (stigande/fallande)
    def sortera_namn(self, namn):
        return

    # Sorterar alla djur i parken efter alder (stigande/fallande)
    def sortera_alder(self, alder):
        return

    # Sorterar alla djur i parken efter art (stigande/fallande)
    def sortera_art(self, art):
        return

    # Sorterar alla djur i parken efter kön (stigande/fallande)
    def sortera_kon(self, kon):
        return

    # Sparar listan på alla djur i parken
    def spara(self, filename):
        return

# Huvudprogram

FILNAMN = "djurpark.txt"
djurpark = Djurpark(FILNAMN)

# val = "";
# while val:
#   djurpark.menu()
#   val = djurpark.val()
#   # utför detta val

djurpark.spara(FILNAMN)