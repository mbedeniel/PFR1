#include "./include/image_interface.h"
#include <stdio.h>

int main()
{
    Object search_object,processed_object;
    Object patterns[NUMBER_OF_COLOR*NUMBER_OF_SHAPE];
    int i =0,size_patterns,number_valid_pattern,image_number;
    char path[35];
    /* recuperer les infos de l object sous format json*/
    char json_buffer[256]; /*Tampon pour la chaîne JSON*/


    /*Path vers l'image*/
    scanf("%i", &image_number);
    snprintf(path, 200, "IMG_RGB_TEST/IMG_%i.txt", image_number);

    printf("\n%s\n",path);

    printf("\n\n\n OBJET AVANT LE TRAITEMENT \n");
    search_object = init_object();
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);
    printf("\n LES PATTERNS GENERÉES SONT : \n");
    size_patterns=pattern_generator(search_object,patterns);
    for(i=0;i<size_patterns;i++)
    {
        object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
        printf("\t %s \n",json_buffer);
    }
    printf("\n LES ANALYSES DES PATTERNS GENERÉES SONT : \n");
    number_valid_pattern=pattern_analyser(search_object,patterns,path);
    for(i=0;i<number_valid_pattern;i++)
    {
        object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
        printf("\t %s \n",json_buffer);
    }


    printf("\n\n\n OBJET AVANT LE TRAITEMENT \n");
    search_object = init_object();
    search_object.shape=BALL;
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);
    pattern_generator(search_object,patterns);
    printf("\n LES PATTERNS GENERÉES SONT : \n");
    size_patterns=pattern_generator(search_object,patterns);
    for(i=0;i<size_patterns;i++)
    {
        object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
        printf("\t %s \n",json_buffer);
    }
    printf("\n LES ANALYSES DES PATTERNS GENERÉES SONT : \n");
    number_valid_pattern=pattern_analyser(search_object,patterns,path);
    for(i=0;i<number_valid_pattern;i++)
    {
        object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
        printf("\t %s \n",json_buffer);
    }


    printf("\n\n\n OBJET AVANT LE TRAITEMENT \n");
    search_object = init_object();
    search_object.color=BLUE;
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);
    pattern_generator(search_object,patterns);
    printf("\n LES PATTERNS GENERÉES SONT : \n");
    size_patterns=pattern_generator(search_object,patterns);
    for(i=0;i<size_patterns;i++)
    {
        object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
        printf("\t %s \n",json_buffer);
    }
    printf("\n LES ANALYSES DES PATTERNS GENERÉES SONT : \n");
    number_valid_pattern=pattern_analyser(search_object,patterns,path);
    for(i=0;i<number_valid_pattern;i++)
    {
        object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
        printf("\t %s \n",json_buffer);
    }


    printf("\n\n\n OBJET AVANT LE TRAITEMENT \n");
    search_object = init_object();
    search_object.shape=BALL;
    search_object.color=BLUE;
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\t %s \n",json_buffer);
    pattern_generator(search_object,patterns);
    printf("\n LES PATTERNS GENERÉES SONT : \n");
    size_patterns=pattern_generator(search_object,patterns);
    for(i=0;i<size_patterns;i++)
    {
        object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
        printf("\t %s \n",json_buffer);
    }
    printf("\n LES ANALYSES DES PATTERNS GENERÉES SONT : \n");
    number_valid_pattern=pattern_analyser(search_object,patterns,path);
    for(i=0;i<number_valid_pattern;i++)
    {
        object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
        printf("\t %s \n",json_buffer);
    }






    /*search_object.shape=BALL;
    search_object.color=BLUE;

    processed_object = image_treatment(search_object,path);


    object_to_json(&processed_object, json_buffer, sizeof(json_buffer));
    printf("\n %s \n",json_buffer);




    
    
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