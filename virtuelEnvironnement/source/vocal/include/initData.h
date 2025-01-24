#include "synonyme.h"

// Définition des synonymes pour les commandes, objets et couleurs
Synonyme command_synonyms[] = {
    { "avance", {"avance", "marche", "progresse", "continue", "poursuis", "forward", NULL} },
    { "gauche", {"gauche", "left", NULL} },
    { "recule", {"recule", "rétrograde", "retourne", "back", "reverse", "backward", NULL} },
    { "droite", {"droite", "right", NULL} },
    { "stop",   {"stop", "arrête", "pause", "annule", "quitte", "exit", "cancel", "end", NULL} },
    { "aller",  {"aller", "dirige","cherche", "vas", "go", "proceed", "move", "reach", "advance", NULL}}
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



// Nombre de synonymes pour les commandes, objets et couleurs
    int num_commands = sizeof(command_synonyms) / sizeof(command_synonyms[0]);
    int num_objects = sizeof(object_synonyms) / sizeof(object_synonyms[0]);
    int num_colors = sizeof(color_synonyms) / sizeof(color_synonyms[0]);

    

