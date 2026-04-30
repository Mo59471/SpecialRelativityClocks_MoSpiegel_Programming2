import pygame

class Checkbox:
    
    def __init__(self, label, y, img, hovImg):
        self.label = label
        self.y = y
        self.rect = pygame.Rect(37, y, 35, 35 )
        self.img = img
        self.hovImg = hovImg
        self.checked = 1
        self.hovering = False
        
        
    def display(self, screen):
        if self.hovering: 
            screen.blit(self.hovImg, (0,0))
        else:
            screen.blit(self.img, (0,0))
    

    def hover(self):
        mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos):
            self.hovering = True
        else:
            self.hovering = False


    def check(self, clicked):
        if self.hovering and clicked:
            self.checked = self.checked * -1