import math
from settings import __DEBUG__

############ DETECTION DE COLLISION AVEC LES OBSTACLES ############################


##########################fonction pour verifier si le robot qui se deplace d un angle "heading" rique de percuter  un obstacle ou pas
#pour cela il y a deux cas a considerer:

'''
Cas d'un obstacle sous forme d'un cercle :
-------------------
L’équation d’un cercle est donnée par : (x - xc)² + (y - yc)² = r²
- xc et yc : Coordonnées du centre du cercle.
- r : Rayon du cercle.

Pour vérifier une collision avec un cercle :
1. La position du point (robot) à un instant t est donnée par :
   P(t) = (x0 + t * cos(α), y0 + t * sin(α))
   - x0, y0 : Position initiale du point.
   - α : Direction (heading) du point.

2. On remplace les coordonnées de P(t) dans l’équation du cercle.
   Cela permet de trouver la distance entre le point et le centre du cercle :
   X = x0 + t * cos(α)
   Y = y0 + t * sin(α)

3. Après injection de X et Y dans l’équation du cercle, on obtient une équation quadratique :
   t² - 2 * A * t + B = 0
   - A = (x0 - xc) * cos(α) + (y0 - yc) * sin(α)
   - B = (x0 - xc)² + (y0 - yc)² - r²

4. Analyse du discriminant (Δ) :
   - Si Δ < 0 : Pas de collision. Le point ne rencontrera jamais le cercle.
   - Si Δ = 0 : Collision tangente. Le point effleure le cercle.
   - Si Δ > 0 : Deux temps t1 et t2.
     * Le plus petit t correspond à l’entrée dans le cercle.
     * Le plus grand t correspond à la sortie.

5. Points de collision :
   - Calculés avec P(T) = (x0 + T * cos(α), y0 + T * sin(α)).
   - On remplace le temps T par t1 et t2 pour obtenir les points d’entrée et de sortie. dans le cercle.

Cas d'un obstacle sous forme d'un rectangle :
-------------------
Un rectangle est défini par ses coordonnées : (X1, Y1) et (X2, Y2)

Pour vérifier une collision avec un rectangle :
1. Conditions d’intersection :
   - Le point doit respecter :
     X1 ≤ xp ≤ X2 et Y1 ≤ yp ≤ Y2
   - xp et yp : Coordonnées de la trajectoire à un instant t.

2. Calcul des temps d’intersection :
   - Pour les côtés verticaux (à X = X1 ou X = X2) :
     t_x = (X1 - x0) / cos(α) ou t_x = (X2 - x0) / cos(α)
   - Pour les côtés horizontaux (à Y = Y1 ou Y = Y2) :
     t_y = (Y1 - y0) / sin(α) ou t_y = (Y2 - y0) / sin(α)

3. Temps valides :
   - Conservez les valeurs de t > 0.
   - Vérifiez si les coordonnées correspondantes sont dans les limites du rectangle.
   - Le plus petit t est le temps d’entrée.
   - Le plus grand t est le temps de sortie.

4. Points d’intersection :
   - Coordonnées calculées avec P(t) = (x0 + t * cos(α), y0 + t * sin(α))
   - On remplace le temps t par les valeurs de T trouvées pour avoir les coordonnées des points d'entré et de sortie 

5. Absence de collision :
   - Si aucune valeur de t ne satisfait les conditions, alors il n’y a pas de collision avec le rectangle.
'''

####" cas pratique "
import math 


def collision_avec_cercle(curseur, obstacle):
    """
    Vérifie si un point en mouvement entrera en collision avec un cercle et retourne les points de collision.
    
    :param x0: Position initiale en X.
    :param y0: Position initiale en Y.
    :param alpha: Direction du mouvement (en radians).
    :param xc: Coordonnée X du centre du cercle.
    :param yc: Coordonnée Y du centre du cercle.
    :param r: Rayon du cercle.
    :return: Tuple (collision, point_entree, point_sortie)
             collision est un booléen indiquant s'il y a une collision,
             point_entree et point_sortie sont les coordonnées des points d'entrée et de sortie (ou None si pas de collision).
    """
    # Récupération des coordonnées du curseur
    x0, y0 = curseur.position()
    heading = curseur.heading()
    # Récupération des coordonnées du cercle
    centre = obstacle.get("coin_HD")
    xc, yc = centre[0], centre[1] - obstacle.get("dimension")
    r = obstacle.get("dimension")

    alpha = math.radians(heading)
    # Calcul des coefficients A et B
    cos_alpha = math.cos(alpha)
    sin_alpha = math.sin(alpha)
    A = (x0 - xc) * cos_alpha + (y0 - yc) * sin_alpha
    B = (x0 - xc)**2 + (y0 - yc)**2 - r**2
    
    # Calcul du discriminant
    delta = A**2 - B
    
    if delta < 0:
        return (False, None, None)  # Pas de collision
    elif delta == 0:
        t = A  # Collision tangente
        x = x0 + t * cos_alpha
        y = y0 + t * sin_alpha
        return True, (x, y), None
    else:
        t1 = A - math.sqrt(delta)
        t2 = A + math.sqrt(delta)
        # Calcul des points de collision
        point_entree = (x0 + t1 * cos_alpha, y0 + t1 * sin_alpha)
        point_sortie = (x0 + t2 * cos_alpha, y0 + t2 * sin_alpha)
        return True, point_entree, point_sortie


