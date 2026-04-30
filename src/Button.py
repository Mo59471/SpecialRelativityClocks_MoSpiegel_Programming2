import pygame

class Button:

    def __init__(self, label, x, y, w, h, img, hovImg, clickImg, show):
        self.label = label
        self.rect = pygame.Rect(x,y,w,h)
        self.img = img
        self.hovImg = hovImg
        self.clickImg = clickImg
        self.hovering = False
        self.toggle = -1
        self.show = show

    def display(self, screen, clicked):
        if self.show == 1:
            if clicked == False and self.hovering:
                screen.blit(self.hovImg, (0,0))
            elif clicked and self.hovering:
                screen.blit(self.clickImg, (0,0))
            else:
                screen.blit(self.img, (0,0))
    
    def hover(self):
        mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos):
            self.hovering = True
        else:
            self.hovering = False