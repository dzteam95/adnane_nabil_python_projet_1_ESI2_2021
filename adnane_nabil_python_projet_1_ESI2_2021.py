import random

player1 = {
    "name" : "",
    "health" : 50,
    "potions" : 3,
}

player2 = {
    "name" : "Quelqu'un",
    "health" : 50,
    "potions" : 0,
}

# game finished
def endGame(looser) :
    if looser==1 :
        print("Le joueur ", player2["name"], "à gagner")
    else :
        print("Le joueur ", player1["name"], "à gagner")

# potions
def takePotions() :
    heal = random.randint(15, 50)
    player1["health"] = player1["health"] + heal
    player1["potions"] = player1["potions"] - 1
    print("Vous récupérez ",heal, "de vie")


# computer attack
def attack() :
    dmg = random.randint(5, 10)
    player1["health"] = player1["health"] - dmg

    print("Vous subissez ",dmg, "de dégats")

    if player1["health"] <= 0 :
        endGame(1)

# player attack
def playerAttack() :
    dmg = random.randint(5, 15)
    player2["health"] = player2["health"] - dmg

    print("Vous infligez ",dmg, "de dégats")

    if player2["health"] <= 0 :
        endGame(2)

# player attack
def recap() :
    print("Vous avez ",player1["health"], "pts de vie et votre adversaire a", player2["health"], "pts de vie")

# player actions
def playerActions() :
    choice = 0
    while choice !=1 and choice !=2 :
        if player1["potions"]>0 :
            choice = int(input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "))
        else :
            choice = int(input("Vous n'avez plus de potions, vous ne pouvez qu'attaquer (1) : "))


    print(" ")

    if choice==1 :
        playerAttack()
    if choice==2 :
        takePotions()
    print(" ")

    if player1["health"]>0 and player2["health"]>0 :
        attack()
        print(" ")
        recap()


player1["name"] = input("Quel est votre nom ? ")

while player1["health"]>0 and player2["health"]>0 :
    playerActions()
