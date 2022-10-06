import pygame as pg
import math as m
from settings import *

class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.game.player.angle - HALF_FOV + 0.0001 # according to the internet, the use of the +0.0001 or a very small number will ensure that there will be no division by zero.

        ### TRIGONOMETRY CALCULATIONS
           
        for ray in range(NUM_RAYS): 
            # VERTICAL LINES VALIDATION
            sin_a = m.sin(ray_angle)
            cos_a = m.cos(ray_angle)
            
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 0.000001, -1) # expansion of grid starts at top left corner so to check left tile, x_map pos has to be less than the tile itself or else it is just checking the same tile itself
            depth_vert = (x_vert - ox) / cos_a # trigonometry to validate first connection to verticle line
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break # hehehehar
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # HORIZONTAL LINES VALIDATION

            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 0.000001, -1)
            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break # hahahahaahaha
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # choosing depth

            if depth_vert < depth_hor: # because each point is on the lines of the grid and structures are made on grids, this checks which point is closer making sure of the distance between player and object for one ray
                real_depth = depth_vert
            else:
                real_depth = depth_hor
            
            

            # debugging

            #pg.draw.line(self.game.screen, 'yellow', (100 * ox, 100 * oy), 
                        #(100 * ox + 100 * real_depth * cos_a, 100 * oy + 100 * real_depth * sin_a), 2)

            # projection
            projection_height = SCREEN_DIST / (real_depth + 0.00001) # zero division error

            # displaying walls/structures
            pg.draw.rect(self.game.screen, 'white',
                        (ray * SCALE, HALF_HEIGHT - projection_height // 2, SCALE, projection_height))

            ray_angle += DELTA_ANGLE



    def update(self):
        self.ray_cast()