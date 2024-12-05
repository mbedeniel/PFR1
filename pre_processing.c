#include "pre_processing.h"
#include <stdio.h>
#include <math.h>

void quantification(int pixel, int* pixels)
{
    int i,pixel_processed;
    for(i=0;i<NUMBER_QUANTIFIED_BIT;i++)
    {
        pixel_processed=pixel/pow(2,7-i);
        *(pixels+i)=pixel_processed;
        if(pixel_processed)
        {
            pixel-= pow(2,7-i);
        }
    }
}