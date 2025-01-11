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
    // Ignorer les caractères non numériques et les espaces pour accélérer le pointeur
    while (*texte && !isdigit(*texte)) {
        texte++;
    }
    // Extraire le nombre
    while (*texte && isdigit(*texte)) {
        number = number * 10 + (*texte - '0');
        texte++;
    }
    return number;
}

// Ajouter des séparateurs entre les commandes en fonction de la liste des synonymes de chaque commande
char* splitText(const char* texte, const char* commands[], int num_commands) {
    // Allouer de l'espace pour le nouveau texte (double taille de texte pour être sûr d'avoir assez d'espace)
    char* newText = malloc(2 * strlen(texte) + 1);
    if (!newText) return NULL;
    newText[0] = '\0';

    const char* remaining_text = texte;
    while (*remaining_text) {
        int found_command = 0;
        for (int i = 0; i < num_commands; i++) {
            int position = get_index(remaining_text, commands[i]);
            if (position == 0) {
                strcat(newText, "/");  // Ajouter un séparateur "/"
                strcat(newText, commands[i]);

                found_command = 1;
                // Avancer le texte jusqu'au prochain espace
                remaining_text += strlen(commands[i]);
                while (*remaining_text && !isspace(*remaining_text)) remaining_text++;
                // Ajouter un espace après la commande
                strcat(newText, " ");
                break;
            }
        }
        if (!found_command) {
            strncat(newText, remaining_text, 1);
            remaining_text++;
        }
    }
    return newText;
}

char *speech_analysis_to_json(const char* texte) {
    const char *commands[] = {"avance", "gauche", "recule", "droite", "stop", "aller"};
    const char *objects[] = {"balle", "cube"};
    const char *colors[] = {"rouge", "bleu", "vert", "jaune"}; // Liste des couleurs possibles
    const int num_commands = sizeof(commands) / sizeof(commands[0]);
    char *json = malloc(1024);
    if (!json) return NULL;
    strcpy(json, "{");
    strcat(json, "\"texte\": \"");
    strcat(json, texte);
    strcat(json, "\"");
    strcat(json, ", \"commandes\": [");



    if (texte == NULL) return NULL;
    char *splitedText = splitText(texte, commands, num_commands);

    int index = 0;
    while (splitedText[index] != '\0') {
        char *postionSparator = strchr(splitedText + index, '/');
        int positionSeparatorIndex = postionSparator ? postionSparator - (splitedText + index) : -1;
        // Si le séparateur n'est pas trouvé, on considère que c'est la dernière commande
        // Si le séparateur n'est pas trouvé, on considère que c'est la dernière commande
        if (positionSeparatorIndex == -1) {
            char *tmp = textToCommandeJson(splitedText + index);
            strcat(json, tmp);
            strcat(json, "]");
            strcat(json, "}");
            free(tmp);
            free(splitedText);
            return json;
            // Traiter cette section ici
        }
        else if (positionSeparatorIndex == 0) {
            // Si le séparateur est trouvé au début de la chaîne, on ignore le séparateur
            index++;
        }
        else {
            // Remplacer le séparateur par un caractère de fin de chaîne
            
            splitedText[index + positionSeparatorIndex] = '\0';
            char *tmp = textToCommandeJson(splitedText + index);
            strcat(json, tmp);
            free(tmp);
            strcat(json, ", ");

            // Traiter cette section ici
            index += positionSeparatorIndex + 1;
        }
    }
    free(splitedText);
    return NULL;
}

