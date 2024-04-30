import pygame
from pygame.locals import *

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprite/player_r.png")
        self.last_key_pressed = "right"
        self.rect = self.image.get_rect()
        self.pos = vec((320, 650))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.ACC = 0.5
        self.FRIC = -0.15
        self.jumping = False

    def jump(self, all_platforms):
        self.hits = pygame.sprite.spritecollide(self, all_platforms, False)
        if self.hits and not self.jumping:
            self.jumping = True
            self.vel.y = -15

    def move(self, all_platforms):
        self.acc = vec(0, 0.5)

        if self.last_key_pressed == "right":
            self.image = pygame.image.load("sprite/player_r.png")
        else:
            self.image = pygame.image.load("sprite/player_l.png")
        self.pressed_keys = pygame.key.get_pressed()
        if self.pressed_keys[K_RIGHT]:
            self.acc.x = self.ACC
            self.image = pygame.image.load("sprite/player_run_r.png")
            self.last_key_pressed = "right"
        if self.pressed_keys[K_LEFT]:
            self.acc.x = -self.ACC
            self.image = pygame.image.load("sprite/player_run_l.png")
            self.last_key_pressed = "left"
        if self.pressed_keys[K_UP]:
            self.jump(all_platforms)

        self.acc.x += self.vel.x * self.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

    def update(self, all_platforms):
        hits = pygame.sprite.spritecollide(self, all_platforms, False)
        if self.vel.y > 0:
            if hits:
                if self.pos.y < hits[0].rect.bottom:
                    self.pos.y = hits[0].rect.top + 1
                    self.vel.y = 0
                    self.jumping = False
                if self.pos.y >= hits[0].rect.bottom:
                    self.pos.y = hits[0].rect.bottom + 75
                    self.vel.y = -self.vel.y

        # refaire rect
        """
        self.hits_platform = pygame.sprite.spritecollide(self, all_platforms, False)
        if self.hits_platform:
            self.vel.y = 0
            self.pos.y = self.hits_platform[0].rect.top + 1
        """






