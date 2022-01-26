import tkinter as tk
from tkinter import *
from tkinter import PhotoImage, filedialog, ttk
from PIL import ImageTk, Image


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Bai 9: Scroll anh')
        self.geometry('620x620')
        self.resizable(FALSE, FALSE)

        self.canvas = tk.Canvas(
            self, width=592, height=592, relief=SUNKEN, bd=2)
        self.canvas.grid(row=0, column=0)

        # create menu
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open Image", command=self.openImage)
        filemenu.add_command(label="Clear Image", command=self.clearImage)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)

        self.scroll_y = ttk.Scrollbar(
            self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scroll_y.place(x=598, y=4, height=598)

        self.scroll_x = ttk.Scrollbar(
            self, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scroll_x.place(x=4, y=598, width=598)

        self.canvas.config(xscrollcommand=self.scroll_x.set)
        self.canvas.config(yscrollcommand=self.scroll_y.set)

    def openImage(self):
        f_types = [('Image Files', '*.jpg *.png *.jpeg')]
        self.fileName = filedialog.askopenfilename(filetypes=f_types)
        self.img_original = Image.open(self.fileName)
        img = ImageTk.PhotoImage(self.img_original)
        self.canvas.create_image(20, 20, image=img, anchor='nw')
        self.canvas.image = img
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

    def clearImage(self):
        self.canvas.delete('all')


if __name__ == '__main__':
    app = App()
    app.mainloop()
