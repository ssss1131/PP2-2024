import os
path=r"C:\Users\Acer\Desktop\универ\2-семестр\пп2\lab\lab 6\file_4.txt"

if os.path.exists(path):
    os.remove(path)
    print("removed")
else:
    print("Does not exist")
