import cv2
import numpy as np

def compress_image(img, max_size=600):
    """Compresse l'image jusqu'à ce que la hauteur et la largeur soient toutes deux < max_size."""
    height, width, _ = img.shape
    while height + width > max_size*2:
        # Diviser les dimensions par 2
        new_width = max(width // 4, 1)  # Éviter des dimensions nulles
        new_height = max(height // 4, 1)
        img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
        height, width, _ = img.shape
    return img

def extract_channels(img):
    """Extrait les canaux B, G, R d'une image."""
    height, width, _ = img.shape
    B = [img[i, j, 0] for i in range(height) for j in range(width)]
    G = [img[i, j, 1] for i in range(height) for j in range(width)]
    R = [img[i, j, 2] for i in range(height) for j in range(width)]
    return B, G, R, height, width

for img_idx in range(8, 20):
    img = cv2.imread(f"img_{img_idx}.png")
    if img is None:
        print(f"Image img_{img_idx}.png introuvable ou corrompue. Passons à l'image suivante.")
        continue

    # Compresser l'image si nécessaire
    img = compress_image(img, max_size=600)

    # Extraction des canaux
    B, G, R, height, width = extract_channels(img)

    # Convertir les listes en numpy arrays
    try:
        B = np.array(B, dtype=np.uint8).reshape(height, width)
        G = np.array(G, dtype=np.uint8).reshape(height, width)
        R = np.array(R, dtype=np.uint8).reshape(height, width)
    except ValueError as e:
        print(f"Erreur de reshape pour img_{img_idx}.png : {e}")
        print(f"Taille de B : {len(B)}, Dimensions : {height}x{width}")
        continue

    # Écriture dans le fichier texte
    with open(f"img_{img_idx}.txt", "w") as file:
        file.write(f"{height} {width * 2}\n")
        for i in range(height):
            file.write(" ".join(map(str, B[i])) + "\n")
        for i in range(height):
            file.write(" ".join(map(str, G[i])) + "\n")
        for i in range(height):
            file.write(" ".join(map(str, R[i])) + "\n")

    print(f"Fichier texte img_{img_idx}.txt généré avec succès.")
