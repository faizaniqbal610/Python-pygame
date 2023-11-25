import pygame

pygame.init()

WIDTH, HEIGHT = 300, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris Game by Faizan")
FPS = 60

GRAY = (32, 33, 35)
WHITE = (225, 225, 225)


class Grid:
    def __init__(self) -> None:
        self.num_rows = 20
        self.num_coul = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_coul)] for i in range(self.num_rows)]
        print(self.grid)
        self.color = self.get_cell_colors()
    
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_coul):
                print(self.grid[row][column], end=" ")
            print()
    
    def get_cell_colors(self):
        dark_gray = (26, 31, 40)
        green = (47, 230, 23)
        red = (232, 18, 18)
        orange = (226, 116, 17)
        yellow = (237, 234, 4)
        purple = (116, 0, 247)
        cyan = (21, 204, 209)
        blue = (13, 64, 216)

        return [dark_gray, green, red, orange, yellow, purple, cyan, blue]
    
    def draw(self, win):
        for row in range(self.num_rows):
            for column in range(self.num_coul):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size +1, self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(win, self.color[cell_value], cell_rect)
                # pygame.draw.rect(win, WHITE, cell_rect)

def main():
    game_exit = False
    Clock = pygame.time.Clock()

    game_grid = Grid()
    
    # game_grid.grid[0][0] = 1
    # game_grid.grid[3][5] = 4
    # game_grid.grid[17][8] = 7
    game_grid.grid[0][0] = 1
    game_grid.grid[0][1] = 1
    game_grid.grid[0][2] = 1
    game_grid.grid[1][1] = 1

    while not game_exit:
        Clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
        
        WIN.fill(GRAY)
        game_grid.draw(WIN)
        pygame.display.update()
    
    pygame.quit()
    quit()

if __name__ == "__main__":

    main()

