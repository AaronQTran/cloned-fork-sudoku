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

def game_screen(screen, difficulty, board = None, reset = False):
    screen.fill("white")
    green = (0, 255, 0)
    clock = pygame.time.Clock()
    running = True
    if not reset:
        main_board = Board(screen,difficulty)
    else:
        main_board = board
        main_board.board = main_board.og_board
        for i in range(9):
            for j in range(9):
                main_board.cell_board[i][j].value =  main_board.og_board[i][j]

    main_board.draw()
    for i in range(9):
        for j in range(9):
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

    # add the buttons onto the screen
    screen.blit(reset_surface,reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)



    cur_x, cur_y = 100, 100




    #print("yo")

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x <= 540 and y <= 540:
                    y, x = x//60, y//60
                    if main_board.cell_board[x][y].editable:
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
                if reset_rectangle.collidepoint(event.pos):
                    return "reset", main_board
                    pass
                if restart_rectangle.collidepoint(event.pos):
                    return "restart"
                    pass
                if exit_rectangle.collidepoint(event.pos):
                    return "exit"

            if cur_x != 100:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        main_board.sketch(1, cur_x,cur_y)
                    elif event.key == pygame.K_2:
                        main_board.sketch(2, cur_x,cur_y)
                    elif event.key == pygame.K_3:
                        main_board.sketch(3, cur_x,cur_y)
                    elif event.key == pygame.K_4:
                        main_board.sketch(4, cur_x,cur_y)
                    elif event.key == pygame.K_5:
                        main_board.sketch(5, cur_x, cur_y)
                    elif event.key == pygame.K_6:
                        main_board.sketch(6, cur_x, cur_y)
                    elif event.key == pygame.K_7:
                        main_board.sketch(7, cur_x,cur_y)
                    elif event.key == pygame.K_8:
                        main_board.sketch(8, cur_x,cur_y)
                    elif event.key == pygame.K_9:
                        main_board.sketch(9, cur_x,cur_y)
                    if main_board.cell_board[cur_x][cur_y].sketched_value != 0:
                        if event.key == pygame.K_RETURN:
                            main_board.place_number(cur_x, cur_y)
                            if main_board.is_full():
                                if main_board.check_board():
                                    return 'True'
                                    pass
                                else:
                                    return 'False'
                                    pass





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


def game_screen_end_win(screen):
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    clock = pygame.time.Clock()
    running = True

    #title characteristics
    title_font = pygame.font.Font('freesansbold.ttf', 32)
    text = title_font.render('Game Won!', True, green, white)
    textRect = text.get_rect()
    textRect.center=(540//2, 600//5)

    #button
    button_font = pygame.font.Font('freesansbold.ttf', 30)
    exit_end_text = button_font.render("Exit", 0, (255, 255, 255))
    exit_end_size = exit_end_text.get_size()[0]
    exit_end_surface = pygame.Surface((exit_end_size + 20, exit_end_text.get_size()[1]+15))
    exit_end_surface.fill(green)
    exit_end_surface.blit(exit_end_text,(10,10))
    exit_end_rectangle = exit_end_surface.get_rect(center =(530//2,600//2 + 50))

    screen.fill("white")

    while running:

        screen.blit(text, textRect)
        screen.blit(exit_end_surface, exit_end_rectangle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_end_rectangle.collidepoint(event.pos):
                    sys.exit() #implement this in main to check if the user has won or lost

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    pass

def game_screen_end_lose(screen):
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (0, 255, 0)
    clock = pygame.time.Clock()
    running = True

    #title characteristics
    title_font = pygame.font.Font('freesansbold.ttf', 32)
    text = title_font.render('Game Over :(', True, green, white)
    textRect = text.get_rect()
    textRect.center=(540//2, 600//5)

    #button
    button_font = pygame.font.Font('freesansbold.ttf', 30)
    exit_restart_text = button_font.render("Restart", 0, (255, 255, 255))
    exit_restart_size = exit_restart_text.get_size()[0]
    exit_restart_surface = pygame.Surface((exit_restart_size + 20, exit_restart_text.get_size()[1]+15))
    exit_restart_surface.fill(green)
    exit_restart_surface.blit(exit_restart_text,(10,10))
    exit_restart_rectangle = exit_restart_surface.get_rect(center =(530//2,600//2 + 50))

    screen.fill("white")

    while running:

        screen.blit(text, textRect)
        screen.blit(exit_restart_surface, exit_restart_rectangle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_restart_rectangle.collidepoint(event.pos):
                    return "restart" # need to implement restart for this in main

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    pass

def main():
    pygame.init()
    screen = pygame.display.set_mode((540, 600))
    difficulty = game_start_screen(screen)
    occurrence = ''  # Initialize occurrence variable outside the loop
    running = True
    running_lost_end = True

    while running:
        if 'reset' in occurrence:
            occurrence = game_screen(screen, difficulty, occurrence[1], True)
        elif occurrence == "restart":
            difficulty = game_start_screen(screen)
            occurrence = game_screen(screen, difficulty)
        elif occurrence == "exit":
            running = False
        elif occurrence == '':
            occurrence = game_screen(screen, difficulty)
        else:
            if occurrence == 'True':
                game_screen_end_win(screen)
                running = False
            else:
                lost_end_return = game_screen_end_lose(screen)
                while running_lost_end:
                    if lost_end_return == "restart":
                        occurrence = "restart"
                        break

    #this must be implemented
    #if user_wins:
        #game_screen_end_win(screen)
    #elif not user_wins:
        #game_screen_end_lose(screen)

    pygame.quit()







if __name__ == '__main__':
    main()