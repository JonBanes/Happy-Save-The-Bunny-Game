import pygame
import random
import constants
import user_interface

class Game():
    """ represents an instance of the game, can reset game w/ new instance 
    of the Game class """
    def __init__(self):
        """ Constructor, attr and initialize game """
        self.session_seed = random.random()
        self.mouse_button_pressed = False
        self.mouse_pos_x = 0
        self.mouse_pos_y = 0
        
        #set up UI object
        self.test_screen = user_interface.UserInterface()
        
    def process_events(self):
        """ process pygame's event queue, return true if window is closed"""
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_pressed = True
        
        # get the mouse position for object
        self.test_screen.mouse_x = pygame.mouse.get_pos()[0]
        self.test_screen.mouse_y = pygame.mouse.get_pos()[1]        
        
        return False
    
    def run_logic(self):
        """ This method is run once a tick and contains all the game logic """
        if self.mouse_button_pressed:
            grid_column = self.test_screen.mouse_x // 30
            grid_row = self.test_screen.mouse_y // 30
            
            self.test_screen.terrain_grid[grid_row][grid_column] = 1
            
            self.mouse_button_pressed = False
    
    def display_frame(self, screen):
        """ this draws the frame once a tick """
        
        
        
        # draw tiles
        if self.test_screen.whole_map_blitted == False:
            self.test_screen.draw_whole_terrain_grid(screen)
            
        # draw cursor
        self.test_screen.set_cursor_sprite(screen, self.test_screen.cursor_water)
        
        # flip to screen
        pygame.display.flip()