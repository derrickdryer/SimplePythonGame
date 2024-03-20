# main.py

# Import game logic
import pygame
from game_logic import handle_input, game_logic, player

def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    running = True
    clock = pygame.time.Clock()
    
    while running:
        clock.tick(60)
        screen.fill((0, 0, 0))
        running = handle_input()
        game_logic()
        screen.blit(player.image, player.rect)
        pygame.display.flip()

if __name__ == "__main__":
    main()