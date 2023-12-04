from sudoku_cell import Cell as ce
import sudoku_generator as sg
import pygame


class Board:
    def __init__(self, screen, diffuculty):
        self.width = 540
        self.height = 600
        self.screen = screen
        if diffuculty == 'easy':
            self.difficulty = 30
        elif diffuculty == 'medium':
            self.difficulty = 40
        elif diffuculty == 'hard':
            self.difficulty = 50
        self.board = sg.generate_sudoku(9, self.difficulty)

    def draw(self):
        for i in range(0, len(self.board)+ 1):
            pygame.draw.line(self.screen, (0,0,0), (0, i * 60), (self.width, i * 60), 1)
        for i in range(0, len(self.board) + 1):
            pygame.draw.line(self.screen, (0,0,0), (i * 60, 0), (i * 60, self.height - 60), 1)
        for i in range(1, 4):
            pygame.draw.line(self.screen, (0,0,0), (0, i * 180), (self.width, i * 180), 4)
        for i in range(0, len(self.board) + 1):
            pygame.draw.line(self.screen, (0,0,0), (i * 180, 0), (i * 180, self.height - 60), 4)
