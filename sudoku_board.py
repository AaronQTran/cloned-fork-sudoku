from sudoku_cell import Cell
import sudoku_generator
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
        self.board, self.board_answer = sudoku_generator.generate_sudoku(9, self.difficulty)
        self.cell_board = []
        for i in range(9):
            new = []
            for j in  range(9):
                new.append(Cell(self.board[i][j],i,j,screen))
            self.cell_board.append(new)


    def draw(self):
        for i in range(0, len(self.board)+ 1):
            pygame.draw.line(self.screen, (0,0,0), (0, i * 60), (self.width, i * 60), 1)
        for i in range(0, len(self.board) + 1):
            pygame.draw.line(self.screen, (0,0,0), (i * 60, 0), (i * 60, self.height - 60), 1)
        for i in range(1, 4):
            pygame.draw.line(self.screen, (0,0,0), (0, i * 180), (self.width, i * 180), 4)
        for i in range(0, len(self.board) + 1):
            pygame.draw.line(self.screen, (0,0,0), (i * 180, 0), (i * 180, self.height - 60), 4)

    def select(self,row,col):
        pygame.draw.line(self.screen, ('red'), (col*60, row * 60), (col * 60, (row+1) * 60), 4)
        pygame.draw.line(self.screen, ('red'), (col*60, row * 60), ((col + 1) * 60, (row) * 60), 4)
        pygame.draw.line(self.screen, ('red'), ((col + 1) * 60, row * 60), ((col + 1)* 60, (row + 1) * 60), 4)
        pygame.draw.line(self.screen, ('red'), ((col ) * 60, (row + 1) * 60), ((col + 1) * 60, (row + 1) * 60), 4)
