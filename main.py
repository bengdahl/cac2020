import tkinter as tk

w = tk.Tk()
w['width'] = 300
w['height'] = 400

label = tk.Label(w, text="Hello world")
label.pack()

w.mainloop()