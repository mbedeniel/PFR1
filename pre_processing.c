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

int color_histogram(int** pixel_images,int ligne,int column,double** color_histograms)
{
	int i,j,k,count=0,test;
	
	/*i et j des Compteurs*/
	/*test pour verifier si le pixel est deja dans pixel_histogrammes*/
	/*count permet de connaitre le nombre d element contenue dans pixel_histogrammes*/

	/*
	la premiere ligne pour stocker les pixels
	la seconde pour stocker leurs frequence d'apparition
	*/
	
	/*La gestion de l espace memoire pourrait etre largement optimisé avec les pointeurs dynamique*/
	/*Mais il ne sont pas vue ici*/

	/*CALCUL*/
	

	/*
	Je selectionne un pixel dans IMAGE
	Je verifie si ce pixel est present dans pixel_histogrammes
		si oui, j'augmente sa frequence selon la formule 1.0/ligne*column
		si non, 
			je l'ajoute a pixel_histogrammes puis
			je l'affecte une frequence selon la formule 1.0/ligne*column
			j'incremente count car le nombre d element pixel_histogrammes de a augmente

	Et j'iterre le procéde pour chaque pixel
	*/

	/*Il faut au moins une valuer dans pixel_histogrammes pour executer notre alogrithme*/
	**color_histograms=**pixel_images;
	**(color_histograms+1)=0.0;
	count++;
	for(i=0;i<ligne;i++)
	{
		for(j=0;j<column;j++)
		{
			test=1;
			for(k=0;k<count;k++)
			{
				if(*(*color_histograms+k)==(double)*(*(pixel_images+i)+j)){
					*(*(color_histograms+1)+k)=*(*(color_histograms+1)+k)+1.0/(ligne*column);
					test=0;
				}
			}
			if(test)
			{
				*(*color_histograms+count)=*(*(pixel_images+i)+j);
				*(*(color_histograms+1)+count)=1.0/(ligne*column);
				count++;
			}
			
		}
	}
    return count; /*retourner le nombre d'element du tableau*/
}