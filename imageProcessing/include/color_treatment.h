#include <stdio.h>
/*Nou travaillerons par defaut en anglais.*/
/*La prise en compte de la langue sera faite par le module de simulation*/

/*TYPE: Color*/
/*RED or GREEN or YELLOW*/
typedef enum colors
{
    RED,
    GREEN,
    BLUE,
    NONE_COLOR /*pour marquer que la couleur ne matche avec aucune couleur*/
} Color;

/*FUNCTION: bit_image
    on se base sur la saturation S 
    et la teinte H pour chercher la couleur search_color
    par segementation
*/
/*INPUT: 
    double *** image_hsv
        une image dans la base HSV
        ou H la premiere dimenssion
        S la seconde et V la troisiemme
    int nbr_pixel
        le nombre de pixel necessaire pour dire que la couleur est presente
    int ligne 
        Nombre de ligne de l'image d'une matrice des matrices du tenseur
    int column
         Nombre de colone de l'image d'une matrice des matrices du tenseur
    Color search_color
        la couleur recherchée
    int ** binary_image
        image issu de la binarisation de image_hsv
*/
/*OUTPUT: int
    return 
        on retourne le nombre de pixel presents dans l'image qui ont
        la couleur recherchée
 */
int bit_image(Color search_color,int ligne,int column,double *** image_hsv,int ** binary_image);