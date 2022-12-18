import random

import pygame
from settings import *
from entity import Entity
from debug import *
class Enemy(Entity):
    def __init__(self,pos,groups,obstacle_sprites,enemy_sprites):
        super().__init__(groups)
        self.obstacle_sprites = obstacle_sprites
        self.image = pygame.image.load('./graphics/test/enemy.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2()
        self.health = 10
        self.enemy_sprites = enemy_sprites
        self.bisturi = 0
    def hit(self, bullets):
        for bullet in bullets:
            if bullet.rect.colliderect(self.rect) and self.health > 0:
                self.health -= bullet.dmg
                if self.health <= 0:
                    self.kill()
                if not bullet.bisturi:
                    bullet.kill()

    def change_dir(self,player_x,player_y):
        self.direction.x = player_x - self.rect.x
        self.direction.y = player_y - self.rect.y

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite != self:
                    if sprite.rect.colliderect(self.rect):
                        if self.direction.x > 0:  # move right
                            self.rect.right = sprite.rect.left
                        if self.direction.x < 0:  # move left
                            self.rect.left = sprite.rect.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite != self:
                    if sprite.rect.colliderect(self.rect):
                        if self.direction.y > 0:  # move up
                            self.rect.bottom = sprite.rect.top
                        if self.direction.y < 0:  # move down
                            self.rect.top = sprite.rect.bottom

        if direction == 'horizontal':
            for sprite in self.enemy_sprites:
                if sprite != self:
                    if sprite.rect.colliderect(self.rect):
                        if self.direction.x > 0:  # move right
                            self.rect.right = sprite.rect.left
                        if self.direction.x < 0:  # move left
                            self.rect.left = sprite.rect.right
        if direction == 'vertical':
            for sprite in self.enemy_sprites:
                if sprite != self:
                    if sprite.rect.colliderect(self.rect):
                        if self.direction.y > 0:  # move up
                            self.rect.bottom = sprite.rect.top
                        if self.direction.y < 0:  # move down
                            self.rect.top = sprite.rect.bottom



