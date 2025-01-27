from simulation.data.settings import get_text
from simulation.plateform.drawing import est_dans_piece
from math import cos, sin, radians
from simulation.navigation.dectection_collision import Test_collision_obstacle , get_Obstacles_critiques , point_is_in_obstacle
from simulation.navigation.navigation import  aller_vers
from simulation.data.init import get_obsatcle_by_forme_or_color
from simulation.logger.logger import display 

def translantion(curceur, val, piece):
    """
    Déplace le curseur d'une valeur donnée (positive ou négative).
    """
    #verifier si le curseur risque de sortir de la piece
    x_curseur, y_curseur = curceur.position()
    heading = curceur.heading()
    #calculer la nouvelle position du curseur
    new_x_curseur = x_curseur + val * cos(radians(heading))
    new_y_curseur = y_curseur + val * sin(radians(heading))
    #verifier si le curseur risque de sortir de la piece
    destination = (new_x_curseur, new_y_curseur)
    if not est_dans_piece(destination, piece):
        display(get_text('not_in_piece'))
        #se deplacer jusqu au bord de la piece
        return
    
    if val < 0: #le robot recule
        #pour que le robot recule, on verifie s il n y a d'obstacle derriere lui
        obstacle_derriere = get_Obstacles_critiques(piece.get('obstacles', []), curceur, heading + 180)
        if len(obstacle_derriere) != 0:
            (obstacle , point_entre , point_sortie) = obstacle_derriere[0]
            #on verifie la distance entre le curseur et l'obstacle
            distance_obstacle = curceur.distance((point_entre[0], point_entre[1])) - 20
            if distance_obstacle < abs(val) or point_is_in_obstacle(destination, obstacle):
                display(get_text('critical_obstacle'))
                display(get_text('impossible_to_move'))
                return
            else: #on peut reculer  car la distance est suffisamment  (petite) pour reculer (aucun risque e percuter l obstacle)
                curceur.backward(-val) #comme val est negatif, on le rend positif pour que le robot recule sinon il va avancer
        else: #il n y a pas d'obstacle derriere le robot
            curceur.backward(-val)
    else: #le robot avance , pour ne pas tenir compte des obstacles ,if faut utiliser la fonction forward
        aller_vers(curceur, piece , destination) #utiliser la fonction aller_vers pour contourner les obstacles

def rotation(curceur, val):
    """
    Fait tourner le curseur d'un angle donné (positif ou négatif).
    """
    curceur.right(val)


def vocal_reception(curceur, reception, piece):
    """
    Déplace et oriente le curseur en fonction des données reçues dans le dictionnaire `reception`.

    
    """
    if reception["mouvement"] != None:
        if  'avance' in reception["mouvement"].lower():
            translantion(curceur, reception["distance_mouvement"], piece)
        elif 'recule' in reception["mouvement"].lower():
            translantion(curceur, -reception["distance_mouvement"], piece)
        else :
            display(get_text('invalid_movement'))

    if reception["rotation"] != None:
        if 'droite' in reception["rotation"].lower():
            rotation(curceur, reception["angle_rotation"])
        elif 'gauche' in reception["rotation"].lower():
            rotation(curceur, -reception["angle_rotation"])
        else:
            display(get_text('invalid_rotation'))


    if reception["mission"] != None:
        display(get_text('mission_in_progress'))
        
        objectif = reception["mission"]
        if objectif["commande"] == "aller":
            display(get_text('move_to_object').format(objectif["object"], objectif["color"]))
            forme = objectif["object"]
            color = objectif["color"]
            obstacle = get_obsatcle_by_forme_or_color(piece, forme, color, curceur)
            if obstacle != None:
                heading_obstacle = curceur.towards(obstacle['coin_HD'])
                distance_obstacle = curceur.distance(obstacle['coin_HD']) - 20
                curceur.setheading(heading_obstacle)
                #recuperer le point d'entrée et de sortie de l'obstacle
                colision , point_entre, point_sortie = Test_collision_obstacle(obstacle, curceur,curceur.heading())
                
                #aller vers le point d'entrée de l'obstacle si la collision est détectée
                if point_entre !=None :
                    distance_obstacle = curceur.distance((point_entre[0], point_entre[1])) - 20
                    translantion(curceur, distance_obstacle, piece)
                else:
                    translantion(curceur, distance_obstacle, piece)
                display(get_text('mission_accomplished'))
                
                
            else:
                display(get_text('Object_not_found').format(forme, color))
                display(get_text('cancel_mission'))
            
                
        
        #executer la mission (aller vers l object specifie)


#fonction pour adapter les données reçues en fonction des données attendues
def adaptation_donnees(data):
    """
    Adapte les données reçues au format requis pour le déplacement et l'orientation.
    """
    reception = {
        'mouvement': None,
        'distance_mouvement': None,
        'rotation': None,
        'angle_rotation': None,
        "mission": None
    }

    if data ==None or  len(data) == 0:
        return reception
    
    commande = data.get('action')
    if 'avance' in commande or 'recule' in commande:
        reception["mouvement"] = commande
        reception["distance_mouvement"] = data.get('valeur')
    elif 'droite' in commande or 'gauche' in commande:
        reception["rotation"] = commande
        reception["angle_rotation"] = data.get('valeur')
    elif 'aller' in commande:
        _object = data.get('object', None)
        #traduire l'objet en donnée attendue
        if _object == "balle":
            object_ = "cercle"
        elif _object == "cube":
            object_ = "carree"
        else:
            object_ = None
        
        _couleur = data.get('color', None)
        #traduire la couleur en donnée attendue
        color = color_translation(_couleur)

        reception["mission"] = {"commande": "aller", "object": object_, "color": color}

    return reception



def color_translation(color):
    """
    Traduit la couleur en français en anglais.
    """
    couleur={
        "rouge": "red",
        "bleu": "blue",
        "vert": "green",
        "jaune": "yellow",
        "orange": "orange",
        "violet": "purple",
        "rose": "pink",
        "noir": "black",
        "blanc": "white",
        "marron": "brown",
        "gris": "gray",
        "cyan": "cyan"
    }
    return couleur.get(color, None)