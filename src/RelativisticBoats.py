# Relativistic Boat
# Mo Spiegel
# Period 3B

import pygame
import math
from Boat import Boat
from Button import Button
from Checkbox import Checkbox
from Clock import Clock
from Slider import Slider

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1150,850))

# Load images
eqImg = pygame.image.load("Equations.png").convert_alpha()
endImg = pygame.image.load("EndScreen.png").convert_alpha()
startImg = pygame.image.load("StartScreen.png").convert_alpha()
backImg = pygame.image.load("Background.png").convert_alpha()
sidebarImg = pygame.image.load("Sidebar.png")
sidebarOverlayImg = pygame.image.load("SidebarOverlay.png").convert_alpha()
sidebarElementImg = pygame.image.load("SidebarElements.png").convert_alpha()
starImg = pygame.image.load("Star.png").convert_alpha()
typeBarImg = pygame.image.load("TypeBar.png").convert_alpha()

# Display method
def display(screen, clicked, justClicked, v, font1, font2, font3, font4, input, toggleT, blinkTime, tx, switchScreen, play, lorentzC, showClocks, dt):

    # Start screen
    if switchScreen == 's':
        screen.blit(startImg, (0,0))

    # End screen    
    elif switchScreen == 'e':
        screen.blit(endImg, (0,0))

    # Equation screen
    elif switchScreen == "eq":
        screen.blit(eqImg, (0,0))
    
    # Main screen
    elif switchScreen == 'm':

        # Draw background
        screen.blit(backImg, (0,0))

        # Display boat (with Lorentz contraction)
        boat.lorentzContraction(lorentzC, v)
        boat.display(screen, v, play, lorentzC, font1, font3)
        
        # Draw sidebar
        screen.blit(sidebarImg, (0,0))
        screen.blit(sidebarOverlayImg, (0,0))
        screen.blit(sidebarElementImg, (0,0))

        # Draw typebar
        if toggleT == 1:
            screen.blit(typeBarImg, (0,0))
            # Draw blinking type cursor
            if blinkTime <= 20:
                pygame.draw.line(screen, (255,255,255), (346 + tx,770), (346 + tx, 795), 2)

        # Draw text
        if len(str(v)) <= 13:
            vText = font1.render(f"v = {v} m/s", True, (172,176,222)) 
        else:
            vText = font1.render(f"v = {str(v)[0:11]}... m/s", True, (172, 176, 222))
        vRect = vText.get_rect()
        vRect.center = (157,515)
        screen.blit(vText, vRect)

        if v >= 2997990:
            v2Text = font1.render("v = " + str(v/299792458)[0:str(v/299792458).index('.')+3] + "c", True, (172,176,222))
        else:
            v2Text = font1.render("v = 0.0c", True, (172,176,222))
        v2Rect = v2Text.get_rect()
        v2Rect.center = (157, 443)
        screen.blit(v2Text, v2Rect)

        tText = font2.render(input, True, (243, 243, 243))
        tRect = tText.get_rect()
        tRect.topleft = (346,760)
        if toggleT == 1:
            screen.blit(tText, tRect)
        else:
            input = ""

        text = font3.render("elapsed time in rest frame:", True, (243,243,243))
        textRect = text.get_rect()
        textRect.topleft = (36, 575)
        screen.blit(text, textRect)

        text = font4.render("boat's observed elapsed time:", True, (243,243,243))
        textRect= text.get_rect()
        textRect.topleft = (36,630)
        screen.blit(text, textRect)

        boatTimeStr =  str(boatTime)[0:str(boatTime).index('.')+4]
        restTimeStr =  str(restTime)[0:str(restTime).index('.')+4]

        dtText = font3.render(f"{str(boatTimeStr)} s", True, (243,243,243))
        dtTextRect = dtText.get_rect()
        dtTextRect.topleft = (36, 655)
        screen.blit(dtText, dtTextRect)

        dtText = font3.render(f"{str(restTimeStr)} s", True, (243,243,243))
        dtTextRect = dtText.get_rect()
        dtTextRect.topleft = (36, 600)
        screen.blit(dtText, dtTextRect)

        # Draw buttons
        for button in buttons:
            button.hover()
            button.display(screen, clicked)
            
        # Draw checkboxes
        for checkbox in checkboxes:
            checkbox.hover()
            checkbox.check(justClicked)
            checkbox.display(screen)
            if checkbox.checked == 1:
                screen.blit(starImg, (31, checkbox.y - 6))
        
        # Draw slider
        slider.display(screen, clicked)

        if play == 1:
            tClock.tick(dt)
        if showClocks == 1:
            tClock.display(screen, font1, play)
                    
    # Update screen
    pygame.display.flip()

