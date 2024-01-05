import pygame, sys
from pygame.locals import *

pygame.init()

DISPSURF=    pygame.display.set_mode((640,480),0,32)

BLACK = (0,0,0)
WHITE = (255 ,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN =   (0,255,0)
myfont = pygame.font.SysFont("Arial", 64)
pygame.display.set_caption("Drawing")
label = myfont.render("Hello, world!", 1, (255, 255, 255))
DISPSURF.fill(WHITE)

pygame.draw.polygon(DISPSURF, GREEN,((146,0),(296,108),(236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.line(DISPSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPSURF, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPSURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPSURF, RED, (200, 150, 100, 50))

pixObj =    pygame.PixelArray(DISPSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

while    True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()