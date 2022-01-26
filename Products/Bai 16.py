import tkinter as tk
import numpy as np

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bai 16: Trackbar thay doi bien do hinh sin")
        self.geometry("325x245")
        self.height = tk.IntVar()
        self.trackbar = tk.Scale(self, length = 300, orient=tk.HORIZONTAL, showvalue=False,
                                variable=self.height, command=self.trackbar_command)
        self.figure = tk.Canvas(self, bd = 1, height = 200, width = 300,
                                relief = tk.SUNKEN)
        
        self.figure.place(x = 10, y = 30)
        self.trackbar.place(x = 10, y = 10)

    def ve_hinh(self, height):
        height = int(height)
        W = self.figure.winfo_width()-1
        H = self.figure.winfo_height()-1
        x = np.arange(0, W, 5)
        x1 = x * (6 * np.pi) / W
        y = -height * np.sin(x1) + H/2

        p = []
        for i in range (0, len(x)):
            p += [x[i], y[i]]
        self.figure.delete('all')
        self.figure.create_line(p)
        self.figure.update()

    def trackbar_command(self, height):
        height = self.height.get()
        self.ve_hinh(height)

if __name__ == "__main__":
    app = App()
    app.mainloop()