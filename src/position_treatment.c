#include "position_treatment.h"
#include <stdio.h>

/**
 * Fonction pour calculer la position d'un objet dans une image.
 * Le calcul repose sur le centre de masse des pixels pertinents.
 */
Position image_position(int** pixel_image, int rows, int cols) {
    int sum_x = 0, sum_y = 0, total_pixels = 0;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (pixel_image[i][j] > PIXEL_THRESHOLD) { // Seuil pour détecter les pixels de l'objet
                sum_x += j;
                sum_y += i;
                total_pixels++;
            }
        }
    }

    Position pos;
    if (total_pixels > 0) {
        pos.x = sum_x / total_pixels;
        pos.y = sum_y / total_pixels;
    } else {
        pos.x = -1; // Position invalide
        pos.y = -1; // Position invalide
    }
    return pos;
}

/**
 * Fonction pour afficher la position détectée de l'objet.
 */
void display_position(Position pos) {
    if (pos.x >= 0 && pos.y >= 0) {
        printf("Object position: (%d, %d)\n", pos.x, pos.y);
    } else {
        printf("Object position: Not detected\n");
    }
}
