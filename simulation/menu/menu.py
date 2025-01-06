from simulation.navigation.mouvement import vocal_reception, adaptation_donnees
from time import sleep
from simulation.data.settings import __DEBUG__,__SPEAK__, MENU_TEXT, LANGUAGES , get_text, set_language ,current_language
from simulation.loader.interaction import mode_ihm , mode_Vocal
from vocal.python.speaker import speak


def menu(new_curseur, piece):
    """
    Affiche le menu principal et gère le choix de mode (vocal ou IHM).
    L'utilisateur peut changer la langue ou quitter avec 'q'.
    """
    set_language()  # Permet de choisir la langue au lancement

    print(get_text('welcome'))

    if __SPEAK__:
        speak(get_text('welcome'), current_language)

    while True:
        print(get_text('choose_mode'))
        if __SPEAK__:
            speak(get_text('choose_mode'), current_language)
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
            if __SPEAK__:
                speak(get_text('invalid_choice'), current_language)

    print(get_text('goodbye'))
    if __SPEAK__:
        speak(get_text('goodbye'), current_language)

def lancer_mode_vocal(new_curseur, piece):
    """
    Gère le fonctionnement du mode vocal.
    """
    print(get_text('vocal_mode'))
    if __SPEAK__:
        speak(get_text('vocal_mode'), current_language)

    while True:
        print(get_text('quit_vocal'))
        if __SPEAK__:
            speak(get_text('quit_vocal'), current_language)
        data = mode_Vocal()
        adapted_data = adaptation_donnees(data)
        
        vocal_reception(new_curseur, adapted_data, piece)
        sleep(2)
        #verifier si "Stop" a été prononcé 
        commande = data.get('action', '')
        if "stop" in commande.lower():
            break

    print(get_text('end_vocal'))
    if __SPEAK__:
        speak(get_text('end_vocal'), current_language)

def lancer_mode_ihm(new_curseur, piece):
    """
    Gère le fonctionnement du mode IHM.
    """
    print(get_text('ihm_mode'))
    while True:
        print(get_text('quit_ihm'))
        if __SPEAK__:
            speak(get_text('quit_ihm'), current_language)

        data = mode_ihm()
        adapted_data = adaptation_donnees(data)
        vocal_reception(new_curseur, adapted_data, piece)
        sleep(2)
        quitter = input(get_text('quit_prompt')).strip().lower()
        if quitter == 'o':
            break

    print(get_text('end_ihm'))
    if __SPEAK__:
        speak(get_text('end_ihm'), current_language)
