# Entity Class

# Import libraries
import pygame
import json

class Entity(pygame.sprite.Sprite):
    DIRECTIONS = {'up':1, 'down':0, 'left':3, 'right':2}
    def __init__(self, json_file, sprite_sheet_file, sprite_size):
        super().__init__()
        self.spritesheet = pygame.image.load(sprite_sheet_file)
        self.sprite_size = sprite_size
        self.sprites = self.load_sprites()
        self.direction = 'down'
        self.current_sprite = 0
        self.animation_speed = 1
        self.moving = False
        self.scale_sprites(10)
        
        # Read json file
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

    def move(self, direction, boundary):
        if direction == 'up' and self.rect.y > 0:
            self.rect.y -= self.speed
        elif direction == 'down' and self.rect.y < boundary[1] - self.rect.height:
            self.rect.y += self.speed
        elif direction == 'left' and self.rect.x > 0:
            self.rect.x -= self.speed
        elif direction == 'right' and self.rect.x < boundary[0] - self.rect.width:
            self.rect.x += self.speed
        self.direction = direction
        self.moving = True

    def scale_sprites(self, scale_factor):
        for direction in self.sprites:
            for i in range(len(self.sprites[direction])):
                self.sprites[direction][i] = pygame.transform.scale(self.sprites[direction][i], (self.sprite_size[0]*scale_factor, self.sprite_size[1]*scale_factor))

    def load_sprites(self):
        sprites = {
            'up': [],
            'down': [],
            'left': [],
            'right': []
        }

        for y in range(4):
            for x in range(3):
                sprite = self.spritesheet.subsurface(
                    x * self.sprite_size[0], y * self.sprite_size[1], self.sprite_size[0], self.sprite_size[1])
                if y == 0:
                    sprites['down'].append(sprite)
                elif y == 1:
                    sprites['up'].append(sprite)
                elif y == 2:
                    sprites['left'].append(sprite)
                elif y == 3:
                    sprites['right'].append(sprite)

        return sprites

    def update(self):
        if self.moving:
            self.current_sprite = (self.current_sprite + 1) % 3  # Cycle through the 3 sprites
        else:
            self.current_sprite = 0  # Use the idle sprite
        self.image = self.sprites[self.direction][self.current_sprite]