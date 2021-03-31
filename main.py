import os

print('Créer un projet : \n')

# Choose technology
print("1- Angular")
print("2- Laravel")
print("3- React Native")
print("4- Ionic")
technology = input('Quelle technologie voulez-vous utiliser ? ')

# Project name
projectName = input('Quel est le nom de votre programme ? ')

# Angular
if technology == '1':
    # Set repository destination
    # os.system('cmd /k cd C:\\Users\\alexa\\Documents\\Dev\\Web\\Front\\Angular\\')

    # Generate project
    os.system('cmd /k ng new ' + projectName +
              ' --style=scss --routing --strict')

    # Open in VS Code
    os.system('cmd /k cd ' + projectName)
    os.system('cmd /k code .')

    # Start server
    os.system('cmd /k ng serve')
