import pygame

y,x, di , width , height = 0,0,1,800,600
blueval=0
bluedir=1
barheight=124

linecolor=255,0,0
bgcolor=0,0,0
running=1
screen = pygame.display.set_mode((width, height))
clock=pygame.time.Clock()


# barcolor=[]
# for i in range(1,63):
#     barcolor.append((0,0,255-i*4))
# for i in range(1,63):
#     barcolor.append((0,0,i*4))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        elif event.type==pygame.MOUSEMOTION:
            x , y=event.pos
    



        # print "Mouse at ( %d , %d) "% event.pos
    screen.fill(bgcolor)
    pygame.draw.line(screen, linecolor, (x, 0), (x, height-1))
    pygame.draw.aaline(screen, linecolor, (0, y), (width-1, y))
    blueval+=bluedir
    if blueval == 255 or blueval == 0: bluedir *= -1
    pygame.display.flip()
    #   screen.fill((0, 0, 0))

    # for i in range(barheight):
    #     pygame.draw.aaline(screen , barcolor[i], (0 , y+i), (799, y+i))
    # pygame.draw.aaline(screen, linecolor, (0, y), (width-1, y))
    # y+=di
    # if y==0 or y==height-1: di*=-1
    #
    # for i in range(barheight):
    #     pygame.draw.line(screen , barcolor[i], (x+i , 0), (x+i,599))
    #
    # pygame.draw.line(screen, linecolor, (x, 0), (x, height-1))
    # x+=di
    # if x==0 or x==height-1: di*=-1

    # pygame.draw.aaline(screen, (0, 0, 255), (639, 0), (0, 479))
    pygame.display.flip()
