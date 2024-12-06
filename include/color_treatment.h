/*Nou travaillerons par defaut en anglais.*/
/*La prise en compte de la langue sera faite par le module de simulation*/

/*TYPE: Color*/
/*RED or GREEN or YELLOW*/
typedef enum
{
    RED,
    GREEN,
    BLUE
} Color;

/*INPUT: char* path*/
/*Chemin relatif vers l'image*/
/*OUTPUT: char* */
/*element de type Color representant la couleur de l'objet*/
/*Color image_color(char* path)*/
/*Donne la couleur dominante sur l'image traitée*/
Color image_color(char[] path);