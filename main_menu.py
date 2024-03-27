# main_menu.py

# Import the necessary libraries
import pygame, sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FONT = pygame.font.Font(None, 32)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
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
                print("Start Game")
            if buttons[1].collidepoint(event.pos):
                print("Options")
            if buttons[2].collidepoint(event.pos):
                print("Credits")
            if buttons[3].collidepoint(event.pos):
                pygame.quit()
                sys.exit()