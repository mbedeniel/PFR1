from simulation.data.settings import get_text , load_parametre
from simulation.logger.logger import display 
import subprocess
import json
import os


def appeler_programme_c(path_programme_c):
    """
    Appelle un programme C externe, exécute le fichier, et parse les données JSON retournées.
    :param path_programme_c: Chemin relatif vers le fichier exécutable du programme C.
    :return: Les données JSON retournées par le programme, ou None en cas d'erreur.
    """
    
    dossier = os.path.dirname(os.path.abspath(__file__))
    racine = os.path.dirname(os.path.dirname(dossier))
    chemin_programme_c = os.path.abspath(os.path.join(racine, path_programme_c))

    process = subprocess.Popen([chemin_programme_c], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        sortie = stderr.decode()
        print(sortie)
        display(get_text('not_understood'))
        return {}
    else:
        #decider de l'encodage avec le plus approprié
        data = {}
        try:
           sortie = stdout.decode("utf-8").replace('\r', '').replace('\n', '')
            
        except UnicodeDecodeError:
            sortie = stdout.decode("latin1").replace('\r', '').replace('\n', '')
            
        except Exception as e:
            display(get_text('error_interactions').format(e))
            return {}
        
        
        try:
            data = json.loads(sortie)
        except json.JSONDecodeError:
            print(sortie)
            return {}
        
        return data


def mode_Vocal():
    """
    Mode vocal : appelle le programme C responsable de la reconnaissance vocale.
    :return: Les données JSON retournées par le programme.
    """
    programm = load_parametre('PROGRAMS')
    chemin_programme_c = programm.get('vocal').get("path")
    data = appeler_programme_c(chemin_programme_c)
    return data

def mode_ihm():
    """
    Mode IHM : permet de choisir une option (avancer , reculer , tourner ) et retourne les données JSON associées.
    :return: Les données JSON retournées par le programme.
    """
    continuer = True
    while continuer:
        # Présentation du menu
        display(get_text('presentation_ihm'))
        programm = load_parametre('PROGRAMS')
        chemin_programme_c = programm.get('ihm').get("path")
        data = appeler_programme_c(chemin_programme_c)
        # Vérifier si la taille de la liste n'est pas nulle
        if data is None or len(data) == 0:
            display(get_text('invalid_input'))
            return None
        else:
            continuer = False
    return data

def mode_image_processing():
    """
    Mode de traitement d'image : appelle le programme C responsable du traitement d'image.
    :return: Les données JSON retournées par le programme.
    """
    programm = load_parametre('PROGRAMS')
    chemin_programme_c = programm.get('image_processing').get("path")
    data = appeler_programme_c(chemin_programme_c)
    return data