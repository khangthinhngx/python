import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x430')
        self.title('Bai 11: Truyen nghich')
        self.resizable(FALSE, FALSE)

        # canvas
        self.canvas = tk.Canvas(self, relief=tk.SUNKEN,
                                bd=2, width=392, height=392)

        self.btn_nhap = tk.Button(
            self, text='Nhap ban kinh', width=14, command=self.nhap)

        # grid
        self.canvas.grid(row=0, column=0)
        self.btn_nhap.grid(row=1, column=0)

        self.radius = 0

    def nhap(self):
        # ve cua so moi
        self.newWin = Toplevel(self)
        self.newWin.title('Nhap ban kinh')
        self.newWin.geometry('380x150')
        self.newWin.resizable(FALSE, FALSE)
        self.newWin.focus_force()

        self.radius_input = tk.StringVar()

        self.lbl_nhap = tk.Label(self.newWin, text='Nhap ban kinh', font=(10))
        self.entry = tk.Entry(self.newWin, width=15,
                              font=(10), justify=tk.RIGHT)
        self.btn_draw = tk.Button(
            self.newWin, width=10, text='Ve hinh', font=(10), command=self.draw)

        self.lbl_nhap.place(x=20, y=30)
        self.entry.place(x=180, y=30)
        self.btn_draw.place(x=125, y=80)

    def draw(self):
        def isFloat(value):
            answer = 0.0
            try:
                answer = float(value)
                return True, answer
            except ValueError:
                return False, answer

        value_get = self.entry.get()
        check, self.radius = isFloat(value_get)
        self.radius = int(self.radius)
        if check == False:
            msg.showwarning('Sai input', 'Ban phai nhap chu so')
            self.entry.delete(0, 'end')
            self.entry.focus_set()
            return
        else:
            # xoa canvas ban dau
            self.canvas.destroy()
            # ve lai geometry va canvas moi
            self.geometry('{w}x{h}'.format(
                w=2*self.radius+20, h=2*self.radius+50))
            self.canvas = tk.Canvas(
                self, relief=tk.SUNKEN, bd=2, width=2*self.radius+12, height=2*self.radius+12)
            self.canvas.grid(row=0, column=0)
            # xoa cua so input
            self.newWin.destroy()
            # ve hinh tron
            self.canvas.create_oval(
                10, 10, 2*self.radius+10, 2*self.radius+10, fill='red', outline='red')


if __name__ == '__main__':
    app = App()
    app.mainloop()
