


// la structure Position qui contient les coordonnées x et y d'un objet
typedef struct {
    int x;
    int y;
} Position;
// la forme d un objet (soit un cercle ou un rectangle)
typedef enum {
    CUBE,
    BOULE
} Forme;
//les couleur possible
typedef enum {
    ROUGE,
    VERT,
    BLEU,
    JAUNE,
    CYAN,
    MAGENTA,
    BLANC,
    NOIR
} Couleur;
//un objet est defini par sa position, sa forme et sa couleur
typedef struct {
    Position position;
    Forme forme;
    Couleur couleur;
} Objet;
