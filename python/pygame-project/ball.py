import pygame

class Ball(object):
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 5
        self.radius = radius
    def update(self,width,height):
        self.x+=self.speed_x
        self.y+=self.speed_y
        if self.x+self.radius>width:
            self.speed_x=-5
        if self.y+self.radius>height:
            self.speed_y=-5
        if self.x-self.radius<0:
            self.speed_x=5
        if self.y-self.radius<0:
            self.speed_y=5
    def render(self,screen):
        pygame.draw.circle(screen,(255,0,0),(self.x,self.y),self.radius)

def main():
    # declare the size of the canvas
    width = 500
    height = 500
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
    balls = [
        Ball(50,50,50),
        Ball(100,200,20),
        Ball(30,240,12),
        Ball(160,20,30),
        Ball(200,80,80),
        Ball(500,400,10)
    ]

    # game loop
    stop_game = False
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

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        for ball in balls:
            ball.update(width,height)

        # fill background color
        screen.fill(blue_color)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        for ball in balls:
            ball.render(screen)

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
