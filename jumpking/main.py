import pygame
import os
from random import *

pygame.init()

screen_width = 600
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("Jumpking By Orensi")  #게임 이름

current_path = os.path.dirname(__file__) # 상대경로 설정



# 이미지 로딩


background_01_underground = pygame.image.load(os.path.join(current_path, 'images/background_01_underground.jpg'))




character = pygame.image.load(os.path.join(current_path, 'images/character.png'))



def imageload(src, type="png"):
    global current_path
    return pygame.image.load(os.path.join('images/{}.{}'.format(src, type)))



# 블록 로딩

blocks_img = {
    1 : imageload('block_1_0')
}


backgrounds_img = {
    1 : imageload('background_02_underground', 'jpg'),
    2 : background_01_underground,
    3 : imageload('background_03_underground', 'jpg'),
    4 : imageload('background_04_underground', 'jpg'),
    5 : imageload('background_05_underground', 'jpg'),


}








character_xpos = 0
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

# 스테이지

stage = 1




# 중력 가속도

earth_gravity = 9.8 # 9.8m/s^2

start_acceleration = 0
acceleration = 0




# 중요 : [xpos, ypos , designtype]
map_data = {
    1 : [[100, 600, 1  ], [300, 400, 1], [400,200,1], [100, 150, 1]],

    2 : [[200, 550, 1  ], [400, 300, 1], [0,100,1]],

    3 : [[200, 550, 1  ], [400, 300, 1], [0,100,1]],

    4 : [[300, 700, 1], [300, 400, 1], [300, 100, 1],  [570, 220, 1],],

    5 : [[300, 700, 1],  [300, 100, 1],  [540, 220, 1], [100, 420, 1]],

    






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









def change_stage(plusminus):
    global stage
    if(plusminus == 1):
        stage += 1

    elif(plusminus == -1):
        stage -= 1







def move_character_x(movetype):
    global character_xpos, character_ypos, tox

    if(movetype == 0):
        tox = 0

    if(movetype == -1):
        tox -= 1
    
    if(movetype == 1):
        tox += 1
        





def blocks_blit():
    global stage, blocks_img, map_data, screen

    for i in range(len(map_data[stage])):
       
        current_map_data = map_data[stage][i]
        

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
    global character_fixed, acceleration, canjump
    
  

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
            block_touched = True
            acceleration = 0
            if(character_rect.bottom > block_rect.top):
                character_ypos = block_rect.top - 80
             

        else:
            pass
            
           
            
    

   
            
            
    
    if(block_touched == True ):
        character_fixed = True
        is_character_jumping = False
        canjump = True
        
        
    elif(block_touched == False   ):
        character_fixed = False
        #print(randint(1,2))


            

        
        

















pygame.time.set_timer(pygame.USEREVENT + 1, 10, -1)
pygame.time.set_timer(pygame.USEREVENT + 2, 10, -1)


Clock = pygame.time.Clock()



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

            if(event.key == pygame.K_LEFT):
                move_character_x(-1)
            if(event.key == pygame.K_RIGHT):
                move_character_x(1)

        
        if(event.type == pygame.KEYUP):

            if(event.key == pygame.K_SPACE):
                check_collision()
                print(is_character_jumping)
                print(character_fixed)
                if(character_fixed or not is_character_jumping):

                    is_jump_charging = False

                    is_character_jumping = True
                    character_fixed = False
                    acceleration = jump_charged * 0.06
                    jump_charged = 0
                    character_ymove()

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






    


    screen.blit(character, (character_xpos, character_ypos))
    

   

    
    screen.blit(font.render('Stage {}'.format(stage), True, (0,255,0)), (0,0))
    screen.blit(font.render('{:.2}%'.format((stage-1) / 99 * 100), True, (0,255,0)), (0,40))



    
    
    jump_charge_blit()



    # 화면 업데이트
    pygame.display.update()

# Pygame 종료
pygame.quit()