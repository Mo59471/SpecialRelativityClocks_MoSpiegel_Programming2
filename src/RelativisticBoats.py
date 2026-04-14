import pygame
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


def display(screen, clicked, justClicked, v, font1):

    # Draw background
    screen.blit(backImg, (0,0))

    # Draw sidebar
    screen.blit(sidebarImg, (0,0))
    screen.blit(sidebarOverlayImg, (0,0))
    screen.blit(sidebarElementImg, (0,0))
    
    # Draw text
    vText = font1.render(f"v = {int(v)} m/s", True, (172,176,222))
    vRect = vText.get_rect()
    vRect.center = (157,515)
    screen.blit(vText, vRect)

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


def getdt():
    pass

# Initialize data                      

font1 = pygame.font.Font("MavenPro-Bold.ttf", 20)

clicked = False
justClicked = False
showClocks = True
lorentzC = True
dt = 0
clock = pygame.time.Clock()
v = 0

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
                        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicked = False

    # Method calls
    v = slider.getV()
    display(screen, clicked, justClicked, v, font1)
    
    clock.tick(60)
