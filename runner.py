
import pygame
from sys import exit
import random


class Obstacle (pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == "fly":
            fly_surface1 = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
            fly_surface2 = pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()
            self.frames = [fly_surface1,fly_surface2]
            y_pos = 210
        else:
            snail_surface1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            snail_surface2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_surface2,snail_surface1]
            y_pos = 300
        self.animation_index = 0 
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (random.randint(900,1200),y_pos))
    def animation(self):
        self.animation_index = 0.1
        
        if self.animation_index == len(self.frames):
            print("anim")
            self.animation_index = 0
             
        self.image = self.frames[int(self.animation_index)]
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
    def update(self):
        self.animation()
        self.rect.x -= 6
        self.destroy()
   
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_surface1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
        player_surface2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
        self.player_walk = [player_surface2,player_surface1]
        self.player_index = 0
        self.player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()
        self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
        self.jump_sound.set_volume(0.03)
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.player_gravity = 0
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_SPACE] and self.rect.bottom >= 300:
            self.player_gravity = -20
            self.jump_sound.play()
    def apply_gravity(self):
        self.player_gravity += 1
        self.rect.y += self.player_gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    def animation(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score : {current_time}',False,(64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)
    return current_time
def collision (player_rect,obstacles_rect_list):
    if obstacles_rect_list:
        for obstacle_rect in obstacles_rect_list:
           if player_rect.colliderect(obstacle_rect):
               return False
    return True
def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_ground,False):
        obstacle_ground.empty()
        return False
    else:
        return True   
def player_anim():
    global player_surface
    global player_index
    
    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surface = player_walk[int(player_index)]
def obstacle_movement(obstacle_rect_list):
    if obstacle_rect_list:
        for obstacle_rect in obstacle_rect_list:
            obstacle_rect.x -= 5
            
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface,obstacle_rect)
            else:
                screen.blit(fly_surface,obstacle_rect)
            
        
        obstacle_rect_list = [obstacle for obstacle in obstacle_rect_list if obstacle.x > -110]
        
        return obstacle_rect_list
    else: 
        return []
pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.05)
bg_music.play(loops = -1)
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

game_activate = False
running = True
start_time = 0
score = 0


sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
text_surface = test_font.render("my game", False ,(64,64,64))
text_rect = text_surface.get_rect(midbottom = (400,100))

obstacle_ground = pygame.sprite.Group()
snail_surface1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_surface2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snail_frame = [snail_surface2,snail_surface1]
snail_index = 0
snail_surface = snail_frame[snail_index]
fly_surface1 = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()
fly_surface2 = pygame.image.load("graphics/Fly/Fly2.png").convert_alpha()
fly_frame = [fly_surface2,fly_surface1]
fly_index = 0
fly_surface = fly_frame[fly_index]
obstacle_rect_list = []

player = pygame.sprite.GroupSingle()
player.add(Player())
player_surface1 = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_surface2 = pygame.image.load("graphics/Player/player_walk_2.png").convert_alpha()
player_walk = [player_surface2,player_surface1]
player_jump = pygame.image.load("graphics/Player/jump.png").convert_alpha()
player_index = 0
player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom =(80,300))
player_stand = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
player_stand_scaled = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect =player_stand_scaled.get_rect(center = (400,200))
Instruction = test_font.render("Game Over",False,(64,64,64))
Instruction_rect = Instruction.get_rect(center = (400,80))
press_space = test_font.render("Press space",False,(64,64,64))
press_space_rect =press_space.get_rect(center =(400,330))

player_gravity = 0

timer = pygame.USEREVENT +1
pygame.time.set_timer(timer,1400)

snail_anim_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_anim_timer,500)

fly_anim_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_anim_timer,250)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_activate == False:
                game_activate = True
                # snail_rect.x = 800
                start_time = pygame.time.get_ticks()
                start_time = int(start_time / 1000)
        if game_activate == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20 
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
        if game_activate == True:
            if event.type == timer:
                obstacle_ground.add(Obstacle(random.choice(['fly','snail','snail','snail'])))
                # if random.randint(0,2):
                #     obstacle_rect_list.append(snail_surface.get_rect(midbottom = (random.randint(900,1100),300)))
                # else:
                #     obstacle_rect_list.append(fly_surface.get_rect(midbottom = (random.randint(900,1100),200)))
            if event.type == snail_anim_timer:
                if snail_index == 0:
                    snail_index = 1
                else:
                    snail_index = 0
                snail_surface = snail_frame [snail_index]
            if event.type == fly_anim_timer:
                if fly_index == 0:
                    fly_index = 1
                else:
                    fly_index = 0
                fly_surface = fly_frame [fly_index]
                
    if game_activate:
        screen.blit(sky_surface,(0,0))         
        screen.blit(ground_surface,(0,300))
        
        # pygame.draw.rect(screen,"#c0e8ec",text_rect)
        # screen.blit(text_surface,text_rect)
        score = display_score()
        # snail_rect.x -= 6
        # if snail_rect.right <= 0 :snail_rect.left = 800
        # screen.blit(snail_surface,snail_rect)
        
        # player_gravity = player_gravity + 1
        # player_rect.y += player_gravity
        # if player_rect.bottom>=300:
        #     player_rect.bottom = 300
        # player_anim()
        # screen.blit(player_surface,player_rect)
        player.draw(screen)
        player.update()
        
        obstacle_ground.draw(screen)
        obstacle_ground.update()
        
        # obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        # if snail_rect.colliderect(player_rect):
        #     game_activate = False
        game_activate = collision_sprite()
        # game_activate = collision(player_rect,obstacle_rect_list)
        
    else:   
        screen.fill((94,129,162))
        screen.blit(player_stand_scaled,player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom=(80,300)
        player_gravity = 0
        
        score_massage = test_font.render(f'Your score : {score}',False,(64,64,64))
        score_massage_rect = score_massage.get_rect(center=(400,330))
        if score == 0:
            screen.blit(press_space,press_space_rect)
        else:
            screen.blit(Instruction,Instruction_rect)
            screen.blit(score_massage,score_massage_rect)
    pygame.display.update()
    clock.tick(60) 
    
