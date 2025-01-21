#include "./include/image_interface.h"
#include <stdio.h>

int main()
{
    Object search_object,processed_object;
    Object patterns[NUMBER_OF_COLOR*NUMBER_OF_SHAPE];
    int i =0,size_patterns,number_valid_pattern,image_number,mode=0,color_shape;
    char path[35];
    /* recuperer les infos de l object sous format json*/
    char json_buffer[256]; /*Tampon pour la chaîne JSON*/



    /*Recuperation dumode*/
    printf("\n MODE : ");
    scanf("%i", &mode);


    /*Generation du Path vers l'image*/
    printf("\n PATH : ");
    scanf("%i", &image_number);
    snprintf(path, 200, "IMG_RGB_TEST/IMG_%i.txt", image_number);


    /*Collecte d'information pour la recherche*/
    search_object = init_object();

    if(mode==1) /* La couleur et la forme sont fournis*/
    {
        /*Recuperation de la couleur*/
        printf("\n COLOR : ");
        scanf("%i",&color_shape);
        /*Mise a jour de la couleur l'objet*/
        search_object.color = get_color(color_shape);

        /*Recuperation de la forme*/
        printf("\n SHAPE : ");
        scanf("%i",&color_shape);
        /*Mise a jour de la forme l'objet*/
        search_object.shape = get_shape(color_shape);

        /*Lancement du traitement et resultat*/
        number_valid_pattern=pattern_analyser(search_object,patterns,path);
        for(i=0;i<number_valid_pattern;i++)
        {
            /*------------------------------------*/
            /*ADD PYTHON FOR MARKING POSITION HEAR*/
            /*------------------------------------*/
            object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
            printf("\t %s \n",json_buffer);
        }
    }
    else if(mode==2) /*eul la forme est forunie*/
    {
        /*Recuperation de la forme*/
        printf("\n SHAPE : ");
        scanf("%i",&color_shape);
        /*Mise a jour de la couleur l'objet*/
        search_object.color = get_color(color_shape);

        /*Lancement du traitement et resultat*/
        number_valid_pattern=pattern_analyser(search_object,patterns,path);
        for(i=0;i<number_valid_pattern;i++)
        {
            /*------------------------------------*/
            /*ADD PYTHON FOR MARKING POSITION HEAR*/
            /*------------------------------------*/
            object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
            printf("\t %s \n",json_buffer);
        }
    }
    else if(mode==3) /*seul la couleur est fourni*/
    {
        /*Recuperation de la couleur*/
        printf("\nCOLOR : ");
        scanf("%i",&color_shape);
        /*Mise a jour de la couleur l'objet*/
        search_object.color = get_color(color_shape);

        /*Lancement du traitement et resultat*/
        number_valid_pattern=pattern_analyser(search_object,patterns,path);
        for(i=0;i<number_valid_pattern;i++)
        {
            /*------------------------------------*/
            /*ADD PYTHON FOR MARKING POSITION HEAR*/
            /*------------------------------------*/
            object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
            printf("\t %s \n",json_buffer);
        }
    }
    else /*Analyse complete de l'image*/
    {
        /*Lancement du traitement et resultat*/
        number_valid_pattern=pattern_analyser(search_object,patterns,path);
        for(i=0;i<number_valid_pattern;i++)
        {
            /*------------------------------------*/
            /*ADD PYTHON FOR MARKING POSITION HEAR*/
            /*------------------------------------*/
            object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
            printf("\t %s \n",json_buffer);
        }
    }
    
    return 0;
}