import os
from pprint import pprint

cwd = os.getcwd()
input_file_name = "day9_input.txt"
input_file = cwd + "\\" + input_file_name

# open and read file
with open(input_file,'r') as file:
    input_file_content = file.read()
file.close()

input = [ int(char)for char in input_file_content]
# input = [2,3,3,3,1,3,3,1,2,1,4,1,4,1,3,1,4,0,2]
total_blocks = sum(input)
mapped_disk_block = [ val * [idx // 2] if idx % 2 == 0  else val * ['.'] for idx, val in enumerate(input)]

isFinished = False

counter = 0
for file_block_idx in reversed(range(0,len(mapped_disk_block), 2)):
    counter += 1
    if isFinished:
        break

    file_block = mapped_disk_block[file_block_idx]

    file_block_value = file_block[0]
    remaining_file_block_len = len(file_block)

    if not file_block:
        continue

    while True:
        empty_block_idx, empty_block  = next(((idx, b) for idx, b in enumerate(mapped_disk_block) if "."  in b), (None, None))
        if empty_block_idx >= file_block_idx or  empty_block_idx is None:
            isFinished = True
            break
        empty_location_len = empty_block.count(".")
        first_empty_location_index = empty_block.index(".")

        if empty_location_len >= remaining_file_block_len:
            mapped_disk_block[empty_block_idx][first_empty_location_index: remaining_file_block_len + first_empty_location_index] = [file_block_value] * remaining_file_block_len
            mapped_disk_block[file_block_idx]  = ["."] * remaining_file_block_len
            remaining_file_block_len = 0
            break
        else:
            mapped_disk_block[empty_block_idx][first_empty_location_index:] = [file_block_value] * empty_location_len
            remaining_file_block_len -= empty_location_len


flatten_mapped_disk_block = [item for sublist in mapped_disk_block for item in sublist]
result =  sum(idx * val for idx, val in enumerate(flatten_mapped_disk_block) if val != '.')
print(f"Resulting filesystem checksum: {result}")
