import os
from pprint import pprint
import sys

# function to find visited postions from a start point to a obstruction or until exit from the grid.
def walk_grid(start_row, start_col, direction, grid_row_count, grid_col_count, grid):
    traveled_postions = [(start_row, start_col)]
    current_row = start_row
    current_col = start_col
    is_exit_found = False
    finish_direction = None
    if direction == "north":
        while current_row - 1 >= 0 and grid[current_row - 1][current_col] != "#":
             current_row = current_row - 1
             traveled_postions.append((current_row, current_col))
        finish_direction , is_exit_found = (direction, True) if current_row - 1 < 0 else ("east", False)
    if direction == "east":
        while current_col + 1 < grid_col_count and grid[current_row][current_col + 1] != "#":
             current_col = current_col + 1
             traveled_postions.append((current_row, current_col))
        finish_direction , is_exit_found = (direction, True) if current_col + 1 >= grid_col_count else ("south", False)
    if direction == "south":
        while current_row + 1 < grid_row_count and grid[current_row + 1][current_col] != "#":
             current_row = current_row + 1
             traveled_postions.append((current_row, current_col))
        finish_direction , is_exit_found = (direction, True) if current_row + 1 >= grid_row_count else ("west", False)  
    if direction == "west":
        while current_col - 1 >= 0 and grid[current_row][current_col - 1] != "#":
             current_col = current_col - 1
             traveled_postions.append((current_row, current_col))
        finish_direction , is_exit_found = (direction, True) if current_col - 1 < 0 else ("north", False)
    return current_row, current_col, traveled_postions, finish_direction, is_exit_found

cwd = os.getcwd()
input_file_name = "day6_input.txt"
input_file = cwd + "\\" + input_file_name

# open and read file
with open(input_file,'r') as file:
    input_lines = file.read().splitlines() 
file.close()

# get a grid (list of lists) from input lines.
grid = [[*line] for line in input_lines]

num_of_rows = len(input_lines)
num_of_columns = len(input_lines[0])

# find guard's stating position.
starting_row, starting_col  = next((idx, sublist.index("^")) for idx,sublist in enumerate(grid) if "^" in sublist)
all_traveled_positions = []
traveled_positions = []
is_travel_completed =  False
travel_direction = "north"

# until travel is completed(until gurads is out of grid)m, call the walk_grid function and add visitied positions into a list
while not is_travel_completed:
    starting_row, starting_col, traveled_positions, travel_direction, is_travel_completed = walk_grid(starting_row, starting_col, travel_direction, num_of_rows, num_of_columns, grid)
    all_traveled_positions.extend(traveled_positions)

# filter visited positions and remove duplicates.
filtered_all_traveled_postions = list(set(all_traveled_positions))

# print result.
print(f'Distinct positions will the guard will visit:  {len(filtered_all_traveled_postions)}')