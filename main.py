import sys

print("hello world!")
with open("/Users/jaspergilley/Desktop/test.txt", 'w') as f:
    f.write("it works!!!")

sys.stdout.flush()