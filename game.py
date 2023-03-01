# Import necessary libraries for the game
import numpy as np
import pygame
import random
from pygame.locals import *
from pygame import mixer

pygame.init()      # Initialize Pygame module

mixer.music.load('dreams.mp3')
mixer.music.set_volume(0.6)  # Load and set the volume for the background music using Pygame mixer module

black = (0, 0, 0)
blue = (0,0,255)
yellow = (255, 255, 0)
green = (0,200,0)   # Define color variables in RGB format

surface = pygame.display.set_mode([750, 650])
image = pygame.image.load("cheer.png")
width = image.get_rect().width
height = image.get_rect().height
image = pygame.transform.scale(image, (int(width*0.22), int(height*0.19)))
rect = image.get_rect()
visible = True  # Start the image as visible
diff = 500  # Blink every half-second
visibleTime = pygame.time.get_ticks()     # Create the main game window

W = 650
H = 650
N = 4    # Define variables for game window size and number of blocks

clock = pygame.time.Clock()
clock.tick(60)   # Set up the Pygame clock for managing the frame rate of the game


def text_objects(text, font, clr):
    textSurface = font.render(text, True, clr)
    return textSurface, textSurface.get_rect()


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
        if 180+100 > mouse[0] > 180 and 520+50 > mouse[1] > 520:
           pygame.draw.rect(surface, green, (180,520,100,50))
           pygame.draw.rect(surface, yellow, (375,520,100,50))
           if click[0] == 1:
              play()
        elif 475 > mouse[0] > 375 and 570 > mouse[1] > 520:
            pygame.draw.rect(surface, yellow, (180,520,100,50))
            pygame.draw.rect(surface, green, (375,520,100,50))
            if click[0] == 1:
              help()
        else:
           pygame.draw.rect(surface, yellow,  (180,520,100,50))
           pygame.draw.rect(surface, yellow, (375,520,100,50))
        
        txt2 = pygame.font.Font('freesansbold.ttf', 20)
        textSurf = txt2.render("Play", True, black)
        txtrect = textSurf.get_rect()
        txtrect.center =(230, 543)
        surface.blit(textSurf, txtrect)
        textSurf2 = txt2.render("Help", True, black)
        txtrect2 = textSurf2.get_rect()
        txtrect2.center =(425, 543)
        surface.blit(textSurf2, txtrect2)

        pygame.display.update()

def restart():                         #function to restart the game
    global Highest_score
    end = True 
    while end:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        surface.fill((102,178,255))
        
        fontType = pygame.font.Font('freesansbold.ttf',50)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 265+100 > mouse[0] > 265 and 500+50 > mouse[1] > 500:
           pygame.draw.rect(surface, green, (265,500,100,50))
           pygame.draw.rect(surface, yellow,  (265,100,100,50))
           if click[0] == 1:
             play()
        elif 265+100 > mouse[0] > 265 and 100+50 > mouse[1] > 100:
           pygame.draw.rect(surface, green, (265,100,100,50))
           pygame.draw.rect(surface, yellow,  (265,500,100,50))
           if click[0] == 1:
             help()
        else:
           pygame.draw.rect(surface, yellow,  (265,500,100,50))
           pygame.draw.rect(surface, yellow, (265,100,100,50))

        fontType = pygame.font.Font('freesansbold.ttf',50)
        Txt = fontType.render("Your Score = ", True, (255,255,255))
        txtRect = Txt.get_rect()
        txtRect.center = (280,290)
        surface.blit(Txt,txtRect)
        score = calculate_score()
        
        Txt2 = fontType.render(str(score), True, (0,240,0))
        txtRect2 = Txt2.get_rect()
        txtRect2.center = (467,293)
        surface.blit(Txt2, txtRect2)
        fontType2 = pygame.font.Font('freesansbold.ttf',33)

        if score>=Highest_score:
            Highest_score = score
            Txt3 = fontType2.render("You have made a new high Score!!", True, (255,51,51))
            txtRect3 = Txt.get_rect()
            txtRect3.center = (210,370)
            surface.blit(Txt3, txtRect3)
        else:
            Txt3 = fontType2.render("Highest Score = ", True, (255,51,51))
            txtRect3 = Txt.get_rect()
            txtRect3.center = (290,370)
            surface.blit(Txt3, txtRect3)
            Txt4 = fontType2.render(str(Highest_score), True, (255,51,51))
            txtRect4 = Txt.get_rect()
            txtRect4.center = (550,370)
            surface.blit(Txt4, txtRect4)



        txt1 = pygame.font.Font('freesansbold.ttf', 20)
        textSurf1 = txt1.render("Help", True, black)
        txtrect1 = textSurf1.get_rect()
        txtrect1.center =(317, 123)
        surface.blit(textSurf1, txtrect1)

        txt2 = pygame.font.Font('freesansbold.ttf', 20)
        textSurf = txt2.render("restart", True, black)
        txtrect = textSurf.get_rect()
        txtrect.center =(315, 524)
        surface.blit(textSurf, txtrect)
      
        pygame.display.update()


