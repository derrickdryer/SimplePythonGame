import pygame
from settings import *

class UI:
    def __init__(self):
        
        # UI Settings
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        
        # Main UI Elements
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 40, ENERGY_BAR_WIDTH, BAR_HEIGHT)
        
        # Weapon Graphics Reference
        self.weapon_graphics = []
        for weapon in WEAPONS_LIST.values():
            path = weapon['sprite']
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)
        
        # Magic Graphics Reference
        self.magic_graphics = []
        for magic in MAGIC_DATA.values():
            path = magic['sprite']
            magic = pygame.image.load(path).convert_alpha()
            self.magic_graphics.append(magic)
    
    # Show Bar Method
    def show_bar(self, current, max_amount, bg_rect, color):
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
    
    # Show Experience Points Method
    def show_exp(self, exp):
        text_surf = self.font.render(str(int(exp)),False,TEXT_COLOR)
        x = pygame.display.get_surface().get_size()[0] - 10
        y = pygame.display.get_surface().get_size()[1] - 10
        text_rect = text_surf.get_rect(bottomright = (x, y))
        
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(10, 5))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(10, 5), 3)
    
    # Magic/Weapon Switch Overlays
    def selection_box(self, left, top, has_switched):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        if has_switched:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 3)
        else:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
        return bg_rect
    
    # Weapon Graphic Overlay
    def weapon_overlay(self, weapon_index, has_switched):
        bg_rect = self.selection_box(10, 620, has_switched)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center = bg_rect.center)
        self.display_surface.blit(weapon_surf, weapon_rect)
    
    # Magic Graphic Overlay
    def magic_overlay(self, magic_index, has_switched):
        bg_rect = self.selection_box(100, 620, has_switched)
        magic_surf = self.magic_graphics[magic_index]
        magic_rect = magic_surf.get_rect(center = bg_rect.center)
        self.display_surface.blit(magic_surf, magic_rect)
    
    # Display Handler
    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)
        self.show_exp(player.exp)
        self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)
        self.magic_overlay(player.magic_index, not player.can_switch_magic)