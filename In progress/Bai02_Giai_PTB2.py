import tkinter as tk
from tkinter import messagebox as msg

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Bai Thuc Hanh So 2')
        # widget: nut dieu khien
        lbl_nhap_a = tk.Label(self, text = 'Nhap a')  
        lbl_nhap_b = tk.Label(self, text = 'Nhap b')  
        lbl_nhap_c = tk.Label(self, text = 'Nhap c')
        lbl_nghiem = tk.Label(self, text = 'Nghiem')

        self.a = tk.StringVar()
        self.b = tk.StringVar()
        self.c = tk.StringVar()

        self.ent_nhap_a = tk.Entry(self, justify = tk.RIGHT, textvariable = self.a)
        self.ent_nhap_b = tk.Entry(self, justify = tk.RIGHT, textvariable = self.b)
        self.ent_nhap_c = tk.Entry(self, justify = tk.RIGHT, textvariable = self.c)
 
        self.lbl_ket_qua = tk.Label(self, bg = 'white', relief = tk.SUNKEN)

        btn_giai = tk.Button(self, text = 'Giai', width = 7, command = self.btn_giai_click)
        btn_xoa = tk.Button(self, text = 'Xoa', width = 7, command = self.btn_xoa_click)
        btn_thoat = tk.Button(self, text = 'Thoat', width = 7)

        lbl_nhap_a.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.W)
        lbl_nhap_b.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = tk.W)
        lbl_nhap_c.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = tk.W)
        lbl_nghiem.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = tk.W)

        self.ent_nhap_a.grid(row = 0, column = 1, padx = 10, pady = 10, ipady = 3)
        self.ent_nhap_b.grid(row = 1, column = 1, padx = 10, pady = 10, ipady = 3)
        self.ent_nhap_c.grid(row = 2, column = 1, padx = 10, pady = 10, ipady = 3)

        self.lbl_ket_qua.grid(row = 3, column = 1, columnspan = 2, padx = 10, 
                         pady = 10, ipady = 3, sticky = tk.NSEW)
        btn_giai.grid(row = 0, column = 2, padx = 10, pady = 10, ipadx = 10)
        btn_xoa.grid(row = 1, column = 2, padx = 10, pady = 10, ipadx = 10)
        btn_thoat.grid(row = 2, column = 2, padx = 10, pady = 10, ipadx = 10)

        self.ent_nhap_a.focus_set()

    def btn_giai_click(self):
        def isfloat(value):
            value_num = 0.0
            try:
                value_num = float(value)
                return True, value_num
            except ValueError:
                return False, value_num

        value_a = self.a.get()
        value_b = self.b.get()
        value_c = self.c.get()
 
        result, a = isfloat(value_a)
        if result == False:
            msg.showerror('Error', 'Ban phai nhap a la chu so!')
            self.ent_nhap_a.focus_set()
            return

        result, b = isfloat(value_b)
        if result == False:
            msg.showerror('Error', 'Ban phai nhap b la chu so!')
            self.ent_nhap_b.focus_set()
            return

        result, c = isfloat(value_c)
        if result == False:
            msg.showerror('Error', 'Ban phai nhap c la chu so!')
            self.ent_nhap_c.focus_set()
            return

        d = a + b + c
        s = '%.2f' % d
        self.lbl_ket_qua.configure(text = s)

    def btn_xoa_click(self):
        self.ent_nhap_a.delete(0, tk.END)
        self.ent_nhap_b.delete(0, tk.END)
        self.ent_nhap_c.delete(0, tk.END)
        self.lbl_ket_qua.configure(text = '')
        self.ent_nhap_a.focus_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()
