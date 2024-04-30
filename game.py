import pygame
from pygame.locals import *
from player import *
from platform import *
from banane import *



class Game():
    def __int__(self):
        super().__int__()
    def load(self):
        self.FPS = pygame.time.Clock()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.window.fill((255, 255, 255))
    def run(self):
        self.load()

        all_platforms = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        all_bananes = pygame.sprite.Group()

        player = Player()
        all_sprites.add(player)

        banane = Banane()
        all_bananes.add(banane)
        all_sprites.add(banane)

        p_def = Platform()
        p_def.spawn_default()
        all_platforms.add(p_def)
        all_sprites.add(p_def)

        area = [(150,250),(300,400),(450,550),(600,650)]
        for k in range(4):
            platform = Platform()
            platform.spawn_platform(area[k])
            all_sprites.add(platform)
            all_platforms.add(platform)

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False
            self.window.fill((255, 255, 255))

            player.move(all_platforms)
            player.update(all_platforms)
            for entity in all_sprites:
                self.window.blit(entity.image, entity.rect)

            # Score
            font = pygame.font.SysFont("Lato", 30, False)
            score_text = font.render("Score: " + str(banane.score), True, (0, 0, 0))
            self.window.blit(score_text, (10, 10))

            # hit banane player
            self.hits_banane = pygame.sprite.spritecollide(player, all_bananes, False)
            if self.hits_banane:
                banane.pos_x = 0
                banane.pos_y = 0
                banane.score += 1


            pygame.display.update()
            self.FPS.tick(60)
        pygame.quit()