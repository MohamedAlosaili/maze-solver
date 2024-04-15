#!/usr/bin/env python

from tkinter import Canvas, BOTH
from typing import Self
import time
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1, point_2) -> None:
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas: Canvas, fill = "red"):
        canvas.create_line(
            self.point_1.x,
            self.point_1.y,
            self.point_2.x,
            self.point_2.y,
            fill=fill,
            width=2
        )
        canvas.pack(fill=BOTH, expand=1)


class Cell:
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
        self._p1 = None # top-left corner
        self._p2 = None # bottom-right corner
        self.visited = False
             
    def draw(self, p1: Point, p2: Point):

        sides = []
        self._p1 = p1
        self._p2 = p2

        sides.append({"line": Line(Point(self._p1.x, self._p1.y), Point(self._p1.x, self._p2.y)), "transparent": not self.has_left_wall}) # Left
        sides.append({ "line": Line(Point(self._p2.x, self._p1.y), Point(self._p2.x, self._p2.y)), "transparent": not self.has_right_wall}) # Right 
        sides.append({ "line": Line(Point(self._p1.x, self._p1.y), Point(self._p2.x, self._p1.y)), "transparent": not self.has_top_wall}) # Top
        sides.append({ "line": Line(Point(self._p1.x, self._p2.y), Point(self._p2.x, self._p2.y)), "transparent": not self.has_bottom_wall}) # Bottom

        if self._win is None: return

        for side in sides:
            self._win.draw_line(side["line"], "#add8e6" if side["transparent"] else "black")

    def draw_move(self, to_cell: Self, undo=False):
        if self._win is None: return
        
        self_mid_x = (self._p1.x + self._p2.x) / 2
        self_mid_y = (self._p1.y + self._p2.y) / 2
        to_mid_x = (to_cell._p1.x + to_cell._p2.x) / 2
        to_mid_y = (to_cell._p1.y + to_cell._p2.y) / 2

        line = Line(
                Point(self_mid_x, self_mid_y), 
                Point(to_mid_x, to_mid_y)
            )
        fill = "red"
        if undo:
            fill = "gray"

        self._win.draw_line(line, fill)
        

class Maze:
    def __init__(
            self, 
            start_point: Point, 
            num_rows: int, 
            num_cols: int, 
            cell_size_x: int, 
            cell_size_y: int, 
            win = None,
            seed = None
    ):
        self._start_point = start_point
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited_cells()

    def _create_cells(self):
        for _ in range(self._num_cols):
            cells_col = []
            for _ in range(self._num_rows):
                cells_col.append(Cell(self._win))

            self._cells.append(cells_col)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j): 
        if len(self._cells) == 0:
            return

        x1 = self._start_point.x + (i * self._cell_size_x) 
        y1 = self._start_point.y + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(Point(x1, y1), Point(x2, y2))

        self._animate()

    def _animate(self):
        if self._win is None: return
        self._win.redraw()
        time.sleep(0.025)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False 
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if self._num_cols - 1 > i and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j)) 
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if self._num_rows - 1 > j and not self._cells[i][j+1].visited:
                to_visit.append((i, j + 1))
            
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
        
            new_i, new_j = to_visit[random.randrange(len(to_visit))]
            
            target_cell = self._cells[new_i][new_j]
            if new_i > i:
                self._cells[i][j].has_right_wall = False 
                target_cell.has_left_wall = False
            elif new_i < i:
                self._cells[i][j].has_left_wall = False 
                target_cell.has_right_wall = False
            elif new_j > j:
                self._cells[i][j].has_bottom_wall = False 
                target_cell.has_top_wall = False
            elif new_j < j:
                self._cells[i][j].has_top_wall = False 
                target_cell.has_bottom_wall = False
        
            self._break_walls_r(new_i, new_j)

    def _reset_visited_cells(self):
        for cells in self._cells:
            for cell in cells:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        cell = self._cells[i][j]
        cell.visited = True

        next_cell = None
        if not cell.has_top_wall and j > 0 and not self._cells[i][j - 1].visited:
            next_cell = self._cells[i][j - 1]
            cell.draw_move(next_cell)
            if self._solve_r(i, j - 1):
                return True
            cell.draw_move(next_cell, True)
        if not cell.has_right_wall and i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
            next_cell = self._cells[i+ 1][j]
            cell.draw_move(next_cell)
            if self._solve_r(i+ 1, j):
                return True
            cell.draw_move(next_cell, True)
        if not cell.has_bottom_wall and j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
            next_cell = self._cells[i][j + 1]
            cell.draw_move(next_cell)
            if self._solve_r(i, j + 1):
                return True
            cell.draw_move(next_cell, True)
        if not cell.has_left_wall and i > 0 and not self._cells[i - 1][j].visited:
            next_cell = self._cells[i - 1][j]
            cell.draw_move(next_cell)
            
            if self._solve_r(i - 1, j):
                return True
            cell.draw_move(next_cell, True)

        return False

