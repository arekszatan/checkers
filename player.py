import pygame as pg
from settings import *
import logging
import math

class Player:
    def __init__(self, app, player_num, col, row):
        logging.info("Create instance of Player class")
        self.app = app
        self.screen = pg.display.get_surface()
        self.player_num = player_num
        if self.player_num == 1:
            self.position = self.position_x, self.position_y = (50 + col * 100, 50 + row * 100)
            self.player_color = "red"
        elif self.player_num == 2:
            self.position = self.position_x, self.position_y = (50 + col * 100, 750 - row * 100)
            self.player_color = "yellow"
        self.is_grabbed = False
        self.row = -1
        self.col = -1


    def draw(self):
        pg.draw.circle(self.screen, self.player_color, self.position, PLAYER_SIZE)

    def get_event(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            distance = math.sqrt((mouse_x - self.position_x) ** 2 + (mouse_y - self.position_y) ** 2)
            if distance <= PLAYER_SIZE:
                self.is_grabbed = True
        elif event.type == pg.MOUSEBUTTONUP:
            self.is_grabbed = False
        self.set_grab()

    def set_grab(self):
        if self.is_grabbed:
            self.player_color = "green"
            self.position = self.position_x, self.position_y = pg.mouse.get_pos()
        else:
            if self.player_num == 1:
                self.player_color = "red"
            elif self.player_num == 2:
                self.player_color = "yellow"

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col