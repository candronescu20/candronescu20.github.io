import pygame
import time
import random

pygame.init() #"initialize" all of the pygame modules used

white = (255,255,255) #(r, g, b)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
bbblue = (137, 207, 240)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))  #tuple (800 = width, 600 = height)
pygame.display.set_caption('sad snake game')

img = pygame.image.load ('C:/Users/Christina Andronescu/Desktop/py.shit/lacabeza.png')
appleimg = pygame.image.load('C:/Users/Christina Andronescu/Desktop/py.shit/mar.png')

clock = pygame.time.Clock()

block_size = 20
FPS = 15

direction = "right"

smallfont = pygame.font.SysFont("fixedsys", 25)
medfont = pygame.font.SysFont("fixedsys", 50)
largefont = pygame.font.SysFont("fixedsys", 80)

def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c: #key of C
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()                  
        
        gameDisplay.fill(white)
        message_to_screen("welcome to disappointment",
                          bbblue,
                          -100,
                          size="large")
        message_to_screen("goal: eat the ambiguous red blobs",
                          black,
                          -30,)
        message_to_screen("result: the more blobs eaten, the longer the snake",
                          black,
                          10,)
        message_to_screen("warning: don't run into the walls and/or yourself, dummy",
                          black,
                          50,)
        message_to_screen("begin: press C",
                          black,
                          180,)
        message_to_screen("quit before u even begin coward: press Q",
                          black,
                          210,)
        
        pygame.display.update()
        clock.tick(15)   

def snake(block_size,snakeList):
    
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
        
    if direction == "left":
        head = pygame.transform.rotate(img, 90)       #These moves the snake

    if direction == "up":
        head = img
        
    if direction == "down":
         head = pygame.transform.rotate(img, 180)
    
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace #y_displacement = center of text
    gameDisplay.blit(textSurf, textRect)
    
def gameLoop():
    global direction #turns into a global variable

    direction = 'right'
    gameExit = False
    gameOver = False
    #specify variables
    lead_x = display_width/2     #"lead" will be the leader of the group, the number one block
    lead_y = display_height/2
    
    lead_x_change = 10
    lead_y_change = 0
    
    snakeList = []
    snakeLength = 1
    
    randAppleX = round(random.randrange(0, display_width - block_size))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - block_size))#/10.0)*10.0
    
    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("you done goofed",
                              red,
                              y_displace = -50,
                              size = "large")
            message_to_screen("press C to play again or Q to quit",
                              black,
                              50,
                              size = "medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()   
        
        for event in pygame.event.get():
            #event handling: event is only a change in status; holding a key down is NOT an event, but lifting a key IS 
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:   #if this if statement is true, won't even ask the following elif ones
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size 
                    lead_y_change = 0  #every time x changes have to reaffirm that y does not, otherwise end up with jagged diagonal movement
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size 
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size 
                    lead_x_change = 0  #same applies for when x changes, reaffirm that y does not
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size 
                    lead_x_change = 0
        #setting boundaries   
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
           
        lead_x += lead_x_change  #sum lead_x and lead_x_change #top left x and y coordinates
        lead_y += lead_y_change
        
        gameDisplay.fill(white)

        AppleThickness = 30
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        
        if len (snakeList) > snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
   
        
        snake(block_size, snakeList)
       
        
        snake(block_size,snakeList)
        
        pygame.display.update()
        
##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
##            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
##                randAppleX = round(random.randrange(0, display_width - block_size))#/10.0)*10.0
##                randAppleY = round(random.randrange(0, display_height - block_size))#/10.0)*10.0
##                snakeLength += 1

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0, display_width - block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0, display_height - block_size))#/10.0)*10.0
                snakeLength += 1
                
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0, display_width - block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0, display_height - block_size))#/10.0)*10.0
                snakeLength += 1
            
            
            
        clock.tick(FPS) #frames per second
       
    pygame.quit()   #uninitializing pygame
    quit()  #exit out of python

game_intro()   
gameLoop()
