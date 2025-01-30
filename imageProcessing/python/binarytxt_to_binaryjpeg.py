import numpy as np
import cv2

pathList = ["img_1"]


for path in pathList:
    # Lire le fichier texte
    with open(path+".txt", "r") as file:
        lines = file.readlines()

    # Extraire la taille de l'image
    height, width = map(int, lines[0].strip().split())

    # Initialiser les trois canaux
    B = []
    Z = np.zeros((height, width), dtype=np.uint8)
    A = np.array((height, width))

    # Lire le canal 
    for i in range(1, height + 1): 
        B.append(list(map(int, lines[i].strip().split())))

    # Convertir les listes en matrices numpy
    print(len(B[0]))
    B = np.array(B, dtype=np.uint8)

    # Empiler les trois canaux pour créer l'image RGB
    image = np.stack((B, B, B), axis=-1)

    image *= 255

    # Affichage de l'image avec OpenCV
    cv2.imwrite(path+".jpeg", image)

    print("Fichier texte généré avec succès.")
