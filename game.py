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
        number_platform = 1
        pos_platform = [(320, 50), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        number_banane = 0
        score = 0

        all_platforms = pygame.sprite.Group()
        all_bananes = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()

        player = Player()
        all_sprites.add(player)

        run = True
        while run:
            ### INIT ###
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False
            self.window.fill((255, 255, 255))


            ### OBJECT ###
            if number_platform == 1:
                platform = Platform(pos_platform[0][0],
                                    pos_platform[0][1])
                all_platforms.add(platform)
                all_sprites.add(platform)

            while number_platform < len(pos_platform):
                platform = Platform(pos_platform[number_platform-1][0],
                                    pos_platform[number_platform-1][1])
                all_platforms.add(platform)
                all_sprites.add(platform)

                pos_platform[number_platform] = platform.rect.center
                number_platform += 1
                print(pos_platform)

            ### SCORE ###
            while number_banane < 5:
                banane = Banane()
                all_sprites.add(banane)
                all_bananes.add(banane)
                number_banane += 1

            font = pygame.font.SysFont("Lato", 15, False)
            score_text = font.render("Score: " + str(score), True, (0, 0, 0))
            self.window.blit(score_text, (10, 10))

            self.hits_banane = pygame.sprite.spritecollide(player, all_bananes, True)
            if self.hits_banane:
                score += 1
                number_banane -= 1


            ### UPDATE ###
            player.move(all_platforms)
            player.update(all_platforms)
            for entity in all_sprites:
                self.window.blit(entity.image, entity.rect)


            pygame.display.update()
            self.FPS.tick(60)
        pygame.quit()