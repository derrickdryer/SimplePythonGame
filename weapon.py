import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.sprite_type = 'weapon'
        direction = player.status.split('_')[0]
        
        full_path = f'./assets/sprites/weapons/{player.weapon}/{direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()

        # Set the position of the weapon
        if direction == 'right':
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,5))
        if direction == 'left':
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,5))
        if direction == 'up':
            self.rect = self.image.get_rect(midtop = player.rect.midtop + pygame.math.Vector2(4,-14))
        if direction == 'down':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-6,-7))