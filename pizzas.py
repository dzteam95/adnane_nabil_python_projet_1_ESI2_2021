pizzas_list = []
menus = True
vegetarienne = "VEGETARIENNE"



class Pizza:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
        self.vegetarienne = vegetarienne
        self.ingredients = []

    def ajoutIngredients(self, list):
        self.ingredients = self.ingredients + list

    def list_pizza(self):
        print(f"PIZZA {self.nom} {self.prix}€ {self.vegetarienne}")
        for list in self.ingredients:
            print(list)

class Personnalisation_pizza(Pizza):
    def __init__(self, nom, prix):
        Pizza.__init__(self, nom, prix)

    def Addpers(self) :
     add = input(f'Ajoutez ingrédients personnalisé ( ou ENTER pour terminé) : ')
     if add == "":
        return ""
     else:
        self.ingredients = self.ingredients + [add]
        self.prix += 1.2
        return add


fromages = Pizza("4 fromages", 8.5)
fromages.ajoutIngredients(['brie', 'emmental', 'compté', 'parmesan'])

hawai = Pizza("hawai", 8.5)
hawai.ajoutIngredients(['tomate', 'ananas', 'oignons'])

saisons = Pizza("4 saisons", 11)
saisons.ajoutIngredients(['oeuf', 'emmental', 'tomate', 'jambon', 'olives'])

vegetarienne = Pizza("Végétarienne", 7.8)
vegetarienne.ajoutIngredients(['champignons', 'tomate', 'oignons', 'poivrons'])

pizzas_list = [fromages, hawai, saisons, vegetarienne]



for i in range(len(pizzas_list)):
    pizzas_list[i].list_pizza()
    print("\n")

while menus:
    act = int(input(f'terminer (2) ou créer une pizza personnalisée (1) ? : '))
    if(act == 1):
        w = True
    pizzaPers = Personnalisation_pizza("Pizza personnalisé 1", 7)
    while w:
        step = pizzaPers.Addpers()
        if(step == ''):
                 w = False
        pizzaPers.list_pizza()
        pizzas_list.append(pizzaPers)
    if(act == 3):
        print("fin")
        menus = False



