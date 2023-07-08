from typing import List

class Colors:
    WHITE_GREEN = (189, 236, 182)
    FERN_COLOR = (113, 188, 120)
    RED = (128, 0, 0)
    BLUE = (0, 114, 207)
    DARK_BLUE = (0, 68, 131)
    VIOLET = (232, 136, 241)
    BROWN = (92, 64, 51)
    YELLOW = (244, 154, 24)
    WHITE = (255, 250, 245)
    COFFEE_WHITE = (238, 227, 216)
    GREY = (27, 27, 27)


class Palette:
    def __init__(
        self,
        *non_keywords,
        snake_body_color: List[int],
        snake_head_color: List[int],
        background_color_1: List[int],
        background_color_2: List[int],
        background_color_3: List[int],
        food_color: List[int], 
        score_color: List[int],
        selection_color: List[int],
        title_color: List[int],
        widget_color: List[int],
        game_over_colors: List[list], 
        dark_widget_color: List[list]

    ):
        self.i = 0
        self.snake_body_color = snake_body_color
        self.snake_head_color = snake_head_color
        self.background_color_1 = background_color_1
        self.background_color_2 = background_color_2
        self.background_color_3 = background_color_3
        self.food_color = food_color
        self.score_color = score_color
        self.widget_color = widget_color
        self.title_color = title_color
        self.selection_color = selection_color
        self.game_over_colors = game_over_colors
        self.dark_widget_color = dark_widget_color




palette_1 = Palette(
    snake_body_color= Colors.WHITE,
    snake_head_color= Colors.COFFEE_WHITE,
    background_color_1= Colors.BLUE,
    background_color_2= Colors.DARK_BLUE,
    background_color_3= Colors.WHITE,

    food_color = Colors.YELLOW,
    score_color = Colors.GREY,
    widget_color= Colors.COFFEE_WHITE,
    dark_widget_color = Colors.GREY,
    title_color= Colors.COFFEE_WHITE,
    selection_color = Colors.YELLOW,
    game_over_colors = [
        (Colors.YELLOW), 
        (Colors.BLUE), 
        (Colors.DARK_BLUE), 
        (Colors.RED), 
        (Colors.VIOLET), 
        (Colors.FERN_COLOR)]
)

