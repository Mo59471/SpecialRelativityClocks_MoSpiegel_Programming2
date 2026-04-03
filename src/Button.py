import pygame

class Button:

    def __init__(self, label, x, y, w, h, img, hovImg, clickImg):
        self.label = label
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = img
        self.hovImg = hovImg
        self.clickImg = clickImg
        self.hovering = False

    def display(self, screen, clicked):
        if clicked == False and self.hovering:
            screen.blit(self.hovImg, (0,0))
        elif clicked and self.hovering:
            screen.blit(self.clickImg, (0,0))
        else:
            screen.blit(self.img, (0,0))
    
    def hover(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseX >= self.x and mouseX <= self.x +self.w and mouseY >= self.y and mouseY <= self.y + self.h:
            self.hovering = True
        else:
            self.hovering = False