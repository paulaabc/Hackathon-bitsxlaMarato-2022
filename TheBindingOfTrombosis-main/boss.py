import random

import pygame
from settings import *
from entity import Entity
from debug import *
from projectile import Projectile
import numpy as np
class Boss(pygame.sprite.Sprite):
    def __init__(self,pos,groups,player):
        super().__init__(groups)

        self.image = pygame.image.load('./graphics/test/boss.png').convert_alpha()
        DEFAULT_IMAGE_SIZE = (256, 276)
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.health = 300
        self.pos = pos
        self.rect = self.image.get_rect(topleft = pos)
        self.attack_direction = pygame.math.Vector2()
        self.projectile_sprites = pygame.sprite.Group()
        self.attacking = False
        self.attack_cooldown = 600
        self.attack_time = None
        self.player = player
        self.victory = False
    def create_bullet(self):
        vector = np.array([self.rect.x - (self.player.get_player_x()), self.rect.y - (self.player.get_player_y())])
        unit_vector = vector / np.linalg.norm(vector)
        return Projectile(self.rect.x + TILESIZE/2,self.rect.y + TILESIZE/2,'boss',-unit_vector,0)

    def hit(self, bullets):
        for bullet in bullets:
            if bullet.rect.colliderect(self.rect) and self.health > 0:
                self.health -= bullet_dmg
                if self.health <= 50:
                    self.attack_cooldown = 250
                elif self.health <= 100:
                    self.attack_cooldown = 350
                elif self.health <= 120:
                    self.attack_cooldown = 400
                elif self.health <= 160:
                    self.attack_cooldown = 500

                if self.health <= 0:
                    self.victory = True
                    self.kill()
                bullet.kill()


    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def get_proj_sp(self):
        return self.projectile_sprites

    def shoot(self):
        if not self.attacking:
            self.attacking = True
            self.projectile_sprites.add(self.create_bullet())
            self.attack_time = pygame.time.get_ticks()
    def update(self):
        self.shoot()
        self.cooldowns()

    def get_proj_sp(self):
        return self.projectile_sprites
