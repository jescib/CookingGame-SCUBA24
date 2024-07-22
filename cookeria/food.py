import pygame


class Burger():
    def __init__(self, window, coordinates):
        self.window = window
        self.coordinates = coordinates
        self.burger_state = [] #empty list to add burger ingredients

        #scenes
        self.kitchen = pygame.image.load('images/kitchen.png')
        self.checkout = pygame.image.load('images/checkout.png')

        #burger images
        self.bottom = pygame.image.load('images/burger/bottom_bun.png')
        self.cheese = pygame.image.load('images/burger/cheese.png')
        self.lettuce = pygame.image.load('images/burger/lettuce.png')   
        self.patty = pygame.image.load('images/burger/patty.png')  
        self.tomato = pygame.image.load('images/burger/tomato.png')
        self.top = pygame.image.load('images/burger/top_bun.png')


    #give it the window you're on and where to add the pizza
    #this will come from main most likely

    def draw_kitchen(self,window,event,coordinates):
        if event.key == pygame.K_s:
            window.fill((255,255,255))
            print(coordinates)
            window.blit(self.kitchen,coordinates) 
            return True
        else:
            return False
    
    def make_burger(self, window, event, coordinates):
        ingredient_added = False

        if event.key == pygame.K_b:
            window.fill((255, 255, 255))
            window.blit(self.kitchen, (0, 0))
            window.blit(self.bottom, coordinates)
            self.burger_state.append('bottom')
            ingredient_added = True
            return ingredient_added,coordinates
        elif event.key == pygame.K_c:
            coordinates = (coordinates[0], coordinates[1] - 20)
            window.blit(self.cheese, coordinates)
            self.burger_state.append('cheese')
            ingredient_added = True
            return ingredient_added,coordinates
        elif event.key == pygame.K_l:
            coordinates = (coordinates[0], coordinates[1] - 20)
            window.blit(self.lettuce, coordinates)
            self.burger_state.append('lettuce')
            ingredient_added = True
            return ingredient_added,coordinates
        elif event.key == pygame.K_p:
            coordinates = (coordinates[0], coordinates[1] - 20)
            window.blit(self.patty, coordinates)
            self.burger_state.append('patty')
            ingredient_added = True
            return ingredient_added,coordinates
        elif event.key == pygame.K_t:
            coordinates = (coordinates[0], coordinates[1] - 20)
            window.blit(self.tomato, coordinates)
            self.burger_state.append('tomato')
            ingredient_added = True
            return ingredient_added,coordinates
        elif event.key == pygame.K_u:
            coordinates = (coordinates[0], coordinates[1] - 50)
            window.blit(self.top, coordinates)
            self.burger_state.append('top')
            ingredient_added = True  # Assuming this is the final step to complete the burger
            return ingredient_added,coordinates
        elif event.key == pygame.K_r: 
            self.burger_state.clear()  # Reset the burger state
            return False  # Return False to indicate no ingredient was added, but a reset occurred

        if ingredient_added:
            return ingredient_added,coordinates  # Return True if an ingredient was added
        else:
            return ingredient_added,coordinates  # Return False if no ingredient was added and no reset occurred

        


