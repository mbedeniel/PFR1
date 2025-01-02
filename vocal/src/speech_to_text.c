#include "../include/speech_to_text.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* speech_reception() {
    FILE* fp = popen("python ./python/speech.py", "r");
    if (!fp) return NULL;

    // Tampon pour stocker la sortie
    static char buffer[1024];
    char* result = fgets(buffer, sizeof(buffer), fp); 

    pclose(fp);
    return result ? buffer : NULL;
}