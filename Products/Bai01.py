import tkinter as tk
from tkinter import messagebox as msg
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Bai Thuc Hanh Dau Tien')
        lbl_chao = tk.Label(self, text = 'Khoa CNTT - DHSPKT TP HCM\nChao mung cac ban SV khoa 2021',
        bg = 'white', fg = 'blue', relief = tk.SUNKEN, font = ('Calibri', 15))
        btn_thoat = tk.Button(self, text = 'Thoat', command = self.btn_thoat_click)

        lbl_chao.grid(row = 0, column = 0, padx = 10, pady = 10,
                      ipadx = 20, ipady = 20)
        btn_thoat.grid(row = 1, column = 0, padx = 10, pady = 10,
                      ipadx = 5, ipady = 5)
        self.protocol('WM_DELETE_WINDOW', self.btn_thoat_click)
        
    def btn_thoat_click(self):
        tra_loi = msg.askquestion('Question', 'Ban co muon thoat khong?')
        if tra_loi == 'yes':
            self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
