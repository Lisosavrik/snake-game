import pygame 
from pygame import Vector2
from fsutils import resource_path
from window import window
from game_func import GameFunc
from game_logic import GameLogic
from game_values import game_values
from game_palette import palette_1
from theme_menu import ThemeMenu
# import psutil

# ps = psutil.Process()

flag = True
pygame.init()
pygame.mixer.init()

timer = pygame.time.Clock()

def draw_loading():
    theme = ThemeMenu(
        screen=window.screen,
        titles={"loading": "Loading"},
        buttons={},
        pos_title="CENTER"
    )

    theme.create_titles(theme.titles["loading"], palette_1.background_color_3)
    theme.draw_menu(background_color=palette_1.background_color_2)
    pygame.display.flip()


def all_game():
    draw_loading()

    delta_time = 0 
    music = pygame.mixer.Sound(resource_path("mozart.mp3"))
    def start_music():
        music.play()


    columns = int(window.size[0] / GameFunc.square_size) 
    rows = int(window.size[1] / GameFunc.square_size - GameFunc.score_board / GameFunc.square_size)
    score_board_game = GameFunc.score_board_game

    game_logic = GameLogic(columns=columns, rows=rows, goal=21, score_board_game=score_board_game)
    game_func = GameFunc(game_logic, columns, rows)

    game_logic.add_blocks(Vector2(8, 8))
    game_logic.regist_food_locaton()


    start_music()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and game_logic.last_dir.y != -1:
                    game_logic.change_direction('DOWN')
                if event.key == pygame.K_UP and game_logic.last_dir.y != 1:
                    game_logic.change_direction('UP')
                if event.key == pygame.K_RIGHT and game_logic.last_dir.x != -1:
                    game_logic.change_direction('RIGHT')
                if event.key == pygame.K_LEFT and game_logic.last_dir.x != 1:
                    game_logic.change_direction('LEFT')

        game_func.draw_background()
        delta_time += timer.tick(120)

        if delta_time >= game_values.ms_per_movement:
            game_logic.move()
            if game_logic.snake_game[-1] == game_logic.food_location:
                game_logic.eat_food()
                pygame.mixer.Sound(resource_path("had_choise.mp3")).play(loops=0)
            else:
                game_logic.snake_game.pop(0)
            if game_logic.score[0] == game_logic.score[1]:
                music.stop()
                return "game_over"
                


            for i in range(len(game_logic.snake_real)):

                flag = True
                if game_logic.snake_real[i].x <= -0.9:
                    game_logic.command = "LEFT"
                elif game_logic.snake_real[i].x >= columns - 0.1:
                    game_logic.command = "RIGHT"
                elif game_logic.snake_real[i].y <= game_func.score_board_game -0.9:
                    game_logic.command = 'UP'
                elif game_logic.snake_real[i].y >= rows + game_func.score_board_game - 0.1:
                    game_logic.command = 'DOWN'
                else:
                    flag = False

                if flag == True:
                    game_logic.teleport(i)

                

            delta_time = 0
        
            for coord in (game_logic.snake_game[:-1]):
                if game_logic.snake_game[-1] == coord:
                    game_logic.snake_game.clear()
                    game_logic.snake_real.clear()
                    game_logic.add_blocks(Vector2(6, 6))
                    game_logic.score[0] = 0
                    music.stop()
                    start_music()

            
            # for coord in game_logic.walls:
            #     if game_logic.snake_game[-1] == coord:
            #         game_logic.snake_game.clear()
            #         game_logic.snake_real.clear()
            #         game_logic.add_blocks(Vector2(6, 6))
            #         game_logic.score[0] = 0

                


        game_func.draw_food()
        game_func.draw_snake()
        game_func.draw_score_board()
        game_func.draw_score_text()

        pygame.display.flip()

