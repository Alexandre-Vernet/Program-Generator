import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("My app")


def createProjectAngular():
    # Set repository destination
    # os.system('cmd /k cd C:/Users/alexa/Documents/Dev/Web/Front/Angular/')

    # Generate project
    os.system('cmd /k ng new C:/Users/alexa/Documents/Dev/Web/Front/Angular/couocu --style=scss --routing --strict')

    # # Open in VS Code
    # os.system('cmd /k cd ' + "projectName")
    # os.system('cmd /k code .')

    # # Start server
    # os.system('cmd /k ng serve')


def generatePath():

    fileName = filedialog.askdirectory(
        initialdir="C:/Users/alexa/Documents/Dev/Web/Front/Angular/", title="Select file")

    os.system("cmd /c cd " + fileName)
    os.system('cmd /c ng new coucou --style=scss --routing --strict')


frame = tk.Frame(root, bg="white")
frame.place(relwidth=1, relheight=1)

btnAngular = tk.Button(frame, text="Angular", padx=10,
                       pady=5, fg="white", bg="#FF0000", command=createProjectAngular).pack()

openFile = tk.Button(frame, text="Open File", padx=10, pady=5,
                     fg="white", bg="#263D42", command=generatePath).pack()

root.mainloop()
