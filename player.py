
from settings import *
import pygame as pg
import math as m

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self): # movement using sin and cos method (online research still unsure)
        sin_a = m.sin(self.angle) # sin affects y axis
        cos_a = m.cos(self.angle) # cos affects x axis
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time # correlating speed of player with frame rate incase it drops and possibly future npcs with the framerate
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        
        keys = pg.key.get_pressed()
        if keys[pg.K_w]: # uses trigonometry to calculate angle
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx -= speed_cos
            dy -= speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy -= speed_cos
        if keys[pg.K_d]:
            dx -= speed_sin
            dy += speed_cos


        self.check_wall_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= m.tau # 2pi = 360 degrees

    def check_wall(self, x, y): # check for object
        if (x, y) not in self.game.map.world_map:
            return True

    def check_wall_collision(self, dx, dy): # check for collision
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy


    #def draw(self):
        #pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y *100), 
        #            (self.x * 100 + WIDTH * m.cos(self.angle),
        #            self.y * 100 + WIDTH * m.sin(self.angle)), 2)
        #pg.draw.circle(self.game.screen, 'lightblue', (self.x * 100, self.y * 100), 15)


    # note for myself: the enlarged grid and player position is just an illusion to make the grid larger, all enlarged by 100x (can be changed but make sure it is equal to grid size)


    def update(self):
        self.movement()


    @property # special function used to retrieve a private attributed value without the use of getters. In this case, is used to be called to find the location of player more easily
    def map_pos(self):
        return int(self.x), int(self.y)


    

