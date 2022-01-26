import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bai Thuc Hanh Truot File Text")
        self.geometry('453x600')
        self.resizable(False, False)
        style = ttk.Style()
        style.theme_use('classic')
        style.configure("Vertical.TScrollbar", background="green", bordercolor="red", arrowcolor="white")

        self.btn_open = tk.Button(self, text = 'Open Text File', command = self.btn_open_click)
        self.text = tk.Text(self, font = ('Calibri', 14), width = 42, wrap = tk.WORD)
        
        scroll_y = ttk.Scrollbar(self, orient = tk.VERTICAL, command = self.text.yview)
        self.text.config(yscrollcommand = scroll_y.set)

        self.btn_open.place(x = 5, y = 5)
        self.text.place(x = 5, y = 40)
        scroll_y.place(x = 430, y = 40, height = 558)

    def btn_open_click(self):
        f = open('Ho_Alphonse_de_Lamartine.txt', 'r', encoding = 'utf-8')
        content = f.read()
        f.close()
        self.text.insert(tk.INSERT, content)
        self.text.configure(state = tk.DISABLED)
        self.btn_open.configure(state = tk.DISABLED)


if __name__ == "__main__":
    app = App()
    app.mainloop()
