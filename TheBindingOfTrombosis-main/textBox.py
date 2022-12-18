import pygame
from settings import *

class TextBox(pygame.sprite.Sprite):
    def __init__(self, pos, groups, capital):
        super().__init__(groups)
        if capital == "H":
            self.image = pygame.image.load('./graphics/test/textHeparina.png').convert_alpha()
        elif capital == "B":
            self.image = pygame.image.load('./graphics/test/textBistu.png').convert_alpha()
        elif capital == "V":
            self.image = pygame.image.load('./graphics/test/textBrocoli.png').convert_alpha()
        elif capital == "E":
            self.image = pygame.image.load('./graphics/test/textEsport.png').convert_alpha()
        elif capital == "GO":
            self.image = pygame.image.load('./graphics/test/GameOver.png').convert_alpha()
            DEFAULT_IMAGE_SIZE = (1280, 720)
            self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        elif capital == "W":
            self.image = pygame.image.load('./graphics/test/Win.png').convert_alpha()
            DEFAULT_IMAGE_SIZE = (1280, 720)
            self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.pos = pos
        self.rect = self.image.get_rect(topleft = pos)
        self.type = "hep"

