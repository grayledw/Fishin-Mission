import pygame

class Clouds():
    def __init__(self, frame):
        self.frame = frame
        self.width, self.height = pygame.display.get_surface().get_size()
        self.xcloud1pos = 100
        self.ycloud1pos = 0
        self.xcloud2pos = 700
        self.ycloud2pos = 20
        self.xcloud1_direction = 0.5
        self.ycloud1_direction = 0
        self.xcloud2_direction = -0.5
        self.ycloud2_direction = 0
        self.cloudwidth = 213
        self.cloudheight = 117
        self.image = pygame.image.load('images/clouds.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.cloudwidth, self.cloudheight))


    def draw(self):
        self.frame.blit(self.image, (self.xcloud1pos, self.ycloud1pos))
        self.frame.blit(self.image, (self.xcloud2pos, self.ycloud2pos))

    def move_cloud(self):
        self.xcloud1pos += self.xcloud1_direction
        self.xcloud2pos += self.xcloud2_direction

    def collision(self):
        if (self.xcloud1pos >= self.width):
            self.xcloud1pos = 0 - self.cloudwidth

        if (self.xcloud2pos + self.cloudwidth <= 0):
            self.xcloud2pos = self.width