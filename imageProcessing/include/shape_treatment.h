#include "position_treatment.h"
#include <math.h>
/*Nou travaillerons par defaut en anglais.*/
/*La prise en compte de la langue sera faite par le module de simulation*/

/*TYPE: Shape*/
/*BALL or CUBE*/
typedef enum
{
    BALL,
    CUBE,
    NONE_SHAPE /*Si la forme ne correspond a aucune forme*/
} Shape;


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

typedef struct
{
    Position highest_pixel; /*premier pixel de l'image*/
    Position lowest_pixel; /*pixel le plus bas de l'image*/
}image_max_min_pixel;

/*FUNCTION:image_form
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

/*FUNCTION:get_image_best_point
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