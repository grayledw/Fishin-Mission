import pygame
from math import *
from Game import *

class Title:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.frame = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        self.size = pygame.display.get_surface().get_size()
        self.width = self.size[0]
        self.height = self.size[1]
        self.image_wave = pygame.image.load('images/WavePattern.png')
        self.image_boat = pygame.image.load('images/brown row boat.png')
        self.image_Norton = pygame.image.load('images/Norton.png')
        self.image_small_fish = pygame.image.load('images/small fish.png')
        self.image_medium_fish = pygame.image.load('images/medium sized fish.png')
        print(self.width, self.height)
        pygame.display.set_caption("Fishin' Mission")

        #Start Circle
        self.circle_radius = 100
        self.circle_x = self.width - 100 - self.circle_radius
        self.circle_y = self.height - 100 - self.circle_radius
        #Boat
        self.boat_pos_x = 250
        self.boat_pos_y = 275
        self.boat_width = 357
        self.boat_height = 137
        self.image_boat = pygame.transform.scale(self.image_boat, (self.boat_width, self.boat_height))
        #Waves
        self.wavewidth = self.width // 3
        self.waveheight = 98
        self.xwave1pos = 0
        self.ywavepos = self.height * (4/9)
        self.xwave2pos = self.xwave1pos + self.wavewidth
        self.xwave3pos = self.xwave2pos + self.wavewidth
        self.image_wave = pygame.transform.scale(self.image_wave, (self.wavewidth, self.waveheight))
        #Text Title
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans', 100, False, False)
        self.text = font.render("Fishin' Mission", True, (0, 0, 225))
        #Text Start
        font = pygame.font.SysFont('Comic Sans', 50, False, False)
        self.play = font.render("Play!", True, (0, 0, 225))
        #Fish Norton
        self.Norton_pos_x = 25
        self.Norton_pos_y = 500
        self.Norton_width = 150
        self.Norton_height = 236
        self.image_Norton = pygame.transform.scale(self.image_Norton, (self.Norton_width, self.Norton_height))
        #Small Fish
        self.small_fish_pos_x = 650
        self.small_fish_pos_y = 550
        self.small_fish_width = 117
        self.small_fish_height = 117
        self.image_small_fish = pygame.transform.scale(self.image_small_fish, (self.small_fish_width, self.small_fish_height))
        #Medium Fish
        self.medium_fish_pos_x = 350
        self.medium_fish_pos_y = 460
        self.medium_fish_width = 146
        self.medium_fish_height = 146
        self.image_medium_fish = pygame.transform.scale(self.image_medium_fish, (self.medium_fish_width, self.medium_fish_height))

    def draw_wave(self):
        self.frame.blit(self.image_wave, (self.xwave1pos, self.ywavepos))
        self.frame.blit(self.image_wave, (self.xwave2pos, self.ywavepos))
        self.frame.blit(self.image_wave, (self.xwave3pos, self.ywavepos))

    def draw_boat(self):
        self.frame.blit(self.image_boat, (self.boat_pos_x, self.boat_pos_y))

    def start_circle(self):
        self.circle_color = (0,0,225)
        self.circle_center = (self.circle_x, self.circle_y)
        self.circle_border_width = 5

        pygame.draw.circle(self.frame, self.circle_color, self.circle_center, self.circle_radius, self.circle_border_width)

    def draw_text(self):
        self.text_pos_x = 200
        self.text_pos_y = 100


        self.textRect = self.text.get_rect()
        self.textRect.center = (self.text_pos_x, self.text_pos_y)
        self.frame.blit(self.text, (self.textRect.center))

    def draw_play(self):
        self.play_pos_x = self.width - 245
        self.play_pos_y = self.height - 215

        self.playRect = self.text.get_rect()
        self.playRect.center = (self.play_pos_x, self.play_pos_y)
        self.frame.blit(self.play, (self.playRect.center))

    def draw_Norton(self):
        self.frame.blit(self.image_Norton, (self.Norton_pos_x, self.Norton_pos_y))

    def draw_small_fish(self):
        self.frame.blit(self.image_small_fish, (self.small_fish_pos_x, self.small_fish_pos_y))

    def draw_medium_fish(self):
        self.frame.blit(self.image_medium_fish, (self.medium_fish_pos_x, self.medium_fish_pos_y))

    def distance(self, point1, point2):
        point1x = point1[0]
        point1y = point1[1]
        point2x = point2[0]
        point2y = point2[1]

        return sqrt((point2x - point1x) ** 2 + (point2y - point1y) ** 2)

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click_position = event.pos
                    distance_from_circle = self.distance(self.click_position, self.circle_center)
                    if distance_from_circle < self.circle_radius:
                        game = Game(self.frame)
                        game.run_game()

            # Sky
            self.frame.fill((135, 206, 235))

            # Water
            self.draw_boat()
            pygame.draw.rect(self.frame, (0, 187, 209), (0, self.height // 2, self.width, self.height // 2))
            self.draw_wave()
            self.start_circle()
            self.draw_text()
            self.draw_Norton()
            self.draw_small_fish()
            self.draw_medium_fish()
            self.draw_play()


            pygame.display.update()

title = Title()
title.run_game()
pygame.quit()
