# game_logic.py

# Import libraries
import pygame
from entity import Entity, EntityNoSprite
from player import Player, PlayerNoSprite
from goblin import GoblinNoSprite

# player = Player('json/player.json', 'assets/sprites/player_spritesheet.png', (32, 32))
# goblin = Entity('json/goblin.json', 'assets/sprites/goblin_spritesheet.png', (32, 32))
player = PlayerNoSprite('json/player.json')
goblin = GoblinNoSprite('json/goblin.json')

# Game Logic
def game_logic():
    player.update()
    goblin.update()
    return player

def handle_input():
    global player # Use the global player variable
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move_up()
    if keys[pygame.K_DOWN]:
        player.move_down()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()

    return True