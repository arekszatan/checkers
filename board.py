import pygame as pg
from settings import *
import logging

class Board:
    def __init__(self, app):
        logging.info("Create instance of Board class")
        self.app = app
        self.screen = pg.display.get_surface()


    def draw(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    pg.draw.rect(self.screen, 'white', (i * WIDTH / 8, j * HEIGHT / 8, WIDTH / 8, HEIGHT / 8))
                else:
                    pg.draw.rect(self.screen, 'black', (i * WIDTH / 8, j * HEIGHT / 8, WIDTH / 8, HEIGHT / 8))

    def get_board(self):
        return