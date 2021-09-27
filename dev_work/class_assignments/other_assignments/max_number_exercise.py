def myMax(list1):
  
    # Assume first number in list is largest
    # initially and assign it to variable "max"
    max = list1[0]
   
    # Now traverse through the list and compare 
    # each number with "max" value. Whichever is 
    # largest assign that value to "max'.
    for x in list1:
        if x > max :
             max = x
      
    # after complete traversing the list 
    # return the "max" value
    return max
  
  
# Driver code
list1 = [100, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))




def maximum_number(my_list):
  max_num = 0

  for num in range(0, len(my_list)):
    if(my_list[num] > max_num):
      max_num = my_list[num]
      print(max_num)
  
  return max_num

print(maximum_number([4, 1, 20, 50, 2, 15, 35]))
