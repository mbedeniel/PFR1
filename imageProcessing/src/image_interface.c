#include "./../include/image_interface.h"

Objects image_treatment(const Object search_image_inforrmation,const char* path)
{
    /*
    ****************************************
    ********DECLARATION DES VARIABLES*******
    ****************************************
    */

    int i,j,k,nbr_pixel,ligne,colonne;
    double *** image_hsv; /*image obtenu grace a rgb_to_hsv*/
    double *** image_rgb; /*image recupéré*/
    int ** binary_image; /*image obtebur grace a bit_image*/
    Object * object_array; /*tableau d'objets*/
    Objects processed_images; /*les differents resultats du traitement de l'image*/
    image_max_min_pixel max_min_pixel; /*le pixel au deux extremités suivant la hauteur*/
    double my_ratio_area;
    Object processed_image; 
    FILE* fichier;/*Lecture du ficheir image*/
    char command[256]; /* Ajout d'un croix avec un script python*/
    int result; /* Resultat de l'appel*/
    int nombre_objet;
    MA_FILE file_image;

    /*
    processed_image : resultat du traitement d'une image contenant un seul objet
    processed_images : resultat du traitement d'une image 
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
    ********DEFINITION DES VARIABLES*******
    ***************************************
    */

    /*Initialisation d'un Object*/
    processed_image=init_object();
    processed_images=init_objects();
    INIT_FILE(&file_image);



    /*
    ***************************************
    ********RECUPERATION DES DONNES********
    ***************************************
    */
    


    /*Recuperation des lignes et colonnes*/

    /*Ouvrir le fichier en lecture*/
    fichier = fopen(path, "r");
    if (!fichier) {
        perror("ERREUR DE LECTURE");
        return processed_images;
    }

    /*Lire les dimensions de l'image*/
    fscanf(fichier, "%i", &ligne);
    fscanf(fichier, "%i", &colonne);


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
                return processed_images;
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
                    return processed_images;
                }
            }
        }
    }
    else
    {
        fprintf(stderr,"ERREUR ALLOCATION");
        return processed_images;
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
                return processed_images;
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
                    return processed_images;
                }
            }
        }
    }
    else
    {
        fprintf(stderr,"ERREUR ALLOCATION");
        return processed_images;
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
                return processed_images;
            }
        }
    }
    else
    {
        fprintf(stderr,"ERREUR ALLOCATION");
        return processed_images;
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

    /*Lire les valeurs du fichier*/
    for (k = 0; k < 3; k++){
        for (i = 0; i < ligne; i++) {
            for (j = 0; j < colonne; j++) {
                fscanf(fichier, "%lf", &image_rgb[i][j][k]);
            }
        }
    }

    fclose(fichier); /*Fermer le fichier*/

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
        case ORANGE:
            nbr_pixel=bit_image(ORANGE,ligne,colonne,image_hsv, binary_image);
            break;
        case YELLOW:
            nbr_pixel=bit_image(YELLOW,ligne,colonne,image_hsv, binary_image);
            break;
        case BLUE:
            nbr_pixel=bit_image(BLUE,ligne,colonne,image_hsv, binary_image);
            break;
        /*On peut envisager qu'on demande au robot d'avancer vers la balle*/
        default:
            break;
    }
    if(nbr_pixel>=COLOR_MIN_PIXEL)
    {
        processed_image.color=search_image_inforrmation.color;
    }

    /*------- FILTRAGE DE L'IMAGE -------*/

    image_filter(binary_image,ligne,colonne);
 

    


   /*------- SEGMENTATION DE L IMAGE -------*/

    nombre_objet = segmentation_img_b(binary_image, 6,COLOR_MIN_PIXEL, ligne, colonne,&file_image);
    printf("\n NOMBRE OBJECT : %i",nombre_objet);
    /*printf("\nnombre d'objet = %i\n",nombre_objet);*/

    object_array = create_object_array(nombre_objet);
    if(object_array==NULL)
    {
        fprintf(stderr,"ERREUR ALLOCATION");
        return processed_images; /*On aurrait pu retourner NULL*/
        /*Mais on a initalisé processed_images donc c'est beaucoup mieux ainsi*/
    }


    /*recuperation des differents images abtenue aprés segmentation*/
    binary_image = DEFILER(&file_image);

   

    for(i=0;binary_image != NULL;i++,binary_image = DEFILER(&file_image)){

        /*if(i>0){
             for(i=0;i<ligne;i++)
            {
                for(j=0;j<colonne;j++)
                {
                    printf("%i\t",binary_image[i][j]);
                }
                printf("\n");
            }
        }*/

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
            /*On peut envisager qu'on demande au robot d'avancer vers l'objet bleue*/
            default:
                break;
        }
        /*ANALYSE DES RESULTATS ET MISE A JOUR DE processed_image-*/
        if(my_ratio_area>=SHAPE_MIN_PERCENTAGE)
        {
            processed_image.shape=search_image_inforrmation.shape;
        }
        else
        {
            processed_image.shape=NONE_SHAPE;
        }

        /*------- DETECTION POSITION ------*/
        processed_image.position=get_pixel_position(max_min_pixel.lowest_pixel);

        /*Prépare la commande pour exécuter le script Python*/
        /*Appel du programme python pour marqué une croix a la position detectée*/
        /*snprintf(command, sizeof(command), "python3 ../python/ajout_croix.py %s %s %s", path, processed_image.position.x, processed_image.position.y);
        result = system(command);*/


        /*------- RECUPERATION DES RESULTATS ------*/
        object_array[i]=processed_image;

        /*recuperation des differents images abtenue aprés segmentation*/
    }
    
    processed_images.count_element = nombre_objet;
    processed_images.table = object_array;

    return processed_images;
}

int pattern_analyser(const Object searched_pattern, Objects * image_objects,const char * path)
{
    
    /*
    ****************************************
    ********DECLARATION DES VARIABLES*******
    ****************************************
    */
    Object patterns[NUMBER_OF_COLOR*NUMBER_OF_SHAPE];
    Objects pattern_array;
    int i,j,size_patterns,size_image_objects=0;
    Object pattern;
     
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
        pattern_array=image_treatment(patterns[i],path);

        /*for(j=0;j<pattern_array.count_element;j++)
        {
            pattern = pattern_array.table[j]; /*Recuperation des resultats*/
            /*
            On ne retient que les patterns complets
            On peut tout de meme retirer ce if pour une analyse de l'image beaucoup plus large
            De facon a detecter des objets qui ne sont ni des balles ni des carré
            */
            /*if(pattern.color!=NONE_COLOR && pattern.shape!=NONE_SHAPE)
            {
                image_objects[size_image_objects]=pattern;
                size_image_objects++;
            }
        }*/
       image_objects[i] = pattern_array;
       size_image_objects++;
        
    }
    
    return size_image_objects;
}

int pattern_generator(const Object object, Object* match_patterns)
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
            for(j=ORANGE;j<NUMBER_OF_COLOR;j++,k++)
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
        for(i=ORANGE;i<NUMBER_OF_COLOR;i++)
        {
            match_patterns[i]=create_object(object_shape,i,init_position());
            size_match_patterns++;
        }
    }
    return size_match_patterns;
}
