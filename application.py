import pygame as pg
from settings import *
from board import *
from player import *
import logging


class Application:
    def __init__(self):
        logging.info("Create instance of Application class")
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.running = True
        # create instance of Board
        self.board = Board(self)
        # create instance of Player
        self.player1 = Player(self)
        self.player2 = Player(self)

    def run(self):
        while self.running:
            events = pg.event.get()
            for event in events:
                self.player1.get_event(event)
                if event.type == pg.QUIT:
                    self.running = False

            self.screen.fill(BACKGROUND_COLOR)
            # main content of application
            self.draw()
            pg.display.flip()
            self.clock.tick(FPS)

        pg.quit()
    def draw(self):
        self.board.draw()
        self.player1.draw()

