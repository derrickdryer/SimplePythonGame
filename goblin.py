import random
from entity import Entity, EntityNoSprite

class GoblinNoSprite(EntityNoSprite):
    def __init__(self, json_file):
        super().__init__(json_file)
        self.speed = 2  # Adjust this value to change the goblin's speed
        self.image.fill((0, 0, 255))  # Fill with blue color

    def update(self):
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up' and self.rect.y > 0:
            self.rect.y -= self.speed
        elif direction == 'down' and self.rect.y < 1080 - self.rect.height:
            self.rect.y += self.speed
        elif direction == 'left' and self.rect.x > 0:
            self.rect.x -= self.speed
        elif direction == 'right' and self.rect.x < 1920 - self.rect.width:
            self.rect.x += self.speed