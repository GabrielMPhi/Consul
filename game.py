import random
from player import Player
from city import City
from factions import Factions
from monde import Monde


class Game:
    monde1 = Monde()

    # Création de la cité
    liste_nom_cite = ["Laval", "Mordor", "Candiac", "Laval", "Londres", "Arcadia"]
    nom_cite = random.sample(liste_nom_cite, k=1)
    population_cite = random.randint(500, 1000)
    factions_cite = {
        "noblesse": Factions("noblesse", 100, 100, 100, 5),  # effectifs, richesse, force
        "clerge": Factions("clerge", 30, 30, 300, 5),
        "marchand": Factions("marchand", 50, 150, 50, 5),
        "plebe": Factions("plebe", 500, 2, 500, 5)
    }
    richesse_cite = random.randint(2, 10)
    ordre_cite = random.randint(2, 10)
    defence_city = random.randint(2, 10)
    cite_strenght = random.randint(2, 10)
    diplomacy_cite = []

    cite_joueur = City(nom_cite, population_cite, factions_cite, richesse_cite, ordre_cite, defence_city,
                       cite_strenght, diplomacy_cite)

    ## Création joueur 1
    richesse_joueur = random.randint(1, 5)

    joueur_nom = str(
        input("Quel est le nom du nouveau consul élu dans la cité de " + str(cite_joueur.get_name()) + "!"))
    player1 = Player(joueur_nom, 10, 10, richesse_joueur, 5, {}, ["Courage", "Humilité"], ["Avarice"], ["Grand"])



    fin_du_jeu = False
    tour = 1




    while fin_du_jeu == False:

        print("##### " + str(tour) + " #####")
        if tour == 1:
            player1.background_player()
        player1.age += 1
        print(player1.get_age())
        player1.decision_player()     #Pourquoi pas : Player.decision_player(player1)
        monde1.court_decision(player1)
        print("Fin du tour!")
        tour += 1
        if player1.health == 0:
            print("Fin du jeu.")
            fin_du_jeu = True
        if tour == 5:
            print("Fin du jeu.")
            fin_du_jeu = True