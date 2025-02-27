import turtle as tl
from simulation.data.init import init_coins
from simulation.data.settings import get_text
from simulation.logger.logger import display 

"""
CE FICHIER CONTIENT LES FONCTIONS DE TRACAGE DES PIECES, DES OUVERTURES ET DES OBSTACLES.
C EST LUI QUI GERE L AFFICHAGE DES ELEMENTS DU JEU. (Interface graphique)
"""

def tracer_piece(piece, curseur):
    curseur.speed(10)
    """
    Trace un rectangle représentant une pièce de jeu selon ses dimensions, son coin haut droit,
    sa couleur et l'épaisseur des traits définis dans le dictionnaire `piece`.
    """
    curseur.up()
    #aller au positon du coin HD et orienter le curseur vers le bas
    curseur.goto(piece["coin_HD"])
    curseur.width(piece['trait'])
    curseur.color(piece['couleur'])
    
    #tracer le rectangle
   #aller au positon du coin HD et orienter le curseur vers le bas
    curseur.down()
    curseur.goto(piece["coins"]["coin_BD"])
    curseur.goto(piece["coins"]["coin_BG"])
    curseur.goto(piece["coins"]["coin_HG"])
    curseur.goto(piece["coin_HD"])


    curseur.up()
    #tracer les ouvertures et les obstacles
    for ouv in piece['ouvertures']:
        tracer_ouverture(ouv, curseur, piece)
        
    #tracer les obstacles
    for obs in piece['obstacles']:
        tracer_obstacle(obs, curseur, piece)
    curseur.speed(1)

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
def tracer_cercle(dimension, curseur):
    """
    Trace un cercle de rayon `rayon` et de couleur `couleur` sur la curseur `curseur`.
    """
    curseur.setheading(180)  # Assurez-vous que le curseur commence dans la bonne direction
    #cercle de centre xc, yc = curseur.position()[0], curseur.position()[1] - dimension
    curseur.circle(dimension) 

#verifier si un point est a l interieur de la piece
def est_dans_piece(point, piece):
    """
    Vérifie si un point est à l'intérieur de la pièce.
    Retourne True si le point est à l'intérieur, False sinon.
    """
    coins = init_coins(piece)
    
    # Extraire les limites de la pièce
    piece_x1 = coins["coin_HG"][0]
    piece_x2 = coins["coin_HD"][0]
    piece_y1 = coins["coin_HD"][1]
    piece_y2 = coins["coin_BD"][1]

    # Vérifier les conditions
    if piece_x1 <= point[0] <= piece_x2 and piece_y2 <= point[1] <= piece_y1:
        return True

    # Si le point est en dehors, afficher les messages d'erreur
    return False

def tracer_obstacle_carre(curseur, obstacle):
    """
    Trace un obstacle carré et imprime les coins.
    """
    cote = obstacle["dimension"]
    curseur.setheading(180)  # Assurez-vous que le curseur commence dans la bonne direction
    for i in range(4):
        curseur.forward(cote)
        curseur.left(90)

def tracer_obstacle(obstacle, curseur, piece):
    """
    Trace un obstacle de forme `obstacle` avec le curseur `curseur`.
    un obstacle est soit un cercle, soit un carré.
    """
    #verifier si le coin_HD de l obstacle est a l interieur de la piece 
    if not est_dans_piece(obstacle["coin_HD"], piece):
        display(get_text('obstacle_outside').format(obstacle["nom"]))
        return None 
    #aller au positon du coin HD
    curseur.up()
    curseur.goto(obstacle["coin_HD"])
    curseur.down()
    curseur.color(obstacle["couleur"])
    curseur.begin_fill()
    if "cercle" == obstacle["forme"]:
        tracer_cercle(obstacle["dimension"],curseur)
    elif "carree" == obstacle["forme"]:
        tracer_obstacle_carre(curseur, obstacle)
    else:
        display(get_text('invalid_form').format(obstacle.get("nom")))

    #AJOUTER UNE DISTANCE DE SECURITE SUR LES OBSTACLES POUR QUE LE ROBOT NE LES TOUCHE PAS
    obstacle["dimension"] += 5
    
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
    if ouverture["coin_droite"] == coins["coin_HG"]:
        curseur.setheading(0)
    elif ouverture["coin_droite"] == coins["coin_BG"]:
        #oriebter le curseur vers le coin le haut
        curseur.setheading(90)
    elif ouverture["coin_droite"] == coins["coin_BD"]:
        curseur.setheading(180)
    elif ouverture["coin_droite"] == coins["coin_HD"]:
        curseur.setheading(270)
    else :
        display(get_text('invalid_coin').format(ouverture.get("coin_HD"), ouverture.get("nom")))
        return None
    curseur.forward(ouverture["distance_coin"])

    
    