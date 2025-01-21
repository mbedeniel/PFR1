import os
import json

# Initialisation des variables globales
__DEBUG__ = True
__SPEAK__ = False
__DISPLAY__ = True

current_language = 'fr'
dossier = os.path.dirname(os.path.abspath(__file__))
__PATH_SETTINGS_FILE__ = os.path.join(dossier, "settings.json")
__PATH_LOG_FILE__ = os.path.join(dossier, "log.txt")
LANGUAGES = {
    'fr': 'Français',
    'en': 'English'
}

MENU_TEXT = {
    'fr': {
        'welcome': "Bienvenue dans le menu principal !",
        'choose_mode': "\nVeuillez choisir un mode parmi les suivants :\n1 : Mode Vocal\n2 : Mode IHM\n3 : Configurations\n4 : Mode Manuel\n5 : Mode Auto\n6 : Mode Traitement d'image\nq : Quitter",
        'prompt': "Entrez votre choix : ",
        'invalid_choice': "Choix invalide. Veuillez réessayer.",
        'goodbye': "À bientôt !",
        'vocal_mode': "__Mode Vocal__",
        'quit_vocal': "Dites 'Stop' pour quitter le mode vocal. Je vous écoute...",
        'end_vocal': "Fin du mode vocal.",
        'ihm_mode': "__Mode IHM__",
        'auto_mode': "__Mode Auto__",
        'image_processing_mode': "__Mode Traitement d'image__",
        'quit_image_processing': "Appuyez sur 'o' pour quitter le mode traitement d'image.",
        'quit_auto': "Appuyez sur 'Échap' pour quitter le mode auto.",
        'quit_ihm': "Appuyez sur 'o' pour quitter le mode IHM.",
        'end_ihm': "Fin du mode IHM.",
        'quit_prompt': "Voulez-vous vraiment quitter ? (o/n) : ",
        'presentation_ihm': """Veuillez choisir un mode parmi les suivants :
            a : avancer
            r : reculer
            d : droite
            g : gauche
            Saisissez le mode et la valeur (ex : a 15 ou r) : """,
        'manuel_mode': "__Mode Manuel__\n\tAppuyer sur les flèches pour déplacer le robot.\n\tAppuyer sur 'échape' pour quitter.",
        'invalid_input':"Entrée invalide. Veuillez réessayer.",
        'error': "Une erreur est survenue : {0}",
        'not_understood': "Je n'ai pas compris votre demande. Veuillez réessayer.",
        'create_config': "Création du fichier de configuration par défaut...",
        'success_config': "Paramètres sauvegardés avec succès.",
        'file_not_found': "Fichier de configuration introuvable. Création d'un fichier par défaut...",
        
        'set_language': "Actuellement, la langue est réglée sur {0}.\nChoisissez une langue :\n\tEntrez le code de la langue 'en' ou 'fr' (par défaut 'fr') : ",
        'error_set_language': "Entrée non reconnue. La langue est conservée en {0}.",
        'success_set_language': "Langue changée avec succès.",
        #interactions
        'error_interactions': "Erreur lors de l'appel du programme C. {0}",
        #menu
        'you_said': "vous avez dit : {0}",
        'command': "Commandes associées : {0}",
        'settings_text': "\n___ Configuration du système ___\n1 : Activer/Désactiver le mode DEBUG (actuel : {0})\n2 : Activer/Désactiver le mode SPEAK (actuel : {1})\n3 : Changer la langue actuelle\nq : Retour au menu principal\n\tEntrez votre choix : ",
        "back_to_main": "Retour au menu principal...",
        'invalid_choice': "Choix invalide. Veuillez réessayer.",
        #detection_collision
        "invalid_form":"Erreur : la forme de L'objet {0} n'est pas reconnue ",
        #mouvement
        'not_in_piece':"Déplacement impossible. Le Robot risque de percuter la paroi de la pièce.",
        'invalid_movement':"Mouvement non reconnu.",
        'invalid_rotation':"Rotation non reconnue.",
        'mission_in_progress':"Mission en cours d'execution",    
        'move_to_object':"Deplacement vers l'objet de type {0} et de couleur {1}",
        'mission_accomplished':"Mission accomplie.",
        'Object_not_found':"Erreur: Obstacle de type {0} et de couleur {1} non trouvé.",
        'cancel_mission':"Mission annulée.",
        #navigation
        'no_ouverture':"Erreur : La pièce ne contient pas d'ouverture.",
        'no_sortie':"Erreur : le point de sortie correctement n'a pas été fourni.",
        'destination_outside':"Erreur: la destination est en dehors de la pièce.",
        'mouving_robot':"Déplacement du Robot ....",
        'critical_obstacle':"Obstacle critique détecté.",
        'destination_in_obstacle':"La destination est dans l'obstacle.",
        'impossible_to_move':"Impossible de se déplacer.",
        'contournement_obstacle':"Contournement de l'obstacle {0} ...",
        'end_contournement':"Fin du contournement de l'obstacle.",
        "go_to_destination":"Déplacement du Robot vers la destination ....",
        #drawing
        'obstacle_outside':"Erreur : l'obstacle {0} est en dehors de la pièce.",
        'invalid_coin':"Erreur : le coin {0} de l'ouverture {1} est invalide.",
        },
    'en': {
        'welcome': "Welcome to the main menu!",
        'choose_mode': "\nPlease choose a mode from the following:\n1: Vocal Mode\n2: IHM Mode\n3: Settings\n4: Manual Mode\n5: Auto Mode\n6: Image Processing Mode\nq: Quit",
        'invalid_choice': "Invalid choice. Please try again.",
        'goodbye': "See you soon!",
        'vocal_mode': "__Vocal Mode__",
        'quit_vocal': "Say 'Stop' to exit vocal mode. I'm listening...",
        'end_vocal': "Exiting vocal mode.",
        'ihm_mode': "__IHM Mode__",
        'auto_mode': "__Auto Mode__",
        'image_processing_mode': "__Image Processing Mode__",
        'quit_image_processing': "Press 'o' to exit image processing mode.",
        'quit_auto': "Press 'Escape' to exit auto mode.",
        'quit_ihm': "Press 'o' to exit IHM mode.",
        'end_ihm': "Exiting IHM mode.",
        'quit_prompt': "Are you sure you want to exit? (o/n): ",
        'presentation_ihm': """Please choose a mode from the following:
            a: forward
            r: backward
            d: right
            g: left
            Enter the mode and the value (ex: a 15 or r): """,
        'manuel_mode': "__Manual Mode__\n\tUse the arrow keys to move the robot.\n\tPress 'escape' to exit.",
        'invalid_input':"Invalid input. Please try again.",
        'error': "An error occurred: {0}",
        'not_understood': "I did not understand your request. Please try again.",
        'create_config': "Creating default configuration file...",
        'success_config': "Settings saved successfully.",
        'file_not_found': "Configuration file not found. Creating a default file...",
        'set_language': "Currently, the language is set to {0}.\nChoose a language:\n\tEnter the language code 'en' or 'fr' (default 'en'): ",
        'error_set_language': "Unrecognized input. Language is kept in {0}.",
        'success_set_language': "Language changed successfully.",
        #interactions
        'error_interactions': "Error when calling the C program. {0}",
        #menu
        'you_said': "you said: {0}",
        'command': "Associated commands: {0}",
        'settings_text': "\n___ System Configuration ___\n1: Enable/Disable DEBUG mode (current: {0})\n2: Enable/Disable SPEAK mode (current: {1})\n3: Change the current language\nq: Back to main menu\n\tEnter your choice: ",
        "back_to_main": "Back to main menu...",
        'invalid_choice': "Invalid choice. Please try again.",
        #detection_collision
        "invalid_form":"Error: The shape of the object {0} is not recognized",
        #mouvement
        'not_in_piece':"Impossible to move. The Robot may hit the room's wall.",
        'invalid_movement':"Movement not recognized.",
        'invalid_rotation':"Rotation not recognized.",
        'mission_in_progress':"Mission in progress",
        'move_to_object':"Moving to the object of type {0} and color {1}",
        'mission_accomplished':"Mission accomplished.",
        'Object_not_found':"Error: Obstacle of type {0} and color {1} not found.",
        'cancel_mission':"Mission canceled.",
        #navigation
        'no_ouverture':"Error: The room does not contain an opening.",
        'no_sortie':"Error: the correct exit point was not provided.",
        'destination_outside':"Error: the destination is outside the room.",
        'mouving_robot':"Robot moving ....",
        'critical_obstacle':"Critical obstacle detected.",
        'destination_in_obstacle':"The destination is in the obstacle.",
        'impossible_to_move':"Impossible to move.",
        'contournement_obstacle':"Bypassing obstacle {0} ...",
        'end_contournement':"End of obstacle bypass.",
        "go_to_destination":"Robot moving to destination ....",
        #drawing
        'obstacle_outside':"Error: obstacle {0} is outside the room.",
        'invalid_coin':"Error: corner {0} of opening {1} is invalid.",
        
        }
}

