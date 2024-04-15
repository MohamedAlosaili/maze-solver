from window import Window
from maze import Maze, Point

def main():
    win_height = 800
    win_width = 600
    win = Window(win_height, win_width)
    maze = Maze(Point(50, 50), 10, 10, 50, 50, win)
    maze.solve()
    win.wait_for_close()


main()
