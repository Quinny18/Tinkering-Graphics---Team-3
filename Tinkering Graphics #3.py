import random
import pygame


def load_assets():  # this function loads all the assets of the monster parts
    heads = ["Assets\Heads\HumanHead.png", "Assets\Heads\LizardHead.png", "Assets\Heads\MonkeyHead.png",
             "Assets\Heads\ToucanHead.png"]    # all the head assets are stored in an array
    wings = ["Assets\Wings\BatWing.png", "Assets\Wings\ParrotWing.png", "Assets\Wings\ToucanWing.png"]
    # all the wing assets are stored in an array
    arms = ["Assets\Arms\HumanArm.png", "Assets\Arms\LizardArm.png", "Assets\Arms\LobsterArm.png",
            "Assets\Arms\MonkeyArm.png"]    # all the arm assets are stored in an array
    torsos = ["Assets\Torsos\HumanTorso.png", "Assets\Torsos\LizardTorso.png", "Assets\Torsos\MonkeyTorso.png",
              "Assets\Torsos\ToucanTorso.png"]    # all the torso assets are stored in an array
    legs = ["Assets\Legs\HumanLeg.png", "Assets\Legs\LizardLeg.png", "Assets\Legs\MonkeyLeg.png",
            "Assets\Legs\ToucanLeg.png"]    # all the leg assets are stored in an array
    monster_parts = heads + wings + arms + torsos + legs # all arrays are combined into one large array
    return monster_parts  # this array it returned to the main program


def random_number_generator():  # this function generates random numbers
    head = random.randint (0, 3)
    wing = random.randint(4, 6)
    arm = random.randint(7, 10)
    torso = random.randint(11, 14)
    leg = random.randint(15, 18)
    random_numbers = [head, wing, arm, torso, leg]
    return random_numbers  # the random numbers are put into an array then returned to the main program


def print_monster(monster, number):  # this function loads all the assets for the monster into pygame and lines them up
    head, wing, arm, torso, leg = number[0], number[1], number[2], number[3], number[4]
    main_window.blit(pygame.image.load(monster[wing]), (60, 30))  # loads the wings
    main_window.blit(pygame.image.load(monster[arm]), (20, 70))  # loads the left arm
    main_window.blit(pygame.image.load(monster[leg]), (25, 120))  # loads the left leg
    main_window.blit(pygame.image.load(monster[torso]), (25, 60))  # loads the torso
    main_window.blit(pygame.image.load(monster[leg]), (55, 120))  # loads the right leg
    main_window.blit(pygame.image.load(monster[arm]), (55, 70))  # loads the right arm
    main_window.blit(pygame.image.load(monster[head]), (0, 40))  # loads the head


def keep_monster():  # this function allows the user to keep their monster or get a new one
    loop, running = True, True
    while loop == True:  # makes the function loop if the player does not input yes or no
        keep = input("Do you want to keep the current monster?")
        if keep == "yes":  # ask the user if they want to keep the generated monster
            print('Your monster has been saved as "Monster.png"')
            pygame.image.save(main_window, "Monster.png")  # saves the monster as a png file
            input("Press enter to end the program")
            running = False
            loop = False
        elif keep == "no":
            print("Loading next monster")
            loop = False  # ends the function and starts the generation of a new monster
        else:
            print('Please enter "yes" or "no"')
    return running

# the below code is the main program
pygame.init()
main_window = pygame.display.set_mode((150, 220))  # declares the size of the window
running = True

monster_parts = load_assets()  # loads the assets
# basic pygame set up to keep the window up
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_window.fill((255, 255, 255))
    random_numbers = random_number_generator()  # generates the random numbers
    print_monster(monster_parts, random_numbers)  # prints the monster to the pygame window
    pygame.display.update()  # updates the window with the new monster
    running = keep_monster()  # ask user if they want to keep the monster

pygame.quit()
