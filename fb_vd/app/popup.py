import tkinter as tk
import subprocess
import sys
import os

from ..settings import *

class Popup:
    def __init__(self, msg, *args, **kwargs):
        self.msg = msg
        self.win = tk.Toplevel()
        self.config()
        self.create_widgets()

    def config(self):
        self.win.resizable(False, False)
        self.win.title("Warning!")

    def create_widgets(self):
        tk.Label(self.win, text=self.msg, font=("Lucida", 10)).pack(side="top", padx=5)
        tk.Button(self.win, text="Ok", width=BUTTON_WIDTH, command=self.win.destroy).pack(side="right", padx=5)


class CreateDirectory(Popup):
    def __init__(self, msg, ndir, *args, **kwargs):
        self.prev_win = kwargs["prev"]
        super().__init__(msg, *args, **kwargs)
        self.ndir = ndir

    def config(self):
        self.win.resizable(False, False)
        self.win.title("Create new directory")

        if self.prev_win:
            self.prev_win._toggle_state(state="disabled")

    def create_widgets(self):
        #set a message
        tk.Label(self.win, text=self.msg, font=("Lucida", 10)).pack(side="top", padx=5)
        
        #create a confirm button
        tk.Button(self.win, text="Sim", width=BUTTON_WIDTH, command=self.confirm_click).pack(side="right", padx=5, pady=5)
        
        #create a cancel button
        tk.Button(self.win, text="Cancelar", width=BUTTON_WIDTH, command=self.win.destroy).pack(side="right", padx=5, pady=5)

    def confirm_click(self):
        div = "\\" if sys.platform == "win32" else "/"

        directory_list = self.ndir.split(div)
        curr_dir = ''

        for directory in directory_list:
            curr_dir += directory+div
            if(not os.path.isdir(curr_dir)):
                subprocess.call(["mkdir", curr_dir]) 
        
        self.win.destroy()