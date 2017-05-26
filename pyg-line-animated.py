""" Animated Lines """

import pygame

try:
    width=int(sys.argv[1])
    height=int(sys.argv[2])

except:

    width=640
    height=400


screen = pygame.display.set_mode((width, height))
clock=pygame.time.Clock()
running=True
bgcolor=(0,0,0)
size=250
step=10
w=h=500
lines=[]
pos=0
maxlines=40



for x in range(0 , size+1 , step):
    lines.append((0 , size-x , x, 0))
    lines.append((w-(size-x),0,w , x))
    lines.append((w, h -(size-x), w-x, h))
    lines.append((size-x, h, 0, h-x))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.fill(bgcolor)
    col=0
    cur=pos

    for i in range(maxlines):
         x1, y1, x2, y2 = lines[cur]
         pygame.draw.line(screen, (col, col, col), (x1, y1), (x2, y2))

         cur += 1
         if cur >= len(lines): cur = 0
         col += 240 / maxlines
    pos += 1
    if pos >= len(lines): pos = 0

    pygame.display.flip()
    clock.tick()
