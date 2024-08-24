import pygame
import os
from random import *

pygame.init()

screen_width = 600
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("JumpQueen")  #게임 이름

current_path = os.path.dirname(__file__) # 상대경로 설정



# 이미지 로딩


background_01_underground = pygame.image.load(os.path.join(current_path, 'images/background_01_underground.jpg'))




character = pygame.image.load(os.path.join(current_path, 'images/character.png'))



def imageload(src, type="png"):
    global current_path
    return pygame.image.load(os.path.join('images/{}.{}'.format(src, type)))



# 블록 로딩

blocks_img = {
    1 : imageload('block_1_0'),
    2 : imageload('block_2'),
    3 : imageload('block_3'),





    51 : imageload('block_51'),

}


backgrounds_img = {
    1 : imageload('background_02_underground', 'jpg'),
    2 : background_01_underground,
    3 : imageload('background_03_underground', 'jpg'),
    4 : imageload('background_04_underground', 'jpg'),
    5 : imageload('background_05_underground', 'jpg'),
    6 : imageload('background_06_underground', 'jpg'),
    7 : imageload('background_06_underground', 'jpg'),
    8 : imageload('background_06_underground', 'jpg'),
    9 : imageload('background_06_underground', 'jpg'),
    10 : imageload('background_06_underground', 'jpg'),
    11 : imageload('background_06_underground', 'jpg'),
    12 : imageload('background_06_underground', 'jpg'),
    13 : imageload('background_06_underground', 'jpg'),
    14 : imageload('background_06_underground', 'jpg'),
    15 : imageload('background_06_underground', 'jpg'),
    16 : imageload('background_06_underground', 'jpg'),
    17 : imageload('background_06_underground', 'jpg'),


}








character_xpos = 50
character_ypos = screen_height - 120
tox = 0
toy = 0

character_fixed = True

jump_charged = 0

is_jump_charging = False

is_character_jumping = False

pushed_jump = False

false = False
true = True


canjump = True

super_activated = False

super_cooldown = 0

#바람
wind_exist = False
wind_direction = 0

# 얼음(밟으면 깨짐)
iceblock_cooldown = 0
iceblock_exist = True

iceblock_touched = False


# 스테이지

stage = 12


time = 90

# 중력 가속도

earth_gravity = 9.8 # 9.8m/s^2

start_acceleration = 0
acceleration = 0

# 궁극기
ultimate_exist = False
ultimate_cooldown = 0

ultimate_available = [15, 18, 20]



stage_5_added = False
stage_10_added = False
stage_15_added = False
stage_20_added = False





# 중요 : [xpos, ypos , designtype]
map_data = {
    1 : [[100, 600, 1  ], [300, 400, 1], [400,200,1], [100, 150, 1]],

    2 : [[200, 550, 1  ], [400, 300, 1], [0,100,1]],

    3 : [[200, 550, 1  ], [400, 300, 1], [0,100,1]],

    4 : [[300, 700, 1], [300, 400, 1], [300, 100, 1],  [570, 220, 1],],

    5 : [[300, 700, 1],  [300, 100, 1],  [540, 220, 1], [100, 420, 1]],

    6 : [[300, 700, 2],  [310, 400, 2],  [320, 100, 2], [-10, 100, 2]],

    7 : [[90, 600, 2], [130, 500, 2], [340,400,2],  [500, 240, 2], [500, 81, 2]],

    8 : [ [400, 300, 2], [400, 450, 2], [590, 145, 1]],

    9 : [[444, 456, 1], [222, 222, 2], [111, 111, 1]],

    10 : [[444, 456, 1], [222, 222, 2], [111, 111, 1], [500, 300, 51]],

    11 : [ [300, 430, 51], [120, 270, 51],  [400, 120, 51]],

    12 : [ [480, 680, 2],[300, 540, 1] , [0, 530, 51], [0, 470, 51], [0, 410, 51], [0, 350, 51], [50,680,2], [55, 300, 2], [300, 240, 1], [590, 160, 51], [590, 80, 51]],

    13 : [[0,0,1], [500, 600, 2], [100, 340, 1], [300, 600, 1], [590, 660, 51] ],

    14 : [[0, 670, 1], [214, 407, 3], [206, 142, 3]],

    15 : [[0, 680, 1], [270, 160, 3]],

    16 : [[500, 540, 2], [269, 425, 1], [85, 263, 3]],

    17 : []

    






}







# 폰트 로딩

font = pygame.font.Font(None, 40)


def character_ymove():
    global is_character_jumping
    global character_ypos
    global jump_charged, character_fixed
    global start_acceleration, acceleration

    if(is_character_jumping or not character_fixed):
        #print("{}{}".format(is_character_jumping, character_fixed))
        
     

        


       

        character_ypos -= acceleration

        if(acceleration > -2):
            acceleration -= earth_gravity * 0.0015



        if(character_ypos > screen_height - 80):
            if(stage == 1):

                character_ypos = screen_height - 80
                is_character_jumping = False
                character_fixed = True
                return
            else:

                change_stage(-1)
                character_ypos = 0
        
        
        if(character_ypos < 0):
            if(stage != 99):
                character_ypos = screen_height - 80
                change_stage(1)



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



