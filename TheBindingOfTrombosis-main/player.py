import pygame

from projectile import Projectile
from entity import Entity
from settings import *
from debug import *

class Player(Entity):

    def __init__(self,pos,groups,obstacle_sprites,life):
        super().__init__(groups)

        self.image = pygame.image.load('./graphics/test/isaac.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2()
        self.attack_direction = pygame.math.Vector2()
        self.speed = 6
        if life != None:
            self.health = life
        else:
            self.health = 20
        self.obstacle_sprites = obstacle_sprites
        self.projectile_sprites = pygame.sprite.Group()
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        self.attacked = False
        self.attacked_cooldown = 700
        self.attacked_time = 400
        self.bisturi = 0
    def upgrade_attack_speed(self):
        self.attack_cooldown = 100

    def equipbist(self):
        self.bisturi = 1
    def upgrade_speed(self):
        self.speed = 8

    def create_bullet(self,dir):
        return Projectile(self.rect.x + TILESIZE/2,self.rect.y + TILESIZE/2,dir,(1,1), self.bisturi)

    def hit(self, bullets):
        for bullet in bullets:
            if bullet.rect.colliderect(self.rect) and self.health > 0:
                self.health -= proj_dmg
                if self.health <= 0:
                    self.kill()
                bullet.kill()


    def input(self):
        keys = pygame.key.get_pressed()
        #attack
        if keys[pygame.K_UP] and not self.attacking:
            self.attacking = True
            self.projectile_sprites.add(self.create_bullet('up'))
            self.attack_time = pygame.time.get_ticks()
            self.attack_direction.y = -1
        elif keys[pygame.K_DOWN] and not self.attacking:
            self.attacking = True
            self.projectile_sprites.add(self.create_bullet('down'))
            self.attack_direction.y = 1
            self.attack_time = pygame.time.get_ticks()
        elif keys[pygame.K_RIGHT] and not self.attacking:
            self.attacking = True
            self.projectile_sprites.add(self.create_bullet('right'))
            self.attack_direction.x = 1
            self.attack_time = pygame.time.get_ticks()
        elif keys[pygame.K_LEFT] and not self.attacking:
            self.attacking = True
            self.projectile_sprites.add(self.create_bullet('left'))
            self.attack_direction.x = -1
            self.attack_time = pygame.time.get_ticks()
        else:
            self.attack_direction.x = 0
            self.attack_direction.y = 0

        #movement
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False

    def cooldowns_atcked(self):
        current_time = pygame.time.get_ticks()
        if self.attacked:
            if current_time - self.attacked_time >= self.attacked_cooldown:
                self.attacked = False
    def hit_enemy(self,enemies):

        for enemy in enemies:
            current_time = pygame.time.get_ticks()
            if enemy.rect.colliderect(self.rect) and (not self.attacked) and current_time - self.attacked_time >= self.attacked_cooldown and self.health > 0:
                self.health -= 5
                self.attacked = True
                self.attacked_time = pygame.time.get_ticks()
                if self.health <= 0:
                    self.kill()
    def get_proj_sp(self):
        return self.projectile_sprites

    def bullet_collision(self):
        for bullet in self.projectile_sprites:
            for sprite in self.obstacle_sprites:
                bullet.collide(sprite)

    def upgrade_life(self):
        self.health += 10
    def get_life(self):
        return self.health
    def update(self):
        self.input()
        self.cooldowns()
        self.cooldowns_atcked()
        self.move(self.speed)
        debug(self.health)

    def get_player_x(self):
        return self.rect.x

    def get_player_y(self):
        return self.rect.y
    def collision(self, direction):
        if direction == 'horizontal':
            if self.rect.x >= WIDTH - 64:
                self.rect.right = WIDTH
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:  # move right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:  # move left
                        self.rect.left = sprite.rect.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:  # move up
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:  # move down
                        self.rect.top = sprite.rect.bottom


    def get_rect(self):
        return self.rect