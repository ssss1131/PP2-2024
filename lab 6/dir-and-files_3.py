import os
path=r"C:\Users\Acer\Desktop\универ\2-семестр\пп2\lab\lab 6\file_1.txt"
list=path.split("\\")

if os.path.exists(path):
    print(f"file name : {list[-1]}")
    print(f"folder : {list[-2]}")
else:
    print("path does not exist")

