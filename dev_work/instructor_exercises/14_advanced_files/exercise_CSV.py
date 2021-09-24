import csv

header_fields = ['State', 'Capital', 'Year Founded']

data = [
    ['Oregon','Salem',1855],
  ['Utah','Salt Lake City',1858],
  ['Oklahoma', 'Oklahoma City', 1910],
  ['Nebraska', 'Lincoln', 1867],
  ['Florida',	'Tallahassee', 1824]
  ]

with open('exercisecsv.csv', 'w') as file:
    new_file = csv.writer(file)

    new_file.writerow(header_fields)

    new_file.writerows(data)

writer = csv.writer(f)

#documentation for the csv module recommends 
#opening the file with the newline=‘’ parameter on all platforms 
# (Windows, Linux, Mac) to disable universal newlines 
# translation: with open('output.csv', 'w', newline='',
#  encoding='utf-8') as f:
#writer = csv.writer(f)
