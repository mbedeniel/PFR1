/*Nou travaillerons par defaut en anglais.*/
/*La prise en compte de la langue sera faite par le module de simulation*/

/*TYPE: Shape*/
/*BALL or CUBE*/
typedef enum
{
    BALL,
    CUBE
} Shape;

/*INPUT: char* path*/
/*Chemin relatif vers l'image*/
/*OUTPUT: char* */
/*element de type Shape representant la forme de l'objet*/
/*Shape image_form(char* path)*/
/* */
Shape image_form(char* path);