import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from weapon import Weapon
from ui import UI
from enemy import Enemy

class Level:
    def __init__(self):
        
        # Get Display Surface
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        self.current_attack = None
        
        # Create Map
        self.create_map()
        
        # Create UI
        self.ui = UI()
    
    # Create Map Method
    def create_map(self):
        layout = {
            'walls' : import_csv_layout('./assets/map/map_Walls.csv'),
            'entities' : import_csv_layout('./assets/map/map_Entity.csv'),
        }
        
        graphics = {
            'tileset' : import_folder('./assets/tileset')
        }
        for style,layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE        
                        y = row_index * TILESIZE

                        if style == 'walls':
                            #Stone Walls
                            if col == '18':
                                Tile((x,y), [self.visible_sprites, self.obstacles_sprites], 'walls', graphics['tileset'][1])
                            #Wood Walls
                            if col == '26':
                                Tile((x,y), [self.visible_sprites, self.obstacles_sprites], 'walls', graphics['tileset'][5])
                        if style == 'entities':
                            if col == '29':
                                self.player = Player(
                                    (x,y), 
                                    [self.visible_sprites], 
                                    self.obstacles_sprites, 
                                    self.create_attack, 
                                    self.destroy_attack,
                                    self.create_magic)
                            else:
                                if col == '30' : enemy_name = 'bat'
                                elif col == '31' : enemy_name = 'blob'
                                elif col == '32' : enemy_name = 'zombie'
                                elif col == '33' : enemy_name = 'bat'
                                Enemy(enemy_name, (x,y), [self.visible_sprites], self.obstacles_sprites)

    
    # Create Attack Method
    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites])
    
    # Create Magic Method // Just prints for now
    def create_magic(self, style, strength, cost):
        print(style, strength, cost)
    
    # Destroy Attack Method
    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None
    
    # Run Method
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.ui.display(self.player)

# Camera Handler Class
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] / 2
        self.half_height = self.display_surface.get_size()[1] / 2
        self.offset = pygame.math.Vector2()

        # Draw Floor
        self.floor_surf = pygame.image.load('./assets/graphics/floor.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
    
    # Custom Draw Method
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #floor_offset_pos = self.floor_rect.topleft - self.offset
        #self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
    
    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
            enemy.update()
