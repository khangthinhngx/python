import tkinter as tk
import numpy as np


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bai 16: Trackbar thay doi bien do hinh sin")
        self.geometry("425x445")
        self.height = tk.IntVar()
        self.trackbar = tk.Scale(self, length=403, orient=tk.HORIZONTAL, showvalue=False,
                                 variable=self.height, command=self.trackbar)
        self.canvas = tk.Canvas(self, bd=2, height=400, width=400,
                                relief=tk.SUNKEN)

        self.canvas.place(x=8, y=30)
        self.trackbar.place(x=8, y=10)

    def draw(self, height):
        height = int(height)
        W = self.canvas.winfo_width()-1
        H = self.canvas.winfo_height()-1
        x = np.arange(0, W, 5)
        x1 = x * (6 * np.pi) / W
        y = -height * np.sin(x1) + H/2

        p = []
        for i in range(0, len(x)):
            p += [x[i], y[i]]
        self.canvas.delete('all')
        self.canvas.create_line(p)
        self.canvas.update()

    def trackbar(self, height):
        height = self.height.get()
        self.draw(height)


if __name__ == "__main__":
    app = App()
    app.mainloop()
