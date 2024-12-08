#include "shape_treatment.h"
#include <stdio.h>
#include <math.h>

/**
 * Fonction pour analyser et détecter la forme d'un objet.
 * Une heuristique simple basée sur la détection des bords est utilisée.
 */
int image_form(int** pixel_image, int rows, int cols) {
    int edges_detected = 0;

    for (int i = 1; i < rows - 1; i++) {
        for (int j = 1; j < cols - 1; j++) {
            if (abs(pixel_image[i][j] - pixel_image[i + 1][j]) > EDGE_THRESHOLD ||
                abs(pixel_image[i][j] - pixel_image[i][j + 1]) > EDGE_THRESHOLD) {
                edges_detected++;
            }
        }
    }

    if (edges_detected > SHAPE_CIRCLE_THRESHOLD) {
        return SHAPE_CIRCLE; // Cercle
    } else if (edges_detected > SHAPE_SQUARE_THRESHOLD) {
        return SHAPE_SQUARE; // Carré
    }
    return SHAPE_UNKNOWN; // Forme non reconnue
}

/**
 * Fonction pour afficher la forme détectée.
 */
void display_shape(int shape_id) {
    switch (shape_id) {
        case SHAPE_CIRCLE:
            printf("Shape detected: Circle\n");
            break;
        case SHAPE_SQUARE:
            printf("Shape detected: Square\n");
            break;
        default:
            printf("Shape detected: Unknown\n");
            break;
    }
}
