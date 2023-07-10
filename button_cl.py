import pygame
from pygame import Vector2
from typing import List, Tuple
from game_palette import palette_1
from fsutils import resource_path

def within_range(val: int, min: int, max: int):
    return val > min and val < max

class Button():
    def __init__(
        self, 
        window_size: List[int],
        button_title: str,
        button_color: List[int],
        selection_color: List[int],
        font: pygame.font.Font,
        index_button: int, 
        main_title_rect: pygame.Rect,
        background_color: List[int],

        margin_between_buttoms=30
    ):

        self.button_title = button_title
        self.window_size = window_size
        self.button_color = button_color
        self.selection_color = selection_color
        self.font = font
        self.index_button = index_button
        self.main_title_rect = main_title_rect
        self.margin_between_buttoms = margin_between_buttoms
        self.background_color = background_color
        self.first_move = True

        self.set_button()

        


    def set_button(self):
        self.set_center_button_pos(self.main_title_rect.bottom)

        self.button_text: pygame.Surface = self.font.render(self.button_title, True, self.button_color)
        self.button_rect = self.button_text.get_rect(topleft=self.pos)
        self.button_surface = pygame.Surface(self.button_text.get_size())


    def check_change_color(self, pos: Tuple[int, int]):
        if within_range(pos[0], self.button_rect.left, self.button_rect.right) and within_range(pos[1],self.button_rect.top, self.button_rect.bottom):
            # self.button_text = self.font.render(self.button_title, True, self.selection_color)
            self.button_surface_color = self.selection_color
            self.flag = True


        else:
            self.button_surface_color = self.background_color
            self.flag = False
            self.first_move = True

            # self.button_text = self.font.render(self.button_title, True, self.button_color)

    def update_buttons(self, screen: pygame.Surface):
        self.button_surface.fill(self.button_surface_color)
        screen.blit(self.button_surface, self.button_rect)
        screen.blit(self.button_text, self.button_rect)
        if self.flag and self.first_move == True:

            pygame.mixer.Sound(resource_path("variant.mp3")).play(loops=0)

            self.first_move = False


    def check_for_mousebutton(self, pos: Tuple[int, int]):
        if within_range(pos[0], self.button_rect.left, self.button_rect.right) and within_range(pos[1], self.button_rect.top, self.button_rect.bottom):
            return True
        else:
            return False
        
    def button_size(self):
        self.button_size =  pygame.font.Font.size(self.font, self.button_title)
    
    def set_center_button_pos(self, title_bottom):
        self.button_size()
        x = self.window_size[0] // 2 - self.button_size[0] // 2

        y = ( title_bottom + self.margin_between_buttoms * 2) +  ((self.button_size[1] + self.margin_between_buttoms) * self.index_button) 
        self.pos =  Vector2(x, y)
        1



# class Btn:

#     def __init__(self):
#         self.inside = False
#         self.entered = False

#     def update(self):
#         self.setInside(insideButton)

#     def setInside(self, newVal: bool):
#         if (self.inside != newVal and newVal):
#             self.entered = True
#         else:
#             self.entered = False
#         self.inside = newVal



