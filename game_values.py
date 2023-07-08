class GameValues:


    def __init__(self, *non_keywords, lerp_coeficient: float, ms_per_movement: int):
        self.lerp_coeficient = lerp_coeficient
        self.ms_per_movement = ms_per_movement

game_values = GameValues(
    lerp_coeficient = 0.05,
    ms_per_movement = 400
)

