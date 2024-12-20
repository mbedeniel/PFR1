#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_json_response(const char *mode, int value) {
    printf("{\"%s\": %d}", mode, value);
}

void print_error_response() {
    printf("{}");
}

int main() {
    char mode;
    int value = 0; // Valeur par défaut
    char *mode_name;

    
    /*
    // Présentation du menu
    printf("Veuillez choisir un mode parmi les suivants :\n");
    printf("a : avancer\n");
    printf("r : reculer\n");
    printf("d : droite\n");
    printf("g : gauche\n");

    // Lecture du mode et de la valeur
    printf("Saisissez le mode et la valeur (ex : a 15 ou r) : ");

    */
    int inputs = scanf("%c %d", &mode, &value); // Lecture du mode et éventuellement de la valeur

    // Validation du mode
    switch (mode) {
        case 'a':
            mode_name = "avancer";
            break;
        case 'r':
            mode_name = "reculer";
            break;
        case 'd':
            mode_name = "droite";
            break;
        case 'g':
            mode_name = "gauche";
            break;
        default:
            // Si le mode est invalide
            print_error_response();
            return 1;
    }

    // Si la valeur n'est pas saisie, elle reste à la valeur par défaut (0)
    if (inputs == 1) {
        value = 0;
    }

    // Générer la réponse JSON au format demandé
    print_json_response(mode_name, value);

    return 0;
}
