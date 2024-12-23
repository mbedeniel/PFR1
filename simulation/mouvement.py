from drawing import est_dans_piece
from math import cos, sin, radians

def translantion(curceur, val, piece):
    """
    Déplace le curseur d'une valeur donnée (positive ou négative).
    """
    #verifier si le curseur risque de sortir de la piece
    x_curseur, y_curseur = curceur.position()
    heatding = curceur.heading()
    #calculer la nouvelle position du curseur
    new_x_curseur = x_curseur + val * cos(radians(heatding))
    new_y_curseur = y_curseur + val * sin(radians(heatding))
    #verifier si le curseur risque de sortir de la piece
    if not est_dans_piece((new_x_curseur, new_y_curseur), piece):
        print(f"Erreur: le curseur risque de sortir de la piece.")
        #se deplacer jusqu au bord de la piece
        return
    curceur.forward(val)

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
        if reception["mouvement"] == 'avance':
            translantion(curceur, reception["distance_mouvement"], piece)
        else: 
            translantion(curceur, -reception["distance_mouvement"], piece)
    if reception["rotation"] != None:
        if reception["rotation"] == 'droite':
            rotation(curceur, reception["angle_rotation"])
        else: 
            rotation(curceur, -reception["angle_rotation"])

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
    if len(data) == 0:
        return reception

    cle, valeur = next(iter(data.items()))
    if 'avance' in cle or 'recule' in cle:
        reception["mouvement"] = cle
        reception["distance_mouvement"] = valeur
    elif 'droite' in cle or 'gauche' in cle:
        reception["rotation"] = cle
        reception["angle_rotation"] = valeur

    return reception
