#include "../include/text_to_command.h"
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>

// Définition globale des synonymes
typedef struct {
    const char *key;       // Clé principale (commande ou objet)
    const char *synonyms[8]; // Liste des synonymes (terminée par NULL)
} Synonyme;

// Définition des synonymes pour les commandes, objets et couleurs
Synonyme command_synonyms[] = {
    { "avance", {"avance", "marche", "progresse", "continue", "poursuis", "forward", NULL} },
    { "gauche", {"gauche", "left", NULL} },
    { "recule", {"recule", "reculer", "rétrograde", "retourne", "back", "reverse", "backward", NULL} },
    { "droite", {"droite", "right", NULL} },
    { "stop",   {"stop", "arrête", "pause", "halte", "immobilise", "annule", "quitte", "exit", "cancel", "halt", "end", NULL} },
    { "aller",  {"aller", "dirige", "vas", "parcours", "atteins", "continue", "go", "proceed", "move", "reach", "advance", NULL}}
};


Synonyme object_synonyms[] = {
    { "balle", {"ball", "ballon", "sphère", "boule", "rond", "sphérique", "cercle", "sphere", "round", "orb", "circle"} },
    { "cube",  {"cube", "bloc", "parallélépipède", "carré", "cubique", "rectangle", "box", "square", "block", "parallelepiped", "rectangular"} },
};

Synonyme color_synonyms[] = {
    { "rouge", {"rouge", "red"} },
    { "bleu",  {"bleu", "blue"} },
    { "vert",  {"vert", "green"} },
    { "jaune", {"jaune", "yellow"} }
};

// Fonction pour obtenir l'index d'un mot dans une chaîne
int get_index(const char *texte, const char *mot) {
    char *position = strstr(texte, mot);
    return position ? position - texte : -1;
}

