import subprocess
import json
import os
import os
import subprocess
import json

def appeler_programme_c(path_programme_c):
    # Obtenir la racine du projet
    dossier = os.path.dirname(os.path.abspath(__file__))
    racine = os.path.dirname(dossier)

    relatif_path_file = path_programme_c
    chemin_programme_c = os.path.abspath(os.path.join(racine, relatif_path_file))
    
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
        print("Erreur lors de l'exécution du programme C :", e.stderr)
        return None
    except FileNotFoundError:
        print("Le programme C est introuvable. Vérifiez le chemin ou compilez-le.")
        return None
    except json.JSONDecodeError:
        print("La sortie du programme C n'est pas un JSON valide.")
        return None

def Mode_Vocal():
    chemin_programme_c = "vocal/app.exe"
    data = appeler_programme_c(chemin_programme_c)
    return data
def mode_ihm():
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
        #verifier si la taille de la liste n est pas nulle
        if len(data) == 0:
            print("Saisie incorrecte. Veuillez réessayer.")
            continuer = True
        else:
            continuer = False
    return data
