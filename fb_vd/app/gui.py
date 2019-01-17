import requests
import urllib.request
import os
import sys
import subprocess
import re
import tkinter as tk
import time

from ..settings import *

from .progress_bar import ProgressBar
from .popup import Popup, CreateDirectory
from ..scrapping.request_url import Url
from ..scrapping.url_exception import URLException

from tkinter.filedialog import askdirectory
from tkinter import ttk

class Gui(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self._file_path = tk.StringVar()
        self.config()
        self.pack()
        self.create_widgets()

    def config(self):
        self.master.title("Download vídeos Facebook")
        self.master.resizable(False, False)
        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth())//2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight())//2
        self.master.geometry(f"{x}x{y}")

        self.master.protocol('WM_DELETE_WINDOW', self.cancel_click)

    def create_widgets(self):
        # path frame
        self.path_frame = tk.Frame(self)
        self.path_frame.grid(row=0, column=0, padx=FRAME_PADDING_X, pady=FRAME_PADDING_Y)

        tk.Label(self.path_frame, text="Rota do arquivo").grid(row=0, column=0)
        self.path_text = tk.Entry(self.path_frame, textvariable=self._file_path, width=ENTRY_WIDTH)
        self.set_file_path(DOWNLOAD_PATH) # changes the text of the path_text entry
        self.path_text.grid(row=1, column=0, padx=10)

        self.path_btn = tk.Button(self.path_frame, text="Browse", width=BUTTON_WIDTH, command=self.browse_click)
        self.path_btn.grid(row=1, column=1)

        # download frame
        self.download_frame = tk.Frame(self)
        self.download_frame.grid(row=1, column=0, padx=FRAME_PADDING_X, pady=FRAME_PADDING_Y)

        tk.Label(self.download_frame, text="URL do vídeo").grid(row=0, column=0)
        self.url_entry = tk.Entry(self.download_frame, width=ENTRY_WIDTH)
        self.url_entry.grid(row=1, column=0, padx=10)

        self.download_btn = tk.Button(self.download_frame, text="Download", width=BUTTON_WIDTH, command=self.download_click)
        self.download_btn.grid(row=1, column=1)

        tk.Label(self.download_frame, text="Nome do arquivo").grid(row=2, column=0)
        self.file_name_entry = tk.Entry(self.download_frame, width=ENTRY_WIDTH)
        self.file_name_entry.grid(row=3, column=0, padx=10)

        # control frame
        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=2, column=0,padx=FRAME_PADDING_X, pady=FRAME_PADDING_Y)

        self.log_label = tk.Label(self.control_frame, font=("Lucida", 10))
        self.log_label.grid(row=0, column=0, pady=5)

        self.progress_bar = ttk.Progressbar(self.control_frame, orient="horizontal", length=400, mode='determinate')
        self.progress_bar.grid(row=1, column=0, padx=10)

        self.cancel_btn = tk.Button(self.control_frame, text="Cancelar", width=BUTTON_WIDTH, command=self.cancel_click)
        self.cancel_btn.grid(row=0, column=1, padx=5, pady=5)

        self.open_folder_btn = tk.Button(self.control_frame, text="Abrir Pasta",width=BUTTON_WIDTH, command=self.open_folder_click)
        self.open_folder_btn.grid(row=1, column=1, padx=5, pady=5)

    def download_click(self):
        if(self.url_entry.get()):
            try:
                url = Url(self.url_entry.get())
                
                if(requests.get(url.get_url())):
                    try:
                        raw = requests.get(url.get_url(), stream=True).raw
                        buffer = raw.read(1024)
                        file_name = self.file_name_entry.get() if self.file_name_entry.get() else url.get_default_name()
                        
                        down_path = self.path_text.get()

                        if down_path[-1] != "\\" and down_path[-1] != "/":
                            down_path = down_path+"\\" if sys.platform == "win32" else down_path+"/"

                        if(os.path.isdir(down_path)):
                            with open(down_path+file_name+'.mp4', "wb") as f:
                                while(buffer):
                                    f.write(buffer)
                                    buffer = raw.read(1024)
                            self.set_log_msg(LOG_MESSAGES['completed'][0], 'green')
                        else:
                            self._create_directory(down_path)
                        
                    except FileNotFoundError:
                        self.set_log_msg("Directory not found!", "red")
                    except Exception as e:
                        self.set_log_msg(e, 'red')
            except URLException as e:
                self.set_log_msg(e, 'red')

        else:
            self.set_log_msg(LOG_MESSAGES['error'][0], 'red')
 
    def cancel_click(self):
        self.master.destroy()

    def browse_click(self):
        self.master.withdraw() # hide the root
        dirname = askdirectory(initialdir=os.getcwd(),title="Selecione a pasta onde será salvo o vídeo")
        if len(dirname) > 0:
            self.set_file_path(dirname)
        self.master.deiconify() # show the root again

    def open_folder_click(self):
        filepath = self.path_text.get()

        if sys.platform == "win32":
            os.startfile(filepath)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.Popen([opener, filepath])

    def set_log_msg(self, log=None, color='black'):
        if log:
            self.log_label['text'] = log
            self.log_label['foreground'] = color
        else:
            self.log_label['text'] = ''

    def set_file_path(self, new_path):
        self._file_path.set(new_path)

    def _create_directory(self, path):
        msg = f"Não existe um diretório chamado {path}, deseja criar?"
        CreateDirectory(msg, path, prev=self)

    def _toggle_state(self, state="normal"):
        pass