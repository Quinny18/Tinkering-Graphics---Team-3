import random
import pygame

pygame.init()
main_window = pygame.display.set_mode((800,600))
running = True

# imports monster
image = pygame.image.load("Monster.png")

# change colours function (green to blue)
def green_to_blue(surface=pygame.Surface((1, 1))):
# check for pixels that are green
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_width()):
            pixel = surface.get_at((x, y))
            surface.set_at((x, y), pygame.Color(pixel.r, pixel.g, pixel.b))
# change colours function (red to black)
def red_to_black(surface=pygame.Surface((1, 1))):
# check for pixels that are green
    pixel = pygame.Color(0, 0, 0)
# change colours function (black? to red)
def black_to_red(surface=pygame.Surface((1, 1))):
# check for pixels that are green
    pixel = pygame.Color(0, 0, 0)
# change colours function (skin to green)
def skin_to_green(surface=pygame.Surface((1, 1))):
# check for pixels that are green
    pixel = pygame.Color(0, 0, 0)

# run image through the functions
green_to_blue(image)
red_to_black(image)
black_to_red(image)
skin_to_green(image)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_window.fill((255,255,255))
    main_window.blit(my_surface, (0, 60))

    # save new image
pygame.quit()