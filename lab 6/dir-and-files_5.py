path = r"C:\Users\Acer\Desktop\универ\2-семестр\пп2\lab\lab 6\file_2.txt"
file = open(path, "w")
list = ["AAAA", "UUUU", "SUUUI"]
for i in list:
    file.write(i+"\n")
file.close()