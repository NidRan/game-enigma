"""The idea behind the game is very simple. You control a worm that move around the screen looking for food. When the worm gets the food, you get some points and the worms grows longer. Crashing onto yourself or the borders ends the game."""

import pygame
import random
import sys

try:
    width=int(sys.argv[1])
    height=int(sys.argv[2])
except:

    width=640
    height=400

# Directions
up=(0,-1)
down=(0, 1)
left=(-1,0)
right=(1, 0)


class worm():

    def __init__(self, surface   ):

        self.surface=surface
        self.x=surface.get_width()/2
        self.y=surface.get_height()/2
        self.length=1
        self.grow_to=50
        self.vx=0                   #Horizontal velocity
        self.vy=-1                  #Vertical Velocity
        self.body=[]
        self.crashed=False
        self.color=255,255,0

    def key_event(self, event):
        if event.key==pygame.K_UP:
            self.vx=0
            self.vy=-1

        elif event.key==pygame.K_DOWN:
            self.vx=0
            self.vy=1

        elif event.key==pygame.K_LEFT:
            self.vx=-1
            self.vy=0
        elif event.key==pygame.K_RIGHT:
            self.vx=1
            self.vy=0



    def move(self):
        self.x+=self.vx
        self.y+=self.vy

        # r , g , b , a =self.surface.get_at((self.x, self.y))
        #
        # if (r, g, b)!=(0,0,0):
        #     self.crashed=True

        # self.body.insert(0,(self.x, self.y))

        #
        if (self.x, self.y ) in self.body:
            self.crashed=True

        self.body.insert(0, (self.x, self.y))

        if (self.grow_to> self.length):
            self.length+=1

        if (len(self.body))>self.length:
            self.body.pop()


    def draw(self ):
        for x, y in self.body:
            self.surface.set_at((x, y), self.color)
    def position(self):
        return self.x, self.y
    def eat(self):
        self.grow_to+=25


class Food:
    def __init__(self , surface):
        self.surface=surface
        self.x=random.randint(0 , surface.get_width())
        self.y=random.randint(0, surface.get_height())
        self.color=255,255,255

    def draw(self):
        self.surface.set_at((self.x, self.y), self.color)

    def position(self):
        return self.x , self.y


w, h=500, 500
screen = pygame.display.set_mode((w, h))
clock=pygame.time.Clock()

score=0
running=True
bgcolor=0,0,0
wo=worm(screen)
f=Food(screen)

while running:
    screen.fill((bgcolor))
    wo.move()
    wo.draw()
    f.draw()

    if wo.crashed :
        print "Crash"
        running=False
    elif wo.x<=0 or wo.x>=w-1 or wo.y<=0 or wo.y>=h-1:
        print "Crash"
        running=False
    elif wo.position()==f.position():
        score+=1
        wo.eat()
        print "Score : ", score
        f=Food(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            wo.key_event(event)

    pygame.display.flip()
    clock.tick(240)
