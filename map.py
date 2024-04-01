# map.py

# Import libraries
import pygame

tileset = pygame.image.load('assets/tilesheet/DevTextures.png')
tile_size = (16, 16) 

tiles = []
for i in range(4):  # assuming there are 4 tiles in a row
    tile = tileset.subsurface((i * tile_size[0], 0, tile_size[0], tile_size[1]))
    tiles.append(tile)

map_data = [[0 for _ in range(120)] for _ in range(68)]

def draw_map(screen):
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            screen.blit(tiles[tile], (x * tile_size[0], y * tile_size[1]))