with open('coundata.csv', 'rt') as infile:
    header_row = infile.readline()

    while True:
        line = infile.readline()
        if not line:
            break

        my_list = line.split(',')
        county = my_list(0)
        pop_2010 = my_list[1]
        pop_2019 = my_list[-1]