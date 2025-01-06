import math
from simulation.data.settings import __DEBUG__

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


def collision_avec_rectangle(curseur, obstacle):

    return False, None, None
    """
    Détecte une collision entre un curseur (avec une position et un angle) et un rectangle.
    
    Args:
        curseur: Objet avec les méthodes `xcor()` (position x), `ycor()` (position y), 
                 et `heading()` (direction en degrés).
        obstacle: Dictionnaire contenant :
            - "coin_HD": tuple (x, y) pour le coin supérieur droit du rectangle.
            - "dimension": côté du carré (on suppose un carré pour cette implémentation).
    
    Returns:
        tuple:
            - bool: Indique si une collision a lieu.
            - tuple: Coordonnées (x, y) du point d'entrée (si collision).
            - tuple: Coordonnées (x, y) du point de sortie (si collision).
    """
    coin_HD = obstacle.get("coin_HD")
    cote = obstacle.get("dimension")

    # Calcul des limites du rectangle
    X_min, X_max = coin_HD[0] - cote, coin_HD[0]
    Y_min, Y_max = coin_HD[1] - cote, coin_HD[1]

    # Calcul de l'angle du curseur en radians
    angle_radians = math.radians(curseur.heading())
    cos_angle = math.cos(angle_radians)
    sin_angle = math.sin(angle_radians)

    # Éviter la division par zéro en cas de direction parallèle aux axes
    if cos_angle == 0 and (curseur.xcor() < X_min or curseur.xcor() > X_max):
        return False, None, None  # Pas de collision (parallèle aux côtés verticaux)
    if sin_angle == 0 and (curseur.ycor() < Y_min or curseur.ycor() > Y_max):
        return False, None, None  # Pas de collision (parallèle aux côtés horizontaux)

    # Calcul des temps de collision avec les côtés verticaux
    t_x1 = (X_min - curseur.xcor()) / cos_angle if cos_angle != 0 else float('inf')
    t_x2 = (X_max - curseur.xcor()) / cos_angle if cos_angle != 0 else float('inf')

    # Calcul des temps de collision avec les côtés horizontaux
    t_y1 = (Y_min - curseur.ycor()) / sin_angle if sin_angle != 0 else float('inf')
    t_y2 = (Y_max - curseur.ycor()) / sin_angle if sin_angle != 0 else float('inf')

    # Récupération des temps valides (positifs)
    t_valides = [t for t in [t_x1, t_x2, t_y1, t_y2] if t > 0]
    if not t_valides:
        return False, None, None  # Pas de collision

    # Temps d'entrée et de sortie
    t_entree = min(t_valides)
    t_sortie = max(t_valides)

    # Calcul des points d'entrée et de sortie
    x_entree = curseur.xcor() + t_entree * cos_angle
    y_entree = curseur.ycor() + t_entree * sin_angle
    x_sortie = curseur.xcor() + t_sortie * cos_angle
    y_sortie = curseur.ycor() + t_sortie * sin_angle

    return True, (x_entree, y_entree), (x_sortie, y_sortie)

