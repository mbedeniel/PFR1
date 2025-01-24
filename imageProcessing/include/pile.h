#ifndef DEF_PILE
#define DEF_PILE
#include "file_dynamique.h"

/* 
STRUCTURE : CELLULE
    Représente un élément dans une pile, contenant des coordonnées (x, y)
    et un pointeur vers l'élément suivant de la pile.
*/
typedef struct cellule {
    int x;                     /*Coordonnée x*/
    int y;                     /*Coordonnée y*/
    struct cellule* suivant;   /*Pointeur vers la cellule suivante*/
} CELLULE;

/*
TYPEDEF : PILE
    Définit une pile comme un pointeur vers une cellule.
*/
typedef CELLULE* PILE;

/*
FUNCTION : PILE init_PILE(void)
    Initialise une pile vide.
*/
/*
INPUT: NONE
*/
/*
OUTPUT: Une pile vide.
*/
PILE init_PILE(void);

/*
FUNCTION : void affiche_PILE(PILE p)
    Affiche les éléments de la pile.
*/
/*
INPUT:
    PILE p : La pile à afficher.
*/
/*
OUTPUT: NONE
*/
void affiche_PILE(PILE p);

/*
FUNCTION : int PILE_estVide(PILE p)
    Vérifie si une pile est vide.
*/
/*
INPUT:
    PILE p : La pile à vérifier.
*/
/*
OUTPUT:
    Retourne 1 si la pile est vide, 0 sinon.
*/
int PILE_estVide(PILE p);

/*
FUNCTION : PILE emPILE(PILE p, int x, int y)
    Empile un nouvel élément avec les coordonnées (x, y) dans la pile.
*/
/*
INPUT:
    PILE p : La pile existante.
    int x : Coordonnée x de l'élément à empiler.
    int y : Coordonnée y de l'élément à empiler.
*/
/*
OUTPUT:
    Retourne la pile mise à jour.
*/
PILE emPILE(PILE p, int x, int y);

/*
FUNCTION : int connexN(PILE p, int x, int y, int n)
    Vérifie si un point (x, y) est dans la zone de connectivité d'un élément de la pile.
*/
/*
INPUT:
    PILE p : La pile à vérifier.
    int x : Coordonnée x du point.
    int y : Coordonnée y du point.
    int n : Rayon de la connectivité.
*/
/*
OUTPUT:
    Retourne 1 si le point (x, y) est dans la connectivité, 0 sinon.
*/
int connexN(PILE p, int x, int y, int n);

/*
STRUCTURE : CELLULEP
    Représente un élément dans une pile de piles (PILE_stack), contenant une pile et un pointeur vers la pile suivante.
*/
typedef struct cellu {
    struct cellu* suivant; /*Pointeur vers l'élément suivant*/
    PILE p;               /*Pile associée*/
    int num_object;       /*Identifiant de l'objet*/
} CELLULEP;

/*
TYPEDEF : PILE_stack
    Définit une pile de piles comme un pointeur vers une cellule de pile.
*/
typedef CELLULEP* PILE_stack;

/*
FUNCTION : PILE_stack init_PILE_stack(void)
    Initialise une pile de piles vide.
*/
/*
INPUT: NONE
*/
/*
OUTPUT: Une pile de piles vide.
*/
PILE_stack init_PILE_stack(void);

/*
FUNCTION : PILE_stack emPILE_stack(PILE_stack ps, PILE p)
    Ajoute une pile à une pile de piles.
*/
/*
INPUT:
    PILE_stack ps : La pile de piles existante.
    PILE p : La pile à ajouter.
*/
/*
OUTPUT:
    Retourne la pile de piles mise à jour.
*/
PILE_stack emPILE_stack(PILE_stack ps, PILE p);

/*
FUNCTION : int PILE_estVide_stack(PILE_stack ps)
    Vérifie si une pile de piles est vide.
*/
/*
INPUT:
    PILE_stack ps : La pile de piles à vérifier.
*/
/*
OUTPUT:
    Retourne 1 si la pile de piles est vide, 0 sinon.
*/
int PILE_estVide_stack(PILE_stack ps);

/*
FUNCTION : PILE_stack parcour_PILE_connex(PILE_stack ps, int x, int y, int n)
    Ajoute un point (x, y) à une pile existante ou en crée une nouvelle si aucune pile ne le contient dans sa zone de connectivité.
*/
/*
INPUT:
    PILE_stack ps : La pile de piles à parcourir.
    int x : Coordonnée x du point.
    int y : Coordonnée y du point.
    int n : Rayon de la connectivité.
*/
/*
OUTPUT:
    Retourne la pile de piles mise à jour.
*/
PILE_stack parcour_PILE_connex(PILE_stack ps, int x, int y, int n);

/*
FUNCTION : int*** objecBinariser(PILE_stack ps, int HEIGHT, int WIDTH, int CHANNELS, int seuil)
    Crée une image binaire pour chaque objet dans la pile de piles.
*/
/*
INPUT:
    PILE_stack ps : La pile de piles contenant les objets.
    int HEIGHT : Hauteur de l'image.
    int WIDTH : Largeur de l'image.
    int seuil : Seuil pour filtrer les petits objets.
*/
/*
OUTPUT:
    Retourne une image binaire contenant les objets dépassant le seuil.
*/
int objecBinariser(PILE_stack ps, int HEIGHT, int WIDTH, int seuil, MA_FILE* file);

/*
FUNCTION : void affiche_PILE_stack(PILE_stack ps)
    Affiche les objets contenus dans une pile de piles.
*/
/*
INPUT:
    PILE_stack ps : La pile de piles à afficher.
*/
/*
OUTPUT: NONE
*/
void affiche_PILE_stack(PILE_stack ps);
#endif
