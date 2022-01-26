import tkinter as tk
from tkinter import *
import math


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('460x358')
        self.resizable(FALSE, FALSE)
        self.title('Bai 7: Timer')

        self.canvas = tk.Canvas(self, relief=tk.SUNKEN,
                                bd=2, width=350, height=350)

        self.btn_start = tk.Button(
            self, text='Start', font=(10), width=8, command=self.start)
        self.btn_stop = tk.Button(
            self, text='stop', font=(10), width=8, command=self.stop)

        self.canvas.grid(row=0, column=0)
        self.btn_start.grid(row=0, column=1, sticky=tk.N, pady=(2, 0))
        self.btn_stop.grid(row=0, column=1, sticky=tk.N, pady=(45, 0))

        self.pX = []
        self.pY = []
        i = 1.57
        while i >= 0:
            x = 125*math.cos(i)
            self.pX.append(x)
            y = math.sqrt(125*125 - x*x)
            self.pY.append(y)
            i = i-0.01
        while i >= -3.14:
            x = 125*math.cos(i)
            self.pX.append(x)
            y = -math.sqrt(125*125 - x*x)
            self.pY.append(y)
            i = i-0.01
        while i >= -4.71:
            x = 125*math.cos(i)
            self.pX.append(x)
            y = math.sqrt(125*125-x*x)
            self.pY.append(y)
            i = i-0.01

        self.i = 0
        self.canvas.create_oval(50, 50, 300, 300, outline='blue')
        self.btn_stop.configure(state='disabled')
        self.cid = self.canvas.create_rectangle(
            170, 45, 180, 55, outline='red', fill='red')

        self.status = 'stop'

    def draw(self):
        if self.i == len(self.pX):
            self.i = 0
        if self.status == 'start':
            self.cid = self.canvas.create_rectangle(
                170+self.pX[self.i], 170-self.pY[self.i], 180 + self.pX[self.i], 180-self.pY[self.i], outline='red', fill='red')
            self.i = self.i+1
            self.canvas.after(20, self.canvas.delete, self.cid)
            self.after(15, self.draw)

    def start(self):
        self.btn_start.configure(state='disabled')
        self.btn_stop.configure(state='active')
        self.status = 'start'
        self.canvas.after(0, self.canvas.delete, self.cid)
        self.draw()

    def stop(self):
        self.status = 'stop'
        self.btn_start.configure(state='active')
        self.btn_stop.configure(state='disabled')
        self.cid = self.canvas.create_rectangle(
            170+self.pX[self.i], 170-self.pY[self.i], 180 + self.pX[self.i], 180-self.pY[self.i], outline='red', fill='red')


if __name__ == '__main__':
    app = App()
    app.mainloop()
