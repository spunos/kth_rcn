from time import sleep
from random import random


class Attraktion:
    def __init__(self, namn, beskrivning, kapacitet, minlangd, utrop1, utrop2, utrop3, vantetid, haveri):
        self.namn = namn
        self.kapacitet = kapacitet
        self.beskrivning = beskrivning
        self.minlangd = minlangd
        self.utrop1 = utrop1
        self.utrop2 = utrop2
        self.utrop3 = utrop3
        self.vantetid = vantetid
        self.haveri = haveri

    def __str__(self):
        return self.namn.capitalize() + "! " + self.beskrivning

    def langd(self):
        if self.minlangd:
            return input("Är du minst " + str(self.minlangd) + "cm lång? (j/n)")
        else:
            return "j"

    def vanta(self):
        print("Väntetiden till " + self.namn + " är " + str(self.vantetid) + " minuter just nu.")
        for i in range(self.vantetid):
            if self.vantetid-i == 1:
                pluralis = ""
            else:
                pluralis = "er"
            print("..." + str(self.vantetid-i) + " minut" + pluralis + "...")
            sleep(1)
        print("Äntligen!")

    def starta(self):
        print("Alla " + str(self.kapacitet) + " personer är redo för " + self.namn + ".")
        sleep(1)
        print("Här kör vi!")
        for i in range(3):
            u = random()
            sleep(1)
            if u < 0.33:
                print(self.utrop1)
            elif u < 0.66:
                print(self.utrop2)
            else:
                print(self.utrop3)
        print("")
        sleep(1)
        if random() < 0.1:
            val.crash()
        else:
            print(self.namn.capitalize() + " stannar.")
            sleep(1)
            print("Det var kul! Vill du välja en annan attraktion nu?", end="\n\n")

    def crash(self):
        print("Åh nej! " + self.namn.capitalize() + " havererar!", end="\n\n")


def valkommen():
    print("Här är attraktionerna som du kan välja emellan:")
    for a in range(len(attraktioner)):
        beskrivning = attraktioner[a]
        print(str(a+1) + ": " + str(beskrivning))
    print("")
    val = input("Ange attraktionen som du vill uppleva: (1/2/3/4/5)")
    if not val or not val.isdigit() or int(val) < 1 or int(val) > 5:
        return False
    else:
        return attraktioner[int(val)-1]


attraktioner = []
pass
attraktioner.append(Attraktion("pariserhjulet", "Det är toppen på toppen!", 50, False,
                               "Jag kan se mitt hus!", "Ooh, så vackert", "Vad små alla människor ser ut.", 5,
                               "Hjulet kan inte stanna längre... du måste vänta på mekanikerna."))
attraktioner.append(Attraktion("berg-och dalbanan", "De högsta bergen och de djupaste dalarna!", 40, 140,
                               "Wheeee!!", "Aaaaah!!", "Whoaaaaa!!", 15,
                               ""))
attraktioner.append(Attraktion("lustiga huset", "Världens lustigaste hus!", 25, False,
                               "Hahaha!", "Hohoho!", "Hihihi!", 5,
                               ""))
attraktioner.append(Attraktion("radiobilarna", "Vi har även televisionbilar och blueraybilar!", 16, 130,
                               "Bam!", "Whap!", "Pow!", 0,
                               ""))
attraktioner.append(Attraktion("frittfall", "Fall fritt som en fågel! Eller en tegel.", 30, 140,
                               "Aaaahh!!", "Ihhhh!", "Jag är rädd!", 10,
                               ""))

print("☆.。.:*・°☆.。.:*・°☆.。.:*・°☆.。.:*・°☆")
print("         Välkommen på nöjesfältet!")
print("☆.。.:*・°☆.。.:*・°☆.。.:*・°☆.。.:*・°☆", end="\n\n")
val = valkommen()

while val:
    if (val.langd()[0].lower()) != "j":
        print("Tyvärr! Du får inte gå på " + val.namn + ". Vill du försöka igen?", end="\n\n")
    else:
        if val.vantetid != 0:
            val.vanta()
        val.starta()
    val = valkommen()

print("Hejdå!")
