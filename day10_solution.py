import os
from pprint import pprint

cwd = os.getcwd()
input_file_name = "day10_input.txt"
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


# get trail start points (points with value "0")
trail_start_points =  [(i, j) for i, sublist in enumerate(grid) for j, val in enumerate(sublist) if val == "0"]

# create an all paths dictionary. Key will be strating point and value will be list of lists.
all_paths = {start_point: [[start_point]] for start_point in trail_start_points}
all_path_keys  = list(all_paths.keys())

# loop 9 steps because ecah trail need to gO 0-1-2-3-4-5-6-7-8-9 if possible.
for i in range(9):
    # loop over all_paths dictionary.
    for key in all_path_keys:  
        current_paths = all_paths[key] # get all paths for the key
        # print(current_paths)
        new_paths = []

        # loop over paths for a key.
        # each path is possible to branch/produce to 4 paths
        for path_idx, path in enumerate(current_paths):
            # get last point on the path and find north, south, east and points and check if they qualify to be on the path.
            path_last_point = path[-1] 
            north_p = (path_last_point[0] - 1, path_last_point[1]) if path_last_point[0] - 1 >= 0 and grid[path_last_point[0] - 1][path_last_point[1]] == str(i + 1) else None
            south_p = (path_last_point[0] + 1, path_last_point[1]) if path_last_point[0] + 1 < grid_row_count and grid[path_last_point[0] + 1][path_last_point[1]] == str(i + 1)  else None
            west_p = (path_last_point[0], path_last_point[1] - 1) if  path_last_point[1] - 1 >= 0 and grid[path_last_point[0]][path_last_point[1] - 1] == str(i + 1) else None
            east_p = (path_last_point[0], path_last_point[1] + 1) if  path_last_point[1] + 1 < grid_col_count and grid[path_last_point[0]][path_last_point[1] + 1] == str(i + 1) else None            
            new_possible_paths = [path + [p] for p in [north_p, south_p, west_p, east_p] if p is not None]
            new_paths.extend(new_possible_paths)
        #replace the paths for the key with new calculated paths.
        all_paths[key] = new_paths

# calculate the sum of score.
# trailhead's score is the number of 9-height positions reachable from a start-point(0)
sum_of_scores = 0
for key in all_path_keys:
    # remove duplicates. 
    # for a starting points, if two trails ends with the same end-point(9) then eliminate one of them.
    sum_of_scores += len(set([sublist[-1] for sublist in all_paths[key]]))
print(sum_of_scores)
print(f"Sum_of_scores: {sum_of_scores}")

# part - two
# A trailhead's score is the number of distinct hiking trails which begin at a start-point(0)
# So, in part two we do not need to eliminate the trails that end with the same end-point(9). We count all of them.
sum_of_scores = 0
for key in all_path_keys:
    sum_of_scores += len(all_paths[key])
print(f"Sum_of_scores: {sum_of_scores}")