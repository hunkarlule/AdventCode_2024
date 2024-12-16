import os
from pprint import pprint
import sys

def create_pairs_from_list(input_list):
    result = []
    for i, ival in enumerate(input_list):
        for j, jval in  enumerate(input_list[i + 1:]): 
            result.append([ival, jval])
    return result

cwd = os.getcwd()
input_file_name = "day5_input.txt"
input_file = cwd + "\\" + input_file_name

# open and read file
with open(input_file,'r') as file:
    contents = file.read()
    #get the content of files into two strings
    page_ordering_rules_str, pages_to_print_str = contents.split('\n\n')

file.close()

# pager ordering rules string into a list of lists
page_ordering_rules = [line.split("|") for line in page_ordering_rules_str.splitlines()]

# pages_to print string to string array
pages_to_print = pages_to_print_str.splitlines()

# convert pages_to_print string list to list of lists
page_lists = [pages.split(",") for pages in pages_to_print]

right_page_lists = []
wrong_page_lists = []
for page_list in page_lists:
    page_pairs = create_pairs_from_list(page_list)
    if all([element in page_ordering_rules for element in page_pairs]):
        right_page_lists.append(page_list)
    else:
        wrong_page_lists.append(page_list)

middle_page_numbers = [int(update[len(update) // 2]) for update in right_page_lists]
print(f"Sum of middle page numbers: {sum(middle_page_numbers)}")


# part two
corrected_middle_page_numbers = []
for the_list in wrong_page_lists: 
    pairs_list = create_pairs_from_list(the_list)
    for idx, pair in enumerate(pairs_list):
        if pair not in page_ordering_rules:
            pair[0], pair[1] = pair[1], pair[0] 
            pairs_list[idx] = pair
    modified = [ pair[1] for pair in pairs_list]
    corrected_page_list_pairs_count = sorted([[l, modified.count(l) ]for l in the_list], key=lambda x: x[-1])
    corrected_page_list = [o[0] for o in corrected_page_list_pairs_count]
    corrected_middle_page_numbers.append(int(corrected_page_list[len(corrected_page_list) // 2]))
print(f"Sum of middle page numbers after correction: {sum(corrected_middle_page_numbers)}")


