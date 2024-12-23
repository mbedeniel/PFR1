#include "../include/color_treatment.h"

Color init_color()
{
    return NONE_COLOR;
}

int bit_image(Color search_color,int ligne,int column,double *** image_hsv,int ** binary_image)
{
    /*ETAPE 1 CALIBRAGE DE LA TEINTE*/
    int pixel_h,pixel_s,s_min,condition,h_min,h_max,i,j,test=0;
    /*test permet de verifier si la couleur recherchée est presente dans l'image*/
    /*de plus test indique aussi le nombre de pixel qui on la couleur recherchée*/
    /*h_min represente la teinte (hue) minimum et h_max la tiente maximum*/
    switch (search_color)
    {
        case RED:
            h_min=315;
            h_max=15;
            s_min=0.0;
            break;
        case GREEN:
            h_min=105;
            h_max=155;
            s_min=0.0;
            break;
        case BLUE:
            h_min=205;
            h_max=255;
            s_min=55.0;
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
            /*la strcuture de la condition change suivant la couleur*/
            switch(search_color)
            {
                case RED:
                    condition=(pixel_h>=315 || pixel_h<=15)&&(pixel_s>=s_min); 
                    break;
                case BLUE:
                case GREEN:
                    condition=pixel_h>=h_min && pixel_h<=h_max && pixel_s>=s_min;
                    break;
                /*Dans ce cas on arrete la programme*/
                default :
                    return 0;
                   
            }
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


/* Fonctions auxiliaires */
const char* get_color_name(Color color) {
    switch (color) {
        case RED: return "RED";
        case GREEN: return "GREEN";
        case BLUE: return "BLUE";
        default: return "NONE_COLOR";
    }
}