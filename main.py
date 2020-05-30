import random
from tkinter import *


#window = Tk()
#window.title("Le Doge")
#window.geometry("640x360")
#window.mainloop()


class Cite:

    def __init__(self, name, wealth, order, defence, strength, diplomacy):
        self.name = name
        self.wealth = wealth
        self.order = order
        self.defence = defence
        self.strength = strength
        self.diplomacy = diplomacy

    def get_order(self):
        return self.order

    def get_wealth(self):
        return self.wealth

    def description_cite(self):
        print("La cité de" + str(self.name) + " est sympa.")


class Player:

    def __init__(self, name, health, wealth, influence, virtues, vices, traits):
        self.name = name
        self.health = health
        self.wealth = wealth
        self.influence = influence
        self.virtues = virtues
        self.vices = vices
        self.traits = traits
        print("Bienvenue au joueur" + str(self.name) + ". " + "Tu as " + str(self.wealth) + " de richesse.")

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_wealth(self):
        return self.wealth

    def get_influence(self):
        return self.influence

    def augmenter_influence(self, quantite):
        self.influence = self.influence + quantite
        return self.influence

    def decision_joueur(self):
        decision_joueur = True
        while decision_joueur == True:
            # print(self.name, "doit faire un choix") # Ici, ça ne fonctionne pas le self.name
            choix = int(input("doit faire un choix. \n 1) Lire \n 2) organiser une journée de marché "))
            if choix is not int:
                print ("Il doit y avoir un choix.")
            if choix == 1:
                print ("Le Doge lit. Il augmente son influence. Celle-ci était de :" + str(self.influence))
                self.augmenter_influence(2)
                print ("Elle est maintenant de :" + str(self.influence))
                decision_joueur = False
            if choix == 2:
                decision_joueur = False
        return self


## Création joueur 1
richesse_joueur = random.randint(1,5)

joueur_nom = str(input("Quel est le nom du Doge?"))
player1 = Player("Martin", 10, richesse_joueur, 5, ["Courage", "Humilité"], ["Avarice"], ["Grand"])

# Création de la cité

liste_nom_cite = ["Laval", "Mordor", "Candiac", "Laval"]

nom_cite = random.sample(liste_nom_cite, k=1)
richesse_cite = 10
ordre_cite = 10
defence_city = 10
cite_strenght = 10
diplomacy_cite = []

cite_joueur = Cite("Montrael", richesse_cite, ordre_cite, defence_city,cite_strenght , diplomacy_cite)

#### Structure du jeu #####

fin_du_jeu = False
tour = 1

while fin_du_jeu == False:
    print("##### " + str(tour) + " #####")
    player1.decision_joueur()
    #Player.decision_joueur(player1)
    print("Fin!")
    tour += 1
    if tour == 5:
        fin_du_jeu = True
