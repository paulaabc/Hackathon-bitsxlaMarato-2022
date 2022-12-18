import pygame

from enemy import Enemy
from settings import *
from textBox import TextBox
from tile import Tile
from player import Player
from debug import *
from exit import Exit
from boss import Boss
from trombocytes import Trombocyte
from item_hep import Item_hep
from item_bici import Item_bici
from item_verdurita import Item_verdurita
from item_bisturi import Item_bisturi

class Level:
    def __init__(self,num_level,screen):
        self.draw_text = False
        self.text = ""
        self.hide_text_event = None
        self.display_surface = pygame.display.get_surface()
        self.screen = screen
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        self.enemies_sprites = pygame.sprite.Group()
        self.trombocyte_sprites = pygame.sprite.Group()
        self.exit_sprites = pygame.sprite.Group()
        self.item_sprites = pygame.sprite.Group()
        self.textico = None
        self.enemies = []
        self.exits = []
        self.num_level = num_level
        self.boss = None
        self.vida = 20
        self.create_map()
        self.showText()

    def create_map(self):

        for row_id, row in enumerate(WORLD_MAP[self.num_level - 1]):
            for col_id, col in enumerate(row):
                x = col_id * TILESIZE
                y = row_id * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.obstacles_sprites])
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites,self.vida)
                if col == 'e':
                    self.enemies.append(
                        Enemy((x, y), [self.visible_sprites, self.enemies_sprites], self.obstacles_sprites,self.enemies_sprites))
                if col == 's':
                    self.exits.append(Exit((x, y), [self.exit_sprites]))
                if col == 'b':
                    self.boss = Boss((x, y), [self.visible_sprites,self.obstacles_sprites],self.player)
                if col == 't':
                    Trombocyte((x,y), [self.visible_sprites, self.obstacles_sprites, self.trombocyte_sprites])
                if col == 'h':
                    Item_hep((x,y),[self.visible_sprites,self.item_sprites])
                if col == 'c':
                    Item_bici((x,y),[self.visible_sprites,self.item_sprites])
                if col == 'v':
                    Item_verdurita((x,y),[self.visible_sprites,self.item_sprites])
                if col == 'i':
                    Item_bisturi((x,y),[self.visible_sprites,self.item_sprites])
    def reset_sprites(self):
        self.vida = self.player.get_life()
        self.player.kill()
        for enemy in self.enemies_sprites:
            enemy.kill()
            del enemy
        for tile in self.obstacles_sprites:
            tile.kill()
            del tile
        for exit in self.exits:
            exit.kill()
            del exit
        self.player.kill()
        if self.boss:
            self.boss.kill()
        del self.player
        if self.textico:
            self.textico.kill()
        for object in self.visible_sprites:
            object.kill()

    def collision_exit(self):
        for sprite in self.exit_sprites:
            if sprite.rect.colliderect(self.player.get_rect()) and not self.boss and len(self.enemies_sprites) == 0:
                self.num_level += 1
                self.reset_sprites()
                self.create_map()
    def collision_item(self):
        for sprite in self.item_sprites:
            if sprite.rect.colliderect(self.player.get_rect()) and sprite.type == "hep":
                for sp in self.trombocyte_sprites:
                    sp.kill()
                    del sp
                    sprite.kill()
                    self.player.upgrade_attack_speed()
                    self.player.upgrade_speed()

                self.draw_text = True
                self.text = "heparina"
                self.hide_text_event = pygame.USEREVENT + 1
                pygame.time.set_timer(self.hide_text_event, 5000, 1)  # 5 seconds, one time

            elif sprite.rect.colliderect(self.player.get_rect()) and sprite.type == "bici":
                sprite.kill()
                self.player.upgrade_speed()

                self.draw_text = True
                self.text = "bici"
                self.hide_text_event = pygame.USEREVENT + 1
                pygame.time.set_timer(self.hide_text_event, 5000, 1)  # 5 seconds, one time

            elif sprite.rect.colliderect(self.player.get_rect()) and sprite.type == "verdura":
                sprite.kill()
                self.player.upgrade_life()

                self.draw_text = True
                self.text = "verdurita"
                self.hide_text_event = pygame.USEREVENT + 1
                pygame.time.set_timer(self.hide_text_event, 5000, 1)  # 5 seconds, one time

            elif sprite.rect.colliderect(self.player.get_rect()) and sprite.type == "bisturi":
                sprite.kill()
                self.player.equipbist()

                self.draw_text = True
                self.text = "bisturi"
                self.hide_text_event = pygame.USEREVENT + 1
                pygame.time.set_timer(self.hide_text_event, 5000, 1)  # 5 seconds, one time

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        self.player.bullet_collision()
        self.player.get_proj_sp().draw(self.display_surface)
        self.player.get_proj_sp().update()
        if self.boss != None:
            self.boss.get_proj_sp().draw(self.display_surface)
            self.boss.get_proj_sp().update()
        for enemy in self.enemies:
            enemy.hit(self.player.get_proj_sp())
            enemy.change_dir(self.player.get_player_x(),self.player.get_player_y())
            enemy.move(enemy_speed)
        for trombocyte in self.trombocyte_sprites:
            trombocyte.hit(self.player.get_proj_sp())
        if self.boss:
            if self.boss.victory:
                self.draw_text = True
                self.text = "win"
            self.boss.hit(self.player.get_proj_sp())
            self.player.hit(self.boss.get_proj_sp())
        self.player.hit_enemy(self.enemies_sprites)
        self.collision_exit()
        self.collision_item()
        self.showText()
        # Revive:
        keys = pygame.key.get_pressed()
        if self.player.health <= 0 and keys[pygame.K_SPACE]:
            self.player.health = 15
            self.num_level = 1
            self.reset_sprites()
            self.create_map()

    def showText(self):
        for event in pygame.event.get():
            if event.type == self.hide_text_event:
                if self.textico:
                    self.textico.kill()
                    self.text = ""
                    self.hide_text_event = None
        if self.draw_text:
            x=(WIDTH-422)/2
            y=HEIGHT-120
            if self.text == "heparina":
                self.textico = TextBox((x, y), [self.visible_sprites], "H")
            elif self.text == "bisturi":
                self.textico = TextBox((x, y), [self.visible_sprites], "B")
            elif self.text == "verdurita":
                self.textico = TextBox((x, y), [self.visible_sprites], "V")
            elif self.text == "bici":
                self.textico = TextBox((x, y), [self.visible_sprites], "E")
            elif self.text == "win":
                self.textico = TextBox((0, 0), [self.visible_sprites], "W")
        else:
            if self.player.health <= 0:
                self.textico = TextBox((0, 0), [self.visible_sprites], "GO")
        self.draw_text = False

    def get_num_level(self):
        return self.num_level