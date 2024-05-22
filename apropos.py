import pygame #import la librairy pygame
import vars

# Initialisation de la librairie pygame
pygame.init()
# Création écran
screen = pygame.display.set_mode((vars.largeur, vars.hauteur))  #On definie la largeur et la longeur de la fenêtre

# Affichage texte multi-lignes
def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 1, (255,255,255))
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def guide():
    screen.fill(pygame.Color('black'))
    blit_text(screen, "But du jeu  : \nVous devez vous démener à sauter toujours plus haut afin d'obtenir le plus de Bananes.\n\nGuide du jeu\nTouches :\n      - « flèche droite » te permet de te déplacer à droite \n      - « flèche gauche » te permet de te déplacer à gauche\n      - « flèche haut » te permet de sauter\n      - « escape » te permet de quitter le jeu ou de quitter la partie si tu es en game.", (10, 100), vars.police)
    return True


def main():
    guide()
    running = True
    while running: 
        
        pygame.event.poll()
        keys = pygame.key.get_pressed()     

        if keys[pygame.K_ESCAPE]:
            running = False            

        pygame.display.update()    
