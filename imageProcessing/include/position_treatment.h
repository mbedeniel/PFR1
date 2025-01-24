#ifndef DEF_POSITION_TREATMENT
#define DEF_POSITION_TREATMENT
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

/*
FUNCTION : Position get_pixel_position()
    calcul les coordonnées du point le plus bas de l'objet recherché
    l'unité etant le pixel
*/
/*
INPUT: 
    Position lowest_pixel
        pixel le plus bas de la forme sur l'image qui a la couleur rechrchée
*/
/*
OUTPUT: Position 
    le pixel le plus bas de la forme recherchée
*/
Position get_pixel_position(Position lowest_pixel);
#endif