import os
import re
import platform

## settings ##

## path
# download path
if platform.system() == "Windows": #windows
    DOWNLOAD_PATH = 'D:/FbVideos/'
elif platform.system() == "Linux": #linux
    DOWNLOAD_PATH = '~/Documents/FbVideos/'
elif platform.system() == "Darwin": #mac
    #DOWNLOAD_PATH = '/Users/FbVideos/'
    pass

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

