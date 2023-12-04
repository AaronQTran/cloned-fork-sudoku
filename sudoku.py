import pygame
import sudoku_generator as sg
import sys


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
    textRect.center = (540 // 2, 630 // 5)

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
    easy_rectangle = easy_surface.get_rect(center=(530//2,630//2 + 50))
    medium_rectangle = medium_surface.get_rect(center=(530//2,630//2 + 120))
    hard_rectangle = hard_surface.get_rect(center=(530//2,650//2 + 190))

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
                    return
                if medium_rectangle.collidepoint(event.pos):
                    difficulty = "medium"
                    return
                if hard_rectangle.collidepoint(event.pos):
                    difficulty = "hard"
                    return




        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

def game_screen():

    pass


def main():
    pygame.init()
    screen = pygame.display.set_mode((540, 630))
    game_start_screen(screen)
    game_screen()






if __name__ == '__main__':
    main()
