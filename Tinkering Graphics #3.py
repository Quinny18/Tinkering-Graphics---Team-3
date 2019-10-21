import random
import pygame


def load_assets():  # this function loads all the assets of the monster parts
    heads = ["Assets\Heads\HumanHead.png", "Assets\Heads\LizardHead.png", "Assets\Heads\MonkeyHead.png",
             "Assets\Heads\ToucanHead.png"]
    # horns=["Assets\Horns\BigHorn.png","Assets\Horns\Little Horn.png"]
    wings = ["Assets\Wings\BatWing.png", "Assets\Wings\ParrotWing.png", "Assets\Wings\ToucanWing.png"]
    arms = ["Assets\Arms\HumanArm.png", "Assets\Arms\LizardArm.png", "Assets\Arms\LobsterArm.png",
            "Assets\Arms\MonkeyArm.png"]
    torsos = ["Assets\Torsos\HumanTorso.png", "Assets\Torsos\LizardTorso.png", "Assets\Torsos\MonkeyTorso.png",
              "Assets\Torsos\ToucanTorso.png"]
    legs = ["Assets\Legs\HumanLeg.png", "Assets\Legs\LizardLeg.png", "Assets\Legs\MonkeyLeg.png",
            "Assets\Legs\ToucanLeg.png"]
    monster_parts = heads + wings + arms + torsos + legs
    return monster_parts


def random_number_generator():  # this function generates random numbers
    head = random.randint(0, 3)
    wing = random.randint(4, 6)
    arm = random.randint(7, 10)
    torso = random.randint(11, 14)
    leg = random.randint(15, 18)
    random_numbers = [head, wing, arm, torso, leg]
    return random_numbers


def print_monster(monster, number):  # this function loads all the assets for the monster into pygame and lines them up
    head, wing, arm, torso, leg = number[0], number[1], number[2], number[3], number[4]
    main_window.blit(pygame.image.load(monster[wing]), (60, 30))  # wing
    main_window.blit(pygame.image.load(monster[arm]), (20, 70))  # arm
    main_window.blit(pygame.image.load(monster[leg]), (25, 120))  # leg, out or range?
    main_window.blit(pygame.image.load(monster[torso]), (25, 60))  # torso
    main_window.blit(pygame.image.load(monster[leg]), (55, 120))  # leg
    main_window.blit(pygame.image.load(monster[arm]), (55, 70))  # arm
    main_window.blit(pygame.image.load(monster[head]), (0, 40))  # head
    # main_window.blit(load_Horn, (40, 20))


def keep_monster():  # this function allows the user to keep their monster or get a new one
    loop = True
    while loop == True:
        keep = input("Do you want to keep the current monster?")
        if keep == "yes":
            print('Your monster has been saved as "Monster.png"')
            pygame.image.save(main_window, "Monster.png")
            input("Press enter to end the program")
            running = False
            loop = False
        elif keep == "no":
            print("Loading next monster")
            loop = False
        else:
            print('Please enter "yes" or "no"')


pygame.init()
main_window = pygame.display.set_mode((150, 220))
running = True

monster_parts = load_assets()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_window.fill((255, 255, 255))
    random_numbers = random_number_generator()
    print_monster(monster_parts, random_numbers)
    pygame.display.update()
    keep_monster()

pygame.quit()
