import tkinter as tk

BUTTON_WIDTH = 10
ENTRY_WIDTH = 50
LOG_MESSAGES = {
    "error": ("Erro: Download não pode ser concluido!", "red"),
    "processing": ("Download em progresso...", "blue"),
    "completed": ("Download completo!", "green")
}
PADDING_FRAME_X = 10
PADDING_FRAME_Y = 10

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
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
        self.path_frame.grid(row=0, column=0, padx=PADDING_FRAME_X, pady=PADDING_FRAME_Y)

        self.file_path = tk.StringVar()

        tk.Label(self.path_frame, text="Rota do arquivo").grid(row=0,column=0)
        self.path_text = tk.Entry(self.path_frame, textvariable=self.file_path, width=ENTRY_WIDTH)
        self.file_path.set("D:/FbVideos/")
        self.path_text.grid(row=1,column=0, padx=10)

        self.path_btn = tk.Button(self.path_frame, text="Browse", width=BUTTON_WIDTH, command=self.browse_click) 
        self.path_btn.grid(row=1, column=1) 

        # download frame
        self.download_frame = tk.Frame(self)
        self.download_frame.grid(row=1, column=0, padx=PADDING_FRAME_X, pady=PADDING_FRAME_Y)

        tk.Label(self.download_frame, text="URL do vídeo").grid(row=0, column=0)
        self.url_entry = tk.Entry(self.download_frame, width=ENTRY_WIDTH)
        self.url_entry.grid(row=1, column=0, padx=10)

        self.download_btn = tk.Button(self.download_frame, text="Download", width=BUTTON_WIDTH, command=self.download_click)
        self.download_btn.grid(row=1, column=1)

        tk.Label(self.download_frame, text="Nome do arquivo").grid(row=2, column=0)
        self.file_name_entry = tk.Entry(self.download_frame, width=ENTRY_WIDTH)
        self.file_name_entry.grid(row=3, column=0, padx=10)

        self.enter_name_btn = tk.Button(self.download_frame, text="Enter", width=BUTTON_WIDTH, command=self.enter_name_click)
        self.enter_name_btn.grid(row=3, column=1)

        # log frame
        self.log_frame = tk.Frame(self)
        self.log_frame.grid(row=2, column=0, padx=PADDING_FRAME_X, pady=PADDING_FRAME_Y)

        self.log_label = tk.Label(self.log_frame, text=LOG_MESSAGES['completed'][0], font=("Lucida", 12), foreground=LOG_MESSAGES['completed'][1])
        self.log_label.grid(row=0,column=0)

        # control frame
        self.control_frame = tk.Frame(self)
        self.control_frame.grid(row=2, column=1, padx=PADDING_FRAME_X, pady=PADDING_FRAME_Y)

        self.cancel_btn = tk.Button(self.control_frame, text="Cancelar", width=BUTTON_WIDTH, command=self.cancel_click)
        self.cancel_btn.grid(row=0, column=0,padx=5,pady=5)
        self.open_folder_btn = tk.Button(self.control_frame, text="Abrir Pasta", width=BUTTON_WIDTH, command=self.open_file_click, state='disabled')
        self.open_folder_btn.grid(row=1, column=0, padx=5, pady=5)

    def download_click(self):
        print(self.url_entry.get())

    def cancel_click(self):
        self.master.destroy()

    def browse_click(self):
        pass

    def open_file_click(self):
        pass

    def enter_name_click(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()
