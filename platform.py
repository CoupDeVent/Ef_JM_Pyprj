import random

import pygame
from pygame.locals import *
from random import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, last_platform_x, last_platform_y):
        super().__init__()
        self.image = ["sprite/platform.png"]
        self.image = pygame.image.load(self.image[0])
        self.rect = self.image.get_rect()
        self.vel_y = 1

        self.min_distance_y_platform = 125
        self.max_distance_y_platform = 175
        self.possible_x_platform = [60, 580]

        self.pos_x = randint(self.possible_x_platform[0], self.possible_x_platform[1])
        self.pos_y = randint(last_platform_y - self.max_distance_y_platform, last_platform_y - self.min_distance_y_platform)

        self.rect.center = (self.pos_x, self.pos_y)

    def move(self):
        self.rect.y += self.vel_y