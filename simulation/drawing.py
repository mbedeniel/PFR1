import turtle as tl
from init import init_coins

"""
CE FICHIER CONTIENT LES FONCTIONS DE TRACAGE DES PIECES, DES OUVERTURES ET DES OBSTACLES.
C EST LUI QUI GERE L AFFICHAGE DES ELEMENTS DU JEU. (Interface graphique)
"""


def tracer_piece(piece, curseur):
    """
    Trace un rectangle représentant une pièce de jeu selon ses dimensions, son coin haut droit,
    sa couleur et l'épaisseur des traits définis dans le dictionnaire `piece`.
    """
    curseur.up()
    curseur.speed(10)
    #aller au positon du coin HD et orienter le curseur vers le bas
    curseur.goto(piece["coin_HD"])
    curseur.setheading(270)

    curseur.width(piece['trait'])
    curseur.color(piece['couleur'])
    curseur.down()
    #tracer le rectangle
    for _ in range(2):
        curseur.forward(piece["dimensions"][0])
        curseur.right(90)
        curseur.forward(piece["dimensions"][1])
        curseur.right(90)
    
    curseur.up()
    #tracer les ouvertures et les obstacles
    for ouv in piece['ouvertures']:
        tracer_ouverture(ouv, curseur, piece)
    #tracer les obstacles
    for obs in piece['obstacles']:
        tracer_obstacle(obs, curseur, piece)

def modif_curseur():
    """
    Modifie la forme du curseur pour utiliser une forme personnalisée définie par des coordonnées.
    """
    custom_shape = [(-8.5, -12.5), (-8.5, -9.5), (-10.5, -9.5), (-10.5, -6.5), (-8.5, -6.5), 
                    (-8.5, 6.5), (-10.5, 6.5), (-10.5, 9.5), (-8.5, 9.5), (-8.5, 12.5), 
                    (0, 12.5), (0, 5), (-5, -2.5), (5, -2.5), (0, 5), (0, 12.5), 
                    (8.5, 12.5), (8.5, 9.5), (10.5, 9.5), (10.5, 6.5), (8.5, 6.5), 
                    (8.5, -6.5), (10.5, -6.5), (10.5, -9.5), (8.5, -9.5), (8.5, -12.5), 
                    (-8.5, -12.5)]
    tl.register_shape("plateform", tuple(custom_shape))
    curceur_modifier = tl.Turtle()
    curceur_modifier.shape("plateform")
    curceur_modifier.color("black")

    return curceur_modifier
def tracer_cercle(rayon, curseur):
    """
    Trace un cercle de rayon `rayon` et de couleur `couleur` sur la curseur `curseur`.
    """
    curseur.circle(rayon)
def tracer_carre(cote, curseur ):
    """
    Trace un carré de côté `cote` et de couleur `couleur` avec le curseur `curseur`.
    """
    for _ in range(4):
        curseur.forward(cote)
        curseur.right(90)
#verifier si un point est a l interieur de la piece
def est_dans_piece(point, piece):
    """
    Verifie si un point est a l interieur de la piece.
    """
    coins = init_coins(piece)
    #si !(piece_x1 < point_x1 < piece_x2) ou ! (piece_y1 > point_y1 > piece_y2) alors le point est en dehors de la piece
    piece_x1 , piece_y1 = coins["coin_HG"]
    piece_x2 , piece_y2 = coins["coin_BD"]
    if not (piece_x1 <= point[0] <= piece_x2) or not (piece_y1 >= point[1] >= piece_y2):
        if not (piece_x1 < point[0] < piece_x2):
            print(f"Erreur: le point {point} est en dehors de la piece sur l'axe X.")
        if not (piece_y1 > point[1] > piece_y2):
            print(f"Erreur: le point {point} est en dehors de la piece sur l'axe Y.")
        print(f"\tCoordonné de la piece: x∈[{piece_x1}, {piece_x2}] et y∈[{piece_y2}, {piece_y1}]\n\tCoordonné du point: x={point[0]} et y={point[1]}")
        return False
    return True

def tracer_obstacle(obstacle, curseur, piece):
    """
    Trace un obstacle de forme `obstacle` avec le curseur `curseur`.
    un obstacle est soit un cercle, soit un carré.
    """
     #verifier si le coin_HD de l obstacle est a l interieur de la piece
    coins = init_coins(piece)
    #verifier si le coin_HD de l obstacle est a l interieur de la piece 
    if not est_dans_piece(obstacle["coin_HD"], piece):
        print(f"Erreur: l obstacle {obstacle['nom']} est en dehors de la piece.")
        return None 
    
    #aller au positon du coin HD
    curseur.up()
    curseur.goto(obstacle["coin_HD"])
    curseur.down()

    curseur.color(obstacle["couleur"])
    curseur.begin_fill()

    if obstacle["forme"] == "cercle":
        tracer_cercle(obstacle["dimension"],curseur)
    elif obstacle["forme"] == "carre":
        tracer_carre(obstacle["dimension"], curseur)
    else:
        print(f"Erreur: l obstacle {obstacle['nom']} a une forme invalide.Sa forme({obstacle['forme']}) doit être 'cercle' ou 'carre'.")

    curseur.end_fill()
    curseur.up() 

def tracer_ouverture(ouverture, curseur , piece):
    """
    Trace une ouverture de forme `ouverture` avec le curseur `curseur`.
    une ouverture est soit un cercle, soit un carré.
    """
    curseur.up()
    curseur.goto(ouverture["coin_droite"])
    curseur.down()

    curseur.color(ouverture["color"])
    curseur.begin_fill()

    #si le coin est le coin_HD  l orientation de l ouverture est vers le bas pour aller vers le coin BD (angle 270 ou -90)
    #si le coin est le coin_HG  l orientation de l ouverture est vers la droite pour aller vers le coin HD (angle 0)
    #si le coin est le coin_BD  l orientation de l ouverture est vers la gauche pour aller vers le coin BG (angle 180)
    #si le coin est le coin_BG  l orientation de l ouverture est vers le haut pour aller vers le coin HG (angle 90)
    coins = init_coins(piece)
    if ouverture["coin_droite"] == coins["coin_HD"]:
        curseur.setheading(-90)
    elif ouverture["coin_droite"] == coins["coin_HG"]:
        curseur.setheading(0)
    elif ouverture["coin_droite"] == coins["coin_BD"]:
        curseur.setheading(90)
    elif ouverture["coin_droite"] == coins["coin_BG"]:
        curseur.setheading(180)
    else :
        print(f"Erreur: l ouverture {ouverture['coin_droite']} n est pas un coin de la piece.")
        return None
    curseur.forward(ouverture["distance_coin"])

    
    