import pygame
import random

from dino_runner.utils.constants import HEART_TYPE,SMALL_CACTUS, LARGE_CACTUS, BIRD, SHIELD_TYPE, HAMMER_TYPE
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import bird

class Obstacle_Manager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                cactus = Cactus(SMALL_CACTUS, 325)
                self.obstacles.append(cactus) 
            elif random.randint(0, 2) == 1:
                Lcactus = Cactus(LARGE_CACTUS, 300)
                self.obstacles.append(Lcactus)
            elif random.randint(0, 2) == 2:
                Bird = bird(BIRD)
                self.obstacles.append(Bird)


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            
            if game.player.dino_rect.colliderect(obstacle.rect): 
                if not game.player.type == SHIELD_TYPE and not game.player.type == HAMMER_TYPE:   
                    game.heart_manager.reduce_heart()
                if game.player.type == SHIELD_TYPE and game.player.type == HAMMER_TYPE:
                    self.obstacles.remove(obstacle)
                if not game.player.type == SHIELD_TYPE and not game.player.type == HAMMER_TYPE and game.player.type == HEART_TYPE:
                    game.more_manager.more_heart()
                    self.obstacles.remove(obstacle) 
                if  game.heart_manager.heart_count < 1:    
                    pygame.time.delay(1000)
                    game.death_count += 1
                    game.playing = False
                    break
                else:
                    self.obstacles.remove(obstacle)
                
                    
                    
                

    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
