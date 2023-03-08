import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS,BIRD,LARGE_CACTUS,CLOUD
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.cloud import Cloud1,Cloud2,Cloud3,Cloud4

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        
    def update(self,game_speed,game):
      
        if len(self.obstacles) == 0:
            obstacle_it = random.randint(0,2)
            if obstacle_it == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif obstacle_it ==1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif obstacle_it == 2:    
                self.obstacles.append(Bird(BIRD))
            
        
        for obstacle in self.obstacles:
            obstacle.update(game_speed,self.obstacles)
            # agarrar el martillo y hacer inmune a los obstacles
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(300)
                game.playing = False
                break    
    
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)