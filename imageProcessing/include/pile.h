typedef int ELEMENT;

void affiche_ELEMENT(ELEMENT element);

typedef struct cell{
    struct cell *suivant;
    int x;
    int y;
} CELLULE;

typedef CELLULE * PILE;


PILE init_PILE(void);

void affiche_PILE(PILE p);

int PILE_estVide(PILE p);

PILE emPILE(PILE p, int x, int y);

int connexN(PILE p, int x, int y, int n);

typedef struct cellu{
    struct cellu *suivant;
    PILE p;
    int num_object;
} CELLULEP;

typedef CELLULEP * PILE_stack;

PILE_stack init_PILE_stack(void);


PILE_stack emPILE_stack(PILE_stack ps, PILE p);

int PILE_estVide_stack(PILE_stack ps);

PILE_stack parcour_PILE_connex(PILE_stack ps, int x, int y, int n);

int objecBinariser(PILE_stack ps, int HEIGHT, int WIDTH, int CHANNELS, int seuil);

void affiche_PILE_stack(PILE_stack ps);
