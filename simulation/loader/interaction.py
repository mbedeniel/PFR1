import subprocess
import json
import os
from simulation.data.settings import __DEBUG__

def appeler_programme_c(path_programme_c):
    """
    Appelle un programme C externe, exécute le fichier, et parse les données JSON retournées.
    :param path_programme_c: Chemin relatif vers le fichier exécutable du programme C.
    :return: Les données JSON retournées par le programme, ou None en cas d'erreur.
    """
    # Obtenir la racine du projet
    dossier = os.path.dirname(os.path.abspath(__file__))

    racine = os.path.dirname(dossier)
    racine = os.path.dirname(racine)

    relatif_path_file = path_programme_c
    chemin_programme_c = os.path.abspath(os.path.join(racine, relatif_path_file))

    print(f"chemin Programme : {chemin_programme_c}")
    
    try:
        # Exécuter le programme C
        resultat = subprocess.run(
            [chemin_programme_c],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(chemin_programme_c),  # Répertoire de l'exécutable
            check=True
        )
        # Parse le JSON de la sortie du programme C
        data = json.loads(resultat.stdout)
        return data
    except subprocess.CalledProcessError as e:
        if __DEBUG__:
            print("Erreur lors de l'exécution du programme C :", e.stderr)
        return None
    except FileNotFoundError:
        if __DEBUG__:
            print("Le programme C est introuvable. Vérifiez le chemin ou compilez-le.")
        return None
    except json.JSONDecodeError:
        if __DEBUG__:
            print("La sortie du programme C n'est pas un JSON valide.")
        return None

def mode_Vocal():
    """
    Mode vocal : appelle le programme C responsable de la reconnaissance vocale.
    :return: Les données JSON retournées par le programme.
    """
    chemin_programme_c = "vocal/app.exe"
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
        print("Veuillez choisir un mode parmi les suivants :\n")
        print("a : avancer\n")
        print("r : reculer\n")
        print("d : droite\n")
        print("g : gauche\n")
        # Lecture du mode et de la valeur
        print("Saisissez le mode et la valeur (ex : a 15 ou r) : ")
        chemin_programme_c = "vocal/ihm.exe"
        data = appeler_programme_c(chemin_programme_c)
        # Vérifier si la taille de la liste n'est pas nulle
        if data is None or len(data) == 0:
            print("Saisie incorrecte. Veuillez réessayer.")
            return None
        else:
            continuer = False
    return data
