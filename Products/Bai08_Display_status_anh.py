from fileinput import filename
import tkinter as tk
from tkinter import *
from tkinter import PhotoImage, filedialog
from PIL import ImageTk, Image


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x420')
        self.title('Bai 8: Display status anh')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.canvas = tk.Canvas(
            self, width=392, height=392, relief=tk.SUNKEN, bd=2)

        self.canvas.rowconfigure(0, weight=1)
        self.canvas.columnconfigure(0, weight=1)
        self.lbl_address = tk.Label(self, text='Filename')
        self.lbl_size = tk.Label(self, text='WxH')

        self.canvas.grid(row=0, column=0, columnspan=2,
                         sticky=tk.NSEW, pady=(0, 20))
        self.lbl_address.grid(row=0, column=0, sticky=tk.S+tk.W)
        self.lbl_size.grid(row=0, column=1, sticky=tk.S + tk.E)

        # create menu
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open Image", command=self.openImage)
        filemenu.add_command(label="Clear Image", command=self.clearImage)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.destroy)
        menubar.add_cascade(label="File", menu=filemenu)

        self.config(menu=menubar)

        self.lbl = tk.Label(self.canvas)
        self.lbl.grid(row=0, column=0)

        self.H = 400
        self.W = 400

        self.canvas.bind('<Configure>', self.configure)
        self.img_original = ''

    def openImage(self):
        f_types = [('Image Files', '*.jpg *.png *.jpeg')]
        self.fileName = filedialog.askopenfilename(filetypes=f_types)
        self.img_original = Image.open(self.fileName)
        self.img_original2 = self.img_original
        img_resized = self.img_original2.resize((self.W-10, self.H-10))
        img = ImageTk.PhotoImage(img_resized)
        self.lbl.configure(image=img)
        self.lbl.image = img

        self.lbl_address.configure(
            text='{fileName}'.format(fileName=self.fileName))
        self.lbl_size.configure(text='{W}x{H}'.format(W=self.W-8, H=self.H-8))

    def clearImage(self):
        self.lbl.destroy()
        self.lbl_address.configure(text='Filename')
        self.lbl_size.configure(text='WxH')
        self.lbl = tk.Label(self.canvas)
        self.lbl.grid(row=0, column=0)
        self.img_original = ''

    def configure(self, event):
        self.H = event.height
        self.W = event.width
        if self.img_original != '':
            self.img_original2 = self.img_original
            img_resized = self.img_original2.resize((self.W-10, self.H-10))
            img = ImageTk.PhotoImage(img_resized)
            self.lbl.configure(image=img)
            self.lbl.image = img
            self.lbl_address.configure(
                text='{fileName}'.format(fileName=self.fileName))
            self.lbl_size.configure(
                text='{W}x{H}'.format(W=self.W-8, H=self.H-8))


if __name__ == '__main__':
    app = App()
    app.mainloop()
