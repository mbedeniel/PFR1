# Lancer le menu
import keyboard
from interaction import *
from time import sleep
from menu import *
from init import *
from navigation import *
from mouvement import *
import turtle as tl
from drawing import *

# Initialisation de la pièce
piece =  init_piece()
obstacle = init_obstable("obstacle2", (100, 20), "blue", "carree", 50)
piece['obstacles'].append(obstacle)
obstacle = init_obstable("obstacle3", (50, -60), "orange", "cercle", 50)
piece['obstacles'].append(obstacle)
obstacle = init_obstable("obstacle4", (-50, 20), "yellow", "carree", 50)
#piece['obstacles'].append(obstacle)
#recuperer les coins de la piece (coin_HG, coin_HD, coin_BD, coin_BG) (coin haut gauche, coin haut droit, coin bas droit, coin bas gauche)
coins = init_coins(piece)

trace_piece = tl.Turtle()
trace_piece.hideturtle()
#VITESSE LENTE
trace_piece.speed(5)
#tracer la pieces
tracer_piece(piece, trace_piece)

# Initialisation du curseur sous forme de robot
new_curseur = modif_curseur()

reception = {
    'mouvement': None,
    'distance_mouvement': None,
    'rotation': None,
    'angle_rotation': None,
}

while keyboard.is_pressed("esc") == False:
    if keyboard.is_pressed("up"):
        translantion(new_curseur, 20, piece)
    if keyboard.is_pressed("down"):
        translantion(new_curseur, -20, piece)
    if keyboard.is_pressed("left"):
        rotation(new_curseur, 5)
    if keyboard.is_pressed("right"):
        rotation(new_curseur, -5)
            
    
exit()
tl.done()

