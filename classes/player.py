# player.py
from classes.entity import *

class Player(Entity):
    DIRECTIONS = {'up':0, 'down':1, 'left':2, 'right':3}
    def __init__(self, json_file, sprite_sheet_file, sprite_size):
        super().__init__(json_file, sprite_sheet_file, sprite_size)
        self.inventory = []
        self.exp = 0
        self.speed = 5
        self.spritesheet = pygame.image.load(sprite_sheet_file)
        self.sprite_size = sprite_size
        self.sprites = self.load_sprites()
        self.direction = 'down'
        for direction in ['up', 'down', 'left', 'right']:
            self.sprites.append(self.load_sprites_for_direction(direction))
        self.image = self.sprites[self.DIRECTIONS[self.direction]][0]
        self.rect = self.image.get_rect()
        self.current_sprite = 0
        self.animation_speed = 1
        self.moving = False
    
    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed
            self.direction = 'up'
            self.moving = True

    def move_down(self):
        if self.rect.y < 1080 - self.rect.height:
            self.rect.y += self.speed
            self.direction = 'down'
            self.moving = True
    
    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.speed
            self.direction = 'left'
            self.moving = True
    
    def move_right(self):
        if self.rect.x < 1920 - self.rect.width:
            self.rect.x += self.speed
            self.direction = 'right'
            self.moving = True
    
    def update(self):
        if self.moving:
            self.current_sprite += 1
            sprite_list_length = len(self.sprites[self.DIRECTIONS[self.direction]])
            if self.animation_speed != 0:
                self.current_sprite %= (sprite_list_length * self.animation_speed)
            else:
                self.current_sprite = 0
            self.image = self.sprites[self.DIRECTIONS[self.direction]][self.current_sprite // max(1, self.animation_speed)]