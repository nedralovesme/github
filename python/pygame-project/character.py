import time
from random import *
import pygame

HEROSPEED=5
HEROIMG="images/hero.png"
MONSTERSPEED=5
MONSTERIMG="images/monster.png"
GOBLINSPEED=5
GOBLINIMG="images/goblin.png"
SAFEBUFFER=50

class Hero(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.speed_x = HEROSPEED
        self.speed_y = HEROSPEED
        self.surface = pygame.image.load(HEROIMG).convert_alpha()
        self.maxspeed = HEROSPEED
        self.width=self.surface.get_width()
        self.height=self.surface.get_height()
    def render(self,screen):
        screen.blit(self.surface, (self.x,self.y))
    def update(self,width,height,edgeWidth):
        self.move()
        self.checkBoundaries(width,height,edgeWidth)
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def checkBoundaries(self,width,height,edgeWidth):
        if self.x<edgeWidth:
            self.speed_x=self.maxspeed
        if self.y<edgeWidth:
            self.speed_y=self.maxspeed
        if self.x+self.width>width-edgeWidth:
            self.speed_x=-self.maxspeed
        if self.y+self.height>height-edgeWidth:
            self.speed_y=-self.maxspeed

    def changeDirection(self,speed_x,speed_y):
        self.speed_x=speed_x
        self.speed_y=speed_y
class Monster(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.speed_x = MONSTERSPEED
        self.speed_y = 0
        self.surface = pygame.image.load(MONSTERIMG).convert_alpha()
        self.width=self.surface.get_width()
        self.height=self.surface.get_height()
        self.lastDirectionChange = time.time()
    def render(self,screen):
        screen.blit(self.surface, (self.x,self.y))
    def setInitialPosition(self,width,height,hero):
        #get hero's position, don't place monster
        #within 50 pixels of the hero
        min_x = hero.x - SAFEBUFFER
        min_y = hero.y - SAFEBUFFER
        max_x = hero.x + SAFEBUFFER
        max_y = hero.y + SAFEBUFFER

        safe_x = randint(0,width)
        safe_y = randint(0,height)

        while safe_x>=min_x and safe_x<=max_x and safe_y>=min_y and safe_y<=max_y:
            #placed in the safe zone
            safe_x = randint(0,width)
            safe_y = randint(0,height)
        self.x=safe_x
        self.y=safe_y
    def update(self,width,height):
        self.move()
        self.checkBoundaries(width,height)
        if time.time()-self.lastDirectionChange >2:
            self.changeDirection()
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
    def checkBoundaries(self,width,height):
        if self.x<0:
            self.x=width
        if self.y<0:
            self.y=height
        if self.x>width:
            self.x=0
        if self.y>height:
            self.y=0
    def changeDirection(self):
        r = randint(1,4)
        if r==1:
            self.speed_x=0
            self.speed_y=MONSTERSPEED
        if r==2:
            self.speed_x=0
            self.speed_y=-MONSTERSPEED
        if r==3:
            self.speed_x=MONSTERSPEED
            self.speed_y=0
        if r==4:
            self.speed_x=-MONSTERSPEED
            self.speed_y=0
        self.lastDirectionChange=time.time()
class Goblin(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.speed_x = GOBLINSPEED
        self.speed_y = GOBLINSPEED
        self.surface = pygame.image.load(GOBLINIMG).convert_alpha()
        self.lastDirectionChange = time.time()
    def render(self,screen):
        screen.blit(self.surface, (self.x,self.y))
    def setInitialPosition(self,width,height,hero):
        #get hero's position, don't place monster
        #within 50 pixels of the hero
        min_x = hero.x - SAFEBUFFER
        min_y = hero.y - SAFEBUFFER
        max_x = hero.x + SAFEBUFFER
        max_y = hero.y + SAFEBUFFER

        safe_x = randint(0,width)
        safe_y = randint(0,height)

        while safe_x>=min_x and safe_x<=max_x and safe_y>=min_y and safe_y<=max_y:
            #placed in the safe zone
            safe_x = randint(0,width)
            safe_y = randint(0,height)
        self.x=safe_x
        self.y=safe_y
    def update(self,width,height):
        self.move()
        self.checkBoundaries(width,height)
        if time.time()-self.lastDirectionChange >2:
            self.changeDirection()
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
    def checkBoundaries(self,width,height):
        if self.x<0:
            self.x=width
        if self.y<0:
            self.y=height
        if self.x>width:
            self.x=0
        if self.y>height:
            self.y=0
    def changeDirection(self):
        r = randint(1,4)
        if r==1:
            self.speed_x=0
            self.speed_y=GOBLINSPEED
        if r==2:
            self.speed_x=0
            self.speed_y=-GOBLINSPEED
        if r==3:
            self.speed_x=GOBLINSPEED
            self.speed_y=0
        if r==4:
            self.speed_x=-GOBLINSPEED
            self.speed_y=0
        self.lastDirectionChange=time.time()

def checkCollision(char1,char2):
    return (char1.x + char1.width > char2.x) and (char2.x + char2.width > char1.x) and  (char1.y + char1.height > char2.y) and (char2.y + char2.height > char1.y)
