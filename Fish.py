import pygame
import random

class Fish:
    def __init__(self, id, frame, image):
        self.frame = frame
        self.image = image
        self.width, self.height = pygame.display.get_surface().get_size()
        self.fishwidth = self.image.get_width()
        self.fishheight = self.image.get_height()
        self.xfishpos = 0 - self.fishwidth
        self.xfish3pos = self.width + self.fishheight
        self.yfishpos1 = random.randrange(500, 600, 1)
        self.yfishpos2 = random.randrange(400, 500, 1)
        self.yfishpos3 = random.randrange(600, 700, 1)
        self.xfish1_direction = 3
        self.xfish2_direction = 2
        self.xfish3_direction = 1
        self.yfish_direction = 0
        self.id = id
        self.rect1 = pygame.Rect(self.xfishpos, self.yfishpos1, self.image.get_width(), self.image.get_height())
        self.rect2 = pygame.Rect(self.xfishpos, self.yfishpos2, self.image.get_width(), self.image.get_height())
        self.rect3 = pygame.Rect(self.xfish3pos, self.yfishpos3, self.image.get_width(), self.image.get_height())
        self.offscreen = False
        self.offscreen3 = False

    def move_fish1(self):
        self.xfishpos += self.xfish1_direction
        self.rect1 = pygame.Rect(self.xfishpos, self.yfishpos1, self.image.get_width(), self.image.get_height())

    def move_fish2(self):
        self.xfishpos += self.xfish2_direction
        self.rect2 = pygame.Rect(self.xfishpos, self.yfishpos2, self.image.get_width(), self.image.get_height())

    def move_fish3(self):
        self.xfish3pos -= self.xfish3_direction
        self.rect3 = pygame.Rect(self.xfish3pos, self.yfishpos3, self.image.get_width(), self.image.get_height())

    def draw_fish1(self):
        self.frame.blit(self.image, (self.xfishpos, self.yfishpos1))

    def draw_fish2(self):
        self.frame.blit(self.image, (self.xfishpos, self.yfishpos2))

    def draw_fish3(self):
        self.frame.blit(self.image, (self.xfish3pos, self.yfishpos3))

    def collision(self):
        if self.xfishpos >= self.width:
            self.offscreen = True

    def collision3(self):
        if self.xfish3pos <= 0 - self.fishwidth:
            self.offscreen3 = True