#include "../include/speech_to_text.h"
#include <stdio.h>
#include <stdlib.h>

char* speech_reception() {
    // Exécuter le script Python
    //pour le chemin dacces au fichier python , raisonnez par rapport a votre fichier app.exe ou main.c
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
