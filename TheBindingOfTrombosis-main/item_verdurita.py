import pygame
from settings import *

class Item_verdurita(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('./graphics/brocoli.png').convert_alpha()
        DEFAULT_IMAGE_SIZE = (64, 64)
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect(topleft = pos)
        self.type = "verdura"
