/* la structure Position qui contient les coordonnées x et y d'un objet*/
typedef struct 
{
    int x; /*ligne occupée dans la matrice de pixel*/
    int y; /*colonne occupée dans la matrice de pixel*/
} Position;


/*
FUNCTION : Position init_position()
    initialise une strcuture Position
*/
/*
INPUT: NONE
*/
/*
OUTPUT: une structure Position
*/
Position init_position();