def stage_change_setting():
    global stage, acceleration, earth_gravity, wind_exist, wind_direction
    global stage_10_added, stage_5_added, stage_15_added, stage_20_added, time

    if(stage == 12):
        earth_gravity = 9.8 + 4.9

    else:
        earth_gravity = 9.8
        



    if(stage == 13):
        wind_exist = True

        wind_direction = 1

    elif(stage == 10):
        wind_exist = True

        wind_direction = 0.2

    elif(stage == 14):
        wind_exist = True

        wind_direction = -1.5

    elif(stage == 15):
        wind_exist = True
        wind_direction = 0.2

    elif(stage == 16):
        wind_exist = True
        wind_direction = 2




    else:
        wind_exist = False


    if(stage == 5 and stage_5_added == False):

        stage_5_added = True
        time += 40
    if(stage == 10 and stage_10_added == False):

        stage_10_added = True
        time += 60

    if(stage == 15 and stage_15_added == False):

        stage_15_added = True
        time += 80
          
        





def change_stage(plusminus):
    global stage, earth_gravity
    if(plusminus == 1):
        stage += 1








    elif(plusminus == -1):
        stage -= 1



    stage_change_setting()







def move_character_x(movetype):
    global character_xpos, character_ypos, tox

    if(movetype == 0):
        tox = 0

    if(movetype == -1):
        tox -= 1
    
    if(movetype == 1):
        tox += 1
        





def blocks_blit():
    global stage, blocks_img, map_data, screen, iceblock_cooldown, iceblock_exist

    for i in range(len(map_data[stage])):
       
        current_map_data = map_data[stage][i]
        
        if(current_map_data[2] == 3 and iceblock_exist == False):
            screen.blit(font.render('{}'.format(iceblock_cooldown),True,(0,255,0)), (current_map_data[0], current_map_data[1]))


        else:

            screen.blit(blocks_img[current_map_data[2]], (current_map_data[0], current_map_data[1]))

        # 중요 : [xpos, ypos, designtype]


def check_xpos():
    global character_xpos, character_ypos, screen_width

    if(character_xpos < 0):
        character_xpos = 0
    if(character_xpos > screen_width - 40):
        character_xpos = screen_width -40




def check_collision():

    global character, character_xpos, character_ypos, blocks_img, map_data, stage, is_character_jumping
    global character_fixed, acceleration, canjump, iceblock_cooldown, iceblock_exist, iceblock_touched
    
  

    # 지역 변수
    block_touched = False


    character_rect = character.get_rect()
    character_rect.top = character_ypos
    character_rect.left = character_xpos

    
    for i in map_data[stage]:
        current_map_data = i


        

        block_rect = blocks_img[current_map_data[2]].get_rect()
        block_rect.top = current_map_data[1]
        block_rect.left = current_map_data[0]
        
        
 
        if((character_rect.colliderect(block_rect) and (character_rect.bottom <= block_rect.top + 10)) ):
          
            if(current_map_data[2] <= 2):

                block_touched = True
                acceleration = 0
                if(character_rect.bottom > block_rect.top):
                    character_ypos = block_rect.top - 80
            

            elif(current_map_data[2] == 3 and iceblock_exist):

                block_touched = True
                acceleration = 0
                if(character_rect.bottom > block_rect.top):
                    character_ypos = block_rect.top - 80
                # 보정 끝난 후 타이머


                if(iceblock_touched == False):
                    iceblock_touched = True

                    pygame.time.set_timer(pygame.USEREVENT + 3, 1500, 1)







            elif(current_map_data[2] == 51):

                if(acceleration < 2):

                    acceleration = 2
                




        elif(character_rect.colliderect(block_rect) and (character_rect.top <= block_rect.bottom -5)):
            if(current_map_data[2] <= 50):

            
            
            
                if(acceleration > 0 ):

                    acceleration -= 1.6
                character_ypos += 5

            elif(current_map_data[2] == 51):

                if(acceleration < 1.5):

                
                
                    character_ypos -= 5

                    acceleration += 0.1

                # if(acceleration > 0.9):

                #     acceleration -= 0.1
             

        else:
            pass
            
           
            
    

   
            
            
    
    if(block_touched == True ):
        character_fixed = True
        is_character_jumping = False
        canjump = True
        
        
    elif(block_touched == False   ):
        character_fixed = False
        #print(randint(1,2))


            
def environment_effect():
    global character_xpos, wind_exist, wind_direction

    if(wind_exist == True):
        character_xpos += wind_direction * 0.04
        
        







clock = pygame.time.Clock()









