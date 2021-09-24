import csv

data = [
    { 'State': 'Oregon', 'Capital': 'Salem', 'Year Founded': 1855 },
  { 'State': 'Utah', 'Capital': 'Salt Lake City', 'Year Founded': 1858 },
  { 'State': 'Oklahoma', 'Capital': 'Oklahoma City', 'Year Founded': 1910 },
  { 'State': 'Nebraska', 'Capital': 'Lincoln', 'Year Founded': 1867 },
  { 'State': 'Florida', 'Capital': 'Tallahassee', 'Year Founded': 1824 },
]

fields = []
for key in data[0].keys():
    fields.append(key)

data_lists =[]

for dict in data:
    data_line = []
    for value in dict.values():
        data_line.append(value)
    data_lists.append(data_line)

with open('state_foundings.txt','wt',newline='',encoding='utf-8') as state_file:
    wrt = csv.writer(state_file)
    wrt.writerow(fields)
    wrt.writerows(data_lists)

with open('state_foundings.txt','rt',newline='',encoding='utf-8') as state_file:
    for line in state_file:
        print(state_file.read())