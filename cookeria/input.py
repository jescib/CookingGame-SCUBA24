import pygame
from food import Burger

class Input:
    def __init__(self, window, coordinates):
        self.window = window
        self.coordinates = coordinates
        self.burger_loaded = False

    def handle_app_run_events(self, event):
        if event.type == pygame.QUIT:
            return False
        return True
        
    def handle_input(self):
        app_continue_running = True
        burger_class = Burger(self.window, self.coordinates)  # Assuming Burger is the correct class
        for event in pygame.event.get():
            app_continue_running = self.handle_app_run_events(event)
            if event.type == pygame.KEYDOWN:
                if not self.burger_loaded:  # Assuming we load the kitchen once a burger is not loaded
                    self.burger_loaded = burger_class.draw_kitchen(self.window, event, (0, 0))
                *_,self.coordinates= burger_class.make_burger(self.window, event, self.coordinates)  # Making a burger regardless of the loaded state
                # Optionally handle the burger state here, if needed
        return app_continue_running