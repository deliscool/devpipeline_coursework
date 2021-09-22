with open('countydata.csv', 'rt') as infile:
  header_row = infile.readline()
  title = header_row.split(',')
  heading = title[0]
  h1 = title[1]
  h2 = title[-1].replace('\n', '')
  h3 = "Growth"
  h4 = "Rate %"
  print(f"{heading:>16} {h1:>7} {h2:>8} {h3:>9} {h4:>8}")
  print("----------------- -------- -------- -------- ---------")
  while True:
    line = infile.readline()
    if not line:
      break
    # else:
    #   print(line)

    my_list = line.split(',')
    county = my_list[0]
    pop_2010 = int(my_list[1])
    pop_2019 = int(my_list[-1].replace('\n', ''))
    difference = pop_2019 - pop_2010
    percentage = (difference / pop_2010) * 100
    print(f"{county:<19} {pop_2010:<8} {pop_2019:<8} {difference:<7} {percentage:.2f} %")