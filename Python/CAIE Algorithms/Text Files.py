def append():
    MyFile = open("Append_File.txt", "a")
    MyFile.write(input("write: ") + "\n")
    MyFile.close()

def write():
    MyFile = open("Write_File.txt", "w")
    MyFile.write(input("write: ") + "\n")
    MyFile.close()

def read():
    try:
        MyFile = open("Read_File.txt", "r")
        line = MyFile.readline().strip()
        while line != "":
            print(line)
            line = MyFile.readline().strip()
        MyFile.close()
    except IOError:
        print("File does not exist doofus")

# main
mode = input("Input the mode bro: ")

if mode == "a":
    append()
elif mode == "w":
    write()
elif mode == "r":
    read()
else:
    print("doofus! input correct value")

# FOR PATH
# MyFile = l
# print(MyFile.read())