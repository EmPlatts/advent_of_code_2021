"""Day 2: Dive!
Part 1: The submarine takes a series of commands:
    - 'forward X' increases the horizontal position by X units.
    - 'down X' increases the depth by X units.
    - 'up X' decreases the depth by X units.
The submarine already has a planned course, so you need to figure out where it
is going.
Your horizontal and depth both start at 0.
Calculate the horizontal position and depth for the planned course.
What is the final horizontal position multiplied by the depth?
"""

def find_sub_position(course):
    coords = [0, 0] # (horizontal, depth)
    for move in course:
        value = int(''.join(filter(str.isdigit, move)))
        if 'forward' in move:
            coords[0] += value
        elif 'up' in move:
            coords[1] -= value
        elif 'down' in move:
            coords[1] += value
        else:
            raise ValueError("Direction not recognised! Must contain 'up', "
                            "'down' or 'forward'.")
    return coords[0]*coords[1]

"""Part 2: In addition to horizontal position and depth, you also need to
track the aim, which also starts at 0. The commands also mean something
entirely different to what you first thought.
    - 'down X' increases aim by X units.
    - 'up X' decreases aim by X units.
    - 'forward X' does two things:
            * it increases your horiztontal position by X units.
            * it increases your depth by your aim multiplied by X.
Return the product of the final horizontal position and depth.
"""

def find_actual_sub_position(course):
    coords = [0, 0, 0] # (horizontal, depth, aim)
    for move in course:
        value = int(''.join(filter(str.isdigit, move)))
        if 'up' in move:
            coords[2] -= value
        elif 'down' in move:
            coords[2] += value
        elif 'forward' in move:
            coords[0] += value
            coords[1] += coords[2]*value
        else:
            raise ValueError("Direction not recognised! Must contain 'up', "
                            "'down' or 'forward'.")
    return coords[0]*coords[1]

  
with open('inputs/input_day_2.txt') as f:
    course_file = f.read()
    sub_course = course_file.splitlines()
    print(f"The answer to Part 1 is: {find_sub_position(sub_course)}.")
    print(f"The answer to Part 2 is: {find_actual_sub_position(sub_course)}.")