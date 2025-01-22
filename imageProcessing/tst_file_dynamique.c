#include "./include/file_dynamique.h"
int main()
{
  int matrice[3][3];
  MA_FILE file;

  /*TEST DE INIT_FILE*/
  printf("------- \n");
  printf("TEST DE INIT_FILE \n");
  printf("------- \n");
  
  printf("\t AVANT APPELE DE INIT_FILE \n : ");
  printf("\t \t file.head : %i \n", file.head);
  printf("\t \t file.tail : %i \n", file.tail);
  INIT_FILE(&file);
  printf("\t APRES APPELE DE INIT_FILE \n : ");
  printf("\t \t file.head : %i \n", file.head);
  printf("\t \t file.tail : %i \n", file.tail);

  /*TEST DE FILE_EST_VIDE*/
  printf("------- \n");
  printf("TEST DE FILE_EST_VIDE \n");
  printf("------- \n");
  if(FILE_EST_VIDE(file))
  {
    printf("\t la file est vide \n");
  }
  else
  {
    printf("\t la file n'est vide \n");
  }

  /*TEST DE ENFILER*/
  ELEMENT element = matrice;
  printf("------- \n");
  printf("TEST DE ENFILER \n");
  printf("------- \n");
  ENFILER(&file,element);

  /*TEST DE FILE_EST_VIDE*/
  printf("------- \n");
  printf("TEST DE FILE_EST_VIDE \n");
  printf("------- \n");
  if(FILE_EST_VIDE(file))
  {
    printf("\t la file est vide \n");
  }
  else
  {
    printf("\t la file n'est vide \n");
  }

  /*TEST DE DEFILER*/
  printf("------- \n");
  printf("TEST DE DEFILER \n");
  printf("------- \n");
  DEFILER(&file);

  /*TEST DE FILE_EST_VIDE*/
  printf("------- \n");
  printf("TEST DE FILE_EST_VIDE \n");
  printf("------- \n");
  if(FILE_EST_VIDE(file))
  {
    printf("\t la file est vide \n");
  }
  else
  {
    printf("\t la file n'est vide \n");
  }


}
