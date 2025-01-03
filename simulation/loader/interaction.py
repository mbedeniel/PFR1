from simulation.data.settings import __DEBUG__, MENU_TEXT, LANGUAGES, PROGRAMS , get_text, set_language


def appeler_programme_c(path_programme_c):
    """
    Appelle un programme C externe, exécute le fichier, et parse les données JSON retournées.
    :param path_programme_c: Chemin relatif vers le fichier exécutable du programme C.
    :return: Les données JSON retournées par le programme, ou None en cas d'erreur.
    """
    import subprocess
    import json
    import os

    dossier = os.path.dirname(os.path.abspath(__file__))
    racine = os.path.dirname(os.path.dirname(dossier))
    chemin_programme_c = os.path.abspath(os.path.join(racine, path_programme_c))

    try:
        resultat = subprocess.run(
            [chemin_programme_c],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(chemin_programme_c),
            check=True
        )
        data = json.loads(resultat.stdout)
        return data
    except subprocess.CalledProcessError as e:
        if __DEBUG__:
            print(get_text('error_execution'), e.stderr)
        return None
    except FileNotFoundError:
        if __DEBUG__:
            print(get_text('error_not_found'))
        return None
    except json.JSONDecodeError:
        if __DEBUG__:
            print(get_text('error_json'))
        return None
    

def mode_Vocal():
    """
    Mode vocal : appelle le programme C responsable de la reconnaissance vocale.
    :return: Les données JSON retournées par le programme.
    """
    chemin_programme_c = PROGRAMS.get('vocal').get("path")
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
        # Vérifier si la taille de la liste n'est pas nulle
        if data is None or len(data) == 0:
            print(get_text('invalid_input'))
            return None
        else:
            continuer = False
    return data