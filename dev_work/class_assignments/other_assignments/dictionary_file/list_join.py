#def list_join(iterator, separator):
    #declare a variable that will map out and string the iterator
    #it = map(str, iterator)
    #declare another variable that converts the separator into a string
    #separator = str(separator)
    #declare a variable that
    #string = next(it, '')
    #for s in it:
    #    string += separator + s
    #return string
  
  
  # Don't forget to return the completed string
  
#print(list_join(["Apple","Banana",15,17.6,"Orange"], ','))

#output 
# Apple,Banana,15,17.6,Orange


# next homework build it without a map section


def list_join(it_obj, separator):
    list = []
    it = str(it_obj)
    sep = str(separator)
  # Your code goes here
  
  # Don't forget to return the completed string
  
print(list_join(["Apple","Banana",15,17.6,"Orange"], ','))
