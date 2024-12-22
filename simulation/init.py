def init_piece():
    """
    Initialise une pièce de jeu.
    une pièce est un dictionnaire contenant les informations suivantes:
    - nom: le nom de la pièce
    - dimensions: les dimensions de la pièce (largeur, hauteur)
    - coin_HD: le coin haut droit de la pièce
    - couleur: la couleur de la pièce
    - trait: l'épaisseur des traits de la pièce
    - ouvertures: la liste des ouvertures de la pièce
    - obstacles: la liste des obstacles de la pièce
    """
    piece ={
    'nom': 'piece',
    'dimensions': (400, 600),
    'coin_HD': (300, 200),
    'couleur': 'blue',
    'trait': 5,
    'ouvertures': [],
    'obstacles': []
    }
    return piece

def init_obstable(nom ,coin_HD, couleur, forme, dimension):
    """
    Initialise un obstacle de jeu.
    un obstacle est un dictionnaire contenant les informations suivantes:
    - nom: le nom de l'obstacle
    - coin_HD: le coin haut droit de l'obstacle
    - couleur: la couleur de l'obstacle
    - forme: la forme de l'obstacle('cercle' ou 'carre')
    - dimension: 
                    *si la forme est 'cercle', c'est le rayon du cercle, 
                    *si la forme est 'carre', c'est la longueur du côté du carré
    """
    if forme != 'cercle' and forme != 'carre':
        print(f"Erreur: l obstacle {nom} a une forme invalide.Sa forme({forme}) doit être 'cercle' ou 'carre'.")
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
    Initialise les coins d'une pièce de jeu.
    les coins sont des tuples de coordonnées (x, y) représentant les coins d'une pièce de jeu.
    """
    coin_HG = (Piece['coin_HD'][0] - Piece['dimensions'][0], Piece['coin_HD'][1])
    coin_HD = Piece['coin_HD']
    coin_BD = (Piece['coin_HD'][0], Piece['coin_HD'][1] - Piece['dimensions'][1])
    coin_BG = (Piece['coin_HD'][0] - Piece['dimensions'][0], Piece['coin_HD'][1] - Piece['dimensions'][1])

    return {'coin_HG': coin_HG, 'coin_HD': coin_HD, 'coin_BD': coin_BD, 'coin_BG': coin_BG}
def init_ouverture(coin , longueur, distance_coin):
    """
    Initialise les ouvertures d'une pièce de jeu.
    une ouverture est un dictionnaire contenant les informations suivantes:
    - coin: le coin de la pièce où se trouve l'ouverture
    - longueur: la longueur de l'ouverture
    - distance_coin: la distance entre le coin de la pièce et le début de l'ouverture
    - color: la couleur de l'ouverture qui est bleu (fixe)
    """
    ouverture = {
    'coin_droite': coin,
    'longueur': longueur,
    'distance_coin': distance_coin,
    'color': 'orange'
    }
    return ouverture