def collision_cercle__(curseur, obstacle, marge=20 ):
    """
    Vérifie si le curseur risque de pénétrer dans un obstacle circulaire lorsqu'il avance tout droit.

    :param curseur: Objet curseur avec les méthodes position() et heading().
    :param obstacle: Dictionnaire contenant 'coin_HD' (coordonnées) et 'dimension' (rayon du cercle).
    :param marge: Distance minimale de sécurité autour de l'obstacle.
    :return: (collision, point_entree, point_sortie)
    """
    # Centre corrigé et rayon de l'obstacle
    coin_hd = obstacle.get("coin_HD")
    r = obstacle.get("dimension")
    xc, yc = coin_hd[0], coin_hd[1] - r  # Ajustement du centre si nécessaire

    # Position initiale et direction du curseur
    x0, y0 = curseur.position()
    alpha = math.radians(curseur.heading())

    # Distance actuelle du curseur au centre du cercle
    distance_to_center = curseur.distance((xc, yc))

    LIMIT = r + marge  # Limite de sécurité

    if distance_to_center <= LIMIT:
        # Calcul des points d'entrée et de sortie dans la direction de l'angle
        point_entree = (
            x0 + (distance_to_center - LIMIT) * math.cos(alpha),
            y0 + (distance_to_center - LIMIT) * math.sin(alpha),
        )

        point_sortie = (
            x0 + (distance_to_center + LIMIT) * math.cos(alpha),
            y0 + (distance_to_center + LIMIT) * math.sin(alpha),
        )
        return True, point_entree, point_sortie
    elif distance_to_center == LIMIT:
        # Le curseur est juste à la distance limite
        point = (
            x0 + (distance_to_center - LIMIT) * math.cos(alpha),
            y0 + (distance_to_center - LIMIT) * math.sin(alpha),
        )
        return False, point, None
    else:
        # Pas de collision ou danger
        return False, None, None
import math
import math

def verifier_collision_cercle(curseur, obstacle, marge=40):
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
    curseur_x, curseur_y = curseur.position()

    # Calcul de la direction infinie basée sur l'angle du curseur
    angle = curseur.heading() #math.radians(curseur.heading())
    print(f"angle : {angle}  heading : {curseur.heading()}")
    direction_x = math.cos(angle)  # Composante x de la direction
    direction_y = math.sin(angle)  # Composante y de la direction

    # Paramètres pour l'équation quadratique de la trajectoire
    dx = curseur_x - centre_x
    dy = curseur_y - centre_y
    a = direction_x**2 + direction_y**2
    b = 2 * (dx * direction_x + dy * direction_y)
    c = dx**2 + dy**2 - rayon**2

    # Calcul du discriminant
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        # Pas de collision : pas d'intersection entre la trajectoire et le cercle
        return False, None, None

    # Calcul des points d'intersection
    t1 = (-b - math.sqrt(discriminant)) / (2 * a)
    t2 = (-b + math.sqrt(discriminant)) / (2 * a)

    # Si t1 et t2 sont négatifs, la collision se trouve derrière le curseur
    if t1 < 0 and t2 < 0:
        return False, None, None

    # Points d'entrée et de sortie
    point_entree = (curseur_x + marge + t1 * direction_x, curseur_y + marge + t1 * direction_y) if t1 >= 0 else None
    point_sortie = (curseur_x + marge + t2 * direction_x, curseur_y + marge + t2 * direction_y) if t2 >= 0 else None

    return True, point_entree, point_sortie



def Test_collision_obstacle(Obstacle , curseur):
    #collision est un booleen qui indique s il y a une collision ou pas 
    if Obstacle.get("forme") == "cercle":
        # Vérification de la collision avec le cercle
        return verifier_collision_cercle(curseur,Obstacle)
    elif Obstacle.get("forme") == "carree":
        # Vérification de la collision avec le rectangle
        return  collision_avec_rectangle(curseur, Obstacle)

#recuperer la liste des obstacles critiques et les coordonnees des points d entree et de sortie pour les contourner facilement


def get_Obstacles_critiques(obstacles:list , curseur):
    Obstacles_critiques = []
    for obstacle in obstacles:
        collision , point_entree , point_sortie = Test_collision_obstacle(obstacle, curseur)
        if collision :
            Obstacles_critiques.append((obstacle,point_entree,point_sortie))
            if __DEBUG__:
                print(f"Collision avec l'obstacle {obstacle.get('nom')} au point d'entré : {point_entree} et de sortie {point_sortie}")
   
    return sorted(Obstacles_critiques, key=lambda obstacle: curseur.distance(obstacle[1]))
    

############ DETECTION DE COLLISION AVEC LES OBSTACLES ############################



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
        if __DEBUG__:
            print(f"Erreur: l obstacle {obstacle['nom']} a une forme invalide.Sa forme({obstacle['forme']}) doit être 'cercle' ou 'carre'.")
        return False