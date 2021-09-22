dictionary = {}

with open('raw_dictionary.txt') as my_file:
  my_fv = my_file.readlines()
for line in my_fv:
    key, value = line.split()
    dictionary[key] = value

print(dictionary)