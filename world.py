import grid
from threading import Thread
from time import sleep
from tkinter import messagebox


class World(grid.Grid):
    def __init__(self, master=None, size=3, fps=10, on_stop=None):
        super().__init__(master, [[False] * size for _ in range(0, size)])
        self.size = size
        self.time_frame = 1 / fps
        self._on_stop = on_stop
        self.simulation = False

    def start(self):
        self.simulation = True
        Thread(target=self._next_loop).start()

    def stop(self):
        self.simulation = False
        self._on_stop and self._on_stop()

    def _next_loop(self):
        while self.simulation:
            sleep(self.time_frame)
            self.next()

    def for_all_cell(self, f):
        new_cell = [[False] * self.size for _ in range(0, self.size)]
        for y in range(0, self.size):
            for x in range(0, self.size):
                new_cell[x][y] = f(x, y)
        if self.simulation and self.cell == new_cell:
            self.stop()
            messagebox.showwarning("The simulation stopped")
            self.clear()
        else:
            self.cell = new_cell
            self.draw()

    def clear(self):
        self.for_all_cell(lambda x, y: False)

    def next(self):
        def f(x, y):
            neighbors = -self.cell[x][y]
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    neighbors += self.cell[(x+dx) % self.size][(y+dy) % self.size]
            return neighbors == 2 and self.cell[x][y] or neighbors == 3
        self.for_all_cell(f)