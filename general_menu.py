import pygame, sys
from fsutils import resource_path
from window import window
from game_palette import palette_1
from button_cl import Button 
from theme_menu import ThemeMenu

pygame.init()
pygame.mixer.init()



def general_menu():

    theme = ThemeMenu(
        screen=window.screen,
        titles={"general_title": "Snake"},
        buttons={"play": "Play", "levels": "Levels", "exit": "Quit"}
    )

    theme.create_titles(theme.titles["general_title"], palette_1.selection_color)

    play_btn = Button(
        [theme.screen.get_width(), theme.screen.get_height()], 
        theme.buttons["play"], 
        palette_1.widget_color, 
        palette_1.selection_color, 
        theme.widget_font, 
        0, 
        theme.title_rect, palette_1.background_color_2)
    
    levels_btn = Button([theme.screen.get_width(), theme.screen.get_height()], 
                        theme.buttons["levels"], 
                        palette_1.widget_color, 
                        palette_1.selection_color, 
                        theme.widget_font, 
                        1, 
                        theme.title_rect, 
                        palette_1.background_color_2
                        )
    
    quit_btn = Button([theme.screen.get_width(), theme.screen.get_height()], 
                    theme.buttons["exit"], 
                    palette_1.widget_color, 
                    palette_1.selection_color, 
                    theme.widget_font, 
                    2, 
                    theme.title_rect, 
                    palette_1.background_color_2
                    )

    
    while True:
        theme.draw_menu(palette_1.background_color_2)


        mouse_pos = pygame.mouse.get_pos()



        for button in [play_btn, levels_btn, quit_btn]:
            button.check_change_color(mouse_pos)
            button.update_buttons(theme.screen)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.check_for_mousebutton(mouse_pos):
                    pygame.mixer.Sound(resource_path("had_choise.mp3")).play(loops=0)
                    return "play"
                elif levels_btn.check_for_mousebutton(mouse_pos):
                    pygame.mixer.Sound(resource_path("had_choise.mp3")).play(loops=0)
                    levels()
                elif quit_btn.check_for_mousebutton(mouse_pos):
                    pygame.mixer.Sound(resource_path("had_choise.mp3")).play(loops=0)
                    return "exit"
    
        pygame.display.flip()


def levels():
    pass





