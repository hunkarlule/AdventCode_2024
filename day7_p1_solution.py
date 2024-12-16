import itertools
import os
import sys
from pprint import pprint

# function to get permuations of n from a given list of values.
def generate_permutations(n):
    list_for_permutations = ["*", "+"]
    permutations = list(itertools.product(list_for_permutations, repeat=n))
    return permutations

# function to perform given operation on two given values.
def perform_operation(n1, n2, operand):
    if operand == "+":
        return n1 + n2
    else:
        return n1 * n2


cwd = os.getcwd()
input_file_name = "day7_input.txt"
input_file = cwd + "\\" + input_file_name

# open and read file
with open(input_file,'r') as file:
    input_lines = file.read().splitlines() 
file.close()

 # format the input lines to prcess
formatted_input = [line.split(":") for line in input_lines]
formatted_input = [(int(input[0]),[int(x) for x in input[1].strip().split(' ')]) for input in formatted_input]

all_test_values_with_correct_premutations = []

# for each line, get the all possible  operator permuatins and apply each premuation to the operand to check if they result in the target value.
for target, operands in formatted_input:
    correct_operator_premutations = []
    operands_length = len(operands)
    num_of_operators = len(operands) - 1
    possible_operation_premutations = generate_permutations(num_of_operators)
    possible_operation_premutations.sort(reverse=True)

    for index,prem in enumerate(possible_operation_premutations):
        temp_result = operands[0]
        operator_counter = 1

        for idx, op in enumerate(prem):
            temp_result = perform_operation(temp_result, operands[idx + 1], op)
            operator_counter += 1
            if temp_result > target:
                break
        if temp_result == target and operator_counter == operands_length:
            correct_operator_premutations.append(prem)
    all_test_values_with_correct_premutations.append((target,correct_operator_premutations))

print(f'Total calibration result: {sum([x[0] for x in all_test_values_with_correct_premutations if x[1]])}')

