import turtle as tl

from drawing import *
from menu import menu
from init import*

# Initialisation des variables

# Initialisation de la pièce
piece =  init_piece()
#recuperer les coins de la piece (coin_HG, coin_HD, coin_BD, coin_BG) (coin haut gauche, coin haut droit, coin bas droit, coin bas gauche)
coins = init_coins(piece)
# Initialisation des ouvertures
ouverture = init_ouverture(coins['coin_HG'], 10,50)
ouverture2 = init_ouverture(coins['coin_HD'], 10,50)
ouverture3 = init_ouverture(coins['coin_BG'], 10,50)
ouverture4 = init_ouverture(coins['coin_BD'], 10,50)

# Initialisation des obstacles
obstacle = init_obstable('obstacle1', (-100,150), 'red', 'cercle', 25)
obstacle2 = init_obstable('obstacle2', (200, 100), 'green', 'carre', 50)
obstacle3 = init_obstable('obstacle3', (500, 100), 'orange', 'carre', 50)

#ajouter les ouvertures et les obstacles à la pièce
for ouv in [ouverture, ouverture2, ouverture3, ouverture4]:
    piece['ouvertures'].append(ouv)
for obs in [obstacle, obstacle2, obstacle3]:
    piece['obstacles'].append(obs)


# Initialisation de la fenêtre de jeu
trace_piece = tl.Turtle()
trace_piece.hideturtle()
#tracer la pieces
tracer_piece(piece, trace_piece)

# Initialisation du curseur sous forme de robot
new_curseur = modif_curseur()


# Lancer le menu
#menu(new_curseur)  # Remplacez par vos fonctions réelles

tl.done()
