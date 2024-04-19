import pygame
from settings import *
from support import import_folder
from entity import Entity

class Player(Entity):
    def __init__(self, pos, groups, obstacles_sprites, create_attack, destroy_attack, create_magic):
        super().__init__(groups)
        # Basic Sprite Settings w/ Fallback Image
        self.image = pygame.image.load('assets/player_placeholder.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -10)
        
        # Animation
        self.import_player_assets()
        self.status = 'down'

        # Movement
        self.attacking = False
        self.attacking_cooldown = 500
        self.attack_time = None
        self.obstacles_sprites = obstacles_sprites
        
        # Weapon
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(WEAPONS_LIST.keys())[self.weapon_index]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = 300
        
        # Magic
        self.create_magic = create_magic
        self.destroy_magic = None
        self.magic_index = 0
        self.magic = list(MAGIC_DATA.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None
        self.switch_magic_cooldown = 300
        
        # Player Stats
        self.stats = {'health' : 100, 'energy' : 60, 'attack' : 10, 'magic' : 4, 'speed' : 6}
        self.health = self.stats['health'] * 0.5
        self.energy = self.stats['energy'] * 0.8
        self.attack = self.stats['attack']
        self.magic = self.stats['magic']
        self.speed = self.stats['speed']
        self.exp = 10
        
    # Input Handler
    def input(self):
        if not self.attacking:
            keys = pygame.key.get_pressed()
            
            # Movement Vertical
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            # Movement Horizontal
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0
            
            # Weapon Attack
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()

            # Magic Attack
            if keys[pygame.K_LSHIFT]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                style = list(MAGIC_DATA.keys())[self.magic_index]
                strength = list(MAGIC_DATA.values())[self.magic_index]['strength'] + self.stats['magic']
                cost = list(MAGIC_DATA.values())[self.magic_index]['cost']
                self.create_magic(style, strength, cost)
            
            # Weapon Switching
            if keys[pygame.K_TAB] and self.can_switch_weapon:
                self.can_switch_weapon = False
                self.weapon_switch_time = pygame.time.get_ticks()
                if self.weapon_index < len(list(WEAPONS_LIST.keys())) - 1:
                    self.weapon_index += 1
                else:
                    self.weapon_index = 0
                self.weapon = list(WEAPONS_LIST.keys())[self.weapon_index]
            
            # Magic Switching
            if keys[pygame.K_q] and self.can_switch_magic:
                self.can_switch_magic = False
                self.magic_switch_time = pygame.time.get_ticks()
                if self.magic_index < len(list(MAGIC_DATA.keys())) - 1:
                    self.magic_index += 1
                else:
                    self.magic_index = 0
                self.weapon = list(MAGIC_DATA.keys())[self.magic_index]
    
    # Get Player Status
    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
        
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')

    # Animation Handler
    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    # Graphic Handler
    def import_player_assets(self):
        character_path = './assets/sprites/player'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
            'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
            'up_attack': [], 'down_attack': [], 'left_attack': [], 'right_attack': []}
        
        for animation in self.animations.keys():
            full_path = character_path + '/' + animation
            self.animations[animation] = import_folder(full_path)
    
    # Cooldown Handler
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        
        if self.attacking:
            if current_time - self.attack_time >= self.attacking_cooldown:
                self.attacking = False
                self.destroy_attack()
        
        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True
        
        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
                self.can_switch_magic = True
    
    # Update Handler
    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
