import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING

class Dinosaurio(Sprite):
    POS_X=80
    POS_Y=360
    POS_Y_DUNCKING = 394
    JUMP_VEL = 8.5
    
    def __init__(self):
        self.image=RUNNING[0]
        self.image=DUCKING[0]
        self.image=JUMPING
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x=self.POS_X
        self.dino_rect.y=self.POS_Y
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
    
        
    def update(self,user_input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        
        if self.step_index >= 10:
            self.step_index = 0


        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

            
        
    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x=self.POS_X
        self.dino_rect.y=self.POS_Y
        self.step_index += 1
        
    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x=self.POS_X
        self.dino_rect.y=self.POS_Y_DUNCKING
        self.step_index += 1
        
        
    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 3 # Salto
            self.jump_vel -= 0.5 # Salto, cuando llega a negativo, baja
        if self.jump_vel < -self.JUMP_VEL: # Cuando llega a JUMP_VEL en negativo, este se detiene
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL
            self.dino_rect.y = self.POS_Y
            
            
    def draw(self,screen):
        screen.blit(self.image,(self.dino_rect.x,self.dino_rect.y))
    