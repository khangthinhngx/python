import tkinter as tk
import tkcalendar

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bai Thuc Hanh So 5")
        self.geometry('595x400')
        self.resizable(False, False)
        lbl_ho_ten = tk.Label(self, text = 'Ho Ten')
        lbl_ngay_sinh = tk.Label(self, text = 'Ngay Sinh')
        lbl_gioi_tinh = tk.Label(self, text = 'Gioi Tinh')
        lbl_diem = tk.Label(self, text = 'Diem')
        lbl_danh_sach = tk.Label(self, text = 'Danh Sach')
        self.so_sv = 0
        self.lbl_so_sv = tk.Label(self, text = 'So SV:')
        
        self.ho_ten = tk.StringVar()
        self.ent_ho_ten = tk.Entry(self, textvariable = self.ho_ten, width = 35)

        self.ngay_sinh = tk.StringVar()
        self.ent_ngay_sinh = tkcalendar.DateEntry(self, date_pattern = 'dd/mm/yyyy',
        day = 1, month = 1, year = 2003, textvariable = self.ngay_sinh)

        self.gioi_tinh = tk.IntVar()
        self.chk_gioi_tinh = tk.Checkbutton(self, variable = self.gioi_tinh)

        self.diem = tk.StringVar()
        self.ent_diem = tk.Entry(self, textvariable = self.diem, width = 15, justify = tk.RIGHT)

        self.lst_danh_sach = tk.Listbox(self, width = 57, font = ('Courier New', 12),
                                        activestyle = tk.NONE)
        
        btn_nhap = tk.Button(self, text = 'Nhap', width = 8, command = self.btn_nhap_click)

        lbl_ho_ten.place(x = 10, y = 10)
        lbl_ngay_sinh.place(x = 10, y = 45)
        lbl_gioi_tinh.place(x = 10, y = 75)
        lbl_diem.place(x = 10, y = 105)
        lbl_danh_sach.place(x = 10, y = 145)
        self.lbl_so_sv.place(x = 10, y = 370)


        self.ent_ho_ten.place(x = 100, y = 10)
        self.ent_ngay_sinh.place(x = 100, y = 45)
        self.chk_gioi_tinh.place(x = 95, y = 75)
        self.ent_diem.place(x = 100, y = 105)
        self.lst_danh_sach.place(x = 10, y = 165)
        btn_nhap.place(x = 519, y = 9, height = 22)
        self.ent_ho_ten.focus_set()

    def btn_nhap_click(self):
        ho_ten = self.ho_ten.get().strip()
        if ho_ten == "":
            return

        ho_ten = ho_ten.split()
        ten = ho_ten[-1]
        ho = ''
        for x in ho_ten[:-1]:
            ho = ho + x + ' '
        ho = ho.strip()
        ho = ho + ' '*(25-len(ho))
        ten = ten + ' '*(10 - len(ten))
        ho_ten = ho + ten
        ngay_sinh = self.ngay_sinh.get()
        gioi_tinh = 'Nam'
        if self.gioi_tinh.get() == 1:
            gioi_tinh = 'Nu '
        
        diem = self.diem.get().strip()
        if diem == "":
            return

        diem = float(diem)
        diem = '%8.1f' % diem
        content = ho + ten + ngay_sinh + ' ' + gioi_tinh + diem
        self.lst_danh_sach.insert(tk.END, content)
        self.so_sv += 1

        self.lbl_so_sv.configure(text = 'So SV: %d' % self.so_sv)

        self.ent_ho_ten.delete(0, tk.END)
        self.ent_ngay_sinh.set_date('01/01/2003')
        self.chk_gioi_tinh.deselect()
        self.ent_diem.delete(0, tk.END)
        self.ent_ho_ten.focus_set()

if __name__ == "__main__":
    app = App()
    app.mainloop()
