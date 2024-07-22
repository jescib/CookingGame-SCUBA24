import pygame
from input import Input
from food import Burger


def main_func():

    #loading pygame
    pygame.init()
    window = pygame.display.set_mode((600,500))
    loading_image = pygame.image.load('images/logo.png')
    window.blit(loading_image,(0,0))
    pygame.display.update()
    input_handler = Input(window, (120,400))
    burger_class = Burger(window,(120,400))
    
    app_is_running = True
    # main game loop
    while app_is_running == True:
        app_is_running = input_handler.handle_input()
        pygame.display.update()
        
        
main_func()

