#include "element.h"
/*Definition des cellules de MA_FILE*/
typedef struct CELL
{
  ELEMENT data; /*donnée contenue par la CELL*/
  struct CELL * next_cell;/*adresse de la CELL suivante*/
}CELL;

/*Definition de la structure MA_FILE*/
/*Elle est constité d'une tete (adresse de la premiere CELL ajoute)*/
/*et d'une queue (Adresse de la derniere CELL ajoute)*/
typedef struct
{
  CELL* head;
  CELL* tail;
}MA_FILE;


/*INIT FILE qui initialise la file (donn´ee en param`etre)*/
void  INIT_FILE(MA_FILE* file);

/*FILE EST VIDE qui permet de tester si la file (donn´ee en param`etre) est vide*/
/*retourne 1 si la file est vide et 0 sinon*/
int FILE_EST_VIDE(MA_FILE file);

/*ENFILER qui permet d’enfiler un element (donn´e en parametre) `a une file (donnee en parametre)*/
/*cette fonction doit placer lelement en queue de fil*/
void ENFILER(MA_FILE* file,ELEMENT element);

/*DEFILER qui permet de d´efiler une file (donn´ee en param`etre),*/
/*cette fonction doit renvoyer aussi l’´el´ement qui ´etait en tˆete de file*/
ELEMENT DEFILER(MA_FILE* file);
