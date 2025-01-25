#include "../include/file_dynamique.h"

void  INIT_FILE(MA_FILE* file)
{
  (*file).head = NULL;
  (*file).tail = NULL;
}

int FILE_EST_VIDE(MA_FILE file)
{
  return file.head==NULL;
}

void ENFILER(MA_FILE* file, ELEMENT element)
{
  CELL* previous_tail;

  CELL* new_cell = (CELL*)malloc(sizeof(CELL)); /*create a new cell*/
  if(new_cell!=NULL) /*verify if the allocation is okey*/
  {
      if(FILE_EST_VIDE(*file))/*si la file est vide alors */
      {
        file->tail=new_cell; /*affect the new tail*/
        file->head=new_cell; /*affecte the new head*/
      }
      else
      {
        previous_tail = file->tail; /*take the previous tail*/
        file->tail=new_cell; /*affect the new tail*/
        previous_tail->next_cell=new_cell; /*update previous tail*/
      }
      new_cell->data=element; /*update new cell*/
      new_cell->next_cell=NULL; /*update new cell*/
  }
  else
  {
    fprintf(stderr,"ERREUR ALLOCATION");
  }
}

ELEMENT DEFILER(MA_FILE* file)
{

  ELEMENT element;
  CELL* previous_head;
  if(FILE_EST_VIDE(*file))
  {
    return NULL;
  }
  previous_head = file->head;
  element = (file->head)->data;
  file->head=(file->head)->next_cell;
  free(previous_head);
  return element;
}
