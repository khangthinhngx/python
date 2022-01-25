import tkinter as tk
import numpy as np


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bai Thuc Hanh Dau Tien")
        self.geometry('640x480')
        self.cvs_figure = tk.Canvas(self, relief=tk.SUNKEN, bg='white', bd=1,
                                    width=300, height=300)
        btn_tron = tk.Button(self, text='Tron', width=8,
                             command=self.btn_tron_click)
        btn_sin = tk.Button(self, text='Sin', width=8,
                            command=self.btn_sin_click)
        btn_parabol = tk.Button(self, text='Parabol',
                                width=8, command=self.btn_parabol_click)

        self.cvs_figure.place(x=5, y=5)
        btn_tron.place(x=320, y=6)
        btn_sin.place(x=320, y=36)
        btn_parabol.place(x=320, y=66)

    def btn_tron_click(self):
        self.cvs_figure.delete('all')
        self.cvs_figure.update()
        W = self.cvs_figure.winfo_width() - 1
        H = self.cvs_figure.winfo_height() - 1
        xc = W // 2
        yc = H // 2
        r = 100
        n = 50
        dx = 2*r/n
        m = n // 2
        data = []
        for i in range(-m, m+1):
            x = i*dx
            y = np.sqrt(r**2 - x**2)
            data.append(xc + x)
            data.append(yc - y)

        for i in range(m-1, -m-1, -1):
            x = i*dx
            y = -np.sqrt(r**2 - x**2)
            data.append(xc + x)
            data.append(yc - y)

        self.cvs_figure.create_line(data)

    def btn_sin_click(self):
        self.cvs_figure.delete('all')
        self.cvs_figure.update()
        W = self.cvs_figure.winfo_width() - 4
        H = self.cvs_figure.winfo_height() - 4
        n = 50
        m = 2  # so chu ky
        dx = m * 2*np.pi/n
        data = []
        for i in range(0, n+1):
            x = i*dx
            y = np.sin(x)
            p = W*x/(m * 2*np.pi)
            q = (H-4)*(1-y)/2 + 4
            data.append(p)
            data.append(q)

        self.cvs_figure.create_line(data)

    def btn_parabol_click(self):
        self.cvs_figure.delete('all')
        self.cvs_figure.update()
        W = self.cvs_figure.winfo_width() - 4
        H = self.cvs_figure.winfo_height() - 4
        n = 50
        dx = 4/n
        m = n // 2
        data = []
        for i in range(-m, m+1):
            x = i*dx
            y = x**2
            p = W*(x+4)/8
            q = H*(4-y)/8
            data.append(p)
            data.append(q)
        self.cvs_figure.create_line(data)


if __name__ == "__main__":
    app = App()
    app.mainloop()
