from sudoku_cell import Cell
import sudoku_generator
import pygame


class Board:
    selected = False
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
        self.board, self.board_answer, self.og_board = sudoku_generator.generate_sudoku(9, self.difficulty)
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
        pygame.draw.line(self.screen, ('red'), (col*60, row * 60), (col * 60, (row+1) * 60), 1)
        pygame.draw.line(self.screen, ('red'), (col*60, row * 60), ((col + 1) * 60, (row) * 60), 1)
        pygame.draw.line(self.screen, ('red'), ((col + 1) * 60, row * 60), ((col + 1)* 60, (row + 1) * 60), 1)
        pygame.draw.line(self.screen, ('red'), ((col ) * 60, (row + 1) * 60), ((col + 1) * 60, (row + 1) * 60), 1)
        self.cell_board[row][col].selected = True
    def deselect(self,row,col):
        pygame.draw.line(self.screen, ('black'), (col*60, row * 60), (col * 60, (row+1) * 60), 1)
        pygame.draw.line(self.screen, ('black'), (col*60, row * 60), ((col + 1) * 60, (row) * 60), 1)
        pygame.draw.line(self.screen, ('black'), ((col + 1) * 60, row * 60), ((col + 1)* 60, (row + 1) * 60), 1)
        pygame.draw.line(self.screen, ('black'), ((col ) * 60, (row + 1) * 60), ((col + 1) * 60, (row + 1) * 60), 1)
        self.cell_board[row][col].selected = False
    def update_board(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.cell_board[i][j].value

    def sketch(self, value, row, col):
        if self.cell_board[row][col].sketched_value == 0:
            self.cell_board[row][col].sketched_value = value
            font = pygame.font.SysFont('arial', 30)
            num_surf = font.render(str(value), 0, ('grey'))
            num_rect = num_surf.get_rect(center=(col * 60 + 60 // 4, row * 60 + 60 // 4))
            self.screen.blit(num_surf, num_rect)
        elif self.cell_board[row][col].sketched_value != value:
            font = pygame.font.SysFont('arial', 30)
            num_surf = font.render(str(self.cell_board[row][col].sketched_value), 0, ('white'))
            num_rect = num_surf.get_rect(center=(col * 60 + 60 // 4, row * 60 + 60 // 4))
            self.screen.blit(num_surf, num_rect)
            self.cell_board[row][col].sketched_value = 0
            self.sketch(value, row, col)
        else:
            self.cell_board[row][col].sketched_value = value
            font = pygame.font.SysFont('arial', 30)
            num_surf = font.render(str(value), 0, ('grey'))
            num_rect = num_surf.get_rect(center=(col * 60 + 60 // 4, row * 60 + 60 // 4))
            self.screen.blit(num_surf, num_rect)

    def place_number(self, row, col):
        if self.cell_board[row][col].value == 0:
            self.cell_board[row][col].value = self.cell_board[row][col].sketched_value
            font = pygame.font.SysFont('arial', 30)
            num_surf = font.render(str(self.cell_board[row][col].sketched_value), 0, ('white'))
            num_rect = num_surf.get_rect(center=(col * 60 + 60 // 4, row * 60 + 60 // 4))
            self.screen.blit(num_surf, num_rect)
            self.cell_board[row][col].sketched_value = 0
            self.cell_board[row][col].draw()
        elif self.cell_board[row][col].value == self.cell_board[row][col].sketched_value:
            self.cell_board[row][col].value = self.cell_board[row][col].sketched_value
            font = pygame.font.SysFont('arial', 30)
            num_surf = font.render(str(self.cell_board[row][col].sketched_value), 0, ('white'))
            num_rect = num_surf.get_rect(center=(col * 60 + 60 // 4, row * 60 + 60 // 4))
            self.screen.blit(num_surf, num_rect)
            self.cell_board[row][col].sketched_value = 0
            self.cell_board[row][col].draw()
        else:
            font = pygame.font.SysFont('arial', 30)
            num_surf = font.render(str(self.cell_board[row][col].value), 0, ('white'))
            num_rect = num_surf.get_rect(center=(col * 60 + 60 // 2, row * 60 + 60 // 2))
            self.screen.blit(num_surf, num_rect)
            self.cell_board[row][col].value = self.cell_board[row][col].sketched_value
            self.place_number(row, col)


    def check_board(self):
        self.update_board()
        if self.board == self.board_answer:
            return True
        else:
            return False
    def reset_to_orignal(self):
        pass
    def is_full(self):
        for i in range(9):
            for j in range(9):
                if self.cell_board[i][j].value == 0:
                    return False
        return True