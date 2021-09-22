data = "Four score and seven years ago our fathers brought forth on this continent..."

new_list = data.split(maxsplit=3)

new_list = new_list[:-1] + new_list[-1].rsplit(maxsplit=3)

print(new_list)