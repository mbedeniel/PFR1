import turtle as tl

# ___________________Fonctions___________________

# Surface de jeu
def tracer_piece(piece, page):
    # Déplacement au coin Haut Droit
    page.up()
    page.speed(10)
    page.goto(piece["coin_HD"])
    page.setheading(270)  # Tourne vers le bas

    # Données pour le traçage
    page.width(piece['trait'])
    page.color(piece['couleur'])
    page.down()
    
    for _ in range(2):
        page.forward(piece["dimensions"][0])
        page.right(90)
        page.forward(piece["dimensions"][1])
        page.right(90)
    
    page.up()

def modif_curseur():    
    custom_shape = [(-8.5, -12.5),(-8.5, -9.5),(-10.5, -9.5),(-10.5, -6.5),(-8.5, -6.5),(-8.5, 6.5),(-10.5, 6.5),(-10.5, 9.5),(-8.5, 9.5),(-8.5,12.5),(0,12.5),(0,5),(-5,-2.5),(5,-2.5),(0,5),(0,12.5),(8.5,12.5),(8.5,9.5),(10.5,9.5),(10.5,6.5),(8.5,6.5),(8.5,-6.5),(10.5,-6.5),(10.5,-9.5),(8.5,-9.5),(8.5, -12.5),(-8.5, -12.5)]
    tl.register_shape("plateform", tuple(custom_shape))
    # Création d'une tortue avec la nouvelle forme
    curceur_modifier = tl.Turtle()
    curceur_modifier.shape("plateform")
    curceur_modifier.color("black")  # Couleur de la forme

    return curceur_modifier


def translantion(curceur,val):
    curceur.forward(val)

def rotation(curceur,val):
    curceur.right(val)
    
reception = {
        'mouvement': None, #(Avance/Recule)
        'distance_mouvement' : None, #(Valeur numerique)
        'rotation' : None, #(Droite/Gauche)
        'angle_rotation' : None, #(Valeur Numerique)
    }

def vocal_reception(curceur ,reception):
    # Avec reception un dictionnaire :
    if reception["mouvement"]!= None :
        if reception["mouvement"] == 'avance':
            translantion(curceur ,reception["distance_mouvement"])
        else: 
            translantion(curceur ,- reception["distance_mouvement"])
    if reception["rotation"]!= None :
        if reception["rotation"] == 'droite':
            rotation(curceur ,reception["angle_rotation"])
        else: 
            rotation(curceur ,- reception["angle_rotation"])
        


# ___________________Main___________________

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
trace_piece.hideturtle()  # Masque le curseur
tracer_piece(piece, trace_piece)
new_curseur = modif_curseur()

# Déplacement de démonstration
new_curseur.up()
new_curseur.goto(0, 0)
new_curseur.down()
new_curseur.speed(1)
new_curseur.right(32)
new_curseur.forward(300)
new_curseur.right(58+90)
new_curseur.forward(400)


tl.done()
