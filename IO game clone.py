import pygame

pygame.init()

#Get display size
infoObject = pygame.display.Info()
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

#Set display mode to Fullscreen
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

#Window Name
pygame.display.set_caption("Learn.io")

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
yellow = (255, 255, 0)


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
    
    #Don't think PEMDAS/BODMAS look at what it is doing
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
                    break
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
        
def initializeGame(gameType):
    
    running = True
    
    #Clear all previous blits
    window.blit(bkg, (0,0))
    #Black Background as 'Page'
    pageX = width/4
    pageY = height/6
    pageWidth = width-(2*pageX)
    pageHeight = height-(2*pageY)
    
    pageSize = (pageX, pageY, pageWidth, pageHeight)
    
    #User Input - Player Name
    enterName = font.render('Enter Name:', True, titleColour)
    enterNamePos = enterName.get_rect(center=( pageX+pageWidth/2, pageY+pageHeight/6) )
    
    name = ""
    playerName = font.render(name, True, titleColour)
    #User Input - Text Box
    inputBoxX = width / 2.9
    inputBoxY = height / 2.5
    inputBoxWidth = 600
    inputBoxHeight = 100
    
    inputBoxSize = (inputBoxX, inputBoxY, inputBoxWidth, inputBoxHeight)
    inputBoxCenter = playerName.get_rect(center=( inputBoxX+inputBoxWidth/2, inputBoxY+inputBoxHeight/2) )
    
    #Play Game Text & Button
    playGame = font.render('Play', True, titleColour)
    playGameCenter = playGame.get_rect(center=( pageX+pageWidth/2, pageHeight-pageY/2) )
    playGameBox = (pageX+(pageWidth/4),pageHeight-pageY/2 - 45,(pageWidth/2),90)
    
    #Drawing on Page
    pygame.draw.rect(window,black,pageSize)
    window.blit(enterName, enterNamePos)        
    pygame.draw.rect(window,white,playGameBox, 1)
    
    if(gameType == "sp"):
        while running:
            pygame.time.delay(100)
            
            mouse_pos  = pygame.mouse.get_pos()
            mouse_press = pygame.mouse.get_pressed()
            #keyPress = pygame.key.get_pressed()
            
            pygame.draw.rect(window,white,inputBoxSize)
            
            playerName = font.render(name, True, titleColour)
            inputBoxCenter = playerName.get_rect(center=( (inputBoxX+inputBoxWidth/2)-len(name), inputBoxY+inputBoxHeight/2) )
            window.blit(playerName, inputBoxCenter)
            
       
            
                 
            if pageX+(pageWidth/4) < mouse_pos[0] < pageX+(pageWidth/1.33) and pageHeight-pageY/2 -45  < mouse_pos[1] < pageHeight-pageY/2 + 45 :
                playGame = font.render('Play', True, yellow)
                window.blit(playGame, playGameCenter)
                if (mouse_press[0] == 1):
                    return name[:32]
            else:
                playGame = font.render('Play', True, titleColour)
                window.blit(playGame, playGameCenter)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == 8:          # For some reason, K_BACKSPACE wasn't working so using 8 instead
                        name = name[:-1]
                    else:
                        name = name + event.unicode
                        #print(event.key)
                
            pygame.display.update()
    
    return name[:32]
def singleplayerGame():
    window.blit(bkg, (0,0))
    playerName = initializeGame("sp")
    print("success ",playerName)
    
    
    
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
pygame.display.quit()
pygame.quit()
exit()
