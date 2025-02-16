"""@package docstring
Documentation for this module.

Ce module contient les fonctions d'initialisation des pièces et des obstacles.
"""
from simulation.logger.logger import display 

def init_piece():
    """
    Documentation for a function.

    Cette fonctions initialise une pièce de jeu.
    une pièce est un dictionnaire contenant les informations suivantes:
    - nom: le nom de la pièce
    - dimensions: les dimensions de la pièce (largeur, hauteur)
    - coin_HD: le coin haut droit de la pièce
    - couleur: la couleur de la pièce
    - trait: l'épaisseur des traits de la pièce
    - ouvertures: la liste des ouvertures de la pièce
    - obstacles: la liste des obstacles de la pièce

    Returns:
        piece: un dictionnaire contenant les informations de la pièce initialisée
    """
    piece ={
    'nom': 'piece',
    'dimensions': (600, 400), #600, 400
    'coin_HD': (300, 200),
    'coins': {},
    'couleur': 'blue',
    'trait': 5,
    'ouvertures': [],
    'obstacles': []
    }
    piece['coins'] = init_coins(piece)
    return piece

def init_obstable(nom ,coin_HD, couleur, forme, dimension):
    """
    Documentation for a function.

    cette fonction initialise un obstacle de jeu.
    un obstacle est un dictionnaire contenant les informations suivantes:
    - nom: le nom de l'obstacle
    - coin_HD: le coin haut droit de l'obstacle
    - couleur: la couleur de l'obstacle
    - forme: la forme de l'obstacle('cercle' ou 'carree')
    - dimension: 
                    *si la forme est 'cercle', c'est le rayon du cercle, 
                    *si la forme est 'carree', c'est la longueur du côté du carré
    
    Args:
        nom: le nom de l'obstacle
        coin_HD: le coin haut droit de l'obstacle
        couleur: la couleur de l'obstacle
        forme: la forme de l'obstacle('cercle' ou 'carree')
        dimension: 
                    *si la forme est 'cercle', c'est le rayon du cercle, 
                    *si la forme est 'carree', c'est la longueur du côté du carré
    
    Returns:
        obstacle: un dictionnaire contenant les informations de l'obstacle initialisé

    """
    if forme != 'cercle' and forme != 'carree':
        display(f"Erreur: l obstacle {nom} a une forme invalide.Sa forme({forme}) doit être 'cercle' ou 'carre'.")
        return None
    
    obstacle ={
    'nom': nom,
    'coin_HD': coin_HD,
    'couleur': couleur,
    'forme': forme,
    'dimension': dimension
    }
    return obstacle
def init_coins(Piece):
    """
    Documentation for a function.

    cette fonction initialise les coins d'une pièce de jeu.
    les coins sont des tuples de coordonnées (x, y) représentant les coins d'une pièce de jeu.

    Args:
        Piece: un dictionnaire contenant les informations de la pièce

    Returns:
        coins: un dictionnaire contenant les coins de la pièce initialisée
    
    """
    coin_HG = (Piece['coin_HD'][0] - Piece['dimensions'][0], Piece['coin_HD'][1])
    coin_HD = Piece['coin_HD']
    coin_BD = (Piece['coin_HD'][0], Piece['coin_HD'][1] - Piece['dimensions'][1])
    coin_BG = (Piece['coin_HD'][0] - Piece['dimensions'][0], Piece['coin_HD'][1] - Piece['dimensions'][1])

    return {'coin_HG': coin_HG, 'coin_HD': coin_HD, 'coin_BD': coin_BD, 'coin_BG': coin_BG}
def init_ouverture(coin , longueur, distance_coin):
    """
    Documentation for a function.

    cette fonction initialise les ouvertures d'une pièce de jeu.
    une ouverture est un dictionnaire contenant les informations suivantes:
    - coin: le coin de la pièce où se trouve l'ouverture
    - longueur: la longueur de l'ouverture
    - distance_coin: la distance entre le coin de la pièce et le début de l'ouverture
    - color: la couleur de l'ouverture qui est bleu (fixe)

    Args:
        coin: le coin de la pièce où se trouve l'ouverture
        longueur: la longueur de l'ouverture
        distance_coin: la distance entre le coin de la pièce et le début de l'ouverture
        color: la couleur de l'ouverture qui est bleu (fixe)

    Returns:
        ouverture: un dictionnaire contenant les informations de l'ouverture initial
    """
    ouverture = {
    'coin_droite': coin,
    'longueur': longueur,
    'distance_coin': distance_coin,
    'color': 'orange'
    }
    return ouverture

def get_obsatcle_by_forme_or_color(piece ,forme , color , curseur):
    """
    Documentation for a function.

    cette fonction retourne un obstacle le plus plus proche du robot dont la forme et la couleur sont données.

    Args:
        piece: un dictionnaire contenant les informations de la pièce
        forme: la forme de l'obstacle('cercle' ou 'carree')
        color: la couleur de l'obstacle
        curseur: le curseur de la pièce
    
    Returns:
        obstacle : un dictionnaire contenant les informations de l'obstacle le plus proche du robot dont la forme et la couleur sont données
    """
   
    obstacles = piece['obstacles'] #recuperer tous les obstacles de la piece
    selected_obstacle = []
    #filtrer les obstacles de la piece de la forme dont la couleur est celle donnée
    for obstacle in obstacles:
        if obstacle['forme'] == forme and obstacle['couleur'] == color:
            selected_obstacle.append(obstacle)

  
            
    if len(selected_obstacle) == 0:
        return None
    #trier en fonction de la distance entre le curseur et l'obstacle
    #returner le plus proche obstacle si la liste n est pas vide
    selected_obstacle.sort(key=lambda obstacle: curseur.distance(obstacle['coin_HD']))
    return selected_obstacle[0]
   