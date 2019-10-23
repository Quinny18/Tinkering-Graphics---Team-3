import math
import random
import pygame

pygame.init()
main_window = pygame.display.set_mode((150, 220))
running = True

# imports monster
image = pygame.image.load("Monster.png")

green = (173, 243, 77)
gray = (211, 211, 211)
red = (204, 27, 0)
beige = (250, 221, 182)
lower_Green = (173, 125, 77)
higher_Green = (173, 255, 77)


def colour_distance(colour1, colour2):
    answer = math.sqrt((colour1[0]-colour2[0])**2+(colour1[1]-colour2[1])**2+(colour1[2]-colour2[2])**2)
    return answer

def make_green(colour1, colour2, tolerance, surface=pygame.Surface((1, 1))):
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_width()):
            pixel = surface.get_at((x, y))
            if colour_distance(colour1, colour2) < tolerance:
                surface.set_at((x, y), pygame.Color(211, 211, 211))

# change colours function (green to blue)
def green_to_gray(surface=pygame.Surface((1, 1))):
# check for pixels that are green
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_width()):
            pixel = surface.get_at((x, y))
            if pixel == green:
                surface.set_at((x, y), pygame.Color(211, 211, 211))


make_green(higher_Green, lower_Green, 135, image)
green_to_gray(image)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_window.fill((255,255,255))
    main_window.blit(image, (0, 0))
    pygame.display.update()

    # save new image
pygame.quit()