import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, Text, simpledialog
import os
import time


# Set window
root = tk.Tk()
root.title("Program Generator")
root.geometry("300x450")
root.minsize(300, 450)
root.tk.call('wm', 'iconphoto', root._w,
             tk.PhotoImage(file='img/icon.png'))

frame = tk.Frame(root, bg="#4065A4").place(relwidth=1, relheight=1)

title = Label(root, text="Program Generator",
              font=("Courrier, 25"), fg="red", bg="#4065A4").pack()

# Set home path
homepath = os.path.expanduser(os.getenv('USERPROFILE'))


def generateProject(project):

    # Angular
    if project == "angular":

        # Set repository destination
        fileName = filedialog.askdirectory(
            title="Target project", initialdir=homepath + "/Documents/Dev/Web/Front/Angular")

        if fileName.strip():
            # Set project name
            projectName = simpledialog.askstring(title="Name",
                                                 prompt="What's the name of your project ? ")

            # Generate project
            os.chdir(fileName)
            os.system("cmd /c ng new " + projectName +
                      " --style=scss --routing --strict")

    # React
    if project == "react":

        # Set repository destination
        fileName = filedialog.askdirectory(
            title="Target project", initialdir=homepath + "/Documents/Dev/Web/Front/React")

        if fileName.strip():
            # Set project name
            projectName = simpledialog.askstring(title="Name",
                                                 prompt="What's the name of your project ? ")

            # Generate project
            os.chdir(fileName)
            os.system("cmd /c npx create-react-app " + projectName)

    # NodeJS
    if project == "node":

        # Set repository destination
        fileName = filedialog.askdirectory(
            title="Target project", initialdir=homepath + "/Documents/Dev/Web/Back/NodeJS")

        if fileName.strip():
            # Set project name
            projectName = simpledialog.askstring(title="Name",
                                                 prompt="What's the name of your project ? ")

            # Generate project
            os.chdir(fileName)
            os.system("cmd /c npm init -y")


    # Laravel
    elif project == "laravel":

        # Set repository destination
        fileName = filedialog.askdirectory(
            title="Target project",  initialdir="C:/laragon/www")

        if fileName.strip():
            # Set project name
            projectName = simpledialog.askstring(title="Name",
                                                 prompt="What's the name of your project ? ")

            # Generate project
            os.chdir(fileName)
            os.system("cmd /c composer create-project laravel/laravel " +
                      projectName + " --prefer-dist")

    # Ionic
    elif project == "ionic":

        # Set repository destination
        fileName = filedialog.askdirectory(
            title="Target project",  initialdir=homepath + "/Documents/Dev/Mobile/Web/Ionic")

        if fileName.strip():
            # Set project name
            projectName = simpledialog.askstring(title="Name",
                                                 prompt="What's the name of your project ? ")

            # Generate project
            os.chdir(fileName)
            os.system("cmd /c ionic start " +
                      projectName + " blank --type=angular")



tk.Button(frame, text="Angular", padx=10,
          pady=5, fg="white", bg="#c3002f", font=("Courrier, 14"), command=lambda: generateProject("angular")).pack(fill=X, expand=YES)

tk.Button(frame, text="React", padx=10,
        pady=5, fg="white", bg="#61DAFB", font=("Courrier, 14"), command=lambda: generateProject("react")).pack(fill=X, expand=YES)

tk.Button(frame, text="NodeJS", padx=10,
        pady=5, fg="white", bg="#79B461", font=("Courrier, 14"), command=lambda: generateProject("node")).pack(fill=X, expand=YES)

tk.Button(frame, text="Laravel", padx=10,
          pady=5, fg="white", bg="#ff2d20", font=("Courrier, 14"), command=lambda: generateProject("laravel")).pack(fill=X, expand=YES)

tk.Button(frame, text="Ionic", padx=10,
          pady=5, fg="white", bg="#4e8df7", font=("Courrier, 14"), command=lambda: generateProject("ionic")).pack(fill=X, expand=YES)


root.mainloop()
