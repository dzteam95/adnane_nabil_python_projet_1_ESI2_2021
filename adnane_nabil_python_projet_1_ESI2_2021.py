import random

me = {
        "nom" : "",
        "vies" : 50,
        "potions" : 3,
    }

machine = {
        "nom" : "machine",
        "vies" : 50,
        "potions" : 0,
}
me["name"] = input("saissaiez un pseudo")



def vie() :
        vie = random.randint(15, 50)
        me["vies"] = me["vies"] + vie

def potions() :
        vie = random.randint(5, 10)
        me["potions"] = me["potions"] - 1
        print("Vous récupérez ",vie, "de vie")

def donner() :
        dmg = random.randint(5, 10)
        me["vies"] = me["vies"] - dmg

        print("Vous subissez ",dmg, "de dégats")

        if me["vies"] <= 0 :
            finjeu(1)

def reçu() :
        dmg = random.randint(5, 15)
        machine["vies"] = machine["vies"] - dmg

        print("Vous infligez ",dmg, "de dégats")

        if machine["vies"] <= 0 :
            finjeu(2)

def recap() :
        print("Vous avez ",me["vies"], "pts de vie et votre adversaire a", machine["vies"], "pts de vie")

def actions() :
        menus = 0
        while menus !=1 and menus !=2 :
            if me["potions"]>0 :
                menus = int(input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "))
            else :
                menus = int(input("Vous n'avez plus de potions, vous ne pouvez qu'attaquer (1) : "))


        if menus==1 :
            potions()
        if menus==2 :
            reçu()

        if me["vies"]>0 and machine["vies"]>0 :
            donner()
            recap()

def finjeu(win) :
            if win==1 :
                print(machine["nom"], "win")
            else :
                print(me["nom"], "win")


while me["vies"]>0 and machine["vies"]>0 :
    actions()
