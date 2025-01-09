#include "./include/image_interface.h"
#include <stdio.h>

int main()
{
    Object search_object,processed_object;
    Object patterns[NUMBER_OF_COLOR*NUMBER_OF_SHAPE];
    int i =0;
    /* recuperer les infos de l object sous format json*/
    char json_buffer[256]; /*Tampon pour la chaîne JSON*/

    printf("\n\n\n OBJET AVANT LE TRAITEMENT \n");
    search_object = init_object();
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);
    generate_pattern(search_object,patterns);
    printf("\n LES PATTERNS GENERÉES SONT : \n");
    for(i=0;i<NUMBER_OF_COLOR*NUMBER_OF_SHAPE;i++)
    {
        object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
        printf("\t %s \n",json_buffer);
    }

    printf("\n\n\n OBJET AVANT LE TRAITEMENT \n");
    search_object = init_object();
    search_object.shape=BALL;
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);
    generate_pattern(search_object,patterns);
    printf("\n LES PATTERNS GENERÉES SONT : \n");
    for(i=0;i<NUMBER_OF_COLOR;i++)
    {
        object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
        printf("\t %s \n",json_buffer);
    }

    printf("\n\n\n OBJET AVANT LE TRAITEMENT \n");
    search_object = init_object();
    search_object.shape=CUBE;
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);
    generate_pattern(search_object,patterns);
    printf("\n LES PATTERNS GENERÉES SONT : \n");
    for(i=0;i<NUMBER_OF_COLOR;i++)
    {
        object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
        printf("\t %s \n",json_buffer);
    }

    printf("\n\n\n OBJET AVANT LE TRAITEMENT \n");
    search_object = init_object();
    search_object.color=RED;
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);
    generate_pattern(search_object,patterns);
    printf("\n LES PATTERNS GENERÉES SONT : \n");
    for(i=0;i<NUMBER_OF_SHAPE;i++)
    {
        object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
        printf("\t %s \n",json_buffer);
    }

    printf("\n\n\n OBJET AVANT LE TRAITEMENT \n");
    search_object = init_object();
    search_object.color=BLUE;
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);
    generate_pattern(search_object,patterns);
    printf("\n LES PATTERNS GENERÉES SONT : \n");
    for(i=0;i<NUMBER_OF_SHAPE;i++)
    {
        object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
        printf("\t %s \n",json_buffer);
    }

    printf("\n\n\n OBJET AVANT LE TRAITEMENT \n");
    search_object = init_object();
    search_object.color=GREEN;
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);
    generate_pattern(search_object,patterns);
    printf("\n LES PATTERNS GENERÉES SONT : \n");
    for(i=0;i<NUMBER_OF_SHAPE;i++)
    {
        object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
        printf("\t %s \n",json_buffer);
    }

    printf("\n\n\n OBJET AVANT LE TRAITEMENT \n");
    search_object = init_object();
    search_object.shape=CUBE;
    search_object.color=RED;
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);
    generate_pattern(search_object,patterns);
    printf("\n LES PATTERNS GENERÉES SONT : \n");
    object_to_json(&patterns[0], json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);

    printf("\n\n\n OBJET AVANT LE TRAITEMENT \n");
    search_object = init_object();
    search_object.shape=CUBE;
    search_object.color=BLUE;
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);
    generate_pattern(search_object,patterns);
    printf("\n LES PATTERNS GENERÉES SONT : \n");
    object_to_json(&patterns[0], json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);

    printf("\n\n\n OBJET AVANT LE TRAITEMENT \n");
    search_object = init_object();
    search_object.shape=CUBE;
    search_object.color=GREEN;
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);
    generate_pattern(search_object,patterns);
    printf("\n LES PATTERNS GENERÉES SONT : \n");
    object_to_json(&patterns[0], json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);

    printf("\n\n\n OBJET AVANT LE TRAITEMENT \n");
    search_object = init_object();
    search_object.shape=BALL;
    search_object.color=BLUE;
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);
    generate_pattern(search_object,patterns);
    printf("\n LES PATTERNS GENERÉES SONT : \n");
    object_to_json(&patterns[0], json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);

    printf("\n\n\n OBJET AVANT LE TRAITEMENT \n");
    search_object = init_object();
    search_object.shape=BALL;
    search_object.color=RED;
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);
    generate_pattern(search_object,patterns);
    printf("\n LES PATTERNS GENERÉES SONT : \n");
    object_to_json(&patterns[0], json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);

    printf("\n\n\n OBJET AVANT LE TRAITEMENT \n");
    search_object = init_object();
    search_object.shape=BALL;
    search_object.color=GREEN;
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);
    generate_pattern(search_object,patterns);
    printf("\n LES PATTERNS GENERÉES SONT : \n");
    object_to_json(&patterns[0], json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);






    /*search_object.shape=BALL;
    search_object.color=BLUE;

    processed_object = image_treatment(search_object);


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
    }*/
    
    return 0;
}