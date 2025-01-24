#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "include/speech_to_text.h"
#include "include/text_to_command.h"
#include "include/synonyme.h"




int main() {
    // Récupérer le texte de la reconnaissance vocale
    char* texte = speech_reception();
    if (texte == NULL) {
        printf("{\"texte\" : \"\", \"commande\" : [] , \"erreur\" :\"Erreur lors de la réception du texte.\"}");
        return 1;
    }

    // Analyser le texte pour extraire les commandes, objets et couleurs sous forme de JSON
    char* json = speech_analysis_to_json(texte);
    if (json == NULL) {
        printf("{\"texte\" : \"%s\", \"commande\" : [] , \"erreur\" :\"Erreur lors de l'analyse du texte.\"}", texte);
        return 1;
    }
    // Afficher le résultat
    printf("%s", json);

    free(texte);
    free(json);
    return 0;
}
