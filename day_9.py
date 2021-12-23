"""Day 9: Smoke Basin.
Part 1: on a grid, determine all the low points, i.e. points that are lower
than all their surrounding points. They are assigned a risk level of 1 plus
their height. Find the sum of all the risks for all the low points. 
"""

def make_grid(grid):
    """Put grid in readable format."""
    grid = [list(x) for x in grid]
    grid = [[int(e) for e in x] for x in grid]
    return grid

def pad_grid(grid):
    """Add padding of 10s around grid to make it easy to find low points."""
    grid.insert(0, [10]*len(grid[0]))
    grid.append([10]*len(grid[0]))
    [grid[i].insert(0,10) for i in range(len(grid))]
    [grid[i].append(10) for i in range(len(grid))]
    return grid

def get_risk_score(grid):
    """To do this, we'll simply add a buffer of 10s around our grid, and then
    find all points which are smaller than the 4 points around them.
    """
    grid = make_grid(grid)
    grid = pad_grid(grid)
    low_pts = []
    for i in range(1, len(grid[0])-1):
        for j in range(1, len(grid)-1):
            if ((grid[j][i] < grid[j-1][i]) and (grid[j][i] < grid[j+1][i]) and
            (grid[j][i] < grid[j][i-1]) and (grid[j][i] < grid[j][i+1])):
                low_pts.append(grid[j][i])
    risk_score = sum([x+1 for x in low_pts])
    return risk_score

"""Part 2: Now we want to find the size of the basins, i.e. any point 
surrounding the sink that is less than 9 (or 10, in our buffered version).
Find the three biggest basins and return their sizes (number of grid points)
multiplied together.

This looks like a job for the flood-fill algorithm.
"""

from functools import reduce

def transform_grid(grid):
    """Make grid 0s and 1s."""
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid)):
            if grid[j][i]>=9:
                grid[j][i] = 1
            else:
                grid[j][i] = 0
    return grid

def get_basin_size(grid):
    """Get coords (x, y) -- the lowest points -- then find the size of
    the basin using a recursive depth-first search."""
    def flood_fill(grid, x, y, empty_space, filled_space):
        """Recursive function to fill the basins."""
        grid_height = len(grid)
        grid_width = len(grid[0])
        if grid[x][y]!=empty_space: #if not empty, break out of function
            return
        grid[x][y] = filled_space
        n_pts = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] #neighbouring points
        for pt in n_pts:
            if (0 < pt[0] <= grid_height-1) and (0 < pt[1] <= grid_width-1):
                flood_fill(grid, pt[0], pt[1], empty_space, filled_space)
        return grid
    # Neaten and pad grid
    grid = make_grid(grid)
    grid = pad_grid(grid)
    # Get coords of low points
    coords = []
    for i in range(1, len(grid[0])-1):
        for j in range(1, len(grid)-1):
            if ((grid[j][i] < grid[j-1][i]) and (grid[j][i] < grid[j+1][i]) and
            (grid[j][i] < grid[j][i-1]) and (grid[j][i] < grid[j][i+1])):
                coords.append((i, j))
    # Simplify grid to 0s and 1s
    grid = transform_grid(grid)
    basin_sizes = []
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid)):
            if (i,j) in coords:
                grid = flood_fill(grid, j, i, 0, 2)
                count = len([item for sublist in grid for item in sublist if item==2])
                basin_sizes.append(count)
    # Sort basins by size and keep top 3
    basin_sizes = sorted([basin_sizes[0]]+
                         [b - a for a, b in zip(basin_sizes, basin_sizes[1:])],
                         reverse=True)[:3]
    basin_score = reduce((lambda a, b: a*b), basin_sizes)
    return basin_score


with open('inputs/input_day_9.txt') as f:
    grid_file = f.read()
    grid = grid_file.splitlines()
    print(f'The answer to Part 1 is {get_risk_score(grid)}.')
    print(f'The answer to Part 2 is {get_basin_size(grid)}.')