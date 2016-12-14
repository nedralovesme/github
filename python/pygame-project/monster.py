import pygame
from character import *

def main():
    # declare the size of the canvas
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    # initialize the pygame framework
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    background = pygame.image.load('images/background.png').convert_alpha()
    hero = Hero(width/2,height/2)
    monster = Monster()
    monster.setInitialPosition(width, height,hero)

    # game loop
    stop_game = False
    game_over = False
    soundPlayed = False
    level=1
    enemies=[monster]
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    hero.changeDirection(0,hero.maxspeed)
                elif event.key == pygame.K_UP:
                    hero.changeDirection(0,-hero.maxspeed)
                elif event.key == pygame.K_LEFT:
                    hero.changeDirection(-hero.maxspeed,0)
                elif event.key == pygame.K_RIGHT:
                    hero.changeDirection(hero.maxspeed,0)
                elif event.key == pygame.K_RETURN:
                    game_over=False
                    soundPlayed=False
                    monster.setInitialPosition(width, height, hero)
                    goblin = Monster()
                    goblin.setInitialPosition(width, height, hero)
                    enemies.append(goblin)
        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################

        for e in enemies:
            e.update(width,height)

        hero.update(width,height,32)

        # fill background color
        # screen.fill(blue_color)
        # print background.get_width()
        screen.blit(background,(0,0))

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        hero.render(screen)
        if not game_over:
            for e in enemies:
                e.render(screen)
        else:
            #play sound
            if not soundPlayed:
                sound = pygame.mixer.Sound('sounds/win.wav')
                sound.play()
            soundPlayed = True
            level+=1

        if not game_over and checkCollision(monster,hero):
            game_over = True

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
