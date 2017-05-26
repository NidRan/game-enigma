""" The worm game ~~~~~>  Beware of Borders & Self"""

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

    def __init__(self, surface , x, y , length  ):
        self.x=x
        self.y=y
        self.surface=surface
        self.length=length
        self.dir_x=0
        self.dir_y=-1
        self.body=[]
        self.crashed=False

    def key_event(self, event):
        if event.key==pygame.K_UP:
            self.dir_x=0
            self.dir_y=-1

        elif event.key==pygame.K_DOWN:
            self.dir_x=0
            self.dir_y=1

        elif event.key==pygame.K_LEFT:
            self.dir_x=-1
            self.dir_y=0
        elif event.key==pygame.K_RIGHT:
            self.dir_x=1
            self.dir_y=0



    def move(self):
        self.x+=self.dir_x
        self.y+=self.dir_y

        r , g , b , a =self.surface.get_at((self.x, self.y))

        if (r, g, b)!=(0,0,0):
            self.crashed=True

        self.body.insert(0,(self.x, self.y))

        #
        # if (self.x, self.y ) in self.body:
        #     self.crashed=True
        # self.body.insert(0, (self.x, self.y))

        if (len(self.body))>self.length:
            self.body.pop()


    def draw(self ):
        for x, y in self.body:
            self.surface.set_at((x, y), (255, 255, 255))



screen = pygame.display.set_mode((width, height))
clock=pygame.time.Clock()
running=True
bgcolor=0,0,0

w=worm(screen , width/2, height/2, 200)

while running:
    screen.fill((bgcolor))
    w.move()
    w.draw()

    if w.crashed or w.x<=0 or w.x>=width-1 or w.y<=0 or w.y>=height-1:
        print "Crash"
        running=False


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            w.key_event(event)

    pygame.display.flip()
    clock.tick(20)
