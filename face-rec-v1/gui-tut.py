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

window.mainloop() # these three lines will open an application window



