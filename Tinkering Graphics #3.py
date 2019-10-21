import random
import pygame
import time

pygame.init()
main_window = pygame.display.set_mode((150,220))
running = True

heads=[r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Heads\HumanHead.png",
r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Heads\LizardHead.png",
r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Heads\MonkeyHead.png",
r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Heads\ToucanHead.png"]

horns=[r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Horns\BigHorn.png",
r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Horns\Little Horn.png"]

wings=[r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Wings\BatWing.png",
r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Wings\ParrotWing.png",
r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Wings\ToucanWing.png"]

arms=[r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Arms\HumanArm.png",
r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Arms\LizardArm.png",
r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Arms\LobsterArm.png",
r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Arms\MonkeyArm.png"]

torsos=[r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Torsos\HumanTorso.png",
r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Torsos\LizardTorso.png",
r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Torsos\MonkeyTorso.png",
r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Torsos\ToucanTorso.png"]

legs=[r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Legs\HumanLeg.png",
r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Legs\LizardLeg.png",
r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Legs\MonkeyLeg.png",
r"C:\Users\isaac\Desktop\Tinkering-Graphics---Team-3\Assets\Legs\ToucanLeg.png"]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #images = [my_surface,my_surface2]
    #location = [(0, 60) ,(50, 60)]
    #length = len(images)

    main_window.fill((255,255,255))
    load_Arm = pygame.image.load (random.choice(arms))
    load_Head = pygame.image.load(random.choice(heads))
    load_Leg = pygame.image.load (random.choice(legs))
    load_Torso = pygame.image.load(random.choice(torsos))
    load_Wing = pygame.image.load(random.choice(wings))
    load_Horn = pygame.image.load(random.choice(horns))

    main_window.blit(load_Wing, (60, 30))
    main_window.blit(load_Arm, (20, 70))
    main_window.blit(load_Leg, (25, 120))
    main_window.blit(load_Torso, (25, 60))
    main_window.blit(load_Leg, (55, 120))
    main_window.blit(load_Arm, (55, 70))
    main_window.blit(load_Head, (0, 40))
    #main_window.blit(load_Horn, (40, 20))

    pygame.display.update()
    time.sleep(2)
pygame.image.save(main_window,"Monster.png")
pygame.quit()