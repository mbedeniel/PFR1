from simulation.data.settings import __PATH_LOG_FILE__ , load_parametre
from vocal.python.speaker import speak

def display(message):
    if load_parametre('display'):
        print(message)
    if load_parametre('speak'):
        language = load_parametre('current_language')
        speak(message , language)
    if load_parametre('debug'):
        log(message)


def log(message):
    with open(__PATH_LOG_FILE__, "a") as f:
        f.write(message + "\n")