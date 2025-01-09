from simulation.data.settings import __PATH_LOG_FILE__, __DEBUG__ , __SPEAK__ , __DISPLAY__ 
from vocal.python.speaker import speak

def display(message):
    if __DISPLAY__:
        print(message)
    if __SPEAK__:
        speak(message)
    if __DEBUG__:
        log(message)


def log(message):
    with open(__PATH_LOG_FILE__, "a") as f:
        f.write(message + "\n")