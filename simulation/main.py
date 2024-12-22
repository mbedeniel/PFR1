import turtle as tl
from drawing import tracer_piece, modif_curseur
from menu import menu

# Initialisation
piece = {
    'nom': 'piece',
    'dimensions': (400, 600),
    'coin_HD': (300, 200),
    'couleur': 'blue',
    'trait': 5,
    'ouvertures': [],
    'obstacles': []
}

trace_piece = tl.Turtle()
trace_piece.hideturtle()
tracer_piece(piece, trace_piece)
new_curseur = modif_curseur()

# Lancer le menu
menu(new_curseur)  # Remplacez par vos fonctions réelles

tl.done()
