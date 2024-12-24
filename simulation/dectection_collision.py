############ DETECTION DE COLLISION AVEC LES OBSTACLES ############################


##########################fonction pour verifier si le robot qui se deplace d un angle "heading" rique de percuter  un obstacle ou pas
#pour cela il y a deux cas a considerer:

"""
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
"""

####" cas pratique "
import math 


def collision_avec_cercle(x0, y0, alpha, xc, yc, r):
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
        return True, (x, y), (x, y)
    else:
        t1 = A - math.sqrt(delta)
        t2 = A + math.sqrt(delta)
        # Calcul des points de collision
        point_entree = (x0 + t1 * cos_alpha, y0 + t1 * sin_alpha)
        point_sortie = (x0 + t2 * cos_alpha, y0 + t2 * sin_alpha)
        return True, point_entree, point_sortie

def collision_avec_rectangle(x0, y0, alpha, x_min, x_max, y_min, y_max):
    """
    Vérifie si un point en mouvement entrera en collision avec un rectangle et retourne les points d'entrée et de sortie.
    
    :param x0: Position initiale en X.
    :param y0: Position initiale en Y.
    :param alpha: Direction du mouvement (en radians).
    :param x_min: Bord gauche du rectangle.
    :param x_max: Bord droit du rectangle.
    :param y_min: Bord inférieur du rectangle.
    :param y_max: Bord supérieur du rectangle.
    :return: Tuple (collision, point_entree, point_sortie)
             collision est un booléen indiquant s'il y a une collision,
             point_entree et point_sortie sont les coordonnées des points d'entrée et de sortie (ou None si pas de collision).
    """
    # Calcul des temps d'intersection avec les côtés verticaux et horizontaux
    cos_alpha = math.cos(alpha)
    sin_alpha = math.sin(alpha)
    
    t_x_min = (x_min - x0) / cos_alpha if cos_alpha != 0 else float('inf')
    t_x_max = (x_max - x0) / cos_alpha if cos_alpha != 0 else float('inf')
    t_y_min = (y_min - y0) / sin_alpha if sin_alpha != 0 else float('inf')
    t_y_max = (y_max - y0) / sin_alpha if sin_alpha != 0 else float('inf')
    
    # Temps d'entrée et de sortie
    t_entree = max(min(t_x_min, t_x_max), min(t_y_min, t_y_max))
    t_sortie = min(max(t_x_min, t_x_max), max(t_y_min, t_y_max))
    
    # Vérification des intersections valides
    if t_entree > t_sortie or t_sortie < 0:
        return False, None, None  # Pas de collision

    # Calcul des points d'entrée et de sortie
    point_entree = (x0 + t_entree * cos_alpha, y0 + t_entree * sin_alpha)
    point_sortie = (x0 + t_sortie * cos_alpha, y0 + t_sortie * sin_alpha)
    return True, point_entree, point_sortie



def Test_collision_obstacle(Obstacle):
    collision, point_entree, point_sortie = (False , None , None)
    if Obstacle.get("forme") == "cercle":

        collision, point_entree, point_sortie = collision_avec_cercle(0, 0, 0, Obstacle.get("centre")[0], Obstacle.get("centre")[1], Obstacle.get("rayon"))
    if Obstacle.get("forme") == "carree":
        collision, point_entree, point_sortie = collision_avec_rectangle(0, 0, 0, Obstacle.get("coin1")[0], Obstacle.get("coin2")[0], Obstacle.get("coin1")[1], Obstacle.get("coin2")[1])
    
    return collision, point_entree, point_sortie

#recuperer la liste des obstacles critiques et les coordonnees des points d entree et de sortie pour les contourner facilement
def get_Obstacles_critiques(obstacles:list):
    Obstacles_critiques = []
    for obstacle in obstacles:
        collision , point_entree , point_sortie = Test_collision_obstacle(obstacle)
        if collision :
            Obstacles_critiques.append((obstacle,point_entree,point_sortie))
    return Obstacles_critiques

############ DETECTION DE COLLISION AVEC LES OBSTACLES ############################