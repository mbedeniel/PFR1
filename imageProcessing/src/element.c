#include "../include/element.h"

void affect_ELEMENT(ELEMENT* ptr_element,ELEMENT data){
  *ptr_element=data;
}

int ** creer_ELEMENT(int ligne, int colonne)
{
  /*Declaration*/
  int i;
  int ** binary_image;

  /*Allocation des tableaux de pointeurs*/
  binary_image = (int**)malloc(ligne*sizeof(int*));

  /*tableau binary_image*/
  if (binary_image!=NULL)
  {
      for(i=0;i<ligne;i++)
      {
          binary_image[i] = (int*)malloc(colonne*sizeof(int));
          if(binary_image[i]==NULL)
          {
              fprintf(stderr,"ERREUR ALLOCATION");
              return NULL;
          }
      }
    return binary_image;
  }
  else
  {
      fprintf(stderr,"ERREUR ALLOCATION");
      return NULL;
  }
}