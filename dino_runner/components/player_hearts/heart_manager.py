from dino_runner.components.player_hearts.heart import Heart
from dino_runner.utils.constants import LIVES,HEART_MORE

class HeartManager:
    def __init__(self):
        self.heart_count = LIVES
        self.more_heart = HEART_MORE
        
    def reduce_heart(self):
        self.heart_count -= 1 + HEART_MORE
        
    def more_heart(self):
        self.more += 1
        
    def draw(self,screen):
        x_position = 10
        y_position = 20
        
        for counter in range(self.heart_count):
            heart = Heart(x_position,y_position)
            heart.draw(screen)
            x_position += 30
            
    def reset_heart(self):
        self.heart_count = LIVES
    