// Fonction pour analyser et sérialiser en JSON
char* textToCommandeJson(const char* texte) {
    if (texte == NULL) return NULL;

    const char *commands[] = {"avance", "gauche", "recule", "droite", "stop", "aller"};
    const char *objects[] = {"balle", "cube"};
    const char *colors[] = {"rouge", "bleu", "vert", "jaune"}; // Liste des couleurs possibles

    const int num_commands = sizeof(commands) / sizeof(commands[0]);
    const int num_objects = sizeof(objects) / sizeof(objects[0]);
    const int num_colors = sizeof(colors) / sizeof(colors[0]);

    char *json = malloc(1024);
    if (!json) return NULL;
    // Création du json qui contiendra les commandes et les valeurs et sera utilisé pour la communication avec le robot
    strcpy(json, "{");
    int first = 1;

    const char *remaining_text = texte;
    
    int trouve = 0;
    while (*remaining_text) {
        int found_command = 0;
        
        // Recherche chaque commande dans le texte 
        // Si la commande est trouvée, on extrait le nombre associé à la commande
        // Si elle est trouvée sans nombre, on lui attribue une valeur par défaut
        // Si la commande n'est pas trouvée, on passe à la suivante
        for (int i = 0; i < num_commands; i++) {
            int position = get_index(remaining_text, commands[i]); // Obtenir l'index de la commande dans le texte
            if (position == 0) {
                found_command = 1;
                //marquer la commande comme trouvée
                trouve = 1;

                if (strcmp(commands[i], "aller") == 0) {
                    // Si la commande est "aller", rechercher l'objet et la couleur
                    strcat(json, "\"action\": \"aller\"");
                    // Recherche de l'objet (balle, cube)
                    char object[20] = "null";
                    char color[20] = "null";
                    // Recherche de l'objet dans le texte
                    for (int j = 0; j < num_objects; j++) {
                        if (get_index(remaining_text, objects[j]) != -1) {
                            strcpy(object, objects[j]);
                            break;
                        }
                    }
                    // Recherche de la couleur dans le texte
                    for (int j = 0; j < num_colors; j++) {
                        if (get_index(remaining_text, colors[j]) != -1) {
                            strcpy(color, colors[j]);
                            break;
                        }
                    }
                    // Ajouter l'objet et la couleur au JSON
                    char buffer[100];
                    sprintf(buffer, ", \"object\": \"%s\", \"color\": \"%s\"", object, color);
                    strcat(json, buffer);
                } else {
                    int number = extract_number_from_position(remaining_text + strlen(commands[i]));
                    // Vérifier les valeurs par défaut de number pour chaque commande si elle n'est pas fournie
                    if (number <= 0) {
                        if (strcmp(commands[i], "avance") == 0 || strcmp(commands[i], "recule") == 0) {
                            number = 75;
                        } else if (strcmp(commands[i], "droite") == 0 || strcmp(commands[i], "gauche") == 0) {
                            number = 90;
                        }
                    }

                    // Ajouter la commande et le nombre au JSON
                    if (!first) strcat(json, ", "); // Ajouter une virgule pour séparer les commandes
                    first = 0;
                    // Ajouter la commande et le nombre au JSON
                    char buffer[100];
                    sprintf(buffer, "\"action\": \"%s\", \"valeur\": %d", commands[i], number);
                    strcat(json, buffer);
                }

                // Accélérer le pointeur pour passer à la commande suivante en sautant les espaces et les caractères non valides
                remaining_text += strlen(commands[i]);
                while (*remaining_text && !isspace(*remaining_text)) remaining_text++;
                
                // Arrêt de la recherche de commande
                strcat(json, "}");
                return json;
            }
        }
        // Si aucune commande n'est trouvée, on passe à la suivante en sautant les espaces et les caractères non valides 
        // Cela permet de ne pas bloquer le programme si une commande n'est pas reconnue
        if (!found_command) {
            while (*remaining_text && !isspace(*remaining_text)) remaining_text++;
            while (*remaining_text && isspace(*remaining_text)) remaining_text++;
        }
    }

    strcat(json, "}");
    //si une commande est trouvée, on retourne le json
    if (trouve) return json;
    //si aucune commande n'est trouvée, on retourne NULL et on libère la mémoire
    free(json);
    return NULL;
}
