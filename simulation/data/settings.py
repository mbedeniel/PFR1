# settings.py

__DEBUG__ = True

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
    }
}


current_language = 'fr'  # Par défaut, la langue est le français

def set_language():
    """
    Permet à l'utilisateur de choisir la langue de l'interface.
    """
    global current_language
    print("\nChoisissez une langue :")
    for code, lang in LANGUAGES.items():
        print(f"{code} : {lang}")
    choix = input("\nEntrez le code de la langue (par défaut 'fr') : ").strip().lower()
    if choix in LANGUAGES:
        current_language = choix
    else:
        print("Langue non reconnue, le français est conservé par défaut.")

def get_text(key):
    """
    Récupère le texte dans la langue actuelle.
    """
    return MENU_TEXT[current_language].get(key, "Texte manquant")
