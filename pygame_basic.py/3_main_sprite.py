import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480  # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정(제목)
pygame.display.set_caption("Game_made by jihwan") # 게임 이름 작성

# 배경 이미지 불러오기 (변수지정, 경로에 있는 파일을 불러옴)
background = pygame.image.load("/Users/joojihwan/Desktop/Python_Sources/pygame_basic.py/background_img.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/joojihwan/Desktop/Python_Sources/pygame_basic.py/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]   # 캐릭터의 가로 크기
cterharac_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (x축_가로)
character_y_pos = screen_height - cterharac_height  # 화면 세로 크기 가장 아래에 위치 (y축_세로)

# 이벤트 루프
running = True # 게임이 진행중인가? 확인하는것
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # running이 false로 변경되어 게임이 진행중이 아님

    screen.blit(background, (0,0))  # 배경 그리기_background 위치 설정(좌표)
    # blit이 background 이미지를 그려주는 역활을 함

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기_character 위치 설정(좌표)
    # blit이 character 이미지를 그려주는 역활을 함

    pygame.display.update() # 게임화면을 다시 그리기!
    # 매번 프레임마다 화면을 계속 새로 그려주는 동작을 해야한다.

# pygame 종료
pygame.quit()
