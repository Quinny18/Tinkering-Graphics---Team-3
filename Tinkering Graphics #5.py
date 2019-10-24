import pygame
import time

def blindness(my_surface):
    loop=True
    while loop==True:
        answer = int(input("What type of texture do you want to generate? Enter the corresponding number\n 1) Normal: \n 2) "
                           "Protanopia: \n 3) Deuteranopia: \n 4) Tritanopia: \n Enter Here:" ))
        if answer == 1:
            normal_view(my_surface)
            loop=False
        elif answer == 2:
            protanopia_view(my_surface)
            loop=False
        elif answer == 3:
            deuteranopia_view(my_surface)
            loop=False
        elif answer == 4:
            tritanopia_view(my_surface)
            loop=False
        else:
            print("Please Enter 1,2,3 or 4")
    return my_surface


def normal_view(picture):
    pixel = pygame.Color(0,0,0)
    for a in range(picture.get_width()):
        for b in range(picture.get_height()):
            pixel = picture.get_at((a,b))
            picture.set_at((a, b), pygame.Color(pixel.r, pixel.g, pixel.b))
    return my_surface


def protanopia_view(picture):
    pixel = pygame.Color(0, 0, 0)
    for a in range(picture.get_width()):
        for b in range(picture.get_height()):
            pixel = picture.get_at((a, b))
            picture.set_at((a, b), pygame.Color(int(pixel.r * 0.5), int(pixel.g * 0.5), pixel.b))
    return my_surface


def deuteranopia_view(picture):
    pixel = pygame.Color(0, 0, 0)
    for a in range(picture.get_width()):
        for b in range(picture.get_height()):
            pixel = picture.get_at((a, b))
            picture.set_at((a, b), pygame.Color(int(pixel.r * 0.5), int(pixel.g * 0.2), pixel.b))
    return my_surface


def tritanopia_view(picture):
    pixel = pygame.Color(0, 0, 0)
    for a in range(picture.get_width()):
        for b in range(picture.get_height()):
            pixel = picture.get_at((a, b))
            picture.set_at((a, b), pygame.Color(pixel.r, int(pixel.g * 0.2), int(pixel.b * 0.5)))
    return my_surface

pygame.init()
main_window = pygame.display.set_mode((800,600))
my_surface = pygame.image.load('test.png').convert()
blindness(my_surface)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_window.fill((255, 255, 255))
    main_window.blit(my_surface, (0, 0))
    pygame.display.update()
    print("Converted Image")
    time.sleep(10)
    running=False
pygame.quit()