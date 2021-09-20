with open('raw_data.txt','r') as save_file:
    all_lines = save_file.read()
    lines = all_lines.split('|')
    join_lines = ','.join(l)

print(lines)

with open('new_data.txt', 'wt') as new_file:
    content = new_file.writelines(lines)
print(content)

#with open("raw_data.txt") as my_file:
#     txt = my_file.read()

#     lines = txt.split("|")
#     joined_lines = ",".join(lines)


#with open("join_text.txt", "a") as newfile:
#   for line in joined_lines:
#       newfile.write(line)