import random

import pygame
from settings import *
from debug import *
class Exit(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.Surface((64,64))
        self.rect = self.image.get_rect(topleft = pos)
    def get_rect(self):
        return self.rect