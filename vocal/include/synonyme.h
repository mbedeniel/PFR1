#include <stdio.h>  
typedef struct {
     char *key;       // Clé principale (commande ou objet)
     char *synonyms[100]; // Liste des synonymes (terminée par NULL)
} Synonyme;



char* replaceListSynonyme(char *result, Synonyme *table, int nbre_element);
char *replaceWord(char *s,  char *old,  char *new) ;