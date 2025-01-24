#include "./../include/pile.h"

PILE init_PILE(void) {
    return NULL;
}

void affiche_PILE(PILE p){
    PILE act = p;
    while (act != NULL){
        printf("L'element est : ");
        printf("%d", act->x);
        printf(",");
	    printf("%d", act->y);
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
    int xcon8,ycon8,x_connex,y_connex;
    while (act != NULL){
        xcon8 = 0;
        ycon8 = 0;
        for(x_connex = -n; x_connex<=n+1; x_connex++){
            for(y_connex = -n; y_connex<=n+1; y_connex++){
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


PILE_stack init_PILE_stack(void) {
    return NULL;
}


PILE_stack emPILE_stack(PILE_stack ps, PILE p) {
    CELLULEP * cel;
    cel = malloc(sizeof(CELLULEP));
    if(cel != NULL)
    {
        cel->p = p;
        cel->num_object = 1 ;
        cel->suivant = ps;
    }
    else
    {
        fprintf(stderr,"ERREUR ALLOCATION");
        return ps;
    } 
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

int objecBinariser(PILE_stack ps, int HEIGHT, int WIDTH, int seuil, MA_FILE* file){
    int nombre_objet = 0;  
    int nb_pixels;
    PILE act_pile;
    ELEMENT img;
    PILE_stack act_stack = ps;
    while (act_stack != NULL) {
        act_pile = act_stack->p;
        nb_pixels = 0;

        img = creer_ELEMENT(HEIGHT, WIDTH);
        if(img==NULL)
        {
            fprintf(stderr,"ERREUR ALLOCATION");
            return 0;
        }
        while (act_pile != NULL) {
            img[act_pile->x][act_pile->y] = 1;
	        nombre_objet++;
            act_pile = act_pile->suivant;  
        }
        if (seuil<nb_pixels){
            ENFILER(file, img);
        }
        act_stack = act_stack->suivant;
    }
    return nombre_objet;
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
