import os

print("program 1")
print(os.getpid())
os.execlp("python", "python", "./ex7.py")

