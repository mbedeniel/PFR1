/*--------------------------------------------------------------------------------------------------------------------------------*/
/*------------------------------------------------ @author DEVELLOPER : MBEDE Niel -----------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------VERSION : 1.1---------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/
/*---------------------------------------------------- @date DATE : 22/01/2025 ---------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/


/** @brief
*-----------------------------------------------------------------------------------------------------------------------------------
*    MANAGEMENT OF THE "Color" STRUCTURE AND GET THE THE "Color" of an OBJECT IN THE IMAGE
*-----------------------------------------------------------------------------------------------------------------------------------
*/

#ifndef DEF_COLOR_TREATMENT 
#define DEF_COLOR_TREATMENT

/*
******************************************
********PARAMETRES DE CONFIGURATION*******
******************************************
*/

#define NUMBER_OF_COLOR 3 /*Nombre de couleur de Color*/
/*Nou travaillerons par defaut en anglais.*/
/*La prise en compte de la langue sera faite par le module de simulation*/

/*
    *Firstly we are in HSV(Hue Saturation Value)
    *H_MIN_COLOR_NAME : Hue minimum of the color COLOR_NAME
    *H_MAX_COLOR_NAME : Hue maximum og the color COLOR_NAME
    *S_COLOR_NAME : Saturation minimu of the color COLOR_NAME
*/
#define H_MIN_ORANGE 12
#define H_MAX_ORANGE 25
#define S_ORANGE 75.0
#define H_MIN_BLUE 205
#define H_MAX_BLUE 255
#define S_BLUE 55.0
#define H_MIN_YELLOW 33
#define H_MAX_YELLOW 55
#define S_YELLOW 55.0

/*
****************************************
********ENUMERATION ET STRUCTURES*******
****************************************
*/

/*TYPE: Color*/
/*RED or GREEN or BLUE*/
typedef enum
{
    ORANGE=0,
    YELLOW=1,
    BLUE=2,
    NONE_COLOR=3 /*pour marquer que la couleur ne matche avec aucune couleur*/
} Color;



/*
**************************************
********PROTOTYPE DES FONCTIONS*******
**************************************
*/


/*
FUNCTION : Color init_color()
    initialise une strcuture Color
*/
/*
INPUT: 
    @param NONE
*/
/*
@return 
OUTPUT: une structure Color
*/
Color init_color();



/*FUNCTION: bit_image
    on se base sur la saturation S 
    et la teinte H pour chercher la couleur search_color
    par segementation
*/
/*INPUT: 
    @param double *** image_hsv
        une image dans la base HSV
        ou H la premiere dimenssion
        S la seconde et V la troisiemme
    @param int nbr_pixel
        le nombre de pixel necessaire pour dire que la couleur est presente
    @param int ligne 
        Nombre de ligne de l'image d'une matrice des matrices du tenseur
    @param int column
         Nombre de colone de l'image d'une matrice des matrices du tenseur
    @param Color search_color
        la couleur recherchée
    @param int ** binary_image
        image issu de la binarisation de image_hsv
*/
/*@return 
OUTPUT: int
    return 
        on retourne le nombre de pixel presents dans l'image qui ont
        la couleur recherchée
 */
int bit_image(Color search_color,int ligne,int column,double *** image_hsv,int ** binary_image);



/*FUNCTION: Color get_color(int number)
    Cette fonction nous permet d'associer des Color a des nombres
    Nous aurions pu le faire directement lors de la definition
    Mais cela cause des problémes. Raison pour laquelle nous
    le realisons via une fonction
*/
/*INPUT:
    @param int number
        le numero correspondant da la Color que l'on veut(voir definition de l'enumeration)
*/
/*@return 
OUTPUT: Color 
    la Color correspondant au nombre recu (voir definition de l'enumeration)
*/
Color get_color(int number);



/*FUNCTION:const char* get_color_name(Color color)
    cette fontion retourne le nom de la couleur sous forme de chaine de caractère
*/

/*INPUT: 
    @param Color color
        en entrée elle prend la couleur dont on veut le nom

*/

/*@return 
OUTPUT: const char*
    en sortie elle retourne le nom de la couleur sous forme de chaine de caractère

*/
const char* get_color_name(Color color);

#endif