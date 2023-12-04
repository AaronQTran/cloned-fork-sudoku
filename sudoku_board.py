from sudoku_cell import Cell as ce
import sudoku_generator as sg
import pygame


class Board:
    def __init__(self, width, height, screen, diffuculty):
        self.width = 9
        self.height = 9
        self.screen = screen
        if diffuculty == 'easy':
            self.difficulty = 30
        elif diffuculty == 'medium':
            self.difficulty = 30
        elif diffuculty == 'hard':
            self.difficulty = 30
        self.board = sg.generate_sudoku(9, self.difficulty)

    def draw(self):
        pass