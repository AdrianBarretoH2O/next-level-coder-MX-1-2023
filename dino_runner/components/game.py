import pygame
from dino_runner.utils.constants import BG,CLOUD, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaurio import Dinosaurio 
from dino_runner.components.cloud import Cloud,CloudTwo
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 430
        self.player = Dinosaurio()
        self.cloud = Cloud()
        self.cloud_two = CloudTwo()
        self.obstacles_manager=ObstacleManager()
        self.points = 0
        self.font = pygame.font.Font('freesansbold.ttf',20)
        
    def score(self):
        self.points,self.game_speed
        self.points+=1 
        if self.points % 500 == 0:
            self.game_speed+=1
        
        text = self.font.render("score: "+str(self.points),True,(255,0,0))
        textRect = text.get_rect()
        textRect.center = (900,30)
        self.screen.blit(text,textRect)

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.cloud.updatec()
        self.cloud_two.updatec2()
        self.score()
        self.obstacles_manager.update(self.game_speed,self)
        
    def draw(self):
        
        self.clock.tick(FPS)
        if self.points <= 2000:
            self.screen.fill((255, 255, 255))
        else:
            self.screen.fill((0,0,0))
        self.draw_background()
        self.player.draw(self.screen)
        self.cloud.drawc(self.screen)
        self.cloud_two.drawc2(self.screen)
        self.score()
        self.obstacles_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
