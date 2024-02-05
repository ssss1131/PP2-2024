import os, re


path = r"C:\Users\Acer\Desktop\универ\2-семестр\пп2\lab\lab 6\file_1.txt"

if os.path.exists(path):
    print("exists")
    if os.access(path,os.W_OK):
        print("can write")
    else:
        print("cant write")
    if os.access(path,os.R_OK):
        print("can read")
    else:
        print("cant write")
    if os.access(path,os.X_OK):
        print("executability")
    else:
        print("not executability")
