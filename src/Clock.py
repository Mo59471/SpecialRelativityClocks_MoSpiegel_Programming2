import pygame

class Clock:

    def __init__(self):
        self.img1 = pygame.image.load("Clocks.png").convert_alpha()
        self.img2 = pygame.image.load("Clocks.png").convert_alpha()
        self.rot = 0
        self.dTick = 1

    def display(self, screen, font1):
        
        # Rotate clock images as it ticks
        self.rotImg1 = pygame.transform.rotate(self.img1, self.rot)
        self.rotImg1Rect = self.rotImg1.get_rect()
        self.rotImg1Rect.center = (477,158)
        self.rotImg2 = pygame.transform.rotate(self.img2, self.dTick)
        self.rotImg2Rect = self.rotImg2.get_rect()
        self.rotImg2Rect.center = (998,158)
        screen.blit(self.rotImg1, self.rotImg1Rect)
        screen.blit(self.rotImg2, self.rotImg2Rect)

        text1 = font1.render("r e s t  f r a m e", True, (172,176,222))
        text1Rect = text1.get_rect()
        text1Rect.center = (387+90, 280)
        screen.blit(text1, text1Rect)

        text2 = font1.render("m o v i n g  f r a m e", True, (172,176,222))
        text2Rect = text2.get_rect()
        text2Rect.center = (908+90,280)
        screen.blit(text2, text2Rect)

    # Get rotation/clock tick interval based on time dilation
    def tick(self, dt):
        self.rot += 1
        self.dTick += dt