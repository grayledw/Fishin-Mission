import pygame
import random

class Trash:
    def __init__(self, frame):
        self.frame = frame
        self.width, self.height = pygame.display.get_surface().get_size()
        self.trashwidth = 213
        self.trashheight = 117
        self.xtrash1pos = 0 - self.trashwidth
        self.ytrash1pos = random.randrange(400, 600, 1)
        self.xtrash1_direction = 1
        self.ytrash1_direction = 0
        self.ytrash_direction = 0
        self.image = pygame.image.load('images/trashpiece.png')
        self.rect = pygame.Rect(self.xtrash1pos, self.ytrash1pos, self.image.get_width(), self.image.get_height())
        self.image = pygame.transform.scale(self.image, (self.trashwidth, self.trashheight))
        self.offscreen = False


    def draw(self):
        self.frame.blit(self.image, (self.xtrash1pos, self.ytrash1pos))

    def move_trash(self):
        self.xtrash1pos += self.xtrash1_direction
        self.rect = pygame.Rect(self.xtrash1pos, self.ytrash1pos, self.image.get_width(), self.image.get_height())

    def collision(self):
        if (self.xtrash1pos >= self.width):
            self.offscreen = True
