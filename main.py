import window
from tkinter import Tk, messagebox, Canvas
from tkinter.ttk import Style, Frame, Button


if __name__ == '__main__':
    root = Tk()
    Style().theme_use('clam')
    window.Window(root)
    root.mainloop()
