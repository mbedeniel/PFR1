import speech_recognition as sr
# pour une reconnaissance de la parole en français

r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio_data = r.listen(source)

try:
    result = r.recognize_google(audio_data, language="fr-FR")
except Exception as e:
    result = ""

print(result)