PROGRAMS = {
    'vocal': {'path': "vocal/app.exe", 'description': "Programme vocal"},
    'ihm': {'path': "vocal/ihm.exe", 'description': "Interface utilisateur"},
    'image_processing' : {'path' : "imageProcessing\main_test_image.exe", 'description':"Image Processing"}
}

def init_settings_file():
    """
    Sauvegarde les paramètres dans un fichier de configuration.
    """
    data = {
        'debug': __DEBUG__,
        'speak': __SPEAK__,
        'display': __DISPLAY__,
        'current_language': current_language,
        'LANGUAGES': LANGUAGES,
        'MENU_TEXT': MENU_TEXT,
        'PROGRAMS': PROGRAMS
    }
    with open(__PATH_SETTINGS_FILE__, "w") as f:
        json.dump(data, f, indent=4)
    print(get_text('create_config'))

def load_all_parameters():
    """
    Charge les paramètres depuis un fichier. Recrée le fichier par défaut si le chargement échoue.
    """
    if not os.path.exists(__PATH_SETTINGS_FILE__):
        print(get_text('file_not_found'))
        init_settings_file()
    try:
        with open(__PATH_SETTINGS_FILE__, "r") as f:
            data = json.load(f)
        global __DEBUG__, __SPEAK__, __DISPLAY__, current_language, LANGUAGES, MENU_TEXT, PROGRAMS
        __DEBUG__ = data.get('debug', __DEBUG__)
        __SPEAK__ = data.get('speak', __SPEAK__)
        __DISPLAY__ = data.get('display', __DISPLAY__)
        current_language = data.get('current_language', current_language)
        LANGUAGES = data.get('LANGUAGES', LANGUAGES)
        MENU_TEXT = data.get('MENU_TEXT', MENU_TEXT)
        PROGRAMS = data.get('PROGRAMS', PROGRAMS)
        print(get_text('success_config'))
    except Exception as e:
        print(get_text('error').format(e))
        init_settings_file()

