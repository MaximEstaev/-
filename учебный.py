import os

GB = 1024 * 1024 * 1024

def createFile(name, size):

    file_size = os.stat(name).st_size
    print("File created of ", file_size / size, " GB size")

createFile("test.txt", GB)












