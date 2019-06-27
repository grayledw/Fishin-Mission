import pygame

class Fisher:
    def __init__(self, frame):
        self.frame = frame
        self.size = pygame.display.get_surface().get_size()
        self.width = self.size[0]
        self.height = self.size[1]
        self.fisherwidth = 239
        self.fisherheight = 265
        self.xfisher1pos = 0
        self.yfisherpos = self.height * (1/2) - self.fisherheight
        self.xfisher1_direction = 3
        self.yfisher1_direction = 0
        self.image = pygame.image.load('images/kid player.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.fisherwidth, self.fisherheight))

    def draw(self):
        self.collision()
        self.frame.blit(self.image, (self.xfisher1pos, self.yfisherpos))

    def collision(self):
        if (self.xfisher1pos >= self.width - self.fisherwidth - 81):
            self.xfisher1pos = self.width - self.fisherwidth - 81
        if (self.xfisher1pos <= 0):
            self.xfisher1pos = 0

    def move_fisher_right(self):
        self.xfisher1pos += self.xfisher1_direction
        #self.draw()

    def move_fisher_left(self):
        self.xfisher1pos -= self.xfisher1_direction
        #self.draw()