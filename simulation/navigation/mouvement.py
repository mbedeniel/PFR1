from simulation.plateform.drawing import est_dans_piece
from math import cos, sin, radians

from simulation.navigation.navigation import  aller_vers
from simulation.data.settings import __DEBUG__

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
        if __DEBUG__:
            print(f"Erreur: le curseur risque de sortir de la piece.")
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
            if __DEBUG__:
                print("Erreur: mouvement non reconnu.")

    if reception["rotation"] != None:
        if 'droite' in reception["rotation"].lower():
            rotation(curceur, reception["angle_rotation"])
        elif 'gauche' in reception["rotation"].lower():
            rotation(curceur, -reception["angle_rotation"])
        else:
            if __DEBUG__:
                print("Erreur: rotation non reconnue.")

def adaptation_donnees(data):
    """
    Adapte les données reçues au format requis pour le déplacement et l'orientation.
    """
    reception = {
        'mouvement': None,
        'distance_mouvement': None,
        'rotation': None,
        'angle_rotation': None,
    }
    
    if data ==None or  len(data) == 0:
        return reception

    cle, valeur = next(iter(data.items()))
    if 'avance' in cle or 'recule' in cle:
        reception["mouvement"] = cle
        reception["distance_mouvement"] = valeur
    elif 'droite' in cle or 'gauche' in cle:
        reception["rotation"] = cle
        reception["angle_rotation"] = valeur

    return reception
