#include "./../include/object.h"
#include <stdio.h>
#include <string.h>

Object init_object()
{
    Object new_object;
    new_object.position=init_position();
    new_object.color=init_color();
    new_object.shape=init_shape();
    return new_object;
}

Object create_object(Shape shape,Color color,Position position)
{
    Object new_object;
    new_object.color=color;
    new_object.shape=shape;
    new_object.position=position;
    return new_object;
}

Objects init_objects()
{
    Objects new_objects;
    new_objects.count_element=0;
    new_objects.table=NULL;
    return new_objects;
}

Object * create_object_array(int size)
{
    Object * object_array = (Object *)malloc(sizeof(Object)*size);
    return object_array;
}


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