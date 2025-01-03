from simulation.navigation.mouvement import vocal_reception, adaptation_donnees
from simulation.loader.interaction import mode_Vocal, mode_ihm
from time import sleep
from simulation.data.settings import __DEBUG__, MENU_TEXT, LANGUAGES , get_text, set_language


def menu(new_curseur, piece):
    """
    Affiche le menu principal et gère le choix de mode (vocal ou IHM).
    L'utilisateur peut changer la langue ou quitter avec 'q'.
    """
    set_language()  # Permet de choisir la langue au lancement

    print(get_text('welcome'))

    while True:
        print(get_text('choose_mode'))
        choix = input(get_text('prompt')).strip()

        if choix == '1':
            lancer_mode_vocal(new_curseur, piece)
        elif choix == '2':
            lancer_mode_ihm(new_curseur, piece)
        elif choix.lower() == 'l':
            set_language()
        elif choix.lower() == 'q':
            break
        else:
            print(get_text('invalid_choice'))

    print(get_text('goodbye'))

def lancer_mode_vocal(new_curseur, piece):
    """
    Gère le fonctionnement du mode vocal.
    """
    print(get_text('vocal_mode'))
    while True:
        print(get_text('quit_vocal'))
        data = mode_Vocal()
        adapted_data = adaptation_donnees(data)
        vocal_reception(new_curseur, adapted_data, piece)
        sleep(2)
        quitter = input(get_text('quit_prompt')).strip().lower()
        if quitter == 'o':
            break
    print(get_text('end_vocal'))

def lancer_mode_ihm(new_curseur, piece):
    """
    Gère le fonctionnement du mode IHM.
    """
    print(get_text('ihm_mode'))
    while True:
        print(get_text('quit_ihm'))
        data = mode_ihm()
        adapted_data = adaptation_donnees(data)
        vocal_reception(new_curseur, adapted_data, piece)
        sleep(2)
        quitter = input(get_text('quit_prompt')).strip().lower()
        if quitter == 'o':
            break
    print(get_text('end_ihm'))
