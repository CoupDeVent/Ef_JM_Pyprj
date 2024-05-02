import pygame
from pygame.locals import *

from player import *
from platform import *
from banane import *
from jungle import *
from score import *



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
        pos_platform = [(350, 700), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        number_banane = 0
        score = 0

        all_platforms = pygame.sprite.Group()
        all_bananes = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()

        jungle = Jungle()
        all_sprites.add(jungle)
        player = Player()
        all_sprites.add(player)

        run = True
        while run:
            ### INIT ###
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False


            ### PLATFORM ###
            if number_platform == 1:
                platform = Platform(0, 0)
                platform.start()
                all_platforms.add(platform)
                all_sprites.add(platform)

            while number_platform < len(pos_platform):
                platform = Platform(pos_platform[number_platform-1][0],
                                    pos_platform[number_platform-1][1])
                if pygame.sprite.spritecollide(platform, all_platforms, True):
                    pass
                else:
                    all_platforms.add(platform)
                    all_sprites.add(platform)

                    pos_platform[number_platform] = platform.rect.center
                    number_platform += 1

            k = 0
            for platform in all_platforms:
                platform.move()
                pos_platform[k] = platform.rect.center
                if platform.rect.y > 750:
                    pygame.sprite.Sprite.kill(platform)
                    number_platform -= 1
                    del pos_platform[k]
                    pos_platform.append((0, 0))
                k += 1
                print(pos_platform)


            ### SCORE/BANANE ###
            score = Score(0)
            all_sprites.add(score)

            while number_banane < 5:
                banane = Banane()
                all_sprites.add(banane)
                all_bananes.add(banane)
                number_banane += 1

            hits_banane = pygame.sprite.spritecollide(player, all_bananes, True)
            if hits_banane:
                score.add_banane(1)
                number_banane -= 1


            ### UPDATE ###
            player.move(all_platforms)
            player.update(all_platforms)
            for entity in all_sprites:
                self.window.blit(entity.image, entity.rect)


            pygame.display.update()
            self.FPS.tick(60)
        pygame.quit()