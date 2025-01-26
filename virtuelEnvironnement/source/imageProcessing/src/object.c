#include "./../include/object.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


/*--------------------------------------------------------------------------------------------------------------------------------*/
/*------------------------------------------------------------FUNCTION------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/

Object init_object()
{
    Object new_object;
    new_object.position=init_position();
    new_object.color=init_color();
    new_object.shape=init_shape();
    return new_object;
}

/*--------------------------------------------------------------------------------------------------------------------------------*/
/*------------------------------------------------------------FUNCTION------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/

Object create_object(Shape shape,Color color,Position position)
{
    Object new_object;
    new_object.color=color;
    new_object.shape=shape;
    new_object.position=position;
    return new_object;
}

/*--------------------------------------------------------------------------------------------------------------------------------*/
/*------------------------------------------------------------FUNCTION------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/

/* Fonction pour convertir un objet en JSON */
void object_to_json(const Object* obj, char* json_buffer, size_t buffer_size) {
    snprintf(
        json_buffer, buffer_size,
        "{ \"position\": { \"x\": %d, \"y\": %d }, \"shape\": \"%s\", \"color\": \"%s\" }",
        obj->position.x,
        obj->position.y,
        get_shape_name(obj->shape),
        get_color_name(obj->color)
    );
}