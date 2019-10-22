import noise
import numpy as np
import random
from scipy.misc.pilutil import toimage

user_input = int(input("What type of texture do you want to generate? Enter the corresponding number"
                       "\n 1. Wet Grass"
                       "\n 2. Snowy Grass"
                       "\n 3. Autumn Grass : "))

# This can be used to request a specific pattern -> base_input = int(input("Enter a number between 1 - 100 : "))


shape = (1024, 1024)    #This determines the size of the image that is output
scale = 50.0   #This determines the distances in which we view the noise map
octaves = 3 #This determines the level of detail of the noise map
persistence = 0.25 #This determines how much each of the octaves contributes to the shape
lacunarity = 1.0    #This determines how much detail is added and removed from each octave (adjusting the frequency)



world = np.zeros(shape)
pattern_number = random.randrange(1, 101)

for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise.pnoise2(i / scale,
                                    j / scale,
                                    octaves=octaves,
                                    persistence=persistence,
                                    lacunarity=lacunarity,
                                    repeatx=1024,
                                    repeaty=1024,
                                    base= pattern_number)

print(pattern_number)

def snowy_grass(world):

    green = [32, 105, 32]  # blue
    white = [244, 245, 244]  # green

    color_world = np.zeros(world.shape+(3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.25:
                color_world[i][j] = green

            elif world[i][j] < 1.0:
                color_world[i][j] = white

    return color_world

def wet_grass(world):

    blue = [65, 105, 225]  # blue
    green = [32, 105, 32]  # green

    color_world = np.zeros(world.shape+(3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.25:
                color_world[i][j] = blue

            elif world[i][j] < 1.0:
                color_world[i][j] = green

    return color_world


def autumn_grass(world):

    orange = [191, 123, 13]  # blue
    green = [120, 138, 51]  # green
    red = [150, 44, 12]  # red


    color_world = np.zeros(world.shape+(3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < -0.5:
                color_world[i][j] = orange

            elif world[i][j] > 0.35:
                color_world[i][j] = red

            elif world[i][j] < 1.0:
                color_world[i][j] = green

    return color_world


if user_input == 1:
    world_output = wet_grass(world)

elif user_input == 2:
    world_output = snowy_grass(world)

elif user_input == 3:
    world_output = autumn_grass(world)
else:
    print("Error, invalid input. Please try again")

toimage(world_output).show()