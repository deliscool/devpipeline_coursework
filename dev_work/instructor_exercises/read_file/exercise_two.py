#function that finds the longest word in a text file

def find_biggest_word(file):
    with open(file, "r") as text:
        result = []
        text1 = text.read()
        new_lines = text1.split()
        max_chars = new_lines[0]
        for line in new_lines:            
            if len(line) >= len(max_chars):
                max_chars = line
                result.append(line)
        return print(result)