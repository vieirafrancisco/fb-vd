import tkinter as tk
from tkinter import ttk
from threading import Thread
import time

class ProgressBar:
    def __init__(self, frame):
        self.frame = frame

    def create_bar(self):
        self.thread = Thread(target=self.create)
        self.thread.start()

    def create(self):
        self.var = tk.IntVar()
        self.var.set(0)
        
        self.progress_bar = ttk.Progressbar(self.frame, variable=self.var, orient="horizontal", length=400)
        self.progress_bar.grid(row=1, column=0)

        self.update(self.var)

    def update(self, var):
        self.variable = var
        for i in range(0,9999999,1024):
            time.sleep(0.1)
            self.variable.set(i)
