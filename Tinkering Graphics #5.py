import pygame

pygame.init()


def normal_view(picture):

    for a in range(picture.get_width()):
        for b in range(picture.get_height()):
            colourofpixel = picture.get_at((a,b))
            colourofpixel[0] = 0
            picture.set_at((a, b), colourofpixel)


def protanopia_view(picture):

    for a in range(picture.get_width()):
        for b in range(picture.get_height()):
            colourofpixel = picture.get_at((a,b))
            colourofpixel[0] = 0
            picture.set_at((a, b), colourofpixel)


def deuteranopia_view(picture):

    for a in range(picture.get_width()):
        for b in range(picture.get_height()):
            colourofpixel = picture.get_at((a,b))
            colourofpixel[0] = 0
            picture.set_at((a, b), colourofpixel)


def tritanopia_view(picture):

    for a in range(picture.get_width()):
        for b in range(picture.get_height()):
            colourofpixel = picture.get_at((a,b))
            colourofpixel[0] = 0
            picture.set_at((a, b), colourofpixel)


main_window = pygame.display.set_mode((800,600))
my_surface = pygame.image.load('test.png').convert()


running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_window.fill((255, 255, 255))
    main_window.blit(my_surface, (0, 0))
    pygame.display.update()

pygame.quit()