import turtle as tl
from integration.main import *
import keyboard
#faites "pip install keyboard" pour installer le module keyboard

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
        

############################################### aajouter  par Djibril pour des tests
# Adaptation des données reçues 
def adaptation_donnees(data):
    #verifier si la cle c est avance , recule , droite ou gauche et recuperer la valeur associee
   
    
    reception = {
        'mouvement': None, #(Avance/Recule)
        'distance_mouvement' : None, #(Valeur numerique)
        'rotation' : None, #(Droite/Gauche)
        'angle_rotation' : None, #(Valeur Numerique)
    }
    print("-------------------Debug-------------------")
    print("Données reçues : ", data)
    if len (data) == 0:
        return reception
    cle, valeur = next(iter(data.items()))
    if 'avance' in cle or 'recule' in cle:
        reception["mouvement"] = cle
        reception["distance_mouvement"] = valeur
    elif 'droite' in cle or 'gauche' in cle:
        reception["rotation"] = cle
        reception["angle_rotation"] = valeur

    
    print("Données adaptées : ", reception)
    print("-------------------------------------------")

    return reception
    
def menu():
    # Présentation du menu
    print("Veuillez choisir un mode parmi les suivants :\n")
    print("1 : Mode Vocal\n")
    print("2 : Mode IHM\n")
    # Lecture du mode et de la valeur
    choix = input("Saisissez le mode (1 ou 2) : ")
    if choix == "1":
        print("__Mode Vocal__")
        while not keyboard.is_pressed('q'):
            print("Appuyez sur 'q' pour quitter le mode vocal")
            data = Mode_Vocal()
            adapted_data = adaptation_donnees(data)
            vocal_reception(new_curseur, adapted_data)
    if choix == "2":
        #q pour quitter le mode ihm
        print("__Mode IHM__")
        while not keyboard.is_pressed('q'):
            print("Appuyez sur 'q' pour quitter le mode IHM")
            data = mode_ihm()
            adapted_data = adaptation_donnees(data)
            vocal_reception(new_curseur, adapted_data)
        
#############################################################fin
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
new_curseur.speed(1)
while True:
    menu()
    
"""
# Déplacement de démonstration
new_curseur.up()
new_curseur.goto(0, 0)
new_curseur.down()
new_curseur.speed(1)
new_curseur.right(32)
new_curseur.forward(300)
new_curseur.right(58+90)
new_curseur.forward(400)
"""

tl.done()
