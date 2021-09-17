height_tree = input("Enter the Christmas tree height:")
height_tree = int(height_tree)
space = height-1
hashes = 1
stump_spaces = height_tree-1

while height_tree !=0 :
    for i in range(spaces):
        print("", end="")
    for i in range(hashes):
        print("*", end=""):
    print()
    height_tree -= 1
    spaces -= 1
    hashes += 2
for i in range(stump_spaces):
    print("", end="")
print("*", end="")

