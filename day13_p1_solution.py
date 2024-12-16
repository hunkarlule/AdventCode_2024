
import os
from pprint import pprint

cwd = os.getcwd()
input_file_name = "day13_input.txt"
input_file = cwd + "\\" + input_file_name

# open and read file
with open(input_file,'r') as file:
    input_file_content = file.read()
file.close()

buttons_and_prizes = input_file_content.split("\n\n")
# for line in buttons_and_prizes:
#     print(line)
#     print("Next Line")

buttons_and_prizes = [ config.split("\n") for config in buttons_and_prizes]
# print(buttons_and_prizes)

buttonA_token_cost = 3
buttonB_token_cost = 1
button_counts_for_prizes = []

for config in buttons_and_prizes:
    config = [ c.split(",") for c in config]
    # print(config)

    prize_X = int(config[2][0].split("=")[1])
    prize_Y = int(config[2][1].split("=")[1])

    buttonA_count = 0
    buttonB_count = 0

    buttonA_X = int(config[0][0].split("+")[1])
    buttonA_Y = int(config[0][1].split("+")[1])

    buttonB_X = int(config[1][0].split("+")[1])
    buttonB_Y = int(config[1][1].split("+")[1])

    remaining_X_to_prize = prize_X
    remaining_Y_to_prize = prize_Y

    while True:
        if remaining_X_to_prize % buttonA_X == 0 and remaining_Y_to_prize % buttonA_Y == 0 and remaining_X_to_prize // buttonA_X == remaining_Y_to_prize // buttonA_Y:
            buttonA_count = remaining_X_to_prize // buttonA_X
            break
        else:
            buttonB_count += 1
            remaining_X_to_prize -= buttonB_X
            remaining_Y_to_prize -= buttonB_Y
        if (remaining_X_to_prize < buttonA_X and remaining_X_to_prize > 0) or  (remaining_X_to_prize < 0) or (remaining_Y_to_prize < buttonA_Y and remaining_Y_to_prize > 0) or  (remaining_Y_to_prize < 0) or buttonB_count > 100:
                buttonA_count = None
                buttonB_count = None
                break
    if (buttonA_count is not None and buttonA_count > 100) or (buttonB_count is not None and buttonB_count > 100):
        buttonA_count = None
        buttonB_count = None         
    button_counts_for_prizes.append((buttonA_count,buttonB_count))

#calculate cost
total_cost = sum( (c[0] * buttonA_token_cost) + (c[1] * buttonB_token_cost) for c in button_counts_for_prizes if c[0] is not None and c[1] is not None)
print(f'Total token cost: {total_cost}')