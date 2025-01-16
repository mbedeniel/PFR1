#include "../include/pre_processing.h"

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

			/* S et V  sont  en pourcentage*/
			

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
				*(*(*(image_hsv+i)+j)+1)=s*100.0;
				*(*(*(image_hsv+i)+j)+2)=v*100.0;
			}
			else if(r==0.0) /*case where R=0 G=0 and B=0*/
			{
				**(*(image_hsv+i)+j)=0.0;
				*(*(*(image_hsv+i)+j)+1)=0.0;
				*(*(*(image_hsv+i)+j)+2)=0.0;
			}
			else /*case where R=255 G=255 and B=255*/
			{
				**(*(image_hsv+i)+j)=0.0;
				*(*(*(image_hsv+i)+j)+1)=0.0;
				*(*(*(image_hsv+i)+j)+2)=100.0;
			}

		}
	}
}

int int_comparer(const void *a, const void *b)
{
	return *(int*)a - *(int*)b;
}

void image_filter(int ** image,int ligne,int column)
{
	int i,j,k;
	int new_image[ligne+PAMAETRE_FILTRE*2][column+PAMAETRE_FILTRE*2];
	/*ETAPE 1: gestion des bord
		il faut gerer les bord des l'image
		pour cela nous crons un nouveau tableau
	*/
	add_padding(new_image,ligne+PAMAETRE_FILTRE*2,column+PAMAETRE_FILTRE*2,PAMAETRE_FILTRE); /*les bord serons initialisé a 0*/
	
	/*ETAPE 2: remplissage
		on rempli le nouveau tableau avec les elements de l'ancien
	*/
	for(i=0;i<ligne;i++)
	{
		for(j=0;j<column;j++)
		{
			new_image[i+PAMAETRE_FILTRE][j+PAMAETRE_FILTRE]=image[i][j];
		}
	}
	
	/*ETAPE 3: calcul median
		on fait appel a une fonction pour cela
	*/
	for(i=PAMAETRE_FILTRE;i<ligne;i++)
	{
		for(j=PAMAETRE_FILTRE;j<column;j++)
		{
			median(new_image,i,j);
		}
	}

	/*ETAPE 4 : retirer les bordures ajoutée
		on met a jour image
	*/
	for(i=0;i<ligne;i++)
	{
		for(j=0;j<column;j++)
		{
			image[i][j]=new_image[i+PAMAETRE_FILTRE][j+PAMAETRE_FILTRE];
		}
	}

}

void add_padding(int ** image,int ligne,int column, int padding_size)
{
	int i,j,k;
	/*
	Nous travaillons dans un cadre generique car
	au PFR2 il peut arriver que nous decidons d'augmenter la taille dumasque
	*/
	for(k=0;k<padding_size;k++)
	{
		/*Initialisation de la premiere ligne et de la derniere ligne  du tableau*/
		for(i=k;i<ligne;i+=ligne-(1+2*k))
		{
			for(j=k;j<column;j++)
			{
				image[i][j]=0;
			}
		}
		/*Initialisation de la premiere colonne et de la derniere colone  du tableau*/
		for(j=k;j<column;j+=column-(1+2*k))
		{
			for(i=k;i<ligne;i++)
			{
				image[i][j]=0;
			}
		}
	}
}

void median(int ** image,int i,int j)
{
	int local_i,local_j,k=0,size=pow(2*PAMAETRE_FILTRE+1,2);
	int filtres[size];
	/*ETAPE 1 : mise des valuers du filtre dans un tableau*/
	for(local_i=i-PAMAETRE_FILTRE;local_i<i+PAMAETRE_FILTRE+1;local_i++)
	{
		for(local_j=j-PAMAETRE_FILTRE;local_j<j+PAMAETRE_FILTRE+1;local_j++,k++)
		{
			filtres[k]=image[local_i][local_j];
		}
	}

	/*ETAPE 2 : tire du tableau*/
	qsort(filtres,size,sizeof(filtres[0]),int_comparer);


	/*ETAPE 3 : mise a jour de l'element i,j avec la valeur de la mediane*/
	image[i][j]=filtres[size/2];
}