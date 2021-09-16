import wikipedia
from wikipedia.wikipedia import search

# finding result for the search
# sentences = 2 refers to numbers of line
search = input("Enter a search topic:")
result = wikipedia.summary({search}, sentences = 2) 
  
# printing the result
print(result)