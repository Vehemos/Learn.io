import pygame
pygame.init()

#Get display size
infoObject = pygame.display.Info()
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

#Set display mode to Fullscreen
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#Window Name
pygame.display.set_caption("testy.io")

#Load Images, Fonts, etc
bkg = pygame.image.load('gridBKG.jpg')
titleFont = pygame.font.Font('fonts/nemoy/NemoyMedium.otf', 132)
font = pygame.font.Font('fonts/nemoy/NemoyLight.otf', 70)

#Draw Background Once
window.blit(bkg, (0,0))

#Global Colour Variables
titleColour = (50, 195, 230)
black = (0,0,0)
darkGrey = (50,50,50)
lightGrey = (120,120,120)
white = (255,255,255)


def game_menu():
    
    display_menu = True
    play = 0
    
    title = titleFont.render('Learn.io', True, titleColour)
    
    playGame = font.render('Play', True, titleColour)
    quitGame = font.render('Quit', True, titleColour)
    singleplayer = font.render('Single Player', True, titleColour)
    multiplayer = font.render('Multi Player', True, titleColour)
    
    buttonX = width/3 + 25
    buttonY = height/2.3
    buttonWidth = 625
    buttonHeight = 90
    
    topButton = (buttonX, buttonY, buttonWidth, buttonHeight)
    bottomButton = (buttonX, buttonY + 100, buttonWidth, buttonHeight)
        
    window.blit(title, (width/3,height/4)) 
    
    playGameCenter = playGame.get_rect(center=( buttonX+buttonWidth/2, buttonY+buttonHeight/2) )
    quitGameCenter = quitGame.get_rect(center=( buttonX+buttonWidth/2, buttonY+buttonHeight+120/2) )
    singleplayerCenter = singleplayer.get_rect(center=( buttonX+buttonWidth/2, buttonY+buttonHeight/2) )
    multiplayerCenter = multiplayer.get_rect(center=( buttonX+buttonWidth/2, buttonY+buttonHeight+120/2) )
    
    
    while display_menu:
        pygame.time.delay(100)
        
        mouse_pos  = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()
        
        if play == 0: 
            if buttonX < mouse_pos[0] < buttonX + buttonWidth and buttonY < mouse_pos[1] < buttonY + buttonHeight :
                pygame.draw.rect(window, darkGrey, topButton)
                window.blit(playGame, playGameCenter)
                if (mouse_press[0] == 1):
                    play = 1
            else:
                pygame.draw.rect(window, black, topButton)
                window.blit(playGame, playGameCenter)
                
            if buttonX < mouse_pos[0] < buttonX + buttonWidth and buttonY+100 < mouse_pos[1] < buttonY + buttonHeight+100 :
                pygame.draw.rect(window, darkGrey, bottomButton)
                window.blit(quitGame, quitGameCenter)
                if (mouse_press[0] == 1):
                    display_menu = False
            else:
                pygame.draw.rect(window, black, bottomButton)
                window.blit(quitGame, quitGameCenter)
        else:
            if buttonX < mouse_pos[0] < buttonX + buttonWidth and buttonY < mouse_pos[1] < buttonY + buttonHeight :
                pygame.draw.rect(window, darkGrey, topButton)
                window.blit(singleplayer, singleplayerCenter)
                if (mouse_press[0] == 1):
                    singleplayerGame()
                    display_menu = False
            else:
                pygame.draw.rect(window, black, topButton)
                window.blit(singleplayer, singleplayerCenter)
                
            if buttonX < mouse_pos[0] < buttonX + buttonWidth and buttonY+100 < mouse_pos[1] < buttonY + buttonHeight+100 :
                pygame.draw.rect(window, darkGrey, bottomButton)
                window.blit(multiplayer, multiplayerCenter)
                if (mouse_press[0] == 1):
                    multiplayerGame()
                    display_menu = False
            else:
                pygame.draw.rect(window, black, bottomButton)
                window.blit(multiplayer, multiplayerCenter)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display_menu = False
                    
        pygame.display.update()
        
def singleplayerGame():
    window.blit(bkg, (0,0))
    
    
def multiplayerGame():
    print("To Do")
    
'''
x = 500
y = 500

radius = 50
vel = 5

run = True

while run:
    pygame.time.delay(1)
    
    keyPress = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if keyPress[pygame.K_LEFT] and (x-radius) > vel:
            x -= vel
    if keyPress[pygame.K_RIGHT] and (x+radius+vel) < infoObject.current_w:
            x += vel
    if keyPress[pygame.K_UP] and y-radius > vel:
        y -= vel
    if keyPress[pygame.K_DOWN] and (y+radius) < infoObject.current_h:
        y += vel
    
    
    
    window.blit(bkg, (0,0))
    pygame.draw.circle(window, (90,90,255), (x, y), radius, 10)
    pygame.draw.circle(window, (150,150,255), (x, y), radius-10, 0)
    
    pygame.display.update()
'''
game_menu() 
pygame.quit()
