#include <stdio.h>
#include <stdlib.h>
#include "include/speech_to_text.h"
#include "include/text_to_command.h"

int main() {

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

