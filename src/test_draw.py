from window import Window
from maze import Maze, Point, Cell, Line

i, j = (1, 2)

print(i, j)

def main_test():
    height = 800
    width = 600
    win = Window(height, width)
    draw_maze_cells(win)
    win.wait_for_close()

## Test Drawing a maze cells
def draw_maze_cells(win):
    Maze(Point(50, 50), 10,10, 50, 50, win).solve()
    

## Test drawing line between two cells
def draw_line_between_two_cells(win: Window):
    cell_1 = Cell(win)
    cell_1.has_right_wall = False
    cell_1.draw(Point(50, 50), Point(150, 150))
    
    cell_2 = Cell(win)
    cell_2.has_left_wall = False
    cell_2.has_bottom_wall = False
    cell_2.draw(Point(150, 50), Point(250, 150))

    cell_3 = Cell(win)
    cell_3.has_top_wall = False
    cell_3.draw(Point(150, 150), Point(250, 250))

    cell_3.draw_move(cell_2)
    cell_2.draw_move(cell_1)
    # cell_2.draw_move(cell_3, True)

## Test drawing cells
def draw_some_cells(win: Window):
    """
    Test cases:
        - All walls
        - parallel walls (top/bottom OR left/right)
        - 3 walls (remove one side)
    """


    cell_all_walls = Cell(win) 
    cell_all_walls.draw(Point(50, 50), Point(100, 100))
    
    cell_parallel_walls_1 = Cell(win) 
    cell_parallel_walls_1.has_top_wall = False
    cell_parallel_walls_1.has_bottom_wall = False
    cell_parallel_walls_1.draw(Point(150, 50), Point(200, 100))

    cell_parallel_walls_2 = Cell(win) 
    cell_parallel_walls_2.has_right_wall = False
    cell_parallel_walls_2.has_left_wall = False
    cell_parallel_walls_2.draw(Point(250, 50), Point(300, 100))

    cell_3_walls_1 = Cell(win) 
    cell_3_walls_1.has_left_wall = False
    cell_3_walls_1.draw(Point(50, 150), Point(100, 200))

    cell_3_walls_2 = Cell(win) 
    cell_3_walls_2.has_top_wall = False
    cell_3_walls_2.draw(Point(150, 150), Point(200, 200))
    
    cell_3_walls_3 = Cell(win) 
    cell_3_walls_3.has_bottom_wall = False
    cell_3_walls_3.draw(Point(250, 150), Point(300, 200))


## Test drawing lines 
def draw_some_lines(win: Window, win_height: int, win_width: int):
    draw_horizontal_lines(win, win_height, win_width)
    draw_vertical_lines(win, win_height, win_width)

def draw_vertical_lines(win: Window, win_height: int, win_width):
    line_length = 50
    padding_from_edges = 50
    current_x_pos = padding_from_edges
    current_y_pos = padding_from_edges
    while current_y_pos < win_height - padding_from_edges:
        p_1 = Point(current_x_pos, current_y_pos)
        p_2 = Point(current_x_pos, current_y_pos + line_length)
        line = Line(p_1, p_2)
        win.draw_line(line, "black")

        if current_x_pos + padding_from_edges == win_width:
            current_x_pos = padding_from_edges
            current_y_pos += line_length
        else:
            current_x_pos += 50
    
    
def draw_horizontal_lines(win: Window, win_height: int, win_width):
    line_length = 50
    padding_from_edges = 50
    current_x_pos = padding_from_edges
    current_y_pos = padding_from_edges
    while current_y_pos < win_height:
        p_1 = Point(current_x_pos, current_y_pos)
        p_2 = Point(current_x_pos + line_length, current_y_pos)
        line = Line(p_1, p_2)
        win.draw_line(line, "black")

        if current_x_pos + (2 * padding_from_edges) == win_width:
            current_x_pos = padding_from_edges
            current_y_pos += line_length
        else:
            current_x_pos += 50
        
if __name__ == "__main__":
    main_test()