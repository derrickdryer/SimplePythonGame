import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Untitled Game')
        self.clock = pygame.time.Clock()
        self.level = Level()
    
    # Game Loop
    def run(self):
        self.playing = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
                    if event.key == pygame.K_ESCAPE:
                        self.level.pause_menu()
            
            self.screen.fill((75, 229, 89))
            self.level.run()
            pygame.display.flip()
            self.clock.tick(FPS)

# Main Function
if __name__ == '__main__':
    game = Game()
    game.run()
