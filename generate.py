import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, Text, simpledialog
import os
import time

# Get user directory
homePath = os.path.expanduser(os.getenv('USERPROFILE'))

webPath = homePath + '/Documents/Dev/Web/'
mobilePath = homePath + '/Documents/Dev/Mobile/'


def generate(project):

    # Angular
    if project == "angular":

        # Set repository destination
        projectTarget = filedialog.askdirectory(
            title="Target project", initialdir=webPath)

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
            title="Target project", initialdir=webPath)

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
            title="Target project", initialdir=webPath)

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


    # NX
    if project == "nx":

        # Set repository destination
        projectTarget = filedialog.askdirectory(
            title="Target project", initialdir=webPath)

        if projectTarget.strip():
            # Set project name
            projectName = simpledialog.askstring(title="Name",
                                                 prompt="What's the name of your project ? ")

            # Generate project
            os.chdir(projectTarget)
            os.system("cmd /c npx create-nx-workspace --preset=angular-nest --appName=front --style=scss --nx-cloud=N " + projectName)



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
            title="Target project",  initialdir=mobilePath)

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
