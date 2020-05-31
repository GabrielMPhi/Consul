from game import Game
from tkinter import *

partie_joueur = Game()

# Créer une fenêtre
window = Tk()
window.title("Le Consul")
window.geometry("640x360")
window.config(bakcground='#000000')

# ajouter un premier texte
label_title = Label(window, text="Bienvenue, Consul", font=("Courrier", 40))
label_title.pack()

#créer un premier menu
menu_bar = Menu(window)
#créer un menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Quitter", command=partie_joueur)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(labe="Fichier", menu=file_menu)

#configurer notre fenêtre pour ajouter cette menu bar
window.config(menu=menu_bar)

window.mainloop()

