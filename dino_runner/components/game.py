import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaurio import Dinosaurio 
from dino_runner.components.cloud import Cloud1,Cloud2,Cloud3,Cloud4
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.heart_manager import HeartManager



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
        self.cloud1 = Cloud1()
        self.cloud2 = Cloud2()
        self.cloud3 = Cloud3()
        self.cloud4 = Cloud4()
        self.obstacles_manager=ObstacleManager()
        self.heart_manager = HeartManager()
        self.points = 0
        self.font = pygame.font.Font('freesansbold.ttf',20)
        
    def score(self):
        self.points,self.game_speed
        self.points+=1 
        if self.points % 500 == 0:
            self.game_speed+=0.5
        
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
        self.cloud1.update1()
        self.cloud2.update2()
        self.cloud3.update3()
        self.cloud4.update4()
        self.score()
        self.obstacles_manager.update(self.game_speed,self)
        
    def draw(self):
        
        self.clock.tick(FPS)
        if self.points <= 800:
            self.screen.fill((255, 255, 255))
        else:
            self.screen.fill((0,0,0))
        self.draw_background()
        self.player.draw(self.screen)
        self.cloud1.draw1(self.screen)
        self.cloud2.draw2(self.screen)
        self.cloud3.draw3(self.screen)
        self.cloud4.draw4(self.screen)
        self.score()
        self.obstacles_manager.draw(self.screen)
        self.heart_manager.draw(self.screen)
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
