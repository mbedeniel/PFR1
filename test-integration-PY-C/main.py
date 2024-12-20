import subprocess
import json

def appeler_programme_c():
    # Spécifiez le chemin vers l'exécutable C
    chemin_programme_c = "./test"

    try:
        # Exécuter le programme C
        resultat = subprocess.run(
            [chemin_programme_c],
            capture_output=True,
            text=True,
            check=True  # Lever une exception si le programme C retourne une erreur
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

if __name__ == "__main__":
    data = appeler_programme_c()
    if data:
        print("Données reçues depuis le programme C :")
        print(f"ID      : {data['id']}")
        print(f"Nom     : {data['name']}")
        print(f"Valeur  : {data['value']}")
