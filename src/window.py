#!/usr/bin/env python

from tkinter import Tk, BOTH, Canvas, messagebox, Menu
from maze import Line

class Window:
    def __init__(self, height, width):
        self.__window = Tk()
        self.__window.title("MAZE")
        self.__window.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__window, { "height": height, "width": width, "bg": "#add8e6" })
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False    

    def redraw(self):
        self.__window.update_idletasks()
        self.__window.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("Window closed")

    def draw_line(self, line: Line, fill):
        line.draw(self.__canvas, fill)

    def get_window_width(self):
        return self.__window.winfo_width()
    
    def get_window_height(self):
        return self.__window.winfo_height()

    def close(self):
        if messagebox.askokcancel("Close", "Are you sure you want to close the window?"):
            self.__window.destroy()
            self.__is_running=False