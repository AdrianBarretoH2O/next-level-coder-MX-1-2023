import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaurio import Dinosaur 
from dino_runner.components.cloud import Cloud1,Cloud2,Cloud3,Cloud4
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.heart_manager import HeartManager
from dino_runner.components.power.power_manager import PowerUpManager
score_COLOR = pygame.Color(255, 0, 0)
record_COLOR = pygame.Color(255, 0, 0)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 430
        self.player = Dinosaur()
        self.cloud1 = Cloud1()
        self.cloud2 = Cloud2()
        self.cloud3 = Cloud3()
        self.cloud4 = Cloud4()
        self.obstacles_manager=ObstacleManager()
        self.heart_manager = HeartManager()
        self.power_up_manager = PowerUpManager()
        self.score = 0
        self.runnig = False
        self.points =0
        self.best_score = 0
        self.font = pygame.font.Font('freesansbold.ttf',20)
        self.death_count = 0
        
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.game_over = True
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
        
    

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
        self.obstacles_manager.update(self.game_speed, self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        self.update_score()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        if self.score <= 800:
            self.screen.fill((255, 255, 255))
        elif self.score <= 2000:
            self.screen.fill((255, 0, 255))
        elif self.score <= 10000:
            self.screen.fill((255, 255, 0))
        else:
            self.screen.fill((0,0,0))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacles_manager.draw(self.screen)
        self.draw_score()
        self.cloud1.update1()
        self.cloud2.update2()
        self.cloud3.update3()
        self.cloud4.update4()
        self.power_up_manager.draw(self.screen)
        self.heart_manager.draw(self.screen)
        pygame.display.update() #update objects inside
        pygame.display.flip() #display/show

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
        
        
 
                
    def update_score(self):
        self.score += 1

        if self.death_count >= 0:
            if self.score % 500 == 0 and self.game_speed < 60:
                self.game_speed += 1
        self.player.check_invincibility()
        
        if self.score >= self.best_score:
            self.best_score = self.score
                        
    def draw_score(self):
        self.generate_text(f"Score:{self.score}", 850, 15, 10, score_COLOR)
        self.generate_text(f"Best score:{self.best_score}", 850, 35, 10, record_COLOR)
    
   
    
    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()
    
    def generate_text(self, text, half_screen_width, half_screen_heigh, size, color):
        
        font = pygame.font.Font('freesansbold.ttf', size)
        text = font.render(f"{text}", True, color)
        text_rec = text.get_rect()
        text_rec.center = (half_screen_width, half_screen_heigh)
        self.screen.blit(text, text_rec)
    
    def show_menu(self):
        print(self.death_count)
        self.screen.fill((255, 255, 255))
        half_screen_heigh = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.generate_text("Press any key to play...",  550,550 // 2, 45, SCORE_COLOR)
            self.screen.blit(ICON, (half_screen_width - 50, half_screen_heigh + 40))
        else:
            self.generate_text("You Died",  half_screen_width , half_screen_heigh - 170, 70, SCORE_COLOR)
            self.generate_text(f"Deaths: {self.death_count}", half_screen_width, half_screen_heigh , 40, SCORE_COLOR)
            self.generate_text(f"Score: {self.score}",  half_screen_width, half_screen_heigh+50, 45, SCORE_COLOR)
            self.generate_text(f"Best Score: {self.best_score}", half_screen_width, half_screen_heigh + 100, 47, SCORE_COLOR)
            self.generate_text("Press any key to restart", half_screen_width, half_screen_heigh +170, 50, SCORE_COLOR)
            self.screen.blit(DEAD, ( half_screen_width - 40, half_screen_heigh - 120))
            self.screen.blit(RESET, ( half_screen_width - 35, half_screen_heigh + 210))
        pygame.display.update()
        self.handle_events_on_menu()
        
        
    