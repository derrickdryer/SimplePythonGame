# player.py
from classes.entity import Entity, EntityNoSprite

class Player(Entity):
    def __init__(self, json_file, sprite_sheet_file, sprite_size):
        super().__init__(json_file, sprite_sheet_file, sprite_size)
        self.inventory = []
        self.exp = 0
    # Additional player-specific methods here

class PlayerNoSprite(EntityNoSprite):
    def __init__(self, json_file):
        super().__init__(json_file)
        self.inventory = []
        self.exp = 0
        self.speed = 5
    # Additional player-specific methods here
    
    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= self.speed
    
    def move_down(self):
        if self.rect.y < 1080 - self.rect.height:
            self.rect.y += self.speed
    
    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= self.speed
    
    def move_right(self):
        if self.rect.x < 1920 - self.rect.width:
            self.rect.x += self.speed