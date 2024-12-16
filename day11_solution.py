
import os
from pprint import pprint

cwd = os.getcwd()
input_file_name = "day11_input.txt"
input_file = cwd + "\\" + input_file_name

# open and read file
with open(input_file,'r') as file:
    input_file_content = file.read().strip()
file.close()

# get rock into a list from file content.
input_lines = input_file_content.splitlines()
rocks = input_lines[0].split(" ")
rocks = [rock for rock in rocks]

# generate a dictionary. keys will be the stones and values will be the count(number) of each stone.
# it will produce something like this: {'4022724': 1, '951333': 1, '0': 1, '21633': 1, '5857': 1, '97': 1, '702': 1, '6': 1}
rocks_grouped_by_count = {rock: rocks.count(rock)for rock in rocks}
# print(rocks_grouped_by_count)

#for part-1 set this value to 25 and for part-2 set this value to 75
blinking_number = 25 

# loop over n(blinking_number) times
for i in range(blinking_number):
    new_rocks_grouped_by_count = {}
    # loop over dictionary items and add new keys wtih their count a new dictionary.
    for rock, rock_count in rocks_grouped_by_count.items():
        if rock == "0":
            if "1" in new_rocks_grouped_by_count:
                new_rocks_grouped_by_count["1"] = new_rocks_grouped_by_count["1"] + rock_count
            else:
                new_rocks_grouped_by_count["1"] = rock_count
        elif len(rock) % 2 == 0:
            rock_length = len(rock)
            first_part = str(int(rock[0:rock_length // 2]))
            second_part = str(int(rock[rock_length // 2:]))
            if first_part in new_rocks_grouped_by_count:
                new_rocks_grouped_by_count[first_part] = new_rocks_grouped_by_count[first_part] + rock_count
            else:
                new_rocks_grouped_by_count[first_part] = rock_count
            if second_part in new_rocks_grouped_by_count:
                new_rocks_grouped_by_count[second_part] = new_rocks_grouped_by_count[second_part] + rock_count
            else:
                new_rocks_grouped_by_count[second_part] = rock_count
        else:
            new_rock = str(int(rock) * 2024)
            if new_rock in new_rocks_grouped_by_count:
                new_rocks_grouped_by_count[new_rock] = new_rocks_grouped_by_count[new_rock] + rock_count
            else:
                new_rocks_grouped_by_count[new_rock] = rock_count

    # assign the new created dictionary to  orginal dictionary. So, it will be the state of stones before the next blinking.
    rocks_grouped_by_count = new_rocks_grouped_by_count

# get sum of values from dictionary
rock_count = sum(item for item in rocks_grouped_by_count.values())
print(f"Stone count after blinking {blinking_number} times: {rock_count}")

