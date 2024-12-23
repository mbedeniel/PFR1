import keyboard
from mouvement import vocal_reception, adaptation_donnees
from interaction import mode_Vocal, mode_ihm

def menu(new_curseur, piece):
    """
    Affiche le menu principal et gère le choix de mode (vocal ou IHM).
    """
    print("Veuillez choisir un mode parmi les suivants :\n")
    print("1 : Mode Vocal\n")
    print("2 : Mode IHM\n")

    choix = input("Saisissez le mode (1 ou 2) : ")
    if choix == "1":
        print("__Mode Vocal__")
        while not keyboard.is_pressed('q'):
            print("Appuyez sur 'q' pour quitter le mode vocal")
            data = mode_Vocal()
            adapted_data = adaptation_donnees(data)
            vocal_reception(new_curseur, adapted_data, piece)
    elif choix == "2":
        print("__Mode IHM__")
        while not keyboard.is_pressed('q'):
            print("Appuyez sur 'q' pour quitter le mode IHM")
            data = mode_ihm()
            adapted_data = adaptation_donnees(data)
            vocal_reception(new_curseur, adapted_data, piece)