def set_language():
    """
    Permet à l'utilisateur de choisir la langue de l'interface.
    """
    print(get_text('set_language').format(load_parametre('current_language'), ', '.join(LANGUAGES.keys())))
    for code, lang in load_parametre('LANGUAGES').items():
        print(f"{code} : {lang}")
    choix = input().strip().lower()
    if choix in LANGUAGES:
        save_parametre('current_language', choix)
        print(get_text('success_set_language'))
    else:
        print(get_text('error_set_language').format(load_parametre('current_language')))

def get_text(key):
    """
    Récupère le texte dans la langue actuelle.
    """
    langue  = load_parametre('current_language')
    menu_text = load_parametre('MENU_TEXT')
    return menu_text[langue].get(key, f"Texte introuvable pour la clé '{key}'.")


def load_parametre(key):
    if os.path.exists(__PATH_SETTINGS_FILE__) == False:
        init_settings_file()
    with open(__PATH_SETTINGS_FILE__, "r") as f:
        data = json.load(f)
        return data[key]
def save_parametre(key, value):
    if os.path.exists(__PATH_SETTINGS_FILE__) == False:
        init_settings_file()
        
    with open(__PATH_SETTINGS_FILE__, "r") as f:
        data = json.load(f)
        data[key] = value
    with open(__PATH_SETTINGS_FILE__, "w") as f:
        json.dump(data, f, indent=4)
    print(get_text('success_set_language'))

# Point d'entrée principal
if __name__ == "__main__":
    load_all_parameters()
    print(get_text('welcome'))
    save_parametre('current_language', 'en')
    print(get_text('choose_mode'))
    save_parametre('current_language', 'fr')
    print(get_text('goodbye'))
