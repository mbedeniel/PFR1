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