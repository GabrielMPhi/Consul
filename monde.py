import random

class Monde:
    def nommer_npc(self):
        #classe et méthode pour créer des noms aléatoires pour le npcs
        liste_de_noms_npc_random = ["Catherine", "Liene", "Sophie", "Anne-Sophie", "Frida", "Fridrika", "Martin", "Bernard", "Simon", "Gabriel"]
        choix_nom_npc = random.sample(liste_de_noms_npc_random, k=1)
        liste_de_noms_npc_random.remove(choix_nom_npc)
        selection = choix_nom_npc
        return selection

    def court_decision(self, joueur):
        seance_en_cours = True
        while seance_en_cours == True:
            print("----------------------")
            print("Séance du tour X")
            print("----------------------")
            print()
            seance_en_cours = False
        return joueur