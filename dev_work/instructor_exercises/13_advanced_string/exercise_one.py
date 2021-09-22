#Write some code to read a text file containing long text 
# and break the text into sentences by calling the .split() function 
# to split the text on a period combined with a space '. ' 
# Then, write the lines one at a time to a different text file.

with open('exercise_one.txt','r') as fh:
    all_lines = fh.read()
    lines = fh.split('. ')

with open('new_exercise', 'wt') as new_file:
    for line in lines:
        temp_string = line
        if not temp_string.endswith('.'):
            temp_string = temp_string + '.\n'
            new_file.write(temp_string)
