from simulation.navigation.mouvement import vocal_reception, adaptation_donnees
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
        display(f"vous avez dit : {text}")
        print(f"\tCommandes associées : {data_from_C_module.get('commandes', [])}")
        for data in data_from_C_module.get("commandes",[]):
            
            display(data.get('texte', ''))
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
        adapted_data = adaptation_donnees(data)
        vocal_reception(new_curseur, adapted_data, piece)
        sleep(2)
        quitter = input(get_text('quit_prompt')).strip().lower()
        if quitter == 'o':
            break

    display(get_text('end_ihm'))
    
def settings():
    """
    Permet de configurer le système.
    """
    choix = ''
    while choix != 'q':
        print("\n=== Configuration du système ===")
        print("1 : Activer/Désactiver le mode DEBUG (actuel : {})".format("Activé" if load_parametre('debug') else "Désactivé"))
        print("2 : Activer/Désactiver le mode SPEAK (actuel : {})".format("Activé" if load_parametre('speak') else "Désactivé"))
        print("3 : Changer la langue actuelle")
        print("q : Retour au menu principal")

        choix = input("Entrez votre choix : ").strip().lower()

        if choix == '1':
            debug = load_parametre('debug')
            print(f"AVDEBUG : {debug}")
            save_parametre('debug', not debug)
        elif choix == '2':
            speak = load_parametre('speak')
            save_parametre('speak', not speak)
        elif choix == '3':
            set_language()
        elif choix == 'q':
            print("Retour au menu principal...")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
