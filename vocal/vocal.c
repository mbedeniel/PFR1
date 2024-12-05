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
int extract_number_from_position(const char *texte) {
    int number = 0;
    int count = 0;
    int start = 0;
    //rechercher le nombre dans le texte
    while(!isdigit(texte[count]) && texte[count] != '\0') {
        count++;
    }
    //extraire le nombre
    while (texte[count] != '\0') {
        if (isdigit(texte[count])) {
            start = 1;
            number = number * 10 + (texte[count] - '0');
        } else if (start) {
            break;
        }
        count++;
    }

    return number;
}

// Fonction pour analyser et sérialiser en JSON
char* speech_analysis_to_json(char* texte) {
    if (texte == NULL) {
        return NULL;
    }

    // Commandes à vérifier
    const char *commands[] = {"avance", "gauche", "recule", "droite", "stop"};
    const int num_commands = sizeof(commands) / sizeof(commands[0]);

    // Déclaration d'un tableau pour les positions des commandes
    int position_command[num_commands];
    for (int i = 0; i < num_commands; i++) {
        position_command[i] = get_index(texte, commands[i]);
    }

    // Trier les commandes par leur position dans le texte (en tenant compte des -1)
    for (int i = 0; i < num_commands - 1; i++) {
        for (int j = i + 1; j < num_commands; j++) {
            if ((position_command[i] > position_command[j] && position_command[j] != -1) ||
                (position_command[i] == -1 && position_command[j] != -1)) {
                int temp = position_command[i];
                position_command[i] = position_command[j];
                position_command[j] = temp;

                // Échanger les commandes pour qu'elles restent synchronisées avec les indices
                const char *temp_cmd = commands[i];
                commands[i] = commands[j];
                commands[j] = temp_cmd;
            }
        }
    }

    // Allocation dynamique de mémoire pour le JSON
    char *json = malloc(1024 * sizeof(char));
    if (!json) return NULL;

    // Initialisation du JSON
    strcpy(json, "{");
    int first = 1; // Pour savoir si on ajoute une virgule

    // Construire le JSON
    for (int i = 0; i < num_commands; i++) {
        if (position_command[i] != -1) {
            int number = extract_number_from_position(texte + position_command[i]);
            if (number >= 0) {
                if (!first) {
                    strcat(json, ", ");
                }
                first = 0; // Après la première commande
                char buffer[100];
                sprintf(buffer, "\"%s\": %d", commands[i], number);
                strcat(json, buffer);
            }
        }
    }
    // Fermer le JSON
    strcat(json, "}");
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
    // ENLEVER UN DES COMMENTAIRES POUR TESTER AVEC UN TEXTE PRÉDÉFINI OU AVEC LA RECONNAISSANCE VOCALE
        // Lire le texte de la reconnaissance vocale
    //char* texte = speech_reception();
        //la ligne ci-dessus et décommenter la ligne ci-dessous pour tester avec un texte prédéfini
    char* texte = "avance de 10 mètres à gauche  ";
    
    
    
    
    // Générer le JSON à partir du texte
    char* json = speech_analysis_to_json(texte);
    printf("JSON: %s\n", json);

    // Libérer la mémoire allouée
    free(texte);
    free(json);

    return 0;
}
