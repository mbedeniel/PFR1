from simulation.plateform.drawing import est_dans_piece
from math import cos, sin, radians
from simulation.navigation.dectection_collision import Test_collision_obstacle
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
        display(f"Déplacement impossible. Le Robot risque de percuter la paroi de la pièce.")
        #se deplacer jusqu au bord de la piece
        return
    
    if val < 0: #le robot recule
        curceur.backward(-val) #comme val est negatif, on le rend positif pour que le robot recule sinon il va avancer
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
            display("Erreur: mouvement non reconnu.")

    if reception["rotation"] != None:
        if 'droite' in reception["rotation"].lower():
            rotation(curceur, reception["angle_rotation"])
        elif 'gauche' in reception["rotation"].lower():
            rotation(curceur, -reception["angle_rotation"])
        else:
            display("Erreur: rotation non reconnue.")


    if reception["mission"] != None:
        display("Mission en cours d'execution")
        
        objectif = reception["mission"]
        if objectif["commande"] == "aller":
            display(f"Deplacement vers l'objet de type {objectif['object']} et de couleur {objectif['color'] if objectif['color'] != None else 'non spécifiée'}")
            forme = objectif["object"]
            color = objectif["color"]
            obstacle = get_obsatcle_by_forme_or_color(piece, forme, color, curceur)
            if obstacle != None:
                heading_obstacle = curceur.towards(obstacle['coin_HD'])
                distance_obstacle = curceur.distance(obstacle['coin_HD']) - 20
                curceur.setheading(heading_obstacle)
                #recuperer le point d'entrée et de sortie de l'obstacle
                colision , point_entre, point_sortie = Test_collision_obstacle(obstacle, curceur)
                
                #aller vers le point d'entrée de l'obstacle si la collision est détectée
                if point_entre !=None :
                    distance_obstacle = curceur.distance((point_entre[0], point_entre[1])) - 20
                    translantion(curceur, distance_obstacle, piece)
                else:
                    translantion(curceur, distance_obstacle, piece)
                display("Mission accomplie.")
                
                
            else:
                display("Erreur: Obstacle de type " + str(forme) + " et de couleur " + str(color) + " non trouvé.")
                display("Mission annulée.")
            
                
        
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
    if color == "rouge":
        return "red"
    elif color == "bleu":
        return "blue"
    elif color == "vert":
        return "green"
    elif color == "jaune":
        return "yellow"
    elif color == "orange":
        return "orange"
    elif color == "violet":
        return "purple"
    elif color == "rose":
        return "pink"
    else:
        return None