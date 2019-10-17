import random
import pygame

pygame.init()
main_window = pygame.display.set_mode((800,600))
running = True

def monster_generator():    #this generates what part of the monster we are using
    head_type = random.randint(0,3)
    horns_type = random.randint(0, 3)
    wings_type = random.randint(0, 3)
    arms_type = random.randint(0, 3)
    torso_type = random.randint(0, 3)
    legs_type = random.randint(0, 3)
    return arms_type, legs_type

monster_generator()
heads=[]
horns=[]
wings=[]
arms=[]
torso=[]
legs=[]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    my_surface, my_surface2 = pygame.image.load(r"C:\Users\isaac\OneDrive - Falmouth University\Pycharm\Shrek.png"), pygame.image.load(r"C:\Users\isaac\OneDrive - Falmouth University\Pycharm\Shrek.png")
    #images = [my_surface,my_surface2]
    #location = [(0, 60) ,(50, 60)]
    #length = len(images)

    main_window.fill((255,255,255))
    main_window.blit(my_surface, (0, 60))
    main_window.blit(my_surface2, (50, 60))

    pygame.display.update()
pygame.quit()