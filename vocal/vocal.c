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

// Fonction pour extraire le nombre à partir de la position donnée dans le texte
int extract_number_from_position(const char *texte, int start) {
    int number = 0;
    while (texte[start] != '\0' && isdigit(texte[start])) {
        number = number * 10 + (texte[start] - '0');
        start++;
    }
    return number;
}

// Fonction pour analyser et sérialiser en JSON
char* speech_analysis_to_json(char* texte) {
    if (texte == NULL) {
        return NULL;
    }

    // Commandes à vérifier
    const char *commands[] = {"avance", "gauche", "recule", "droite"};
    const int num_commands = sizeof(commands) / sizeof(commands[0]);

    // Déclaration d'un tableau pour les positions des commandes
    int position_command[num_commands];
    for (int i = 0; i < num_commands; i++) {
        position_command[i] = get_index(texte, commands[i]);
        printf("position_command[%d]: %d , %s\n", i, position_command[i], commands[i]);
    }

    // Allocation dynamique de mémoire pour le JSON
    char *json = malloc(1024 * sizeof(char));
    if (!json) return NULL;

    // Initialisation du JSON
    strcpy(json, "{");
    int first = 1; // Pour savoir si on ajoute une virgule

    // Trier les commandes par leur position dans le texte
    for (int i = 0; i < num_commands; i++) {
        for (int j = i + 1; j < num_commands; j++) {
            if (position_command[i] > position_command[j] && position_command[i] != -1 && position_command[j] != -1) {
                int temp = position_command[i];
                position_command[i] = position_command[j];
                position_command[j] = temp;
            }
        }
    }

    // Analyser le texte et récupérer les commandes et leurs nombres associés
    for (int i = 0; i < num_commands; i++) {
        // Récupérer la position de la commande dans le texte
        int position = position_command[i];
        if (position != -1) {
            // Chercher le nombre après la commande
            int number = extract_number_from_position(texte, position + strlen(commands[i]));
            
            // Si un nombre est trouvé, ajouter au JSON
            if (number > 0) {
                if (!first) {
                    strcat(json, ", ");
                }
                first = 0; // Après la première commande
                char buffer[200];
                sprintf(buffer, "\"%s\": %d", commands[i], number);
                strcat(json, buffer);
            }
        }
    }

    // Fermer le JSON
    strcat(json, "}");
    printf("JSON: %s\n", json);

    return json;  // Retourner directement le JSON
}

// Fonction pour lire le texte généré par la reconnaissance vocale
char* speech_reception() {
    // Exécuter le script Python pour la reconnaissance vocale et
    // récupérer le texte qui est redirigé vers la sortie standard sur un fichier
    int status = system("py ./python/speech.py > ./python/texte.txt");

    if (status == -1) {
        return NULL;
    }

    // Lire le texte depuis le fichier
    FILE* file = fopen("./python/texte.txt", "r");
    if (file == NULL) {
        return NULL;
    }

    fseek(file, 0, SEEK_END);
    long length = ftell(file);
    fseek(file, 0, SEEK_SET);

    // Allouer de la mémoire pour le texte
    char* texte = malloc((length + 1) * sizeof(char));
    if (!texte) {
        fclose(file);
        return NULL;
    }

    // Lire le texte depuis le fichier
    fread(texte, 1, length, file);
    texte[length] = '\0';  // Assurez-vous que la chaîne est terminée

    fclose(file);
    return texte;
}

int main() {
    // Exemple de réception du texte de la reconnaissance vocale

    // Lire le texte de la reconnaissance vocale
    char* texte = "avance de 10, gauche de 90, recule de 5, droite de 45";
    // Générer le JSON à partir du texte
    char* json = speech_analysis_to_json(texte);
    printf("JSON: %s\n", json);

    // Libérer la mémoire allouée
    free(texte);
    free(json);

    return 0;
}
