import pygame

class Boat:
    def __init__(self, x, img):
        self.x = x
        self.img = img
        self.speed = 0
        
    def display(self, screen, v):
        self.x = self.x + v/40000000
        screen.blit(self.img, (self.x,0))
        if self.x > 820:
            self.x = -50
        

    def move(self, v):
        pass
    
    def update(self):
        pass
    
    def lorentzContraction(self, lorentzC):
        pass
        
