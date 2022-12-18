import pygame
from settings import *
import numpy as np
class Projectile(pygame.sprite.Sprite):

    def __init__(self, x_pos, y_pos, direction, vect, bisturi):
        super().__init__()
        self.image = pygame.image.load('./graphics/bullet.png').convert_alpha()
        self.direction = direction
        if direction == 'up':
            self.rect = self.image.get_rect(center=(x_pos, y_pos-32))
        elif direction == 'down':
            self.rect = self.image.get_rect(center=(x_pos, y_pos+32))
        elif direction == 'left':
            self.rect = self.image.get_rect(center=(x_pos-32, y_pos))
        elif direction == 'right':
            self.rect = self.image.get_rect(center=(x_pos+32, y_pos))
        else:
            self.vect = vect
            self.rect = self.image.get_rect(center=(x_pos,y_pos))
            self.image = pygame.image.load('./graphics/bala_enemy.png').convert_alpha()

        self.bisturi = bisturi


        self.dmg = proj_dmg
    def update(self):
        if self.direction == 'up':
            self.rect.y -= proj_speed
            if self.rect.y <= - 200:
                self.kill()
        elif self.direction == 'down':
            self.rect.y += proj_speed
            if self.rect.y >= HEIGHT + 200:
                self.kill()
        elif self.direction == 'left':
            self.rect.x -= proj_speed
            if self.rect.x <= -200:
                self.kill()
        elif self.direction == 'right':
            self.rect.x += proj_speed
            if self.rect.x >= WIDTH + 200:
                self.kill()
        else:
            self.rect.x += proj_speed * self.vect[0]
            self.rect.y += proj_speed * self.vect[1]
            DEFAULT_IMAGE_SIZE = (32, 32)
            self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
            if self.rect.y <= - 200 or self.rect.x >= WIDTH + 200 or self.rect.x <= -200 or self.rect.y >= HEIGHT + 200:
                self.kill()

    def collide(self, rect):
        if self.rect.colliderect(rect) and self.direction != 'boss':
            self.kill()

    def get_pos_x(self):
        return self.rect.x

    def get_pos_y(self):
        return self.rect.y
