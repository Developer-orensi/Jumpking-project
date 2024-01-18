import pygame
import os
from random import *

pygame.init()

screen_width = 600
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("우상의 게임")  #게임 이름

current_path = os.path.dirname(__file__) # 상대경로 설정



# 이미지 로딩


background_01_underground = pygame.image.load(os.path.join(current_path, 'background_01_underground.jpg'))




character = pygame.image.load(os.path.join(current_path, 'character.png'))


character_xpos = 0
character_ypos = screen_height - 120
tox = 0
toy = 0

jump_charged = 0

is_jump_charging = False

is_character_jumping = False

pushed_jump = False

false = False
true = True



# 스테이지

stage = 1




# 중력 가속도

earth_gravity = 9.8 # 9.8m/s^2

start_acceleration = 0
acceleration = 0





# 폰트 로딩

font = pygame.font.Font(None, 40)


def character_ymove():
    global is_character_jumping
    global character_ypos
    global jump_charged
    global start_acceleration, acceleration

    if(is_character_jumping):
        if(character_ypos > screen_height - 120):
            character_ypos = screen_height - 120
            return
        
        character_ypos -= acceleration
        acceleration -= earth_gravity * 0.007

        if(character_ypos > screen_height - 120):
            character_ypos = screen_height - 120
            return
        




def character_jump():
    pass



def jump_charge_blit():
    global jump_charged
    global screen
    if(jump_charged < 15):
 
        screen.blit(font.render('Jump : '+'|' * jump_charged, True, (0,255,0)), (0,80))
    elif(jump_charged < 40):
        screen.blit(font.render('Jump : '+'|' * jump_charged, True, (255,255,0)), (0,80))

    else:
        screen.blit(font.render('Jump : '+'|' * jump_charged, True, (255,0,0)), (0,80))




pygame.time.set_timer(pygame.USEREVENT + 1, 10, -1)
pygame.time.set_timer(pygame.USEREVENT + 2, 10, -1)

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_jump_charging = True
                pushed_jump = true

        
        if(event.type == pygame.KEYUP):
            if event.key == pygame.K_w:
                toy = 0

            if(event.key == pygame.K_SPACE):
                is_jump_charging = False

                is_character_jumping = True
                acceleration = jump_charged * 0.2

        
        if(event.type ==  pygame.USEREVENT + 1):
            if(jump_charged > 0 and not is_jump_charging):
                jump_charged -= 1
        
        if(event.type == pygame.USEREVENT + 2):
            
            if(jump_charged >=49):
                pushed_jump = false
            if(is_jump_charging and jump_charged < 50 and pushed_jump):
                jump_charged += 1

                
            if(is_jump_charging and jump_charged < 50 and not pushed_jump and jump_charged > 30):
                if(randint(0, 10) == 8):
                    jump_charged -= 1
            
            


    # 배경 그리기
    screen.blit(background_01_underground, (0,0))






                

    # ypos 더하기
    character_ypos += toy

    character_ymove()

    


    screen.blit(character, (character_xpos, character_ypos))
    

   

    
    screen.blit(font.render('Underground', True, (0,255,0)), (0,0))
    screen.blit(font.render('0.00%', True, (0,255,0)), (0,40))



    
    
    jump_charge_blit()



    # 화면 업데이트
    pygame.display.update()

# Pygame 종료
pygame.quit()