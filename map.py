# map.py

# Import libraries
import pytmx
tmx_data = pytmx.load_pygame('/assets/map.tmx')

def draw_tile(surface, tile_image, position):
    surface.blit(tile_image, (position[0] * TILE_SIZE, position[1] * TILE_SIZE))