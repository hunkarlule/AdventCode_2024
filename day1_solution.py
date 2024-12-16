import os
import re
cwd = os.getcwd()
input_file_name = "day1_input.txt"
input_file = cwd + "\\" + input_file_name

# input_lines = [] 
with open(input_file,'r') as file:
    input_lines = file.read().splitlines() 

file.close()

first_list = [ int(re.split(r'\s+', line)[0]) for line in input_lines]
second_list = [ int(re.split(r'\s+', line)[1]) for line in input_lines]
first_list.sort()
second_list.sort()


difference_list = [abs(item2 - item1) for item1, item2 in zip(first_list, second_list)]
total_distance = sum(difference_list)
print(f'Total distance: {total_distance}')

# part two
second_list_occurances = {element: second_list.count(element) for element in set(second_list)}
similarity_score = sum([ n * second_list_occurances[n] for n in first_list if n in second_list_occurances])
print(f'Similarity score: {similarity_score}')