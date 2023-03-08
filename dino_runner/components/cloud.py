
import random
from dino_runner.utils.constants import CLOUD,SCREEN_WIDTH

class Cloud1():
    def __init__(self):
        self.image = CLOUD
        self.x = SCREEN_WIDTH + random.randint(1,1000)
        self.y = random.randint(10,60)
        self.width = self.image.get_width()
        self.game_speed = 4
        
    def update1(self):
        self.x -= self.game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(1,1000)
            self.y = random.randint(10,60)
            
    def draw1(self,screen):
        screen.blit(self.image,(self.x,self.y))
        
class Cloud2():
    def __init__(self):
        self.image = CLOUD
        self.x = SCREEN_WIDTH + random.randint(1,500)
        self.y = random.randint(40,60)
        self.width = self.image.get_width()
        self.game_speed = 5
        
    def update2(self):
        self.x -= self.game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(1,500)
            self.y = random.randint(40,60)
            
    def draw2(self,screen):
        screen.blit(self.image,(self.x,self.y))
class Cloud3():
    def __init__(self):
        self.image = CLOUD
        self.x = SCREEN_WIDTH + random.randint(500,1000)
        self.y = random.randint(40,60)
        self.width = self.image.get_width()
        self.game_speed = 5
        
    def update3(self):
        self.x -= self.game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(500,1000)
            self.y = random.randint(40,60)
            
    def draw3(self,screen):
        screen.blit(self.image,(self.x,self.y))
class Cloud4():
    def __init__(self):
        self.image = CLOUD
        self.x = SCREEN_WIDTH + random.randint(500,1000)
        self.y = random.randint(20,40)
        self.width = self.image.get_width()
        self.game_speed = 4
        
    def update4(self):
        self.x -= self.game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(500,1000)
            self.y = random.randint(20,40)
            
    def draw4(self,screen):
        screen.blit(self.image,(self.x,self.y))