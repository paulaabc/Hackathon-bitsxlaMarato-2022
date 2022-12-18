import pygame
from settings import *


class Trombocyte(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.health = 10
        self.image = pygame.image.load('./graphics/test/trombocyte.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

    def hit(self, bullets):
        for bullet in bullets:
            if bullet.rect.colliderect(self.rect) and self.health > 0:
                self.health -= bullet.dmg
                if self.health <= 0:
                    self.kill()
                bullet.kill()
