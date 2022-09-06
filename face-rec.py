print('''__      ___    _ _   _______ _    _ _____  ______ 
 \ \    / / |  | | | |__   __| |  | |  __ \|  ____|
  \ \  / /| |  | | |    | |  | |  | | |__) | |__   
   \ \/ / | |  | | |    | |  | |  | |  _  /|  __|  
    \  /  | |__| | |____| |  | |__| | | \ \| |____ 
     \/    \____/|______|_|   \____/|_|  \_\______''')

import face_recognition as fr
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename # We will use this to give user the option to browse the image file
import numpy as np
import cv2
import os # will help find file directories

# which file to analyse:
Tk().withdraw()
load_image = askopenfilename()

target_image = fr.load_image_file(load_image) # image file to be analyzed
target_encoding = fr.face_encodings(target_image)

print(target_encoding)


