import math
from simulation.data.settings import get_text
from simulation.logger.logger import display 

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

def test_collision_avec_rectangle(curseur, obstacle):
    """
    Vérifie si le curseur entre en collision avec un rectangle en avançant tout droit.
    
    Args:
        curseur: Objet avec `xcor()`, `ycor()`, `heading()` (en degrés).
        obstacle: Dictionnaire avec :
            - "coin_HD": tuple (x, y) pour le coin supérieur droit du rectangle.
            - "dimension": côté du carré.
    
    Returns:
        tuple: (collision: bool, point_entree: tuple, point_sortie: tuple)
    """
    # Récupération des données du rectangle
    coin_HD = obstacle["coin_HD"]
    cote = obstacle["dimension"]

    # Calcul des limites du rectangle
    x_min = coin_HD[0] - cote
    x_max = coin_HD[0]
    y_min = coin_HD[1] - cote
    y_max = coin_HD[1]

    # Position et direction du curseur
    curseur_x, curseur_y = curseur.xcor(), curseur.ycor()
    angle_deg = curseur.heading()
    angle_rad = math.radians(angle_deg)

    # Composantes directionnelles
    direction_x = math.cos(angle_rad)
    direction_y = math.sin(angle_rad)

    # Vérification de l'intersection avec les côtés du rectangle
    points_intersection = []

    # Vérifier l'intersection avec les côtés verticaux (x_min et x_max)
    if direction_x != 0:
        t_x_min = (x_min - curseur_x) / direction_x
        t_x_max = (x_max - curseur_x) / direction_x

        for t in [t_x_min, t_x_max]:
            if t > 0:  # On ne considère que les intersections futures
                y_inter = curseur_y + t * direction_y
                if y_min <= y_inter <= y_max:
                    points_intersection.append((curseur_x + t * direction_x, y_inter))

    # Vérifier l'intersection avec les côtés horizontaux (y_min et y_max)
    if direction_y != 0:
        t_y_min = (y_min - curseur_y) / direction_y
        t_y_max = (y_max - curseur_y) / direction_y

        for t in [t_y_min, t_y_max]:
            if t > 0:  # On ne considère que les intersections futures qui sont devant le robot 
                x_inter = curseur_x + t * direction_x
                if x_min <= x_inter <= x_max:
                    points_intersection.append((x_inter, curseur_y + t * direction_y))

    # Si aucune intersection trouvée, pas de collision
    if not points_intersection:
        return False, None, None

    # Trier les points d'intersection par ordre de distance (temps t croissant)
    points_intersection.sort(key=lambda p: math.hypot(p[0] - curseur_x, p[1] - curseur_y))

    # Le premier point est le point d'entrée, le dernier le point de sortie
    point_entree = points_intersection[0]
    point_sortie = points_intersection[-1] if len(points_intersection) > 1 else None

    return True, point_entree, point_sortie


