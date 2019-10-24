import pygame
import time


def blindness(my_surface):  # this array allows the user to pick what view they want to use
    list_of_views = [1, 1, 1, 0.5, 0.5, 1, 0.5, 0.2, 1, 1, 0.2, 0.5]
    while True:  # loops until the user has given a valid input
        answer = int(input("What type of texture do you want to generate? Enter the corresponding number"
                           "\n 1) Normal: \n 2) Protanopia:"
                           "\n 3) Deuteranopia: \n 4) Tritanopia: "
                           "\n Enter Here:"))
        # prints the options the user can use
        if answer == 1:
            array_colour = 0  # sets the correct position in the array
            change_view(my_surface, array_colour, list_of_views)
            break  # ends the loop and the function
        elif answer == 2:
            array_colour = 3  # sets the correct position in the array
            change_view(my_surface, array_colour, list_of_views)
            break  # ends the loop and the function
        elif answer == 3:
            array_colour = 6  # sets the correct position in the array
            change_view(my_surface, array_colour, list_of_views)
            break  # ends the loop and the function
        elif answer == 4:
            array_colour = 9  # sets the correct position in the array
            change_view(my_surface, array_colour, list_of_views)
            break  # ends the loop and the function
        else:  # loops back to the beginning if the user gives a invalid input
            print("Please Enter 1,2,3 or 4")  # tells the user the valid inputs
    return my_surface  # returns the image back to the main program


def change_view(picture, array_colour, list_of_views):  # Declaring the function and passing variables
    pixel = pygame.Color(0, 0, 0)
    for a in range(picture.get_width()):  # Will go through all of the pixels in the x and y axis
        for b in range(picture.get_height()):
            pixel = picture.get_at((a, b))  #
            picture.set_at((a, b), pygame.Color(int(pixel.r * list_of_views[array_colour]),
                                                int(pixel.g * list_of_views[array_colour+1]),
                                                int(pixel.b * list_of_views[array_colour+2])))
            # Changing the values of the red,green and blue in the picture depending on what is being input by the user
            # at any location in the picture
    return my_surface


pygame.init()
main_window = pygame.display.set_mode((800, 600))  # Creates a window, 800 pixels by 600 pixels
my_surface = pygame.image.load('test.png').convert()  # Converting the picture to the window
blindness(my_surface)

running = True  # The game will run until it is turned off
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_window.fill((255, 255, 255))  # Makes the window white
    main_window.blit(my_surface, (0, 0))  # Puts the picture in the top left corner of the window
    pygame.display.update()
    print("Converted Image")
    time.sleep(10)  # Stops the program after 10 after seconds
    running = False
pygame.quit()  # Will close pygame