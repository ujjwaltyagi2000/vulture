import tkinter as tk

window = tk.Tk() # creates window

window.geometry("800x500")
window.title("Vulture")

label = tk.Label(window, text="VULTURE", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(window, height=3, font=('Arial', 16))
textbox.pack(padx=20, pady=20)

button = tk.Button(window, text="Upload an Image", font=('Arial', 18))
button.pack(padx=10, pady=10)

buttonframe = tk.Frame(window)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

bt1 = tk.Button(buttonframe, text = "1", font = ('Arial', 18))
bt1.grid(row=0,column=0,sticky=tk.W+tk.E)

bt2 = tk.Button(buttonframe, text = "2", font = ('Arial', 18))
bt2.grid(row=0,column=1,sticky=tk.W+tk.E)

bt3 = tk.Button(buttonframe, text = "3", font = ('Arial', 18))
bt3.grid(row=0,column=2,sticky=tk.W+tk.E)

bt4 = tk.Button(buttonframe, text = "4", font = ('Arial', 18))
bt4.grid(row=1,column=0,sticky=tk.W+tk.E)

bt5 = tk.Button(buttonframe, text = "5", font = ('Arial', 18))
bt5.grid(row=1,column=1,sticky=tk.W+tk.E)

bt6 = tk.Button(buttonframe, text = "6", font = ('Arial', 18))
bt6.grid(row=1,column=2,sticky=tk.W+tk.E)

buttonframe.pack(fill="x")

window.mainloop() # these three lines will open an application window



