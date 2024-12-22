#include "../include/shape_treatment.h"

double ratio_area(int nbr_pixel_image,image_max_min_pixel max_min_pixel,Shape search_shape)
{
    int height=max_min_pixel.lowest_pixel.y-max_min_pixel.highest_pixel.y;
    switch (search_shape)
    {
    case BALL:
        return ((double)nbr_pixel_image)/(pow(((double)height)/2.0,2)*3.14);
    case CUBE:
        return ((double)nbr_pixel_image)/(double)pow(height,2);
    default:
        fprintf(stderr,"\n \t ERROR TYPE NON PRIX EN CHARGE");
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