# Calculate the dilated time interval for the boat given velocity
def getdt(v):
    return (math.sqrt(1-(v**2/89875517873681764)))
    

# Initialize data                      

font1 = pygame.font.Font("MavenPro-Bold.ttf", 20)
font2 = pygame.font.Font("MavenPro-Bold.ttf", 35)
font3 = pygame.font.Font("MavenPro-Bold.ttf", 19)
font4 = pygame.font.Font("MavenPro-Bold.ttf", 16)

clicked = False
justClicked = False
showClocks = 1
lorentzC = 1
dt = 0
clock = pygame.time.Clock()
v = 0
input = ""
toggleT = -1
blinkTime = 0
boatTime = 0.000000
restTime = 0.000000
tx = 0
switchScreen = 's'
play = -1
waveTog = 1

# Load sound
pygame.mixer.music.load("Debussy.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.7)
waves = pygame.mixer.Sound("Waves.mp3")
chanel1 = waves.play(loops=-1)
waves.set_volume(0.1)

# Initialize button data
buttonData = [
    {"label" : "play", "x": 30, "y": 37, "w": 258, "h": 75, "img": pygame.image.load("StartButtonNorm.png").convert_alpha(), 
    "hovImg": pygame.image.load("StartButtonHov.png").convert_alpha(), "clickImg": pygame.image.load("StartButtonClick.png").convert_alpha(), "show": 1},
    
    {"label" : "reset", "x": 30, "y": 140, "w": 258, "h": 75, "img": pygame.image.load("ResetButtonNorm.png").convert_alpha(), 
    "hovImg": pygame.image.load("ResetButtonHov.png").convert_alpha(), "clickImg": pygame.image.load("ResetButtonClick.png").convert_alpha(), "show": 1 },
    
    {"label" : "equations", "x": 30, "y": 725, "w": 258, "h": 75, "img": pygame.image.load("EquationButtonNorm.png").convert_alpha(), 
    "hovImg": pygame.image.load("EquationButtonHov.png").convert_alpha(), "clickImg": pygame.image.load("EquationButtonClick.png").convert_alpha(), "show": 1},
    
    {"label" : "done", "x": 990, "y": 742, "w": 115, "h": 58, "img": pygame.image.load("DoneButtonNorm.png").convert_alpha(), 
    "hovImg": pygame.image.load("DoneButtonHov.png").convert_alpha(), "clickImg": pygame.image.load("DoneButtonClick.png").convert_alpha(), "show": -1}
    
]

# Initialize checkbox data
checkboxData = [
    {"label" : "lorentz contraction", "y": 255, "img" : pygame.image.load("LorentzCheckboxNorm.png").convert_alpha(), "hovImg" : pygame.image.load("LorentzCheckboxHover.png").convert_alpha()},
    
    {"label" : "show clocks", "y": 314, "img" : pygame.image.load("ClockCheckboxNorm.png").convert_alpha(), "hovImg" : pygame.image.load("ClockCheckboxHover.png").convert_alpha()}
 
]

buttons = []
checkboxes = []

# Initialize slider
slider = Slider()
boat = Boat(0, pygame.image.load("Boat.png").convert_alpha())
tClock = Clock()

# Initialize buttons
for data in buttonData:
    buttons.append(Button(**data))
    
# Initialize checkboxes
for data in checkboxData:
    checkboxes.append(Checkbox(**data))

# Appliction loop
running = True
while running:

    justClicked = False
    
    # Event Detection
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()

            if switchScreen == 'm':
                if event.button == 1:
                    clicked = True
                    justClicked = True

                    # Click sound effect logic
                    for button in buttons:
                        if button.hovering:
                            if justClicked:
                                clickAud = pygame.mixer.Sound("Click.mp3")
                                clickAud.play()
                    for checkbox in checkboxes:
                        if checkbox.hovering:
                            if justClicked:
                                clickAud = pygame.mixer.Sound("Click.mp3")
                                clickAud.play()
                    if slider.hovering:
                        if justClicked:
                            clickAud = pygame.mixer.Sound("Click.mp3")
                            clickAud.play()            
                    
                    # Slider logic
                    if mouseX > slider.slideX + 25 and mouseX < slider.slideX + 75 and mouseY > 455 and mouseY < 505:
                        slider.hovering = True       
                    else:
                        slider.hovering = False

                    # Toggle typebar
                    if mouseX > 32 and mouseX < 285 and mouseY > 501 and mouseY < 528:
                        toggleT = toggleT * -1
                        buttons[3].show *= -1

                    # Checkbox logic
                    for checkbox in checkboxes:
                        if checkbox.hovering == True:
                            if checkbox.label == "lorentz contraction":
                                lorentzC *= -1
                            elif checkbox.label == "show clocks":
                                showClocks *= -1
                    
                    # Toggle sound
                    if mouseX >= 16 and mouseX <= 35 and mouseY >= 811 and mouseY <= 830:
                        if pygame.mixer.music.get_busy() == False:
                            pygame.mixer.music.unpause()
                        elif pygame.mixer.music.get_busy():
                            pygame.mixer.music.pause()
                    if mouseX >= 42 and mouseX <= 66 and mouseY >= 811 and mouseY <= 827:
                        waveTog *= -1
                        if waveTog == 1:
                            chanel1.unpause()
                        else:
                            chanel1.pause()

        elif event.type == pygame.MOUSEBUTTONUP:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked = False

            # Exit equation screen
            if switchScreen == "eq":
                if event.button == 1:
                    if mouseX > 1110 and mouseX <1134 and mouseY > 20 and mouseY < 41:
                        switchScreen = "m"
                        clickAud = pygame.mixer.Sound("Click.mp3")
                        clickAud.play()

            # Exit main screen
            elif switchScreen == 'm':
                if event.button == 1:
                    if mouseX > 1110 and mouseX <1134 and mouseY > 20 and mouseY < 41:
                        switchScreen = "e"
                        clickAud = pygame.mixer.Sound("Click.mp3")
                        clickAud.play()

                    # Done button
                    if buttons[3].hovering:
                        if input == "":
                            input = "0"
                            tx = 23
                        elif float(input) > 299792458:
                            input = "299792458"
                            tx = 193
                        else:
                            toggleT = -1
                            buttons[3].show = -1
                            v = float(input)
                            slider.slideX = int(v/1368915.33333)

                    # Play button
                    if buttons[0].hovering:
                        play *= -1
                        if buttons[0].label == "play":
                            buttons[0].img = pygame.image.load("PauseButtonNorm.png").convert_alpha()
                            buttons[0].hovImg = pygame.image.load("PauseButtonHov.png").convert_alpha()
                            buttons[0].clickImg = pygame.image.load("PauseButtonClick.png").convert_alpha()
                            buttons[0].label = "pause"
                        elif buttons[0].label == "pause":
                            buttons[0].img = pygame.image.load("StartButtonNorm.png").convert_alpha()
                            buttons[0].hovImg = pygame.image.load("StartButtonHov.png").convert_alpha()
                            buttons[0].clickImg = pygame.image.load("StartButtonClick.png").convert_alpha()
                            buttons[0].label = "play"
                    
                    # Reset button
                    if buttons[1].hovering:
                        v = 0
                        lorentzC = 1
                        slider.slideX = 0
                        boat.x = 0
                        dt = 1
                        play = -1
                        restTime = 0.00000
                        boatTime = 0.00000
                        buttons[0].img = pygame.image.load("StartButtonNorm.png").convert_alpha()
                        buttons[0].hovImg = pygame.image.load("StartButtonHov.png").convert_alpha()
                        buttons[0].clickImg = pygame.image.load("StartButtonClick.png").convert_alpha()
                        buttons[0].label = "play"
                        for checkbox in checkboxes:
                            checkbox.checked = 1
                        tClock.rot = 0
                        tClock.dTick = 0
                    
                    # Equation button
                    if buttons[2].hovering:
                        switchScreen = "eq"

        # Velocity typing
        elif event.type == pygame.KEYDOWN:
            if switchScreen == 's':
                if event.key == pygame.K_SPACE:
                    clickAud = pygame.mixer.Sound("Click.mp3")
                    clickAud.play()
                    switchScreen = 'm'
            if switchScreen == 'e':
                if event.key == pygame.K_SPACE:
                    clickAud = pygame.mixer.Sound("Click.mp3")
                    clickAud.play()
                    running = False
            if switchScreen == 'm':
                if toggleT == 1:
                    keyAud = pygame.mixer.Sound("Key.mp3")
                    keyAud.play()
                    if len(input)<27:
                        if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                            input = input + "1"
                            tx += 16
                        elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                            input = input + "2"
                            tx += 21                    
                        elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                            input = input + "3"
                            tx += 21
                        elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                            input = input + "4"
                            tx += 21
                        elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                            input = input + "5"
                            tx += 21
                        elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                            input = input + "6"
                            tx += 22
                        elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                            input = input + "7"
                            tx += 21
                        elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                            input = input + "8"
                            tx += 22
                        elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                            input = input + "9"
                            tx += 22
                        elif event.key == pygame.K_0 or event.key == pygame.K_KP0:
                            if input != "":
                                input = input + "0"
                                tx += 23
                        elif event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
                            if "." not in input and input != "":
                                input += "."
                                tx += 10
                    if event.key == pygame.K_BACKSPACE:
                        if len(input) > 0:
                            if input[len(input)-1] == "1":
                                tx-=16
                            elif input[len(input)-1] == ".":
                                tx -= 10
                            elif input[len(input)-1] == "0":
                                tx -= 23
                            elif input[len(input)-1] == "6" or input[len(input)-1] == "8" or input[len(input)-1] == "9":
                                tx-=22
                            else:
                                tx -= 21
                            input = input[0:len(input)-1]
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if input == "":
                            input = "0"
                            tx = 23
                        elif float(input) > 299792458:
                            input = "299792458"
                            tx = 193
                        else:
                            toggleT = -1
                            buttons[3].show = -1
                            v = float(input)
                            slider.slideX = int(v/1368915.33333)

    # Cursor blinking
    blinkTime += 1
    if blinkTime == 40:
        blinkTime = 0

    # Set slider according to velocity input
    if input == "":
        v = slider.getV()
    elif int(float(input)/1368915.33333)!=slider.slideX:
        v = slider.getV()
        
    # Method calls
    display(screen, clicked, justClicked, v, font1, font2, font3, font4, input, toggleT, blinkTime, tx, switchScreen, play, lorentzC, showClocks, dt)
    dt = getdt(v)

    # Track time
    if play == 1:
        if switchScreen == 'm':
            restTime += 1/60
            boatTime += dt/60
    
    clock.tick(60)
