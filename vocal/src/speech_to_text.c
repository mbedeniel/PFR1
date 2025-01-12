#include "../include/speech_to_text.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* speech_reception() {
    //exécution de la commande python
    //FILE* fp = popen("python ./vocal/python/speech.py", "r"); //C:\Users\djibril\Desktop\cours\filRouge\PFR1\vocal\python\speech.py
    FILE* fp = popen("python -m vocal.python.speech", "r");
    
    if (!fp) return NULL;

    // Tampon pour stocker la sortie
    static char buffer[1024];
    char* result = fgets(buffer, sizeof(buffer), fp); 

    pclose(fp);
    return result ? buffer : NULL;
}