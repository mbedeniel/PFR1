/*--------------------------------------------------------------------------------------------------------------------------------*/
/*-----------------------------------------------------DEVELLOPER : MBEDE Niel----------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------VERSION : 1.1---------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/
/*--------------------------------------------------------DATE : 22/01/2025-------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/


/*
-----------------------------------------------------------------------------------------------------------------------------------
    MANAGEMENT OF THE "Shape" STRUCTURE AND GET THE THE "Shape" of an OBJECT IN THE IMAGE
-----------------------------------------------------------------------------------------------------------------------------------
*/

#ifndef DEF_SHAPE_TREATMENT
#define DEF_SHAPE_TREATMENT

#include "position_treatment.h"
#include "pre_processing.h"
#include <math.h>

/*
******************************************
********PARAMETRES DE CONFIGURATION*******
******************************************
*/

#define NUMBER_OF_SHAPE 2/*nombre d'elment de Shape*/


/*
****************************************
********ENUMERATION ET STRUCTURES*******
****************************************
*/



/*Nou travaillerons par defaut en anglais.*/
/*La prise en compte de la langue sera faite par le module de simulation*/

/*TYPE: Shape*/
/*BALL or CUBE*/
typedef enum
{
    BALL=0,
    CUBE=1,
    NONE_SHAPE=2 /*Si la forme ne correspond a aucune forme*/
} Shape;



typedef struct
{
    Position highest_pixel; /*premier pixel de l'image(forme sur l'image)*/
    Position lowest_pixel; /*pixel le plus bas de l'image(forme sur l'image)*/
}image_max_min_pixel;



/*
**************************************
********PROTOTYPE DES FONCTIONS*******
**************************************
*/



/*
FUNCTION : Shape init_shape()
    initialise une strcuture Shape
*/
/*
INPUT: NONE
*/
/*
OUTPUT: une structure Shape
*/
Shape init_shape();



/*FUNCTION: double ratio_area(int nbr_pixel_image,image_max_min_pixel max_min_pixel,Shape search_shape)
    permet d'exprimer la presence d'une forme.
    Plus le resulats est proche de 01 plus il y a de chance que ce
    soit la forme cherché. En multipliant le resultat retourner par 100
    on obtient les chances que la forme soir presente en pourcentage
*/
/*INPUT:
    image_max_min_pixel max_min_pixel
        point le plus haut et point le plus bas de l'image
    int nbr_pixel_image
        nombre de pixel de l'image original
    Shape search_shape
        la forme que l'on recherche
*/
/*OUTPUT: 
    double
        ratio entre le nombre de pixel de l'image
        et le nombre de pixel de l'image rechercé.
        Voir doc de conception pour plus d'information
        Le ratio est exprimée en pourcentage
*/
double ratio_area(int nbr_pixel_image,image_max_min_pixel max_min_pixel,Shape search_shape);



/*FUNCTION: image_max_min_pixel get_image_best_point(int ** binary_image,int ligne,int column)
    retourne le point le plus haut et le point le plus bas de l'image
*/
/*INPUT:
    int ** binary_image
        l'image binarisé par bit_image
    int ligne
        nombre de ligne de binary_image
    int column
        nombre de colone de binary_image
*/
/*OUTPUT: 
    image_max_min_pixel
        structure contenant les coordonnées des deux points recherchés
*/
image_max_min_pixel get_image_best_point(int ** binary_image,int ligne,int column);



/*FUNCTION:const char* get_shape_name(Shape shape)

*/

/*INPUT: Shape shape
    
*/

/*OUTPUT: const char* 

*/
const char* get_shape_name(Shape shape);



/*FUNCTION: Shape get_shape(int number)
    Cette fonction nous permet d'associer des Shape a des nombres
    Nous aurions pu le faire directement lors de la definition
    Mais cela cause des problémes. Raison pour laquelle nous
    le realisons via une fonction
*/
/*INPUT:
    int number
        numéro de la Shape que l'on veut (voir definition de l'enumeration)
*/
/*OUTPUT: Shape 
    la Shape correspondant au nombre recu (voir definition de l'enumeration)
*/
Shape get_shape(int number);

#endif