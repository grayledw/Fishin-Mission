import pygame

class Rod:
    def __init__(self, frame):
        self.frame = frame
        self.size = pygame.display.get_surface().get_size()
        self.width = self.size[0]
        self.height = self.size[1]
        self.rodwidth = 250
        self.rodheight = 300
        self.xrodpos = 120
        self.yrodpos = self.height * (1 / 7)
        self.xrod_direction = 3
        self.yrod_direction = 0
        self.image = pygame.image.load('images/fishingrod.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.rodwidth, self.rodheight))
        self.image = pygame.transform.rotate(self.image, 310)
        self.line_width = 2
        self.line_length = 143
        self.rod_line_offset_x = 274
        self.rod_line_offset_y = 97
        self.end_y_pos = self.yrodpos + self.rod_line_offset_y + self.line_length
        self.line_start_pos = (self.xrodpos + self.rod_line_offset_x, self.yrodpos + self.rod_line_offset_y)
        self.line_end_pos = (self.xrodpos + self.rod_line_offset_x, self.yrodpos + self.rod_line_offset_y + self.line_length)

    def draw(self):
        self.collision()
        self.frame.blit(self.image, (self.xrodpos, self.yrodpos))

    def collision(self):
        if (self.xrodpos >= self.width - self.rodheight):
            self.xrodpos = self.width - self.rodheight
        if (self.xrodpos <= 120):
            self.xrodpos = 120

    def move_rod_right(self):
        self.xrodpos += self.xrod_direction


    def move_rod_left(self):
        self.xrodpos -= self.xrod_direction


    def draw_line(self):
        self.line_collision()
        self.line_start_pos = (self.xrodpos + self.rod_line_offset_x, self.yrodpos + self.rod_line_offset_y)
        self.line_end_pos = (self.xrodpos + self.rod_line_offset_x, self.yrodpos + self.rod_line_offset_y + self.line_length)
        pygame.draw.line(self.frame, pygame.Color('white'), self.line_start_pos, self.line_end_pos, self.line_width)

    def line_down(self):
        self.line_length += 2

    def line_up(self):
        self.line_length -= 2

    def line_collision(self):
        if self.line_length >= self.height - (self.yrodpos + self.rod_line_offset_y):
            self.line_length = self.height - (self.yrodpos + self.rod_line_offset_y)

        if self.line_length <= 143:
            self.line_length = 143
