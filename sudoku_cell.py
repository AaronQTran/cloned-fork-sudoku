import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        if self.value != 0:
            font = pygame.font.SysFont('arial',30)
            num_surf = font.render(str(self.value), 0, (0,0,0))
            num_rect = num_surf.get_rect(center = (self.col * 60 + 60//2,self.row * 60 + 60//2))
            self.screen.blit(num_surf,num_rect)