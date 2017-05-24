""" Plot random pixels on the screen using keyboard moves"""

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


class moving_pixel():

    def _init_ (self , x, y):
        self.x=x
        self.y=y
        self.hdir=0
        self.vdir=-1

    def directions (self , dir):
        self.hdir , self.vdir= dir

    def move(self):
        self.x+=self.hdir
        self.y+=self.vdir

    def draw(self , surface):
        surface.set_at((self.x, self.y), (255, 255,255))



screen = pygame.display.set_mode((width, height))
clock=pygame.time.Clock()

running=True
pix=moving_pixel(width/2, height/2)

while running:
    pix.move()

    if pix.x<=0 or pix.x>=width or pix.y<=0 or pix.y>height:
        print "Crash"
        running=False
    screen.fill((0,0,0))
    pix.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP:
                pix.dir( UP)
            elif event.type == pygame.K_DOWN:
                pix.dir( DOWN)
            elif event.type == pygame.K_LEFT:
                pix.dir( LEFT)
            elif event.type == pygame.K_RIGHT:
                pix.dir(RIGHT)


    pygame.display.flip()
    clock.tick(20)
