"""Day 5: Hydrothermal Venture.
Part 1: Find the dangerous areas in the map -- these are defined as areas
where verticle or horizontal lines from vents touch at least two times.
"""
import itertools

def get_vents_crossed(vents):
    """Get the number of points that are overlapped by the vents at least
    twice.
    Args:
        vents (list): A list of lists of integers describing the vent
            locations.
    Returns:
        num_dangerous (int): Number of points which have at least two vents.
    """
    vent_points = list(itertools.chain.from_iterable(vents))
    x_coords = [x[0] for x in vent_points]
    y_coords = [x[1] for x in vent_points]
    vent_area = [[0]*(max(x_coords)+1) for x in range(max(y_coords)+1)]
    for vent in vents:
        if vent[0][0]==vent[1][0]:
            x_val = vent[0][0]
            y_vals = [vent[0][1], vent[1][1]]
            y_range = range(min(y_vals), max(y_vals)+1)
            all_points = [(x_val, y_val) for y_val in y_range]
            for x,y in all_points:
                vent_area[y][x] += 1
        if vent[0][1]==vent[1][1]:
            y_val = vent[0][1]
            x_vals = [vent[0][0], vent[1][0]]
            x_range = range(min(x_vals), max(x_vals)+1)
            all_points = [(x_val, y_val) for x_val in x_range]
            for x,y in all_points:
                vent_area[y][x] += 1
    counter = []
    for vent_row in vent_area:
        counter.append([vent_pt for vent_pt in vent_row if vent_pt>1])
    num_dangerous = len([item for sublist in counter for item in sublist])
    return num_dangerous

"""Part 2: Oh no, the lines can also be at 45 degrees! We'll need to check
how many points are crossed by vents at 45 degrees, too, i.e. have a
gradient of 1.
"""

def get_actual_vents_crossed(vents):
    """Get the number of points that are overlapped by the vents at least
    twice.
    Args:
        vents (list): A list of lists of integers describing the vent
            locations.
    Returns:
        num_dangerous (int): Number of points which have at least two vents.
    """
    vent_points = list(itertools.chain.from_iterable(vents))
    x_coords = [x[0] for x in vent_points]
    y_coords = [x[1] for x in vent_points]
    vent_area = [[0]*(max(x_coords)+1) for x in range(max(y_coords)+1)]
    for vent in vents:
        if vent[0][0]==vent[1][0]:
            x_val = vent[0][0]
            y_vals = [vent[0][1], vent[1][1]]
            y_range = range(min(y_vals), max(y_vals)+1)
            all_points = [(x_val, y_val) for y_val in y_range]
            for x,y in all_points:
                vent_area[y][x] += 1
        elif vent[0][1]==vent[1][1]:
            y_val = vent[0][1]
            x_vals = [vent[0][0], vent[1][0]]
            x_range = range(min(x_vals), max(x_vals)+1)
            all_points = [(x_val, y_val) for x_val in x_range]
            for x,y in all_points:
                vent_area[y][x] += 1
        elif (vent[0][0]-vent[1][0])/(vent[0][1]-vent[1][1])==1:
            if vent[0][0]>vent[1][0]:
                x_vals = list(range(vent[0][0], vent[1][0]-1, -1))
                y_vals = list(range(vent[0][1], vent[1][1]-1, -1))
            else:
                x_vals = list(range(vent[0][0], vent[1][0]+1))
                y_vals = list(range(vent[0][1], vent[1][1]+1))
            for x,y in zip(x_vals, y_vals):
                vent_area[y][x] += 1
        elif  (vent[0][0]-vent[1][0])/(vent[0][1]-vent[1][1])==-1:
            if vent[0][0]>vent[1][0]:
                x_vals = list(range(vent[0][0], vent[1][0]-1, -1))
                y_vals = list(range(vent[0][1], vent[1][1]+1))
            else:
                x_vals = list(range(vent[0][0], vent[1][0]+1))
                y_vals = list(range(vent[0][1], vent[1][1]-1, -1))
            for x,y in zip(x_vals, y_vals):
                vent_area[y][x] += 1
    counter = []
    for vent_row in vent_area:
        counter.append([vent_pt for vent_pt in vent_row if vent_pt>1])
    num_dangerous = len([item for sublist in counter for item in sublist])
    return num_dangerous

with open('inputs/input_day_5.txt') as f:
    vents_file = f.read()
    vents_file = vents_file.splitlines()
    vents = [s.replace(' -> ', ',').split(',') for s in vents_file]
    vents = [[int(x) for x in s] for s in vents]
    vents = [[vent[0:2], vent[2:4]] for vent in vents]
    print(f'The answer to Part 1 is: {get_vents_crossed(vents)}.')
    print(f'The answer to Part 2 is: {get_actual_vents_crossed(vents)}.')