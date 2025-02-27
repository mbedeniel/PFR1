
from simulation.data.settings import load_parametre
import speech_recognition as sr
#pip install SpeechRecognition
# pour une reconnaissance de la parole en français

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    #r.adjust_for_ambient_noise(source) # ajustement du bruit ambiant pour une meilleure reconnaissance
    audio_data = r.listen(source , timeout=15 , phrase_time_limit=40 ) # enregistrement de la voix pendant 15 seconde
try:
    if load_parametre('current_language') == 'en':
        result = r.recognize_google(audio_data , language="en-US").lower()
    else:
        result = r.recognize_google(audio_data, language="fr-FR").lower()
    #result = r.recognize_google(audio_data, language="fr-FR")
except Exception as e:
    result = ''


print(result,end='')