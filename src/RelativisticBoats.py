import pygame
import math
from Boat import Boat
from Button import Button
from Checkbox import Checkbox
from Clock import Clock
from Slider import Slider

pygame.init()

screen = pygame.display.set_mode((1150,850))

# Load images
startImg = pygame.image.load("StartScreen.png").convert_alpha()
backImg = pygame.image.load("Background.png").convert_alpha()
sidebarImg = pygame.image.load("Sidebar.png")
sidebarOverlayImg = pygame.image.load("SidebarOverlay.png").convert_alpha()
sidebarElementImg = pygame.image.load("SidebarElements.png").convert_alpha()
starImg = pygame.image.load("Star.png").convert_alpha()
typeBarImg = pygame.image.load("TypeBar.png").convert_alpha()


def display(screen, clicked, justClicked, v, font1, font2, font3, font4, input, toggleT, blinkTime, tx, switchScreen):

    if switchScreen == 's':
        screen.blit(startImg, (0,0))
    
    elif switchScreen == 'm':

        # Draw background
        screen.blit(backImg, (0,0))

        boat.display(screen, v)
        
        # Draw sidebar
        screen.blit(sidebarImg, (0,0))
        screen.blit(sidebarOverlayImg, (0,0))
        screen.blit(sidebarElementImg, (0,0))

        # Draw typebar
        if toggleT == 1:
            screen.blit(typeBarImg, (0,0))
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
        
        # Draw and update slider
        slider.display(screen, clicked)
                    
    # Update screen
    pygame.display.flip()


def getdt(v):
    return (math.sqrt(1-(v**2/89875517873681764)))
    

# Initialize data                      

font1 = pygame.font.Font("MavenPro-Bold.ttf", 20)
font2 = pygame.font.Font("MavenPro-Bold.ttf", 35)
font3 = pygame.font.Font("MavenPro-Bold.ttf", 19)
font4 = pygame.font.Font("MavenPro-Bold.ttf", 16)

clicked = False
justClicked = False
showClocks = True
lorentzC = True
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
            if switchScreen == 'm':
                if event.button == 1:
                    clicked = True
                    justClicked = True
                    mouseX, mouseY = pygame.mouse.get_pos()
            
                    # Slider logic
                    if mouseX > slider.slideX + 25 and mouseX < slider.slideX + 75 and mouseY > 455 and mouseY < 505:
                        slider.hovering = True       
                    else:
                        slider.hovering = False

                    # Toggle typebar
                    if mouseX > 32 and mouseX < 285 and mouseY > 501 and mouseY < 528:
                        toggleT = toggleT * -1
                        buttons[3].show *= -1

        elif event.type == pygame.MOUSEBUTTONUP:
            if switchScreen == 'm':
                if event.button == 1:
                    clicked = False
                
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
                
        
        # Number typing
        elif event.type == pygame.KEYDOWN:
            if switchScreen == 's':
                if event.key == pygame.K_SPACE:
                        switchScreen = 'm'
            if switchScreen == 'm':
                if toggleT == 1:
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


    blinkTime += 1
    if blinkTime == 40:
        blinkTime = 0

    # Method calls
    if input == "":
        v = slider.getV()
    elif int(float(input)/1368915.33333)!=slider.slideX:
        v = slider.getV()
        
    display(screen, clicked, justClicked, v, font1, font2, font3, font4, input, toggleT, blinkTime, tx, switchScreen)
    dt = getdt(v)

    if switchScreen == 'm':
        restTime += 1/60
        boatTime += dt/60
    
    clock.tick(60)
