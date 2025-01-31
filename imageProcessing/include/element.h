
/*--------------------------------------------------------------------------------------------------------------------------------*/
/*------------------------------------------------ @author DEVELLOPER : MBEDE Niel -----------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------VERSION : 1.0---------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/
/*---------------------------------------------------- @date DATE : 24/01/2025 ---------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/

#ifndef DEF_ELEMENT
#define DEF_ELEMENT
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

ELEMENT creer_ELEMENT();
#endif
