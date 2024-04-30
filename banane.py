import pygame
from random import *

class Banane(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos_x = 300
        self.pos_y = 400
        self.image = pygame.image.load("sprite/banane.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
        self.score = 0

     

        
        
