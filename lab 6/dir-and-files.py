import os

#1
path = "C:\\Users\\Acer\\Desktop\\универ\\2-семестр\\пп2\\lab\\lab 6"

# printing all
print("there are all\n")
for i in os.listdir(path):
    print(i)

print("-" * 50, "\nthis is all dir\n")
# printing only directories
for i in os.listdir(path):
    if os.path.isdir(i):
        print(i)
print("-" * 50, "\nthis is all files\n")
for i in os.listdir(path):
    if not os.path.isdir(i):
        print(i)


