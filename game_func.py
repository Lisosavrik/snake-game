import pygame
from window import window 
from game_palette import palette_1
from pygame import Surface, Vector2
from game_logic import GameLogic
from typing import List
from game_values import game_values
from fsutils import resource_path

import random
import time

pygame.mixer.init()

class GameFunc:
    square_size = 20
    coeficient_score_board = 0.1
    coeficient_text_size = 0.3
    score_board: float = window.size[1] * coeficient_score_board
    score_board_game: float = score_board / square_size
    text_size = int(score_board * coeficient_text_size)
    text: Surface
    
    def __init__(self, game_logic: GameLogic, columns, rows):
        self.game_logic = game_logic
        self.columns = columns
        self.rows = rows


    def draw_blocks(self, pos: Vector2, color: List[int]):
        pygame.draw.rect(window.screen, color, [pos.x, pos.y, self.square_size, self.square_size])
    
    def draw_food(self):
        real_location = self.game_logic.food_location * self.square_size
        self.draw_blocks(real_location, palette_1.food_color)

    def draw_snake(self):
        for i, block in enumerate(self.game_logic.snake_game):
            from_coord = self.game_logic.snake_real[i]
            
            self.game_logic.snake_real[i] = from_coord + (block - from_coord) * game_values.lerp_coeficient
            new_real_coord = self.game_logic.snake_real[i]

            color = palette_1.snake_head_color if i == len(self.game_logic.snake_game) -1 else palette_1.snake_body_color 

            self.draw_blocks(pos=new_real_coord * self.square_size , color=color)

    def draw_background(self):

        for row in range(self.rows):
            row = row + self.score_board_game
            for column in range(self.columns):
                var1 = palette_1.background_color_1 if  column % 2 ==  0 else palette_1.background_color_2
                var2 = palette_1.background_color_1 if  column % 2 !=  0 else palette_1.background_color_2
                color = var1 if row % 2 == 0 else var2
                location = Vector2(column, row)
                real_location = location * self.square_size
                self.draw_blocks(real_location, color)

    def draw_score_board(self):
        pygame.draw.rect(window.screen, palette_1.background_color_3, [0, 0,  window.size[0], self.score_board])

    def draw_score_text(self):
        font = pygame.font.Font(resource_path("8bit.ttf"), self.text_size)

        score = self.game_logic.score
        

        self.score_text = font.render(f"Your rect is {score[0]}  from {score[1]}", True, palette_1.score_color)
        self.score_text_rect = self.score_text.get_rect(center=(window.size[0] // 2, self.score_board // 2))
        window.screen.blit(self.score_text, self.score_text_rect)
        

    def draw_walls(self):
        for coordinate in self.game_logic.walls:
            real_coordinate = coordinate * self.square_size
            real_coordinate.y += self.score_board
            self.draw_blocks(real_coordinate, palette_1.wall_color)
