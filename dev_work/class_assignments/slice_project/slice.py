def slice(iter_obj, start=0, stop=None, step=1):
    
    start_stop_list = []
    finished_list = []
​
    #handle negative inputs for start and stop
    if stop == None:
        stop = len(iter_obj)
    if start < 0:
        start = start + len(iter_obj)
    if stop < 0:
        stop = stop + len(iter_obj)
​
    
    
    #append the correct elements to a new list
    for i in range(len(iter_obj)):
        if i >= start and i < stop or stop == None:
            start_stop_list.append(iter_obj[i])
    
    #handle neg/pos step
    if step < 0:
        step = abs(step)
        start_stop_list.reverse()
​
    #append step values to new list
    for i in range(len(start_stop_list)):
        if i % step == 0:
            finished_list.append(start_stop_list[i])
​
​
    #cast string if string recieved
    if type(iter_obj) == str:
        finished_list = "".join(finished_list)
​
    return finished_list
test = "hello"
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
​
# print(slice(test,1, 5, 2))
​
# print(test[1:5:2])
​
print(slice(nums, 2, -2))
​
print( slice(nums, stop = 4) )
​
print( slice(nums, step=-1) )
