#include "../include/speech_to_text.h"
#include <stdio.h>
#include <stdlib.h>

char* speech_reception() {
    // Exécuter le script Python
    //pour le chemin dacces au fichier python , raisonnez par rapport a votre fichier app.exe ou main.c
    int status = system("py ./python/speech.py > ./python/texte.txt"); // Exécuter le script Python et rediriger la sortie vers un fichier texte
    if (status == -1) return NULL;

    // Ouvrir le fichier texte
    FILE* file = fopen("./python/texte.txt", "r"); // Ouvrir le fichier en mode lecture
    if (!file) return NULL;

    // Déterminer la taille du fichier
    fseek(file, 0, SEEK_END); // Aller à la fin du fichier
    long length = ftell(file); // Obtenir la position actuelle qui est la taille du fichier
    fseek(file, 0, SEEK_SET); // Retourner au début du fichier

    // Allouer de la mémoire pour le texte
    char* texte = malloc(length + 1); 
    if (!texte) {
        fclose(file);
        return NULL;
    }

    // Lire le texte depuis le fichier
    fread(texte, 1, length, file); // Lire 'length' octets depuis le fichier et les stocker dans 'texte'
    texte[length] = '\0';        // Ajouter un caractère de fin de chaîne à la fin du texte
    fclose(file);             // Fermer le fichier

    return texte;
}
