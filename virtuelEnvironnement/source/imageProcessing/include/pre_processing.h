/*--------------------------------------------------------------------------------------------------------------------------------*/
/*------------------------------------------------ @author DEVELLOPER : MBEDE Niel -----------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/
/*----------------------------------------------------------VERSION : 3.0---------------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/
/*---------------------------------------------------- @date DATE : 12/01/2025----------------------------------------------------*/
/*--------------------------------------------------------------------------------------------------------------------------------*/


/** @brief
*-----------------------------------------------------------------------------------------------------------------------------------
*    ALL TREATMENT BEFORE THE REAL ANALYSE OF THE IMAGE : FILTERING, CONVERTING
*-----------------------------------------------------------------------------------------------------------------------------------
*/

#ifndef DEF_PRE_PROCESSING
#define DEF_PRE_PROCESSING

#include<stdlib.h>
#include<stdio.h>
#include<math.h>

/*
******************************************
********PARAMETRES DE CONFIGURATION*******
******************************************
*/

#define PAMAETRE_FILTRE 1 /*la taille du filtre est (2*PAMAETRE_FILTRE)*(2*PAMAETRE_FILTRE) */


/*
**************************************
********PROTOTYPE DES FONCTIONS*******
**************************************
*/


/*les fichiers images que nous traitons sont sous la forme*/
/*Trois matrice de meme taille*/ 
/*la premiere pour le rouge*/
/*la seconde pour le vert*/
/*la derniere pour le bleu*/



/*FUNCTION: void rgb_to_hsv(int ligne,int column,double *** image_rgb,double *** image_hsv)
    elle a pour role de
    faire passer une image de la base 
    RGB(Red Green Blue) a la base HSB(Hue Saturation Value)
    Une image dans la base RGB est une composition de 03 matrices.
    C'est un tenseur.

*/
/*INPUT: 
    @param int ligne 
        Nombre de ligne de l'image d'une matrice des matrices du tenseur
    @param int column
         Nombre de colone de l'image d'une matrice des matrices du tenseur
    @param int *** image_rgb
        image dans la base RGB que l'on veut passer dans la base HSB.
        Il s'agit d'un tenseur (tableau a trois dimenssion)
        Premire dimenssion pour rouge
        Deuxieme dimenssion pour le vert
        troisiemme dimenssion pour le bleu
    @param double *** image_hsv
        image obtenue du passage de l'image RGB dans la base HSB
        il s'agit d'un tenseur.
        Premiere dimenssion represente H
        la seconde dimenssion S
        la troisieme dimenssion V 
*/
/*@return 
OUTPUT: NONE*/
void rgb_to_hsv(int ligne,int column,double *** image_rgb,double *** image_hsv);



/*FUNTUION: double max(double r,double g,double b)
    retourne le max entre trois double
*/
/*INPUT:
    @param double r
    @param double g
    @param double b
*/
/*@return 
OUTPUT: double max
    le max entre r, g et b
*/
double max(double r,double g,double b);



/*FUNTUION: double min(double r,double g,double b)
    retourne le min entre trois double
*/
/*INPUT:
    @param double r
    @param double g
    @param double b
*/
/*@return 
OUTPUT: double min
    le min entre r, g et b
*/
double min(double r,double g,double b);



/*FUNCTION : int int_comparer(const int * a,const int * b)
    retourne le resultat de la soustraction de a par b
    ce qui permet de s'avoir qui est le plus grand.
    Cette fonction est specialement utuliser par la fonction
    qsort() predefinie en c
*/
/*INPUT :
    @param const void *a : un pointeur sur un int
    @param const void *b : un pointeur sur un int
    On precise const pour etre sur de ne pas modifier la valeur de a
*/
/*@return 
OUTPUT: 
    un entier : resultat de la soustraction  
*/
int int_comparer(const void * a, const void * b);



/*FUNCTION: void image_filter(int ** image,int ligne,int column)
    permet d'utiliser le filtre median pour filter une image
    Dans le cadre de notre projet, nous nouns interesson au filtrage de bruit
    de type sel et poivre
*/
/*INPUT:
    @param int ** image
        le tableau a traité
    @param int ligne 
        Nombre de ligne de l'image d'une matrice des matrices du tenseur
    @param int column
         Nombre de colone de l'image d'une matrice des matrices du tenseur
*/
/*@return 
OUTPUT : void*/
void image_filter(int ** image,int ligne,int column);



/*FUNCTION : void median(int ** image,int i,int j)
    permet de calculer la median et mets le pixel i,j a jour
*/
/*INPUT:
    @param const int ** image
        le tableau a traité
    @param int i
        la ligne sur laquelle le centre du masque est
    @param int j
        la colonne sur laquelle le centre du masque est
*/
/*@return 
OUTPUT : void*/
void median(int ** image,int i,int j);



/*FUNCTION : 
    permet d'ajouter des bordures e notre images
    les bordures ajoutées sont fonction de PAMAETRE_FILTRE
    du point de vue d'un tableau cela ce trqduit par l'ajout
    de ligne et de colonne au debut et a la fin
*/
/*INPUT : void add_padding(int ** image,int ligne,int column)
    @param int ** image
        un tableau ou l'on veux initaliser le premiere ligne
        et derniere colonne a 0
    @param int ligne
        nombre de ligne du tableau pri en paramete
    @param int column
        nombre de colonne du tableau pris en paraùetre
*/
/*@return 
OUTPUT: NONE*/
void add_padding(int ** image,int ligne,int column);

#endif
