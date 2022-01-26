import tkinter as tk
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Bai Thuc Hanh So 6')

        self.menu = tk.Menu(self, tearoff = 0)
        self.menu.add_command(label="Select All", command = self.select_all)
        self.menu.add_command(label="Copy to Right", command = self.copy_to_right)
        self.menu.add_command(label="Move to Right", command = self.move_to_right)
        self.menu.add_command(label="Delete", command = self.delete_selected)

        self.so_luong_1 = 0
        self.so_luong_2 = 0

        lbl_trai_cay = tk.Label(self, text = 'Trai Cay')

        self.trai_cay = tk.StringVar()
        
        self.ent_trai_cay = tk.Entry(self, textvariable = self.trai_cay)

        btn_nhap = tk.Button(self, text = 'Nhap', command = self.btn_nhap_click)
        
        self.lst_trai_cay_1 = tk.Listbox(self, activestyle = tk.NONE, selectmode = tk.EXTENDED)

        self.lst_trai_cay_2 = tk.Listbox(self)
        self.lbl_so_luong_1 = tk.Label(self, text = 'So Luong: ')
        self.lbl_so_luong_2 = tk.Label(self, text = 'So Luong: ')

        lbl_trai_cay.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.ent_trai_cay.grid(row = 1, column = 0, padx = 5, pady = 5)
        btn_nhap.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.lst_trai_cay_1.grid(row = 3, column = 0, padx = 5, pady = 5)
        self.lst_trai_cay_2.grid(row = 3, column = 1, padx = 5, pady = 5)
        self.lbl_so_luong_1.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = tk.W)
        self.lbl_so_luong_2.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = tk.W)

        self.ent_trai_cay.focus_set()

        self.lst_trai_cay_1.bind("<Button-3>", self.show_popup)

    def show_popup(self, event):
        self.menu.post(event.x_root, event.y_root)

    def select_all(self):
        self.lst_trai_cay_1.select_set(0, tk.END)

    def delete_selected(self):
        dem = 0
        for i in self.lst_trai_cay_1.curselection()[::-1]:
            self.lst_trai_cay_1.delete(i)
            dem += 1
        self.so_luong_1 -= dem
        self.lbl_so_luong_1.configure(text = 'So Luong: %d' % (self.so_luong_1))

    def move_to_right(self):
        dem = 0
        for i in self.lst_trai_cay_1.curselection()[::-1]:
            trai_cay = self.lst_trai_cay_1.get(i)
            self.lst_trai_cay_2.insert(0, trai_cay)
            self.lst_trai_cay_1.delete(i)
            dem += 1
        self.so_luong_2 += dem
        self.lbl_so_luong_2.configure(text = 'So Luong: %d' % (self.so_luong_2))
        self.so_luong_1 -= dem
        self.lbl_so_luong_1.configure(text = 'So Luong: %d' % (self.so_luong_1))

    def copy_to_right(self):
        dem = 0
        for i in self.lst_trai_cay_1.curselection()[::-1]:
            trai_cay = self.lst_trai_cay_1.get(i)
            self.lst_trai_cay_2.insert(0, trai_cay)
            dem += 1
        self.so_luong_2 += dem
        self.lbl_so_luong_2.configure(text = 'So Luong: %d' % (self.so_luong_2))



    def btn_nhap_click(self):
        trai_cay = self.trai_cay.get()
        trai_cay = trai_cay.strip()
        if trai_cay == '':
            return
        self.lst_trai_cay_1.insert(tk.END, trai_cay)
        self.so_luong_1 += 1
        self.lbl_so_luong_1.configure(text = 'So Luong: %d' % (self.so_luong_1))
        self.ent_trai_cay.delete(0, tk.END)
        self.ent_trai_cay.focus_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()
