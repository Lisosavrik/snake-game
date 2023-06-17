import pygame 
pygame.init()
timer = pygame.time.Clock()
import random 

size = width, height = 400, 300
MAIN_COLOR = (220, 220, 240)
PURPLE_COLOR = (186, 85, 211)
YELLOW_COLOR = (0, 100, 100)
RED_COLOR = (100, 0, 0)
COLOR = (50, 150, 250)

square_size = 20
rows =  int(height / square_size)
columns = int((width / square_size))

screen = pygame.display.set_mode(size)
title = pygame.display.set_caption('Глист🪱')
snake = []
last = []
snake_before = []


k = 0.01
food_location = [0, 0]

def add_block(pos: "list(int)"):
    snake.insert(0, pos)
    snake_before.insert(0, pos)



def regist_food_locaton():
    food_location[0] = int(random.uniform(0, columns))
    food_location[1] = int(random.uniform(0, rows))




def draw_food():
    x, y = food_location[0] * square_size, food_location[1] * square_size
    pygame.draw.rect(screen, COLOR, [x, y, square_size, square_size])



def draw_background():
    squares_in_row = int(columns / 2)

    even = 0
    odd = 1
    for row in range(0, rows, 2):
        y1 = even * square_size
        y2 = odd * square_size  

        for square in range(squares_in_row):
            x1 =  (square_size * square * 2) + square_size
            x2 = square_size * square  * 2
            
            pygame.draw.rect(screen, PURPLE_COLOR, [x1, y1, square_size, square_size])
            pygame.draw.rect(screen, PURPLE_COLOR, [x2, y2, square_size, square_size])
        even += 2
        odd += 2


def draw_snake(before):
    for i, blok in enumerate(snake):
        from_block = snake_before[i]

        to_x = blok[0]
        to_y = blok[1]
        
        from_x = from_block[0]
        from_y = from_block[1]


        from_x = from_x + (to_x - from_x) * k
        from_y = from_y + (to_y - from_y) * k

        from_block[0], from_block[1] = from_x, from_y

        pygame.draw.rect(screen, YELLOW_COLOR, [int(from_x * square_size), int(from_y * square_size), square_size, square_size])

def make_head():
    add_block([6, 7])
    add_block([5, 7])


# def linear_interpolation(coordination, dir, k):
#     match dir[0]:
#         case 1:



make_head()

delta_time = 0
dir = [1, 0]

regist_food_locaton()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and last_saved_dir[1] != -1:
                dir[0] = 0
                dir[1] = 1
            if event.key == pygame.K_UP and last_saved_dir[1] != 1:
                dir[0] = 0
                dir[1] = -1

            if event.key == pygame.K_RIGHT and last_saved_dir[0] != -1:
                dir[0] = 1
                dir[1] = 0
            if event.key == pygame.K_LEFT and last_saved_dir[0] != 1:
                dir[0] = -1
                dir[1] = 0




    screen.fill(MAIN_COLOR)
    draw_background()
    delta_time += timer.tick()

    1
    if delta_time >= 600:
        x_dir, y_dir = dir[0], dir[1]
        head = snake[-1]
        head = [head[0] + x_dir, head[1] + y_dir]
        last_saved_dir = [*dir] 
        snake.append(head)

        if snake[-1] == food_location:
            regist_food_locaton()
            snake_before.insert(0, snake[0])
        else:
            snake.pop(0)


        



        last_saved_dir = [*dir]
        delta_time = 0


    
    draw_food()

    draw_snake(snake_before)
    pygame.display.flip()
    # snake.clear()
    1


