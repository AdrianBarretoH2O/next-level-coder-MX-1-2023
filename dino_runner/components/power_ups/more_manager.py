from dino_runner.components.player_hearts.heart import Heart
from dino_runner.utils.constants import HEART_MORE,LIVES

class MoreManager:
    def __init__(self):
        self.more = HEART_MORE
        
    def more_heart(self):
        self.more += 1
            
    def draw(self,screen):
        x_pos_position = 150
        y_pos_position = 20
        for i in range(self.more):
            heart_more = Heart(x_pos_position,y_pos_position)
            heart_more.draw(screen)
                
            
    def reset_heart(self):
        self.more = HEART_MORE