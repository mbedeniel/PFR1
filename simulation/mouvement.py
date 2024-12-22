def translantion(curceur, val):
    """
    Déplace le curseur d'une valeur donnée (positive ou négative).
    """
    curceur.forward(val)

def rotation(curceur, val):
    """
    Fait tourner le curseur d'un angle donné (positif ou négatif).
    """
    curceur.right(val)

def vocal_reception(curceur, reception):
    """
    Déplace et oriente le curseur en fonction des données reçues dans le dictionnaire `reception`.
    """
    if reception["mouvement"] != None:
        if reception["mouvement"] == 'avance':
            translantion(curceur, reception["distance_mouvement"])
        else: 
            translantion(curceur, -reception["distance_mouvement"])
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
