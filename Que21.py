'''
Write python program to perform file handling and perform following
operations:
open,read,write,tell,seek,rename,delete
'''
import os

# File path
file_path = "Que21.txt"

while True:
    operation = input(
        "\nEnter operation (\n 1.open\n 2.read\n 3.write\n 4.tell\n 5.seek\n 6.rename\n 7.delete\n) or 'exit' to quit: ")

    if operation == "1":
        try:
            file = open(file_path, "a+")
            print("File opened.")
        except IOError as e:
            print("Error: Failed to open the file. Reason:", str(e))

    elif operation == "2":
        try:
            file = open(file_path, "r")
            content = file.read()
            print("File Content:")
            print(content)
            file.close()
        except IOError as e:
            print("Error: Failed to read the file. Reason:", str(e))

    elif operation == "3":
        try:
            file = open(file_path, "w")
            content = input("Enter content to write to the file: ")
            file.write(content)
            file.close()
            print("Content written to the file.")
        except IOError as e:
            print("Error: Failed to write to the file. Reason:", str(e))

    elif operation == "4":
        try:
            file = open(file_path, "r")
            position = file.tell()
            print("Current File Position:", position)
            fileptr = file.read()
            print("File Content : ",fileptr)
            position = file.tell()
            print("Current File Pointer Position after Read Operation:", position)
            file.close()
        except IOError as e:
            print("Error: Failed to get the file position. Reason:", str(e))

    elif operation == "5":
        try:
            file = open(file_path, "r")
            position = int(input("Enter position to seek: "))
            file.seek(position)
            content = file.read()
            print("Content after seeking to position", position, ":")
            print(content)
            file.close()
        except (IOError, ValueError) as e:
            print("Error: Failed to seek the file. Reason:", str(e))

    elif operation == "6":
        try:
            new_file_path = input("Enter new file path: ")
            os.rename(file_path, new_file_path)
            file_path = new_file_path
            print("File renamed to:", file_path)
        except (FileNotFoundError, OSError) as e:
            print("Error: Failed to rename the file. Reason:", str(e))

    elif operation == "7":
        try:
            os.remove(file_path)
            print("File deleted:", file_path)
            break
        except (FileNotFoundError, OSError) as e:
            print("Error: Failed to delete the file. Reason:", str(e))
            break

    elif operation == "exit":
        break

    else:
        print("Invalid operation. Please try again.")
