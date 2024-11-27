import speech_recognition as sr
import pyaudio
from gtts import gTTS


r = sr.Recognizer()
micro = sr.Microphone()
with micro as source:
 audio_data = r.listen(source)
 
result = r.recognize_google(audio_data, language="fr-FR")
# pour une reconnaissance de la parole en anglais
# result = r.recognize_google(audio_data, language="en-EN")
print (result)