#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "include/speech_to_text.h"
#include "include/text_to_command.h"

int main_() {

    char* texte = speech_reception();
    if (texte == NULL) {
        printf("{\"erreur\" :\"Erreur lors de la réception du texte.\"}");
        return 1;
    }

    char* json = speech_analysis_to_json(texte);
    if (json == NULL) {
        printf("{\"erreur\" :\"Erreur lors de la génération du JSON.\"}");
        free(texte);
        return 1;
    }

    printf("%s", json);

    free(texte);
    free(json);
    return 0;
}
// Main pour tester le programme
// Main pour tester le programme
int main() {
    // Texte d'entrée
    const char *texte = "avance  tourne à gauche 30, et vas vers le ballon rouge";

    // Appel de la fonction pour convertir en JSON
    char *result = speech_analysis_to_json(texte);

    // Affichage du résultat
    printf("r = %s\n", result);

    // Libération de la mémoire
    free(result);
    return 0;
}