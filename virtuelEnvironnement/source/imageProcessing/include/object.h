/*--------------------------------------------------------------------------------------------------------------------------------*/
/*------------------------------------------------ @author DEVELLOPER : MBEDE Niel -----------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------VERSION : 1.0---------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/
/*---------------------------------------------------- @date DATE : 24/12/2024----------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/


/** @brief
*-----------------------------------------------------------------------------------------------------------------------------------
*    MANAGEMENT OF THE "Object" STRUCTURE 
*-----------------------------------------------------------------------------------------------------------------------------------
*/

#ifndef DEF_OBJECT
#define DEF_OBJECT

#include "color_treatment.h"
#include "shape_treatment.h"
#include <stdio.h>


/*
****************************************
********ENUMERATION ET STRUCTURES*******
****************************************
*/

/*un objet est defini par sa position, sa forme et sa couleur*/
typedef struct 
{
    Position position;
    Shape shape;
    Color color;
} Object;



/*
**************************************
********PROTOTYPE DES FONCTIONS*******
**************************************
*/


/*
FUNCTION : Object init_object()
    initialise une strcuture Object
*/
/*
INPUT: 
    @param NONE
*/
/*
@return 
OUTPUT: une structure Object
*/
Object init_object();



/*FUNCTION : Object create_object(Position position, Shape shape, Color color)
    crerr un objet
*/
/*INPUT :
    @param Position psotion
        la position a donner a l'objet
    @param Shape shape 
        la forme a donner a l'objet
    @param Color color
        la couleur a donner a l'objet
*/
/*@return 
OUTPUT:
    retourne l'objet creé
*/
Object create_object(Shape shape,Color color,Position position);



/*FUNCTION:void object_to_json(const Object* obj, char* json_buffer, size_t buffer_size)
    
*/

/*INPUT: 
    @param Cette fonction prend en entrée un objet et un buffer de taille buffer_size
*/

/*@return 
OUTPUT: void
    Elle copie les informations de l'objet dans le buffer sous forme de chaine de caractère
*/
void object_to_json(const Object* obj, char* json_buffer, size_t buffer_size);

#endif