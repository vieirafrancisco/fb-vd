import requests
import urllib.request
import os
import tkinter as tk

import settings

from scrapping.request_url import Url
from tkinter.filedialog import askdirectory

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
        self.path_frame.grid(row=0, column=0, padx=settings.FRAME_PADDING_X, pady=settings.FRAME_PADDING_Y)

        tk.Label(self.path_frame, text="Rota do arquivo").grid(row=0, column=0)
        self.path_text = tk.Entry(self.path_frame, textvariable=self._file_path, width=settings.ENTRY_WIDTH)
        self.set_file_path(settings.DOWNLOAD_PATH) # changes the text of the path_text entry
        self.path_text.grid(row=1, column=0, padx=10)

        self.path_btn = tk.Button(self.path_frame, text="Browse", width=settings.BUTTON_WIDTH, command=self.browse_click)
        self.path_btn.grid(row=1, column=1)

        # download frame
        self.download_frame = tk.Frame(self)
        self.download_frame.grid(row=1, column=0, padx=settings.FRAME_PADDING_X, pady=settings.FRAME_PADDING_Y)

        tk.Label(self.download_frame, text="URL do vídeo").grid(row=0, column=0)
        self.url_entry = tk.Entry(self.download_frame, width=settings.ENTRY_WIDTH)
        self.url_entry.grid(row=1, column=0, padx=10)

        self.download_btn = tk.Button(self.download_frame, text="Download", width=settings.BUTTON_WIDTH, command=self.download_click)
        self.download_btn.grid(row=1, column=1)

        tk.Label(self.download_frame, text="Nome do arquivo").grid(row=2, column=0)
        self.file_name_entry = tk.Entry(self.download_frame, width=settings.ENTRY_WIDTH)
        self.file_name_entry.grid(row=3, column=0, padx=10)

        # log frame
        self.log_frame = tk.Frame(self)
        self.log_frame.grid(row=2, column=0,padx=settings.FRAME_PADDING_X, pady=settings.FRAME_PADDING_Y)

        self.log_label = tk.Label(self.log_frame, font=("Lucida", 12))
        self.log_label.grid(row=0, column=0)

        # control frame
        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=2, column=1, padx=settings.FRAME_PADDING_X, pady=settings.FRAME_PADDING_Y)

        self.cancel_btn = tk.Button(self.control_frame, text="Cancelar", width=settings.BUTTON_WIDTH, command=self.cancel_click)
        self.cancel_btn.grid(row=0, column=0, padx=5, pady=5)
        self.open_folder_btn = tk.Button(self.control_frame, text="Abrir Pasta",width=settings.BUTTON_WIDTH, command=self.open_folder_click)
        self.open_folder_btn.grid(row=1, column=0, padx=5, pady=5)

    def download_click(self):
        if(self.url_entry.get()):
            url = Url(self.url_entry.get()).get_url()
            
            if(requests.get(url)):
                try:
                    raw = requests.get(url, stream=True).raw
                    buffer = raw.read(1024)
                    with open(self.path_text.get()+self.file_name_entry.get()+'.mp4', "wb") as f:
                        while(buffer):
                            f.write(buffer)
                            buffer = raw.read(1024)
                    self.set_log_msg('completed')
                except Exception:
                    self.set_log_msg('error')

        else:
            self.set_log_msg('error')
 
    def cancel_click(self):
        self.master.destroy()

    def browse_click(self):
        self.master.withdraw() # hide the root
        dirname = askdirectory(initialdir=os.getcwd(),title="Selecione a pasta onde será salvo o vídeo")
        if len(dirname) > 0:
            self.set_file_path(dirname)
        self.master.deiconify() # show the root again

    def open_folder_click(self):
        os.startfile(self.path_text.get())

    def set_log_msg(self, log):
        msg = settings.LOG_MESSAGES[log]
        self.log_label['text'] = msg[0]
        self.log_label['foreground'] = msg[1]

    def set_file_path(self, new_path):
        self._file_path.set(new_path)
    