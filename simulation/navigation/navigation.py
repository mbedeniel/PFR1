#CE FINCHIER N EST PAS ENCORE COMPLET. IL RESTE DU TRAVAIL A FAIRE.
"""
EN GROS, ICI J'ESSAIE D IMPLEMENTER LA NAVIGATION AUTOMATIQUE DU ROBOT 
LUI DONNER LA FACULTE DE CONTOURNER LES OBSTACLES POUR ATTEINDRE SA DESTINATION
AUTREMENT DIT, IL DOIT SE DEPLACER DANS LA PIECE SANS PERCUTER (traverser) UN OBSTACLE

"""
from math import cos, sin, radians , pi , sqrt
#from simulation.navigation.dectection_collision import *
from simulation.plateform.drawing import est_dans_piece  # Assure-toi que cette fonction contient les définitions nécessaires
from simulation.data.init import init_coins 
from simulation.plateform.drawing import est_dans_piece
from simulation.data.settings import __DEBUG__
from simulation.navigation.dectection_collision import get_Obstacles_critiques, point_is_in_obstacle
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
        if __DEBUG__:
            print("Le robot est déjà à l'intérieur de la pièce.")
        return

    # Récupérer les ouvertures de la pièce
    ouvertures = piece.get('ouvertures', [])
    if not ouvertures:
        if __DEBUG__: 
            print("Erreur : La pièce n'a pas d'ouvertures.")
        return

    # Trouver l'ouverture la plus proche du robot
    robot_pos = curseur.position()
   # ouverture_proche = min(ouvertures, key=lambda ouverture: get_distance(curseur, ouverture['coin_droite']))
    ouverture_proche = min(ouvertures, key=lambda ouverture: curseur.distance(ouverture['coin_droite']))
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


############## FIN DE LA NAVIGATION POUR FAIRE ENTRER LE ROBOT DANS LA PIECE ####################



#navigation 


def contourner_obstacle(curseur, obstacle, entre, sortie):

    dimensions = obstacle.get('dimension') * 2
    heading = curseur.heading()
    # Contourner l'obstacle : se déplace autour de l'obstacle
    distance_sortie = curseur.distance(sortie)
    curseur.setheading(heading + 90) # Se dirige vers la droite
    curseur.forward(dimensions)  # Se déplace autour de l'obstacle
    curseur.setheading(heading) # Se remet dans la direction initiale
    curseur.forward(distance_sortie)  # Se déplace autour de l'obstacle
    curseur.setheading(heading - 90) # Se dirige vers la gauche
    curseur.forward(dimensions)  # Se déplace autour de l'obstacle
    curseur.setheading(heading) # Se remet dans la direction initiale








    """

    curseur.right(angle)
    alpha = radians(curseur.heading())
    
    destination = (curseur.xcor() + dimensions * cos(alpha), curseur.ycor() + dimensions * sin(alpha))
    aller_vers(curseur, obstacle, destination)
    #curseur.forward(dimensions)  # Se déplace autour de l'obstacle
    curseur.left(angle)
    destination = (curseur.xcor() + dimensions * cos(alpha), curseur.ycor() + dimensions * sin(alpha))
    aller_vers(curseur, obstacle, destination)
    #curseur.forward(distance_sortie)  # Se dirige vers la sortie
    curseur.left(angle)
    curseur.forward(dimensions)  # Se déplace autour de l'obstacle de l'autre côté
    curseur.right(angle)

    # Remettre le curseur sur la direction vers la sortie
    curseur.setheading(curseur.towards(sortie))
    """
    



def aller_vers(curseur, piece, destination):
    """
    Déplace le curseur vers une destination donnée.
    """
    # Vérifier si la destination est dans la pièce
    if not est_dans_piece(destination, piece):
        if __DEBUG__:
            print("Erreur: la destination est en dehors de la pièce.")
        return
    

    #orienter le curseur vers la destination
    curseur.setheading(curseur.towards(destination))

    #determiner les obstacles critiques et les contourner
    obstacles = piece.get('obstacles', [])
    obstacles_critiques = get_Obstacles_critiques(obstacles , curseur)
    #condition d'arret
    if len(obstacles_critiques) == 0:
        print("Aucun obstacle critique trouvé.")
        curseur.goto(destination)
        return
    
    #trier les obstacles critiques par distance
    #contourner les obstacles critiques
    for data in obstacles_critiques:
        obstacle, point_entree, point_sortie = data
        #calculer la distance entre le curseur et le point d'entree
        distanceEntre  = curseur.distance(point_entree)
        distanceDestination =   curseur.distance(destination)
        if distanceEntre > distanceDestination: #si le point d'entree est plus loin que la destination
            curseur.goto(destination)
            print(f"Le point d'entrée({point_entree}) est plus loin que la destination({destination}).")
            break
        #contourner l'obstacle
        print("obscalte trouve")
        #verifier si la destination est dans l'obstacle
        if point_is_in_obstacle(destination, obstacle):
            print("La destination est dans l'obstacle.")
            return
        else :
            curseur.goto(point_entree)
            print(f"C'est bon. On contourne l'obstacle {obstacle['nom']}.")
            contourner_obstacle(curseur, obstacle, point_entree, point_sortie)
        