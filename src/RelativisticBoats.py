import pygame
from Boat import Boat
from Button import Button
from Checkbox import Checkbox
from Clock import Clock
from Slider import Slider

pygame.display.init()

screen = pygame.display.set_mode((1150,850))

# Load images
backImg = pygame.image.load("Background.png").convert_alpha()
sidebarImg = pygame.image.load("Sidebar.png")
sidebarOverlayImg = pygame.image.load("SidebarOverlay.png").convert_alpha()
sidebarElementImg = pygame.image.load("SidebarElements.png").convert_alpha()


def display(screen, clicked):

    # Draw background
    screen.blit(backImg, (0,0))

    # Draw sidebar
    screen.blit(sidebarImg, (0,0))
    screen.blit(sidebarOverlayImg, (0,0))
    screen.blit(sidebarElementImg, (0,0))
    
    # Draw buttons
    for button in buttons:
        button.hover()
        button.display(screen, clicked)
    
    # Draw and update slider
    slider.display(screen, clicked)
    
    # Update screen
    pygame.display.flip()


def getdt():
    pass

# Initialize data
clicked = False
showClocks = True
lorentzC = True
dt = 0
clock = pygame.time.Clock()

# Initialize button data
buttonData = [
    {"label" : "play", "x": 30, "y": 37, "w": 258, "h": 75, "img": pygame.image.load("StartButtonNorm.png").convert_alpha(), 
    "hovImg": pygame.image.load("StartButtonHov.png").convert_alpha(), "clickImg": pygame.image.load("StartButtonClick.png").convert_alpha()},
    
    {"label" : "reset", "x": 30, "y": 140, "w": 258, "h": 75, "img": pygame.image.load("ResetButtonNorm.png").convert_alpha(), 
    "hovImg": pygame.image.load("ResetButtonHov.png").convert_alpha(), "clickImg": pygame.image.load("ResetButtonClick.png").convert_alpha()},
    
    {"label" : "equations", "x": 30, "y": 725, "w": 258, "h": 75, "img": pygame.image.load("EquationButtonNorm.png").convert_alpha(), 
    "hovImg": pygame.image.load("EquationButtonHov.png").convert_alpha(), "clickImg": pygame.image.load("EquationButtonClick.png").convert_alpha()}
            ]

buttons = []

# Initialize slider
slider = Slider()

# Initialize buttons
for data in buttonData:
    buttons.append(Button(**data))

# Appliction loop
running = True
while running:

    # Event Detection
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked = True
                mouseX, mouseY = pygame.mouse.get_pos()
        
                # Slider logic
                if mouseX > slider.slideX + 25 and mouseX < slider.slideX + 75 and mouseY > 455 and mouseY < 505:
                    slider.hovering = True       
                else:
                    slider.hovering = False
                    
                # Click logic
                
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicked = False

    # Method calls
    display(screen, clicked)
    
    clock.tick(60)
