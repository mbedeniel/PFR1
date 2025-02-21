# Module de Traitement d'Images (`image_processing`)

Ce module, développé en **langage C**, permet d'effectuer un traitement avancé des images en analysant leurs **formes**, **couleurs** et **positions**. Il utilise une approche basée sur la **décomposition par raffinage successif** pour garantir une détection précise des objets dans une image.

## 📌 Fonctionnalités

- Chargement d’images aux formats **JPG** et **PNG**.
- Conversion de l’espace colorimétrique **RGB** vers **HSV** pour une meilleure robustesse face aux variations de luminosité.
- Segmentation des images en fonction des couleurs.
- Filtrage des bruits via un **filtre médian**.
- Détection et identification des formes (**cercles, carrés, etc.**).
- Communication avec d’autres modules via `image_interface`.

## 📂 Architecture du Module

Le module prend en entrée une image et retourne une structure contenant les informations suivantes :
- **Position** 📍: Localisation de l’objet détecté.
- **Couleur** 🎨: Détection de la couleur dominante.
- **Forme** 🔺: Identification de la géométrie de l’objet.

L’échange de données avec d'autres modules (`commande vocale`, `simulation`, etc.) se fait exclusivement via `image_interface`, garantissant ainsi une meilleure maintenabilité et une réduction des erreurs potentielles.

## 🔍 Fonctionnement de l'algorithme

### **Détection d’un objet coloré (exemple : une balle bleue)**

1. **Prétraitement de l’image**
   - L’image est récupérée dans l’espace colorimétrique **RGB** (Red-Green-Blue) puis convertie en **HSV** (Hue-Saturation-Value).
   - L’espace HSV est préféré, car il est moins sensible aux variations d’éclairage, ce qui facilite l’analyse des couleurs.

2. **Segmentation de la couleur**
   - Le module `color_treatment` segmente l’image en fonction de la couleur recherchée.
   - L’algorithme s’appuie principalement sur la composante **H (teinte)** de chaque pixel, en utilisant des seuils prédéfinis.
   - À l’issue de cette segmentation, une image binaire (`binary_image`) est générée, indiquant la présence ou non de la couleur recherchée.

3. **Filtrage des bruits**
   - Un **filtre médian** est appliqué pour éliminer les bruits parasites et améliorer la précision du traitement.

4. **Détection de la forme**
   - Le module `shape_treatment` analyse `binary_image` pour identifier si la forme détectée correspond à celle recherchée.
   - L’approche varie selon la nature de la figure :

   #### **Cas d’un cercle**
   - Un cercle est caractérisé par son **centre** et son **rayon**.
   - L’algorithme détermine les points extrêmes sur l’axe **Y** et calcule le rayon.
   - L’aire du cercle ainsi défini est comparée à l’aire réelle de la figure détectée dans `binary_image`.

   #### **Cas d’un carré**
   - L’algorithme identifie les points extrêmes sur l’axe **Y** pour en déduire la longueur d’un côté.
   - L’aire du carré est comparée à l’aire mesurée dans `binary_image` pour validation.

> **Remarque** : L’algorithme ne distingue pas les formes similaires (ex. carré vs rectangle vs losange, ou cercle vs ovale).

### **Amélioration de la détection**
Pour affiner l’identification des formes, une méthode d’intersection est utilisée :
- On superpose la figure détectée dans `binary_image` avec la forme idéale reconstruite à partir des paramètres extraits.
- Une **précision de 97 %** pour un cercle et **65 %** pour un cube a été obtenue sur l’exemple testé.

## 🚀 Installation et Exécution

### **1️⃣ Compilation**
Ce projet utilise un **Makefile** pour automatiser la compilation. Pour compiler le module, exécute la commande :

```sh
make
```

### **2️⃣ Lancement sous Linux**
Une fois la compilation terminée, le module peut être exécuté avec :

```sh
./main_test_image.out
```

### **3️⃣ Modification des paramètres**
Les **paramètres de lancement** peuvent être modifiés directement dans le fichier `Makefile`.

## 🛠️ Dépendances

- Un compilateur **C** (`gcc` recommandé).
- Les bibliothèques nécessaires pour la manipulation des images (ex. `libjpeg`, `libpng`).

## 📜 Licence

Ce projet est distribué sous la licence **MIT**. Consulte le fichier `LICENSE` pour plus d’informations.

## 🤝 Contributions

Les contributions sont les bienvenues !  
Si tu souhaites proposer des améliorations, n'hésite pas à créer une **issue** ou à soumettre une **pull request**.

---

🎯 Ce module est conçu pour être évolutif et adaptable à différents cas d’usage en traitement d’images. Amuse-toi bien avec `image_processing` ! 🚀

