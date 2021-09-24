import csv

states = [
    { 'State': 'Oregon', 'Capital': 'Salem', 'Year Founded': 1855 },
  { 'State': 'Utah', 'Capital': 'Salt Lake City', 'Year Founded': 1858 },
  { 'State': 'Oklahoma', 'Capital': 'Oklahoma City', 'Year Founded': 1910 },
  { 'State': 'Nebraska', 'Capital': 'Lincoln', 'Year Founded': 1867 },
  { 'State': 'Florida', 'Capital': 'Tallahassee', 'Year Founded': 1824 },
]

states_list = []

for value in dict.value():
      states_list.appened(value)

    

with open('exercise_csv_loop.txt', 'w') as file:
  nf = csv.writer(file)

  nf.writerow(states_list)
  nf.writerows(states)