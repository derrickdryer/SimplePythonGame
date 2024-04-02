# player.py
from classes.entity import *

class Player(Entity):
    def __init__(self, json_file, sprite_sheet_file, sprite_size):
        self.image = pygame.image.load(sprite_sheet_file)
        super().__init__(json_file, sprite_sheet_file, sprite_size)
        self.inventory = []
        self.exp = 0
        self.speed = 10
        self.rect = self.image.get_rect()
        self.frame_counter = 0
        self.moving = False
        
        for direction in ['up', 'down', 'left', 'right']:
            self.sprites[direction] = self.load_sprites_for_direction(direction)
        
        self.scale_sprites(10)

    def move(self, direction):
        super().move(direction, (1920, 1080))  # Assuming the boundary is (1920, 1080)
        self.moving = True
        self.update()  # Update the player's sprite
    
    def update(self):
        if self.moving:  # Only change the sprite when moving is True
            self.frame_counter += 1
            if self.frame_counter >= 10:  # Change the sprite every 10 frames
                self.frame_counter = 0
                self.current_sprite = (self.current_sprite + 1) % len(self.sprites[self.direction])
        else:
            self.current_sprite = 0  # Reset the sprite to the first frame when not moving
        self.image = self.sprites[self.direction][self.current_sprite]
    
    def load_sprites_for_direction(self, direction):
        sprites = []
        for x in range(3):
            sprite = self.spritesheet.subsurface(
                x * self.sprite_size[0], Entity.DIRECTIONS[direction] * self.sprite_size[1], self.sprite_size[0], self.sprite_size[1])
            sprites.append(sprite)
        return sprites
    
    def check_collision(self, other):
        return pygame.sprite.collide_mask(self, other)