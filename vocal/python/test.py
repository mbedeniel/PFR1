import speech_recognition as sr


r = sr.Recognizer()
mic = sr.Microphone()

# Demander à l'utilisateur de choisir une langue de commande vocale
print("Veuillez choisir une langue  : " )
print("1. Français")
print("2. Anglais")
choix = input("Entrez 1 pour le français ou 2 pour l'anglais : ")


if choix == "1":
    language = "fr-FR"
    language_name = "Français"

elif choix == "2":
    language = "en-US"
    language_name = "Anglais"

else:
    print("Choix invalide. Par défaut, le français sera utilisé.")
    language = "fr-FR"
    language_name = "Français"


with mic as source:

    audio_data = r.listen(source)

result = ''
try:
    result = r.recognize_google(audio_data, language=language)
    print(f"Texte reconnu ({language_name}): {result}")
except Exception as e:
    print(f"Texte non reconnu en {language_name}.")
    
print(result)


