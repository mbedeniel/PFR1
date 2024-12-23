#include "color_treatment.h"
#include "shape_treatment.h"


/*un objet est defini par sa position, sa forme et sa couleur*/
typedef struct 
{
    Position position;
    Shape shape;
    Color color;
} Object;


/*
FUNCTION : Object init_object();
    initialise une strcuture Object
*/
/*
INPUT: NONE
*/
/*
OUTPUT: une structure Object
*/
Object init_object();