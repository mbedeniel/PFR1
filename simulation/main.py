import turtle as tl

from simulation.plateform.drawing import *
from simulation.menu.menu import menu
from simulation.data.init import*
from simulation.navigation.navigation import entrer_robot1
from simulation.data.settings import *

#charger les parametres de configurations depuis le fichier settings.json
load_all_parameters()

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
obstacle2 = init_obstable('obstacle2', (200, 100), 'green', 'carree', 50)
obstacle3 = init_obstable('obstacle3', (100, -150), 'orange', 'carree', 50)

#ajouter les ouvertures et les obstacles à la pièce
for ouv in [ouverture, ouverture2, ouverture3, ouverture4]:
    piece['ouvertures'].append(ouv)
for obs in [obstacle, obstacle2, obstacle3]:
    piece['obstacles'].append(obs)
    #continue


# Initialisation de la fenêtre de jeu
trace_piece = tl.Turtle()
trace_piece.hideturtle()
#VITESSE LENTE
trace_piece.speed(1)
#tracer la pieces
tracer_piece(piece, trace_piece)

# Initialisation du curseur sous forme de robot
new_curseur = modif_curseur()
#new_curseur.speed(1)
#mettre le curseur a l exteieur de la piece
coins = piece['coins']
coin = coins['coin_BD']

##placer le curseur à l'extérieur de la pièce
new_curseur.up()
new_curseur.goto(coin[0]+75 , coin[1] - 30)
new_curseur.down()

#entrer le robot dans la piece
entrer_robot1(new_curseur, piece)
#new_curseur.down()
# Lancer le menu

menu(new_curseur, piece)
#mode_Vocal()
#fermer la fenetre
tl.bye()

#enregistrer tous les paramettres de configurations
save_all_parameters()

