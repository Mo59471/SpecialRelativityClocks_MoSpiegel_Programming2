import pygame
from Boat import Boat
from Button import Button
from Checkbox import Checkbox
from Clock import Clock
from Slider import Slider

def display(screen, clicked):

    # Draw background
    backImg = pygame.image.load("Background.png")
    screen.blit(backImg, (0,0))

    # Draw sidebar
    sidebarImg = pygame.image.load("Sidebar.png")
    screen.blit(sidebarImg, (0,0))
    sidebarOverlayImg = pygame.image.load("SidebarOverlay.png")
    screen.blit(sidebarOverlayImg, (0,0))
    
    #Draw buttons
    for button in buttons:
        button.hover()
        button.display(screen, clicked)
        
    # Update screen
    pygame.display.flip()


def getdt():
    pass

# Initialize data
screen = pygame.display.set_mode((1150,850))
clicked = False

# Initialize button data
buttonData = [
    {"label" : "play", "x": 30, "y": 37, "w": 258, "h": 75, "img": pygame.image.load("StartButtonNorm.png"), 
    "hovImg": pygame.image.load("StartButtonHov.png"), "clickImg": pygame.image.load("StartButtonClick.png")},
    
    {"label" : "reset", "x": 30, "y": 140, "w": 258, "h": 75, "img": pygame.image.load("ResetButtonNorm.png"), 
    "hovImg": pygame.image.load("ResetButtonHov.png"), "clickImg": pygame.image.load("ResetButtonClick.png")},
    
    {"label" : "equations", "x": 30, "y": 725, "w": 258, "h": 75, "img": pygame.image.load("EquationButtonNorm.png"), 
    "hovImg": pygame.image.load("EquationButtonHov.png"), "clickImg": pygame.image.load("EquationButtonClick.png")}
            ]

buttons = []

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
                
                # Click logic
                
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicked = False

    # Method calls
    display(screen, clicked)
