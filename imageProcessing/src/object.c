#include "./../include/object.h"

Object init_object()
{
    Object new_object;
    new_object.position=init_position();
    new_object.color=init_color();
    new_object.shape=init_shape();
    return new_object;
}