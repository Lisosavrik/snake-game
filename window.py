import pygame
# class Snake:
#     def __init__(self, head_position):
#         self.blocks = [head_position];

#     def move(self):
#         pass

class Window:
    def set_size(self, size):
        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.menu_screen = pygame.display.set_mode(size)


    def set_title(self, title):
        self.title: str = title
        pygame.display.set_caption(title)
    
    def __init__(self, size: "list(int)", title: str):
        self.set_size(size)
        self.screen
        self.menu_screen
        self.set_title(title)



    # def update(self, width, height):
    #     self.set_size(self, [width, height])


window = Window(
    size=[400, 400], 
    title= "Snake"
)

