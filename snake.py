x = 140
y = 40
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

import pygame, sys, math, random
from pygame.locals import *
pygame.init()

FPS = 10
WINDOWWIDTH = 720                          # size of window's width in pixels
WINDOWHEIGHT = 720                         # size of windows' height in pixels

BLACK    = (  0,   0,   0)
GRAY     = (100, 100, 100)
WHITE    = (255, 255, 255)
YELLOW   = (255, 255,   0)
BLUE     = (  0,   0, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
ORANGE   = (255, 100,   0)



def main():
    global DISPLAYSURF
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    DISPLAYSURF.fill(ORANGE)
    pygame.display.set_caption('SNAKE')

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Game Over', True, BLACK)
    restartText = font.render('Press the Spacebar to Restart', True, WHITE)

    tail = [(50,360),(60,360)]
    head = (70,360)
    snake = tail + [head]
    direct = (20,0)
    apple = (80,80)
    score = 0
    frames = 0
    
    gameOver = False
    
    while True:                                # main loop
        for event in pygame.event.get():       # event handling loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                a,b = subtract(pos, head)
                direct = (round(20*a/(abs(a)+abs(b))),round(20*b/(abs(a)+abs(b))))
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos    
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    gameOver = False
                    tail = [(50,360),(60,360)]
                    head = (70,360)
                    snake = tail + [head]
                    direct = (20,0)
                    apple = (80,80)
                    score = 0

        
        

        head = add(head,direct)
        tail = snake[1:]
        snake = tail + [head]

        if head[0] < 20 or head[0] > 700: gameOver = True
        if head[1] < 20 or head[1] > 700: gameOver = True
        
        if not gameOver:
            DISPLAYSURF.fill(ORANGE)
        
            if frames % 2 == 0: pygame.draw.rect(DISPLAYSURF, GRAY,[20,20,680,680], 0)
            else: pygame.draw.rect(DISPLAYSURF, GRAY,[21,21,678,678], 0)
            
            for s in snake:
                pygame.draw.circle(DISPLAYSURF, BLUE, s, 15, 0)
            for s in snake:   
                pygame.draw.circle(DISPLAYSURF, YELLOW, add(s,(-5,-5)), 3, 0) 
            pygame.draw.circle(DISPLAYSURF, WHITE, add(head,(-5,-5)), 4, 0)
            pygame.draw.circle(DISPLAYSURF, WHITE, add(head,(5,-5)), 4, 0)
            pygame.draw.circle(DISPLAYSURF, BLACK, add(head,(-5,-5)), 2, 0)
            pygame.draw.circle(DISPLAYSURF, BLACK, add(head,(5,-5)), 2, 0)

            if distance(head,apple) < 30: 
                apple = (random.randint(60,660),random.randint(60,660))
                head = add(head,direct)
                snake = snake + [head]
                score += 1
        
            pygame.draw.circle(DISPLAYSURF, RED, apple, 15, 0)          
            pygame.draw.circle(DISPLAYSURF, WHITE, add(apple,(-5,-5)), 3, 0)
            pygame.draw.circle(DISPLAYSURF, GRAY, add(apple,(0,-17)), 7, 0)
            pygame.draw.line(DISPLAYSURF, BLACK, add(apple,(0,-10)), add(apple,(0,-20)), 3)  

        else: 
            DISPLAYSURF.blit(text, (280, WINDOWHEIGHT // 2))
            DISPLAYSURF.blit(restartText, (140, 420)) 
        
        scoreText = font.render(str(score), 1,WHITE)
        DISPLAYSURF.blit(scoreText,(30,30))
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        frames += 1


def distance(point1,point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2) 

def subtract(a,b):
    return [a[0]-b[0],a[1]-b[1]]

def add(a,b):
    return (a[0]+b[0],a[1]+b[1])


main()