def help():                           #help function will open rules of the game
    intro = True 
    while intro:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        

        surface.fill((227,245,113))
        largeText = pygame.font.Font('freesansbold.ttf',15)
        heading = pygame.font.Font('freesansbold.ttf',50)
        TextSurf0, TextRect0 = text_objects("RULES", heading,(0,255,0))      #rules of the game
        TextSurf, TextRect = text_objects("1.The player must combine tiles of same numbers until they reach the number 2048", largeText,(200,0,0))
        TextSurf2, TextRect2 = text_objects("2.The tiles can contain only integer values starting from 2" , largeText,(200,0,0))
        TextSurf3, TextRect3 = text_objects("3.Numbers are a power of two, like 2, 4, 8, 16, 32, and so on", largeText,(200,0,0))
        TextSurf4, TextRect4 = text_objects("4.The player should reach the 2048 tile within the smallest number of steps", largeText,(200,0,0))
        TextRect0.center = (300, 120)
        TextRect.center = (302, 235)
        TextRect2.center = (207, 270)
        TextRect3.center = (210, 305)
        TextRect4.center = (270, 340)
        surface.blit(TextSurf0, TextRect0)
        surface.blit(TextSurf, TextRect)
        surface.blit(TextSurf2, TextRect2)
        surface.blit(TextSurf3, TextRect3)
        surface.blit(TextSurf4, TextRect4)

        txt2 = pygame.font.Font('freesansbold.ttf', 20)
        textSurf = txt2.render("restart", True, (255,255,255))
        txtrect = textSurf.get_rect()
        txtrect.center =(315, 524)

        if 265+100 > mouse[0] > 265 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(surface, green, (265,500,100,50))
            if click[0] == 1:
             welcome()
        else:
           pygame.draw.rect(surface, blue,  (265,500,100,50))
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

Highest_score = 0

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
        mixer.music.load('Alert.mp3')
        mixer.music.play(1)
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
                    
def Overmove():
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
                rec = Tscreen.get_rect(center=(xcor + widthRec / 2, ycor + HeightRec / 2))
                surface.blit(Tscreen, rec)

def calculate_score():                                     #Calculate the score for the given grid
    score = 0
    for row in matrix:
        for tile in row:
            score += tile
    return score


def play():
    global matrix
    global visibleTime
    global visible
    matrix = np.zeros((4, 4), dtype=int)
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
        pygame.display.flip()                                # This part updates a portion of screen
        LastBlink = pygame.time.get_ticks() - visibleTime
        if LastBlink >= diff:
           visible = not visible  # change visibility
           visibleTime = pygame.time.get_ticks()  
    
        # Draw the image
        if visible:
           surface.blit(image, (440,330))
    
        # Update the screen
        pygame.display.flip()


        inp = waitFun()
        if inp == 'q':
            break
        
        
        mat = matrix.copy()
        moveFun(inp)
    
        if Overmove():
            mixer.music.load('dreams.mp3')
            mixer.music.play(-1)
            print('GAME OVER!')                   #game over condition
            restart()
            break   
                                

        if not all((matrix == mat).flatten()):
          blank = list(zip(*np.where(matrix == 0)))
          for i in random.sample(blank, k=1):
            if random.random() < .1:
               matrix[i] = 4
            else:
               matrix[i] = 2

        pygame.display.update()
     


if __name__ == "__main__":
    welcome()
    play()

    pygame.quit()