#create a function that loops over and randomly selects

import random

lotto_dic = {
  'Green' : 3,
  'Red' : 7,
  'Pink' : 2
}

#intialized and declared an empty 
list_lotto = []

#nested loop 
for key,value in lotto_dic.items():
  for num_times in range(0,value):
    list_lotto.append(key)

print(list_lotto)
print(random.choice(list_lotto))