// Fonction pour extraire un nombre à partir d'une position dans le texte
int extract_number_from_position(const char *texte) {
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

// Remplacer un mot dans une chaîne par un autre
char *replaceWord(char *s, const char *old, const char *new) {
    char *result;
    int i, cnt = 0;
    int newWlen = strlen(new);
    int oldWlen = strlen(old);
    // Compter le nombre de fois que le mot à remplacer apparaît et le stocker dans cnt
    for (i = 0; s[i] != '\0'; i++) {
        if (strstr(&s[i], old) == &s[i]) {
            cnt++;
            i += oldWlen - 1;
        }
    }
    // Allouer de la mémoire pour le nouveau texte de la taille de l'ancien texte plus le nombre de remplacements multiplié par la différence de longueur entre le nouveau et l'ancien mot
    result = (char *)malloc(i + cnt * (newWlen - oldWlen) + 1);
    if (!result) return NULL;

    // Remplacer le mot
    i = 0;
    while (*s) {
        // Si le mot à remplacer est trouvé, le remplacer par le nouveau mot
        if (strstr(s, old) == s) {
            strcpy(&result[i], new);
            i += newWlen; // Avancer l'index de la longueur du nouveau mot
            s += oldWlen; // Avancer l'index de la longueur de l'ancien mot
        } else {
            result[i++] = *s++; // Copier le caractère de l'ancien texte
        }
    }

    result[i] = '\0';
    return result;
}

// Fonction qui remplace tous les synonymes par les clés principales
char *replaceSynonyms(char *texte) {
    int nbre_commandes = sizeof(command_synonyms) / sizeof(command_synonyms[0]);
    int nbre_objets = sizeof(object_synonyms) / sizeof(object_synonyms[0]);
    int nbre_couleurs = sizeof(color_synonyms) / sizeof(color_synonyms[0]);

    char *splitedText = strdup(texte); // Dupliquer le texte pour ne pas l'écraser
    if (!splitedText) return NULL;

    // Remplacer les synonymes des commandes
   
    for (int i = 0; i < nbre_commandes; i++) {
        char *key = command_synonyms[i].key;
        char **synonyms = command_synonyms[i].synonyms;
        for (int j = 0; j < 8 && synonyms[j] != NULL; j++) {
            char *tmp = replaceWord(splitedText, synonyms[j], key);
            free(splitedText);
            splitedText = tmp;
        }
       
    }
   
    

    // Remplacer les synonymes des objets
    for (int i = 0; i < nbre_objets; i++) {
        char *key = object_synonyms[i].key;
        char **synonyms = object_synonyms[i].synonyms;
        for (int j = 0; synonyms[j] != NULL; j++) {
            char *tmp = replaceWord(splitedText, synonyms[j], key);
            free(splitedText);
            splitedText = tmp;
        }
    }
    // Remplacer les synonymes des couleurs
    for (int i = 0; i < nbre_couleurs; i++) {
        char *key = color_synonyms[i].key;
        char **synonyms = color_synonyms[i].synonyms;
        for (int j = 0; synonyms[j] != NULL; j++) {
            char *tmp = replaceWord(splitedText, synonyms[j], key);
            free(splitedText);
            splitedText = tmp;
        }
    }

    return splitedText;
}

// Fonction pour analyser le texte de la parole et générer un JSON
char *speech_analysis_to_json(const char* texte) {
    char *json = malloc(1024);
    char *splitedText;
    int nbre_commandes = sizeof(command_synonyms) / sizeof(command_synonyms[0]);

    const char *commands[nbre_commandes];
    for (int i = 0; i < nbre_commandes; i++) {
        commands[i] = command_synonyms[i].key;
    }
    // Initialiser le JSON
    if (!json) return NULL;
    strcpy(json, "{");
    strcat(json, "\"texte\": \"");
    strcat(json, texte);
    strcat(json, "\"");
    strcat(json, ", \"commandes\": [");
    if (texte == NULL) return NULL;
    // Remplacer les synonymes par les clés principales
    const char *newText = replaceSynonyms(texte);
    // Diviser le texte en fonction des commandes
    splitedText = splitText(newText, commands, nbre_commandes);
    // Ajouter des séparateurs entre les commandes
    int index = 0;
    while (splitedText[index] != '\0') {
        char *positionSeparator = strchr(splitedText + index, '/');
        int positionSeparatorIndex = positionSeparator ? positionSeparator - (splitedText + index) : -1;
        if (positionSeparatorIndex == -1) {
        char *tmp = textToCommandeJson(splitedText + index);
            strcat(json, tmp);
            strcat(json, "]"); // Fin des commandes
            strcat(json, "}");
            free(tmp);
            free(splitedText);
            return json;
        } else if (positionSeparatorIndex == 0) { //si le séparateur est au début de la chaîne
            index++; // Ignorer les séparateurs
        } else {
            splitedText[index + positionSeparatorIndex] = '\0'; // Séparer la chaîne ET remplacer le séparateur par un caractère nul
            char *tmp = textToCommandeJson(splitedText + index);
            strcat(json, tmp);
            free(tmp);
            strcat(json, ", ");
            index += positionSeparatorIndex + 1;// Avancer l'index de la longueur du séparateur + 1
            
        }
    }
    free(splitedText);
    return json;
}

char* textToCommandeJson(const char* texte) {
    if (texte == NULL) return NULL;

    int num_commands = sizeof(command_synonyms) / sizeof(command_synonyms[0]);
    int num_objects = sizeof(object_synonyms) / sizeof(object_synonyms[0]);
    int num_colors = sizeof(color_synonyms) / sizeof(color_synonyms[0]);

    // Initialisation des tableaux de synonymes
    const char *commands[num_commands];
    for (int i = 0; i < num_commands; i++) {
        commands[i] = command_synonyms[i].key;
    }

    const char *objects[num_objects];
    for (int i = 0; i < num_objects; i++) {
        objects[i] = object_synonyms[i].key;
    }

    const char *colors[num_colors];
    for (int i = 0; i < num_colors; i++) {
        colors[i] = color_synonyms[i].key;
    }
    // Allocation mémoire pour le JSON (augmentable dynamiquement si nécessaire)
    char *json = malloc(1024);
    if (!json) return NULL;
    strcpy(json, "{");

    const char *remaining_text = texte;
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
                        number = 75; // Valeur par défaut
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
