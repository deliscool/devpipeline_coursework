#Create a file and write a list of five fruits to it. Then read the list from the file and print it to the screen. 
#Next, append a new fruit to the list and read it again.
my_file = open("fruit.txt", "w")
my_file.write("Apple\n" "Banana\n" "Orange\n" "Apricot\n" "Grape\n")
my_file.close()

my_file= open("fruit.txt", "r")
print(my_file.read())
my_file.close()

