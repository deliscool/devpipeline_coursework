#del_command = open("python_importprojects/del_read.txt", "r")
#print(del_command.read())
#del_command.close("python_importprojects/del_read.txt")

# Using readline()

with open("del_read.txt", "r") as my_file:
    for line in my_file:
        print(my_file.readline())

with open("del_read.txt", "r") as my_file:
    for line in my_file:
        print(my_file.readlines())

count = 0 

with open("read_read.txt", "r") as my_file:
    for line in my_file:
        count += 1
        print(f'Line {count}: {line.strip()}')