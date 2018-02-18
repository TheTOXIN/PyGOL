from functools import partial
from tkinter import Canvas


class Grid(Canvas):
    def __init__(self, master=None, data=None, cell_size=10, color='blue'):
        self.cell = data if data else [[False]]
        self._grid_width = len(self.cell)
        self._grid_height = len(self.cell[0])
        self._width = self._grid_width * cell_size
        self._height = self._grid_height * cell_size
        Canvas.__init__(self, master, width=self._width, height=self._height)
        self.cell_size = cell_size
        self.color = color
        self.bind('<Button-1>', self.on_click)
        self.bind('<B1-Motion>', partial(self.on_click, motion=True))
        self.draw()

    def on_click(self, e, motion=False):
        if e.x in range(0, self._width) and e.y in range(0, self._height):
            x = e.x // self.cell_size
            y = e.y // self.cell_size
            self.cell[x][y] = self.cell[x][y] <= motion
            self.draw()

    def draw(self):
        self.delete('all')
        for y in range(0, self._grid_height):
            for x in range(0, self._grid_width):
                if self.cell[x][y]:
                    self.create_rectangle(
                        x * self.cell_size,
                        y * self.cell_size,
                        (x+1) * self.cell_size,
                        (y+1) * self.cell_size,
                        fill=self.color, width=0)