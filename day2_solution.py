import os
import re

# function to check if a list safe or not.
def is_list_safe(int_list):
  return (all(num > 0 for num in int_list) or  
        all(num < 0 for num in int_list)) and all((abs(num) >=1  and abs(num) <=3)  for num in int_list)
           

cwd = os.getcwd()
input_file_name = "day2_input.txt"
input_file = cwd + "\\" + input_file_name
     
# read file
with open(input_file,'r') as file:
    input_lines = file.read().splitlines() 
file.close()

# split each line by spaces into a string list  
reports_list =  [re.split(r'\s+', line) for line in input_lines]

# converts string lists of list  into int lists of list.
reports_list = [[int(str) for str in sublist] for sublist in reports_list]

# get a difference between each adjacent elements in each sublist.
difference_list  = [[sublist[i+1] - sublist[i] for i in range(len(sublist)-1)] for sublist in reports_list]

# find the number of safe list using 'is_list_safe' function.
safe_reports = [sublist for sublist in difference_list if  is_list_safe(sublist)]

# part-one result    
print(f"Safe report count: {len(safe_reports)}.")

# part two
# filter unsafe reports.
unsafe_reports = [item for item in difference_list if item not in safe_reports]
#print(len(unsafe_reports))

adjusted_safe_report_count = len(safe_reports)

# from each unsafe reports remove the elements one by one and check if the list becomes safe
# if so increment adjusted_safe_report_count by one and continue with next unsafe report.
for report in unsafe_reports:
    if is_list_safe(report[1:]) or is_list_safe(report[:-1]):
        adjusted_safe_report_count +=  1
        continue
    for idx, val in enumerate(report[1:-1], start=1):
        temp_list1 = report[:]
        temp_list2 = report[:]
        temp_list1[idx - 1] =  temp_list1[idx - 1] + val
        temp_list1.pop(idx)

        if is_list_safe(temp_list1):
           adjusted_safe_report_count += 1 
           break
        temp_list2[idx + 1] =  temp_list2[idx + 1] + val
        temp_list2.pop(idx)
        if is_list_safe(temp_list2):
            adjusted_safe_report_count += 1 
            break
        
print(f"Adjusted safe report count: {adjusted_safe_report_count}.")
    


       



