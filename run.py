import tkinter as tk
from fb_vd.app.gui import Gui

if __name__ == "__main__":
    root = tk.Tk()
    app = Gui(root)
    app.mainloop()