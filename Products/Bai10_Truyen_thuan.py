import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Bai 12: Truyen thuan')
        self.geometry('380x150')
        self.resizable(FALSE, FALSE)

        self.radius_input = tk.StringVar()

        self.lbl_nhap = tk.Label(self, text='Nhap ban kinh', font=(10))
        self.entry = tk.Entry(self, width=15, font=(10), justify=tk.RIGHT)
        self.btn_draw = tk.Button(
            self, width=10, text='Ve hinh', font=(10), command=self.draw)

        self.lbl_nhap.place(x=20, y=30)
        self.entry.place(x=180, y=30)
        self.btn_draw.place(x=125, y=80)

    def draw(self):
        # kiem tra input
        def isFloat(value):
            answer = 0.0
            try:
                answer = float(value)
                return True, answer
            except ValueError:
                return False, answer

        value_get = self.entry.get()
        check, value = isFloat(value_get)
        if check == False:
            msg.showwarning('Sai input', 'Ban phai nhap chu so')
            self.entry.focus_set()
            return
        else:
            value = int(value)
            # tao cua so moi
            self.newWin = Toplevel(self)
            self.newWin.geometry('{w}x{h}'.format(w=2*value+30, h=2*value+60))
            self.newWin.resizable(FALSE, FALSE)
            self.newWin.focus_force()

            # tao canvas moi
            self.canvas = tk.Canvas(
                self.newWin, relief=tk.SUNKEN, bd=2, width=2*value+24, height=2*value+24)
            # ve hinh tron
            self.canvas.create_oval(
                15, 15, 2*value+15, 2*value+15, fill='red', outline='red')
            self.btn = tk.Button(self.newWin, text='OK',
                                 command=self.clear, width=5)

            #grid
            self.btn.grid(row=1, column=0)
            self.canvas.grid(row=0, column=0)

    # clear input
    def clear(self):
        self.newWin.destroy()
        self.entry.delete(0, 'end')


if __name__ == '__main__':
    app = App()
    app.mainloop()
