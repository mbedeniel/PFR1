#include "../include/image_interface.h"

int pattern_analyser(Object searched_pattern, Object* image_objects)
{
    
    /*
    ****************************************
    ********DECLARATION DES VARIABLES*******
    ****************************************
    */
    Object patterns[NUMBER_OF_COLOR*NUMBER_OF_SHAPE];
    int i,size_patterns;
     
    /*
    **************************
    ********TRAITEMENT********
    **************************
    */

    /*ETAPE 1 : GENERATION DES PATTERNS*/
    size_patterns=pattern_generator(searched_pattern,patterns);


    /*ETAPE 2 : TRAITEMENT DES PATTERNS GENERÉES*/
    for(i=0;i<size_patterns;i++)
    {
        image_objects[i]=image_treatment(patterns[i]);
    }
    
    return size_patterns;
}

int pattern_generator(Object object, Object* match_patterns)
{
    int i,j,k,size_match_patterns=0;
    Color object_color=object.color;
    Shape object_shape=object.shape;
    if(object.color!=NONE_COLOR && object.shape!=NONE_SHAPE)
    {
        match_patterns[0]=object;
        size_match_patterns++;
        /*
        ICI c'est pour anticiper des erreurs car normalement on ne doit 
        pas appeler cette methode si la stucture a une couleur et une forme
        */
    }
    else if(object.color==NONE_COLOR && object.shape==NONE_SHAPE)
    {
        for(i=BALL,k=0;i<NUMBER_OF_SHAPE;i++)
        {
            for(j=RED;j<NUMBER_OF_COLOR;j++,k++)
            {
                match_patterns[k]=create_object(i,j,init_position());
                size_match_patterns++;
            }
        }
        /*ci dessous le contenue de object_configuration*/
        /*
        { "position": { "x": 0, "y": 0 }, "shape": "BALL", "color": "RED" }
        { "position": { "x": 0, "y": 0 }, "shape": "BALL", "color": "GREEN" }
        { "position": { "x": 0, "y": 0 }, "shape": "BALL", "color": "BLUE" }
        { "position": { "x": 0, "y": 0 }, "shape": "CUBE", "color": "RED" }
        { "position": { "x": 0, "y": 0 }, "shape": "CUBE", "color": "GREEN" }
        { "position": { "x": 0, "y": 0 }, "shape": "CUBE", "color": "BLUE" }
        */
    }
    else if(object_color!=NONE_COLOR)/*Couleur connue on genere donc les differentes formes*/
    {
        for(i=BALL;i<NUMBER_OF_SHAPE;i++)
        {
            match_patterns[i]=create_object(i,object_color,init_position());
            size_match_patterns++;
        }
    }
    else/*forme connue on genere donc les differentes couleurs*/
    {
        for(i=RED;i<NUMBER_OF_COLOR;i++)
        {
            match_patterns[i]=create_object(object_shape,i,init_position());
            size_match_patterns++;
        }
    }
    return size_match_patterns;
}

