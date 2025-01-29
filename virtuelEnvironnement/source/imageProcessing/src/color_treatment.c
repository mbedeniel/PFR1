#include "../include/color_treatment.h"

/*--------------------------------------------------------------------------------------------------------------------------------*/
/*------------------------------------------------------------FUNCTION------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/

Color init_color()
{
    return NONE_COLOR;
}

/*--------------------------------------------------------------------------------------------------------------------------------*/
/*------------------------------------------------------------FUNCTION------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/

int bit_image(Color search_color,int ligne,int column,double *** image_hsv,int ** binary_image)
{
    /*ETAPE 1 CALIBRAGE DE LA TEINTE*/
    int pixel_h,pixel_s,s_min,condition,h_min,h_max,i,j,test=0;
    /*test permet de verifier si la couleur recherchée est presente dans l'image*/
    /*de plus test indique aussi le nombre de pixel qui on la couleur recherchée*/
    /*h_min represente la teinte (hue) minimum et h_max la tiente maximum*/
    switch (search_color)
    {
        case ORANGE:
            h_min=H_MIN_ORANGE;
            h_max=H_MAX_ORANGE;
            s_min=S_ORANGE;
            break;
        case YELLOW:
            h_min=H_MIN_YELLOW;
            h_max=H_MAX_YELLOW;
            s_min=S_YELLOW;
            break;
        case BLUE:
            h_min=H_MIN_BLUE;
            h_max=H_MAX_BLUE;
            s_min=S_BLUE;
            break;
        /*Dans ce cas on arrete la programme*/
        default:
            return 0;
    }

    /*ETAPE 2 SEGMENTATION GRACE A LA TEINTE*/

    /*Nous regardons le tableau ligne par ligne*/
    /*Nous traitons que la composante H de chaque pixel*/
    /*On fait une binarisation de l'image*/
    for(i=0;i<ligne;i++)
    {
        for(j=0;j<column;j++)
        {
            pixel_h=image_hsv[i][j][0]; /*Composante suivnat la teinte du pixel*/
            pixel_s=image_hsv[i][j][1]; /*Composante suivant la saturation*/
            
            /*la strcuture de la condition ne change suivant la couleur*/
            /*meme traitement pour les couleurs*/
            condition=pixel_h>=h_min && pixel_h<=h_max && pixel_s>=s_min;
            if(condition)
            {
                binary_image[i][j]=1;
                /*on compte les pixel de la couleur recherchée*/
                test++;
            }
            else
            {
                 binary_image[i][j]=0;
            }
        }
    }
    return test;
}

/*--------------------------------------------------------------------------------------------------------------------------------*/
/*------------------------------------------------------------FUNCTION------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/

/* Fonctions auxiliaires */
const char* get_color_name(Color color) {
    switch (color) {
        case ORANGE: return "ORANGE";
        case YELLOW: return "YELLOW";
        case BLUE: return "BLUE";
        default: return "NONE_COLOR";
    }
}

/*--------------------------------------------------------------------------------------------------------------------------------*/
/*------------------------------------------------------------FUNCTION------------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/

Color get_color(int number)
{

    /*Si l'input etait de type Color,
        On aurait utulisé un switch
        mais la, c'est un int, donc
        le if est mieux adapté
    */
    if (number==ORANGE)
    {
        return ORANGE;
    }
    else if(number==BLUE)
    {
        return BLUE;
    }
    else if(number==YELLOW)
    {
        return YELLOW;
    }
    else
    {
        return NONE_COLOR;
    } 
}