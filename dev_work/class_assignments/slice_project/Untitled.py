#Feature 1
# Start by making an empty list. 
# Use a loop to add twelve random integers between 50 and 80, inclusive, to the list. 
# Sort the list in descending order from highest to lowest. 
# Use a loop to print the sorted list elements on one line separated by single spaces. 
# Determine if 66 is in the list and generate some appropriate output.

#Feature 2
#  Print the largest element in the list and the smallest element in the list. 
#  Slice out the five elements with indexes 4 through 8 and assign to a variable. 
#  Print the  slice. Print the total of all five elements in this slice. 
#  Use a while loop to display all elements in the slice on one line separated by tabs. 

import random

mt_list = []
num_66 = False

for i in range(12):
    mt_list.append(random.randint(50,80))
    
mt_list.sort(reverse=True)

for i in mt_list:
    print(i, end=" ")
    if i == 66:
        num_66 = True
print()
if num_66:
    print("66 is in the list.")
else:
    print('66 is not in the list.')

print(f'This is the higest number : {mt_list[0]}')
print(f'This is the lowest number : {mt_list[-1]}')

slice_indexes = mt_list[4:9]


total = sum(slice_indexes)
#print(total)

slice_indexes.append(total)
#print(slice_indexes)

counter = 0
while counter < 6:
    print(slice_indexes[counter], end="  ")
    counter +=1
