import sys
import cv2


def ajout_croix_image(image_path, x_center, y_center, taille_croix = 1 ):
    #.txt to .jpeg
    image_path = image_path[:-3] + "jpeg"
    
    # Ouvre l'image
    img = cv2.imread(image_path)

    if img is None:
        print("Erreur : l'image n'a pas pu être chargée.")
        return

    # Récupère les dimensions de l'image
    hauteur, largeur = img.shape[:2]

    # Faire une croix 20 x 20 autour du pixel central
    for x in range(x_center - 10  * taille_croix , x_center + 10 * taille_croix + 1 ):
        if 0 <= x < largeur:  # Validation des indices
            img[y_center, x] = (255, 0, 250)  # Magenta
        
    for y in range(y_center - 10  * taille_croix , y_center + 10 * taille_croix + 1 ):
        if 0 <= y < hauteur:  # Validation des indices
            img[y, x_center] = (255, 0, 250)  # Magenta

    # Affiche l'image
    cv2.imwrite(image_path, img)






if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python script.py <image_path> <x_center> <y_center>")
        sys.exit(1)

    image_path = sys.argv[1]
    x_center = int(sys.argv[2])
    y_center = int(sys.argv[3])
    
    
    ajout_croix_image(image_path, x_center, y_center)
