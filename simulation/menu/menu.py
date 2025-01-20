import random
import keyboard
from simulation.navigation.mouvement import rotation, translantion, vocal_reception, adaptation_donnees
from time import sleep
from simulation.data.settings import get_text, load_parametre, save_parametre, set_language
from simulation.loader.interaction import mode_ihm , mode_Vocal
from simulation.logger.logger import display 
from vocal.python.speaker import speak


def menu(new_curseur, piece):
    """
    Affiche le menu principal et gère le choix de mode (vocal ou IHM).
    L'utilisateur peut changer la langue ou quitter avec 'q'.
    """
    set_language()  # Permet de choisir la langue au lancement
    display(get_text('welcome'))
    while True:
        display(get_text('choose_mode'))
        choix = input(get_text('prompt')).strip()
        if choix == '1':
            lancer_mode_vocal(new_curseur, piece)
        elif choix == '2':
            lancer_mode_ihm(new_curseur, piece)
        elif choix.lower() == '3':
            settings()
        elif choix == '4':
            lancer_mode_manuel(new_curseur, piece)
        elif choix == '5': 
            lancer_mode_auto(new_curseur, piece)
        elif choix == '6':
            lancer_mode_image_processing(new_curseur, piece)
        elif choix.lower() == 'q':
            break
        else:
            display(get_text('invalid_choice'))
    display(get_text('goodbye'))
    
def lancer_mode_vocal(new_curseur, piece):
    """
    Gère le fonctionnement du mode vocal.
    les données envoyer par le c snt de la forme
    {"texte": "aller puis tourner ├á droite  degr├⌐s et aller au balle rouge", "commandes": [{"action": "aller", "object": "null", "color": "null"}, {"action": "droite", "valeur": 90}, {"action": "aller", "object": "balle", "color": "rouge"}]
    """
    display(get_text('vocal_mode'))
    
    while True:
        display(get_text('quit_vocal'))
        data_from_C_module = mode_Vocal()
        text = data_from_C_module.get('texte', '')
        if text == '':
            continue
        display(get_text('you_said').format(text))
        print(get_text('command').format(data_from_C_module.get('commandes', [])))
        
        for data in data_from_C_module.get("commandes",[]):
            
            adapted_data = adaptation_donnees(data)
            vocal_reception(new_curseur, adapted_data, piece)
            #verifier si "Stop" a été prononcé 
            commande = data.get('action', '')
            if "stop" in commande.lower():
                display(get_text('end_vocal'))
                return


            

    
    
def lancer_mode_ihm(new_curseur, piece):
    """
    Gère le fonctionnement du mode IHM.
    """
    display(get_text('ihm_mode'))
    while True:
        display(get_text('quit_ihm'))
        
        data = mode_ihm()
        commandes = data.get('commandes', [])
        for data in commandes:
            adapted_data = adaptation_donnees(data)
            vocal_reception(new_curseur, adapted_data, piece)
        quitter = input(get_text('quit_prompt')).strip().lower()
        if quitter == 'o':
            break

    display(get_text('end_ihm'))


def lancer_mode_manuel(new_curseur, piece):
    display(get_text('manuel_mode'))
    while keyboard.is_pressed("esc") == False:
        if keyboard.is_pressed("up"):
            translantion(new_curseur, 20, piece)
        if keyboard.is_pressed("down"):
            translantion(new_curseur, -20, piece)
        if keyboard.is_pressed("left"):
            rotation(new_curseur, 5)
        if keyboard.is_pressed("right"):
            rotation(new_curseur, -5)

def lancer_mode_auto(new_curseur, piece):
    """
    Gère le fonctionnement du mode automatique.
    """
    display(get_text('auto_mode'))

    while keyboard.is_pressed("esc") == False:
        angle = random.randint(-90, 90)
        disctance = random.randint(0, 250)
        rotation(new_curseur, angle)
        translantion(new_curseur, disctance, piece)
        #sleep(0.2)

def lancer_mode_image_processing(new_curseur, piece):
    """
    Gère le fonctionnement du mode de traitement d'image.
    """
    display(get_text('image_processing_mode'))

    display(get_text('quit_image_processing'))
    if input().strip().lower() == 'o':
        return
        
    
def settings():
    """
    Permet de configurer le système.
    """
    choix = ''
    while choix != 'q':
        display(get_text('settings_text').format(load_parametre('debug'), load_parametre('speak')))
        choix = input().strip().lower()

        if choix == '1':
            debug = load_parametre('debug')
            save_parametre('debug', not debug)
        elif choix == '2':
            speak = load_parametre('speak')
            save_parametre('speak', not speak)
        elif choix == '3':
            set_language()
        elif choix == 'q':
            print(get_text('back_to_main'))
            break
        else:
            get_text('invalid_choice')
