import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, Text, simpledialog
import os
import time

# Set home path
homepath = os.path.expanduser(os.getenv('USERPROFILE'))


def generate(project):

    # Angular
    if project == "angular":

        # Set repository destination
        projectTarget = filedialog.askdirectory(
            title="Target project", initialdir=homepath + "/Documents/Dev/Web/Front/Angular")

        if projectTarget.strip():
            # Set project name
            projectName = simpledialog.askstring(title="Name",
                                                 prompt="What's the name of your project ? ")

            # Generate project
            os.chdir(projectTarget)
            os.system("cmd /c ng new " + projectName +
                      " --style=scss --routing --strict")

    # React
    if project == "react":

        # Set repository destination
        projectTarget = filedialog.askdirectory(
            title="Target project", initialdir=homepath + "/Documents/Dev/Web/Front/React")

        if projectTarget.strip():
            # Set project name
            projectName = simpledialog.askstring(title="Name",
                                                 prompt="What's the name of your project ? ")

            # Generate project
            os.chdir(projectTarget)
            os.system("cmd /c npx create-react-app " + projectName)

    # NodeJS
    if project == "node":

        # Set repository destination
        projectTarget = filedialog.askdirectory(
            title="Target project", initialdir=homepath + "/Documents/Dev/Web/Back/NodeJS")

        if projectTarget.strip():
            # Set project name
            projectName = simpledialog.askstring(title="Name",
                                                 prompt="What's the name of your project ? ")

            # Generate project
            os.chdir(projectTarget)
            os.system("cmd /c npm init")

            # Install express and nodemon
            os.system("cmd /c npm install express nodemon")


    # Laravel
    elif project == "laravel":

        # Set repository destination
        projectTarget = filedialog.askdirectory(
            title="Target project",  initialdir="C:/laragon/www")

        if projectTarget.strip():
            # Set project name
            projectName = simpledialog.askstring(title="Name",
                                                 prompt="What's the name of your project ? ")

            # Generate project
            os.chdir(projectTarget)
            os.system("cmd /c composer create-project laravel/laravel " +
                      projectName + " --prefer-dist")

    # Ionic
    elif project == "ionic":

        # Set repository destination
        projectTarget = filedialog.askdirectory(
            title="Target project",  initialdir=homepath + "/Documents/Dev/Mobile/Web/Ionic")

        if projectTarget.strip():
            # Set project name
            projectName = simpledialog.askstring(title="Name",
                                                 prompt="What's the name of your project ? ")

            # Generate project
            os.chdir(projectTarget)
            os.system("cmd /c ionic start " +
                      projectName + " blank --type=angular")
