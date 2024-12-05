#include "pre_processing.h"

int* quantification(int pixel)
{
    int i, pixels[number_quantified_bit];
    for(i=0;i<number_quantified_bit;i++)
    {
        pixels[i]=pixel/2^(7-i);
    }
}