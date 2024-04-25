import pygame
from support import import_folder
from random import choice

class AnimationPlayer:
    def __init__(self):
        self.frames = {
            # Magic
            'fireball' : import_folder('./assets/particles/fireball'),
            'lightning_bolt' : import_folder('./assets/particles/lightning_bolt'),
            'ice_shard' : import_folder('./assets/particles/ice_shard'),
            'stone_throw' : import_folder('./assets/particles/stone_throw'),
            'wind_cutter' : import_folder('./assets/particles/wind_cutter'),
            'self_heal' : import_folder('./assets/particles/self_heal'),
            
            # Attacks
            'bite' : import_folder('./assets/particles/bite'),
            'bludgeon' : import_folder('./assets/particles/bludgeon'),
            'slash' : import_folder('./assets/particles/slash'),
            
            # Monster Deaths
            'bat' : import_folder('./assets/particles/bat_death'),
            'blob' : import_folder('./assets/particles/blob_death'),
            'zombie' : import_folder('./assets/particles/zombie_death')
            
        }
    def reflect_images(self, frames):
        new_frames = []
        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames
    
    def create_grass_particles(self, pos, groups):
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(pos, animation_frames, groups)
    
    def create_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos, animation_frames, groups)

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'magic'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)
    
    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]
    
    def update(self):
        self.animate()