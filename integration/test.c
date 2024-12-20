#include <stdio.h>

// Définir une structure pour stocker les données
typedef struct {
    int id;
    char name[50];
    float value;
} Data;

// Fonction principale
int main() {
    Data data = {42, "example", 3.14};

    // Afficher les données en JSON (pour une interprétation facile dans Python)
    printf("{\"id\":%d,\"name\":\"%s\",\"value\":%.2f}\n", data.id, data.name, data.value);

    return 0; // Retourne 0 pour indiquer que tout s'est bien passé
}
