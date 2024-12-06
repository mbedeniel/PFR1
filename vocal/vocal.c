#include "vocal.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

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

// Fonction pour analyser et sérialiser en JSON, en respectant l'ordre des commandes
char* speech_analysis_to_json(const char* texte) {
    if (texte == NULL) return NULL;

    // Commandes à vérifier
    const char *commands[] = {"avance", "gauche", "recule", "droite", "stop"};
    const int num_commands = sizeof(commands) / sizeof(commands[0]);

    // Allocation dynamique pour le JSON
    char *json = malloc(1024);
    if (!json) return NULL;

    strcpy(json, "{");
    int first = 1; // Indique si c'est la première commande ajoutée

    const char *remaining_text = texte;

    // Parcourir tout le texte pour analyser chaque commande dans l'ordre
    while (*remaining_text) {
        int found_command = 0;

        for (int i = 0; i < num_commands; i++) {
            int position = get_index(remaining_text, commands[i]);
            if (position == 0) { // La commande est trouvée au début du texte restant
                found_command = 1;

                // Extraire le nombre après la commande
                int number = extract_number_from_position(remaining_text + strlen(commands[i]));
                if (number > 0) {
                    if (!first) strcat(json, ", ");
                    first = 0;
                    char buffer[100];
                    sprintf(buffer, "\"%s\": %d", commands[i], number);
                    strcat(json, buffer);
                }

                // Avancer le texte après la commande analysée
                remaining_text += strlen(commands[i]);
                while (*remaining_text && !isspace(*remaining_text)) remaining_text++; // Ignorer les caractères associés
                break;
            }
        }

        if (!found_command) {
            // Si aucune commande trouvée, avancer d'un mot
            while (*remaining_text && !isspace(*remaining_text)) remaining_text++;
            while (*remaining_text && isspace(*remaining_text)) remaining_text++;
        }
    }

    strcat(json, "}");
    return json;
}

// Fonction pour lire le texte généré par la reconnaissance vocale
char* speech_reception() {
    // Exécuter le script Python
    int status = system("py ./python/speech.py > ./python/texte.txt");
    if (status == -1) return NULL;

    // Ouvrir le fichier texte
    FILE* file = fopen("./python/texte.txt", "r");
    if (!file) return NULL;

    // Déterminer la taille du fichier
    fseek(file, 0, SEEK_END);
    long length = ftell(file);
    fseek(file, 0, SEEK_SET);

    // Allouer de la mémoire pour le texte
    char* texte = malloc(length + 1);
    if (!texte) {
        fclose(file);
        return NULL;
    }

    // Lire le texte depuis le fichier
    fread(texte, 1, length, file);
    texte[length] = '\0'; 
    fclose(file);

    return texte;
}

int main() {
    // Exemple de texte pour tester
    //char* texte = "avance de 5 mètres";
    char* texte = speech_reception();
    // Analyser le texte et générer le JSON
    char* json = speech_analysis_to_json(texte);
    if (json) {
        printf("JSON: %s\n", json);
        free(json); // Libérer la mémoire allouée
    }

    return 0;
}
