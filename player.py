import pygame as pg
from settings import *
import logging

class Player:
    def __init__(self, app):
        logging.info("Create instance of Player class")
        self.app = app
        self.screen = pg.display.get_surface()
        self.position = self.position_x, self.position_y = (0, 0)

    def draw(self):
        pg.draw.circle(self.screen, "yellow", self.position, PLAYER_SIZE)

    def get_event(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            distance_square_between_mouse_and_circle = (mouse_x - self.position_x) ** 2 + (mouse_y - self.position_y) ** 2
            if event.button == 1 and distance_square_between_mouse_and_circle < PLAYER_SIZE**2:
                self.position = (mouse_x, mouse_y)
                print(self.position)

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position