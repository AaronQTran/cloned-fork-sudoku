import pygame



def game_start_screen():

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    white = (255, 255, 255)
    green = (0, 255, 0)

    #title characteristics
    title_font = pygame.font.Font('freesansbold.ttf', 32)
    text = title_font.render('Welcome to Sudoku', True, green, white)
    textRect = text.get_rect()
    textRect.center = (1280 // 2, 720 // 4)

    #button characteristics
    button_font = pygame.font.Font('freesansbold.ttf', 25)

    while running:
        screen.fill("white")
        screen.blit(text, textRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 running = False





        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

def main():
    game_start_screen()


if __name__ == '__main__':
    main()