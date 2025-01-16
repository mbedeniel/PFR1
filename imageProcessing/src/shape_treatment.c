#include "../include/shape_treatment.h"

Shape init_shape()
{
    return NONE_SHAPE;
}

double ratio_area(int nbr_pixel_image,image_max_min_pixel max_min_pixel,Shape search_shape)
{
    /*Le nombre de pixel suivant les lignes compris entre 02 pixel p1(x1,y1) et p2(x2,y2)
    est donné par nb_y=abs(y1-y2)+1
    */
    double height, width, distance,cercle_area,square_area_1,square_area_2,square_ratio_1,square_ratio_2;
    height=max_min_pixel.lowest_pixel.y-max_min_pixel.highest_pixel.y+1;
    width=max_min_pixel.lowest_pixel.x-max_min_pixel.highest_pixel.x+1;
    distance = sqrt(pow(height,2)+pow(width,2));
    switch (search_shape)
    {
    case BALL:
        cercle_area=(pow(((double)height)/2.0,2)*3.14);
        if(nbr_pixel_image<cercle_area)
        {
            return 100*((double)nbr_pixel_image)/cercle_area;
        }
        return 100*cercle_area/((double)nbr_pixel_image);
    case CUBE:
        square_area_1=(double)pow(distance/sqrt(2),2);
        square_area_2=pow(height,2);
        if(nbr_pixel_image<square_area_1)
        {
            square_ratio_1=100*((double)nbr_pixel_image)/square_area_1;
        }
        else
        {
            square_ratio_1=100*square_area_1/((double)nbr_pixel_image);
        }
        if(nbr_pixel_image<square_area_2)
        {
            square_ratio_2=100*((double)nbr_pixel_image)/square_area_2;
        }
        else
        {
            square_ratio_2=100*square_area_2/((double)nbr_pixel_image);
        }
        if(square_ratio_1<square_ratio_2)
        {
            return square_ratio_1;
        }
        return square_ratio_2;
        
    /*on arrete directement la fonction en retournant un ratio impossible*/
    default:
        return 0.0;
    }
}

image_max_min_pixel get_image_best_point(int ** binary_image,int ligne,int column)
{
    int i,j,pixel,test=1;
    image_max_min_pixel max_min_pixel;
    Position max_pixel,min_pixel;
    for (i=0;i<ligne;i++)
    {
        for(j=0;j<column;j++)
        {
            pixel=binary_image[i][j];
            /*recuperation du premier pixel de l'image*/
            if(pixel && test)
            {
                max_pixel.x=j;
                max_pixel.y=i;
                test=0;
            }
            /*recuperation du dernier pixel de l'image*/
            if(pixel)
            {
                min_pixel.x=j;
                min_pixel.y=i;
            }
        }
    }
    max_min_pixel.highest_pixel=max_pixel;
    max_min_pixel.lowest_pixel=min_pixel;
    return max_min_pixel;
}

int segmentation(const int ** image, int ligne, int colonne, int ** segmented_image)
{
    int i,j,pixel,top_pixel,left_pixel;
    /*
        pixel : un pixel de l'image
        
    */
    /*ETAPE 1: initialiser le padding*/
    add_padding(segmented_image,ligne+2,colonne+2,1);

    /*ETAPE 2: recopie de image*/
    for(i=0;i<ligne;i++)
    {
        for(j=0;j<colonne;j++)
        {
            segmented_image[i+1][j+1]=image[i][j];
        }
    }

    /*ETAPE 3:traitement*/
    for(i=1;i<ligne+1;i++)
    {
        for(j=1;j<colonne+1;j++)
        {
            pixel=segmented_image[i][j];
            if()
        }
    }
}


const char* get_shape_name(Shape shape) {
    switch (shape) {
        case BALL: return "BALL";
        case CUBE: return "CUBE";
        default: return "NONE_SHAPE";
    }
}