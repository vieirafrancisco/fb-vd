import os
import sys

## settings ##

## path
# download path
DOWNLOAD_PATH = os.getcwd()+"\\videos\\" if sys.platform == "win32" else os.getcwd()+"/videos/"

## widgets
BUTTON_WIDTH = 10
ENTRY_WIDTH = 50

# frame
FRAME_PADDING_X = 10
FRAME_PADDING_Y = 10

# log messages
LOG_MESSAGES = {
    "error": ("Erro: Download não pode ser concluido!", "red"),
    "processing": ("Download em progresso...", "blue"),
    "completed": ("Download completo!", "green")
}

