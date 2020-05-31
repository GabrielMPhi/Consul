import random
from partie import Partie
from tkinter import *


# Créer une fenêtre
window = Tk()
window.title("Le Consul")
window.geometry("640x360")
window.mainloop()


##### objet affichage, interface, etc... UI?
class UInterface:
    ##### s'occupe de l'affichage général ###
    #### afficher tel dialogue, ou un autre ####
    ### traiter la reponse du joueur
    pass

partie = Partie()
Partie()