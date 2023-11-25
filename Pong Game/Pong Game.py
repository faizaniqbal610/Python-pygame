import pygame

pygame.init()

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong by Faizan")
FPS = 60

BALL_RADIUS = 7

WHITE = (255, 255, 255)
GRAY = (32, 33, 35)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

SCORE_FONT = pygame.font.SysFont("comicsans", 50)

class Paddle:
    COLOR = WHITE
    VAL = 4
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))
    
    def move(self, up=True):
        if up:
            self.y -= self.VAL
        else:
            self.y += self.VAL

class Ball:
    MAX_VAL = 5
    COLOR = WHITE

    def __init__(self, x, y, radius) -> None:
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_val = self.MAX_VAL
        self.y_val = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)
    
    def move(self):
        self.x += self.x_val
        self.y += self.y_val
    
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_val = 0
        self.x_val *= -1

def draw(win, paddles, ball, left_score, right_score):
    win.fill(GRAY)

    left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
    win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
    win.blit(right_score_text, (WIDTH * (3/4) - right_score_text.get_width()//2, 20))

    for paddle in paddles:
        paddle.draw(win)
    
    pygame.draw.rect(win, WHITE, (WIDTH//2-2, 0, 2, HEIGHT))
    ball.draw(win)

    pygame.display.update()


def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_val *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_val *= -1

    if ball.x_val < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_val *= -1

                middle_y = left_paddle.y + left_paddle.height /2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.y / 2) / ball.MAX_VAL
                y_val = difference_in_y / reduction_factor
                ball.y_val = -1 * y_val

    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_val *= -1

                middle_y = left_paddle.y + left_paddle.height /2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.y / 2) / ball.MAX_VAL
                y_val = difference_in_y / reduction_factor
                ball.y_val = -1 * y_val

def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VAL >=0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VAL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y >=0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)

def main():
    game_exit = False
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH //2, HEIGHT //2, BALL_RADIUS)

    left_score = 0
    right_score = 0

    while not game_exit:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    game_exit = True

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()

    pygame.quit()
    quit()

if __name__ == "__main__":

    main()
