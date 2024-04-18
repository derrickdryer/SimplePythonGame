from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    terrain = []
    with open(path, 'r') as level_file:
        level = reader(level_file, delimiter=',')
        for row in level:
            terrain.append(list(row))
        return terrain

#print(import_csv_layout('./assets/map/map_Boundary.csv'))
def import_folder(path):
    surface_list = []
    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            #print(full_path)
            img_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surf)
    return surface_list