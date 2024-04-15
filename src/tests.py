import unittest

from maze import Maze, Point

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 1
        num_rows = 2
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_cell_location_in_maze(self):
        cols = 5
        rows = 5
        cell_size_x = 10
        cell_size_y = 10
        m = Maze(Point(10, 10), cols, rows, cell_size_x, cell_size_y)
        ## cell 3 in 2nd col should be in 
        x1 = 10 + 1 * cell_size_x
        y1 = 10 + 2 * cell_size_y
        x2 = x1 + cell_size_x  
        y2 = y1 + cell_size_y

        target_cell = m._cells[1][2]
        self.assertEqual(target_cell._p1.x, x1)
        self.assertEqual(target_cell._p1.y, y1)
        self.assertEqual(target_cell._p2.x, x2)
        self.assertEqual(target_cell._p2.y, y2)
        print("Cell is drawn in the expected point")  

    def test_cell_size(self):
        cell_size_x = 15
        cell_size_y = 20
        m = Maze(Point(0, 0), 1, 1, cell_size_x, cell_size_y)
        cell = m._cells[0][0]
        self.assertEqual(cell._p2.x - cell._p1.x, cell_size_x)
        self.assertEqual(cell._p2.y - cell._p1.y, cell_size_y)
        print("Cell is in the expected size")


    def test_entrance_and_exit(self):
        m = Maze(Point(0,0), 3, 3, 5, 5)
        self.assertEqual(m._cells[0][0].has_top_wall, False)
        self.assertEqual(m._cells[2][2].has_bottom_wall, False)
        print("Entrance and exit properly set")
    
    def test_reset_visited(self):
        m = Maze(Point(0,0), 3, 3, 5, 5)
        for col in m._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )
        print("Reset visited work perfectly", m._cells[2][2].visited)

    
if __name__ == "__main__":
    unittest.main()