Object image_treatment(Object search_image_inforrmation)
{

    /*
    ****************************************
    ********DECLARATION DES VARIABLES*******
    ****************************************
    */


       system("cat ./IMG_RGB_TEST/IMG_5390.txt");
    int i,j,k,nbr_pixel,ligne,colonne;
    double *** image_hsv; /*image obtenu grace a rgb_to_hsv*/
    double *** image_rgb; /*image recupéré*/
    int ** binary_image; /*image obtebur grace a bit_image*/
    image_max_min_pixel max_min_pixel; /*le pixel au deux extremités suivant la hauteur*/
    double my_ratio_area;
    Object processed_image; 

    /*
    processed_image : resultat du traitement image
    i : variable d'incrementation suivant les lignes
    j : variable d'ncrementation suivant les colonnes
    k : variable d'incrementation suivant la profondeur
    nbr_pixel : nombre de pixel corespondant a la couleur cherchée
    ligne : nombre de ligne de la matrice dans la base RGB suivant R,G ou B
    colonne : nombre de colonne de la matrice dans la base RGB suivant R,G ou B
    image_hsv : image dans la base HSV
    image_rgb : image dans la base RGB
    */
    


    /*
    ***************************************
    ********RECUPERATION DES DONNES********
    ***************************************
    */
    


    /*Recuperation des lignes et colonnes*/
    scanf("%i",&ligne);
    scanf("%i",&colonne);



    /*
    ***************************************       system("cat ./IMG_RGB_TEST/IMG_5390.txt");
    ********DEFINITION DES VARIABLES*******
    ***************************************
    */

    /*Initialisation d'un Object*/
    processed_image=init_object();


    /*creation des tableaux*/

    /*Allocation des tableaux de pointeurs*/
    image_hsv = (double***)malloc(ligne*sizeof(double**));
    image_rgb = (double***)malloc(ligne*sizeof(double**));
    binary_image = (int**)malloc(ligne*sizeof(int*));

    /*allocation du tableau dynamique*/

    /*tableau image_hsv*/
    if (image_hsv!=NULL)
    {
        for(i=0;i<ligne;i++)
        {
            image_hsv[i] = (double**)malloc(colonne*sizeof(double*));
            if(image_hsv[i]==NULL)
            {
                fprintf(stderr,"ERREUR ALLOCATION");
                return processed_image;
            }
        }
        for(i=0;i<ligne;i++)
        {
            for(j=0;j<colonne;j++)
            {
                image_hsv[i][j] = (double*)malloc(3*sizeof(double));
                if(image_hsv[i][j]==NULL)
                {
                    fprintf(stderr,"ERREUR ALLOCATION");
                    return processed_image;
                }
            }
        }
    }
    else
    {
        fprintf(stderr,"ERREUR ALLOCATION");
        return processed_image;
    }
    

    /*tableau image_rgb*/
    if (image_rgb!=NULL)
    {
        for(i=0;i<ligne;i++)
        {

            image_rgb[i] = (double**)malloc(colonne*sizeof(double*));
            if(image_rgb[i]==NULL)
            {
                fprintf(stderr,"ERREUR ALLOCATION");
                return processed_image;
            }
        }
        for(i=0;i<ligne;i++)
        {
            for(j=0;j<colonne;j++)
            {
                image_rgb[i][j] = (double*)malloc(3*sizeof(double));
                if(image_rgb[i][j]==NULL)
                {
                    fprintf(stderr,"ERREUR ALLOCATION");
                    return processed_image;
                }
            }
        }
    }
    else
    {
        fprintf(stderr,"ERREUR ALLOCATION");
        return processed_image;
    }

    /*tableau binary_image*/
    if (binary_image!=NULL)
    {
        for(i=0;i<ligne;i++)
        {
            binary_image[i] = (int*)malloc(colonne*sizeof(int));
            if(binary_image[i]==NULL)
            {
                fprintf(stderr,"ERREUR ALLOCATION");
                return processed_image;
            }
        }
    }
    else
    {
        fprintf(stderr,"ERREUR ALLOCATION");
        return processed_image;
    }


    /*
    ***************************************
    ********RECUPERATION DES DONNES********
    ***************************************
    */


    /*RECUPERATION DE L'IMAGE EN RGB*/
    /*
    l'image est recupere composante par composante
    d'abord la composante R ensuite G ensuit B
    */
    for(k=0;k<3;k++)
    {   
        for(i=0;i<ligne;i++)
        {
            for(j=0;j<colonne;j++)
            {
                scanf("%lf",&image_rgb[i][j][k]);
            }
        }
    }



    /*
    **************************
    ********TRAITEMENT********
    **************************
    */



    /*DETERMINER L'IMAGE DANS LA BASE HSV*/
    rgb_to_hsv(ligne,colonne,image_rgb,image_hsv);

    

    /*------- DETECTION COULEUR -------*/

    /*DETERMINER L'IMAGE BINARISÉ*/
    switch(search_image_inforrmation.color)
    {
        case RED:
            nbr_pixel=bit_image(RED,ligne,colonne,image_hsv, binary_image);
            break;
        case BLUE:
            nbr_pixel=bit_image(BLUE,ligne,colonne,image_hsv, binary_image);
            break;
        case GREEN:
            nbr_pixel=bit_image(GREEN,ligne,colonne,image_hsv, binary_image);
            break;
        /*On peut envisager qu'on demande au robot d'avancer vers la balle*/
        default:
            break; 
    }

    /*ANALYSE DES RESULTATS ET MISE A JOUR DE processed_image*/
    if(nbr_pixel>=color_min_pixel)
    {
        processed_image.color=search_image_inforrmation.color;
    }

   /*------- DETECTION FORME ------*/


    max_min_pixel=get_image_best_point(binary_image,ligne,colonne);
    switch(search_image_inforrmation.shape)
    {
        case BALL:
            my_ratio_area=ratio_area(nbr_pixel,max_min_pixel,BALL);
            break;
        case CUBE:
            my_ratio_area=ratio_area(nbr_pixel,max_min_pixel,CUBE);
            break;
        /*On peut envisager qu'on demande au robot d'avancer vers l'objet rouge*/
        default:
            break; 
    }
    /*ANALYSE DES RESULTATS ET MISE A JOUR DE processed_image-*/
    if(my_ratio_area>=shape_min_percentage)
    {
        processed_image.shape=search_image_inforrmation.shape;
    }
    
    return processed_image;
}