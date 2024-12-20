#define NUMBER_QUANTIFIED_BIT 3

/*les fichiers images que nous traitons sont sous la forme*/
/*Trois matrice de meme taille*/ 
/*la premiere pour le rouge*/
/*la seconde pour le vert*/
/*la derniere pour le bleu*/

/*quantification*/
/*Au préalable, et afin de limiter les calculs, une quantification est nécessaire afin*/
/*de ne retenir que les n bits de poids forts (n premières puissances de 2) pour*/
/*chaque valeur d’intensité dans ces composantes couleurs (Rouge, Vert, Bleu)*/


/*Definition d'une structure RVB*/
/*contient la quantification d'une image*/
typedef struct {
    int R; /*pixel rouge*/
    int V; /*pixel vert*/
    int B; /*pixel bleue*/
} RVB;


/*fait la quantification (NUMBER_QUANTIFIED_BIT premier bit)*/
/*OUTPUT: NONE*/
/*INPUT: pixel a quantifier, adresse du tableau de qui contiendra le resultat*/
void quantification(int pixel,int* pixels);

/*INPUT: 
    int** pixel_images: une matrice contenant les pixel de l'image
    int** color_histograms: le tableau ou charge l'histogramme
    int ligne: nombre de ligne de pixel_images
    int column: nombre de colone de pixel_images
*/
/*OUTPUT: 
    int : le nombre de case rempli de l'histogramme    
*/
int color_histogram(int** pixel_images,int ligne,int column,double** color_histograms);


/*FUNCTION: rgb_to_hsb
    elle a pour role de
    faire passer une image de la base 
    RGB(Red Green Blue) a la base HSB(Hue Saturation Value)
    Une image dans la base RGB est une composition de 03 matrices.
    C'est un tenseur.

*/
/*INPUT: 
    int ligne 
        Nombre de ligne de l'image d'une matrice des matrices du tenseur
    int column
         Nombre de colone de l'image d'une matrice des matrices du tenseur
    int *** image_rgb
        image dans la base RGB que l'on veut passer dans la base HSB.
        Il s'agit d'un tenseur (tableau a trois dimenssion)
        Premire dimenssion pour rouge
        Deuxieme dimenssion pour le vert
        troisiemme dimenssion pour le bleu
    double *** image_hsv
        image obtenue du passage de l'image RGB dans la base HSB
        il s'agit d'un tenseur.
        Premiere dimenssion represente H
        la seconde dimenssion S
        la troisieme dimenssion V 
*/
/*OUTPUT: NONE*/
void rgb_to_hsv(int ligne,int column,double *** image_rgb,double *** image_hsv);


/*FUNTUION: max
    retourne le max entre trois double
*/
/*INPUT:
    double r,double g,double b
*/
/*OUTPUT: int max
    le max entre r, g et b
*/
double max(double r,double g,double b);



/*FUNTUION: max
    retourne le min entre trois double
*/
/*INPUT:
    double r,double g,double b
*/
/*OUTPUT: int max
    le min entre r, g et b
*/
double min(double r,double g,double b);
