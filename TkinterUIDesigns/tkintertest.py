import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.geometry("800x600")
title = tk.Label(root, text="My App", font=("Arial", 24))
title.pack(pady=20)

logo = PhotoImage(file="Button.png")
rect = PhotoImage(file="Entry.png")
label = tk.Button(root, 
                  image=logo,
                  borderwidth=0,
                  highlightthickness=0,
                  relief="flat",
                  bd=0)
label.pack()

label2 = tk.Entry(root)
label2.pack()

root.mainloop()