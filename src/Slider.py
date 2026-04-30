import pygame

class Slider:
    def __init__(self):
        self.slideX = 0
        self.hovering = False
        self.starImg = pygame.image.load("Star.png").convert_alpha()

        
    def display(self, screen, clicked):
        screen.blit(self.starImg, (25+ self.slideX, 456))
        if clicked and self.hovering:
            mouseX, _ = pygame.mouse.get_pos()
            if mouseX >= 25 and mouseX + 50 <= 294:
                self.slideX = mouseX - 25


    def getV(self):
        if self.slideX > 217:
            return 299792458
        else:
            return int(self.slideX * 1368915.33333)


                