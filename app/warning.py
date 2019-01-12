import tkinter as tk
import settings

class WarningWin:
    def __init__(self, master, msg, *args, **kwargs):
        self.master = master
        self.msg = msg
        self.win = tk.Toplevel()
        self.config()
        self.create_widgets()

    def config(self):
        self.win.title("Warning!")

    def create_widgets(self):
        tk.Label(self.win, text=self.msg, font=("Lucida", 10)).pack(side="top", padx=5)


class CreateDirectory(WarningWin):
    def __init__(self, master, msg, *args, **kwargs):
        super().__init__(master, msg, *args, **kwargs)

    def create_widgets(self):
        #set a message
        tk.Label(self.win, text=self.msg, font=("Lucida", 10)).pack(side="top", padx=5)
        
        #create a confirm button
        tk.Button(self.win, text="Yes", width=settings.BUTTON_WIDTH, command=self.confirm_click).pack(side="right", padx=5, pady=5)
        
        #create a cancel button
        tk.Button(self.win, text="Cancel", width=settings.BUTTON_WIDTH, command=self.win.destroy()).pack(side="right", padx=5, pady=5)

    def confirm_click(self):
        pass