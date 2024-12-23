#include "object.h"
#include "pre_processing.h"
#include <stdio.h>
#include <stdlib.h>

/*
******************************************
********PARAMETRES DE CONFIGURATION*******
******************************************
*/

#define color_min_pixel 75
#define shape_min_percentage 75

/*
color_min_pixel : nombre de pixel minimu pour valider la presence d'une couleur
shape_min_percentage : pourcentage minimu pour valider une forme
*/

/*
**************************************************************************
ROLE: INTERFACE D'ACCES AU DIFFRENTES FONCTIONALITÉES DU MODULE IMAGE ****
**************************************************************************
*/

/*
PRINCIPE: 
    L'ACCES AUX FONCTIONNALITÉES DU MODULE DOIT 
    CE FAIRE VIA image_interface ET UNIQUEMENT 
    DE CETTE FACON LA.

    POUR TOUTES DIFFICULTÉES DE COMPREHENSION
    OU DE COMMUNICATION VEULLIEZ ME CONTACTER.
*/


/*
**************************************
********PROTOTYPE DES FONCTIONS*******
**************************************
*/


/*FUNCTION: Object image_treatment(Object search_image_inforrmation)
    Cette fonction analyse l'image qu'elle a recu via l'entree standard
    et recherche les informations qu'elle a recu en INPUT
*/
/*INPUT:
    Object search_image_inforrmation
        une structure de donnes possedants trois champs
        Le champs color contient la couleur recherchée
        Le champs shape contient la forme recherché
        Le contenue du champ position n'est pas important
*/
/*OUTPUT:
    Object
        une structure de donnée Object contenant:
        La couleur recherchée si elle a été trouvé
        La forme recherchée si elle a été trouvée
        Et la position de l'objet si les deux attributs ci dessus ont ete trouvée
*/
Object image_treatment(Object search_image_inforrmation);

