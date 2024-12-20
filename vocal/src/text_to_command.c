#include "../include/text_to_command.h"
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>

// Fonction pour obtenir l'index d'un mot dans une chaîne
int get_index(const char *texte, const char *mot) {
    char *position = strstr(texte, mot);
    return position ? position - texte : -1;
}

// Fonction pour extraire le nombre à partir d'une position donnée dans le texte
int extract_number_from_position(const char *texte) {
    int number = 0;
    while (*texte && !isdigit(*texte)) {
        texte++;
    }
    while (*texte && isdigit(*texte)) {
        number = number * 10 + (*texte - '0');
        texte++;
    }
    return number;
}

// Fonction pour analyser et sérialiser en JSON
char* speech_analysis_to_json(const char* texte) {
    if (texte == NULL) return NULL;

    const char *commands[] = {"avance", "gauche", "recule", "droite", "stop"};
    const int num_commands = sizeof(commands) / sizeof(commands[0]);

    char *json = malloc(1024);
    if (!json) return NULL;

    strcpy(json, "{");
    int first = 1;

    const char *remaining_text = texte;

    while (*remaining_text) {
        int found_command = 0;

        for (int i = 0; i < num_commands; i++) {
            int position = get_index(remaining_text, commands[i]);
            if (position == 0) {
                found_command = 1;

                int number = extract_number_from_position(remaining_text + strlen(commands[i]));
                //verifier les valeur par default de number pour chaque commande
                if (number <= 0) {
                    if (strcmp(commands[i], "avance") == 0 || strcmp(commands[i], "recule") == 0) {
                        number = 200;
                    } else if (strcmp(commands[i], "droite") == 0 || strcmp(commands[i], "gauche") == 0) {
                        number = 90;
                    }
                }


                if (!first) strcat(json, ", ");
                first = 0;
                char buffer[100];
                sprintf(buffer, "\"%s\": %d", commands[i], number);
                strcat(json, buffer);

                // accelerer le pointeur pour passer à la commande suivante en sautant les espaces et les caractères non valides
                remaining_text += strlen(commands[i]);
                while (*remaining_text && !isspace(*remaining_text)) remaining_text++;
                break;
            }
        }
    // Si aucune commande n'est trouvée, on passe à la suivante en sautant les espaces et les caractères non valides 
    //cela permet de ne pas bloquer le programme si une commande n'est pas reconnue
        if (!found_command) {
            // en sautant les espaces et les caractères non valides
            while (*remaining_text && !isspace(*remaining_text)) remaining_text++;
            while (*remaining_text && isspace(*remaining_text)) remaining_text++;
        }
    }

    strcat(json, "}");
    return json;
}