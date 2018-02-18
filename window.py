import world
from tkinter.ttk import Frame, Button


class Window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.resizable(False, False)
        self.master.title("PyGOL")
        self.pack()

        self.button_start = Button(self, text="Start", command=self.button_start)
        self.button_start.grid(row=1, column=1, padx=8, pady=8)

        Button(self, text="Rest", command=self.button_reset).grid(row=2, column=1)

        self.world = world.World(self, 60, on_stop=self.button_start_text_reset)
        self.world.grid(row=1, column=2, rowspan=50)

    def button_start_text_reset(self):
        self.button_start['text'] = 'Start'

    def button_start(self):
        if self.world.simulation:
            self.world.stop()
            self.button_start_text_reset()
        else:
            self.world.start()
            self.button_start['text'] = 'Text'

    def button_reset(self):
        self.world.stop()
        self.world.clear()
        self.button_start_text_reset()