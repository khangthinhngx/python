import tkinter as tk
from tkinter import messagebox as msg
import numpy as np

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Bai Thuc Hanh So 4')
        self.geometry('385x286')
        self.matran = None
        self.content = None
        
        btn_open = tk.Button(self, text = 'Open', width = 10, command = self.btn_open_click)
        self.lbl_matran = tk.Label(self, bg = 'white', relief = tk.SUNKEN, 
                width = 40, height = 10, anchor = tk.NW, justify = tk.LEFT,
                font = ('Consolas', 12))

        btn_cong = tk.Button(self, text = 'Cong', width = 10, command = self.btn_cong_click)
        btn_save = tk.Button(self, text = 'Save', width = 10, command = self.btn_save_click)

        btn_open.place(x = 10, y = 10)
        self.lbl_matran.place(x = 10, y = 45)
        btn_cong.place(x = 10, y = 250)
        btn_save.place(x = 295, y = 250)


    def btn_open_click(self):
        f = open('./matran.txt', 'r')
        content = f.read()
        f.close()
        content = content.splitlines()
        size = content[0]
        size = size.split()
        m = int(size[0])
        n = int(size[1])
        a = np.zeros((m, n), np.float)
        for i in range(0, m):
            line = content[i+1]
            line = line.split()
            for j in range(0, n):
                a[i,j] = float(line[j])

        self.matran = a

        content = '%d %d\n' % (m, n)
        for i in range(0, m):
            for j in range(0, n):
                content = content + '%8.2f' % a[i,j]
            content = content + '\n'

        self.lbl_matran.configure(text = content)

    def btn_cong_click(self):
        a = self.matran
        m, n = a.shape
        content = '%d %d\n' % (m, n)
        for i in range(0, m):
            for j in range(0, n):
                content = content + '%8.2f' % a[i,j]
            content = content + '\n'
        content = content + '-'*32 + '\n'
        line = np.sum(a, axis = 0)
        for x in line:
            content = content + '%8.2f' % x
        content = content + '\n'
        self.content = content
        self.lbl_matran.configure(text = content)

    def btn_save_click(self):
        f = open('ketqua.txt', 'w')
        f.write(self.content)
        f.close()
        msg.showinfo('Thong Bao', 'Ban da ghi xong!')


if __name__ == "__main__":
    app = App()
    app.mainloop()
