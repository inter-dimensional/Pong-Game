#pong game

#=================================================================================================================
#create a window for the game. setup and initiate. next is create an objects: ball and the paddle
#calculate maths for the direction of the ball, collisions. create an event when you press a key, the paddle will
#move up and down to catch the ball. 
#=================================================================================================================


import pygame, sys
from pygame.locals import *

FPS = 30

window_width = 800
window_height = 600

white = ("white")
red = ("red")
black = ("black")

UP = "up"
DOWN = "down"

def main():
    global FPSCLOCK, screen, font
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Pong game")

    running = True
    while running:
        showStartScreen()
        runGame()

def runGame():
    
    player_y = 250
    player_speed = 30
    
    enemy_y = 250
    enemy_speed = 30

    ball_x = 400
    ball_y = 270
    ball_speed_x = 30
    ball_speed_y = 30
    
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_y -= player_speed
        if keys[pygame.K_s]:
            player_y += player_speed
        
        if player_y < 0:
            player_y = 0
        if player_y > 520:
            player_y = 520
        
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        
        #ai logic
        enemy_center = enemy_y + 40
        if ball_y > enemy_center:
            enemy_y += enemy_speed
        elif ball_y < enemy_center:
            enemy_y -= enemy_speed
        
        if enemy_y < 0:
            enemy_y = 0
        if enemy_y > 520:
            enemy_y = 520
        
        #this is to prevent the ball from going outside the window vertically
        if ball_y <= 0:
            ball_speed_y = abs(ball_speed_y)
        if ball_y >= 580:
            ball_speed_y = -abs(ball_speed_y)
        
        #this is to prevent the ball from going outside the window horizontally        
        if ball_x <= 0:
            ball_speed_x = abs(ball_speed_x)
        if ball_x >= 780:
            ball_speed_x = -abs(ball_speed_x)
                
        screen.fill(white)
        
        player_rect = drawPaddle(100, player_y)
        enemy_rect = enemyPaddle(660, enemy_y)
        ball_rect = drawBall(ball_x, ball_y)
        
        if ball_rect.move(ball_speed_x, 0).colliderect(player_rect):
            if ball_speed_x < 0:
                ball_speed_x = -ball_speed_x
                ball_x = player_rect.right
                ball_x = player_rect.left
                
        if ball_rect.colliderect(enemy_rect):
            ball_speed_x = -ball_speed_x
            if ball_speed_x > 0:
                ball_speed_x = -ball_speed_x
                ball_x = enemy_rect.left - 20
        FPSCLOCK.tick(FPS)
        pygame.display.flip()

def checkPressKey():   
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return True
    return False        

def showStartScreen():    
    titleFont = pygame.font.Font("freesansbold.ttf", 48)
    titleScreen = titleFont.render("PONG GAME", True, black)
    
    pressKeyFont = pygame.font.Font("freesansbold.ttf", 20)
    pressKeyMsg = pressKeyFont.render("Press enter to Play", True, black)
    
    elijahFont = pygame.font.Font("freesansbold.ttf", 14)
    elijahMsg = elijahFont.render("First game written from scratch by ELIJAH TAHADLANGIT", True, black)
    
    menu_running = True
    while menu_running:
        screen.fill(white)
        
        screen.blit(titleScreen, (245, 150))
        screen.blit(pressKeyMsg, (310, 290))
        screen.blit(elijahMsg, (390, 580))
        
        if checkPressKey():
            menu_running = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
    
        pygame.display.flip()
        FPSCLOCK.tick(FPS)
    
def drawPaddle(x, y):
    paddleDesign = pygame.Rect(x, y, 40, 100)
    pygame.draw.rect(screen, red, paddleDesign)
    return paddleDesign
    
def enemyPaddle(x, y):
    enemyPaddleDesign = pygame.Rect(x, y, 40, 100)
    pygame.draw.rect(screen, black, enemyPaddleDesign)
    return enemyPaddleDesign
    
def drawBall(x, y):
    ballDesign = pygame.Rect(x, y, 20, 20)
    pygame.draw.circle(screen, black, [x, y], 15)
    return ballDesign
    
  
if __name__ == "__main__":
    main()