pygame.time.set_timer(pygame.USEREVENT + 1, 10, -1)
pygame.time.set_timer(pygame.USEREVENT + 2, 10, -1)


Clock = pygame.time.Clock()


pygame.time.set_timer(pygame.USEREVENT + 6, 3000, 1)


# 메인 루프
running = True
while running:

    clock.tick(540)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_jump_charging = True
                pushed_jump = true

            if(event.key == pygame.K_LEFT):
                move_character_x(-1)
            if(event.key == pygame.K_RIGHT):
                move_character_x(1)
            
            if(event.key == pygame.K_v and stage in ultimate_available):
                # 궁극기
                if(ultimate_cooldown <= 0):
                    
                    acceleration = 50 ** 0.5 * 0.45

                    ultimate_cooldown = 30
                    pygame.time.set_timer(pygame.USEREVENT + 5, 1000, 1)

        
        if(event.type == pygame.KEYUP):

            if(event.key == pygame.K_SPACE):
                #


                check_collision()
         
                if(character_fixed or not is_character_jumping):

                    is_jump_charging = False

                    ultimate_cooldown -= 1

                    is_character_jumping = True 
                    character_fixed = False
                    acceleration = jump_charged ** 0.5 * 0.45
                    jump_charged = 0
                    character_ymove()

                else:
                    jump_charged  = 0

            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                move_character_x(0)
            









        
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

        if(event.type == pygame.USEREVENT + 3):
            iceblock_exist = False
            iceblock_cooldown = 4

            pygame.time.set_timer(pygame.USEREVENT + 4, 1000, 1)
        
        if(event.type == pygame.USEREVENT + 4):
            if(iceblock_cooldown <= 1):
                iceblock_cooldown = 0
                iceblock_exist = True
                iceblock_touched = False
            else:
                iceblock_cooldown -= 1
                pygame.time.set_timer(pygame.USEREVENT + 4, 1000, 1)

        if(event.type == pygame.USEREVENT + 5):
            # 궁극기 쿨다운 -
            if(ultimate_cooldown >= 1):
                ultimate_cooldown -= 1
                pygame.time.set_timer(pygame.USEREVENT + 5, 1000, 1)
            else:
                ultimate_exist = True
                ultimate_cooldown = 0
        
        if(event.type == pygame.USEREVENT + 6):
            if(time > 0):
                time -= 1
                pygame.time.set_timer(pygame.USEREVENT + 6, 1000, 1)

        
        if(event.type == pygame.MOUSEBUTTONDOWN):
            print(pygame.mouse.get_pos())
            


    # 배경 그리기
    screen.blit(backgrounds_img[stage], (0,0))

    # 블록 그리기
    blocks_blit()


    check_collision()

    

    # xpos 더하기

    character_xpos += tox


    # 화면 나감 처리


    check_xpos()



    character_ymove()


    # 추가 처리

    environment_effect()



    


    screen.blit(character, (character_xpos, character_ypos))
    

   

    
    screen.blit(font.render('Stage {}'.format(stage), True, (0,255,0)), (0,0))
   
    if(time >= 30):
   
   
        screen.blit(font.render(' {:01} : {:02}'.format(time//60, time%60), True, (0,255,0)), (0,40))

    if(time < 30 and time >= 11):

        screen.blit(font.render(' {:01} : {:02}'.format(time//60, time%60), True, (255,255,0)), (0,40))

    if(time < 11):

        screen.blit(font.render(' {:01} : {:02}'.format(time//60, time%60), True, (255,0,0)), (0,40))

    




    if(wind_exist):
        if(wind_direction > 0):

            if(wind_direction < 0.5):

                screen.blit(font.render('Wind : >', True, (150, 150,0)), (0,120))

            elif(wind_direction <= 1.5):
                screen.blit(font.render('Wind : >>', True, (200,200,0)), (0,120))

            else:
                screen.blit(font.render('Wind : >>>', True, (255,0,0)), (0,120))




        if(wind_direction < 0):


            if(wind_direction > -0.5):

                screen.blit(font.render('Wind : <', True, (150, 150,0)), (0,120))

            elif(wind_direction >= -1.5):
                screen.blit(font.render('Wind : <<', True, (200,200,0)), (0,120))

            else:
                screen.blit(font.render('Wind : <<<', True, (255,0,0)), (0,120))


            # screen.blit(font.render('Wind : <<', True, (255,255,0)), (0,120))


    if(stage in ultimate_available):
        # 궁극기
        if(ultimate_cooldown <= 0):
            screen.blit(font.render('Ultimate : V', True, (0,255,0)), (0,160))
        else:
            screen.blit(font.render('Ultimate : {}s'.format(ultimate_cooldown), True, (255,255,0)), (0,160))
    
    
    jump_charge_blit()



    # 화면 업데이트
    pygame.display.update()

# Pygame 종료
pygame.quit()
