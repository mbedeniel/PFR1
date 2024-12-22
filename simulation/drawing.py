import turtle as tl

def tracer_piece(piece, page):
    """
    Trace un rectangle représentant une pièce de jeu selon ses dimensions, son coin haut droit,
    sa couleur et l'épaisseur des traits définis dans le dictionnaire `piece`.
    """
    page.up()
    page.speed(10)
    page.goto(piece["coin_HD"])
    page.setheading(270)

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
    """
    Modifie la forme du curseur pour utiliser une forme personnalisée définie par des coordonnées.
    """
    custom_shape = [(-8.5, -12.5), (-8.5, -9.5), (-10.5, -9.5), (-10.5, -6.5), (-8.5, -6.5), 
                    (-8.5, 6.5), (-10.5, 6.5), (-10.5, 9.5), (-8.5, 9.5), (-8.5, 12.5), 
                    (0, 12.5), (0, 5), (-5, -2.5), (5, -2.5), (0, 5), (0, 12.5), 
                    (8.5, 12.5), (8.5, 9.5), (10.5, 9.5), (10.5, 6.5), (8.5, 6.5), 
                    (8.5, -6.5), (10.5, -6.5), (10.5, -9.5), (8.5, -9.5), (8.5, -12.5), 
                    (-8.5, -12.5)]
    tl.register_shape("plateform", tuple(custom_shape))
    curceur_modifier = tl.Turtle()
    curceur_modifier.shape("plateform")
    curceur_modifier.color("black")

    return curceur_modifier
