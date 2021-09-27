import os

# Create list and file
sl = []
shopping_file = "shopping_list.txt"

def clear_console():
    # Clear the console
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_help(list):
    clear_console()
    # Print out instructions on how to use the app
    print('')
    print('='*30)
    print('Shopping List')
    print('='*30)
    print('')
    print("""
You have {} items in your list. \n
Enter O to show options.
Enter P to see your list.
Enter S to save your list
Enter R to remove an item.
Enter C to clear your list.
Enter QUIT to exit without saving.""".format(len(list)))

def show_list(list):
    clear_console()
    if len(list) == 0:
        print("You have 0 items in your list.")
    else:
        print("Here's your list:\n")
        for item in list:
            print(item)

def add_to_list(new_item, list):
    clear_console()
    list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(list)))

def remove_from_list(list):
    clear_console()
    print("What item would you like to remove?\n")
    word = input("Remove an item: ")
    if word in list:
        list.remove(word)
        clear_console()
        print("{} has been removed from your list.".format(word))
    else:
        clear_console()
        print("{} is not in your list.".format(word))

def open_list(filename, list):
    try:
        with open(filename) as file:
            data = file.read().splitlines()
            list.extend(data)
    except FileNotFoundError:
        pass

def save_list(filename, list):
    with open(filename, "w") as file:
        for item in list:
            file.write(item + "\n")
    print("\nYour list has been saved to {}. \n\nHappy shopping!\n".format(filename))

def delete_list(filename, list):
    clear_console()
    list.clear()
    try:
        os.remove(filename)
        print("List deleted successfully.")
    except FileNotFoundError:
        print("List deleted successfully.")

open_list(shopping_file, sl)

show_help(sl

while True:
    new_item = input("\nAdd an item: ")
    if new_item == "q":
        show_list(shopping_list)
        print("\nHave a nice day!\n")
        break
    elif new_item == "o":
        show_help(shopping_list)
        continue
    elif new_item == "p":
        show_list(shopping_list)
        continue
    elif new_item == "s":
        show_list(shopping_list)
        save_list(saved_file, shopping_list)
        break
    elif new_item == "c":
        delete_list(saved_file, shopping_list)
        continue
    elif new_item == "REMOVE":
        remove_from_list(shopping_list)
        continue
    else:
        add_to_list(new_item, shopping_list)