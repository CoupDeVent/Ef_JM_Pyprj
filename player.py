import pygame
from pygame.locals import *

vec = pygame.math.Vector2

WIDTH = 640
HEIGHT = 750

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_right = pygame.image.load("sprite/player_r.png")
        self.image_left = pygame.image.load("sprite/player_l.png")
        self.image_run_right = pygame.image.load("sprite/player_run_r.png")
        self.image_run_left = pygame.image.load("sprite/player_run_l.png")
        self.image = self.image_right
        self.rect = self.image.get_rect()

        self.last_key_pressed = "right"
        self.jumping = False

        self.pos = vec((320, 650))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.ACC = 0.5
        self.FRIC = -0.15

    def jump(self, all_platforms):
        self.hits = pygame.sprite.spritecollide(self, all_platforms, False)
        if self.hits and not self.jumping:
            self.vel.y = -15
            self.jumping = True

    def move(self, all_platforms):
        self.acc = vec(0, 0.5)
        self.hits = pygame.sprite.spritecollide(self, all_platforms, False)

        if self.last_key_pressed == "right":
            self.image = self.image_right
        else:
            self.image = self.image_left

        self.pressed_keys = pygame.key.get_pressed()
        if self.pressed_keys[K_RIGHT]:
            self.acc.x = self.ACC
            self.image = self.image_run_right
            self.last_key_pressed = "right"
        if self.pressed_keys[K_LEFT]:
            self.acc.x = -self.ACC
            self.image = self.image_run_left
            self.last_key_pressed = "left"
        if self.pressed_keys[K_UP]:
            self.jump(all_platforms)


        self.acc.x += self.vel.x * self.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

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
                self.pos.y = self.hits[0].rect.top
                self.jumping = False
            elif self.vel.y < 0:
                self.vel.y = 0
                self.pos.y = self.hits[0].rect.bottom + 75
                self.jumping = True

            """if self.rect.right == self.hits[0].rect.left and (self.rect.top < self.hits[0].rect.top or self.rect.bottom > self.hits[0].rect.bottom) and self.vel.x > 0:
                self.vel.x = 0
                self.rect.x = self.hits[0].rect.left
                self.pos.x = self.rect.x - 26"""