def collision_avec_rectangle(curseur, obstacle):
    """
    Détecte une collision entre la trajectoire du curseur et un rectangle (carré).
    
    Paramètres :
        curseur : un objet avec les méthodes `xcor()`, `ycor()` et `heading()` (angle de trajectoire).
        obstacle : un dictionnaire contenant :
            - "coin_HD" : coordonnées du coin supérieur droit (tuple).
            - "dimension" : taille du carré (côté).

    Retour :
        (bool, tuple, tuple) : 
        - True si collision, False sinon.
        - Coordonnées d'entrée (x, y).
        - Coordonnées de sortie (x, y).
    """
    # Coin supérieur droit et côté du carré
    coin_HD = obstacle.get("coin_HD")
    cote = obstacle.get("dimension")
    
    x_min, y_min = coin_HD[0] - cote, coin_HD[1] - cote
    x_max, y_max = coin_HD[0], coin_HD[1]

    # Position initiale du curseur
    x0, y0 = curseur.xcor(), curseur.ycor()
    angle = math.radians(curseur.heading())
    dx = math.cos(angle) # dx = cos(α) et = 0
    dy = math.sin(angle)

    # Temps pour les côtés verticaux
    if dx != 0:
        t_x1 = (x_min - x0) / dx
        t_x2 = (x_max - x0) / dx
    else:
        t_x1 = t_x2 = float('inf')  # Pas de mouvement horizontal

    # Temps pour les côtés horizontaux
    if dy != 0:
        t_y1 = (y_min - y0) / dy
        t_y2 = (y_max - y0) / dy
    else:
        t_y1 = t_y2 = float('inf')  # Pas de mouvement vertical

    # Temps valides (t > 0)
    t_x = [t for t in [t_x1, t_x2] if t > 0]
    t_y = [t for t in [t_y1, t_y2] if t > 0]

    if not t_x or not t_y:
        return False, None, None  # Pas de collision

    # Temps d'entrée et de sortie
    t_entree = min(min(t_x), min(t_y)) # MAXIMUM DES MINIMUMS DES TEMPS D'ENTREE 
    t_sortie = max(max(t_x), max(t_y)) # MINIMUM DES MAXIMUMS DES TEMPS DE SORTIE
   
    if t_entree > t_sortie:
        print(f"Erreur: t_entree > t_sortie ({t_entree} > {t_sortie})")
        return False, None, None  # Pas de collision

    # Coordonnées des points d'entrée et de sortie
    x_entree = x0 + t_entree * dx
    y_entree = y0 + t_entree * dy
    x_sortie = x0 + t_sortie * dx
    y_sortie = y0 + t_sortie * dy
    
    return True, (x_entree, y_entree), (x_sortie, y_sortie)

    
def Test_collision_obstacle(Obstacle , curseur):
    #collision est un booleen qui indique s il y a une collision ou pas 
    if Obstacle.get("forme") == "cercle":
        # Vérification de la collision avec le cercle
        collision, point_entree, point_sortie = collision_avec_cercle(curseur,Obstacle)
    if Obstacle.get("forme") == "carree":
        # Vérification de la collision avec le rectangle
        collision, point_entree, point_sortie = collision_avec_rectangle(curseur, Obstacle)
        #print (f"collision avec un carree {collision} point d'entree {point_entree} point de sortie {point_sortie}")
    #retourner si il y a collision ou pas et les coordonnees des points d entree et de sortie
    return collision, point_entree, point_sortie

#recuperer la liste des obstacles critiques et les coordonnees des points d entree et de sortie pour les contourner facilement
def get_Obstacles_critiques(obstacles:list , curseur):
    Obstacles_critiques = []

    for obstacle in obstacles:
        collision , point_entree , point_sortie = Test_collision_obstacle(obstacle, curseur)
        if collision :
            Obstacles_critiques.append((obstacle,point_entree,point_sortie))
            if __DEBUG__:
                print(f"Collision avec le {obstacle.get('forme')} {obstacle.get('nom')} au point d'entré : {point_entree} et de sortie {point_sortie}")
   
    return Obstacles_critiques

############ DETECTION DE COLLISION AVEC LES OBSTACLES ############################