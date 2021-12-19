"""Day 1: Sonar Sweep.
Part 1: Find how many measurements in a list have a value higher than the
previous measurement."""

def find_num_increases(input_list):
    increased = 0
    for i in range(1, len(input_list)):
        if input_list[i]>input_list[i-1]:
            increased+=1
    return increased

"""Part 2: Count the number of times the sum of the measurements in a sliding
window of length 3 increases from the previous sum. Stop when there aren't
enough measurements to take a new window of three."""

def increases_in_sliding_win(input_list):
    increases = 0
    summed_list = []
    for i in range(len(input_list)):
        if i+3==len(input_list)+1:
            break
        summed_list.append(sum(input_list[i:i+3]))
    increased = find_num_increases(summed_list)
    return increased


with open('inputs/input_day_1.txt') as f:
    depth_file = f.read()
    depths = depth_file.splitlines()
    depths = [int(x) for x in depths]
    print(f"The answer to Part 1 is: {find_num_increases(depths)}.")
    print(f"The answer to Part 2 is: {increases_in_sliding_win(depths)}.")