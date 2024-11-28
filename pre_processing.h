/*quantification*/
/*Au préalable, et afin de limiter les calculs, une quantification est nécessaire afin
de ne retenir que les n bits de poids forts (n premières puissances de 2) pour
chaque valeur d’intensité dans ces composantes couleurs (Rouge, Vert, Bleu)*/

/*Definition d'une structure RVB*/
/*contient la quantification d'une image*/
typedef struct {
    int R; /*pixel rouge*/
    int V; /*pixel vert*/
    int B; /*pixel bleue*/
} RVB;

