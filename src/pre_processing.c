#include "../include/pre_processing.h"
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


double max(double r,double g,double b)
{
	double max = r;
	if(g>max)
	{
		max = g;
	}
	if (b>max)
	{
		max = b;
	}
	
	return max;
}

double min(double r,double g,double b)
{
	double min = r;
	if(g<min)
	{
		min = g;
	}
	if (b<min)
	{
		min = b;
	}
	
	return min;
}

void rgb_to_hsv(int ligne,int column,double *** image_rgb,double *** image_hsv)
{
	int i,j;
	double v,s,h,max_minus_min,r,g,b;
	for(i=0;i<ligne;i++)
	{
		for(j=0;j<column;j++)
		{
			r=**(*(image_rgb+i)+j);
			g=*(*(*(image_rgb+i)+j)+1);
			b=*(*(*(image_rgb+i)+j)+2);

			r/=255.0;
			g/=255.0;
			b/=255.0;

			v=max(r,g,b);

			/* S et V ne sont pas en pourcentage*/
			/*pour les exprimmer ainsi il suffit de les multipier par 100*/

			max_minus_min = v-min(r,g,b);

			if(max_minus_min!=0)
			{

				if(v==0)
				{
					s=0;
				}
				else
				{
					s=(v-min(r,g,b))/v;
				}

				if(v==r)
				{
					h=(60.0)*(g-b)/max_minus_min;
				}
				else if(v==g)
				{
					h=(60.0)*(2.0+(b-r)/max_minus_min);
				}
				else if(v==b)
				{
					h=(60.0)*(4.0+(r-g)/max_minus_min);
				}
				if(h<0)
				{
					h+=360.0;
				}

				**(*(image_hsv+i)+j)=h;
				*(*(*(image_hsv+i)+j)+1)=s;
				*(*(*(image_hsv+i)+j)+2)=v;
			}
			else if(r==0.0) /*case where R=0 G=0 and B=0*/
			{
				**(*(image_hsv+i)+j)=0;
				*(*(*(image_hsv+i)+j)+1)=0;
				*(*(*(image_hsv+i)+j)+2)=0;
			}
			else /*case where R=255 G=255 and B=255*/
			{
				**(*(image_hsv+i)+j)=0;
				*(*(*(image_hsv+i)+j)+1)=0;
				*(*(*(image_hsv+i)+j)+2)=1;
			}

		}
	}
}