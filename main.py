import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text, simpledialog
import os
import getpass

# Set window
root = tk.Tk()
root.title("Program Generator")
root.geometry("300x450")
root.minsize(300, 450)

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
            title="Emplacement du projet", initialdir=homepath + "/Documents/Dev/Web/Front/Angular")

        # Set project name
        projectName = simpledialog.askstring(title="Nom",
                                             prompt="Quel est le nom de votre programme ? ")

        # Generate project
        os.chdir(fileName)
        os.system("cmd /c ng new " + projectName +
                  " --style=scss --routing --strict")

        # Open in VS Code
        os.chdir(fileName + "/" + projectName)
        os.system("cmd /c code .")

    # Laravel
    elif project == "laravel":

        # Set repository destination
        fileName = filedialog.askdirectory(
            title="Emplacement du projet",  initialdir="C:/laragon/www")

        # Set project name
        projectName = simpledialog.askstring(title="Nom",
                                             prompt="Quel est le nom de votre programme ? ")

        # Generate project
        os.chdir(fileName)
        os.system("cmd /c composer create-project laravel/laravel " +
                  projectName + " --prefer-dist")

        # Open in VS Code
        os.chdir(fileName + "/" + projectName)
        os.system("cmd /c code .")

    # React Native
    elif project == "react_native":

        # Set repository destination
        fileName = filedialog.askdirectory(
            title="Emplacement du projet",  initialdir=homepath + "/Documents/Dev/Mobile/Web/React Native")

        # Set project name
        projectName = simpledialog.askstring(title="Nom",
                                             prompt="Quel est le nom de votre programme ? ")

        # Generate project
        os.chdir(fileName)
        # os.system("cmd /c composer create-project laravel/laravel " +
        #           projectName + " --prefer-dist")

        # Open in VS Code
        os.chdir(fileName + "/" + projectName)
        os.system("cmd /c code .")

    # Ionic
    elif project == "ionic":

        # Set repository destination
        fileName = filedialog.askdirectory(
            title="Emplacement du projet",  initialdir=homepath + "/Documents/Dev/Mobile/Web/Ionic")

        # Set project name
        projectName = simpledialog.askstring(title="Nom",
                                             prompt="Quel est le nom de votre programme ? ")

        # Generate project
        os.chdir(fileName)
        os.system("cmd /c ionic start " +
                  projectName + " blank --type=angular")

        # Open in VS Code
        os.chdir(fileName + "/" + projectName)
        os.system("cmd /c code .")


tk.Button(frame, text="Angular", padx=10,
          pady=5, fg="white", bg="#c3002f", font=("Courrier, 14"), command=lambda: generateProject("angular")).pack(fill=X, expand=YES)

tk.Button(frame, text="Laravel", padx=10,
          pady=5, fg="white", bg="#ff2d20", font=("Courrier, 14"), command=lambda: generateProject("laravel")).pack(fill=X, expand=YES)

tk.Button(frame, text="React Native", padx=10,
          pady=5, fg="white", bg="#61dafb", font=("Courrier, 14"), command=lambda: generateProject("react_native")).pack(fill=X, expand=YES)

tk.Button(frame, text="Ionic", padx=10,
          pady=5, fg="white", bg="#4e8df7", font=("Courrier, 14"), command=lambda: generateProject("ionic")).pack(fill=X, expand=YES)


root.mainloop()
