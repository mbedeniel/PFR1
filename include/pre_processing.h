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

