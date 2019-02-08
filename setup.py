# setup.py
"""
Responsible for configuring the venv in which the Python scripts are to run,
then calling main.py. Modify main.py, NOT this file.
"""

import os
import subprocess
import platform
from time import sleep
import traceback
import datetime

#subprocess.call(["say", "setup dot py called"])

reinstall_modules = True

thisDir = os.getcwd()
venvPath = thisDir + "/venv"
mainPath = thisDir + "/main.py"
fullVenvPath = thisDir + "/venv/bin/python3"
print("thisDir is", thisDir)
print("venvPath is", venvPath)

if os.path.exists(venvPath):
    print("venv already made!")
    if reinstall_modules:
        print("reinstalling modules")
        subprocess.call(["python3", "-m", "pip", "install", "-r", "requirements.txt"])
    else:
        print("not reinstalling modules")
else:
    print("making venv")
    subprocess.call(["python3", "-m", "venv", "venv"])
    subprocess.call(["python3", "-m", "pip", "install", "fuzzywuzzy"])

print("Running main.py")
subprocess.call([fullVenvPath, mainPath])