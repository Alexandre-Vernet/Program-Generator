import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text, simpledialog
import os

root = tk.Tk()
root.title("Program Generator")
root.geometry("300x450")
root.minsize(300, 450)


def createProjectAngular():

    # Set repository destination
    fileName = filedialog.askdirectory(
        initialdir="C:/Users/alexa/Documents/Dev/Web/Front/Angular/", title="Select file")
    print(fileName)

    # Set project name
    projectName = simpledialog.askstring(title="Name",
                                         prompt="Quel est le nom de votre programme ? ")

    # Generate project
    os.system("cmd /c cd " + fileName)
    os.system("cmd /c ng new " + projectName +
              " --style=scss --routing --strict")

    # Open in VS Code
    # os.system("cmd /c cd " + "projectName")
    # os.system("cmd /c code .")

    # # # Start server
    # os.system("cmd /c ng serve")


frame = tk.Frame(root, bg="#4065A4").place(relwidth=1, relheight=1)

title = Label(root, text="Program Generator",
              font=("Courrier, 25"), fg="red", bg="#4065A4").pack()

btnAngular = tk.Button(frame, text="Angular", padx=10,
                       pady=5, fg="white", bg="#c3002f", font=("Courrier, 14"), command=createProjectAngular).pack(fill=X, expand=YES)

btnLaravel = tk.Button(frame, text="Laravel", padx=10,
                       pady=5, fg="white", bg="#ff2d20", font=("Courrier, 14"), command=createProjectAngular).pack(fill=X, expand=YES)

btnReactNative = tk.Button(frame, text="React Native", padx=10,
                           pady=5, fg="white", bg="#61dafb", font=("Courrier, 14"), command=createProjectAngular).pack(fill=X, expand=YES)

btnIonic = tk.Button(frame, text="Ionic", padx=10,
                     pady=5, fg="white", bg="#4e8df7", font=("Courrier, 14"), command=createProjectAngular).pack(fill=X, expand=YES)


root.mainloop()
