import pygame

class Waves():
    def __init__(self, frame):
        self.frame = frame
        self.size = pygame.display.get_surface().get_size()
        self.width = self.size[0]
        self.height = self.size[1]
        self.wavewidth = self.width//3
        self.waveheight = 98
        self.xwave1pos = 0
        self.ywavepos = 340
        self.xwave2pos = self.xwave1pos + self.wavewidth
        self.xwave3pos = self.xwave2pos + self.wavewidth
        self.xwave4pos = self.xwave1pos - self.wavewidth
        self.xwave1_direction = .7
        self.ywave1_direction = 0
        self.image = pygame.image.load('images/WavePattern.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.wavewidth, self.waveheight))

    def draw(self):
        self.frame.blit(self.image, (self.xwave1pos, self.ywavepos))
        self.frame.blit(self.image, (self.xwave2pos, self.ywavepos))
        self.frame.blit(self.image, (self.xwave3pos, self.ywavepos))
        self.frame.blit(self.image, (self.xwave4pos, self.ywavepos))

    def move_wave(self):
        self.xwave1pos += self.xwave1_direction
        self.xwave2pos += self.xwave1_direction
        self.xwave3pos += self.xwave1_direction
        self.xwave4pos += self.xwave1_direction

    def collision(self):
        if (self.xwave1pos >= self.width):
            self.xwave1pos = 0 - self.wavewidth

        if (self.xwave2pos >= self.width):
            self.xwave2pos = 0 - self.wavewidth

        if (self.xwave3pos >= self.width):
            self.xwave3pos = 0 - self.wavewidth

        if (self.xwave4pos >= self.width):
            self.xwave4pos = 0 - self.wavewidth