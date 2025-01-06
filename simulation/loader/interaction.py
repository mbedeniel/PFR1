from simulation.data.settings import __DEBUG__, MENU_TEXT, LANGUAGES, PROGRAMS , get_text, set_language
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
        #print(f"Erreur : {stderr.decode()}")
        return None
    else:
        #print(f"Sortie : {stdout.decode()}")

        data = json.loads(stdout.decode())
        return data
    """
    try:
        resultat = subprocess.run(
            [commande],
            capture_output=True,  # Capture la sortie standard et les erreurs
            text=True,  # Pour avoir la sortie sous forme de texte
            cwd=os.path.dirname(chemin_programme_c),  # Spécifie le répertoire de travail
            check=True  # Vérifie si le programme a échoué
        )
        print(f"Résultat: {resultat.stdout}")
        data = json.loads(resultat.stdout)
        return data
    except subprocess.CalledProcessError as e:
        if __DEBUG__:
            print(f"calledProcessError: {e}")
        return None
    except FileNotFoundError as e:
        if __DEBUG__:
            print(f"Fichier introuvable: {e}")
        return None
    except json.JSONDecodeError as e:
        if __DEBUG__:
            print(f"Erreur de décodage JSON: {e}")
        return None
"""

def mode_Vocal():
    """
    Mode vocal : appelle le programme C responsable de la reconnaissance vocale.
    :return: Les données JSON retournées par le programme.
    """
    chemin_programme_c = PROGRAMS.get('vocal').get("path")
    print(f"Chemin programme C vocal: {chemin_programme_c}")
    data = appeler_programme_c(chemin_programme_c)
    return data

def mode_ihm():
    """
    Mode IHM : permet de choisir une option et retourne les données JSON associées.
    :return: Les données JSON retournées par le programme.
    """
    continuer = True
    while continuer:
        # Présentation du menu
        print(get_text('presentation_ihm'))
        chemin_programme_c = PROGRAMS.get('ihm').get("path")
        data = appeler_programme_c(chemin_programme_c)
        print(f"programme C IHM: {chemin_programme_c}")
        # Vérifier si la taille de la liste n'est pas nulle
        if data is None or len(data) == 0:
            print(get_text('invalid_input'))
            return None
        else:
            continuer = False
    return data