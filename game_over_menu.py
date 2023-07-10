import pygame
from fsutils import resource_path
from window import window 
import time 
from game_palette import palette_1
import random
pygame.init()
pygame.mixer.init()
from button_cl import Button 
import sys
from theme_menu import ThemeMenu








def play_music():
    pygame.mixer.music.load(resource_path("game_over.mp3"))
    pygame.mixer.music.play(loops = 0)

def game_over():
    theme = ThemeMenu(
        screen=window.screen,
        titles={"game_over_title": "Game over"}, 
        buttons={"again": "Play again", "exit": "Quit"},
        scale_widget=0.06,
        pos_title="CENTER",
    )

    play_music()






    
    example_rect = theme.create_titles(theme.titles["game_over_title"], (27, 27, 27))

    again_btn = Button(
        [theme.screen.get_width(), theme.screen.get_height()],
        theme.buttons["again"], 
        palette_1.dark_widget_color,
        palette_1.selection_color, 
        theme.widget_font , 
        0, 
        theme.title_rect, 
        palette_1.background_color_3
        )
    
    exit_btn =  Button(
        [theme.screen.get_width(), theme.screen.get_height()] , 
        theme.buttons["exit"], 
        palette_1.dark_widget_color, 
        palette_1.selection_color, 
        theme.widget_font, 
        1, 
        theme.title_rect, 
        palette_1.background_color_3
        )
    



    while True:
        mouse_pos = pygame.mouse.get_pos()

        time.sleep(0.1)
        color = palette_1.game_over_colors[random.randint(0, len(palette_1.game_over_colors) - 1)]

        theme.create_titles(theme.titles["game_over_title"], color=color)
        theme.draw_menu(palette_1.background_color_3)


        if pygame.mixer.music.get_busy() == False:
            for button in [again_btn, exit_btn]:
                button.check_change_color(mouse_pos)
                button.update_buttons(window.screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if again_btn.check_for_mousebutton(mouse_pos):
                    pygame.mixer.Sound(resource_path("had_choise.mp3")).play(loops=0)
                    return "again"
                elif exit_btn.check_for_mousebutton(mouse_pos):
                    pygame.mixer.Sound(resource_path("had_choise.mp3")).play(loops=0)
                    return "exit"
        
        pygame.display.flip()





