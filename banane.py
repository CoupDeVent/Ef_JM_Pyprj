import pygame
from random import *

class Banane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos_x = randint(60, 580)
        self.pos_y = randint(60, 690)
        self.image = pygame.transform.scale(pygame.image.load("sprite/banane.png"), (45,45))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)