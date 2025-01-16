#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Fonction qui génère une réponse JSON avec le mode (avancer, reculer, etc.) et sa valeur associée.
// Exemple de sortie : {"avancer": 15}
void print_json_response( char *mode, int value) {
    printf("{\"action\": \"%s\", \"valeur\": %d}", mode, value);
}

// Fonction qui génère une réponse JSON vide pour signaler une erreur, lorsque le mode est invalide.
// Exemple de sortie : {}
void print_error_response() {
    printf("{}");
}

/* 
 * Fonction principale (main) qui:
 * 1. Lit les entrées de l'utilisateur : un mode (a, r, d, g) et une valeur (entier).
 * 2. Valide et associe un nom de mode en texte.
 * 3. Si une valeur est fournie, elle est utilisée ; sinon, une valeur par défaut de 0 est utilisée.
 * 4. Génère une réponse JSON avec le mode et la valeur.
 * Si le mode est invalide, une réponse JSON vide est retournée.
 */
int main() {
    char mode;                // Stocke le mode saisi par l'utilisateur (a, r, d, g)
    int value = 0;            // Valeur associée au mode, par défaut à 0
    char *mode_name;          // Pointeur pour le nom du mode en texte
    int inputs;               // Variable pour vérifier le nombre d'entrées utilisateur

    // Lecture des entrées utilisateur : un caractère (mode) et un entier (valeur optionnelle)
    inputs = scanf("%c %d", &mode, &value);

    // Validation du mode saisi et attribution du nom du mode en texte
    switch (mode) {
        case 'a':  // Mode 'a' pour avancer
            mode_name = "avancer";
            break;
        case 'r':  // Mode 'r' pour reculer
            mode_name = "reculer";
            break;
        case 'd':  // Mode 'd' pour tourner à droite
            mode_name = "droite";
            break;
        case 'g':  // Mode 'g' pour tourner à gauche
            mode_name = "gauche";
            break;
        default:
            // Si le mode saisi est invalide, afficher une erreur et terminer le programme
            print_error_response();
            return 1;
    }

    // Si l'utilisateur n'a pas saisi de valeur, la valeur reste à 0
    if (inputs == 1) {
        value = 0;
    }

    // Génération de la réponse JSON avec le mode valide et la valeur associée
    print_json_response(mode_name, value);

    return 0; // Fin du programme
}
