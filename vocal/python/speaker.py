import pyttsx3

def speak(text, language="fr"):
    """Convertir du texte en parole avec détection automatique des voix."""
    # Initialiser le moteur
    engine = pyttsx3.init()

    # Obtenir toutes les voix disponibles
    voices = engine.getProperty('voices')
    selected_voice = None

    # Parcourir les voix pour trouver celle qui correspond à la langue
    for voice in voices:
        if language in voice.id.lower():  # Vérifie si la langue est dans l'ID de la voix
            selected_voice = voice
            break

    if selected_voice:
        engine.setProperty('voice', selected_voice.id)
    else:
        print(f"Aucune voix trouvée pour la langue '{language}'. Utilisation de la voix par défaut.")

    # Lire le texte
    engine.say(text)
    engine.runAndWait()





