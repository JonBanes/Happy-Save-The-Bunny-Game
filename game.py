import pygame
import constants
import user_interface

class Game():
    """ represents an instance of the game, can reset game w/ new instance 
    of the Game class """
    def __init__(self):
        """ Constructor, attr and initialize game """
        
    def process_events(self):
        """ process pygame's event queue, return true if window is closed"""
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        
        return False
    
    def run_logic(self):
        """ This method is run once a tick and contains all the game logic """
        pass
    
    def display_frame(self, screen):
        """ this draws the frame once a tick """
        test_screen = user_interface.UserInterface()
        
        # get the mouse position for object
        test_screen.mouse_x = pygame.mouse.get_pos()[0]
        test_screen.mouse_y = pygame.mouse.get_pos()[1]
        
        # draw tiles
        if test_screen.whole_map_blitted == False:
            test_screen.draw_whole_terrain_grid(screen)
            
        # draw cursor
        test_screen.set_cursor_sprite(screen, test_screen.cursor_land)
        
        # flip to screen
        pygame.display.flip()