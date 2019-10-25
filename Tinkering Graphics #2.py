import pygame
import LevelOptions
import random
import time

ChunkSize = 32
ScreenSizeX = 1024
ScreenSizeY = 576

Dirt = 0
Grass = 1
Water = 2
pit2 = 3
pit3 = 4

Campfire2 = 0
Shrine2 = 1
pit = 2

Textures = {
    Dirt: pygame.image.load('Dirt2.png'),
    Grass: pygame.image.load('Grass2.png'),
    Water: pygame.image.load('Water2.png'),
    pit2: pygame.image.load('Pit2.png'),
    pit3: pygame.image.load('Pit3.png')
}
Line3 = {
    Campfire2: pygame.image.load('Campfire2.png'),
    Shrine2: pygame.image.load('Shrine2.png'),
    pit: pygame.image.load('Pit.png')
}

Main_Window = pygame.display.set_mode((ScreenSizeX, ScreenSizeY))
running = True


def tile_assignment():
    for x in range(0, 1024, 32):
        Main_Window.blit(random.choice(Line3), (x, 480))
    for x in range(0, 1024, 32):
        Main_Window.blit(random.choice(Textures), (x, 512))
    for x in range(0, 1024, 32):
        Main_Window.blit(random.choice(Textures), (x, 544))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Main_Window.fill((135, 206, 235))
    tile_assignment()
    pygame.display.flip()
    Main_Window.blit(random.choice(Textures), (0, 0))
    time.sleep(5)



pygame.quit()
