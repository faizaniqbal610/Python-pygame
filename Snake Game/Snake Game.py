import pygame
import random

x = pygame.init()

screen_width = 1000
screen_hight = 600

gray = (32, 33, 35)
red = (226, 80, 90)
green = (25, 195, 125)

gameWindow = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("Snake game by Faizan")
pygame.display.update()

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)

def display_score(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def gro_snake(gameWindow, color, snake_lst, snake_size):
    for x, y in snake_lst:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def gameloop():
    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 55
    snake_size = 20
    food_x = random.randint(0, screen_width/4*7/2)
    food_y = random.randint(0, screen_hight/4*7/2)
    food_size = 20

    fps = 30
    velocity_x = 0
    velocity_y = 0
    speed = 6

    score = 0
    snake_lst = []
    snake_len = 1

    while not exit_game:
        if game_over:
            gameWindow.fill(gray)
            display_score("Game Over! Press Enter to Continue", red, 170, 290)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = +speed
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -speed
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -speed
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = +speed
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 16 and abs(snake_y - food_y) < 16:
                score +=1
                snake_len += 5
                # print("score is", score)
                food_x = random.randint(40, screen_width/4*7/2)
                food_y = random.randint(40, screen_hight/4*7/2)


            gameWindow.fill(gray)
            display_score("score is: "+str(score), red, 10, 10)
            pygame.draw.rect(gameWindow, green, [food_x, food_y, food_size, food_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_lst.append(head)
            # print(snake_lst)

            if len(snake_lst)>snake_len:
                del snake_lst[0]

            if head in snake_lst[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_hight:
                game_over = True
                
            gro_snake(gameWindow, red, snake_lst, snake_size)
            # pygame.draw.rect(gameWindow, red, [snake_x, snake_y, snake_size, snake_size])

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

gameloop()
