import sys
import subprocess
import datetime
import traceback

try:
    subprocess.call(["say", "python script called"])
    """
    with open("/Users/jaspergilley/Desktop/aloha.txt", 'w') as f:
        f.write(str(datetime.datetime.now()))
    """
    safelih()

    sys.stdout.flush()
except:
    print(traceback.format_exc())