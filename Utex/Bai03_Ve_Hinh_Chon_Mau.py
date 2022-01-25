import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Bai Thuc Hanh So 3')
        self.geometry('445x325')
        self.resizable(False, False)

        self.figure = tk.StringVar()
        self.figure.set('Tam Giac')

        self.cvs_figure = tk.Canvas(self, bg = 'white', bd = 1, relief = tk.SUNKEN, 
                               width = 300, height = 300 )

        lfrm_figure = tk.LabelFrame(self, text = 'Figure')
        rbtn_tam_giac = tk.Radiobutton(lfrm_figure, text = 'Tam Giac', width = 8, 
        anchor = tk.W, value = 'Tam Giac', variable = self.figure, command = self.xu_ly)

        rbtn_tron = tk.Radiobutton(lfrm_figure, text = 'Tron', width = 8, 
        anchor = tk.W, value = 'Tron', variable = self.figure, command = self.xu_ly)
        rbtn_chu_nhat = tk.Radiobutton(lfrm_figure, text = 'Chu Nhat', width = 8, 
        anchor = tk.W, value = 'Chu Nhat', variable = self.figure, command = self.xu_ly)

        lfrm_color = tk.LabelFrame(self, text = 'Color')

        self.red = tk.IntVar()
        self.green = tk.IntVar()
        self.blue = tk.IntVar()

        chk_red = tk.Checkbutton(lfrm_color, text = 'Red', width = 8, anchor = tk.W, 
                    variable = self.red, command = self.xu_ly)
        chk_green = tk.Checkbutton(lfrm_color, text = 'Green', width = 8, anchor = tk.W,
                    variable = self.green, command = self.xu_ly)
        chk_blue = tk.Checkbutton(lfrm_color, text = 'Blue', width = 8, anchor = tk.W, 
                    variable = self.blue, command = self.xu_ly)
        chk_red.select()

        self.cvs_figure.place(x = 10, y = 10)
        lfrm_figure.place(x = 326, y = 4)
        rbtn_tam_giac.grid(row = 0, padx = 10, pady = 5)
        rbtn_tron.grid(row = 1, padx = 10, pady = 5)
        rbtn_chu_nhat.grid(row = 2, padx = 10, pady = 5)

        lfrm_color.place(x = 326, y = 191)
        chk_red.grid(row = 0, padx = 10, pady = 5)
        chk_green.grid(row = 1, padx = 10, pady = 5)
        chk_blue.grid(row = 2, padx = 10, pady = 5)

        self.cvs_figure.update()

        W = self.cvs_figure.winfo_width() - 2
        H = self.cvs_figure.winfo_height() - 2
        #     R    G    B
        #    FF   00   00
        #    color = '#FF0000'
        R = 255
        G = 0
        B = 0
        color = '#%02X%02X%02X' % (R, G, B)
        # cvs_figure.create_oval(10, 10, W-10, H-10, outline = color, fill = color)
        # cvs_figure.create_rectangle(10, 10, W-10, H-10, outline = color, fill = color)
        points = [10, H-10, W // 2, 10, W-10, H-10]
        self.cvs_figure.create_polygon(points, outline = color, fill = color)

    def xu_ly(self):
        self.cvs_figure.delete('all')
        self.cvs_figure.update()
        color = '#'
        if self.red.get() == 1:
            color = color + 'FF'
        else:
            color = color + '00'

        if self.green.get() == 1:
            color = color + 'FF'
        else:
            color = color + '00'
    
        if self.blue.get() == 1:
            color = color + 'FF'
        else:
            color = color + '00'

        W = self.cvs_figure.winfo_width() - 2
        H = self.cvs_figure.winfo_height() - 2
        if self.figure.get() == 'Tam Giac':
            points = [10, H-10, W // 2, 10, W-10, H-10]
            self.cvs_figure.create_polygon(points, outline = color, fill = color)
        elif self.figure.get() == 'Tron':
            self.cvs_figure.create_oval(10, 10, W-10, H-10, outline = color, fill = color)
        else:
            self.cvs_figure.create_rectangle(10, 10, W-10, H-10, outline = color, fill = color)

if __name__ == "__main__":
    app = App()
    app.mainloop()
