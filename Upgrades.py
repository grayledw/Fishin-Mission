import pygame

class Upgrades:
    def __init__(self, frame):
        self.frame = frame
        self.image_young = pygame.image.load('images/young adult player.png')
        self.image_old = pygame.image.load('images/old player.png')
        self.width = self.frame.get_width()
        self.height = self.frame.get_height()
        # Start Circle
        self.circle_radius = 50
        self.circle_x = self.width - self.circle_radius
        self.circle_y = self.circle_radius
        self.upgrade_circle_color = pygame.Color('white')
        self.circle_center = (self.circle_x, self.circle_y)
        self.circle_border_width = 5
        # Text Start
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans', 25, False, False)
        self.upgrades = font.render("Upgrades", True, (0, 0, 0))

    def draw_upgrade_circle(self):
        pygame.draw.circle(self.frame, self.upgrade_circle_color, self.circle_center, self.circle_radius, self.circle_border_width)

    def draw_upgrades(self):
        self.play_pos_x = self.width - 90
        self.play_pos_y = 40

        self.playRect = self.upgrades.get_rect()
        self.playRect.center = (self.play_pos_x, self.play_pos_y)
        self.frame.blit(self.upgrades, (self.playRect.center))
