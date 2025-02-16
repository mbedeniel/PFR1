#CE FINCHIER N EST PAS ENCORE COMPLET. IL RESTE DU TRAVAIL A FAIRE.
"""
EN GROS, ICI J'ESSAIE D IMPLEMENTER LA NAVIGATION AUTOMATIQUE DU ROBOT 
LUI DONNER LA FACULTE DE CONTOURNER LES OBSTACLES POUR ATTEINDRE SA DESTINATION
AUTREMENT DIT, IL DOIT SE DEPLACER DANS LA PIECE SANS PERCUTER (traverser) UN OBSTACLE , NI SE TROUVER DANS UN OBSTACLE
OU DE SORTIR DE LA PIECE EN TRAVERSANT LES MURS
"""
from simulation.data.settings import get_text
from simulation.plateform.drawing import est_dans_piece  # Assure-toi que cette fonction contient les définitions nécessaires
from simulation.data.init import init_coins 
from simulation.plateform.drawing import est_dans_piece
from simulation.logger.logger import display 
from simulation.navigation.dectection_collision import get_Obstacles_critiques, point_is_in_obstacle
## les  fonction a venir sont des fonctions qui permettent de  positionner le robot dans la piece
"""
En d autre terme, si le robot est à l'extérieur de la pièce, ces fonctions permettent 
 de le faire entrer dans la pièce en passant par l ouverture le plus proche de lui.
expliquons un peu le fonctionnement de ces fonctions:
1. On vérifie si le robot est déjà dans la pièce ? si oui, on ne fait rien ,sion 
2. On récupère les ouvertures de la pièce
3. On trouve l'ouverture la plus proche du robot
4. s aligne sur l axe x ou y par rapport au centre de l ouverture la plus proche
5. on se dirige vers le centre de l ouverture
6. on entre dans la pièce en se dirigeant vers le centre de l ouverture en le deplacant de quelques pixels
                7. YOUPIIIII LE ROBOT EST DANS LA PIECE :)
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
 # Vérifier si le robot est déjà dans la pièce , si oui, on ne fait rien
    if est_dans_piece(curseur.position(), piece):
        return
    
    #sinon
    # Récupérer les ouvertures de la pièce
    ouvertures = piece.get('ouvertures', [])
    if not ouvertures:
        display(get_text('no_ouverture'))
        return

    # Trouver l'ouverture la plus proche du robot
    robot_pos = curseur.position()
    #trier les ouvertures par distance minimale
    ouverture_proche = min(ouvertures, key=lambda ouverture: curseur.distance(ouverture['coin_droite']))
    # Identifier l'orientation de l'ouverture
    coin_droite = ouverture_proche['coin_droite']
    coins = init_coins(piece)
    #en fonction du coin_droite, on peut s avoir l'orientation de l'ouverture (horizontal ou vertical)
    if coin_droite == coins['coin_BG']:
        #OKKKKKKKKKKKKKKK
        # aligner le curseur sur l axe x et entrer dans la piece
        centre = (coin_droite[0] + delta , coin_droite[1] + int(ouverture_proche['distance_coin'] / 2))
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


def contourner_obstacle(curseur, obstacle, entre, sortie, piece):

    if entre == None or sortie == None or obstacle == None:
        return
    #calculer les dimensions de l'obstacle
    dimensions = obstacle.get('dimension')
    if obstacle.get('forme') == 'cercle':
        dimensions = dimensions + 10
    else:
        dimensions = dimensions + 10
    
    heading = curseur.heading() 
    #pour savaoir de quelle coter contourner l obstacle, calculer le centre de l obstacle
    #comparer le cap du centre et et le cap de la sortie
    # si cap_centre < cap_sortie, contourner par la droite
    #sinon contourner par la gauche
    coin_HD_obstacle = obstacle.get('coin_HD')

    #calculer le centre de l obstacle
    if obstacle.get('forme') == 'cercle':
        rayon = obstacle.get("dimension")
        centre_x, centre_y = coin_HD_obstacle[0], coin_HD_obstacle[1] - rayon
        centre = (centre_x, centre_y)
    else:
        centre = (coin_HD_obstacle[0] - dimensions / 2, coin_HD_obstacle[1] - dimensions / 2)
    
    #calculer le cap(heading)  du centre de l'obstacle pour savoir de quel coter contourner l'obstacle
    cap_centre_object = curseur.towards(centre)
    if heading < cap_centre_object <= heading + 180:
        bon_angle = -90 # contourner par la gauche de l'obstacle
    else:
        bon_angle = 90 # contourner par la droite de l'obstacle

    # Contourner l'obstacle : se déplace autour de l'obstacle
    distance_sortie = curseur.distance((sortie[0], sortie[1])) + 5
    dimension_contournement = dimensions * (distance_sortie / dimensions) / 1.5 # calculer la longyeur a parcourir pour contourner l'obstacle au plus pres
    curseur.setheading(heading +  bon_angle) 
    curseur.forward(dimension_contournement)  # Se déplace autour de l'obstacle
    curseur.setheading(heading) # Se remet dans la direction initiale
    curseur.forward(distance_sortie)  # Se déplace autour de l'obstacle
    curseur.setheading(heading -  bon_angle) 
    curseur.forward(dimension_contournement)  # Se déplace autour de l'obstacle
    curseur.setheading(heading) # Se remet dans la direction initiale


def aller_vers(curseur, piece, destination):
    """
    Déplace le curseur vers une destination donnée.
    """
    # Vérifier si la destination est dans la pièce
    if not est_dans_piece(destination, piece):
        display(get_text('destination_outside'))
        return
    

    #orienter le curseur vers la destination
    curseur.setheading(curseur.towards(destination))

    #determiner les obstacles critiques et les contourner
    obstacles = piece.get('obstacles', [])
    obstacles_critiques = get_Obstacles_critiques(obstacles , curseur, curseur.heading())
    #condition d'arret
    if len(obstacles_critiques) == 0:
        display(get_text('mouving_robot'))
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
            display(get_text('mouving_robot'))
            curseur.goto(destination)
            break

        #contourner l'obstacle
        display(get_text('critical_obstacle'))
        #verifier si la destination est dans l'obstacle
        if point_is_in_obstacle(destination, obstacle):
            display(get_text('destination_in_obstacle'))
            display(get_text('impossible_to_move'))
            return
        else :
            curseur.goto(point_entree)
            display(get_text('contournement_obstacle').format(obstacle.get('nom')))
            contourner_obstacle(curseur, obstacle, point_entree, point_sortie, piece)
            display(get_text('end_contournement'))
            display(get_text('go_to_destination'))
            aller_vers(curseur, piece, destination)
            break