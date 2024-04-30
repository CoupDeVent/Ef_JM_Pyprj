import random

import pygame
from pygame.locals import *
from random import *

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

    def spawn_default(self):
        self.image = pygame.image.load("sprite/platform.png")
        self.rect = self.image.get_rect()
        self.rect.center = (320,750)

    def spawn_platform(self, area):
        self.image = ["sprite/platform.png"]

        self.image = pygame.image.load(self.image[0])
        self.rect = self.image.get_rect()

        self.rect.center = (randint(60,580), randint(area[0], area[1]))


