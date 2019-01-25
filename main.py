import sys
import subprocess
import datetime

subprocess.call(["say", "python script called"])
"""
with open("/Users/jaspergilley/Desktop/aloha.txt", 'w') as f:
    f.write(str(datetime.datetime.now()))
"""

sys.stdout.flush()