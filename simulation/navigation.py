#CE FINCHIER N EST PAS ENCORE COMPLET. IL RESTE DU TRAVAIL A FAIRE.
"""
EN GROS, ICI J'ESSAIE D IMPLEMENTER LA NAVIGATION AUTOMATIQUE DU ROBOT 
LUI DONNER LA FACULTE DE CONTOURNER LES OBSTACLES POUR ATTEINDRE SA DESTINATION
AUTREMENT DIT, IL DOIT SE DEPLACER DANS LA PIECE SANS PERCUTER (traverser) UN OBSTACLE

"""

import turtle as tl
from math import sqrt, atan2, degrees 

from drawing import *  # Assure-toi que cette fonction contient les définitions nécessaires
from init import init_piece, init_obstable, init_coins  # Tu as ces fonctions pour initialiser la pièce et les obstacles

## les  fonction a venir sont des fonctions qui permettent de  positionner le robot dans la piece
"""
En d autre terme, si le robot est à l'extérieur de la pièce, ces fonctions permettent de le faire entrer dans la pièce en passant par l ouverture le plus proche de lui.
expliquons un peu le fonctionnement de ces fonctions:
1. On vérifie si le robot est déjà dans la pièce
2. On récupère les ouvertures de la pièce
3. On trouve l'ouverture la plus proche du robot
4. s aligne sur l axe x ou y par rapport au centre de l ouverture la plus proche
5. on se dirige vers le centre de l ouverture
6. on entre dans la pièce
"""
def aligner_sur_x(curseur, x):
    """
    Aligne le curseur sur l'axe X à la position donnée `x`.
    """
    new_coordonee = (x, curseur.ycor())
    curseur.goto(new_coordonee)
def aligner_sur_y(curseur, y):
    """
    Aligne le curseur sur l'axe Y à la position donnée `y`.
    """
    new_coordonee = (curseur.xcor(), y)
    curseur.goto(new_coordonee)

def entrer_robot1(curseur, piece):
    delta = 30
 # Vérifier si le robot est déjà dans la pièce
    if est_dans_piece(curseur.position(), piece):
        print("Le robot est déjà à l'intérieur de la pièce.")
        return

    # Récupérer les ouvertures de la pièce
    ouvertures = piece.get('ouvertures', [])
    if not ouvertures:
        print("Erreur : La pièce n'a pas d'ouvertures.")
        return

    # Trouver l'ouverture la plus proche du robot
    robot_pos = curseur.position()
    ouverture_proche = min(ouvertures, key=lambda ouverture: get_distance(curseur, ouverture['coin_droite']))

    # Identifier l'orientation de l'ouverture
    coin_droite = ouverture_proche['coin_droite']
    coins = init_coins(piece)

    if coin_droite == coins['coin_BG']:
        #OKKKKKKKKKKKKKKK
        # aligner le curseur sur l axe x et entrer dans la piece
        centre = (coin_droite[0] + delta , coin_droite[1] + int(ouverture_proche['distance_coin'] / 2))
        #verifier si x_curseur < coin_droite[0] 
        if robot_pos[0] < coin_droite[0]:
            aligner_sur_y(curseur, centre[1])
            curseur.setheading( curseur.towards(centre))
            curseur.goto(centre)
        else:
            aligner_sur_x(curseur, centre[0]*1.5)
            aligner_sur_y(curseur, centre[1])
            curseur.setheading( curseur.towards(centre))
            curseur.goto(centre)
    elif coin_droite == coins['coin_HD']:
        # aligner le curseur sur l axe y et entrer dans la piece
        centre = (coin_droite[0]- delta, coin_droite[1] - int(ouverture_proche['distance_coin'] / 2))
        #verifier si X_curseur > coin_droite[0]
        if robot_pos[0] > coin_droite[0]:
            aligner_sur_y(curseur, centre[1])
            curseur.setheading( curseur.towards(centre))
            curseur.goto(centre)
        else:
            aligner_sur_x(curseur, centre[0]*1.5)
            aligner_sur_y(curseur, centre[1])
            curseur.setheading( curseur.towards(centre))
            curseur.goto(centre)
    elif coin_droite == coins['coin_BD']:
        #OKKKKKKKKKK
        # aligner le curseur sur l axe x et entrer dans la piece
        centre = (coin_droite[0] - int(ouverture_proche['distance_coin'] / 2), coin_droite[1] + delta)
        #verifier si y_curseur < coin_droite[1]
        if robot_pos[1] < coin_droite[1]:
            aligner_sur_x(curseur, centre[0])
            curseur.setheading( curseur.towards(centre))
            curseur.goto(centre)
        else:
            aligner_sur_y(curseur, centre[1]*1.5)
            aligner_sur_x(curseur, centre[0])
            curseur.setheading( curseur.towards(centre))
            curseur.goto(centre)
    elif coin_droite == coins['coin_HG']:
        # aligner le curseur sur l axe y et entrer dans la piece
        centre = (coin_droite[0] + int(ouverture_proche['distance_coin'] / 2), coin_droite[1] - delta)
        #verifier si y_curseur > coin_droite[1]
        if robot_pos[1] > coin_droite[1]:
            aligner_sur_x(curseur, centre[0])
            curseur.setheading( curseur.towards(centre))

            curseur.goto(centre)
        else:
            aligner_sur_y(curseur, centre[1]*1.5)
            aligner_sur_x(curseur, centre[0])
            curseur.setheading( curseur.towards(centre))
            curseur.goto(centre)
