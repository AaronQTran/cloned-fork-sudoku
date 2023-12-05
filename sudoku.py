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
                    return difficulty

                elif medium_rectangle.collidepoint(event.pos):
                    difficulty = "medium"
                    return difficulty
                elif hard_rectangle.collidepoint(event.pos):
                    difficulty = "hard"
                    return difficulty




        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

def game_screen(screen, difficulty):
    screen.fill("white")
    green = (0, 255, 0)
    clock = pygame.time.Clock()
    running = True
    main_board = Board(screen,difficulty)
    main_board.draw()
    for i in range(9):
        for j in range(9):
            if main_board.cell_board[i][j].value != 0:
                main_board.cell_board[i][j].draw()

    #game_screen buttons
    button_font = pygame.font.Font('freesansbold.ttf', 30)
    reset_text = button_font.render('Reset', 0, (255,255,255))
    restart_text = button_font.render('Restart',0, (255,255,255))
    exit_text = button_font.render('Exit', 0, (255,255,255))

    #button background size scaling
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 15))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 15))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, restart_text.get_size()[1] + 15))

    #button background coloring
    reset_surface.fill(green)
    restart_surface.fill(green)
    exit_surface.fill(green)

    #white text in green bckground
    reset_surface.blit(reset_text, (10,10))
    restart_surface.blit(restart_text,(10,10))
    exit_surface.blit(exit_text, (10, 10))

    #initialize buton rectangle
    reset_rectangle = reset_surface.get_rect(center = (530//4, 600//2 + 270))
    restart_rectangle = restart_surface.get_rect(center = (530//1.3, 600//2 + 270))
    exit_rectangle = exit_surface.get_rect(center =  (530//2, 600//2 + 270))

    screen.blit(reset_surface,reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)


    cur_x, cur_y = 100, 100
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x <= 540 and y <= 540:
                    y, x = x//60, y//60
                    if main_board.cell_board[x][y].value == 0:
                        if cur_x == x and cur_y == y and main_board.cell_board[x][y].selected == True:
                            main_board.deselect(x, y)
                            cur_x, cur_y = 100, 100
                        elif cur_x == 100:
                            main_board.select(x, y)
                            cur_x, cur_y = x, y
                        else:
                            main_board.deselect(cur_x, cur_y)
                            main_board.select(x, y)
                            cur_x, cur_y = x, y

            if cur_x != 100:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        print(1)
                    if event.key == pygame.K_2:
                        print(2)
                    if event.key == pygame.K_3:
                        print(3)
                    if event.key == pygame.K_4:
                        print(4)
                    if event.key == pygame.K_5:
                        print(5)
                    if event.key == pygame.K_6:
                        print(6)
                    if event.key == pygame.K_7:
                        print(7)
                    if event.key == pygame.K_8:
                        print(8)
                    if event.key == pygame.K_9:
                        print(9)



        # fill the screen with a color to wipe away anything from last frame

                # if reset_rectangle.collidepoint(event.pos):
                #     pass
                # if restart_rectangle.collidepoint(event.pos):
                #     pass
                # if exit_rectangle.collidepoint(event.pos):
                #     pass



        pygame.display.flip()

        clock.tick(60)

    pygame.quit()



def main():
    pygame.init()
    screen = pygame.display.set_mode((540, 600))
    difficulty = game_start_screen(screen)
    game_screen(screen, difficulty)






if __name__ == '__main__':
    main()