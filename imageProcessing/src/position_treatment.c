#include "./../include/position_treatment.h"

Position init_position()
{
    Position new_position;
    new_position.x=0;
    new_position.y=0;
    return new_position;
}

Position get_pixel_position(Position lowest_pixel)
{
    /*
    Nous aurons pu ne pas mettre cette fonction
    car elle n'effectue aucun calcul. Mais nous avons decidé 
    de la mettre car nous utiliserons cette architecture au PFR2 
    Et des calculs seront reelement realisées dans cette fonction
    */
    return lowest_pixel;
}