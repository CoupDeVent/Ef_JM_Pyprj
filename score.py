import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self, banane):
        super().__init__()
        self.banane = banane
        self.font = pygame.font.SysFont("BN Machine", 30, False)
        self.image = self.font.render("Bananes : " + str(self.banane), True, (0, 0, 0))
        self.rect = self.image.get_rect()

    def add_banane(self, x):
        self.banane += x