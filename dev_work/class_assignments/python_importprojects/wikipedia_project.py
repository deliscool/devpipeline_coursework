import wikipedia
from wikipedia.wikipedia import search


search = input("Enter a search topic:")
result = wikipedia.summary({search}, sentences = 2) 
  

print(result)