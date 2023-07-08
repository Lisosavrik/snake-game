from pygame import Vector2
import random
from typing import List





class GameLogic:
    def __init__(
            self, 
            columns: int, 
            rows: int, 
            goal: int, 
            score_board_game: float
            ):
        
        self.columns = columns
        self.rows = rows
        self.goal = goal
        self.score_board_game = score_board_game

        self.snake_game: List[Vector2] = []
        self.snake_real: List[Vector2]  = []
        self.food_location = Vector2(0, 0)
        self.command: str = ''
        self.score: int = [0, goal]

    dir = Vector2(0, 1)
    last_dir = Vector2(0, 0)

    def add_blocks(self, pos: Vector2):
        self.snake_game.append(pos.copy())
        self.snake_real.append(pos.copy())

    def regist_food_locaton(self):
        self.food_location.x = random.randint(0, self.columns - 1)
        self.food_location.y = random.randint(self.score_board_game, self.rows - 1)

    def eat_food(self):
        self.regist_food_locaton()
        self.add_score()
        self.snake_real.insert(0, self.snake_game[0].copy())


    def teleport(self, i: int):
        match self.command:
            case "LEFT": 
                self.snake_real[i].x = self.columns
                self.snake_game[i].x = self.columns - 1
            case "RIGHT":
                self.snake_real[i].x = -0.5
                self.snake_game[i].x = 0
            case "UP":
                self.snake_real[i].y = self.rows + self.score_board_game
                self.snake_game[i].y = self.rows - 1 + self.score_board_game
            case "DOWN": 
                self.snake_real[i].y = -0.5 + self.score_board_game
                self.snake_game[i].y = 0 + self.score_board_game


    def change_direction(self, pos: str):
        match pos:
            case 'DOWN':
                self.dir.x, self.dir.y = 0, 1
            case 'UP':
                self.dir.x, self.dir.y = 0, -1
            case 'LEFT':
                self.dir.x, self.dir.y = -1, 0
            case 'RIGHT':
                self.dir.x, self.dir.y = 1, 0

    def move(self):
        new_head = Vector2(self.snake_game[-1] + self.dir)
        self.snake_game.append(new_head)
        self.last_dir.x, self.last_dir.y = self.dir.x, self.dir.y

    def add_score(self):
        self.score[0] += 1


    def add_walls(self, game_field):
        walls = []
        for y, mass in enumerate(game_field):
            for x, el in enumerate(mass):
                if el == 1:
                    walls.append(Vector2(x=x, y=y))
        
        self.walls = walls


        
