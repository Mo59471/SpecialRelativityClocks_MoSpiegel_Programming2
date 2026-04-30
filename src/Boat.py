import pygame
import math

class Boat:
    def __init__(self, x, img):
        self.x = x
        self.ogImg = img
        self.img = img
        self.speed = 0
        self.contraction = 1

    # Obtain Lorentz contraction based on velocity
    def lorentzContraction(self, lorentzC, v):
        if lorentzC == 1: 
            self.contraction = math.sqrt(1-(v**2/89875517873681764))  

    def display(self, screen, v, play, lorentzC, font1, font3):

        # Move
        if play == 1:
            self.x = self.x + v/40000000

        # Contract boat image
        if lorentzC == 1:
            self.img = pygame.transform.scale(self.ogImg, (80*self.contraction, 268))
            text = font1.render("l e n g t h:", True, (212, 205, 231))
            textRect = text.get_rect()
            textRect.center = ((self.x + 340 + 40*self.contraction), 650)
            screen.blit(text, textRect)

            lText = font3.render(str(100*self.contraction)[0:str(100*self.contraction).index(".")+4] + " m", True, (212, 205, 231))
            lTextRect = lText.get_rect()
            lTextRect.center = ((self.x + 340 + 40*self.contraction), 680)
            screen.blit(lText, lTextRect)
        else:
            self.img = self.ogImg
        if self.x > 820:
            self.x = -100
        screen.blit(self.img, (self.x+340,355))

      