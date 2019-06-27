import pygame
import Clouds
import Waves
import Boat
import Fish
import Fisher
import time
import Trash
import Rod
import Score
import Upgrades

class Game:
    def __init__(self, frame):
        self.width = 0
        self.height = 0
        self.frame = frame
        self.width, self.height = pygame.display.get_surface().get_size()

        pygame.display.set_caption("Fishin' Mission")
        self.frame.fill((135, 206, 235))
        self.cloud = Clouds.Clouds(self.frame)
        self.fisher = Fisher.Fisher(self.frame)
        self.boat = Boat.Boat(self.frame)
        self.rod = Rod.Rod(self.frame)
        self.wave = Waves.Waves(self.frame)
        self.score = Score.Score(self.frame)
        self.upgrades = Upgrades.Upgrades(self.frame)
        self.trash_list = []
        self.trash_interval = 6
        self.start_time = time.time()
        self.fish1_list = []
        self.fish2_list = []
        self.fish3_list = []
        self.fish1_interval = 10
        self.fish2_interval = 5
        self.fish3_interval = 20
        self.trashCount = 0
        self.fish1Count = 0
        self.fish2Count = 0
        self.fish3Count = 0

        # Load Fish Images
        self.image1 = pygame.image.load('images/small fish.png')
        self.image2 = pygame.image.load('images/medium sized fish.png')
        self.image3 = pygame.image.load('images/big fish.png')
        self.fish1width = 117
        self.fish1height = 117
        self.fish2width = 146
        self.fish2height = 146
        self.fish3width = 176
        self.fish3height = 176
        self.image1 = pygame.transform.scale(self.image1, (self.fish1width, self.fish1height))
        self.image2 = pygame.transform.scale(self.image2, (self.fish2width, self.fish2height))
        self.image3 = pygame.transform.scale(self.image3, (self.fish3width, self.fish3height))

    def run_game(self):
        running = True
        move_boat_right = False
        move_boat_left = False
        move_rod_right = False
        move_rod_left = False
        move_fisher_right = False
        move_fisher_left = False
        move_line_down = False
        move_line_up = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_RIGHT:
                        move_boat_right = True
                        move_fisher_right = True
                        move_rod_right = True
                    if event.key == pygame.K_LEFT:
                        move_boat_left = True
                        move_fisher_left = True
                        move_rod_left = True
                    if event.key == pygame.K_DOWN:
                        move_line_down = True
                    if event.key == pygame.K_UP:
                        move_line_up = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        move_boat_right = False
                        move_fisher_right = False
                        move_rod_right = False
                    if event.key == pygame.K_LEFT:
                        move_boat_left = False
                        move_fisher_left = False
                        move_rod_left = False
                    if event.key == pygame.K_DOWN:
                        move_line_down = False
                    if event.key == pygame.K_UP:
                        move_line_up = False
            # Knowing when to spawn trash
            current_time = time.time()
            time_since_game_start = current_time - self.start_time
            if time_since_game_start > self.trashCount * self.trash_interval:
                new_trash = Trash.Trash(self.frame)
                self.trash_list.append(new_trash)
                self.trashCount +=1

            # Knowing when to spawn fish
            if time_since_game_start > self.fish1Count * self.fish1_interval:
                new_fish1 = Fish.Fish(time_since_game_start, self.frame, self.image1)
                self.fish1_list.append(new_fish1)
                self.fish1Count += 1

            if time_since_game_start > self.fish2Count * self.fish2_interval:
                new_fish2 = Fish.Fish(time_since_game_start, self.frame, self.image2)
                self.fish2_list.append(new_fish2)
                self.fish2Count += 1

            if time_since_game_start > self.fish3Count * self.fish3_interval:
                new_fish3 = Fish.Fish(time_since_game_start, self.frame, self.image3)
                self.fish3_list.append(new_fish3)
                self.fish3Count += 1

            # Update the boat pos if key pressed down
            if move_boat_right:
                self.boat.move_boat_right()
            if move_boat_left:
                self.boat.move_boat_left()

            # Update the rod pos if key pressed down
            if move_rod_right:
                self.rod.move_rod_right()
            if move_boat_left:
                self.rod.move_rod_left()

            if move_line_down:
                self.rod.line_down()
            if move_line_up:
                self.rod.line_up()

            # Update fisher pos if key pressed down
            if move_fisher_right:
                self.fisher.move_fisher_right()
            if move_fisher_left:
                self.fisher.move_fisher_left()

            #Cloud movement
            self.cloud.move_cloud()

            #Wave movement
            self.wave.move_wave()

            #Fish movement
            for fish in self.fish1_list:
                fish.move_fish1()
                if fish.offscreen:
                    self.fish1_list.remove(fish)

            for fish in self.fish2_list:
                fish.move_fish2()
                if fish.offscreen:
                    self.fish2_list.remove(fish)

            for fish in self.fish3_list:
                fish.move_fish3()
                if fish.offscreen3:
                    self.fish3_list.remove(fish)
            #Trash movement
            for trash in self.trash_list:
                trash.move_trash()
                if trash.offscreen:
                    self.trash_list.remove(trash)

            for trash in self.trash_list:
                if trash.rect.collidepoint(self.rod.line_end_pos):
                    self.score.update_score(-50)
                    self.trash_list.remove(trash)
            for fish in self.fish1_list:
                if fish.rect1.collidepoint(self.rod.line_end_pos):
                    self.score.update_score(250)
                    self.fish1_list.remove(fish)
            for fish in self.fish2_list:
                if fish.rect2.collidepoint(self.rod.line_end_pos):
                    self.score.update_score(100)
                    self.fish2_list.remove(fish)
            for fish in self.fish3_list:
                if fish.rect3.collidepoint(self.rod.line_end_pos):
                    self.score.update_score(300)
                    self.fish3_list.remove(fish)

            # Cloud collision
            self.cloud.collision()

            # Wave collision
            self.wave.collision()

            #Draw Sky
            self.frame.fill((135, 206, 235))
            #Draw Water
            pygame.draw.rect(self.frame, (0, 187, 209), (0, self.height // 2, self.width, self.height // 2))
            #Draw Clouds
            self.cloud.draw()
            #Draw Fisher
            self.fisher.draw()
            #Draw Rod
            self.rod.draw()
            #Draw Boat
            self.boat.draw()
            #Draw Waves
            self.wave.draw()
            #Draw Trash
            for trash in self.trash_list:
                trash.draw()
            #Draw fish
            for fish in self.fish1_list:
                fish.draw_fish1()

            for fish in self.fish2_list:
                fish.draw_fish2()

            for fish in self.fish3_list:
                fish.draw_fish3()

            #Draw fishing Line
            self.rod.draw_line()

            #Draw score
            self.score.draw_score_text(self.boat.xboat1pos - 20 + self.boat.image.get_width() // 2, self.boat.yboatpos - 10 + self.boat.image.get_height() // 2)

            #Draw Upgrades
            self.upgrades.draw_upgrades()
            self.upgrades.draw_upgrade_circle()

            pygame.display.update()
