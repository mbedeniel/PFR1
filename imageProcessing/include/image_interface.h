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
Object image_treatment(Object search_image_inforrmation,const char* path);

/*FUNCTION: int pattern_analyser(Object searched_pattern, Object* image_objects);
    analyse le paatern recherché. Par exemple,
    On peut demander au robot d'avancer vers la balle. On remarque  qu'on n'a pas preciser la couleur.
    Il faudra donc regerder si il y a un objet ROUGE, VERT ou BLEU qui est une balle. De meme,
    On peut aussi demander au robot d'avancer vers la l'objet bleu. La forme n'a pas été precisé.
    On peut tout aussi parler d'objet, donc ne pas preciser la forme et la couleur. 
    Les pattern qui matche serons chargé dans un tableau
*/
/*INPUT:
    Object searched_pattern
        une structure de donnes possedants trois champs
        Le champs color contient la couleur recherchée
        Le champs shape contient la forme recherché
        Le contenue du champ position n'est pas important
    Object* image_objects
        L'adresse d'un tableau. Il contiendra les objects present dans l'image qui matchent avec le  pattern
    char * path
        chemin d'access vers l'image
*/
/*OUTPUT:
    int : le resultata de l'analyse de tout les pattern ayant matché
        Le processu est le suivant :
            ->pattern_generator() génére tout les patterns qui matchent avec l'objet
            ->pattern_analyser() envoi chaque pattern a image_treatement() 
            ->pour chaque pattern image_treatment() renvoi le resultat
*/
int pattern_analyser(Object searched_pattern, Object* image_objects, char * path);

/*FUNCTION : int pattern_generator(Object object, Object* patterns);
    genere les differents patters correspondant a une structure de donnée.
    Par exemple si on cherche un objet ROUGE, les differente possibbilités sont:
    un CUBE rouge ou une BALLE rouge. Pareil si l'on cherche un CUBE. Les possibilitée sont :
    un CUBE ROUGE, VERT ou BLEUE. 
    NB, ici on ne s'interesse pas au fait qu'il soit present sur l'image ou pas 
*/
/*INPUT:
    Object object
        une stucture contenant le pattern rechrché
    Object* patterns
        un tableau ou stocker les patterns qui matche
    char * path
        hemin d'access vers l'image
*/
/*OUTPUT:
    int
        nombre de pattern qu on matché
*/
int pattern_generator(Object object, Object* patterns);