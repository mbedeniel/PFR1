#include "./include/image_interface.h"

int main()
{
    Object search_object,processed_object;

    search_object.shape=BALL;
    search_object.color=BLUE;

    processed_object = image_treatment(search_object);
    
    if(processed_object.color==search_object.color)
    {
        printf("Couleur trouvée \n");
    }
    else
    {
        printf("Couleur non trouvée \n");
    }

    if(processed_object.shape==search_object.shape)
    {
        printf("Forme trouvée \n");
    }
    else
    {
        printf("Forme non trouvée \n");
    }
   
    return 0;
}