import pygame #import la librairy pygame
pygame.init()

import menu, apropos, boutique



# Variables Globales
clock = pygame.time.Clock() #créer un objet horloge qui peut être utilisé pour garder une trace du temps 

# Affichage du Menu
menu.affiche()

#boucle principale    
running = True 
mode_menu = True
while running == True: 
    
    # Gestion evenement clavier et menu
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    
    if event.type == pygame.KEYDOWN:

        # Les touches pressés
        keys = pygame.key.get_pressed()             
        if keys[pygame.K_ESCAPE]:            
            running = False
            continue
        
        # Verification du sous-menu lance
        menu.traitement_touches(event, keys)
        if menu.menu_command == MenuCommand.GAME.value: # COMMENCER LE JEU             
            pass
        elif menu.menu_command == MenuCommand.SKIN.value: # SKINS
            boutique.mainsac()
        elif menu.menu_command == MenuCommand.HELP.value: # COMMANDES
            apropos.main()
        elif menu.menu_command == MenuCommand.SHOP.value: # SHOP
            boutique.mainboutique()          
        elif menu.menu_command == MenuCommand.EXIT.value: # EXIT
            running = False
        
    menu.affiche()
        
    pygame.display.update()    

