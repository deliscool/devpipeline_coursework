
def answer_to_exercise():
    Counter = 0
  
    with open("testing_one.txt","r") as content:
        for i in content:
                if i:
                    Counter += 1
          
        return Counter

print(answer_to_exercise())

