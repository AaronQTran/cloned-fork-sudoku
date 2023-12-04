import pygame
from sudoku_board import Board
import sys
from sudoku_cell import Cell


def game_start_screen(screen):



    clock = pygame.time.Clock()
    running = True

    white = (255, 255, 255)
    black = (0,0,0)
    green = (0, 255, 0)

    #title characteristics
    title_font = pygame.font.Font('freesansbold.ttf', 32)
    text = title_font.render('Welcome to Sudoku', True, green, white)
    textRect = text.get_rect()
    textRect.center = (540 // 2, 600 // 5)

    #button font and characteristics
    button_font = pygame.font.Font('freesansbold.ttf', 25)
    easy_text = button_font.render("Easy", 0, (255,255,255))
    medium_text = button_font.render("Medium", 0, (255,255,255))
    hard_text = button_font.render("Hard", 0, (255,255,255))

    #button background
    easy_size = easy_text.get_size()[0]
    medium_size = medium_text.get_size()[0]
    hard_size = hard_text.get_size()[0]

    #button background side space
    easy_surface = pygame.Surface((easy_size + 20, easy_text.get_size()[1]+15))
    medium_surface = pygame.Surface((medium_size + 20, medium_text.get_size()[1]+15))
    hard_surface = pygame.Surface((hard_size+20, hard_text.get_size()[1]+15))
    # makes the space around the button text green
    easy_surface.fill(green)
    medium_surface.fill(green)
    hard_surface.fill(green)

    # adds white text in front of background
    easy_surface.blit(easy_text, (10,10))
    medium_surface.blit(medium_text,(10,10))
    hard_surface.blit(hard_text,(10,10))

    #initialize button rectangle
    easy_rectangle = easy_surface.get_rect(center=(530//2,600//2 + 50))
    medium_rectangle = medium_surface.get_rect(center=(530//2,600//2 + 120))
    hard_rectangle = hard_surface.get_rect(center=(530//2,600//2 + 190))

    screen.fill(white)
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)
    while running:

        screen.blit(text, textRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    difficulty = "easy"


                elif medium_rectangle.collidepoint(event.pos):
                    difficulty = "medium"

                elif hard_rectangle.collidepoint(event.pos):
                    difficulty = "hard"
                return difficulty




        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

def game_screen(screen, difficulty):
    screen.fill("white")

    clock = pygame.time.Clock()
    running = True
    main_board = Board(screen,difficulty)
    main_board.draw()
    for i in range(9):
        for j in range(9):
            if main_board.cell_board[i][j].value != 0:
                main_board.cell_board[i][j].draw()
    #print("yo")
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                print(x//60,y//60)
                main_board.select(y//60,x//60)

        # fill the screen with a color to wipe away anything from last frame


        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()



def main():
    pygame.init()
    screen = pygame.display.set_mode((540, 600))
    difficulty = game_start_screen(screen)
    game_screen(screen, difficulty)






if __name__ == '__main__':
    main()
