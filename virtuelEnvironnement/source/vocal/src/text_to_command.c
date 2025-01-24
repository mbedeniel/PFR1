#include "../include/text_to_command.h"
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>
#include "../include/initData.h"

// Définition globale des synonymes

// Fonction pour obtenir l'index d'un mot dans une chaîne
int get_index( char *texte,  char *mot) {
    char *position = strstr(texte, mot);
    return position ? position - texte : -1;
}

// Fonction pour extraire un nombre à partir d'une position dans le texte
int extract_number_from_position( char *texte) {
    int number = 0;
    while (*texte && !isdigit(*texte)) {
        texte++; // Ignorer les caractères non numériques
    }
    while (*texte && isdigit(*texte)) {
        number = number * 10 + (*texte - '0');
        texte++; // Extraire le nombre
    }
    return number;
}




// Fonction pour analyser le texte de la parole et générer un JSON
char *speech_analysis_to_json( char* texte) {
    char **liste_commandes = getKeys(command_synonyms, num_commands);
    char **liste_objets = getKeys(object_synonyms, num_objects);
    char **liste_couleurs = getKeys(color_synonyms, num_colors);

    //marquer la fin du texte avec \0 au cas où
    if (texte[strlen(texte) - 1] != '\0')
        strcat(texte, "\0");


    // Allocation mémoire pour le JSON (augmentable dynamiquement si nécessaire)
    
    
    
    
    char *json = malloc(1024);
    char *splitedText;
   
    // Initialiser le JSON
    if (!json) return NULL;
    strcpy(json, "{");
    strcat(json, "\"texte\": \"");
    strcat(json, texte);
    strcat(json, "\"");
    strcat(json, ", \"commandes\": [");
    if (texte == NULL) return NULL;


    // remplecer les synonymes par les clés principales
    // Remplacer les synonymes dans le texte
    texte = replaceListSynonyme(texte, command_synonyms, num_commands);
    texte = replaceListSynonyme(texte, object_synonyms, num_objects);
    texte = replaceListSynonyme(texte, color_synonyms, num_colors);


    
    // Diviser le texte en fonction des commandes
    splitedText = splitText(texte, liste_commandes, num_commands);
    // Ajouter des séparateurs entre les commandes
    int index = 0;
    while (splitedText[index] != '\0') {
        char *positionSeparator = strchr(splitedText + index, '/');
        int positionSeparatorIndex = positionSeparator ? positionSeparator - (splitedText + index) : -1;
      
        if (positionSeparatorIndex == -1) { //si le séparateur n'est pas trouvé
            char *tmp = textToCommandeJson(splitedText + index);
            if(tmp != NULL) {
                strcat(json, tmp);
                free(tmp);
            }
            strcat(json, "]"); // Fin des commandes
            strcat(json, "}");
            free(tmp);
            free(splitedText);
            return json;
        } else if (positionSeparatorIndex == 0) { //si le séparateur est au début de la chaîne
            index++; // Ignorer les séparateurs
            
        } else { //si le séparateur est trouvé 
            splitedText[index + positionSeparatorIndex] = '\0'; // Séparer la chaîne ET remplacer le séparateur par un caractère nul
            char *tmp = textToCommandeJson(splitedText + index );
            if(tmp != NULL) {
                    strcat(json, tmp);
                    strcat(json, ", ");
            }
            free(tmp);
            index += positionSeparatorIndex + 1;// Avancer l'index de la longueur du séparateur + 1
            
        }
    }
    free(splitedText);
    return json;
}

char* textToCommandeJson(char* texte) {
    char ** commands = getKeys(command_synonyms, num_commands);
    char ** objects = getKeys(object_synonyms, num_objects);
    char ** colors = getKeys(color_synonyms, num_colors);
    
    if (texte == NULL) return NULL;
        
    // Allocation mémoire pour le JSON (augmentable dynamiquement si nécessaire)
    char *json = malloc(1024);
    if (!json) return NULL;
    strcpy(json, "{");

     char *remaining_text = texte;
    int first = 1;

    while (*remaining_text) {
        int found_command = 0;

        // Recherche des commandes dans le texte
        for (int i = 0; i < num_commands; i++) {
            int position = get_index(remaining_text, commands[i]);
            if (position == 0) { // Commande trouvée au début de remaining_text
                found_command = 1;

                // Traitement de la commande "aller"
                if (strcmp(commands[i], "aller") == 0) {
                    strcat(json, "\"action\": \"aller\"");

                    char object[20] = "null";
                    char color[20] = "null";

                    // Recherche des objets
                    for (int j = 0; j < num_objects; j++) {
                        if (get_index(remaining_text, objects[j]) != -1) {
                            strcpy(object, objects[j]);
                            break;
                        }
                    }

                    // Recherche des couleurs
                    for (int j = 0; j < num_colors; j++) {
                        if (get_index(remaining_text, colors[j]) != -1) {
                            strcpy(color, colors[j]);
                            break;
                        }
                    }

                    // Ajouter objet et couleur au JSON
                    char buffer[100];
                    sprintf(buffer, ", \"object\": \"%s\", \"color\": \"%s\"", object, color);
                    strcat(json, buffer);

                } else { // Autres commandes
                    int number = extract_number_from_position(remaining_text + strlen(commands[i]));
                    if (number <= 0) {
                        number = 90; // Valeur par défaut
                    }

                    if (!first) strcat(json, ", ");
                    first = 0;

                    char buffer[100];
                    sprintf(buffer, "\"action\": \"%s\", \"valeur\": %d", commands[i], number);
                    strcat(json, buffer);
                }

                // Avancer dans le texte après la commande
                remaining_text += strlen(commands[i]);
                while (*remaining_text && !isspace(*remaining_text)) remaining_text++;
                strcat(json, "}");
                return json;
            }
        }

        // Ignorer les parties non reconnues
        if (!found_command) {
            while (*remaining_text && !isspace(*remaining_text)) remaining_text++;
            while (*remaining_text && isspace(*remaining_text)) remaining_text++;
        }
    }

    // Si aucune commande reconnue
    free(json);
    return NULL;
}

// Ajouter des séparateurs entre les commandes en fonction de la liste des synonymes de chaque commande
char* splitText( char* texte,  char* commands[], int num_commands) {
    // Allouer de l'espace pour le nouveau texte (double taille de texte pour être sûr d'avoir assez d'espace)
    char* newText = malloc(2 * strlen(texte) + 1);
    if (!newText) return NULL;
    newText[0] = '\0';

     char* remaining_text = texte;
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