def test_collision_avec_cercle(curseur, obstacle, marge=40):
    """
    Vérifie si le curseur risque de pénétrer dans un obstacle circulaire lorsqu'il avance tout droit.

    :param curseur: Objet curseur avec les méthodes position() et heading().
    :param obstacle: Dictionnaire contenant 'centre' (coordonnées) et 'rayon' (rayon du cercle).
    :param marge: Distance minimale de sécurité autour de l'obstacle.
    :return: (collision, point_entree, point_sortie)
    """
    # Récupération des informations de l'obstacle
    coin_HD_obstacle = obstacle.get("coin_HD")
    rayon = obstacle.get("dimension")
    centre_x, centre_y = coin_HD_obstacle[0], coin_HD_obstacle[1] - rayon
    # Position actuelle du curseur
    # Position et direction du curseur
    curseur_x, curseur_y = curseur.xcor(), curseur.ycor()
    angle_deg = curseur.heading()
    angle_rad = math.radians(angle_deg)

    # Composantes directionnelles
    direction_x = math.cos(angle_rad)
    direction_y = math.sin(angle_rad)

    # Paramètres pour l'équation quadratique (interception trajectoire - cercle)
    dx = curseur_x - centre_x
    dy = curseur_y - centre_y
    a = direction_x**2 + direction_y**2
    b = 2 * (dx * direction_x + dy * direction_y)
    c = dx**2 + dy**2 - rayon**2

    # Calcul du discriminant
    discriminant = b**2 - 4 * a * c

    if discriminant <= 0:
        # Pas de collision : pas d'intersection entre la trajectoire et le cercle
        return False, None, None

    # Calcul des points d'intersection (temps t)
    t1 = (-b - math.sqrt(discriminant)) / (2 * a)
    t2 = (-b + math.sqrt(discriminant)) / (2 * a)

    # Points d'entrée et de sortie
    points_intersection = []
    if t1 >= 0:
        x_entree = curseur_x + t1 * direction_x
        y_entree = curseur_y + t1 * direction_y
        points_intersection.append((x_entree, y_entree))
    if t2 >= 0:
        x_sortie = curseur_x + t2 * direction_x
        y_sortie = curseur_y + t2 * direction_y
        points_intersection.append((x_sortie, y_sortie))

    # Si aucune intersection future, pas de collision
    if not points_intersection:
        return False, None, None

    # Trier les points par distance (temps t croissant)
    points_intersection.sort(key=lambda p: math.hypot(p[0] - curseur_x, p[1] - curseur_y))

    # Retourner les points d'entrée et de sortie
    point_entree = points_intersection[0]
    #le 
    point_sortie = points_intersection[1] if len(points_intersection) > 1 else None
    
    
    #ligne a verifier 
    if point_sortie==None:
        point_sortie = points_intersection[0]

    return True, point_entree, point_sortie



def Test_collision_obstacle(Obstacle , curseur):
    #collision est un booleen qui indique s il y a une collision ou pas 
    if Obstacle.get("forme") == "cercle":
        # Vérification de la collision avec le cercle
        return test_collision_avec_cercle(curseur,Obstacle)
    elif Obstacle.get("forme") == "carree":
        # Vérification de la collision avec le rectangle
        return  test_collision_avec_rectangle(curseur, Obstacle)

#recuperer la liste des obstacles critiques et les coordonnees des points d entree et de sortie pour les contourner facilement


def get_Obstacles_critiques(obstacles:list , curseur):
    Obstacles_critiques = []
    for obstacle in obstacles:
        collision , point_entree , point_sortie = Test_collision_obstacle(obstacle, curseur)
        if collision :
            Obstacles_critiques.append((obstacle,point_entree,point_sortie))
    return sorted(Obstacles_critiques, key=lambda obstacle: curseur.distance(obstacle[1]))
    

############ DETECTION DE COLLISION AVEC LES OBSTACLES ############################


#verifier si un point est  dans un obstacle ou pas 
#c est pour eviter que le robot aie une destination qui est dans un obstacle
def point_is_in_obstacle(point , obstacle):
    #verifier si le point est dans l obstacle
    coin_hd = obstacle.get("coin_HD")
    dimension = obstacle.get("dimension")
    x, y = point
    forme = obstacle.get("forme")
    if forme == "cercle":
        #verifier si le point est dans le cercle
        xc, yc = coin_hd[0], coin_hd[1] - dimension
        return (x - xc) ** 2 + (y - yc) ** 2 <= dimension ** 2
    elif forme == "carree":
        #verifier si le point est dans le carre
        X_min, X_max = coin_hd[0] - dimension, coin_hd[0]
        Y_min, Y_max = coin_hd[1] - dimension, coin_hd[1]
        return X_min <= x <= X_max and Y_min <= y <= Y_max
    else:
        display(get_text('invalid_form').format(obstacle.get("nom")))
        return False