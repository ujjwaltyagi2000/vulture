import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

app_window = tk.Tk()
app_window.geometry("410x330")  # Size of the window 
app_window.title('VULTURE')
app_font=('calibri', 18, 'bold')
line1 = tk.Label(app_window,text='Upload Files & display',width=30,font=app_font)  
line1.grid(row=1,column=1,columnspan=4)
button = tk.Button(app_window, text='Upload Files', width=20,command = lambda:upload_file())
button.grid(row=2,column=1,columnspan=4)

def upload_file():
    file_types = [('jpg Files', '*.jpg'), ('png Files','*.png'), ('jpeg Files','*.jpeg')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(multiple=True,filetypes=file_types)
    col=1 # start from column 1
    row=3 # start from row 3 
    
    for file in filename:

        image=Image.open(file) # read the image file
        image=image.resize((100,100)) # new width & height
        image=ImageTk.PhotoImage(image)
        e1 =tk.Label(app_window)
        e1.grid(row=row,column=col)
        e1.image = image
        e1['image']=image # garbage collection 
        if(col==3): # start new line after third column
            row=row+1# start wtih next row
            col=1    # start with first column
        else:       # within the same row 
            col=col+1 # increase to next column                 
app_window.mainloop()  # Keep the window open