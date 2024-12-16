import os
import re
cwd = os.getcwd()
input_file_name = "day3_input.txt"
input_file = cwd + "\\" + input_file_name


with open(input_file,'r') as file:
    file_content = file.read()
file_length = len(file_content)


command_start_positions = [match.start() for match in re.finditer(re.escape("mul("), file_content)]
possible_command_lengths = [12, 11, 10, 9 ,8]
possible_commands = []


pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
possible_commands.extend([(idx, re.search(pattern, file_content[idx : idx + 12]).group(0)) for  idx in command_start_positions if bool(re.search(pattern, file_content[idx : idx + 12]))])
command_index_and_multipliers =  [ (command[0],int(command[1].split(",")[0][4:]), int(command[1].split(",")[1][:-1])) for command in possible_commands]


multiplications_result = sum([command[1] * command[2] for command in command_index_and_multipliers])
print(f'Results of the multiplications: {multiplications_result}')

# part two
start_positions_for_do = sorted([match.start() for match in re.finditer(re.escape("do()"), file_content)])
start_positions_for_dont = sorted([match.start() for match in re.finditer(re.escape("don't()"), file_content)])

adjusted_command_index_and_multipliers = [ command for command in command_index_and_multipliers if  max([dont_idx for dont_idx in start_positions_for_dont if dont_idx < command[0]], default=-1) < max([do_idx for do_idx in start_positions_for_do if do_idx < command[0]], default=0)]
adjusted_multiplications_result = sum([command[1] * command[2] for command in adjusted_command_index_and_multipliers])
print(f'Adjusted results of the multiplications: {adjusted_multiplications_result}')
       


