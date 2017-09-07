# import all the stuff 
# pygame module
import pygame
# for all the random stuff
import random
# file/directory manipulation
import os

# personal libraries
import constants
import user_interface
import game
    
def main():
    """ Main function for the game. """
    pygame.init()
 
    # Set the width and height of the screen [width,height]
    size = [1200, 900]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("My Game")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # Build UI objects
    test_screen = user_interface.UserInterface()
    
    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
        
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
 
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        
        # get the mouse position in the loop
        test_screen.mouse_x = pygame.mouse.get_pos()[0]
        test_screen.mouse_y = pygame.mouse.get_pos()[1]
        
        if test_screen.whole_map_blitted == False:
            test_screen.draw_whole_terrain_grid(screen)
            
        #test_screen.draw_changed_tiles(screen)
        
        test_screen.set_cursor_sprite(screen)
        test_screen.cursor_sprite = test_screen.cursor_land
        
        
        
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
        # Limit to 60 frames per second
        clock.tick(60)
 
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
 
if __name__ == "__main__":
    main()