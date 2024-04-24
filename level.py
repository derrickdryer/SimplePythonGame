import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice, randint
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particles import AnimationPlayer
from magic import MagicPlayer

class Level:
    def __init__(self):
        
        # Get Display Surface
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()
        
        # Create Map
        self.create_map()
        
        # Create UI
        self.ui = UI()
        
        self.animation_player = AnimationPlayer()
        
        self.magic_player = MagicPlayer(self.animation_player)
    
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
                                Enemy(
                                    enemy_name, 
                                    (x,y), 
                                    [self.visible_sprites, self.attackable_sprites], 
                                    self.obstacles_sprites, 
                                    self.damage_player, 
                                    self.trigger_death_particles)

    
    # Create Attack Method
    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites, self.attack_sprites])
    
    # Create Magic Method // Just prints for now
    def create_magic(self, style, strength, cost):
        if style == 'self_heal':
            self.magic_player.self_heal(self.player, strength, cost, [self.visible_sprites])
        elif style == 'fireball':
            self.magic_player.fireball(self.player, cost, [self.visible_sprites, self.attack_sprites])
        elif style == 'lightning_bolt':
            self.magic_player.lightning_bolt(self.player, cost, [self.visible_sprites, self.attack_sprites])
        elif style == 'ice_shard':
            self.magic_player.ice_shard(self.player, cost, [self.visible_sprites, self.attack_sprites])
        elif style == 'stone_throw':
            self.magic_player.stone_throw(self.player, cost, [self.visible_sprites, self.attack_sprites])
        elif style == 'wind_cutter':
            self.magic_player.wind_cutter(self.player, cost, [self.visible_sprites, self.attack_sprites])
    
    # Destroy Attack Method
    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None
    
    def player_attack_logic(self):
        for attack_sprite in self.attack_sprites:
            collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
            if collision_sprites:
                for target_sprite in collision_sprites:
                    if target_sprite == 'grass':
                        pos = target_sprite.rect.center
                        offset = pygame.math.Vector2(0, 75)
                        for leaf in range(randint(3,6)):
                            self.animation_player.create_grass_particles(pos - offset, [self.visible_sprites])
                        target_sprite.kill()
                    else:
                        target_sprite.get_damage(self.player, attack_sprite.sprite_type)
    
    def damage_player(self, amount, attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            # Spawn Particles
            self.animation_player.create_particles(attack_type, self.player.rect.center, [self.visible_sprites])
            
    def trigger_death_particles(self, pos, particle_type):
        self.animation_player.create_particles(particle_type, pos, [self.visible_sprites])
    
    # Run Method
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()
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
