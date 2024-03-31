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
        self.sprites = []
        for y in range(0, self.sprite_sheet.get_height(), sprite_size[1]):
            for x in range(0, self.sprite_sheet.get_width(),sprite_size[0]):
                sprite = pygame.Surface(sprite_size, pygame.SRCALPHA)
                sprite.blit(self.sprite_sheet, (0, 0), (x, y, sprite_size[0], sprite_size[1]))
                self.sprites.append(sprite)
        
        # Set the current sprite
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
    
    def attack(self, target):
        # Attack logic
        pass
    
    def defend(self):
        # Defend logic
        pass
    
    def update(self):
        # Update sprite logic here
        pass

class EntityNoSprite(pygame.sprite.Sprite):
    def __init__(self, json_file):
        super().__init__()
        with open(json_file, 'r') as f:
            attributes = json.load(f)
        self.name = attributes['name']
        self.level = attributes['level']
        self.health = attributes['health']
        self.mana = attributes['mana']
        self.strength = attributes['strength']
        self.intelligence = attributes['intelligence']
        self.agility = attributes['agility']
        self.wisdom = attributes['wisdom']

        # Use a rectangle as a placeholder sprite
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))  # Fill with red color
        self.rect = self.image.get_rect()

    def update(self):
        # Update the sprite here
        pass