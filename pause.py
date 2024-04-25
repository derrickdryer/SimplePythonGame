import pygame
from settings import *

class Pause:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, PAUSE_FONT_SIZE)
        self.text = self.font.render('PAUSED', False, (255, 255, 255))
        self.text_rect = self.text.get_rect(center = self.display_surface.get_rect().center)
    
    def display(self):
        self.display_surface.blit(self.text, self.text_rect)