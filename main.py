import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, Text, simpledialog
import os
import time
from generate import generate

# Set window
root = tk.Tk()
root.title("Program Generator")
root.geometry("300x450")
root.minsize(300, 450)
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='img/icon.png'))

# Background
frame = tk.Frame(root, bg="#4065A4").place(relwidth=1, relheight=1)

# Title
title = Label(root, text="Program Generator", font=("Courrier, 25"), fg="red", bg="#4065A4").pack()

# Font
fontBtn = "Courrier, 14"


# Generate buttons
tk.Button(frame, text="Angular", padx=10,
          pady=5, fg="white", bg="#c3002f", font=(fontBtn), command=lambda: generate("angular")).pack(fill=X, expand=YES)

tk.Button(frame, text="React", padx=10,
        pady=5, fg="white", bg="#61DAFB", font=(fontBtn), command=lambda: generate("react")).pack(fill=X, expand=YES)

tk.Button(frame, text="NodeJS", padx=10,
        pady=5, fg="white", bg="#79B461", font=(fontBtn), command=lambda: generate("node")).pack(fill=X, expand=YES)

tk.Button(frame, text="Laravel", padx=10,
          pady=5, fg="white", bg="#ff2d20", font=(fontBtn), command=lambda: generate("laravel")).pack(fill=X, expand=YES)

tk.Button(frame, text="Ionic", padx=10,
          pady=5, fg="white", bg="#4e8df7", font=(fontBtn), command=lambda: generate("ionic")).pack(fill=X, expand=YES)


root.mainloop()
