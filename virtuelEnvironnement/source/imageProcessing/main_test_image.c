#include "./include/image_interface.h"

/*--------------------------------------------------------------------------------------------------------------------------------*/
/*------------------------------------------------------------FUNCTION------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/

int main()
{
    Object search_object;
    Object patterns[NUMBER_OF_COLOR*NUMBER_OF_SHAPE];
    int i =0,number_valid_pattern,mode=0,color_shape;
    char path[35];
    char image_name[15];


    /* recuperer les infos de l object sous format json*/
    char json_buffer[256]; /*Tampon pour la chaîne JSON*/
    

    /*Affichege pour l'utilisateur*/
    user_interface(MODE_MENU);

    /*Recuperation du mode*/
    scanf("%i", &mode);

    if(mode==0) /*Arret du programme*/
    {
        return 0;
    }


    /*Affichege pour l'utilisateur*/
    user_interface(PATH_MENU);

    /*Generation du Path vers l'image*/
    scanf("%14s",image_name);/*Limiter la taille a 14 caractere pour laisser la place au /O*/
    snprintf(path, 200, "IMG_RGB_TEST/%s.txt", image_name);


    /*Initialisation de l'objet de la recherche*/
    search_object = init_object();

    /*Collecte d'information pour la recherche*/

    if(mode==1) /* La couleur et la forme sont fournis*/
    {
        /*Affichege pour l'utilisateur*/
        user_interface(COLOR_MENU);
        /*Recuperation de la couleur*/
        scanf("%i",&color_shape);
        /*Mise a jour de la couleur l'objet*/
        search_object.color = get_color(color_shape);

        /*Affichege pour l'utilisateur*/
        user_interface(SHAPE_MENU);
        /*Recuperation de la forme*/
        scanf("%i",&color_shape);
        /*Mise a jour de la forme l'objet*/
        search_object.shape = get_shape(color_shape);
    }
    else if(mode==2) /*seul la forme est forunie*/
    {
        /*Affichege pour l'utilisateur*/
        user_interface(SHAPE_MENU);
        /*Recuperation de la forme*/
        scanf("%i",&color_shape);
        /*Mise a jour de la couleur l'objet*/
        search_object.color = get_color(color_shape);
    }
    else if(mode==3) /*seul la couleur est fourni*/
    {
        /*Affichege pour l'utilisateur*/
        user_interface(COLOR_MENU);
        /*Recuperation de la couleur*/
        scanf("%i",&color_shape);
        /*Mise a jour de la couleur l'objet*/
        search_object.color = get_color(color_shape);
    }


    /*Lancement du traitement et resultat*/

    printf("\n SEARCHING ... ");
    object_to_json(&search_object, json_buffer, sizeof(json_buffer));
    printf("\n \t %s \n",json_buffer);
    number_valid_pattern=pattern_analyser(search_object,patterns,path);
    printf("\n RESULTS FOR IMAGE %s : \n",path);
    for(i=0;i<number_valid_pattern;i++)
    {
        object_to_json(&patterns[i], json_buffer, sizeof(json_buffer));
        printf("\n \t %i. %s \n",i+1,json_buffer);
    }
    
    return 0;
}