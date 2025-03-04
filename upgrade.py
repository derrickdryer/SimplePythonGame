import pygame
from settings import *

class Upgrade:
    def __init__(self, player):
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.attribute_num = len(player.stats)
        self.attribute_names = list(player.stats.keys())
        self.max_values = list(player.max_stats.values())
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        self.selection_index = 0
        self.selection_time = None
        self.can_move = True

        self.height = self.display_surface.get_size()[1] * 0.8
        self.width = self.display_surface.get_size()[0] // 6
        self.create_items()
    
    def input(self):
        keys = pygame.key.get_pressed()
        if self.can_move:
            if keys[pygame.K_RIGHT] and self.selection_index < self.attribute_num - 1:
                self.selection_index += 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_LEFT] and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()

        if keys[pygame.K_SPACE]:
            self.can_move = False
            self.selection_time = pygame.time.get_ticks()
            self.item_list[self.selection_index].trigger(self.player)
    
    def selection_cooldown(self):
        if not self.can_move:
            current_time = pygame.time.get_ticks()
            if current_time - self.selection_time >= 300:
                self.can_move = True
    
    def create_items(self):
        self.item_list = []
        for item, index in enumerate(range(self.attribute_num)):
            full_width = self.display_surface.get_size()[0]
            increment = full_width // self.attribute_num
            left = (item * increment) + (increment - self.width) // 2
            top = self.display_surface.get_size()[1] * 0.1

            item = Item(left, top, self.width, self.height, index, self.font)
            self.item_list.append(item)

    def display(self):
        self.input()
        self.selection_cooldown()

        for index, item in enumerate(self.item_list):
            name = self.attribute_names[index]
            value = self.player.get_value_by_index(index)
            max_value = self.max_values[index]
            cost = self.player.get_cost_by_index(index)
            item.display(self.display_surface, self.selection_index, name, value, max_value, cost)

class Item:
    def __init__(self, l, t, w, h, index, font):
        self.rect = pygame.Rect(l, t, w, h)
        self.index = index
        self.font = font

    def display_names(self, surface, name, cost, selected):
        color = TEXT_COLOR_SELECTED if selected else TEXT_COLOR
        title_surface = self.font.render(name, False, color)
        title_rect = title_surface.get_rect(midtop = self.rect.midtop + pygame.math.Vector2(0, 20))
        surface.blit(title_surface, title_rect)

        cost_surface = self.font.render(f'Cost: {int(cost)}', False, color)
        cost_rect = cost_surface.get_rect(midbottom = self.rect.midbottom - pygame.math.Vector2(0, 20))
        surface.blit(cost_surface, cost_rect)

    def display_bar(self, surface, value, max_value, selected):
        top = self.rect.midtop + pygame.math.Vector2(0, 60)
        bottom = self.rect.midbottom - pygame.math.Vector2(0, 60)
        color = BAR_COLOR_SELECTED if selected else BAR_COLOR

        full_height = bottom[1] - top[1]
        relative_num = (value / max_value) * full_height
        value_rect = pygame.Rect(top[0] - 15, bottom[1] - relative_num, 30, 10)

        pygame.draw.line(surface, color, top, bottom, 10)
        pygame.draw.rect(surface, color, value_rect)

    def trigger(self, player):
        upgrade_attr = list(player.stats.keys())[self.index]
        if player.exp >= player.get_cost_by_index(self.index) and player.stats[upgrade_attr] < player.max_stats[upgrade_attr]:
            player.exp -= player.get_cost_by_index(self.index)
            player.stats[upgrade_attr] *= 1.2
            player.upgrade_cost[upgrade_attr] *= 1.4
        if player.stats[upgrade_attr] > player.max_stats[upgrade_attr]:
            player.stats[upgrade_attr] = player.max_stats[upgrade_attr]

    def display(self, surface, selection_num, name, value, max_value, cost):
        if self.index == selection_num:
            pygame.draw.rect(surface, UPGRADE_BG_COLOR_SELECTED, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
        else:
            pygame.draw.rect(surface, UI_BG_COLOR, self.rect)
        self.display_names(surface, name, cost, self.index == selection_num)
        self.display_bar(surface, value, max_value, self.index == selection_num)