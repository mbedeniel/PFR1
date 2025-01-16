#include <stdio.h>
#include <stdlib.h>
#include "../include/synonyme.h"
#include <string.h>



// Remplacer un mot dans une chaîne par un autre
char *replaceWord(char *s,  char *old,  char *new) {
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

 // Fonction de remplacement des synonymes pour un tableau donné
char* replaceListSynonyme(char *result, Synonyme *table, int nbre_element) {
        for (int i = 0; i < nbre_element; i++) { // Parcourir le tableau  clé principale et synonymes
            char *key = table[i].key;
            int taille = sizeof(table[i].synonyms) / sizeof(table[i].synonyms[0]);
            for (int j = 0; j < taille; j++) { // Parcourir les synonymes
                if (table[i].synonyms[j] == NULL) break;
                char *tmp = replaceWord(result, table[i].synonyms[j], key);
                result = tmp;
            }
           
        }
        return result;
    }

