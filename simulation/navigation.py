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
Cas du cercle :
-------------------
L’équation d’un cercle est donnée par : (x - xc)² + (y - yc)² = r²
- xc et yc : Coordonnées du centre du cercle.
- r : Rayon du cercle.

Pour vérifier une collision avec un cercle :
1. La position du point à un instant t est donnée par :
   P(t) = (x0 + t * cos(α), y0 + t * sin(α))
   - x0, y0 : Position initiale du point.
   - α : Direction (heading) du point.

2. On remplace les coordonnées de P(t) dans l’équation du cercle.
   Cela permet de trouver la distance entre le point et le centre du cercle :
   X = x0 + t * cos(α)
   Y = y0 + t * sin(α)

3. Après injection de X et Y dans l’équation du cercle, on obtient une équation quadratique :
   t² - 2 * A * t + B = 0
   - A = (x0 - xc) * cos(α) + (y0 - yc) * sin(α)
   - B = (x0 - xc)² + (y0 - yc)² - r²

4. Analyse du discriminant (Δ) :
   - Si Δ < 0 : Pas de collision. Le point ne rencontrera jamais le cercle.
   - Si Δ = 0 : Collision tangente. Le point effleure le cercle.
   - Si Δ > 0 : Deux temps t1 et t2.
     * Le plus petit t correspond à l’entrée dans le cercle.
     * Le plus grand t correspond à la sortie.

5. Points de collision :
   - Calculés avec P(T) = (x0 + T * cos(α), y0 + T * sin(α)).

Cas du rectangle :
-------------------
Un rectangle est défini par ses coordonnées : (X1, Y1) et (X2, Y2)

Pour vérifier une collision avec un rectangle :
1. Conditions d’intersection :
   - Le point doit respecter :
     X1 ≤ xp ≤ X2 et Y1 ≤ yp ≤ Y2
   - xp et yp : Coordonnées de la trajectoire à un instant t.

2. Calcul des temps d’intersection :
   - Pour les côtés verticaux (à X = X1 ou X = X2) :
     t_x = (X1 - x0) / cos(α) ou t_x = (X2 - x0) / cos(α)
   - Pour les côtés horizontaux (à Y = Y1 ou Y = Y2) :
     t_y = (Y1 - y0) / sin(α) ou t_y = (Y2 - y0) / sin(α)

3. Temps valides :
   - Conservez les valeurs de t > 0.
   - Vérifiez si les coordonnées correspondantes sont dans les limites du rectangle.
   - Le plus petit t est le temps d’entrée.
   - Le plus grand t est le temps de sortie.

4. Points d’intersection :
   - Coordonnées calculées avec P(t) = (x0 + t * cos(α), y0 + t * sin(α)).

5. Absence de collision :
   - Si aucune valeur de t ne satisfait les conditions, alors il n’y a pas de collision avec le rectangle.
"""

