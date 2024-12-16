import itertools
import os
import sys
from pprint import pprint

# function to return all postions of a given element in a list of lists.
def find_element_positions(element):
    element_positions = []
    for row_idx, row in enumerate(grid):
        start = 0
        for _ in range(row.count(element)):
            col = row.index(element,start)
            element_positions.append((row_idx, col))
            start = col
    return element_positions

# function to create list of pairs from a list: ex: list = [1,2,3] ==> result = [[1,2], [1,3], [2,3]]
def create_pairs_from_list(input_list):
    result = []
    for i, ival in enumerate(input_list):
        for j, jval in  enumerate(input_list[i + 1:]): 
            result.append([ival, jval])
    return result

cwd = os.getcwd()
input_file_name = "day8_input.txt"
input_file = cwd + "\\" + input_file_name

# open and read file
with open(input_file,'r') as file:
    input_file_content = file.read()
file.close()

input_lines = input_file_content.splitlines()

# get a grid (list of lists) from input lines.
grid = [[*line] for line in input_lines]


grid_row_count = len(grid)
grid_col_count = len(grid[0])

# get unique antenna types
antenna_types = list(set(input_file_content))
antenna_types.remove(".")
antenna_types.remove("\n")



# for ach antena type get its postions in the grid.
antennas_and_postitions = {}
for antenna in antenna_types:
   antenna_postitions = find_element_positions(antenna)
   antennas_and_postitions[antenna] = antenna_postitions

# for each antenna type create antenna pairs and calculate positions for antinodes for each pair.
antennas_and_antinode_postitions = {}
for antenna, postitions in antennas_and_postitions.items():
    antenna_pairs = create_pairs_from_list(postitions)
    antinode_positions = []
    for pair in antenna_pairs:
        a1 = pair[0]
        a2 = pair[1]
        row_diff  = a2[0] - a1[0]
        col_diff  = a2[1] - a1[1]

        antinode1 = (a1[0] - row_diff, a1[1] - col_diff)
        antinode2 = (a2[0] + row_diff , a2[1] + col_diff)
        if antinode1[0] >= 0 and  antinode1[0] < grid_row_count and  antinode1[1] >= 0 and  antinode1[1] < grid_col_count:
            antinode_positions.append(antinode1)
        if antinode2[0] >= 0 and  antinode2[0] < grid_row_count and  antinode2[1] >= 0 and  antinode2[1] < grid_col_count:
            antinode_positions.append(antinode2)
    antennas_and_antinode_postitions[antenna] = antinode_positions

# add all antinode postions from all antennas to a list
all_antenna_positions = []
[all_antenna_positions.extend(val) for val in antennas_and_antinode_postitions.values()]

# remove duplicate antinode postitions
all_antenna_positions = list(set(all_antenna_positions))

print(f'Unique locations count for antinodes: {len(all_antenna_positions)}')


