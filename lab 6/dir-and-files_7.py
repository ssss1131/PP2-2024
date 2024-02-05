
with open("file_1.txt","r") as fi:
    with open("file_3.txt","w") as fil:
        for row in fi:
            fil.write(row)