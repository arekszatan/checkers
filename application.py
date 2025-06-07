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
        self.player1 = []
        self.player2 = []
        self.new_game()

    def new_game(self):
        self.player1 = []
        self.player2 = []
        for i in range(8):
            for j in range(3):
                self.player1.append(Player(self,1, i, j))
                self.player2.append(Player(self, 2, i, j))

    def run(self):
        while self.running:
            events = pg.event.get()
            for event in events:
                for pawn in self.player1:
                    pawn.get_event(event)
                for pawn in self.player2:
                    pawn.get_event(event)
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
        for pawn in self.player1:
            pawn.draw()
        for pawn in self.player2:
            pawn.draw()
        # self.player1.draw()

