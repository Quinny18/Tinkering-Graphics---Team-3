import math
import random
import pygame


def define_colours():  # defines some colours used in the assets
    green = (173, 243, 77)
    gray = (211, 211, 211)
    red = (204, 27, 0)
    beige = (250, 221, 182)
    lower_green = (173, 125, 77)
    lower_gray = (161, 161, 161)
    lower_red = (154, 27, 0)
    lower_beige = (230, 201, 162)
    colours = [green, gray, red, beige]  # puts the colours into an array
    lighter_colours = [lower_green, lower_gray, lower_red, lower_beige]  # puts the light colours into an array
    return colours, lighter_colours  # returns the light and normal colour arrays


def pick_colour():  # allows the user to pick what colours will be changed
    loop = False
    while loop == False:
        print("Pick the colour you want to remove and then the colour you want to replace it with")
        remove_colour = str(input("1)Green\n2)Gray\n3)Red\n4)Beige\n"))
        replace_colour = str(input("1)Green\n2)Gray\n3)Red\n4)Beige\n"))
        if remove_colour == "1" or remove_colour == "2" or remove_colour == "3" or remove_colour == "4":
        # checks to make sure user has entered 1,2,3 or 4 for the first number
            if replace_colour == "1" or replace_colour == "2" or replace_colour == "3" or replace_colour == "4":
            # checks to make sure user has entered 1,2,3 or 4 for the second number
                if replace_colour == remove_colour:
                # checks to make sure the user has not picked the two same colours
                    print("Can't Have Two Colours Be The Same")
                else:
                    # convertes the user input to integers so they can be used in the colour array
                    remove_colour = int(remove_colour) - 1
                    replace_colour = int(remove_colour) - 1
                    loop = True
        else:
            print("Please Enter 1,2,3 or 4")
    return remove_colour, replace_colour  # returns the numbers to the main program


def colour_distance(colour1, colour2):  # checks how similar two colours are
    answer = math.sqrt((colour1[0] - colour2[0]) ** 2 + (colour1[1] - colour2[1]) ** 2 + (colour1[2] - colour2[2]) ** 2)
    return answer  # returns the answer


def unshade(colour1, colour2, tolerance, surface=pygame.Surface((1, 1))):
# takes a colour and converts all similar shades to the same colour
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        # loops through all x values
        for y in range(surface.get_width()):
            # loops through all y values
            pixel = surface.get_at((x, y))  # gets the location of the pixel
            if colour_distance(colour1, colour2) < tolerance:
                # changes colour if it is similar to the selected colour
                surface.set_at((x, y), pygame.Color(211, 211, 211))



def colour_to_colour(colours, remove_colour, replace_colour, surface=pygame.Surface((1, 1))):
# change one colour to another
    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        # loops through all x values
        for y in range(surface.get_width()):
            # loops through all y values
            pixel = surface.get_at((x, y))
            if pixel == colours[remove_colour]:
                # checks to find any colour that will be removed
                surface.set_at((x, y), colours[replace_colour])
                # sets the pixel to the new colour
    print("""Recolouring Monster
...
Recolouring Finished
""")


pygame.init()
main_window = pygame.display.set_mode((150, 220))  # sets the size of the pygame window
running = True

# imports the monster from contract 3
image = pygame.image.load("Monster.png")

colours, lighter_colours = define_colours()  # defines all the colours that can be changed
remove_colour, replace_colour = pick_colour()  # lets user pick the colours they want to change
unshade(colours[remove_colour], lighter_colours[remove_colour], 100, image)
# takes the selected colour that will be removed and turns all similar shades to the same colour
colour_to_colour(colours, remove_colour, replace_colour, image)  # replaces the old colour with the new colour

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_window.fill((255, 255, 255))  # fills the back ground of the pygame window as white
    main_window.blit(image, (0, 0))
    pygame.display.update()  # updates the pygame window

    # save the new image as a png
    pygame.image.save(main_window, "Monster.png")
pygame.quit()
