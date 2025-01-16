#include <stdio.h>


int get_index( char *texte,  char *mot);
int extract_number_from_position( char *texte);
char* speech_analysis_to_json( char* texte,  char *commands[], char *objects[],  char *colors[], int num_commands, int num_objects, int num_colors);
char* textToCommandeJson( char* texte,  char *commands[],  char *objects[],  char *colors[], int num_commands, int num_objects, int num_colors);
char* splitText( char* texte,  char* commands[], int num_commands);



