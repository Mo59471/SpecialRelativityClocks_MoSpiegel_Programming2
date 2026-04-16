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
backImg = pygame.image.load("Background.png").convert_alpha()
sidebarImg = pygame.image.load("Sidebar.png")
sidebarOverlayImg = pygame.image.load("SidebarOverlay.png").convert_alpha()
sidebarElementImg = pygame.image.load("SidebarElements.png").convert_alpha()
starImg = pygame.image.load("Star.png").convert_alpha()
typeBarImg = pygame.image.load("TypeBar.png").convert_alpha()


def display(screen, clicked, justClicked, v, font1, font2, input, toggleT, time):

    # Draw background
    screen.blit(backImg, (0,0))

    # Draw sidebar
    screen.blit(sidebarImg, (0,0))
    screen.blit(sidebarOverlayImg, (0,0))
    screen.blit(sidebarElementImg, (0,0))

    # Draw typebar
    if toggleT == 1:
        screen.blit(typeBarImg, (0,0))
        if time <= 20:
            pygame.draw.line(screen, (255,255,255), (346,770), (346, 798), 2)

    # Draw text
    vText = font1.render(f"v = {int(v)} m/s", True, (172,176,222))
    vRect = vText.get_rect()
    vRect.center = (157,515)
    screen.blit(vText, vRect)

    tText = font2.render(input, True, (243, 243, 243))
    tRect = tText.get_rect()
    tRect.topleft = (346,760)

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
    if v < 299792458:
        dt = 1/(math.sqrt(1-(v**2/89875517873681764)))
    else: dt = -1

# Initialize data                      

font1 = pygame.font.Font("MavenPro-Bold.ttf", 20)
font2 = pygame.font.Font("MavenPro-Bold.ttf", 35)

clicked = False
justClicked = False
showClocks = True
lorentzC = True
dt = 0
clock = pygame.time.Clock()
v = 0
input = ""
toggleT = -1
time = 0
greaterC = False

# Initialize button data
buttonData = [
    {"label" : "play", "x": 30, "y": 37, "w": 258, "h": 75, "img": pygame.image.load("StartButtonNorm.png").convert_alpha(), 
    "hovImg": pygame.image.load("StartButtonHov.png").convert_alpha(), "clickImg": pygame.image.load("StartButtonClick.png").convert_alpha()},
    
    {"label" : "reset", "x": 30, "y": 140, "w": 258, "h": 75, "img": pygame.image.load("ResetButtonNorm.png").convert_alpha(), 
    "hovImg": pygame.image.load("ResetButtonHov.png").convert_alpha(), "clickImg": pygame.image.load("ResetButtonClick.png").convert_alpha()},
    
    {"label" : "equations", "x": 30, "y": 725, "w": 258, "h": 75, "img": pygame.image.load("EquationButtonNorm.png").convert_alpha(), 
    "hovImg": pygame.image.load("EquationButtonHov.png").convert_alpha(), "clickImg": pygame.image.load("EquationButtonClick.png").convert_alpha()}
    
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

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicked = False
        
        # Number typing
        elif event.type == pygame.KEYDOWN:
            if input == "":
                greaterC = True
            elif input != "":
                if input[len(input)-1] == ".":
                    if float(input + "0") <= 299792458:
                        greaterC = True
                elif float(input) <= 299792458:
                    greaterC = True

            if greaterC == True:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    input = input + "1"
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    input = input + "2"
                elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    input = input + "3"
                elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    input = input + "4"
                elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    input = input + "5"
                elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    input = input + "6"
                elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    input = input + "7"
                elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    input = input + "8"
                elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    input = input + "9"
                elif event.key == pygame.K_0 or event.key == pygame.K_KP0:
                    if input != "":
                        input = input + "0"
                elif event.key == pygame.K_PERIOD or event.key == pygame.K_KP_PERIOD:
                    if "." not in input and input != "":
                        input += "."
                elif event.key == pygame.K_BACKSPACE:
                    if len(input) > 0:
                        input = input[0:len(input)-1]
                print(input)

    time = time + 1
    if time == 40:
        time = 0

    # Method calls
    v = slider.getV()
    display(screen, clicked, justClicked, v, font1, font2, input, toggleT, time)
    getdt(v)
    
    clock.tick(60)
