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
    # initialize pygame
    pygame.init()
 
    # Set the width and height of the screen [width,height]
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Happy Save The Bunny Game")
 
    # Loop until the user clicks the close button.
    done = False
 
    # used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    # Build game object
    test_game = game.Game()
    
    # set up FPS display
    pygame.font.init()
    myfont = pygame.font.SysFont('Calibri', 30)
    
    # -------- Main Program Loop -----------
    while not done:
        # event processing
        done = test_game.process_events()
        
        # Game logic
        test_game.run_logic()
        
        # Draw the frame
        test_game.display_frame(screen)
        
        # draw current FPS
        current_fps = myfont.render(str(clock.get_fps()), False, constants.BLACK)
        screen.blit(current_fps, (0,0))
        pygame.display.flip()
 
        # Limit to 60 frames per second
        clock.tick(60)
 
    # Close the window and quit.
    pygame.quit()
 
if __name__ == "__main__":
    main()