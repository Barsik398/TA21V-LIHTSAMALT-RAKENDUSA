import random
from playsound import playsound
import pygame
import sys
import random as r

def run():

    pygame.init()
    screen = pygame.display.set_mode((1024,672))
    pygame.display.set_caption('pygame3')
    bg_color = (0, 0, 0)
    image = pygame.image.load('deagle1.jpg')
    screen.blit(image, (100, 100))
    pygame.display.flip()



    while True:
        r_number = random.randint(0, 6)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and r_number == 1:
                    print("loser you die")
                    playsound('shoot.mp3')
                    sys.exit()
                else:
                    print("win")

run()
