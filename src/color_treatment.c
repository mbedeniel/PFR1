#include "color_treatment.h"
#include <stdio.h>

/**
 * Fonction pour analyser et classifier la couleur d'un pixel.
 * Les valeurs RGB sont comparées pour identifier la couleur.
 */
int image_color(int red, int green, int blue) {
    if (red > 200 && green < 100 && blue < 100) {
        return COLOR_RED; // Rouge
    } else if (green > 200 && red < 100 && blue < 100) {
        return COLOR_GREEN; // Vert
    } else if (blue > 200 && red < 100 && green < 100) {
        return COLOR_BLUE; // Bleu
    }
    return COLOR_UNKNOWN; // Couleur non reconnue
}

/**
 * Fonction pour afficher la couleur détectée.
 */
void display_color(int color_id) {
    switch (color_id) {
        case COLOR_RED:
            printf("Color detected: Red\n");
            break;
        case COLOR_GREEN:
            printf("Color detected: Green\n");
            break;
        case COLOR_BLUE:
            printf("Color detected: Blue\n");
            break;
        default:
            printf("Color detected: Unknown\n");
            break;
    }
}
