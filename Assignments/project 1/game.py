# Import necessary libraries for the game
import numpy as np
import pygame
import random
from pygame.locals import *
from pygame import mixer

pygame.init()

# Initialize Pygame module

mixer.music.load('dreams.mp3')
mixer.music.set_volume(0.8)

# Load and set the volume for the background music using Pygame mixer module

black = (0, 0, 0)
blue = (0,0,255)
yellow = (255, 255, 0)
green = (0,200,0)

# Define color variables in RGB format

surface = pygame.display.set_mode([650, 650])

# Create the main game window

W = 650
H = 650
N = 4

# Define variables for game window size and number of blocks

clock = pygame.time.Clock()
clock.tick(60)

# Set up the Pygame clock for managing the frame rate of the game


def btn(txt,x_cor,y_cor,width,height,before_color,hover_color):              #this function is to add buttons
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x_cor+width > mouse[0] > x_cor and y_cor+height > mouse[1] > y_cor:
        pygame.draw.rect(surface, hover_color, (x_cor,y_cor,width,height))
        if click[0] == 1:
           play()
    else:
        pygame.draw.rect(surface, before_color,  (x_cor,y_cor,width,height))
        
    txt2 = pygame.font.Font('freesansbold.ttf', 20)
    textSurf = txt2.render(txt, True, black)
    txtrect = textSurf.get_rect()
    txtrect.center =( (x_cor+(width/2)), (y_cor+(height/2)))
    surface.blit(textSurf, txtrect)




def welcome():                                #this is front page of game
    intro = True 
    image = pygame.image.load('2048.webp')
    width = image.get_rect().width
    height = image.get_rect().height
  
    while intro:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        surface.fill((102,178,255))
        
        wlcmTxt = pygame.font.Font('freesansbold.ttf',50)
        surface.blit(image,(220,240))
        frontTxt = wlcmTxt.render("WELCOME", True, (255,51,51))
        frontTxtRec = frontTxt.get_rect()

        frontTxtRec.center = (320,150)
        surface.blit(frontTxt, frontTxtRec)                           # it writes text and make rectangle


        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 265+100 > mouse[0] > 265 and 520+50 > mouse[1] > 520:
           pygame.draw.rect(surface, green, (265,520,100,50))
           if click[0] == 1:
              play()
        else:
           pygame.draw.rect(surface, yellow,  (265,520,100,50))
        
        txt2 = pygame.font.Font('freesansbold.ttf', 20)
        textSurf = txt2.render("Play", True, black)
        txtrect = textSurf.get_rect()
        txtrect.center =(315, 543)
        surface.blit(textSurf, txtrect)
        pygame.display.update()
        
dist = 11
HashGridColors = {                              #these are color codes for diffrent numbers
    'background': (189, 172, 161),
    0: (203, 210, 253),
    2: (240, 228, 220),
    4: (240, 226, 202),
    8: (242, 177, 121),
    16: (236, 141, 85),
    32: (250, 123, 92),
    64: (234, 90, 56),
    128: (237, 207, 114),
    256: (242, 208, 75),
    512: (237, 200, 80),
    1024: (227, 186, 19),
    2048: (236, 196, 2),
    4096: (96, 217, 146)
}




matrix = np.zeros((4, 4), dtype=int)


pygame.init()
pygame.display.set_caption("2048 GAME")

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)



def TakeNumFun(x):
        arr = x[x != 0]
        SumArr = []
        jump = False
        for j in range(len(arr)):
            if jump==True:
                jump = False
                continue
            if j != len(arr) - 1 and arr[j] == arr[j + 1]:
                new_n = arr[j] * 2
                jump = True
            else:
                new_n = arr[j]

            SumArr.append(new_n)
        return np.array(SumArr)


def moveFun(a):
        for j in range(4):
            if a in 'lr':                                    #moving the board function
                x = matrix[j, :]
            else:
                x = matrix[:, j]

            change = False
            if a in 'rd':
                change = True
                x = x[::-1]

            arr = TakeNumFun(x)

            n_arr = np.zeros_like(x)
            n_arr[:len(arr)] = arr

            if change:
                n_arr = n_arr[::-1]

            if a in 'lr':
                matrix[j, :] = n_arr
            else:
                matrix[:, j] = n_arr

def waitFun():                                         #keyboard input funtion
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return 'q'
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        return 'u'
                    elif event.key == K_RIGHT:
                        return 'r'
                    elif event.key == K_LEFT:
                        return 'l'
                    elif event.key == K_DOWN:
                        return 'd'
                    elif event.key == K_q or event.key == K_ESCAPE:
                        return 'q'
                    
def OverFun():
        global matrix
        matrix_old = matrix.copy()
        for move in 'lrud':
            moveFun(move)
            if not all((matrix == matrix_old).flatten()):
                matrix = matrix_old
                return False
        return True


def draw_function():                              #draw the matrix
        surface.fill(HashGridColors['background'])

        for i in range(4):
            for j in range(4):
                n = matrix[i][j]

                widthRec = W // 4 - 2 * dist
                HeightRec = H // 4 - 2 * dist

                xcor = j *W // 4 + dist
                ycor = i * H // 4 + dist

                pygame.draw.rect(surface, HashGridColors[n], pygame.Rect(xcor, ycor, widthRec, HeightRec), border_radius=10)
                if n == 0:
                    continue
                Tscreen = myfont.render(f'{n}', True, blue)
                rec = Tscreen.get_rect(center=(xcor + widthRec / 2,
                                                          ycor + HeightRec / 2))
                surface.blit(Tscreen, rec)



def play():
    pygame.mixer.music.play(-1)                 #to play music
    blank = list(zip(*np.where(matrix == 0)))
    for i in random.sample(blank, k=2):
        if random.random() < .1:
            
            matrix[i] = 4
        else:
            matrix[i] = 2

    inp = 'q'
    while True:
        draw_function()
        pygame.display.flip()        # This part updates a portion of screen
        inp = waitFun()
        if inp == 'q':
            break

        mat = matrix.copy()
        moveFun(inp)
    
        if OverFun():
          print('GAME OVER!')                   #game over condition
          break                           

        if not all((matrix == mat).flatten()):
          blank = list(zip(*np.where(matrix == 0)))
          for i in random.sample(blank, k=1):
            if random.random() < .1:
               matrix[i] = 4
            else:
               matrix[i] = 2


if __name__ == "__main__":
    welcome()
    play()
    pygame.quit()