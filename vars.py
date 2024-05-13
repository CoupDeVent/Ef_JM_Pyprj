from enum import Enum
import pygame #import la librairy pygame
pygame.font.init()

# hauteur et largeur de base
fond = pygame.image.load("sprite/Fond.png")
largeur = fond.get_width() # Affecte à la variable largeur, la largeur de l'image Fond.jpeg 
hauteur = fond.get_height()# Affecte à la variable hauteur, la hauteur de l'image Fond.jpeg 

# Cree des police en prevision de l'affichage dans le menu et le jeu
police_titre = pygame.font.SysFont('Comic Sans MS', 150) 
police = pygame.font.SysFont('Comic Sans MS', 30)
police_achat = pygame.font.SysFont('Comic Sans MS', 50)

# Utilisation du systeme RGB pour les couleurs 
couleur_noir = (0,0,0)

# Nombre d'or au debut du jeu
Or = 0

