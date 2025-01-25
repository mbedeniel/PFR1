#ifndef DEF_OBJECT
#define DEF_OBJECT
#include "color_treatment.h"
#include "shape_treatment.h"


/*un objet est defini par sa position, sa forme et sa couleur*/
typedef struct 
{
    Position position;
    Shape shape;
    Color color;
} Object;

/*Un Objects est defini par l'adresse d'un tableau d'objet et le nombre d'element contenue dans le tableau*/
typedef struct 
{
    int count_element; /*Le nombre d'element dans le tableau*/
    Object * table; /*l'adresse d'un tableau d'objet*/
}Objects;


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


/*FUNCTION : Object create_object(Position position, Shape shape, Color color);
    crerr un objet
*/
/*INPUT :
    Position psotion
        la position a donner a l'objet
    Shape shape 
        la forme a donner a l'objet
    Color color
        la couleur a donner a l'objet
*/
/*OUTPUT:
    retourne l'objet creé
*/
Object create_object(Shape shape,Color color,Position position);

/*
FUNCTION : Object init_objects();
    initialise une strcuture Object
*/
/*
INPUT: NONE
*/
/*
OUTPUT: une structure Objects
*/
Objects init_objects();

/*FUNCTION : Object * create_objects_array(int size)
    crerr un tableau d'objets dynamiquement
*/
/*INPUT :
    size
        la taille du tableau
*/
/*OUTPUT:
    retourne le tableau d'objet creé si il a pu etre créé
    ou retourne NULL
*/
Object * create_object_array(int size);


/*FUNCTION:void object_to_json(const Object* obj, char* json_buffer, size_t buffer_size)
    
*/

/*INPUT: 
    Cette fonction prend en entrée un objet et un buffer de taille buffer_size
*/

/*OUTPUT: void
    Elle copie les informations de l'objet dans le buffer sous forme de chaine de caractère
*/
void object_to_json(const Object* obj, char* json_buffer, size_t buffer_size);
#endif