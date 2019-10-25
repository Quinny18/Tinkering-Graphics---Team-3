import noise
import numpy as np
import random
from scipy.misc.pilutil import toimage

# Gathering user inputs on what type of tile they want
user_input = int(input("What type of texture do you want to generate? Enter the corresponding number"
                       "\n 1. Wet Grass"
                       "\n 2. Snowy Grass"
                       "\n 3. Autumn Grass : "))

# This can be used to request a specific pattern -> base_input = int(input("Enter a number between 1 - 100 : "))


shape = (1024, 1024)  # This determines the size of the image that is output
scale = 50.0  # This determines the distances in which we view the noise map
octaves = 3  # This determines the level of detail of the noise map
persistence = 0.25  # This determines how much each of the octaves contributes to the shape
lacunarity = 1.0  # This determines how much detail is added and removed from each octave (adjusting the frequency)

world = np.zeros(shape)  # returns a new array of the shape or size initialised in the shape variable
pattern_number = random.randrange(1, 101)

for i in range(shape[0]):  # from the first element of shape[0] to the last
    for j in range(shape[1]):  # from the first element of shape[1] to the last
        world[i][j] = noise.pnoise2(i / scale,  # pnoise is a periodic noise function
                                    j / scale,
                                    octaves=octaves,
                                    persistence=persistence,
                                    lacunarity=lacunarity,
                                    repeatx=1024,
                                    repeaty=1024,
                                    base=pattern_number)

# Tutorial used to create Perlin Noise Map:
# https://medium.com/@yvanscher/playing-with-perlin-noise-generating-realistic-archipelagos-b59f004d8401

print("Pattern Number : ", pattern_number)  # This just displays the pattern used each run, they range from, and include 1 - 100


def snowy_grass(world):  # This function is run when the user inputs that they want to generate a snowy grass tile
    green = [32, 105, 32]  # The colours that will be used on the tiles
    white = [244, 245, 244]

    color_world = np.zeros(world.shape + (3,))  # world.shape is used to return the shape of the array
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.25:  # Sets all of the areas of the noise map that are less than -0.25 to green
                color_world[i][j] = green

            elif world[i][j] < 1.0:
                color_world[i][j] = white  # Sets all of the areas of the noise map that are less than 1 to white

    return color_world


def wet_grass(world):
    blue = [65, 105, 225]  # The colours that will be used on the tiles
    green = [32, 105, 32]

    color_world = np.zeros(world.shape + (3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.25:
                color_world[i][j] = blue # Sets all of the areas of the noise map that are less than -0.25 to blue

            elif world[i][j] < 1.0:
                color_world[i][j] = green # Sets all of the areas of the noise map that are less than-0.25 to green

    return color_world


def autumn_grass(world):
    orange = [191, 123, 13]  # The colours that will be used on the tiles
    green = [120, 138, 51]
    red = [150, 44, 12]

    color_world = np.zeros(world.shape + (3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.5:
                color_world[i][j] = orange # Sets all of the areas of the noise map that are less than -0.5 to orange

            elif world[i][j] > 0.35:
                color_world[i][j] = red # Sets all of the areas of the noise map that are greater than -0.35 to red

            elif world[i][j] < 1.0:
                color_world[i][j] = green # Sets all of the areas of the noise map that are less than 1 to green

    return color_world


if user_input == 1:                     # This gathers the user input for what type of tile they want
    world_output = wet_grass(world)

elif user_input == 2:
    world_output = snowy_grass(world)

elif user_input == 3:
    world_output = autumn_grass(world)
else:
    print("Error, invalid input. Please try again") # This is some basic input validation

toimage(world_output).show() # This opens the image file once it has been generated
