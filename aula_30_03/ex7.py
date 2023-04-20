import os

print("program 2")
print(os.getpid())
os.execlp("python", "python", "./ex6.py")