#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "include/speech_to_text.h"
#include "include/text_to_command.h"
#include "include/synonyme.h"

int main() {

    // Définition des synonymes pour les commandes, objets et couleurs
    Synonyme command_synonyms[] = {
        { "avance", {"avance", "marche", "progresse", "continue", "poursuis", "forward", NULL} },
        { "gauche", {"gauche", "left", NULL} },
        { "recule", {"recule", "rétrograde", "retourne", "back", "reverse", "backward", NULL} },
        { "droite", {"droite", "right", NULL} },
        { "stop",   {"stop", "arrête", "pause", "annule", "quitte", "exit", "cancel", "end", NULL} },
        { "aller",  {"aller", "dirige","recherche", "vas", "go", "proceed", "move", "reach", "advance", NULL}}
    };


    Synonyme object_synonyms[] = {
        { "balle", {"balle", "ballon", "sphère", "boule", "rond", "sphérique", "cercle", "sphere", "round", "orb", "circle", NULL} },
        { "cube",  {"cube", "bloc", "parallélépipède", "carré", "cubique", "rectangle", "box", "square", "block", "parallelepiped", "rectangular", NULL}}
        };

    Synonyme color_synonyms[] = {
        { "rouge", {"rouge", "red", NULL} },
        { "bleu",  {"bleu", "blue",NULL} },
        { "vert",  {"vert", "green", NULL} },
        { "noir",  {"noir", "black", NULL} },
        { "blanc", {"blanc", "white", NULL} },
        { "gris",  {"gris", "grey", NULL} },
        { "orange",{"orange", "orange", NULL} },
        { "violet",{"violet", "purple", NULL} },
        { "rose",  {"rose", "pink", NULL} },
        { "jaune", {"jaune", "yellow", NULL} }
    };


    // Récupérer le texte de la reconnaissance vocale
    char* texte = speech_reception();
    if (texte == NULL) {
        printf("{\"texte\" : \"\", \"commande\" : [] , \"erreur\" :\"Erreur lors de la réception du texte.\"}");
        return 1;
    }

    // Nombre de synonymes pour les commandes, objets et couleurs
    int num_commands = sizeof(command_synonyms) / sizeof(command_synonyms[0]);
    int num_objects = sizeof(object_synonyms) / sizeof(object_synonyms[0]);
    int num_colors = sizeof(color_synonyms) / sizeof(color_synonyms[0]);

    // Initialisation des tableaux de synonymes
     char *commands[num_commands];
    for (int i = 0; i < num_commands; i++) {
        commands[i] = command_synonyms[i].key;
    }

     char *objects[num_objects];
    for (int i = 0; i < num_objects; i++) {
        objects[i] = object_synonyms[i].key;
    }

     char *colors[num_colors];
    for (int i = 0; i < num_colors; i++) {
        colors[i] = color_synonyms[i].key;
    }



    // Remplacer les synonymes dans le texte
    texte = replaceListSynonyme(texte, command_synonyms, num_commands);
    texte = replaceListSynonyme(texte, object_synonyms, num_objects);
    texte = replaceListSynonyme(texte, color_synonyms, num_colors);
    // Analyser le texte pour extraire les commandes, objets et couleurs sous forme de JSON
    char* json = speech_analysis_to_json(texte, commands, objects, colors, num_commands, num_objects, num_colors);
    if (json == NULL) {
        printf("{\"texte\" : \"%s\", \"commande\" : [] , \"erreur\" :\"Erreur lors de l'analyse du texte.\"}", texte);
        return 1;
    }
    // Afficher le résultat
    printf("%s", json);

    free(texte);
    free(json);
    return 0;
}
