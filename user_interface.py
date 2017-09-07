# this will also need these imports

import pygame
import os
import constants

class UserInterface():
    """ UI super class"""
    def __init__(self):
        """ UI initializer"""
    
        #set up mouse input
        self.mouse_x = 0
        self.mouse_y = 0
        #set up previous mouse coords for cover-up
        self.cover_coord_x = 0
        self.cover_coord_y = 0
        
        # which cursor sprite?
        self.cursor_sprite = None
        
        # Set up sprite surface attr
        self.bun_full = None
        self.cursor_land = None
        self.cursor_water = None
        self.land_tile = None
        self.shore_layer_corner = None
        self.shore_layer_corner_isthmus = None
        self.shore_layer_corner_water_fill = None
        self.shore_layer_full = None
        self.water_tile = None
        
        # static var for next
        self.png_list = []
        
        # populate previous with pngs in game dir
        with os.scandir('.') as dir_list:
            for entry in dir_list:
                if entry.name[-3:] == "png":
                    self.png_list.append(entry.name)
        
        # set files to appropriate surfaces
        for file in self.png_list:
            setattr(self, file[:-4], pygame.image.load(file).convert_alpha())
        
        # some terrain grid specific variables
        self.grid_origin = [0, 0]
        self.grid_x = int(1200 / 30)
        self.grid_y = int(900 / 30)
        self.terrain_grid = []
        self.whole_map_blitted = False

        # populate terrain_grid
        for row in range(self.grid_y):
            self.terrain_grid.append([])
        
        for row in range(self.grid_y):
            for column in range(self.grid_x):
                self.terrain_grid[row].append(0)                
    
    def set_cursor_sprite(self, screen, cursor):
        """ display sprite stored in cursor_sprite"""
        
        # set cursor sprite to argument
        self.cursor_sprite = cursor
        
        # if no sprite, set default mouse visible
        if self.cursor_sprite == None:
            pygame.mouse.set_visible(True)
        # else display sprite and hide default cursor
        else:
            pygame.mouse.set_visible(False)
            
            box = []
    
            for x in range(2):
                for y in range(2):
                    box.append([self.cover_coord_x // 30 + x, self.cover_coord_y // 30 + y])
                    
            for item in box:
                row = item[1]
                column = item[0]
                
                if row > 29:
                    row = 0
                if column > 39:
                    column = 0
                
                if self.terrain_grid[row][column] == 0:
                    screen.blit(self.land_tile, 
                                [column * 30 + self.grid_origin[0], 
                                 row * 30 + self.grid_origin[1]])
                    self.shore_blitter(screen, [row, column])
                elif self.terrain_grid[row][column] == 1:
                    screen.blit(self.water_tile, 
                                [column * 30 + self.grid_origin[0], 
                                 row * 30 + self.grid_origin[1]])            
            
            screen.blit(self.cursor_sprite, [self.mouse_x, self.mouse_y])
            
            # set cover-up coords as previous mouse coords
            self.cover_coord_x = self.mouse_x
            self.cover_coord_y = self.mouse_y
    
    def shore_blitter(self, screen, grid_coord):
        """ take grid coordinate and return proper shore line attr """
        # get type (water = True) for surrounding tiles and assign to tile adjacency
        one = False
        two = False
        three = False
        four = False
        five = False
        six = False
        seven = False
        eight = False
        
        # get size for wraparound adjustment
        size = [1200, 900]
        column_total = size[0] / 30
        row_total = size[1] / 30
        
        #wraparround adjustment
        if grid_coord[0] == row_total - 1:
            grid_coord[0] = -1
        if grid_coord[1] == column_total - 1:
            grid_coord[1] = -1
        
        # get water values of adjacent tiles
        if self.terrain_grid[grid_coord[0]][grid_coord[1] - 1] == 1:
            one = True
        if self.terrain_grid[grid_coord[0] + 1][grid_coord[1] - 1] == 1:
            two = True
        if self.terrain_grid[grid_coord[0] + 1][grid_coord[1]] == 1:
            three = True
        if self.terrain_grid[grid_coord[0] + 1][grid_coord[1] + 1] == 1:
            four = True
        if self.terrain_grid[grid_coord[0]][grid_coord[1] + 1] == 1:
            five = True
        if self.terrain_grid[grid_coord[0] - 1][grid_coord[1] + 1] == 1:
            six = True
        if self.terrain_grid[grid_coord[0] - 1][grid_coord[1]] == 1:
            seven = True
        if self.terrain_grid[grid_coord[0] - 1][grid_coord[1] - 1] == 1:
            eight = True
        
        # layer on each long side
        if one:
            screen.blit(self.shore_layer_full, 
                        [grid_coord[0], grid_coord[1]])
        if three:
            screen.blit(self.shore_layer_full.transform.rotate(-90),
                        [grid_coord[0], grid_coord[1]])
        if five:
            screen.blit(self.shore_layer_full.transform.rotate(180),
                        [grid_coord[0], grid_coord[1]])
        if seven:
            screen.blit(self.shore_layer_full.transform.rotate(90),
                        [grid_coord[0], grid_coord[1]])            
        
        # layer on each corner if applicable
        if two and not (one and three):
            screen.blit(self.shore_layer_corner, 
                        [grid_coord[0], grid_coord[1]])
        if four and not (three and five):
            screen.blit(self.shore_layer_corner.transform.rotate(-90), 
                        [grid_coord[0], grid_coord[1]])
        if six and not (five and seven):
            screen.blit(self.shore_layer_corner.transform.rotate(180), 
                        [grid_coord[0], grid_coord[1]])
        if eight and not (one and seven):
            screen.blit(self.shore_layer_corner.transform.rotate(90), 
                        [grid_coord[0], grid_coord[1]])
            
        # waterrrrrr cornerrrrrs, son!
        if one and two and three:
            screen.blit(self.shore_layer_corner_water_fill, 
                        [grid_coord[0], grid_coord[1]])
        if three and four and five:
            screen.blit(self.shore_layer_corner_water_fill.transform.rotate(-90), 
                        [grid_coord[0], grid_coord[1]])
        if five and six and seven:
            screen.blit(self.shore_layer_corner_water_fill.transform.rotate(180), 
                        [grid_coord[0], grid_coord[1]])            
        if seven and eight and one:
            screen.blit(self.shore_layer_corner_water_fill.transform.rotate(90), 
                        [grid_coord[0], grid_coord[1]])
            
        # the isthmus bitches here to rock your goddamn world
        if (one and three) and not two:
            screen.blit(self.shore_layer_corner_isthmus, 
                        [grid_coord[0], grid_coord[1]])
        if (three and five) and not four:
            screen.blit(self.shore_layer_corner_isthmus.transform.rotate(-90), 
                        [grid_coord[0], grid_coord[1]])
        if (five and seven) and not six:
            screen.blit(self.shore_layer_corner_isthmus.transform.rotate(180), 
                        [grid_coord[0], grid_coord[1]])
        if (seven and one) and not eight:
            screen.blit(self.shore_layer_corner_isthmus.transform.rotate(90), 
                        [grid_coord[0], grid_coord[1]])            
            
    def draw_whole_terrain_grid(self, screen):
        """ draws the entire terrain grid to screen """
        for row in range(len(self.terrain_grid)):
            for column in range(len(self.terrain_grid[0])):
                # 0;land, 1:water
                if self.terrain_grid[row][column] == 0:
                    screen.blit(self.land_tile, 
                                [column * 30 + self.grid_origin[0], 
                                 row * 30 + self.grid_origin[1]])
                    self.shore_blitter(screen, [row, column])
                elif self.terrain_grid[row][column] == 1:
                    screen.blit(self.water_tile, 
                                [column * 30 + self.grid_origin[0], 
                                 row * 30 + self.grid_origin[1]])
        # tell class the method has been called
        self.whole_map_blitted = True
    
    def draw_changed_tiles(self, screen):
        """ draws tiles that have been changed including those under the cursor"""
        pass