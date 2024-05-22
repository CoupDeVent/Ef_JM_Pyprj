import pygame
from pygame.locals import *

vec = pygame.math.Vector2

WIDTH = 640
HEIGHT = 750

class Player(pygame.sprite.Sprite):
    def __init__(self, nb_skin):
        super().__init__()
        skin_convert = ['default/default_r.png', 'hat/hat_r.png', 'headset/headset_r.png', 'galaxy/galaxy_r.png', 'angel/angel_r.png', 'king/king_r.png']
        skin = [["sprite/player/default/default_r.png","sprite/player/default/default_l.png",
                 "sprite/player/default/default_run_r.png","sprite/player/default/default_run_l.png"],

                ["sprite/player/hat/hat_r.png", "sprite/player/hat/hat_l.png",
                 "sprite/player/hat/hat_run_r.png", "sprite/player/hat/hat_run_l.png"],

                ["sprite/player/headset/headset_r.png", "sprite/player/headset/headset_l.png",
                 "sprite/player/headset/headset_run_r.png", "sprite/player/headset/headset_run_l.png"],

                ["sprite/player/galaxy/galaxy_r.png", "sprite/player/galaxy/galaxy_l.png",
                 "sprite/player/galaxy/galaxy_run_r.png", "sprite/player/galaxy/galaxy_run_l.png"],

                ["sprite/player/angel/angel_r.png", "sprite/player/angel/angel_l.png",
                 "sprite/player/angel/angel_run_r.png", "sprite/player/angel/angel_run_l.png"],

                ["sprite/player/king/king_r.png", "sprite/player/king/king_l.png",
                 "sprite/player/king/king_run_r.png", "sprite/player/king/king_run_l.png"]]
        self.skin_select = skin_convert.index(nb_skin)
        self.image_right = pygame.image.load(skin[self.skin_select][0])
        self.image_left = pygame.image.load(skin[self.skin_select][1])
        self.image_run_right = pygame.image.load(skin[self.skin_select][2])
        self.image_run_left = pygame.image.load(skin[self.skin_select][3])
        self.image = self.image_right
        self.rect = self.image.get_rect()

        self.last_key_pressed = "right"
        self.jumping = False

        ### Variable pour l'équation de la trajectoire ###
        self.pos = vec((320, 650)) # Vecteur position #
        self.vel = vec(0, 0) # Vecteur vitesse #
        self.acc = vec(0, 0) # Vecteur accélération #
        self.ACC = 0.7 # Constante accélération #
        self.FRIC = -0.15 # Constante friction #
        ###

    def jump(self):
        if not self.jumping:
            self.vel.y = -15 # Saut -> vitesse vertical = -15 #
            self.jumping = True

    def move(self):
        self.acc = vec(0, 0.5) # Donne une accélération naturel vertical de 0.5 (gravité dans notre cas) #

        if self.last_key_pressed == "right":
            self.image = self.image_right
        else:
            self.image = self.image_left

        self.pressed_keys = pygame.key.get_pressed()
        if self.pressed_keys[K_RIGHT]:
            self.acc.x = self.ACC # Donne une accélération de 0.7 en horizontal #
            self.image = self.image_run_right
            self.last_key_pressed = "right"
        if self.pressed_keys[K_LEFT]:
            self.acc.x = -self.ACC # Donne une accélération de -0.7 en horizontal #
            self.image = self.image_run_left
            self.last_key_pressed = "left"
        if self.pressed_keys[K_UP]:
            self.jump()


        self.acc.x += self.vel.x * self.FRIC # Recalcule de l'accélération horizontal avec la friction et la vitesse vertical #
        self.vel += self.acc # Addition de la vitesse avec l'accélération (vertical et horizontal) #
        self.pos += self.vel + 0.5 * self.acc # Recalcule de la position avec la vitesse, une costante 0.5 et l'accélération (vertical et horizontal) #

        self.rect.midbottom = self.pos

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH


    def update(self, all_platforms):
        self.hits = pygame.sprite.spritecollide(self, all_platforms, False)

        if self.hits:
            if self.vel.y > 0:
                self.vel.y = 0
                self.pos.y = self.hits[0].rect.top + 1
                self.jumping = False
            elif self.vel.y < 0:
                self.vel.y = 0
                self.pos.y = self.hits[0].rect.bottom + 85