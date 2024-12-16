import os

cwd = os.getcwd()
input_file_name = "day4_input.txt"
input_file = cwd + "\\" + input_file_name

# open and read file
with open(input_file,'r') as file:
    input_lines = file.read().splitlines() 
file.close()

line_count =  len(input_lines)
all_four_letter_words_starting_with_X = []

# loop over each line to find word "XMAS"
for idx, line in enumerate(input_lines):
    curent_line_length = len(line)

    # get before and after 3 lines from the current line. this lines will be used to find the worjd "XMAS" with looping over current line
    # if it is out of index then default to a line filled with "*"
    before_line1 = "{:*<{}}".format("",curent_line_length) if idx - 1 < 0 else input_lines[idx - 1]
    before_line2 = "{:*<{}}".format("",curent_line_length) if idx - 2 < 0 else input_lines[idx - 2]
    before_line3 = "{:*<{}}".format("",curent_line_length) if idx - 3 < 0 else input_lines[idx - 3]
    after_line1 = "{:*<{}}".format("",curent_line_length) if idx + 1 >= line_count else input_lines[idx + 1]
    after_line2 = "{:*<{}}".format("",curent_line_length) if idx + 2 >= line_count else input_lines[idx + 2]
    after_line3 = "{:*<{}}".format("",curent_line_length) if idx + 3 >= line_count else input_lines[idx + 3]
    
    # get postions of letter "X" in the current line. only this positions will be used to find words "XMAS"
    current_line_X_positions = [idx  for idx, char in enumerate(line) if char == "X"]
    
    
    # loop over the positions of the "X" in current line
    for pos in current_line_X_positions:
        # From an "X" move in 8 different ditections and get all 4 letter words. If there is no four letter availbale in any direction pad it wiht "*" to 4.
        option1 = "{:*<4}".format(line[pos : pos + 4])
        option2 = "{:*<4}".format(line[(0 if pos - 3 < 0 else pos - 3) : pos + 1][::-1])
        option3 = line[pos] + before_line1[pos] + before_line2[pos] + before_line3[pos]
        option4 = line[pos] + after_line1[pos] + after_line2[pos] + after_line3[pos]
        option5 = line[pos] + ("*" if pos - 1 < 0  else before_line1[pos - 1]) + ("*" if pos - 2 < 0 else before_line2[pos - 2]) + ("*" if pos - 3 < 0 else before_line3[pos - 3])
        option6 = line[pos] + ("*" if pos + 1 >= curent_line_length else before_line1[pos + 1]) + ("*" if pos + 2 >= curent_line_length else before_line2[pos + 2]) + ("*" if pos + 3 >= curent_line_length else before_line3[pos + 3])
        option7 = line[pos] + ("*" if pos - 1 < 0  else after_line1[pos - 1]) + ("*" if pos - 2 < 0 else after_line2[pos - 2]) + ("*" if pos - 3 < 0 else after_line3[pos - 3])
        option8 = line[pos] + ("*" if  pos + 1 >= curent_line_length else after_line1[pos + 1]) + ("*" if pos + 2 >= curent_line_length else after_line2[pos + 2]) + ("*" if pos + 3 >= curent_line_length else after_line3[pos + 3])   
        
        # add all four letter words starting with "X" innto a list
        all_four_letter_words_starting_with_X.extend([option1, option2, option3, option4, option5, option6, option7, option8])

# get the count of "XMAS"
count_of_XMAS =  all_four_letter_words_starting_with_X.count("XMAS")
print(f"count_of_XMAS: {count_of_XMAS}")

# part - 2 
count_of_XMAS_pattern = 0
# loop over each line to find X-MAS pattern (two MAS in the shape of an X)
for idx, line in enumerate(input_lines):
    curent_line_length = len(line)

    # get before and after 1 line from the current line. these lines will be used to find the  X-MAS pattern.
    # if it is out of index then default to a line filled with "*"
    before_line = "{:*<{}}".format("",curent_line_length) if idx - 1 < 0 else input_lines[idx - 1]
    after_line = "{:*<{}}".format("",curent_line_length) if idx + 1 >= line_count else input_lines[idx + 1]
     
    # get postions of letter "X" in the current line. only this positions will be used to find words "XMAS"
    current_line_A_positions = [idx  for idx, char in enumerate(line) if char == "A"]
    
    # loop over the positions of the "A" in current line
    for pos in current_line_A_positions:
        # using "A" as strating point form the left and right leg of the X pattern
        left_leg = ("*" if pos + 1 >= curent_line_length else before_line[pos + 1]) + line[pos] + ("*" if pos - 1 < 0 else after_line[pos - 1])
        right_leg = ("*" if pos - 1 < 0 else before_line[pos - 1]) + line[pos] + ("*" if pos + 1 >= curent_line_length else after_line[pos + 1]) 
        
        # increment the counter if pattern is correct.
        if (left_leg == "MAS" or left_leg[::-1] == "MAS") and (right_leg == "MAS" or right_leg[::-1] == "MAS"):
            count_of_XMAS_pattern += 1

# count of "XMAS"
print(f"count_of_XMAS pattern: {count_of_XMAS_pattern}")