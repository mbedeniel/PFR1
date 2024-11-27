#include "vocal.h"
#include <stdio.h>

char* speech_reception(){
    //lire le son du micro
    //transformer le son en texte
    //retourner le texte

    // Exécuter le script Python pour la reconnaissance vocale et
    // récupérer le texte qui est redirigé vers la sortie standard sur un fichier
    int status = system("python3 python/speech_recognition.py > texte.txt");

    if (status == -1) {
       return NULL;
    }
    // Lire le texte depuis le fichier
    FILE* file = fopen("python/texte.txt", "r");
    if (file == NULL) {
        return NULL;
    }
    int taille = 100;
    char* texte = malloc(taille * sizeof(char));
    fgets(texte, taille, file);
    fclose(file);
    return texte;
}

char* speech_analysis(char* texte){
    //analyser le texte
    //retourner un objet commande
    return "commande";
}



int main() {
    
    return 0;
}
