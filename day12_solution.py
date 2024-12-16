import os
from pprint import pprint

cwd = os.getcwd()
input_file_name = "day12_input.txt"
input_file = cwd + "\\" + input_file_name

# function to find if an element exist in a list of lists
def find_element(list_of_lists, element):
    return [idx for idx, sublist in enumerate(list_of_lists) if element in sublist]

# open and read file
with open(input_file,'r') as file:
    input_file_content = file.read()
file.close()

# get rock into a list from file content.
input_lines = input_file_content.splitlines()

# get a grid (list of lists) from input lines.
grid = [[*line] for line in input_lines]

grid_row_count = len(grid)
grid_col_count = len(grid[0])

# loop over the grids and form am dictionary. Keys will be the plan type and values will be list of lists. Each sublist will be correspond to a region for that plant type.
# example: { "A": [[(125, 123), (126, 123)], [(113, 59), (114, 58), (114, 59)]], "B": [[(98, 53)], [(91, 40), (91, 41)]]}
all_plants_regions = {}
for r_idx, row in enumerate(grid):
    for c_idx, plant in enumerate(row):
        if plant not in all_plants_regions:
            all_plants_regions[plant] = [[(r_idx, c_idx)]]
        else:
            left_neighbour = (r_idx, c_idx - 1) if c_idx - 1 >= 0  and  grid[r_idx][c_idx - 1] == plant else None
            up_neighbour = (r_idx - 1, c_idx) if r_idx - 1 >= 0 and  grid[r_idx - 1][c_idx] == plant else None
            if left_neighbour is None and up_neighbour is None:
                all_plants_regions[plant].append([(r_idx, c_idx)])
            else:  
                if up_neighbour is not None:
                    neighbour_indexes = find_element(all_plants_regions[plant],up_neighbour)
                    for i in neighbour_indexes:
                        all_plants_regions[plant][i].append((r_idx, c_idx))
                if left_neighbour is not None:
                    neighbour_indexes = find_element(all_plants_regions[plant],left_neighbour)
                    for i in neighbour_indexes:
                        all_plants_regions[plant][i].append((r_idx, c_idx))
            plant_indexes = find_element(all_plants_regions[plant],(r_idx, c_idx))
            plant_indexes = sorted(plant_indexes, reverse=True)
            temp_set = set()
            [temp_set.update(set(all_plants_regions[plant].pop(idx))) for idx in plant_indexes]
            all_plants_regions[plant].append(list(temp_set))


# Part - 1: total fence price calculations.
# loop over all_plants_regions dictionary and calculate primeter and area for each reagion.
# calculate fencing price/cost for that region (area * perimeter) and add it to total fencing price.
total_price = 0
for plant_type, regions in all_plants_regions.items():
    for region in regions:
        region_area = len(region)
        region_perimeter =  len(region) * 4
        for row, col in region:
            neigbours = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            common_sides = len(set(region).intersection(neigbours))
            region_perimeter -= common_sides
        total_price += region_area * region_perimeter
print(f'Total price of fencing: {total_price}')


# Part - 2: total fence price calculations.
# loop over all_plants_regions dictionary and calculate primeter and area for each reagion.
# calculate fencing price/cost for that region (area * perimeter) and add it to total fencing price.
total_price = 0
for plant_type, regions in all_plants_regions.items():
    for region in regions:
        region_area = len(region)

        region.sort()
        region_perimeter =  0
        for row, col in region:
            left_neighbour = (row, col - 1)
            right_neighbour =  (row, col + 1)
            up_neighbour = (row - 1, col)
            down_neighbour = (row + 1, col)

            is_left_neighbour_exist = 1 if left_neighbour in region else 0   # 1
            is_right_neighbour_exist = 1 if right_neighbour in region else 0 # 0
            is_up_neighbour_exist = 1 if up_neighbour in region else 0       # 1
            is_down_neighbour_exist = 1 if down_neighbour in region else 0   # 0
    
            if is_up_neighbour_exist == 0 and is_left_neighbour_exist == 1:
                left_neighbour_up = (left_neighbour[0] - 1, left_neighbour[1])
                region_perimeter += 1 if left_neighbour_up in region else 0
            elif is_up_neighbour_exist == 0 and is_left_neighbour_exist == 0:
                region_perimeter += 1
        
            if is_down_neighbour_exist == 0 and is_left_neighbour_exist == 1:
                left_neighbour_down = (left_neighbour[0] + 1, left_neighbour[1])
                region_perimeter += 1 if left_neighbour_down in region else 0
            elif is_down_neighbour_exist == 0 and is_left_neighbour_exist == 0:
                region_perimeter += 1
                
            if is_left_neighbour_exist == 0 and is_up_neighbour_exist == 1:
                up_neighbour_left = (up_neighbour[0], up_neighbour[1] - 1)
                region_perimeter += 1 if up_neighbour_left in region else 0
            elif is_left_neighbour_exist == 0 and is_up_neighbour_exist == 0:
                region_perimeter += 1
    
            if is_right_neighbour_exist == 0 and is_up_neighbour_exist == 1:
                up_neighbour_right = (up_neighbour[0], up_neighbour[1] + 1)
                region_perimeter += 1 if up_neighbour_right in region else 0
            elif is_right_neighbour_exist == 0 and is_up_neighbour_exist == 0:
                region_perimeter += 1 
        total_price += region_area * region_perimeter
print(f'Total price of fencing: {total_price}')

