#include "./../include/pile.h"
#include <stdio.h>
#include <string.h>

typedef int ELEMENT;

void affiche_ELEMENT(ELEMENT element){
	printf("%d", element);
}

typedef struct cell{
    struct cell *suivant;
    int x;
    int y;
} CELLULE;

typedef CELLULE * PILE;


PILE init_PILE(void) {
    return NULL;
}

void affiche_PILE(PILE p){
    PILE act = p;
    while (act != NULL){
        printf("L'element est : ");
        affiche_ELEMENT(act->x);
        printf(",");
        affiche_ELEMENT(act->y);
        printf("\n");
        act = act->suivant;
    }
}

int PILE_estVide(PILE p) {
    return (p == NULL);
}

PILE emPILE(PILE p, int x, int y) {
    CELLULE * cel;
    cel = malloc(sizeof(CELLULE));
    if (!PILE_estVide(cel)){
        cel->x = x;
        cel->y = y;
        cel->suivant = p;
    }
    return cel;
}

int connexN(PILE p, int x, int y, int n){
    PILE act = p;
    while (act != NULL){
        int xcon8 = 0;
        int ycon8 = 0;
        for(int x_connex = -n; x_connex<=n+1; x_connex++){
            for(int y_connex = -n; y_connex<=n+1; y_connex++){
                xcon8 = act->x + x_connex;
                ycon8 = act->y + y_connex;
                if (xcon8 == x && ycon8 == y ){
                    return 1;
                }
            }
        }
        act = act->suivant;
    }
    return 0;
}

typedef struct cellu{
    struct cellu *suivant;
    PILE p;
    int num_object;
} CELLULEP;

typedef CELLULEP * PILE_stack;

PILE_stack init_PILE_stack(void) {
    return NULL;
}


PILE_stack emPILE_stack(PILE_stack ps, PILE p) {
    CELLULEP * cel;
    cel = malloc(sizeof(CELLULEP));
    cel->p = p;
    cel->num_object += 1 ;
    cel->suivant = ps;
        
    return cel;
}

int PILE_estVide_stack(PILE_stack ps) {
    return (ps == NULL);
}

PILE_stack parcour_PILE_connex(PILE_stack ps, int x, int y, int n){
    PILE_stack act = ps;
    while (act != NULL){
        if(connexN(act -> p,  x,  y,  n)){
            act -> p = emPILE(act -> p , x, y);
            return ps;
        }
        act = act->suivant;
    }

    ps = emPILE_stack(ps ,emPILE(init_PILE() , x, y));
    return ps;
}

int*** objecBinariser(PILE_stack ps, int HEIGHT, int WIDTH, int CHANNELS, int seuil) {
    int object_num = 1;  
    int max_nb_pixel = 0;
    int ***image_save = (int ***)malloc(HEIGHT * sizeof(int **));
	for (int i = 0; i < HEIGHT; i++) {
	    image_save[i] = (int **)malloc(WIDTH * sizeof(int *));
	    for (int j = 0; j < WIDTH; j++) {
		image_save[i][j] = (int *)calloc(CHANNELS, sizeof(int));  // Initialise tout à 0
	    }
	}
    
    PILE_stack act_stack = ps;
    while (act_stack != NULL) {
        PILE act_pile = act_stack->p;
        int nb_pixels = 0;
    
        int ***image = (int ***)malloc(HEIGHT * sizeof(int **));
        for (int i = 0; i < HEIGHT; i++) {
            image[i] = (int **)malloc(WIDTH * sizeof(int *));
            for (int j = 0; j < WIDTH; j++) {
                image[i][j] = (int *)calloc(CHANNELS, sizeof(int));  // Initialise tout à 0
            }
        }


        while (act_pile != NULL) {
            int x = act_pile->x;
            int y = act_pile->y;

            if (x >= 0 && x < HEIGHT && y >= 0 && y < WIDTH) {
                image[x][y][0] = 1;  
                nb_pixels++;
            }

            act_pile = act_pile->suivant;  
        }
        if (seuil<nb_pixels){
	    if (max_nb_pixel<nb_pixels){
		image_save = image;}
	    object_num++;

        }
        for (int i = 0; i < HEIGHT; i++) {
            for (int j = 0; j < WIDTH; j++) {
                free(image[i][j]);
            }
            free(image[i]);
        }
        free(image);

        act_stack = act_stack->suivant;
    }
return image_save;
}

void affiche_PILE_stack(PILE_stack ps){
    PILE_stack act = ps;
    int cpt_object = 0;
    while (act != NULL){
        printf("_____________________\n");
        cpt_object ++;
        printf("L'object %d est composé de :\n", cpt_object);
        affiche_PILE(act->p);
        act = act->suivant;
    }
}
