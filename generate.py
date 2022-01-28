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

            # Create project folder
            os.mkdir(projectTarget + "/" + projectName)

            # Navigate to folder
            os.chdir(projectTarget + "/" + projectName)

            # Generate project
            os.system("cmd /c npm init -y")

            # Create server.js file with default code
            code = "const express = require('express');\nconst app = express();\nconst port = process.env.PORT || 3333;\nconst axios = require('axios');\n\napp.use(express.static(__dirname + '/public'));\napp.use(express.json());\n\n\napp.get('/', (req, res) => {\n    res.send('Hello World!');\n});\n\n\napp.listen(port, () => {\n    console.log(`App listening on port ${ port } !`);\n});"
            with open("server.js", "w") as file:
                file.write(code)

            # Install express, nodemon, nodemon
            os.system("cmd /c npm install express nodemon axios")



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



    # Open project in explorer
    os.system("cmd /c start " + projectTarget + "/" + projectName)
