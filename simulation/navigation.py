#CE FINCHIER N EST PAS ENCORE COMPLET. IL RESTE DU TRAVAIL A FAIRE.
"""
EN GROS, ICI J'ESSAIE D IMPLEMENTER LA NAVIGATION AUTOMATIQUE DU ROBOT 
LUI DONNER LA FACULTE DE CONTOURNER LES OBSTACLES POUR ATTEINDRE SA DESTINATION
AUTREMENT DIT, IL DOIT POUVOIR SE DEPLACER DANS LA PIECE SANS RENCONTRER D'OBSTACLES

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
def aller_au_point(curseur, point):
    """
    Déplace le curseur vers un point donné.
    """
    curseur.goto(point)

def entrer_robot1(curseur, piece):

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
        centre = (coin_droite[0], coin_droite[1] + int(ouverture_proche['distance_coin'] / 2))
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
        centre = (coin_droite[0], coin_droite[1] - int(ouverture_proche['distance_coin'] / 2))
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
        centre = (coin_droite[0] - int(ouverture_proche['distance_coin'] / 2), coin_droite[1])
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
        centre = (coin_droite[0] + int(ouverture_proche['distance_coin'] / 2), coin_droite[1])
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


##########################fonction pour verifier si le robot qui se deplace d un angle "heading" rencontre un obstacle ou pas
#pour cela il y a deux cas a considerer:
"""
-le cas du cercle : 
    l equation du cercle est donnée par la formule suivante: (x - xc)² + (y - yc)² = r²
    xc et yc sont les coordonnées du centre du cercle et r est le rayon du cercle
    pour verifier si def rencontre_obstacle_cercle(curseur, obstacle):
        La position du point à un instant 𝑡 t est donnée par :
                𝑃(𝑡)=(𝑥0 + 𝑡⋅cos⁡𝛼 , 𝑦0 + 𝑡⋅sin𝛼)
        On remplace les coordonnées de 𝑃(𝑡) dans l'équation du cercle pour trouver la distance entre le point et le centre du cercle
        point le cursuer X= 𝑥0 + 𝑡⋅cos⁡𝛼 et Y = 𝑦0 + 𝑡⋅sin𝛼 avec 𝑥0 et  𝑦0  le position du cursuer et 𝛼 le heading 
        -apres injection de X ET Y sur l equation du cercle on calcule T 
        T^2 - 2AT + B = 0 avec    A = (x0​−xc​)cosα + (y0​−yc​)sinα et B = (x0​−xc​)^2 + (y0​−yc​)^2 − r^2
            +si delta < 0 le curseur ne va jamais se diriger vers ce cercle en gardant ce cap
            +si delta = 0  Cela signifie que le robot efleure l obstacle en ce point 
            +si delta > 0 on a T1 et T2  le plus petit est le T lorsque le robot entre dans l'obstable , et le plus grand au moment ou il vas resortir 

        - Ayant le temps T a la quel le robot va percuter l obstacle , on peut ainsi calculer les coordonnées du point de 
            collision en utilisant P(T) = (𝑥0 + T⋅cos⁡𝛼 , 𝑦0 + T⋅sin𝛼) QUI EST TOUT SIMPLEMENT LE POINT 


-pour le cas des rectangle 
    on sait que un rectangle est defini par 4 point (X1 , X2) et (Y1 , Y2)
    on verifie en quel temps les   X1<=xp<=X2 et Y1<=Yp<=Y2
    ON PRENT LE PLUS PETIT T DE  L INTERSECTION ENTRE C EST DEUX SOLUTION CORRESPONT AU POINT D ENTREE ET E PLUS GRAND AU t DE SORTIE
    -on calcule les coordonnées de c est deux points 
    si n intersecrtion est nul alors pas de collsion avec les rectangles 

"""




