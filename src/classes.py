#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import utils
from tkinter import *
       

class Square():
    """ A square of the game """

    def __init__(self):
        self.is_bomb = False
        self.revealed = False
        self.number = 0

    def left_click(self):
        self.revealed = True
        return (self.is_bomb, self.number)


class Grid:
    """ A grid of the game, containing Squares """

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.bombs = 0
        self.squares = list()

        # create a list of list of Squares
        # -------->
        # |       y
        # |
        # V x
        for i in range(height):
            tmp = list()
            for j in range(width):
                sq = Square()
                tmp.append(sq)
            self.squares.append(tmp)



    def add_bombs(self, bombs):
        if bombs <= 0 or bombs >= self.width * self.height:
            raise Exception("Invalid number of bombs.")
        else:
            self.bombs = bombs
            # sample makes random choices with distinct elements
            # we don't want several bombs on the same square
            pos = random.sample([(x, y) 
                for x in range(self.height) 
                for y in range (self.width)], bombs)

            for (i, j) in pos:
                self.squares[i][j].is_bomb = True
                for (x, y) in utils.neighbours(i, j, self.height, self.width):
                    self.squares[x][y].number += 1



    def __str__(self):
        res = ""
        for i in range(self.height):
            for j in range(self.width):
                if self.squares[i][j].is_bomb:
                    res += "."
                else:
                    res += str(self.squares[i][j].number)
            res += "\n"
        return res


