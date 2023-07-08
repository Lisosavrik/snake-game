import pygame

from game_palette import palette_1
from os import path
from pygame import Vector2

pygame.init()



class ThemeMenu:
    def __init__(
            self,
            screen: pygame.Surface, 
            titles: dict,
            buttons: dict,
            scale_widget: float = 0.1,
            scale_title: float = 0.1,
            font_file: str = "fonts/8bit.ttf", 
            scale_offset_title: float = 0.05,
            pos_title: str ="TOPLEFT"

            
            
            ):
        
        self.screen = screen
        self.titles = titles
        self.buttons = buttons
        self.scale_widget = scale_widget
        self.scale_title = scale_title
        self.font_file = font_file
        self.scale_offset_title = scale_offset_title
        self.pos_title = pos_title

        self.set_title_font()
        self.set_widget_font()



            


    def set_title_font_size(self):
        self.title_font_size  = int(self.screen.get_width() * self.scale_title)


    def set_widget_font_size(self):
        self.widget_font_size = int(self.screen.get_width() * self.scale_widget)



    def set_title_font(self):
        self.set_title_font_size()
        self.title_font = pygame.font.Font(path.join(path.dirname(__file__), self.font_file), self.title_font_size)

    def set_widget_font(self):
        self.set_widget_font_size()
        self.widget_font = pygame.font.Font(path.join(path.dirname(__file__), self.font_file), self.widget_font_size)



    def set_title_offset(self, title_text: str):

        if self.pos_title == "TOPLEFT":

            title_x, _title_y = self.title_font.size(title_text)
            title_offset_x = int(self.screen.get_width() / 2 - title_x / 2)
            title_offset_y = int(self.screen.get_height() * self.scale_offset_title)

        elif self.pos_title == "CENTER":
            title_offset_x = self.screen.get_width() // 2
            title_offset_y = self.screen.get_height() // 2
        
        self.general_title_offset: Vector2 = (title_offset_x, title_offset_y)



    
    def create_titles(self, title_text: str, color):
        self.set_title_offset(title_text)
        self.title_text = self.title_font.render(title_text, True, color)

        if self.pos_title == "TOPLEFT":
            self.title_rect = self.title_text.get_rect(topleft=(self.general_title_offset))

        elif self.pos_title == "CENTER":
            self.title_rect = self.title_text.get_rect(center=(self.general_title_offset))


    def draw_menu(self, background_color, ):
        self.screen.fill(background_color)
        self.screen.blit(self.title_text, self.title_rect)








