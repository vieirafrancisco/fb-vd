import tkinter as tk
from app.gui import Gui

if __name__ == "__main__":
    root = tk.Tk()
    app = Gui(root)
    app.mainloop()