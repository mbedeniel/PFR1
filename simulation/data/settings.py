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
        'choose_mode': "\nVeuillez choisir un mode parmi les suivants :\n1 : Mode Vocal\n2 : Mode IHM\nl : Changer de langue\nq : Quitter",
        'prompt': "Entrez votre choix : ",
        'invalid_choice': "Choix invalide. Veuillez réessayer.",
        'goodbye': "À bientôt !",
        'vocal_mode': "__Mode Vocal__",
        'quit_vocal': "Appuyez sur 'o' pour quitter le mode vocal.",
        'end_vocal': "Fin du mode vocal.",
        'ihm_mode': "__Mode IHM__",
        'quit_ihm': "Appuyez sur 'o' pour quitter le mode IHM.",
        'end_ihm': "Fin du mode IHM.",
        'quit_prompt': "Voulez-vous vraiment quitter ? (o/n) : ",
        'presentation_ihm': """Veuillez choisir un mode parmi les suivants :
            a : avancer
            r : reculer
            d : droite
            g : gauche
            Saisissez le mode et la valeur (ex : a 15 ou r) : """,
        'invalid_input':"Entrée invalide. Veuillez réessayer.",
   
    },
    'en': {
        'welcome': "Welcome to the main menu!",
        'choose_mode': "\nPlease choose a mode from the following:\n1: Vocal Mode\n2: IHM Mode\nl: Change language\nq: Quit",
        'prompt': "Enter your choice: ",
        'invalid_choice': "Invalid choice. Please try again.",
        'goodbye': "See you soon!",
        'vocal_mode': "__Vocal Mode__",
        'quit_vocal': "Press 'o' to exit vocal mode.",
        'end_vocal': "Exiting vocal mode.",
        'ihm_mode': "__IHM Mode__",
        'quit_ihm': "Press 'o' to exit IHM mode.",
        'end_ihm': "Exiting IHM mode.",
        'quit_prompt': "Are you sure you want to exit? (o/n): ",
        'presentation_ihm': """Please choose a mode from the following:
            a: forward
            r: backward
            d: right
            g: left
            Enter the mode and the value (ex: a 15 or r): """,
        'invalid_input':"Invalid input. Please try again.",
    }
}

PROGRAMS = {
    'vocal': {'path': "vocal/app.exe", 'description': "Programme vocal"},
    'ihm': {'path': "vocal/ihm.exe", 'description': "Interface utilisateur"}
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
    print("Paramètres sauvegardés avec succès.")

def load_all_parameters():
    """
    Charge les paramètres depuis un fichier. Recrée le fichier par défaut si le chargement échoue.
    """
    if not os.path.exists(__PATH_SETTINGS_FILE__):
        print("Fichier de configuration introuvable. Création d'un fichier par défaut...")
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
        print("Paramètres chargés avec succès.")
    except Exception as e:
        print(f"Erreur lors du chargement du fichier de configuration : {e}")
        print("Recréation d'un fichier de configuration par défaut...")
        init_settings_file()

def set_language():
    """
    Permet à l'utilisateur de choisir la langue de l'interface.
    """
    print(f"Actuellement, la langue est réglée sur {load_parametre('current_language')}.")
    print("Choisissez une langue :")
    for code, lang in load_parametre('LANGUAGES').items():
        print(f"{code} : {lang}")
    choix = input("\nEntrez le code de la langue 'en' ou 'fr'(par défaut 'fr') : ").strip().lower()
    if choix in LANGUAGES:
        save_parametre('current_language', choix)
        print(f"Langue changée en {load_parametre('current_language')}")
    else:
        print(f"Entrée non reconnue. La langue est conservée en {load_parametre('current_language')}.")

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
    print("Paramètre sauvegardé avec succès.")

# Point d'entrée principal
if __name__ == "__main__":
    load_all_parameters()
    print(get_text('welcome'))
    save_parametre('current_language', 'en')
    print(get_text('choose_mode'))
    save_parametre('current_language', 'fr')
    print(get_text('goodbye'))
