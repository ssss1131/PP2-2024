path = r"C:\Users\Acer\Desktop\универ\2-семестр\пп2\lab\lab 6\file_1.txt"
file = open(path, "r")
all=0
for x in file:all += 1
print(all)
file.close()
