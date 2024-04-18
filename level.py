import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from weapon import Weapon
from ui import UI

class Level:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        
        self.current_attack = None
        
        self.create_map()
        
        self.ui = UI()
    
    def create_map(self):
        layout = {
            'boundary' : import_csv_layout('./assets/map/map_Boundary.csv')
        }
        graphics = {
            'temp' : import_folder('./assets/graphics/Boundary')
        }
        print(graphics)
        for style,layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y), [self.visible_sprites, self.obstacles_sprites], 'boundary', graphics['temp'][0])
                        if style == 'grass':
                            #random_grass_image = choice(graphics['grass'])
                            #Tile((x,y), [self.visible_sprites], 'grass', random_grass_image)
                            pass
                        if style == 'object':
                            #surf = graphics['object'][int(col)]
                            #Tile((x,y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                            pass
        #for row_index, row in enumerate(WORLD_MAP):
        #    for col_index, col in enumerate(row):
        #        x = col_index * TILESIZE
        #        y = row_index * TILESIZE
        #        if col == 'x':
        #            Tile((x,y), [self.visible_sprites, self.obstacles_sprites])
        #        if col == 'p':
        #            self.player = Player((x,y), [self.visible_sprites], self.obstacles_sprites)
        self.player = Player((100,100), [self.visible_sprites], self.obstacles_sprites, self.create_attack, self.destroy_attack)
    
    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites])
        
    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None
    
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.ui.display(self.player)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] / 2
        self.half_height = self.display_surface.get_size()[1] / 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load('./assets/tilemap/floor.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
    
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)