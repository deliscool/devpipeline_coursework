my_list = ["Appple"], "Banana", 15, "Orange", 17.6, "Orange"]

def list_join(itj_obj, separtor)
    my_string = ""
    count = 0
    for i in it_obj:
        if count == len(it_obj)-1:
            my_string +=str(i)
            else:
                my_string += str(i) + separator
    print(my_string)

list_join(my_list, ",")


#another example()
for index, value in enumerate(itj_obj):