import pygame

class Banane(pygame.sprite.Sprite):
    def __init__(self, pos_platform):
        super().__init__()
        self.pos_x, self.pos_y = pos_platform
        self.image = pygame.transform.scale(pygame.image.load("sprite/banane.png"), (45,45))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y - 35)

    def move(self, vel_y):
        self.rect.y += vel_y