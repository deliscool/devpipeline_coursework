dec_num = int(input('Enter in an integer: '))
my_string = ""

def dec_to_bin(dec_num):
  global my_string
  if dec_num >= 1:
      dec_to_bin(dec_num // 2)
  my_string += str(dec_num % 2 )


dec_to_bin (dec_num)

print(my_string)