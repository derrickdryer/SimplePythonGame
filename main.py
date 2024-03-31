# app.py

# Import the necessary libraries
import pygame, sys
from entity import Entity, EntityNoSprite
from player import Player, PlayerNoSprite
from goblin import GoblinNoSprite

# player = Player('json/player.json', 'assets/sprites/player_spritesheet.png', (32, 32))
# goblin = Entity('json/goblin.json', 'assets/sprites/goblin_spritesheet.png', (32, 32))
player = PlayerNoSprite('json/player.json')
goblin = GoblinNoSprite('json/goblin.json')

def game(screen):
    running = True
    clock = pygame.time.Clock()
    
    while running:
        clock.tick(60)
        screen.fill((0, 0, 0))
        result = handle_input(screen)
        if result == 'main_menu':
            return 'main_menu'
        game_logic()
        screen.blit(player.image, player.rect)
        pygame.display.flip()

def pause_menu(screen):
    # Constants
    WIDTH, HEIGHT = 1920, 1080
    FONT = pygame.font.Font(None, 32)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    # Create the buttons
    buttons = [
        pygame.Rect(WIDTH//2-100, 150, 200, 50),  # Resume button
        pygame.Rect(WIDTH//2-100, 250, 200, 50),  # Save button
        pygame.Rect(WIDTH//2-100, 350, 200, 50)   # Main menu button
    ]
    # Create the button texts
    button_texts = [
        FONT.render("Resume", True, WHITE),
        FONT.render("Save", True, WHITE),
        FONT.render("Main Menu", True, WHITE)
    ]
    paused = True
    while paused:
        # Fill the screen
        screen.fill(BLACK)
        # Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()
        # Draw the buttons with highlighting
        for i, button in enumerate(buttons):
            if button.collidepoint(mouse_pos):
                pygame.draw.rect(screen, (255, 255, 0), button)  # Yellow color for highlighting
            else:
                pygame.draw.rect(screen, (255, 0, 0), button)  # Red color
            # Calculate the center of the button and the text
            button_center = button.center
            text_rect = button_texts[i].get_rect(center=button_center)
            # Draw the text at the center of the button
            screen.blit(button_texts[i], text_rect)
        # Update the display
        pygame.display.flip()
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press ESC again to resume
                    paused = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].collidepoint(event.pos):  # Resume button
                    paused = False
                elif buttons[1].collidepoint(event.pos):  # Save button
                    print("Game saved!")
                    #save_game()
                elif buttons[2].collidepoint(event.pos):  # Main menu button
                    return 'main_menu'

def handle_input(screen):
    global player # Use the global player variable
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                result = pause_menu(screen)
                if result == 'main_menu':
                    return 'main_menu'
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

# Game Logic
def game_logic():
    player.update()
    goblin.update()
    return player, goblin

def main(screen=None):
    # Initialize Pygame
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 1920, 1080
    FONT = pygame.font.Font(None, 32)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Create the screen
    if screen is None:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Create the title
    title = FONT.render("Main Menu", True, WHITE)
    title_rect = title.get_rect(center=(WIDTH//2, 50))

    # Create the buttons
    buttons = [
        pygame.Rect(WIDTH//2-100, 150, 200, 50),
        pygame.Rect(WIDTH//2-100, 250, 200, 50),
        pygame.Rect(WIDTH//2-100, 350, 200, 50),
        pygame.Rect(WIDTH//2-100, 450, 200, 50)
    ]

    # Create the button texts
    button_texts = [
        FONT.render("Start Game", True, WHITE),
        FONT.render("Options", True, WHITE),
        FONT.render("Credits", True, WHITE),
        FONT.render("Quit", True, WHITE)
    ]

    # Main loop
    while True:
        # Fill the screen
        screen.fill(BLACK)

        # Draw the title
        screen.blit(title, title_rect)
        
        # Get the current mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Draw the buttons with highlighting
        for i, button in enumerate(buttons):
            if button.collidepoint(mouse_pos):
                pygame.draw.rect(screen, (255, 255, 0), button)  # Yellow color for highlighting
            else:
                pygame.draw.rect(screen, (255, 0, 0), button)  # Red color

            # Calculate the center of the button and the text
            button_center = button.center
            text_rect = button_texts[i].get_rect(center=button_center)

            # Draw the text at the center of the button
            screen.blit(button_texts[i], text_rect)

        # Update the display
        pygame.display.flip()

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].collidepoint(event.pos):
                    result = game(screen)
                    if result == 'main_menu':
                        break
                if buttons[1].collidepoint(event.pos):
                    print("Options")
                if buttons[2].collidepoint(event.pos):
                    print("Credits")
                if buttons[3].collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()