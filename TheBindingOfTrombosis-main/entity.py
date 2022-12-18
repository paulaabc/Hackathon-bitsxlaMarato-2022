import pygame
import math
class Entity(pygame.sprite.Sprite):
    def __int__(self,groups):
        super().__int__(groups)

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        if self.direction.x * speed <= 0:
            self.rect.x += self.direction.x * speed
        else:
            self.rect.x += int(math.ceil(self.direction.x * speed))
        self.collision('horizontal')
        if self.direction.y * speed <= 0:
            self.rect.y += self.direction.y * speed
        else:
            self.rect.y += int(math.ceil(self.direction.y * speed))
        self.collision('vertical')

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