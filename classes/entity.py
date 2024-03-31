# Entity Class

# Import libraries
import pygame
import json

# Define entities that will be used as enemies later on
class Entity(pygame.sprite.Sprite):
    def __init__(self, json_file, sprite_sheet_file, sprite_size):
        super().__init__()
        
        # Read json file
        with open(json_file, 'r') as f:
            attributes = json.load(f)
        
        # Load attributes
        self.name = attributes['name']
        self.level = attributes['level']
        self.health = attributes['health']
        self.mana = attributes['mana']
        self.strength = attributes['strength']
        self.intelligence = attributes['intelligence']
        self.agility = attributes['agility']
        self.wisdom = attributes['wisdom']
        
        # Load the sprite sheet
        self.sprite_sheet = pygame.image.load(sprite_sheet_file).convert_alpha()
        
        # Extract the sprites
        self.sprites = {
            'up' : [],
            'down' : [],
            'left' : [],
            'right' : []
        }
        for y in range(0, self.sprite_sheet.get_height(), sprite_size[1]):
            for x in range(0, self.sprite_sheet.get_width(), sprite_size[0]):
                if x // sprite_size[0] < 3:  # Only take the first 3 sprites of each row
                    sprite = pygame.Surface(sprite_size, pygame.SRCALPHA)
                    sprite.blit(self.sprite_sheet, (0, 0), (x, y, sprite_size[0], sprite_size[1]))
                    direction = 'down' if y < sprite_size[1] else 'up' if y < 2*sprite_size[1] else 'left' if y < 3*sprite_size[1] else 'right'
                    self.sprites[direction].append(sprite)
        
        # Initialize current_sprite and animation_speed
        self.direction = 'down'
        
        # Set the current sprite
        self.image = self.sprites[self.direction][0]
        self.rect = self.image.get_rect()
    
    def update(self):
        self.current_sprite += 1
        if self.current_sprite // self.animation_speed >= len(self.sprites[self.direction]):
            self.current_sprite = 0
        self.image = self.sprites[self.direction][self.current_sprite // self.animation_speed]