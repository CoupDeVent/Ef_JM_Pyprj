import pygame

class Jungle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("sprite/jungle.png"), (2560, 768))
        self.rect = self.image.get_rect()