# Fonction pour calculer la distance entre le curseur et un coin
def get_distance(curseur, point):
    """
    Calcule la distance entre le curseur et un coin donné.
    Retourne la distance.
    """
    x_curseur, y_curseur = curseur.position()
    return sqrt((point[0] - x_curseur) ** 2 + (point[1] - y_curseur) ** 2)
# dans un repere orthonormé, la distance entre deux points est donnée par la formule de pythagore 
#distance = racine ( (x2 - x1)² + (y2 - y1)² )

############## FIN DE LA NAVIGATION POUR FAIRE ENTRER LE ROBOT DANS LA PIECE ####################



#navigation 
from dectection_collision import *
def aller_vers(curseur, piece, destination):
    """
    Déplace le curseur vers une destination donnée.
    """
    #orienter le curseur vers la destination
    curseur.setheading(curseur.towards(destination))

    #determiner les obstacles critiques et les contourner
    obstacles = piece.get('obstacles', [])
    obstacles_critiques = get_Obstacles_critiques(obstacles , curseur)

    if len(obstacles_critiques) == 0:
        #aucun obstacle critique
        curseur.goto(destination)
        return
    
    for obstacle, point_entree, point_sortie in obstacles_critiques:
        #comparer la distance entre le curseur et le point de collision avec la distance entre le curseur et la destination
        distance_collision = curseur.distance(point_entree)
        distance_destination = curseur.distance(destination)
        if distance_collision > distance_destination:
            #le robot est déjà plus proche de la destination que du point de collision
            # pas de collision

            curseur.goto(destination)
            return
        else :
            #le robot est plus proche du point de collision que de la destination
            #contourner l'obstacle
            #se diriger vers le point d'entree
            curseur.goto(point_entree)
            #contourner l'obstacle et se diriger vers le point de sortie en faisant un demi-cercle de rayon diemension

            curseur.right(90)
            curseur.forward(obstacle['dimension']*1.5)
            curseur.left(90)
            curseur.forward(obstacle['dimension']*1.5)
            curseur.left(90)
            curseur.forward(obstacle['dimension']*1.5)
            curseur.setheading(curseur.towards(destination))
            break

    #se diriger vers la destination
    aller_vers(curseur, piece, destination)





