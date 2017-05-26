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
size=250
step=10


for x in range(0 , size+1 , step):
    pygame.draw.line(screen , (255, 255, 255), (0, 500-x ), (x,0))

pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    clock.tick()
