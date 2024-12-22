#include "../include/color_treatment.h"
int bit_image(Color search_color,int ligne,int column,double *** image_hsv,int ** binary_image)
{
    /*ETAPE 1 CALIBRAGE DE LA TEINTE*/
    int pixel_h,condition,h_min,h_max,i,j,test=0;
    /*test permet de verifier si la couleur recherchée est presente dans l'image*/
    /*de plus test indique aussi le nombre de pixel qui on la couleur recherchée*/
    /*h_min represente la teinte (hue) minimum et h_max la tiente maximum*/
    switch (search_color)
    {
        case RED:
            h_min=315;
            h_max=15;
            break;
        case GREEN:
            h_min=105;
            h_max=155;
            break;
        case BLUE:
            h_min=205;
            h_max=255;
            break;
        /*Dans ce cas on arrete la programme*/
        default:
            fprintf(stderr,"\n \n \n \t ERROR COULEUR NON PRISE EN CHARGE \n \n \n");
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
            
            /*la strcuture de la condition change suivant la couleur*/
            switch(search_color)
            {
                case RED:
                    condition=pixel_h>315 || pixel_h<15; 
                    break;
                default:
                    condition=pixel_h>=h_min && pixel_h<=h_max;
                    break;   
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