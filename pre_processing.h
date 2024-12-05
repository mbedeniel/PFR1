#define number_quantified_bit 2

//les fichiers images que nous traitons sont sous la forme :
//Trois matrice de meme taille 
//la premiere pour le rouge
//la seconde pour le vert
//la derniere pour le bleu

//quantification
//Au préalable, et afin de limiter les calculs, une quantification est nécessaire afin
//de ne retenir que les n bits de poids forts (n premières puissances de 2) pour
//chaque valeur d’intensité dans ces composantes couleurs (Rouge, Vert, Bleu)


//Definition d'une structure RVB
//contient la quantification d'une image
typedef struct {
    int R; //pixel rouge
    int V; //pixel vert
    int B; //pixel bleue
} RVB;


//fait la quantification (number_quantified_bit premier bit)
//OUTPUT: tableau a number_quantified_bit entier
//INPUT: pixel a quantifier
int* quantification(int pixel);



