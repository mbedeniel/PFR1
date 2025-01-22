#include <stdlib.h>
#include <stdio.h>
/*Declaration d'un element*/

/*Un element est constitue d'un entier*/
typedef int ** ELEMENT;

/*affect_ELEMENT*/
/*INPUT: ELEMENT* , ELEMENT*/
/*OUTPUT: NONE*/
/*affecte data a element*/
void affect_ELEMENT(ELEMENT* ptr_element,ELEMENT data);

int ** creer_ELEMENT();