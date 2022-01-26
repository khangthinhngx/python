import tkinter as tk
from tkinter import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.title('Bai 12: Ve hinh tron')
        self.H = 400
        self.W = 400
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.canvas = tk.Canvas(self, relief=tk.SUNKEN, bd=2)

        # grid
        self.canvas.grid(row=0, column=0, sticky=tk.NSEW)

        # ve hinh tron ban dau
        self.canvas.create_oval(20, 20, 380, 380, fill='red', outline='red')
        # tracking su thay doi kick thich
        self.canvas.bind('<Configure>', self.configure)

    def configure(self, event):
        # xoa hinh tron
        self.canvas.delete('all')
        self.H = event.height
        self.W = event.width
        # ve lai hinh tron
        self.canvas.create_oval(20, 20, self.W - 20,
                                self.H-20, fill='red', outline='red')


if __name__ == '__main__':
    app = App()
    app.mainloop()
