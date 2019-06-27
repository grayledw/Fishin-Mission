import pygame

class Score:
    def __init__(self, frame):
        self.frame = frame
        self.size = pygame.display.get_surface().get_size()
        self.width = self.size[0]
        self.height = self.size[1]
        self.current_score = 0

        self.text_type = 'Comic Sans'
        self.text_size = 25
        self.bold = False
        self.italic = False

        self.score_text = ('Score: ' + str(self.current_score))
        self.antialias = True
        self.text_color = (255, 255, 255)

        self.font = pygame.font.SysFont(self.text_type, self.text_size, self.bold, self.italic)
        self.score_text_display = self.font.render(self.score_text, self.antialias, self.text_color)

    def draw_score_text(self, x, y):
        self.frame.blit(self.score_text_display, (x, y))

    def update_score(self, score_increment):
        self.current_score += score_increment
        print(self.current_score)
        self.score_text = ('Score: ' + str(self.current_score))
        self.score_text_display = self.font.render(self.score_text, self.antialias, self.text_color)
