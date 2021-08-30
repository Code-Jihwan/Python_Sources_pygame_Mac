import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정(제목)
pygame.display.set_caption("Game_made by jihwan") # 게임 이름 작성

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기 (변수지정, 경로에 있는 파일을 불러옴)
background = pygame.image.load("/Users/joojihwan/Desktop/Python_Sources/pygame_basic.py/background_img2.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/joojihwan/Desktop/Python_Sources/pygame_basic.py/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]   # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (x축_가로)
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래에 위치 (y축_세로)

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 enemy 캐릭터 만들기
enemy = pygame.image.load("/Users/joojihwan/Desktop/Python_Sources/pygame_basic.py/enemy.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]   # 적 캐릭터의 가로 크기
enemy_height = enemy_size[1]  # 적 캐릭터의 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (x축_가로)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 화면 세로 크기 가장 아래에 위치 (y축_세로)

# 이벤트 루프
running = True # 게임이 진행중인가? 확인하는것
while running:
    dt = clock.tick(120) # 게임화면의 초당 프레임 수를 설정
   # print("fps : " + str(clock.get_fps())) # 프레임수 확인
   # 프레임이 달라진다고해서 이동 속도가 달라지면 안됨!
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # running이 false로 변경되어 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키보드 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로 이동
                to_x -= character_speed # to_x = to_x - 5
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로 이동
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위쪽으로 이동
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래쪽으로 이동
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크 (colliderect : 사각형 기준으로 충돌이 있는지 확인하는 함수)
    if character_rect.colliderect(enemy_rect):
        print("창에 맞았어요")
        running = False


    screen.blit(background, (0,0))  # 배경 그리기_background 위치 설정(좌표)
    # blit이 background 이미지를 그려주는 역활을 함

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기_character 위치 설정(좌표)
    # blit이 character 이미지를 그려주는 역활을 함

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 캐릭터  그리기_enemy 위치 설정(좌표)
    # blit이 enemy 이미지를 그려주는 역활을 함

    pygame.display.update() # 게임화면을 다시 그리기!
    # 매번 프레임마다 화면을 계속 새로 그려주는 동작을 해야한다.

# pygame 종료
pygame.quit()
