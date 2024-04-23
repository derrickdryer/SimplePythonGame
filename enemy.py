import pygame
from settings import *
from entity import Entity
from support import import_folder

class Enemy(Entity):
    def __init__(self, enemy_name, pos, groups, obstacles_sprites):
        super().__init__(groups)
        self.sprite_type = 'enemy'

        # Graphics Setup
        self.import_graphics(enemy_name)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]

        # Movement
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacles_sprites = obstacles_sprites

        # Enemy Stats
        self.enemy_name = enemy_name
        enemy_name = monster_data[self.enemy_name]
        self.health = enemy_name['health']
        self.exp = enemy_name['exp']
        self.speed = enemy_name['speed']
        self.attack_damage = enemy_name['damage']
        self.resistance = enemy_name['resistance']
        self.attack_radius = enemy_name['attack_radius']
        self.notice_radius = enemy_name['notice_radius']
        self.attack_type = enemy_name['attack_type']

        # Player Interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400

    
    def import_graphics(self, name):
        self.animations = {'idle':[], 'move':[], 'attack':[]}
        main_path = f'./assets/enemy/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

    def get_player_dist_direct(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()
        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else: direction = pygame.math.Vector2(0,0)
        return distance, direction
    
    def get_status(self, player):
        distance = self.get_player_dist_direct(player)[0]

        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack':
                self.frame_index = 0
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'
    
    def actions(self, player):
        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
            print('attack')
        elif self.status == 'move':
            self.direction = self.get_player_dist_direct(player)[1]
        else:
            self.direction = pygame.math.Vector2()
    
    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def cooldown(self):
        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True
    
    def update(self):
        self.move(self.speed)
        self.animate()
        self.cooldown()
    
    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)