import pygame #import la librairy pygame
import vars, os



# Création écran menu
liste_textes_boutique = ["acheter","acheter","acheter","acheter","acheter"]
liste_skin_boutique = ["Hat: 10 Banane","Headset: 50 Banane","Galaxy: 200 Banane","Angel: 500 Banane","King: 1000 Banane"]
liste_price = [10, 50, 200, 500, 1000]

liste_perso_possede = ['default/default_r.png']
perso_selectionne = liste_perso_possede[0]

screen_boutique = pygame.display.set_mode((vars.largeur, vars.hauteur))  
image_boutique = pygame.image.load("sprite/Fond.png").convert()
#image_boutique = pygame.transform.scale(image_boutique, (vars.largeur, vars.hauteur))


couleur_texte = (255, 255, 255)
couleur_texte_selection = (255, 0, 0)
text = vars.police.render(liste_textes_boutique[0], True, couleur_texte, vars.couleur_noir)
textRect = text.get_rect()
textRect.center = (vars.largeur // 2, vars.hauteur // 2 - 50)

personnages = ['hat/hat_r.png', 'headset/headset_r.png', 'galaxy/galaxy_r.png', 'angel/angel_r.png', 'king/king_r.png']
images_personnages = [pygame.image.load(os.path.join('sprite/player', perso)).convert_alpha() for perso in personnages]
images_personnages_boutique = [pygame.transform.scale(image, (image.get_width()*3, image.get_height()*4)) for image in images_personnages]

shop_command = -1
current_shop_command = 0
last_shop_command = len(liste_textes_boutique) - 1

sac_command = -1
current_sac_command = 0
last_sac_command = len(liste_perso_possede) - 1    

# Carte Perso
# Classe permettant de representer une carte avec des bords de couleurs differentes lorsqu'elle est selectionne

class Card(pygame.sprite.Sprite):
    def __init__(self, objet, x, y, cx, cy, color, fond, actif:False):
        pygame.sprite.Sprite.__init__(self)
        
        bl = 5 # taille bordure

        self.rect = (x, y, cx, cy)
        self.objet = objet
        self.color = color
        self.fond = fond

        self.original_image = pygame.Surface((cx, cy))
        pygame.draw.rect(self.original_image, self.color ,[0, 0, cx, cy])        
        if actif: self.original_image.fill(fond, (bl, bl, cx - (bl * 2), cy - (bl * 2)))
        else: self.original_image.fill(fond)
        
        self.draw()


# Fonction permettant de creer un des bords arrondis  et de centrer l'objet image au centre du rectangle
# en fonction de la largeur et de la hauteur de la carte 

    def draw(self):                
        self.image = self.original_image        
        self.set_rounded(10)
        
        rect = self.objet.get_rect(center=(self.rect[2] / 2, self.rect[3] / 2))
         
        self.image.blit(self.objet, rect)
        
    def set_rounded(self, roundness):
        size = self.original_image.get_size()
        self.rect_image = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.rect(self.rect_image, (255, 255, 255), (0, 0, *size), border_radius=roundness)

        self.image = self.original_image.copy().convert_alpha()
        self.image.blit(self.rect_image, (0, 0), None, pygame.BLEND_RGBA_MIN) 

# dsfdsf 
def init():
    global current_shop_command
    current_shop_command = 0
    affiche_boutique()

def init_sac():
    global current_sac_command
    current_sac_command = 0
    affiche_sac()


# Affiche la boutique
def affiche_boutique():  
     
    global liste_textes_boutique 

    screen_boutique.blit(image_boutique, (0, 0))
    tab = liste_textes_boutique
    tab_skin = liste_skin_boutique

    xt = 150
    xt_texte = 130
    xt_personnage = 0
    yt = vars.hauteur - 80
    yt_texte = 90


    text_or = vars.police.render("Banane : {}".format(vars.Or), True, (255, 255, 255), vars.couleur_noir)
    textRect_or = text_or.get_rect()
    textRect_or.center = (vars.largeur - 100, 30)
    screen_boutique.blit(text_or, textRect_or) 
    
    for i, image in enumerate(images_personnages_boutique):
        element = tab[i]
        element_nom_skin = tab_skin[i]

        couleur = couleur_texte
        if current_shop_command == i: 
            couleur = couleur_texte_selection

        text = vars.police.render(element, True, couleur, vars.couleur_noir)
        # text.set_alpha(127)        
        textRect = text.get_rect()
        textRect.center = (xt, yt)
        screen_boutique.blit(text, textRect) 

        text_skin = vars.police.render(element_nom_skin, True, couleur, vars.couleur_noir)
        textRect1 = text_skin.get_rect()
        textRect1.center = (xt_texte, yt_texte)
        screen_boutique.blit(text_skin, textRect1) 

        screen_boutique.blit(image, (xt_personnage, yt_texte + 30 ))

        xt = xt + 310
        xt_texte = xt_texte + 310
        xt_personnage = xt_personnage + 310


#traitement des touches dans la boutique
def traitement_touches_boutique(event, keys):    
    global shop_command, current_shop_command, last_shop_command,liste_perso_possede       
    #pygame.event.clear()
    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_RIGHT]:
            if current_shop_command == last_shop_command: current_shop_command = 0
            else: current_shop_command = current_shop_command + 1

            affiche_boutique()

        elif keys[pygame.K_LEFT]:
            if current_shop_command == 0 : current_shop_command = last_shop_command
            else: current_shop_command = current_shop_command - 1

            affiche_boutique()

        elif keys[pygame.K_RETURN]:
            if ((vars.Or >= liste_price[current_shop_command]) and (liste_textes_boutique[current_shop_command] == "acheter")):
                vars.Or -= liste_price[current_shop_command]
                liste_textes_boutique[current_shop_command] = "deja acheté"
                liste_perso_possede.append(personnages[current_shop_command])

                affiche_boutique()

                text = vars.police_achat.render("Bravo pour votre achat ! ", True, couleur_texte_selection, vars.couleur_noir)
                textRect = text.get_rect()
                textRect.center = (vars.largeur // 2, vars.hauteur // 2)
                screen_boutique.blit(text, textRect) 

            else:
                if (liste_textes_boutique[current_shop_command] != "acheter"):
                    text = vars.police.render("Vous avez deja acheter ce skin il est disponible dans vos objets !", True, couleur_texte_selection, vars.couleur_noir)
                    textRect = text.get_rect()
                    textRect.center = (vars.largeur // 2, vars.hauteur // 2)
                    screen_boutique.blit(text, textRect) 
                else:
                    text = vars.police_achat.render("Pas assez de Banane !", True, couleur_texte_selection, vars.couleur_noir)
                    textRect = text.get_rect()
                    textRect.center = (vars.largeur // 2, vars.hauteur // 2)
                    screen_boutique.blit(text, textRect) 



        return True

# Fonction permettant de gerer la boutique en appelant les deux fonctions precedentes
def mainboutique():
    init()
    running = True

    #Boucle principal
    while running: 
        
        event = pygame.event.poll()
        keys = pygame.key.get_pressed()     

        if keys[pygame.K_ESCAPE]:
            running = False            
        else:
            traitement_touches_boutique(event, keys)

        pygame.display.update()    




####### PARTIE SAC




# Affichage du sous menu sac
def affiche_sac():       
    global liste_perso_possede, current_sac_command
    images_personnages_sac = [pygame.image.load(os.path.join('sprite/player', perso)).convert_alpha() for perso in liste_perso_possede]
    images_personnages_sac = [pygame.transform.scale(image, (image.get_width()*2, image.get_height()*2)) for image in images_personnages_sac]

    # Calcul du Centrage des cartes
    card_l = 200
    card_h = 300
    x = 0
    y = (vars.hauteur - card_h) // 2
    cards = []

    # Affichage Carte Perso
    x = (vars.largeur - (((len(images_personnages_sac) * card_l)) + ((len(images_personnages_sac) - 1) * 20))) // 2
    
    for i, image in enumerate(images_personnages_sac):
        actif = False
        if current_sac_command == i: actif = True
        card = Card(image, x, y, card_l, card_h, (255, 0, 0), (0, 0, 0), actif)            
        cards.append(card)
        x += card_l + 20    

    # Dessine...
    screen_boutique.blit(image_boutique, (0, 0))    

    text_selection = vars.police.render("Selectionner votre personnage !", True, (255, 255, 255), vars.couleur_noir)
    textRect_selection = text_selection.get_rect()
    textRect_selection.center = (vars.largeur // 2 - 22, (vars.hauteur - card_h) // 2 - 40)
    screen_boutique.blit(text_selection, textRect_selection) 


    text_or = vars.police.render("Banane : {}".format(vars.Or), True, (255, 255, 255), vars.couleur_noir)
    textRect_or = text_or.get_rect()
    textRect_or.center = (vars.largeur - 100, 30)
    screen_boutique.blit(text_or, textRect_or) 

    group = pygame.sprite.Group(cards)
    group.draw(screen_boutique)


#Traitement des tocuhes dans le sous-menu sac
def traitement_touches_sac(event, keys):    
    global liste_perso_possede, current_sac_command, last_sac_command, perso_selectionne
    last_sac_command = len(liste_perso_possede) - 1
    #pygame.event.clear()
    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_RIGHT]:
            if current_sac_command == last_sac_command: current_sac_command = 0
            else: current_sac_command = current_sac_command + 1

            affiche_sac()

        elif keys[pygame.K_LEFT]:
            if current_sac_command == 0 : current_sac_command = last_sac_command
            else: current_sac_command = current_sac_command - 1

            affiche_sac()

        elif keys[pygame.K_RETURN]:

            affiche_sac()

            text = vars.police_achat.render("Ce Personnage à été sélectionné ! ", True, couleur_texte_selection, vars.couleur_noir)
            textRect = text.get_rect()
            textRect.center = (vars.largeur // 2, vars.hauteur // 2)
            screen_boutique.blit(text, textRect) 
            perso_selectionne = liste_perso_possede[current_sac_command]
        
    return True

# Fonction permettant de gerer le sac en appelant les deux fonctions precedentes
def mainsac():
    init_sac()
    running = True

    #Boucle principal
    while running: 
        
        event = pygame.event.poll()
        keys = pygame.key.get_pressed()     

        if keys[pygame.K_ESCAPE]:
            running = False            
        else:
            traitement_touches_sac(event, keys)

        pygame.display.update() 

