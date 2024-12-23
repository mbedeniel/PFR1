#include "./include/image_interface.h"
#include <stdio.h>

int main()
{
    Object search_object,processed_object;

    search_object.shape=BALL;
    search_object.color=BLUE;

    processed_object = image_treatment(search_object);

    // recuperer les infos de l object sous format json
    char json_buffer[256]; // Tampon pour la chaîne JSON

    object_to_json(&processed_object, json_buffer, sizeof(json_buffer));
    printf("%s",json_buffer);




    
    
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