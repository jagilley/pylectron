import os
import subprocess
import platform
from time import sleep

#subprocess.call(["say", "setup dot py called"])

thisDir = os.getcwd()
venvPath = thisDir + "/venv"
mainPath = thisDir + "/main.py"
print("thisDir is", thisDir)
print("venvPath is", venvPath)

if os.path.exists(venvPath):
    print("venv already made!")
else:
    print("making venv")
    subprocess.call(["python3", "-m", "venv", "venv"])

print("Running main.py")
subprocess.call(["/Users/jaspergilley/Code/pylectron/venv/bin/python3", mainPath])