from enum import Enum
import pygame #import la librairy pygame
import vars, boutique, apropos

# Création écran menu
liste_textes = [
    "Commencer la partie", 
    "Commandes", 
    "Objets", 
    "Boutique", 
    "Quitter"
]    

#Variables importantes permettant de creer le fond du menu et autres
screen_menu = pygame.display.set_mode((vars.largeur, vars.hauteur))  
couleur_texte = (255, 255, 255)
couleur_texte_selection = (0, 255, 127)
text = vars.police.render(liste_textes[0], True, couleur_texte, vars.couleur_noir)
textRect = text.get_rect()
textRect.center = (vars.largeur//2, vars.hauteur//2 - 50)
    
menu_command = -1
current_menu_command = 0
last_menu_command = 4

# Permet l'affichage du menu 
def affiche():   
    global liste_textes, current_menu_command 
    screen_menu.fill(vars.couleur_noir) #on remplie la fenêtre avec la couleur noir.    
    tab = liste_textes

    # Centre le texte affiche grace au coordones X et Y
    xt = vars.largeur//2
    yt = vars.hauteur//2 - 80
    

    # Cree une boucle pour afficher chaque chaine de caractere de la liste "liste_textes" soit "tab" ici
    for i in range(0, len(tab)):
        element = tab[i]

        couleur = couleur_texte
        if current_menu_command == i: 
            couleur = couleur_texte_selection

        text = vars.police.render(element, True, couleur, vars.couleur_noir)
        textRect = text.get_rect()
        textRect.center = (xt, yt)
        screen_menu.blit(text, textRect) 

        #Rajoute 50 à la coordonnées y pour espacer les chaines de caracteres
        yt = yt + 50


# Traitement de touches dans le menu
# les seuls touches qui fonctionne sont la fleche du haut, du bas, escape et entré
def traitement_touches(event, keys):    
    global menu_command, current_menu_command, last_menu_command
  
    menu_command = -1

    if keys[pygame.K_RETURN]:
        menu_command = current_menu_command
    
    if keys[pygame.K_DOWN]:
        if current_menu_command == last_menu_command: current_menu_command = 0
        else: current_menu_command = current_menu_command + 1
    elif keys[pygame.K_UP]:
        if current_menu_command == 0 and keys[pygame.K_UP]: current_menu_command = last_menu_command
        else: current_menu_command = current_menu_command - 1
    
    return menu_command

    

