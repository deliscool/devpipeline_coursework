from pprint import pprint

dictionary = {}

with open("raw_dictionary.txt") as my_file:
    for line in my_file:
      # print(line)
      (key, var)= line.split()
      # print(key)
      # print(var)
      dictionary[str(key)] = str(var)

print(pprint(dictionary, sort_dicts=True))
print(dictionary)