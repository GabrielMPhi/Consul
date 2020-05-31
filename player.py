from city import City
from partie import Partie

class Player:

    def __init__(self, name, age, health, wealth, influence, court, virtues, vices, traits):
        self.name = name
        self.age = age
        self.health = health
        self.wealth = wealth
        self.influence = influence
        self.court = court
        self.virtues = virtues
        self.vices = vices
        self.traits = traits
        print("Bienvenue au nouveau consul " + str(self.name) + ". " + "Tu as " + str(self.wealth) + " de richesse.")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, x):
        self.age = x
        return self.age

    def get_health(self):
        return self.health

    def get_wealth(self):
        return self.wealth

    def get_influence(self):
        return self.influence

    def augmenter_influence(self, quantite):
        self.influence = self.influence + quantite
        return self.influence

    def decision_player(self):
        decision_joueur = True
        while decision_joueur == True:
            print ((str(self.name)+ " doit faire un choix. \n1) Lire \n2) organiser une journée de marché. "))
            print("3) détourner des richesses.")
            print("4) explorer la cite")
            print("5) Quitter le jeu")
            choix = int(input("Quel est votre choix?"))
            if choix == 1:
                print ("Le Consul lit. Il augmente son influence. Celle-ci était de :" + str(self.influence))
                self.augmenter_influence(2)
                print ("Elle est maintenant de :" + str(self.influence))
                decision_joueur = False
            if choix == 2:
                decision_joueur = False
            if choix == 3:
                decision_joueur = False
            if choix == 4:
                decision_joueur = False
            if choix == 5:
                self.health = 0
                decision_joueur = False
            else:
                print (str(self.name) + " doit faire un choix.")

    def background_player(self):
        background_player = True
        while background_player == True:
            print("##### Le passé de " + str(self.name) + " #####")
            self.set_age(18)
            print("Dans sa jeunesse " + str(self.name) + "vivait calmement avec sa famille dans citeencoresansnom") # comment faire référence à la cité du joueur?
            ## ajouter un choix avec pour résultat l'anour d'un vice et d'une vertu dans le perso
            print("Cette grande cité était néanmoins gouverné d'une main de fer par un gouvernement autoritaire et despotique.")
            print("Dans sa jeunesse " + str(self.name) + " a rencontré biens des gens, mais une rencontre a été importante.")
            print("Il a finalement élu à la tête de la cité à cause de : ")
            background_choice = int(input("Choix :"))
            if background_choice == 1:
                print("Ok")
            background_joueur = False
            print("##### fin du passé #####")
        return self
