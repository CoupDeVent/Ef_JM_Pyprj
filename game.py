import pygame, os
from pygame.locals import *
from enum import Enum

from player import *
from platform import *
from banane import *
from jungle import *

import menu, apropos, boutique

class MenuCommand(Enum):
    MAIN = -1
    GAME = 0
    HELP = 1
    SKIN = 2
    SHOP = 3
    EXIT = 4

class Game():
    def __int__(self):
        super().__int__()
    def load(self):
        self.FPS = pygame.time.Clock()
        pygame.display.set_caption("Jumping Monke")
        pygame.display.set_icon(pygame.transform.scale(pygame.image.load("sprite/banane.png"), (45,45)))
        self.window = pygame.display.set_mode((1520, 660), pygame.RESIZABLE)
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.window.fill((255, 255, 255))
    def run(self):
        self.load()
        menu.affiche()
        game_mode = "menu"
        change_window = False
        start = True
        score = 0

        run = True
        while run:
            ### MENU ###
            if game_mode == "menu":
                if change_window:
                    self.window = pygame.display.set_mode((1520, 660), pygame.RESIZABLE)
                    os.environ['SDL_VIDEO_CENTERED'] = '1'
                    change_window = False
                event = pygame.event.poll()
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        run = False

                    menu.traitement_touches(event, keys)
                    if menu.menu_command == MenuCommand.GAME.value:
                        game_mode = "play"
                        change_window = True
                    elif menu.menu_command == MenuCommand.SKIN.value:
                        boutique.mainsac()
                    elif menu.menu_command == MenuCommand.HELP.value:
                        apropos.main()
                    elif menu.menu_command == MenuCommand.SHOP.value:
                        boutique.mainboutique()
                    elif menu.menu_command == MenuCommand.EXIT.value:
                        run = False
                menu.affiche()


            ### GAME OVER ###
            if game_mode == "game over":
                if change_window:
                    self.window = pygame.display.set_mode((1520, 660), pygame.RESIZABLE)
                    os.environ['SDL_VIDEO_CENTERED'] = '1'
                    change_window = False
                self.window.blit(pygame.image.load("sprite/game_over.png"), (0,0))
                for event in pygame.event.get():
                    if event.type == QUIT:
                        run = False
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_RETURN]:
                        game_mode = "menu"
                        change_window = True


            ### GAME ###
            if game_mode == "play":
                if change_window:
                    self.window = pygame.display.set_mode((640, 750), pygame.RESIZABLE)
                    os.environ['SDL_VIDEO_CENTERED'] = '1'
                    change_window = False
                for event in pygame.event.get():
                    if event.type == QUIT:
                        run = False
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        game_mode = "menu"
                        change_window = True
                        start = True

                if start:
                    number_platform = 1
                    pos_platform = [(350, 700), (175, 543), (105, 403), (213, 243), (466, 72), (512, -92), (126, -241),
                                    (383, -378), (178, -512), (416, -639)]
                    vel_y = 1

                    all_platforms = pygame.sprite.Group()
                    all_bananes = pygame.sprite.Group()
                    all_sprites = pygame.sprite.Group()

                    jungle = Jungle()
                    all_sprites.add(jungle)
                    player = Player(boutique.perso_selectionne)
                    all_sprites.add(player)
                    start = False


                ### PLATFORM ###
                if number_platform == 1:
                    for pos in pos_platform:
                        platform = Platform(0, 0)
                        platform.start(pos)
                        all_platforms.add(platform)
                        all_sprites.add(platform)

                        banane = Banane(platform.rect.center)
                        all_sprites.add(banane)
                        all_bananes.add(banane)
                    number_platform = len(pos_platform)

                while number_platform < len(pos_platform):
                    platform = Platform(pos_platform[len(pos_platform)-1][0],
                                        pos_platform[len(pos_platform)-1][1])
                    if pygame.sprite.spritecollide(platform, all_platforms, True):
                        pass
                    else:
                        all_platforms.add(platform)
                        all_sprites.add(platform)
                        pos_platform[number_platform] = platform.rect.center
                        number_platform += 1

                        banane = Banane(platform.rect.center)
                        all_sprites.add(banane)
                        all_bananes.add(banane)


                k = 0
                for platform in all_platforms:
                    platform.move(vel_y)
                    pos_platform[k] = platform.rect.center
                    if platform.rect.y > 800:
                        pygame.sprite.Sprite.kill(platform)
                        number_platform -= 1
                        del pos_platform[k]
                        pos_platform.append((0, 0))
                    k += 1


                ### SCORE/BANANE ###
                font = pygame.font.SysFont("BN Machine", 30, False)
                txt_score = font.render("Bananes : " + str(score), True, (0, 0, 0))


                hits_banane = pygame.sprite.spritecollide(player, all_bananes, True)
                if hits_banane:
                    score += 1

                for banane in all_bananes:
                    banane.move(vel_y)
                    if banane.rect.y > 750:
                        pygame.sprite.Sprite.kill(banane)


                ### UPDATE ###
                player.move()
                if player.rect.y > 800:
                    game_mode = "game over"
                    change_window = True
                    start = True
                player.update(all_platforms)
                for entity in all_sprites:
                    self.window.blit(entity.image, entity.rect)
                self.window.blit(txt_score, (10, 10))


            pygame.display.update()
            self.FPS.tick(60)
        pygame.quit()