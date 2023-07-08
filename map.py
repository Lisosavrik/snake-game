from window import window


field = []
map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def create_game_field(square_size):
    for y in range(window.size[1]//square_size):
        field.append([])
        for x in range(window.size[0]//square_size):
            field[y].append(0)
            
def add_wall(square_size):
    global field
    create_game_field(square_size)

    scale = len(map[0])
    for y, mass in enumerate(map):
        for x, el in enumerate(mass):
            if el ==  1:
                percent_x = x * scale / 100
                percent_y = y * scale / 100
                
                need_y = round(len(field) * percent_y)
                need_x = round(len(field[need_y]) * percent_x)

                scale_x = len(field[0]) / scale
                scale_y = len(field) / scale

                i_y = 0
                while i_y < scale_y:
                    i_x = 0
                    needed_y = need_y + i_y
                    while i_x < scale_x:
                        needed_x = need_x + i_x
                        field[needed_y][needed_x] = 1
                        i_x += 1
                    i_y += 1

    
    return field

# def draw_map(map: list[list[int]]):
#     print((len(map[0])  * 3) * "=")
#     for row in map:
#         print(row)
#     print((len(map[0])  * 3) * "=")


# add_wall(20)
# draw_map(field)