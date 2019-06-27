import pygame

class Boat():
    def __init__(self, frame):
        self.frame = frame
        self.size = pygame.display.get_surface().get_size()
        self.width = self.size[0]
        self.height = self.size[1]
        self.boatwidth = 357
        self.boatheight = 137
        self.xboat1pos = 0
        self.yboatpos = self.height * (1/3)
        self.xboat1_direction = 3
        self.yboat1_direction = 0
        self.image = pygame.image.load('images/brown row boat.png')
        self.rect = pygame.Rect(self.xboat1pos, self.yboatpos, self.image.get_width(), self.image.get_height())
        self.image = pygame.transform.scale(self.image, (self.boatwidth, self.boatheight))

    def draw(self):
        self.collision()
        self.frame.blit(self.image, (self.xboat1pos, self.yboatpos))

    def collision(self):
        if (self.xboat1pos >= self.width - self.boatwidth - 57):
            self.xboat1pos = self.width - self.boatwidth - 57
        if (self.xboat1pos <= 0):
            self.xboat1pos = 0

    def move_boat_right(self):
        self.xboat1pos += self.xboat1_direction

    def move_boat_left(self):
        self.xboat1pos -= self.xboat1_direction