from general_menu import general_menu
from game_process import all_game
from game_over_menu import game_over
import sys
import pygame

def events():
    event = "_"

    while True:
        if event == "_":
            event = general_menu()
        elif event == 'play':
            event = all_game()
        elif event == "game_over":
            event = game_over()
        elif event == "again":
            event = all_game()
        elif event == "exit":
            pygame.quit()
            sys.exit()






