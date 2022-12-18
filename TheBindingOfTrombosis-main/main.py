import pygame, sys
from settings import *
from level import Level


class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('TBOT')
        self.clock = pygame.time.Clock()
        self.level = Level(1,self.screen)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            background = pygame.image.load(f'./graphics/backgrounds/background{self.level.get_num_level()}.jpg').convert_alpha()
            self.screen.blit(background, (0, 0))

            self.image = pygame.image.load('./graphics/test/isaac.png').convert_alpha()
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
