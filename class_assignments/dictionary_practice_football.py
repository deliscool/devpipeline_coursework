college_football = {
  "Utes" : "Swoop",
  "Ohio State" : "Buckeyes",
  "Michigan" : "Wolverines",
  "Oregan State" : "Ducks",
  "Boise State" : "Broncos"
}

for key, value in college_football.items():
    print(key, ' : ', value)

while True:
  user_input = input("\nFor options press: \n'Q' to quit \n'R' to remove team \n'A' to add a new team \n What would you like to do?")
  user_input = str(user_input)
  if user_input.lower() == 'r':
    user_removal= str(input ("Which state would you like to remove?"))
    user_removal= college_football.pop(user_removal, None)
    print(college_football)
    continue
  if user_input.lower() == 'a':
    state= input("What state would you like to add?")
    team_name= input("What is the team name?")
    college_football[state] = team_name
    print(college_football)
    continue
  if user_input.lower() == 'q':
    print("Exiting the program")
    break

