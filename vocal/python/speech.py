
#from simulation.data.settings import current_language
import speech_recognition as sr
#pip install SpeechRecognition
# pour une reconnaissance de la parole en français

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio_data = r.listen(source)

try:
    """if current_language == "en":
        result = r.recognize_google(audio_data)
    else:
        result = r.recognize_google(audio_data, language="fr-FR")"""
    result = r.recognize_google(audio_data, language="fr-FR")
except Exception as e:
    result = ''

print(result)