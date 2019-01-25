import os
import subprocess
import platform

subprocess.call(["say", "setup dot py called"])

thisDir = os.getcwd()
venvPath = thisDir + "/venv"
print("thisDir is", thisDir)
print("venvPath is", venvPath)

if os.path.exists(venvPath):
    print("venv already made!")
else:
    subprocess.call(["python3", "-m", "venv", "venv"])