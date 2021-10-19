
#menu selection 
def menu():
  print("")
  print("  Press <enter> to continue")
  print("-"*30)
  print("")
  print("  *** Binary Calculator ***")
  print("")
  print("(B)inary to Decimal Conversion")
  print("(D)ecimal to Binary Conversion")
  print("(A)dd two Binary Numbers")
  print("(S)ubtract two Binary Numbers")
  print("(M)ultiply two Binary Numbers")
  print(" D(i)vide two Binary Numbers")
  print("(Q)uit")
  print("\n")


# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

#This function converts bin to decimal
def bin_to_dec(x):
  x = int(x, 2)
  print(x)

#This function converts decial to bin
def dec_to_bin(x):
    if x >= 1:
        dec_to_bin(x // 2)
    print(x % 2, end="")

#This checks if the value is right
def binary_check(x, y):
  bin_input = ''

  if x.isnumeric():
    for x_check in x:
      if int(x) <= -1 or int(x) >= 2:
        bin_input = ''
        print("Invalid Binary, please use the digits 1 and 0")
        binary_check()
      else:
        bin_input = bin_input + str(x)
  else:
    print("Not valid Binary, please try again utilizing digits of 1 and 0")
    binary_check()

  return bin_input

def main():
  menu()
  while True:
    choice=str(input('Enter choice from menu:'))
    user_c = choice.lower()
    if user_c == 'b':
      x = int(input("Enter Binary Number (8-digits):"))
      x= bin_to_dec(x)
      print(f'The decimal value is:{x}')
      menu()
    elif choice == 'd':
      x = int(input("Enter a Decimal Number (0-255):"))
      x= dec_to_bin(x)
      print(f'The binary value is:{x}')
    elif user_c == 'a':
      x = input("Enter first Binary Number (8-digits):")
      y = input("Enter second Binary Number (8-digits):")
      binary_check (x)
      binary_check (y)
      answer = ( x +y )
      answer= bin_to_dec(answer)
      print(answer)
      menu()
    elif user_c == 's':
      pass
      #call function 
    elif user_c == 'm':
      pass
      #call function 
    elif user_c == 'i':
      pass
      #call function 
    elif user_c == 'q':
      print('Good Bye!')
      quit()
    else:
      menu()
main()