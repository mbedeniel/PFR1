import os
from vocal.python.speaker import speak

# settings.py


__DEBUG__ = True
__SPEAK__ = True

current_language = 'fr'  # Par défaut, la langue est le français


#recuperer le dossier du fichier courant

dossier = os.path.dirname(os.path.abspath(__file__))
__PATH_SETIINGS_FILE__ = os.path.abspath(os.path.join(dossier,"settings.json"))

LANGUAGES = {
    'fr': 'Français',
    'en': 'English'
}

# Textes du menu en plusieurs langues
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

# Configuration pour les exécutables externes
PROGRAMS = {
    'vocal': {
        'path': "vocal/app.exe",  # Chemin vers le programme vocal
        'description': "Programme C pour la reconnaissance vocale"
    },
    'ihm': {
        'path': "vocal/ihm.exe",  # Chemin vers le programme IHM
        'description': "Programme C pour l'interface utilisateur"
    }
}

def save_all_parameters( ):
    """
    Sauvegarde les paramètres dans un fichier.
    """
    data = {
        'debug' : __DEBUG__ ,
        'current_language': current_language ,
        'LANGUAGES': LANGUAGES,
        'MENU_TEXT': MENU_TEXT,
        'PROGRAMS': PROGRAMS,

    }
    import json
    with open(__PATH_SETIINGS_FILE__, "w") as f:
        json.dump(data, f, indent=4)
        print(" parametres ont ete sauvegardes avec succes")
        if __SPEAK__:
            speak(" parametres ont ete sauvegardes avec succes" , current_language)


def load_all_parameters( ):
    """
    Charge les paramètres depuis un fichier.
    """
    import json
    #initialiser le fichier de paramettre s'il n'existe pas
    init_settings_files()

    with open(__PATH_SETIINGS_FILE__, "r") as f:
        data = json.load(f)
        global __DEBUG__ , current_language , LANGUAGES , MENU_TEXT , PROGRAMS
        __DEBUG__ = data['debug']
        current_language = data['current_language']
        LANGUAGES = data['LANGUAGES']
        MENU_TEXT = data['MENU_TEXT']
        PROGRAMS = data['PROGRAMS']
    
def init_settings_files():
    """
    Initialise les fichiers de configurations.
    """
    #verifiers si le fichier de configurations n'existe pas
    import os
    if os.path.exists(__PATH_SETIINGS_FILE__) == False:
        save_all_parameters()




def set_language():
    """
    Permet à l'utilisateur de choisir la langue de l'interface.
    """
    global current_language
    print("\nChoisissez une langue :")
    if __SPEAK__:
        speak("Choisissez une langue." , current_language)
    for code, lang in LANGUAGES.items():
        print(f"{code} : {lang}")
    choix = input("\nEntrez le code de la langue (par défaut 'fr') : ").strip().lower()
    if choix in LANGUAGES:
        current_language = choix
    else:
        print("Langue non reconnue, le français est conservé par défaut.")
        if __SPEAK__:
            speak("Langue non reconnue, le français est conservé par défaut." , current_language)

def get_text(key):
    """
    Récupère le texte dans la langue actuelle.
    """
    return MENU_TEXT[current_language].get(key, "Texte manquant")




