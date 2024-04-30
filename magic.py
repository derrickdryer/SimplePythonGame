import pygame
from settings import *
from random import randint

class MagicPlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player
    
    def self_heal(self, player, strength, cost, groups):
        if player.energy >= cost:
            player.health += strength
            player.energy -= cost
            if player.health > player.stats['health']:
                player.health = player.stats['health']
            self.animation_player.create_particles('self_heal', player.rect.center, groups)
    
    def fireball(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            
            if player.status.split('_')[0] == 'right': direction = pygame.math.Vector2(1,0)
            elif player.status.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
            elif player.status.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
            else: direction = pygame.math.Vector2(0,1)
            
            for i in range(1, 6):
                if direction.x: #horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE//2, TILESIZE//2)
                    y = player.rect.centery
                    self.animation_player.create_particles('fireball', (x, y), groups)
                else: #vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx
                    y = player.rect.centery  + offset_y + randint(-TILESIZE//2, TILESIZE//2)
                    self.animation_player.create_particles('fireball', (x, y), groups)

    def lightning_bolt(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            
            if player.status.split('_')[0] == 'right': direction = pygame.math.Vector2(1,0)
            elif player.status.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
            elif player.status.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
            else: direction = pygame.math.Vector2(0,1)
            
            for i in range(1, 6):
                if direction.x: #horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE//2, TILESIZE//2)
                    y = player.rect.centery
                    self.animation_player.create_particles('lightning_bolt', (x, y), groups)
                else: #vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx
                    y = player.rect.centery  + offset_y + randint(-TILESIZE//2, TILESIZE//2)
                    self.animation_player.create_particles('lightning_bolt', (x, y), groups)
    
    def ice_shard(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            
            if player.status.split('_')[0] == 'right': direction = pygame.math.Vector2(1,0)
            elif player.status.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
            elif player.status.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
            else: direction = pygame.math.Vector2(0,1)
            
            for i in range(1, 6):
                if direction.x: #horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE//2, TILESIZE//2)
                    y = player.rect.centery
                    self.animation_player.create_particles('ice_shard', (x, y), groups)
                else: #vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx
                    y = player.rect.centery  + offset_y + randint(-TILESIZE//2, TILESIZE//2)
                    self.animation_player.create_particles('ice_shard', (x, y), groups)
    
    def stone_throw(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            
            if player.status.split('_')[0] == 'right': direction = pygame.math.Vector2(1,0)
            elif player.status.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
            elif player.status.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
            else: direction = pygame.math.Vector2(0,1)
            
            for i in range(1, 6):
                if direction.x: #horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE//2, TILESIZE//2)
                    y = player.rect.centery
                    self.animation_player.create_particles('stone_throw', (x, y), groups)
                else: #vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx
                    y = player.rect.centery  + offset_y + randint(-TILESIZE//2, TILESIZE//2)
                    self.animation_player.create_particles('stone_throw', (x, y), groups)
    
    def wind_cutter(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            
            if player.status.split('_')[0] == 'right': direction = pygame.math.Vector2(1,0)
            elif player.status.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
            elif player.status.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
            else: direction = pygame.math.Vector2(0,1)
            
            for i in range(1, 6):
                if direction.x: #horizontal
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x + randint(-TILESIZE//2, TILESIZE//2)
                    y = player.rect.centery
                    self.animation_player.create_particles('wind_cutter', (x, y), groups)
                else: #vertical
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx
                    y = player.rect.centery  + offset_y + randint(-TILESIZE//2, TILESIZE//2)
                    self.animation_player.create_particles('wind_cutter', (x, y), groups)