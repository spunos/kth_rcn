# import random & time

# class theme park rides
# name
# wait time
# minimum height
# scariness factor
# max people
class Attraktion:
    def __init__(self, namn, kapacitet, minlangd, pirrfaktor, vantetid):
        self.namn = namn
        self.kapacitet = kapacitet
        self.minlangd = minlangd
        self.pirrfaktor = pirrfaktor
        self.vantetid = vantetid

    def __str__(self):
        return self.namn.capitalize() + "!"

# def describe attraction

    def langd(self):
        if self.minlangd:
            return input("Är du minst " + str(self.minlangd) + "cm lång? (j/n)")
        else:
            return "j"

# def wait

# def ride

# def crash

# def exit

# rides

def valkommen():
    print("☆.。.:*・°☆.。.:*・°☆.。.:*・°☆.。.:*・°☆")
    print("         Välkommen på nöjesfältet!")
    print("☆.。.:*・°☆.。.:*・°☆.。.:*・°☆.。.:*・°☆", end="\n\n")
    print("Här är attraktionerna som du kan välja emellan:")
    for a in range(len(attraktioner)):
        b = attraktioner[a]
        print(str(a) + ": " + str(b))

attraktioner = []
attraktioner.append(Attraktion("pariserhjulet",50,False,0,5))
attraktioner.append(Attraktion("berg-och dalbanan",40,140,5,15))
attraktioner.append(Attraktion("lustiga huset",25,False,3,5))
attraktioner.append(Attraktion("radiobilarna",16,130,2,0))
attraktioner.append(Attraktion("frittfall",30,140,5,10))

valkommen()
